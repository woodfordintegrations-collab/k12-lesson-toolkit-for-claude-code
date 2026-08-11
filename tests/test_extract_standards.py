"""The standards slice: what gets selected, and the rule that is easy to get wrong.

`scripts/extract_standards.py` is the script that produced the shipped `data/ca-math/`. The
selection rule it implements has one clause nobody would guess and every clause is silent when
broken, so each is pinned here against a fixture rather than against the 812 MB export.

The clause that matters: a slice always carries the **Multi-State** standards for its subject
alongside the jurisdiction's own. Every `buildsTowards` edge in the export runs between
Multi-State nodes, and a state reaches them only through the crosswalk. Select California
alone and the extract still succeeds, the store still builds, and every progression lookup
returns an empty list -- the same shape of silent-empty failure that made this project record
"the curriculum layer is not in the public export" as a fact for three weeks.

The first test is therefore a control: if the fixture stops exercising the rule, it fails
rather than letting the rest of the module pass on an empty selection.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "extract_standards", Path(__file__).resolve().parents[1] / "scripts" / "extract_standards.py"
)
assert _SPEC and _SPEC.loader
extract_standards = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(extract_standards)

LIC = "https://creativecommons.org/licenses/by/4.0/"


def _node(identifier: str, labels: list[str], **props: object) -> dict:
    return {"type": "node", "identifier": identifier, "labels": labels,
            "properties": {"identifier": identifier, "license": LIC, **props}}


def _rel(label: str, source: str, target: str, **props: object) -> dict:
    return {"type": "relationship", "identifier": f"r-{source}-{target}-{label}", "label": label,
            "source_identifier": source, "target_identifier": target,
            "source_labels": ["StandardsFrameworkItem"],
            "target_labels": ["StandardsFrameworkItem"],
            "properties": {"license": LIC, **props}}


def _std(identifier: str, jurisdiction: str, subject: str, code: str = "X.1") -> dict:
    return _node(identifier, ["StandardsFrameworkItem"], jurisdiction=jurisdiction,
                 academicSubject=subject, statementCode=code, description=f"text for {identifier}",
                 caseIdentifierUUID=f"case-{identifier}")


@pytest.fixture
def raw(tmp_path: Path) -> Path:
    """A miniature export: two jurisdictions, two subjects, every edge kind."""
    nodes = [
        _std("ca-1", "California", "Mathematics"),
        _std("ca-2", "California", "Mathematics"),
        _std("ms-1", "Multi-State", "Mathematics"),   # the CCSS spine
        _std("ms-2", "Multi-State", "Mathematics"),
        _std("tx-1", "Texas", "Mathematics"),         # another jurisdiction: excluded
        _std("ca-sci", "California", "Science"),      # another subject: excluded
        _node("comp-1", ["LearningComponent"], description="component one"),
        _node("comp-2", ["LearningComponent"], description="component two"),
        _node("comp-unused", ["LearningComponent"], description="never referenced"),
        _node("framework-1", ["StandardsFramework"], description="a framework root"),
    ]
    rels = [
        # hasChild from a framework ROOT, whose source is not a StandardsFrameworkItem and so is
        # never selected. Requiring both endpoints would silently orphan this subtree.
        _rel("hasChild", "framework-1", "ca-1"),
        _rel("hasChild", "ca-1", "ca-2"),
        _rel("hasChild", "ca-1", "ca-sci"),           # target outside the slice: dropped
        _rel("buildsTowards", "ms-1", "ms-2"),
        _rel("buildsTowards", "ms-2", "tx-1"),        # one endpoint outside: dropped
        _rel("relatesTo", "ms-1", "ms-2"),
        _rel("hasStandardAlignment", "ca-1", "ms-1", jaccard="0.9"),
        _rel("hasStandardAlignment", "tx-1", "ms-1", jaccard="0.8"),   # source outside: dropped
        _rel("supports", "comp-1", "ca-1"),
        _rel("supports", "comp-2", "ca-1"),
        _rel("supports", "comp-1", "ca-sci"),         # target outside the slice: dropped
    ]
    (tmp_path / "nodes.jsonl").write_text(
        "".join(json.dumps(n) + "\n" for n in nodes), encoding="utf-8")
    (tmp_path / "relationships.jsonl").write_text(
        "".join(json.dumps(r) + "\n" for r in rels), encoding="utf-8")
    return tmp_path


@pytest.fixture
def slice_dir(raw: Path, tmp_path: Path) -> Path:
    out = tmp_path / "out"
    extract_standards.extract(raw, out, "California", "Mathematics")
    return out


def read(out: Path, name: str) -> list[dict]:
    return [json.loads(line) for line in (out / name).read_text().splitlines() if line.strip()]


def ids(out: Path, name: str) -> set[str]:
    return {r["identifier"] for r in read(out, name)}


def test_control_the_fixture_selects_both_jurisdictions(slice_dir: Path) -> None:
    """Without this, a selection bug makes every assertion below pass on an empty slice."""
    selected = ids(slice_dir, "standards.jsonl")
    assert selected, "the fixture selected no standards at all"
    assert {"ca-1", "ca-2"} <= selected, "the jurisdiction's own standards are missing"
    assert {"ms-1", "ms-2"} <= selected, (
        "Multi-State is missing. Progressions live only between Multi-State nodes, so a slice "
        "without them answers every progression lookup with an empty list and no error."
    )


def test_other_jurisdictions_and_subjects_are_excluded(slice_dir: Path) -> None:
    selected = ids(slice_dir, "standards.jsonl")
    assert "tx-1" not in selected
    assert "ca-sci" not in selected
    assert len(selected) == 4


def test_haschild_keeps_an_edge_whose_source_is_outside_the_slice(slice_dir: Path) -> None:
    """Framework roots are not StandardsFrameworkItems; 6 of California's real edges start there."""
    edges = {(r["source_identifier"], r["target_identifier"]) for r in read(slice_dir,
                                                                           "hierarchy.jsonl")}
    assert ("framework-1", "ca-1") in edges
    assert ("ca-1", "ca-2") in edges
    assert ("ca-1", "ca-sci") not in edges, "target outside the slice must be dropped"


