#!/usr/bin/env python3
"""Extract the curriculum layer from the raw Learning Commons export into data/ca-math/.

Run once against a downloaded `data/raw/` (nodes.jsonl + relationships.jsonl, ~812 MB, not
distributed here). The three files it writes ARE distributed, which is the point: a clone
gets the curriculum layer without the 812 MB.

    python3 scripts/extract_curriculum.py --raw data/raw --out data/ca-math

The join, and the trap in it
---------------------------
    Lesson --hasEducationalAlignment--> StandardsFrameworkItem
    Lesson --hasPart--> Activity | Assessment

One hop each. No crosswalk bridge is needed: measured on the v1.11.0 export, the curriculum
aligns to 561 distinct standards and **all 561** are already in the shipped set.

The trap is that two non-overlapping identifier spaces are in play. Standards carry both an
`identifier` and a `caseIdentifierUUID`, and for all 2,303 shipped standards those values
differ. Alignment edges point at the **node identifier**, even though the edge's own
`targetEntityKey` property says `caseIdentifierUUID`. That property is wrong.

Joining on the wrong key returns an empty result and raises nothing, which is
indistinguishable from "the curriculum data is not in the public export" — the conclusion
this project recorded as fact for three weeks. The run summary below prints the unreachable
count for exactly that reason: a join that silently matches nothing must not be able to
report success.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

LESSON_LABELS = {"Lesson", "LessonGrouping"}
MATERIAL_LABELS = {"Activity", "Assessment"}
# Fields kept per node. The full records carry provenance we do not need to re-ship, but
# licence and attribution are never dropped: they are the terms the data travels under.
KEEP = (
    "identifier", "name", "description", "author", "license", "attributionStatement",
    "courseCode", "curriculumLabel", "ordinalName", "gradeLevel", "academicSubject",
    "educationalUse", "audience", "isOptional", "inLanguage",
)


def load_shipped_standards(out: Path) -> dict[str, str]:
    """node identifier -> caseIdentifierUUID, for every shipped standard.

    Two identifier spaces are in play and they do not overlap at all (0 of 2,303 standards
    have identifier == caseIdentifierUUID). Curriculum alignment edges are keyed by NODE
    identifier, even though the edge's own `targetEntityKey` property says
    `caseIdentifierUUID`. That property is wrong; the data is what it is, and mixing the two
    spaces silently yields an empty join that looks exactly like "no curriculum data exists".

    The store is keyed by caseIdentifierUUID, because that is what the MCP contract passes.
    """
    mapping: dict[str, str] = {}
    with (out / "standards.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            d = json.loads(line)
            p = d.get("properties", d)
            node = d.get("identifier") or p.get("identifier")
            case = p.get("caseIdentifierUUID")
            if node and case:
                mapping[node] = case
    return mapping


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", default="data/raw")
    ap.add_argument("--out", default="data/ca-math")
    args = ap.parse_args()
    raw, out = Path(args.raw), Path(args.out)
    if not (raw / "nodes.jsonl").exists():
        return print(f"error: {raw}/nodes.jsonl not found. It is not distributed; "
                     "download the Learning Commons export first.") or 1

    node2case = load_shipped_standards(out)
    shipped = set(node2case)

    # 1. lesson -> standard alignments, and lesson -> material parts
    aligns: dict[str, list[dict]] = defaultdict(list)
    parts: dict[str, list[str]] = defaultdict(list)
    with (raw / "relationships.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            d = json.loads(line)
            src_labels = set(d.get("source_labels") or [])
            lbl, s, t = d.get("label"), d.get("source_identifier"), d.get("target_identifier")
            if lbl == "hasEducationalAlignment" and src_labels & LESSON_LABELS:
                p = d.get("properties", {})
                aligns[t].append({"lesson": s, "alignmentType": p.get("alignmentType"),
                                  "curriculumAlignmentType": p.get("curriculumAlignmentType")})
            elif lbl == "hasPart" and src_labels & LESSON_LABELS and set(
                    d.get("target_labels") or []) & (MATERIAL_LABELS | {"Lesson"}):
                parts[s].append(t)

    # 2. resolve each shipped standard to its lessons (one hop, on the NODE identifier)
    edges: list[dict] = []
    wanted_lessons: set[str] = set()
    unreachable = {t for t in aligns if t not in shipped}
    for node in node2case:
        for a in aligns.get(node, ()):
            wanted_lessons.add(a["lesson"])
            # Keyed by NODE identifier, because that is what the store's `case_uuid` column
            # actually holds (ingest inserts node["identifier"] into it). The column name
            # says caseIdentifierUUID and its contents do not, which is the same trap this
            # module's docstring describes -- and it caught this join a second time, from
            # the other side, after the first fix.
            edges.append({"standard": node, "lesson": a["lesson"],
                          "alignmentType": a["alignmentType"],
                          "curriculumAlignmentType": a["curriculumAlignmentType"]})

    # 3. materials belonging to those lessons (one hop; a LessonGrouping's parts are lessons)
    wanted_materials: set[str] = set()
    for lid in list(wanted_lessons):
        for child in parts.get(lid, ()):
            wanted_materials.add(child)

    # 4. pull the node bodies
    lessons, materials = [], []
    with (raw / "nodes.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            d = json.loads(line)
            labels = set(d.get("labels") or [])
            ident = (d.get("properties") or {}).get("identifier") or d.get("identifier")
            if labels & LESSON_LABELS and ident in wanted_lessons:
                lessons.append(_slim(d, labels, ident))
            elif labels & (MATERIAL_LABELS | {"Lesson"}) and ident in wanted_materials:
                materials.append(_slim(d, labels, ident))

    kept_material_ids = {m["identifier"] for m in materials}
    part_edges = [{"lesson": lid, "material": c} for lid, cs in parts.items()
                  if lid in wanted_lessons for c in cs if c in kept_material_ids]

    _write(out / "curriculum-lessons.jsonl", lessons)
    _write(out / "curriculum-materials.jsonl", materials)
    _write(out / "curriculum-edges.jsonl",
           [{"kind": "aligns", **e} for e in edges] + [{"kind": "part", **e} for e in part_edges])

    print(f"  lessons          : {len(lessons):,}")
    print(f"  materials        : {len(materials):,}")
    print(f"  alignment edges  : {len(edges):,}")
    print(f"  part edges       : {len(part_edges):,}")
    print(f"  curriculum-aligned standards we do not ship: {len(unreachable):,} of {len(aligns):,}")
    if not edges:
        print("  WARNING: zero alignment edges. Almost certainly an identifier-space "
              "mismatch, not an absence of data. See this module's docstring.")
    return 0


def _slim(d: dict, labels: set[str], ident: str) -> dict:
    p = d.get("properties") or {}
    row = {k: p[k] for k in KEEP if k in p}
    row["identifier"] = ident
    row["entity"] = next(iter(sorted(labels)))
    return row


def _write(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
