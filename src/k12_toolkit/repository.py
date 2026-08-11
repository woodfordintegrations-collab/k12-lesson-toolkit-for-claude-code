"""The ``StandardsRepository`` interface and its two implementations.

The MCP server depends only on the :class:`StandardsRepository` protocol, never on a
concrete storage engine, so the store can be swapped:

- :class:`InMemoryStandardsRepository` — a pure-Python fixture store used by the contract
  tests (and any embedding that already holds the entities in memory).
- :class:`SqliteStandardsRepository` — an embedded sqlite3-backed store for real data.

Query semantics (identical across both implementations):

- ``find_by_code`` is a **prefix** match on ``code``: a leaf code returns just itself; a
  parent code (e.g. ``"2.OA"``) returns the parent AND every descendant whose code starts
  with it. Optional ``academic_subject`` / ``jurisdiction`` filters narrow the result.
- ``search_by_keywords`` is an **OR** match: a standard matches if ANY keyword appears
  (case-insensitively) in its ``statement_text``.

See ``docs/superpowers/specs/2026-07-22-standards-resource-design.md`` §4, §6.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Callable, Iterable, Sequence
from typing import Any, Protocol, runtime_checkable

from k12_toolkit.model import (
    BACKWARD,
    FORWARD,
    CurriculumLesson,
    LearningComponent,
    LessonMaterial,
    Misconception,
    Progression,
    Standard,
)


@runtime_checkable
class StandardsRepository(Protocol):
    """Read interface over the standards store. All methods are total (never raise)."""

    def get_by_uuid(self, uuid: str) -> Standard | None:
        """Return the standard with this ``case_uuid``, or ``None`` if unknown."""
        ...

    def find_by_code(
        self,
        code: str,
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        """Prefix-match standards by ``code`` (parent code returns parent + descendants)."""
        ...

    def search_by_keywords(
        self,
        keywords: list[str],
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        """OR-match standards whose ``statement_text`` contains ANY keyword (ci)."""
        ...

    def children_of(self, uuid: str) -> list[Standard]:
        """Return the direct children (``parent_uuid == uuid``), for ``subStandards``."""
        ...

    def progression(self, uuid: str, direction: str) -> Standard | None:
        """Follow a progression edge from ``uuid`` in ``direction``; return the target."""
        ...

    def misconceptions(self, uuid: str) -> list[Misconception]:
        """Return the misconceptions attached to ``uuid``."""
        ...

    def learning_components(self, uuid: str) -> list[LearningComponent]:
        """Return the learning components of ``uuid``, ordered by ``ordinal``."""
        ...

    def standards_for_mathematical_practice(self) -> list[Standard]:
        """Return the Standards for Mathematical Practice, one per code, ordered by code."""
        ...


def _keyword_match(statement_text: str, keywords: Iterable[str]) -> bool:
    """OR-match: True if any non-empty keyword appears (case-insensitively) in the text."""
    haystack = statement_text.lower()
    return any(kw and kw.lower() in haystack for kw in keywords)


class InMemoryStandardsRepository:
    """A fixture store backed by plain Python lists — used by the contract tests."""

    def __init__(
        self,
        standards: Sequence[Standard] = (),
        progressions: Sequence[Progression] = (),
        misconceptions: Sequence[Misconception] = (),
        components: Sequence[LearningComponent] = (),
    ) -> None:
        self._standards: list[Standard] = list(standards)
        self._by_uuid: dict[str, Standard] = {s.case_uuid: s for s in self._standards}
        self._progressions: list[Progression] = list(progressions)
        self._misconceptions: list[Misconception] = list(misconceptions)
        self._components: list[LearningComponent] = list(components)

    def get_by_uuid(self, uuid: str) -> Standard | None:
        return self._by_uuid.get(uuid)

    def find_by_code(
        self,
        code: str,
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        if not code:
            return []
        matches = [
            s
            for s in self._standards
            if (s.code == code or s.code.startswith(code + "."))
            and (academic_subject is None or s.academic_subject.lower() == academic_subject.lower())
            and (jurisdiction is None or s.jurisdiction.lower() == jurisdiction.lower())
        ]
        return sorted(matches, key=lambda s: s.code)

    def search_by_keywords(
        self,
        keywords: list[str],
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        if not keywords:
            return []
        matches = [
            s
            for s in self._standards
            if _keyword_match(s.statement_text, keywords)
            and (academic_subject is None or s.academic_subject.lower() == academic_subject.lower())
            and (jurisdiction is None or s.jurisdiction.lower() == jurisdiction.lower())
        ]
        return sorted(matches, key=lambda s: s.code)

    def children_of(self, uuid: str) -> list[Standard]:
        matches = [s for s in self._standards if s.parent_uuid == uuid]
        return sorted(matches, key=lambda s: s.code)

    def progression(self, uuid: str, direction: str) -> Standard | None:
        matches = sorted(
            (e for e in self._progressions if e.from_uuid == uuid and e.direction == direction),
            key=lambda e: e.to_uuid,
        )
        if not matches:
            return None
        return self._by_uuid.get(matches[0].to_uuid)

    def misconceptions(self, uuid: str) -> list[Misconception]:
        return [m for m in self._misconceptions if m.case_uuid == uuid]

    def learning_components(self, uuid: str) -> list[LearningComponent]:
        matches = [c for c in self._components if c.case_uuid == uuid]
        return sorted(matches, key=lambda c: c.ordinal)

    def standards_for_mathematical_practice(self) -> list[Standard]:
        practices = [s for s in self._by_uuid.values() if _is_practice_code(s.code)]
        return _one_per_practice_code(practices)


# --- the Standards for Mathematical Practice --------------------------------
# MP1-MP8 are stored once per jurisdiction (a CA-math slice holds California's and
# Multi-State's copies of each, with identical statement text but different attribution).
# Both implementations collapse that to one row per code, preferring the adopting state's
# own record over the Multi-State one, because that is the text and the attribution a
# teacher in that state owes.


def _is_practice_code(code: str) -> bool:
    return len(code) == 3 and code.upper().startswith("MP") and code[2].isdigit()


def _one_per_practice_code(practices: list[Standard]) -> list[Standard]:
    chosen: dict[str, Standard] = {}
    for standard in sorted(practices, key=lambda s: (s.jurisdiction == "Multi-State", s.case_uuid)):
        chosen.setdefault(standard.code.upper(), standard)
    return [chosen[code] for code in sorted(chosen)]


# --- sqlite implementation --------------------------------------------------

_SCHEMA = """
CREATE TABLE IF NOT EXISTS standards (
    case_uuid       TEXT PRIMARY KEY,
    code            TEXT NOT NULL,
    statement_text  TEXT NOT NULL,
    academic_subject TEXT NOT NULL,
    jurisdiction    TEXT NOT NULL,
    grade           TEXT,
    parent_uuid     TEXT,
    source          TEXT NOT NULL,
    source_license  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_standards_code ON standards (code);
CREATE INDEX IF NOT EXISTS idx_standards_parent ON standards (parent_uuid);

CREATE TABLE IF NOT EXISTS progressions (
    from_uuid   TEXT NOT NULL,
    to_uuid     TEXT NOT NULL,
    direction   TEXT NOT NULL,
    source      TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_progressions_from ON progressions (from_uuid, direction);

CREATE TABLE IF NOT EXISTS misconceptions (
    case_uuid        TEXT NOT NULL,
    student_behavior TEXT NOT NULL,
    teacher_move     TEXT NOT NULL,
    source           TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_misconceptions_uuid ON misconceptions (case_uuid);

CREATE TABLE IF NOT EXISTS learning_components (
    case_uuid   TEXT NOT NULL,
    ordinal     INTEGER NOT NULL,
    description TEXT NOT NULL,
    source      TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_components_uuid ON learning_components (case_uuid);

CREATE TABLE IF NOT EXISTS curriculum_lessons (
    lesson_id        TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    description      TEXT,
    author           TEXT,
    entity           TEXT NOT NULL,
    course_code      TEXT,
    curriculum_label TEXT,
    ordinal_name     TEXT,
    grade            TEXT,
    source_license   TEXT NOT NULL,
    attribution      TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_lessons_author ON curriculum_lessons (author);

CREATE TABLE IF NOT EXISTS lesson_alignments (
    case_uuid       TEXT NOT NULL,
    lesson_id       TEXT NOT NULL,
    alignment_type  TEXT,
    curriculum_type TEXT,
    -- NULL for an alignment the export states directly. Otherwise the Multi-State standard
    -- this row was reached through: the curriculum aligns ONLY to Multi-State CCSS nodes, so
    -- without a bridge every lookup of a state's own standard returns nothing.
    bridged_from    TEXT
);
CREATE INDEX IF NOT EXISTS idx_alignments_uuid ON lesson_alignments (case_uuid);

CREATE TABLE IF NOT EXISTS lesson_materials (
    lesson_id       TEXT NOT NULL,
    material_id     TEXT NOT NULL,
    name            TEXT NOT NULL,
    description     TEXT,
    entity          TEXT NOT NULL,
    ordinal_name    TEXT,
    educational_use TEXT,
    is_optional     TEXT,
    source_license  TEXT NOT NULL,
    attribution     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_materials_lesson ON lesson_materials (lesson_id);
"""


def _escape_like(value: str) -> str:
    """Escape LIKE metacharacters (``\\``, ``%``, ``_``) so ``value`` can't act as a wildcard."""
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def _row_to_standard(row: sqlite3.Row) -> Standard:
    return Standard(
        case_uuid=row["case_uuid"],
        code=row["code"],
        statement_text=row["statement_text"],
        academic_subject=row["academic_subject"],
        jurisdiction=row["jurisdiction"],
        grade=row["grade"],
        parent_uuid=row["parent_uuid"],
        source=row["source"],
        source_license=row["source_license"],
    )


class SqliteStandardsRepository:
    """An embedded sqlite3-backed store implementing the read interface.

    The schema is defined here (:func:`create_schema`); actual data ingestion is a
    SEPARATE later task — see :meth:`load` (a TODO stub). The read methods below are
    complete and mirror :class:`InMemoryStandardsRepository` exactly.
    """

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row

    def create_schema(self) -> None:
        """Create the (empty) tables + indexes if they do not already exist."""
        self._conn.executescript(_SCHEMA)
        self._conn.commit()

    def load(self, source: str | None = None) -> None:
        """Populate the store from the openly-licensed Learning Commons CA-math export.

        ``source`` is the directory of ``*.jsonl`` export files (e.g. ``data/ca-math``);
        ingestion is delegated to the :mod:`k12_toolkit.ingest` package (spec §5, §9).
        Called with no ``source`` this remains a stub — an explicit export directory is
        required to ingest (the store is populated by the ``python -m k12_toolkit.ingest``
        CLI, and the MCP server reads the already-built DB via ``K12_TOOLKIT_DB``).
        """
        if source is None:
            raise NotImplementedError(
                "Ingestion requires an explicit export directory; "
                "see k12_toolkit.ingest (python -m k12_toolkit.ingest --source ...)."
            )
        from k12_toolkit.ingest.builder import ingest_into_connection

        self.create_schema()
        ingest_into_connection(self._conn, source)

    def close(self) -> None:
        self._conn.close()

    def get_by_uuid(self, uuid: str) -> Standard | None:
        cur = self._conn.execute(
            "SELECT * FROM standards WHERE case_uuid = ?", (uuid,)
        )
        row = cur.fetchone()
        return _row_to_standard(row) if row is not None else None

    def find_by_code(
        self,
        code: str,
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        if not code:
            return []
        sql = "SELECT * FROM standards WHERE (code = ? OR code LIKE ? ESCAPE '\\')"
        params: list[str] = [code, _escape_like(code) + ".%"]
        if academic_subject is not None:
            sql += " AND LOWER(academic_subject) = LOWER(?)"
            params.append(academic_subject)
        if jurisdiction is not None:
            sql += " AND LOWER(jurisdiction) = LOWER(?)"
            params.append(jurisdiction)
        sql += " ORDER BY code"
        return [_row_to_standard(r) for r in self._conn.execute(sql, params)]

    def search_by_keywords(
        self,
        keywords: list[str],
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        terms = [kw for kw in keywords if kw]
        if not terms:
            return []
        or_clause = " OR ".join(["LOWER(statement_text) LIKE ? ESCAPE '\\'"] * len(terms))
        sql = f"SELECT * FROM standards WHERE ({or_clause})"
        params: list[str] = [f"%{_escape_like(kw.lower())}%" for kw in terms]
        if academic_subject is not None:
            sql += " AND LOWER(academic_subject) = LOWER(?)"
            params.append(academic_subject)
        if jurisdiction is not None:
            sql += " AND LOWER(jurisdiction) = LOWER(?)"
            params.append(jurisdiction)
        sql += " ORDER BY code"
        return [_row_to_standard(r) for r in self._conn.execute(sql, params)]

    def children_of(self, uuid: str) -> list[Standard]:
        cur = self._conn.execute(
            "SELECT * FROM standards WHERE parent_uuid = ? ORDER BY code", (uuid,)
        )
        return [_row_to_standard(r) for r in cur]

    def progression(self, uuid: str, direction: str) -> Standard | None:
        cur = self._conn.execute(
            "SELECT to_uuid FROM progressions WHERE from_uuid = ? AND direction = ? "
            "ORDER BY to_uuid LIMIT 1",
            (uuid, direction),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return self.get_by_uuid(row["to_uuid"])

    def misconceptions(self, uuid: str) -> list[Misconception]:
        cur = self._conn.execute(
            "SELECT * FROM misconceptions WHERE case_uuid = ?", (uuid,)
        )
        return [
            Misconception(
                case_uuid=r["case_uuid"],
                student_behavior=r["student_behavior"],
                teacher_move=r["teacher_move"],
                source=r["source"],
            )
            for r in cur
        ]

    def learning_components(self, uuid: str) -> list[LearningComponent]:
        cur = self._conn.execute(
            "SELECT * FROM learning_components WHERE case_uuid = ? ORDER BY ordinal",
            (uuid,),
        )
        return [
            LearningComponent(
                case_uuid=r["case_uuid"],
                ordinal=r["ordinal"],
                description=r["description"],
                source=r["source"],
            )
            for r in cur
        ]

    def standards_for_mathematical_practice(self) -> list[Standard]:
        # Matched in SQL by shape and re-checked in Python, because `code LIKE 'MP%'` alone
        # would also catch any future code that merely begins MP.
        cur = self._conn.execute(
            "SELECT * FROM standards WHERE UPPER(code) LIKE 'MP_' ORDER BY code"
        )
        rows = [_row_to_standard(r) for r in cur]
        return _one_per_practice_code([s for s in rows if _is_practice_code(s.code)])

    def curriculum_lessons(
        self,
        uuid: str,
        author: str | None = None,
        ordinal_name: str | None = None,
        lesson_name: str | None = None,
    ) -> list[CurriculumLesson]:
        """Lessons aligned to ``uuid``, most directly-taught first.

        ``alignment_type`` distinguishes a lesson that teaches the standard from one that
        merely builds toward it, and the caller almost always wants the former, so the
        ordering is part of the contract rather than a detail.
        """
        sql = [
            # GROUP BY, not a bare join: one lesson can align to one standard through
            # several edges (it teaches it AND builds toward it), and uncollapsed those
            # duplicates fill the caller's result cap with the same lesson two or three times.
            "SELECT l.*, MIN(CASE a.alignment_type WHEN 'teaches' THEN 0 ELSE 1 END) AS rank,",
            # A lesson reached both directly and through the bridge counts as direct: MIN over
            # a column that is NULL for direct rows returns NULL when any direct row exists.
            "MIN(a.bridged_from) AS bridged_from",
            "FROM curriculum_lessons l",
            "JOIN lesson_alignments a ON a.lesson_id = l.lesson_id",
            "WHERE a.case_uuid = ?",
        ]
        params: list[Any] = [uuid]
        if author:
            sql.append("AND l.author = ?")
            params.append(author)
        if ordinal_name:
            sql.append("AND l.ordinal_name = ?")
            params.append(ordinal_name)
        if lesson_name:
            sql.append("AND l.name LIKE ? ESCAPE '\\'")
            params.append(f"%{_escape_like(lesson_name)}%")
        sql.append(
            "GROUP BY l.lesson_id "
            "ORDER BY rank, l.course_code, l.ordinal_name, l.lesson_id"
        )
        cur = self._conn.execute(" ".join(sql), params)
        return [_row_to_lesson(r) for r in cur]

    def materials_for_lesson(
        self, lesson_id: str, material_source: list[str] | None = None
    ) -> list[LessonMaterial]:
        """Activities and assessments belonging to ``lesson_id``.

        ``material_source`` filters on the contract's vocabulary ("lesson", "activity",
        "assessment"). An unrecognised value filters to nothing rather than being ignored:
        silently widening a filter the caller asked for is how you return material the
        caller did not want and cannot tell apart.
        """
        sql = ["SELECT * FROM lesson_materials WHERE lesson_id = ?"]
        params: list[Any] = [lesson_id]
        if material_source:
            wanted = {s.strip().lower() for s in material_source}
            # "lesson" in the contract means the lesson-level overview material; the export
            # models those as Activity rows too, so it maps to the same entity set.
            entities = set()
            if {"activity", "lesson"} & wanted:
                entities.add("Activity")
            if "assessment" in wanted:
                entities.add("Assessment")
            placeholders = ", ".join("?" for _ in entities) or "NULL"
            sql.append(f"AND entity IN ({placeholders})")
            params.extend(sorted(entities))
        sql.append("ORDER BY ordinal_name, material_id")
        cur = self._conn.execute(" ".join(sql), params)
        return [
            LessonMaterial(
                lesson_id=r["lesson_id"],
                material_id=r["material_id"],
                name=r["name"],
                description=r["description"],
                entity=r["entity"],
                ordinal_name=r["ordinal_name"],
                educational_use=r["educational_use"],
                is_optional=r["is_optional"],
                source_license=r["source_license"],
                attribution=r["attribution"],
            )
            for r in cur
        ]


# --- richest-representative selection (query-layer dedup) --------------------
#
# A single code usually resolves to SEVERAL same-code nodes: the canonical CCSS node plus
# multiple California framework/course placements. Data is authored against SOME of those
# nodes, not replicated across all — and different facets (a prerequisite, sub-skills,
# subStandards, misconceptions) can live on DIFFERENT placements. Returning the raw set
# surfaces an empty placement first (and unstably, since same-code ties are unordered).
#
# So we collapse to one representative per code for grounding, but resolve each FACET to the
# sibling that actually holds it:
#   * dedupe_richest / _grounding_score — pick the representative + rank keyword hits, on the
#     progression+component score (what a lesson grounds on).
#   * select_by_code — resolve a bare `code` to the sibling best for ONE facet (a directional
#     edge, a component count, a misconception count), so a code lookup never misses data that
#     sits on a different placement than the "overall richest" one.
# subStandards are unioned across all same-code placements by the server (children, too, can
# live on a sibling). See spec §4, §6.
#
# `cache` memoizes a node's grounding score across the several sort passes of one request.


FacetScore = Callable[["StandardsRepository", Standard], int]


def _row_to_lesson(r: sqlite3.Row) -> CurriculumLesson:
    return CurriculumLesson(
        lesson_id=r["lesson_id"], name=r["name"], description=r["description"],
        author=r["author"], entity=r["entity"], course_code=r["course_code"],
        curriculum_label=r["curriculum_label"], ordinal_name=r["ordinal_name"],
        grade=r["grade"], source_license=r["source_license"], attribution=r["attribution"],
        bridged_from=r["bridged_from"],
    )


def _grounding_score(
    repo: StandardsRepository, std: Standard, cache: dict[str, int] | None = None
) -> int:
    """Progression + component data a node carries — the grounding-representative rank."""
    if cache is not None and std.case_uuid in cache:
        return cache[std.case_uuid]
    score = 0
    if repo.progression(std.case_uuid, BACKWARD) is not None:
        score += 1
    if repo.progression(std.case_uuid, FORWARD) is not None:
        score += 1
    score += len(repo.learning_components(std.case_uuid))
    if cache is not None:
        cache[std.case_uuid] = score
    return score


def dedupe_richest(
    repo: StandardsRepository,
    standards: Sequence[Standard],
    *,
    prefer_jurisdiction: str = "California",
    order_by_richness: bool = False,
    cache: dict[str, int] | None = None,
) -> list[Standard]:
    """Collapse same-code duplicates to the single richest node per code.

    By default preserves the first-seen order of distinct codes (callers pass code-sorted
    input, so the result stays code-sorted). With ``order_by_richness`` the survivors are
    re-sorted richest-first (used for keyword hits, where the best grounding target should
    lead). Ties break deterministically: more grounding data wins, then ``prefer_jurisdiction``,
    then the lexicographically smallest ``case_uuid`` — so the choice is stable across calls.
    Single-member groups skip scoring; ``cache`` avoids re-scoring a node across sort passes.
    """
    if cache is None:
        cache = {}
    groups: dict[str, list[Standard]] = {}
    for std in standards:
        groups.setdefault(std.code, []).append(std)
    out: list[Standard] = []
    for members in groups.values():
        if len(members) == 1:  # no tie to break — skip the scoring queries entirely
            out.append(members[0])
            continue
        members.sort(
            key=lambda s: (
                -_grounding_score(repo, s, cache),
                0 if s.jurisdiction == prefer_jurisdiction else 1,
                s.case_uuid,
            )
        )
        out.append(members[0])
    if order_by_richness:
        out.sort(key=lambda s: (-_grounding_score(repo, s, cache), s.code))
    return out


def select_by_code(
    repo: StandardsRepository,
    code: str,
    facet_score: FacetScore,
    *,
    prefer_jurisdiction: str = "California",
) -> Standard | None:
    """Among exact same-code nodes, return the one that best serves a single facet.

    ``facet_score`` ranks nodes for a specific datum ("has a backward edge", "component count",
    "misconception count"); ties fall back to overall grounding richness, then
    ``prefer_jurisdiction``, then the smallest uuid. This lets a bare-``code`` lookup reach the
    sibling that holds the requested datum even when a DIFFERENT sibling is richer overall.
    """
    if not code:
        return None
    exact = [s for s in repo.find_by_code(code) if s.code == code]
    if not exact:
        return None
    exact.sort(
        key=lambda s: (
            -facet_score(repo, s),
            -_grounding_score(repo, s),
            0 if s.jurisdiction == prefer_jurisdiction else 1,
            s.case_uuid,
        )
    )
    return exact[0]


def richest_by_code(
    repo: StandardsRepository,
    code: str,
    *,
    prefer_jurisdiction: str = "California",
) -> Standard | None:
    """Resolve a single code to its overall-richest node (grounding score, facet-agnostic)."""
    return select_by_code(repo, code, _grounding_score, prefer_jurisdiction=prefer_jurisdiction)