def test_progressions_and_crosswalk_require_both_endpoints(slice_dir: Path) -> None:
    prog = {(r["label"], r["source_identifier"], r["target_identifier"])
            for r in read(slice_dir, "progressions.jsonl")}
    assert prog == {("buildsTowards", "ms-1", "ms-2"), ("relatesTo", "ms-1", "ms-2")}, (
        "both labels share this file, and the edge into unselected tx-1 must be dropped"
    )
    cross = {(r["source_identifier"], r["target_identifier"]) for r in read(slice_dir,
                                                                           "crosswalk.jsonl")}
    assert cross == {("ca-1", "ms-1")}


def test_components_are_edges_then_only_the_bodies_they_reference(slice_dir: Path) -> None:
    """build_rows() reads both kinds from this one file and counts unmatched edges as orphaned."""
    records = read(slice_dir, "components.jsonl")
    kinds = [r["type"] for r in records]
    assert kinds == ["relationship"] * 2 + ["node"] * 2, "edges must precede the bodies"
    assert {r["identifier"] for r in records if r["type"] == "node"} == {"comp-1", "comp-2"}, (
        "comp-unused is referenced by no surviving edge and must not be shipped"
    )


def test_misconceptions_is_written_empty_for_every_slice(slice_dir: Path) -> None:
    """Measured, not stubbed: no misconception data exists anywhere in the public export."""
    assert (slice_dir / "misconceptions.jsonl").read_text() == ""


def test_records_are_copied_verbatim(raw: Path, slice_dir: Path) -> None:
    """Re-serializing would let a future json.dumps default quietly reshape shipped data."""
    source_lines = set((raw / "nodes.jsonl").read_text().splitlines())
    for line in (slice_dir / "standards.jsonl").read_text().splitlines():
        assert line in source_lines


def test_a_misspelled_jurisdiction_fails_instead_of_shipping_multi_state_alone(
    raw: Path, tmp_path: Path
) -> None:
    """The dangerous input is a typo, not an empty export.

    Multi-State matches on subject alone, so a misspelled state still selects a valid-looking
    slice of CCSS standards containing none of what was asked for. Guarding on the total being
    zero would never fire here; the guard is on the jurisdiction's own contribution.
    """
    assert extract_standards.extract(raw, tmp_path / "typo", "Californa", "Mathematics") == {}
    assert extract_standards.extract(raw, tmp_path / "none", "California", "Astrology") == {}


def test_multi_state_may_be_requested_on_its_own(raw: Path, tmp_path: Path) -> None:
    """The one jurisdiction that is legitimately alone must not trip the typo guard."""
    stats = extract_standards.extract(raw, tmp_path / "ms", "Multi-State", "Mathematics")
    assert stats["standards"] == 2


def test_verify_passes_on_a_faithful_copy_and_fails_on_a_changed_record(
    slice_dir: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Proving the checker. It must also tolerate whitespace, which it once wrongly failed."""
    reference = tmp_path / "reference"
    reference.mkdir()
    for name in extract_standards.OUTPUTS:
        # Re-serialize compactly: identical records, different bytes. This is the real shape of
        # the difference, since the export ships compact and json.dumps defaults to spaced.
        records = [json.loads(x) for x in (slice_dir / name).read_text().splitlines() if x.strip()]
        (reference / name).write_text(
            "".join(json.dumps(r, separators=(",", ":")) + "\n" for r in records))
    assert extract_standards.verify(slice_dir, reference) == 0
    assert "different JSON spacing" in capsys.readouterr().out

    changed = [json.loads(x) for x in (reference / "standards.jsonl").read_text().splitlines()]
    changed[0]["properties"]["description"] = "tampered"
    (reference / "standards.jsonl").write_text("".join(json.dumps(r) + "\n" for r in changed))
    assert extract_standards.verify(slice_dir, reference) == 1
