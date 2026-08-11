"""Build the CA-math sqlite store from the adopted Learning Commons JSONL export.

Reads the five populated ``data/ca-math/*.jsonl`` files (``misconceptions.jsonl`` is empty
by design — no misconception data exists in the public export) and maps them into the four
store tables defined by :class:`~k12_toolkit.repository.SqliteStandardsRepository`.

The transformation (:func:`build_rows`) is a **pure function** of the source directory —
connection-free and fully unit-testable. :func:`ingest_into_connection` and
:func:`build_database` are the thin sqlite drivers on top of it.

Field mapping is pinned by ``docs/reference/lc-export-schema.md`` §6. Key decisions made here
(documented for the record):

- **grade** — ``properties.gradeLevel`` is a JSON-encoded array string. A single grade renders
  verbatim (``"6"``, ``"K"``); a contiguous integer run collapses to ``"min-max"``
  (``["9","10","11","12"]`` -> ``"9-12"``); anything else is comma-joined; empty/absent -> NULL.
- **Progression direction** — the store's ``progression(uuid, direction)`` returns the ``to_uuid``
  of the first row whose ``from_uuid == uuid`` and ``direction`` matches. So to make
  ``progression(later, "backward")`` yield ``prereq`` we insert ``(from=later, to=prereq,
  backward)``, and for ``progression(prereq, "forward")`` we insert ``(from=prereq, to=later,
  forward)``. ``buildsTowards`` has ``source = prereq``, ``target = later``.
- **Primary edge selection** — ``buildsTowards`` carries no priority ranking, so when a node has
  several prerequisites/next-standards the primary is the one with the lowest node identifier
  (deterministic and stable across rebuilds). The store returns a single primary anyway.
- **California bridge** — CA standards carry no ``buildsTowards`` (all 757 endpoints are
  Multi-State CCSS). A CA standard C reaches the progression graph via the crosswalk
  ``C --hasStandardAlignment--> E`` (highest ``jaccard`` first): backward-of(C) = prereq-of(E),
  forward-of(C) = forward-of(E). If the chosen CCSS neighbour has exactly one CA standard that
  crosswalks to it (a clean reverse crosswalk) we return that CA equivalent; otherwise the CCSS
  neighbour verbatim. These rows are tagged ``source = SOURCE_BRIDGED``.
- **relatesTo** — non-sequential related edges have no home in the model (``Progression`` is only
  backward/forward, and there is no related-edge table). They are skipped and counted, never
  mapped onto backward/forward.
"""

from __future__ import annotations

import html
import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from k12_toolkit.repository import SqliteStandardsRepository

# Attribution stamps (spec §5).
SOURCE = "Learning Commons KG v1.11.0"
SOURCE_BRIDGED = "Learning Commons KG v1.11.0 (via CA->CCSS crosswalk)"

_MULTI_STATE = "Multi-State"
_CALIFORNIA = "California"

# LaTeX ($...$) is part of the standard text and must survive verbatim; real HTML tags must be
# stripped. A tag starts with a letter (or /letter), which never matches a math inequality like
# "x < c" or "a > 1" (space / digit after the angle bracket).
_LATEX_RE = re.compile(r"\$[^$]*\$")
_HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")
_PLACEHOLDER_RE = re.compile("\x00(\\d+)\x00")

StdRow = tuple[str, str, str, str, str, str | None, str | None, str, str]
ProgRow = tuple[str, str, str, str]
CompRow = tuple[str, int, str, str]


@dataclass(frozen=True)
class IngestStats:
    """Row counts + data-quality signals from one ingest, for reporting."""

    standards: int
    progressions_backward: int
    progressions_forward: int
    learning_components: int
    standards_without_code: int
    progressions_direct: int
    progressions_bridged: int
    relatesto_skipped: int
    component_edges_orphaned: int
    component_edges_missing_standard: int
    html_texts_stripped: int
    non_multistate_buildstowards_endpoints: int
    bridge_self_loops_avoided: int
    multi_parent_children: int
    # Curriculum layer. Defaulted, so an export predating scripts/extract_curriculum.py
    # still builds; zeros here mean "no curriculum files present", which the CLI prints.
    curriculum_lessons: int = 0
    curriculum_alignments: int = 0
    curriculum_materials: int = 0


