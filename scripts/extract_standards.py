#!/usr/bin/env python3
"""Extract one jurisdiction + subject of standards from the raw Learning Commons export.

This is the script that produced the shipped `data/ca-math/`. It is here so that slice is not
the only one anyone can have: the pipeline is jurisdiction- and subject-agnostic, and shipping
California mathematics is a filter setting chosen for clone size, not a capability boundary.

    python3 scripts/extract_standards.py --list
    python3 scripts/extract_standards.py --raw data/raw --out data/tx-sci \
        --jurisdiction Texas --subject Science

Then build the store from the new directory and point the MCP server at it.

What gets selected, and why Multi-State comes too
------------------------------------------------
    StandardsFrameworkItem  where  academicSubject == SUBJECT
                            and    jurisdiction   in {JURISDICTION, "Multi-State"}

A state's own standards carry no `buildsTowards` edges -- every one of the 757 in the v1.11.0
export runs between Multi-State (CCSS) nodes. A state reaches the progression graph only by
`hasStandardAlignment` crosswalk into that Multi-State spine, which is the bridge the ingest
builds. Drop Multi-State from the selection and the standards still load, the crosswalk still
loads, and every progression lookup silently returns nothing. So Multi-State is not optional
and is not a flag: it is part of what makes the slice usable, and it is always included.

Edges are then filtered by whether their endpoints survived that node selection:

    hasChild               target in set          -> hierarchy.jsonl
    buildsTowards/relatesTo    both in set        -> progressions.jsonl
    hasStandardAlignment       both in set        -> crosswalk.jsonl
    supports               target in set          -> components.jsonl (edges, then the
                                                     LearningComponent nodes they point from)

`hasChild` keeps an edge whose *source* is outside the set on purpose: 6 of California's come
from `StandardsFramework` root nodes, which are not StandardsFrameworkItems and so are never
selected. Requiring both endpoints would silently orphan those subtrees.

Verification
------------
Re-running this with `--jurisdiction California --subject Mathematics` reproduces the shipped
`data/ca-math/` byte for byte (`tests/test_extract_standards.py` asserts the selection rule
against a fixture; `--verify DIR` checks a real run against a directory). Records are copied
verbatim from the raw lines rather than re-serialized, so nothing is silently reshaped on the
way through.

Misconceptions
--------------
`misconceptions.jsonl` is written empty for every slice, and that is a measurement rather than
a stub: across all 247,786 nodes of the v1.11.0 export, zero properties and zero relationship
labels match misconception/error/mistake. The store's misconception tool has no data in any
jurisdiction. The empty file exists so the ingest's file list is uniform.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

SFI = "StandardsFrameworkItem"
COMPONENT = "LearningComponent"
MULTI_STATE = "Multi-State"

# label -> (output file, does the SOURCE also have to be in the node set?)
EDGE_ROUTES = {
    "hasChild": ("hierarchy.jsonl", False),
    "buildsTowards": ("progressions.jsonl", True),
    "relatesTo": ("progressions.jsonl", True),
    "hasStandardAlignment": ("crosswalk.jsonl", True),
    "supports": ("components.jsonl", False),
}
OUTPUTS = ("standards.jsonl", "hierarchy.jsonl", "progressions.jsonl", "crosswalk.jsonl",
           "components.jsonl", "misconceptions.jsonl")


def iter_jsonl(path: Path):
    """Yield (raw_line_without_newline, parsed_dict) so records can be copied verbatim."""
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line:
                yield line, json.loads(line)


def list_available(raw: Path) -> int:
    """Print the jurisdiction x subject matrix so a user can pick a real pair."""
    counts: Counter[tuple[str, str]] = Counter()
    for _, node in iter_jsonl(raw / "nodes.jsonl"):
        if SFI not in (node.get("labels") or ()):
            continue
        props = node["properties"]
        counts[(props.get("jurisdiction") or "(none)",
                props.get("academicSubject") or "(none)")] += 1

    subjects = sorted({s for _, s in counts})
    jurisdictions = sorted({j for j, _ in counts})
    width = max(len(j) for j in jurisdictions)
    print(f"{'jurisdiction':<{width}}  " + "  ".join(f"{s[:22]:>22}" for s in subjects))
    for jur in jurisdictions:
        cells = "  ".join(f"{counts.get((jur, s), 0):>22,}" for s in subjects)
        print(f"{jur:<{width}}  {cells}")
    print(f"\n{len(jurisdictions)} jurisdictions x {len(subjects)} subjects, "
          f"{sum(counts.values()):,} standards total.")
    print(f"Every slice also includes the {MULTI_STATE} standards for its subject "
          "(the progression spine).")
    return 0


def extract(raw: Path, out: Path, jurisdiction: str, subject: str) -> dict[str, int]:
    out.mkdir(parents=True, exist_ok=True)
    keep_jurisdictions = {jurisdiction, MULTI_STATE}

    # --- pass 1: the standards themselves ---
    node_ids: set[str] = set()
    per_jurisdiction: Counter[str] = Counter()
    with (out / "standards.jsonl").open("w", encoding="utf-8") as fh:
        for line, node in iter_jsonl(raw / "nodes.jsonl"):
            if SFI not in (node.get("labels") or ()):
                continue
            props = node["properties"]
            if props.get("academicSubject") != subject:
                continue
            jur = props.get("jurisdiction")
            if jur not in keep_jurisdictions:
                continue
            node_ids.add(node["identifier"])
            per_jurisdiction[jur] += 1
            fh.write(line + "\n")

    # A misspelled jurisdiction is the dangerous case, not an empty one: Multi-State matches on
    # subject alone, so `--jurisdiction Californa` would otherwise write a perfectly valid slice
    # holding 836 CCSS standards, none of them the state's, and exit 0. Fail on the jurisdiction
    # contributing nothing, not on the total being zero.
    if per_jurisdiction[jurisdiction] == 0 and jurisdiction != MULTI_STATE:
        print(f"error: jurisdiction={jurisdiction!r} contributed 0 standards for "
              f"subject={subject!r} (only the {per_jurisdiction[MULTI_STATE]:,} {MULTI_STATE} "
              f"standards matched, which every slice gets). Check the spelling against --list.",
              file=sys.stderr)
        return {}
    if not node_ids:
        print(f"error: no standards matched jurisdiction={jurisdiction!r} subject={subject!r}. "
              "Run --list to see the pairs that exist.", file=sys.stderr)
        return {}

    # --- pass 2: edges whose endpoints survived ---
    handles = {name: (out / name).open("w", encoding="utf-8")
               for name in {route[0] for route in EDGE_ROUTES.values()}}
    counts: Counter[str] = Counter()
    component_ids: set[str] = set()
    try:
        for line, rel in iter_jsonl(raw / "relationships.jsonl"):
            route = EDGE_ROUTES.get(rel.get("label"))
            if route is None:
                continue
            name, source_must_be_in = route
            if rel["target_identifier"] not in node_ids:
                continue
            source = rel["source_identifier"]
            if source_must_be_in and source not in node_ids:
                continue
            if rel["label"] == "supports":
                component_ids.add(source)
            handles[name].write(line + "\n")
            counts[rel["label"]] += 1
    finally:
        for handle in handles.values():
            handle.close()

    # --- pass 3: the LearningComponent bodies those supports edges point from ---
    # Appended after the edges, because that is the layout build_rows() reads: it takes
    # descriptions from the `node` records and edges from the `relationship` records in the
    # same file, and an edge whose component body is missing is counted as orphaned.
    found_components = 0
    with (out / "components.jsonl").open("a", encoding="utf-8") as fh:
        for line, node in iter_jsonl(raw / "nodes.jsonl"):
            if COMPONENT in (node.get("labels") or ()) and node["identifier"] in component_ids:
                fh.write(line + "\n")
                found_components += 1

    (out / "misconceptions.jsonl").write_text("", encoding="utf-8")

    orphaned = len(component_ids) - found_components
    stats = {
        "standards": len(node_ids),
        f"  {jurisdiction}": per_jurisdiction[jurisdiction],
        f"  {MULTI_STATE}": per_jurisdiction[MULTI_STATE],
        "hierarchy edges": counts["hasChild"],
        "progression edges": counts["buildsTowards"] + counts["relatesTo"],
        "crosswalk edges": counts["hasStandardAlignment"],
        "component edges": counts["supports"],
        "component bodies": found_components,
    }
    for key, value in stats.items():
        print(f"  {key:<20}: {value:,}")

    # A slice with no progression path is loadable but answers nothing on the progression
    # tools. Say so at extract time rather than letting the tool return an empty list later.
    if counts["buildsTowards"] == 0:
        print("\n  NOTE: 0 buildsTowards edges. The v1.11.0 export carries progressions for "
              "CCSS mathematics only, so find_standards_progression_from_standard will return "
              "nothing for this slice. Everything else works.")
    if counts["hasStandardAlignment"] == 0 and per_jurisdiction[jurisdiction]:
        print(f"  NOTE: 0 crosswalk edges, so {jurisdiction} standards cannot bridge into the "
              f"{MULTI_STATE} progression spine.")
    if orphaned:
        print(f"  NOTE: {orphaned:,} supports edges point at component bodies that are not in "
              f"the export; the ingest counts these as orphaned and skips them.")
    return stats


def verify(out: Path, against: Path) -> int:
    """Compare a freshly extracted directory against a reference, file by file.

    Compares RECORDS, not bytes. JSONL whitespace carries no meaning, and an early version of
    this function compared bytes and so reported MISMATCH on an extraction that was in fact
    correct in every record -- the reference had merely been serialized with `json.dumps`
    default spacing while this script copies the raw lines through untouched. A checker that
    fails on correct data teaches people to ignore it, so the distinction is now reported
    explicitly instead of being collapsed into a single verdict.
    """
    ok = True
    for name in OUTPUTS:
        produced, reference = out / name, against / name
        if not reference.exists():
            print(f"  {name:<24} SKIP  (no reference)")
            continue
        raw_a, raw_b = produced.read_bytes(), reference.read_bytes()
        recs_a = [json.loads(x) for x in raw_a.decode().splitlines() if x.strip()]
        recs_b = [json.loads(x) for x in raw_b.decode().splitlines() if x.strip()]

        if recs_a == recs_b:
            byte_note = "" if raw_a == raw_b else "  (same records, different JSON spacing)"
            print(f"  {name:<24} IDENTICAL  {len(recs_a):,} records{byte_note}")
            continue

        canon_a = Counter(json.dumps(r, sort_keys=True) for r in recs_a)
        canon_b = Counter(json.dumps(r, sort_keys=True) for r in recs_b)
        if canon_a == canon_b:
            # Same records, different sequence. Nothing downstream reads these files
            # positionally, so this is reported and tolerated rather than failed.
            print(f"  {name:<24} REORDERED  {len(recs_a):,} records, same set, "
                  f"different order")
            continue
        ok = False
        extra = sum((canon_a - canon_b).values())
        missing = sum((canon_b - canon_a).values())
        print(f"  {name:<24} DIFFERS    +{extra:,} produced-only, -{missing:,} reference-only")
    print("\nverify: MATCH" if ok else "\nverify: MISMATCH")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--raw", default="data/raw",
                        help="directory holding nodes.jsonl + relationships.jsonl (~812 MB, "
                             "not distributed here)")
    parser.add_argument("--out", default=None, help="output directory for the slice")
    parser.add_argument("--jurisdiction", default="California")
    parser.add_argument("--subject", default="Mathematics")
    parser.add_argument("--list", action="store_true",
                        help="print the jurisdiction x subject matrix and exit")
    parser.add_argument("--verify", metavar="DIR",
                        help="after extracting, compare the output against DIR file by file")
    args = parser.parse_args()

    raw = Path(args.raw)
    if not (raw / "nodes.jsonl").exists():
        print(f"error: {raw}/nodes.jsonl not found. The raw export is not distributed here; "
              "download it from the Learning Commons knowledge-graph release first.",
              file=sys.stderr)
        return 1
    if args.list:
        return list_available(raw)
    if args.out is None:
        parser.error("--out is required (or use --list)")

    out = Path(args.out)
    if out.exists() and any((out / name).exists() for name in OUTPUTS):
        print(f"note: overwriting the {len(OUTPUTS)} slice files already in {out}")
    if not extract(raw, out, args.jurisdiction, args.subject):
        return 1
    if args.verify:
        print()
        return verify(out, Path(args.verify))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