@dataclass(frozen=True)
class BuiltRows:
    """The transformed rows ready for insertion, plus the ingest stats."""

    standards: list[StdRow]
    progressions: list[ProgRow]
    components: list[CompRow]
    stats: IngestStats


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def _strip_html(text: str) -> str:
    """Remove real HTML tags while preserving LaTeX ``$...$`` spans verbatim."""
    spans: list[str] = []

    def _stash(match: re.Match[str]) -> str:
        spans.append(match.group(0))
        return f"\x00{len(spans) - 1}\x00"

    protected = _LATEX_RE.sub(_stash, text)
    protected = _HTML_TAG_RE.sub("", protected)
    protected = html.unescape(protected)

    def _restore(match: re.Match[str]) -> str:
        return spans[int(match.group(1))]

    return _PLACEHOLDER_RE.sub(_restore, protected)


def _encode_grade(raw: str | None) -> str | None:
    """Compact a JSON-encoded grade array: single verbatim, contiguous run -> ``min-max``."""
    if not raw:
        return None
    try:
        values = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None
    tokens = [str(v) for v in values]
    if not tokens:
        return None
    if len(tokens) == 1:
        return tokens[0]
    if all(t.isdigit() for t in tokens):
        nums = [int(t) for t in tokens]
        if nums == sorted(nums) and nums == list(range(nums[0], nums[0] + len(nums))):
            return f"{nums[0]}-{nums[-1]}"
    return ",".join(tokens)


def build_rows(source_dir: str | Path) -> BuiltRows:
    """Transform the CA-math JSONL export at ``source_dir`` into store rows (pure function)."""
    src = Path(source_dir)
    standards = _read_jsonl(src / "standards.jsonl")
    hierarchy = _read_jsonl(src / "hierarchy.jsonl")
    progressions = _read_jsonl(src / "progressions.jsonl")
    crosswalk = _read_jsonl(src / "crosswalk.jsonl")
    components = _read_jsonl(src / "components.jsonl")

    # --- hierarchy: child -> parent (a node's parent = the hasChild source) ---
    parent_of: dict[str, str] = {}
    multi_parent = 0
    for edge in hierarchy:
        if edge.get("label") != "hasChild":
            continue
        child = edge["target_identifier"]
        parent = edge["source_identifier"]
        if child in parent_of and parent_of[child] != parent:
            multi_parent += 1
        parent_of[child] = parent

    # --- standards ---
    std_rows: list[StdRow] = []
    std_ids: set[str] = set()
    jurisdiction_of: dict[str, str] = {}
    without_code = 0
    html_stripped = 0
    for node in standards:
        props = node["properties"]
        uid: str = node["identifier"]
        std_ids.add(uid)
        jur = props.get("jurisdiction", "")
        jurisdiction_of[uid] = jur
        code = props.get("statementCode") or props.get("alternateStatementCode") or ""
        if not code:
            without_code += 1
        raw_desc = props.get("description", "")
        text = _strip_html(raw_desc)
        if text != raw_desc:
            html_stripped += 1
        std_rows.append(
            (
                uid,
                code,
                text,
                props.get("academicSubject", ""),
                jur,
                _encode_grade(props.get("gradeLevel")),
                parent_of.get(uid),
                SOURCE,
                props.get("license", ""),
            )
        )

    # --- progression indices from buildsTowards (source = prereq, target = later) ---
    builds_towards = [r for r in progressions if r.get("label") == "buildsTowards"]
    relatesto_skipped = sum(1 for r in progressions if r.get("label") == "relatesTo")
    prereqs_of: dict[str, list[str]] = defaultdict(list)  # later -> [prereq, ...]
    forwards_of: dict[str, list[str]] = defaultdict(list)  # prereq -> [later, ...]
    non_ms_endpoints = 0
    for rel in builds_towards:
        later = rel["target_identifier"]
        prereq = rel["source_identifier"]
        prereqs_of[later].append(prereq)
        forwards_of[prereq].append(later)
        endpoints = (jurisdiction_of.get(later), jurisdiction_of.get(prereq))
        if endpoints != (_MULTI_STATE, _MULTI_STATE):
            non_ms_endpoints += 1

    # --- crosswalk indices (CA source -> CCSS target) ---
    ca_to_ccss: dict[str, list[tuple[float, str]]] = defaultdict(list)
    ccss_to_ca: dict[str, list[str]] = defaultdict(list)
    for rel in crosswalk:
        jaccard = float(rel["properties"].get("jaccard", "0") or 0)
        ca_to_ccss[rel["source_identifier"]].append((jaccard, rel["target_identifier"]))
        ccss_to_ca[rel["target_identifier"]].append(rel["source_identifier"])

    prog_rows: list[ProgRow] = []
    direct_b = direct_f = bridged_b = bridged_f = self_loops = 0

    # DIRECT (Multi-State CCSS): one primary backward + forward per node.
    for later, sources in prereqs_of.items():
        prog_rows.append((later, sorted(sources)[0], "backward", SOURCE))
        direct_b += 1
    for prereq, targets in forwards_of.items():
        prog_rows.append((prereq, sorted(targets)[0], "forward", SOURCE))
        direct_f += 1

    # CA BRIDGE: CA standard C reaches progressions via the crosswalk to a CCSS neighbour E.
    def _pick_bridge(cid: str, table: dict[str, list[str]]) -> str | None:
        for _jaccard, ccss in sorted(ca_to_ccss[cid], reverse=True):
            candidates = table.get(ccss)
            if candidates:
                primary = sorted(candidates)[0]
                ca_equivalents = ccss_to_ca.get(primary, [])
                chosen = ca_equivalents[0] if len(ca_equivalents) == 1 else primary
                if chosen == cid:  # never emit a self-referential progression
                    return primary if primary != cid else None
                return chosen
        return None

    for node in standards:
        if node["properties"].get("jurisdiction") != _CALIFORNIA:
            continue
        cid = node["identifier"]
        if cid not in ca_to_ccss:
            continue
        back = _pick_bridge(cid, prereqs_of)
        if back is not None:
            prog_rows.append((cid, back, "backward", SOURCE_BRIDGED))
            bridged_b += 1
        forward = _pick_bridge(cid, forwards_of)
        if forward is not None:
            prog_rows.append((cid, forward, "forward", SOURCE_BRIDGED))
            bridged_f += 1

    # --- learning components (supports edge: source = component, target = standard) ---
    node_desc: dict[str, str] = {
        r["identifier"]: r["properties"].get("description", "")
        for r in components
        if r.get("type") == "node"
    }
    supports = [
        r for r in components if r.get("type") == "relationship" and r.get("label") == "supports"
    ]
    by_target: dict[str, list[str]] = defaultdict(list)
    orphan_edges = 0
    for rel in supports:
        comp_id = rel["source_identifier"]
        std_id = rel["target_identifier"]
        if comp_id not in node_desc:
            orphan_edges += 1
            continue
        by_target[std_id].append(comp_id)

    comp_rows: list[CompRow] = []
    edges_missing_standard = 0
    for std_id, comp_ids in by_target.items():
        if std_id not in std_ids:
            edges_missing_standard += len(comp_ids)
            continue
        for ordinal, comp_id in enumerate(sorted(set(comp_ids)), start=1):
            comp_rows.append((std_id, ordinal, node_desc[comp_id], SOURCE))

    stats = IngestStats(
        standards=len(std_rows),
        progressions_backward=direct_b + bridged_b,
        progressions_forward=direct_f + bridged_f,
        learning_components=len(comp_rows),
        standards_without_code=without_code,
        progressions_direct=direct_b + direct_f,
        progressions_bridged=bridged_b + bridged_f,
        relatesto_skipped=relatesto_skipped,
        component_edges_orphaned=orphan_edges,
        component_edges_missing_standard=edges_missing_standard,
        html_texts_stripped=html_stripped,
        non_multistate_buildstowards_endpoints=non_ms_endpoints,
        bridge_self_loops_avoided=self_loops,
        multi_parent_children=multi_parent,
    )
    return BuiltRows(std_rows, prog_rows, comp_rows, stats)


def build_curriculum_rows(
    source_dir: str | Path,
) -> tuple[list[tuple], list[tuple], list[tuple]]:
    """Read the three curriculum files into (lessons, alignments, materials) row tuples.

    Missing files yield empty lists rather than raising: the curriculum layer is optional,
    and an export produced before ``scripts/extract_curriculum.py`` existed has none. The
    counts are reported by the caller, so empty is visible rather than mistaken for success.
    """
    src = Path(source_dir)

    def read(name: str) -> list[dict[str, Any]]:
        path = src / name
        if not path.exists():
            return []
        with path.open(encoding="utf-8") as fh:
            return [json.loads(line) for line in fh if line.strip()]

    lessons = [
        (
            r["identifier"], r.get("name") or "", r.get("description"), r.get("author"),
            r.get("entity") or "Lesson", r.get("courseCode"), r.get("curriculumLabel"),
            r.get("ordinalName"), _encode_grade(r.get("gradeLevel")),
            r.get("license") or "", r.get("attributionStatement") or "",
        )
        for r in read("curriculum-lessons.jsonl")
    ]
    by_id = {r["identifier"]: r for r in read("curriculum-materials.jsonl")}
    aligns: list[tuple] = []
    materials: list[tuple] = []
    for e in read("curriculum-edges.jsonl"):
        if e.get("kind") == "aligns":
            aligns.append((e["standard"], e["lesson"], e.get("alignmentType"),
                           e.get("curriculumAlignmentType"), None))
        elif e.get("kind") == "part":
            m = by_id.get(e["material"])
            if m is None:
                continue
            materials.append((
                e["lesson"], m["identifier"], m.get("name") or "", m.get("description"),
                m.get("entity") or "Activity", m.get("ordinalName"), m.get("educationalUse"),
                str(m["isOptional"]) if "isOptional" in m else None,
                m.get("license") or "", m.get("attributionStatement") or "",
            ))
    aligns.extend(_bridged_alignments(read("crosswalk.jsonl"), aligns))
    return lessons, aligns, materials


def _bridged_alignments(crosswalk: list[dict[str, Any]], direct: list[tuple]) -> list[tuple]:
    """Reach the curriculum from a state's own standards, via the CA->CCSS crosswalk.

    Measured on the v1.11.0 export: **all 561** standards carrying a curriculum alignment are
    Multi-State CCSS nodes, and **zero** are California's. So without this, a teacher who looks
    up their own state's HSG-SRT.B.4 gets an empty list while the Multi-State twin of the very
    same standard has 41 lessons. The tools were built and unreachable from the jurisdiction
    the store is for -- an empty list that looks exactly like "no lessons exist".

    This mirrors the progression bridge in :func:`build_rows` and uses the same edge, the
    export's own evidence-based ``hasStandardAlignment`` crosswalk, taking the highest
    ``jaccard`` neighbour that actually has curriculum. Bridged rows carry the CCSS uuid they
    came from so a caller can tell a stated alignment from an inferred one; nothing is
    presented as direct that is not.
    """
    by_standard: dict[str, list[tuple]] = defaultdict(list)
    for row in direct:
        by_standard[row[0]].append(row)

    candidates: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for rel in crosswalk:
        jaccard = float(rel["properties"].get("jaccard", "0") or 0)
        candidates[rel["source_identifier"]].append((jaccard, rel["target_identifier"]))

    bridged: list[tuple] = []
    for source, targets in candidates.items():
        if source in by_standard:  # it states its own alignments; do not infer over them
            continue
        for _jaccard, target in sorted(targets, reverse=True):
            rows = by_standard.get(target)
            if not rows:
                continue
            bridged.extend(
                (source, lesson, alignment_type, curriculum_type, target)
                for _std, lesson, alignment_type, curriculum_type, _b in rows
            )
            break  # one neighbour only, or a standard inherits several curricula at once
    return bridged


def ingest_into_connection(conn: sqlite3.Connection, source_dir: str | Path) -> IngestStats:
    """Ingest ``source_dir`` into an open sqlite connection (idempotent: clears then inserts)."""
    rows = build_rows(source_dir)
    conn.execute("DELETE FROM standards")
    conn.execute("DELETE FROM progressions")
    conn.execute("DELETE FROM misconceptions")
    conn.execute("DELETE FROM learning_components")
    conn.executemany(
        "INSERT INTO standards VALUES (?,?,?,?,?,?,?,?,?)", rows.standards
    )
    conn.executemany("INSERT INTO progressions VALUES (?,?,?,?)", rows.progressions)
    conn.executemany("INSERT INTO learning_components VALUES (?,?,?,?)", rows.components)

    lessons, aligns, materials = build_curriculum_rows(source_dir)
    conn.execute("DELETE FROM curriculum_lessons")
    conn.execute("DELETE FROM lesson_alignments")
    conn.execute("DELETE FROM lesson_materials")
    conn.executemany("INSERT INTO curriculum_lessons VALUES (?,?,?,?,?,?,?,?,?,?,?)", lessons)
    conn.executemany("INSERT INTO lesson_alignments VALUES (?,?,?,?,?)", aligns)
    conn.executemany("INSERT INTO lesson_materials VALUES (?,?,?,?,?,?,?,?,?,?)", materials)
    conn.commit()
    return replace(
        rows.stats,
        curriculum_lessons=len(lessons),
        curriculum_alignments=len(aligns),
        curriculum_materials=len(materials),
    )


def build_database(source_dir: str | Path, db_path: str | Path) -> IngestStats:
    """Create the schema (via the repository) and ingest the CA-math export into ``db_path``."""
    repo = SqliteStandardsRepository(str(db_path))
    repo.create_schema()
    repo.close()
    conn = sqlite3.connect(str(db_path))
    try:
        return ingest_into_connection(conn, source_dir)
    finally:
        conn.close()
