"""Ingestion tests over a SMALL inline LC-shaped fixture (never the full committed export).

The fixture is the minimum shape that exercises the load-bearing paths:

- a California standard ``C`` (``6.RP.A.2``) with NO ``buildsTowards`` of its own;
- a crosswalk ``C --hasStandardAlignment--> E`` to the Multi-State CCSS ``6.RP.A.2``;
- ``E``'s ``buildsTowards`` prerequisite (``6.RP.A.1``) and next standard (``7.RP.A.1``),
  each also crosswalked back from a CA equivalent (clean reverse crosswalk);
- a ``hasChild`` edge (parent ``6.RP.A`` -> child ``C``) for ``subStandards`` / parent_uuid;
- a ``supports`` component on ``C`` (+ its LearningComponent node);
- a ``relatesTo`` edge (must be skipped, never mapped to backward/forward);
- LaTeX + a stray HTML tag in statement text (LaTeX kept verbatim, tag stripped).

Everything is written to a temp dir and ingested into a temp sqlite DB, then asserted
through :class:`~k12_toolkit.repository.SqliteStandardsRepository`.
"""

from __future__ import annotations

import json
from pathlib import Path

from k12_toolkit.ingest.builder import build_database
from k12_toolkit.model import Standard
from k12_toolkit.repository import SqliteStandardsRepository

_LIC = "https://creativecommons.org/licenses/by/4.0/"

# --- node ids -------------------------------------------------------------------
CA_PARENT = "ca-parent-6rp-a"
CA_C = "ca-6rp-a2"  # the California standard under test
CA_PREREQ = "ca-6rp-a1"  # clean CA equivalent of the CCSS prereq
CA_FORWARD = "ca-7rp-a1"  # clean CA equivalent of the CCSS next
MS_E = "ms-6rp-a2"  # Multi-State crosswalk target of CA_C
MS_PREREQ = "ms-6rp-a1"
MS_FORWARD = "ms-7rp-a1"
COMP = "lc-unit-rate"


def _node(uid: str, code: str, desc: str, jur: str, grade: list[str]) -> dict[str, object]:
    return {
        "type": "node",
        "identifier": uid,
        "labels": ["StandardsFrameworkItem"],
        "properties": {
            "identifier": uid,
            "statementCode": code,
            "description": desc,
            "academicSubject": "Mathematics",
            "jurisdiction": jur,
            "gradeLevel": json.dumps(grade),
            "license": _LIC,
        },
    }


def _rel(label: str, source: str, target: str, **props: object) -> dict[str, object]:
    return {
        "type": "relationship",
        "identifier": f"{label}-{source}-{target}",
        "label": label,
        "properties": {"relationshipType": label, "license": _LIC, **props},
        "source_identifier": source,
        "source_labels": ["StandardsFrameworkItem"],
        "target_identifier": target,
        "target_labels": ["StandardsFrameworkItem"],
    }


def _write_fixture(src: Path) -> None:
    standards = [
        _node(CA_PARENT, "6.RP.A", "Understand ratio concepts and use ratio reasoning.",
              "California", ["6"]),
        # LaTeX ($a/b$) kept verbatim; the <b> tag stripped.
        _node(CA_C, "6.RP.A.2", "Understand the concept of a unit rate <b>$a/b$</b>.",
              "California", ["6"]),
        _node(CA_PREREQ, "6.RP.A.1", "Understand the concept of a ratio.", "California", ["6"]),
        _node(CA_FORWARD, "7.RP.A.1", "Compute unit rates with fractions.", "California", ["7"]),
        _node(MS_E, "6.RP.A.2", "CCSS unit rate.", "Multi-State", ["6"]),
        _node(MS_PREREQ, "6.RP.A.1", "CCSS ratio concept.", "Multi-State", ["6"]),
        _node(MS_FORWARD, "7.RP.A.1", "CCSS compute unit rates.", "Multi-State", ["7"]),
    ]

    hierarchy = [_rel("hasChild", CA_PARENT, CA_C)]

    progressions = [
        # buildsTowards: source = prereq/earlier, target = later. All Multi-State endpoints.
        _rel("buildsTowards", MS_PREREQ, MS_E),
        _rel("buildsTowards", MS_E, MS_FORWARD),
        # relatesTo must be skipped entirely.
        _rel("relatesTo", MS_E, MS_PREREQ),
    ]

    crosswalk = [
        # CA -> CCSS crosswalks. jaccard drives primary selection; clean reverse crosswalks
        # (exactly one CA per CCSS) let the bridge return CA equivalents.
        _rel("hasStandardAlignment", CA_C, MS_E, jaccard="1.0"),
        _rel("hasStandardAlignment", CA_PREREQ, MS_PREREQ, jaccard="1.0"),
        _rel("hasStandardAlignment", CA_FORWARD, MS_FORWARD, jaccard="1.0"),
    ]

    components = [
        {
            "type": "node",
            "identifier": COMP,
            "labels": ["LearningComponent"],
            "properties": {"identifier": COMP, "description": "Write a ratio a:b as a unit rate.",
                           "license": _LIC},
        },
        _rel("supports", COMP, CA_C),
    ]

    (src / "standards.jsonl").write_text("\n".join(json.dumps(r) for r in standards) + "\n")
    (src / "hierarchy.jsonl").write_text("\n".join(json.dumps(r) for r in hierarchy) + "\n")
    (src / "progressions.jsonl").write_text("\n".join(json.dumps(r) for r in progressions) + "\n")
    (src / "crosswalk.jsonl").write_text("\n".join(json.dumps(r) for r in crosswalk) + "\n")
    (src / "components.jsonl").write_text("\n".join(json.dumps(r) for r in components) + "\n")
    (src / "misconceptions.jsonl").write_text("")  # empty by design


def _build(tmp_path: Path) -> SqliteStandardsRepository:
    src = tmp_path / "ca-math"
    src.mkdir()
    _write_fixture(src)
    db = tmp_path / "test.db"
    build_database(src, db)
    return SqliteStandardsRepository(str(db))


def test_ca_standard_resolves_by_code(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        hits = repo.find_by_code("6.RP.A.2", academic_subject="Mathematics",
                                 jurisdiction="California")
        assert [s.code for s in hits] == ["6.RP.A.2"]
        std = hits[0]
        assert std.case_uuid == CA_C
        assert std.jurisdiction == "California"
        assert std.grade == "6"
        assert std.source == "Learning Commons KG v1.11.0"
        assert std.source_license == _LIC
        # LaTeX preserved verbatim; the <b> HTML tag stripped.
        assert "$a/b$" in std.statement_text
        assert "<b>" not in std.statement_text and "</b>" not in std.statement_text
    finally:
        repo.close()


def test_ca_backward_progression_is_bridged(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        back = repo.progression(CA_C, "backward")
        assert isinstance(back, Standard)
        # Clean reverse crosswalk -> the CA equivalent of the CCSS prerequisite.
        assert back.case_uuid == CA_PREREQ
        assert back.code == "6.RP.A.1"
    finally:
        repo.close()


def test_ca_forward_progression_is_bridged(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        forward = repo.progression(CA_C, "forward")
        assert isinstance(forward, Standard)
        assert forward.case_uuid == CA_FORWARD
        assert forward.code == "7.RP.A.1"
    finally:
        repo.close()


def test_direct_multistate_progression(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        # Multi-State nodes carry the direct buildsTowards edges.
        assert repo.progression(MS_E, "backward") is not None
        assert repo.progression(MS_E, "backward").case_uuid == MS_PREREQ  # type: ignore[union-attr]
        assert repo.progression(MS_PREREQ, "forward").case_uuid == MS_E  # type: ignore[union-attr]
    finally:
        repo.close()


def test_components_present_and_ordered(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        comps = repo.learning_components(CA_C)
        assert [c.description for c in comps] == ["Write a ratio a:b as a unit rate."]
        assert comps[0].ordinal == 1
    finally:
        repo.close()


def test_substandards_via_parent(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        children = repo.children_of(CA_PARENT)
        assert [c.case_uuid for c in children] == [CA_C]
    finally:
        repo.close()


def test_relatesto_not_mapped_to_direction(tmp_path: Path) -> None:
    repo = _build(tmp_path)
    try:
        # relatesTo(MS_E -> MS_PREREQ) must NOT create a backward/forward edge on MS_E beyond
        # the real buildsTowards ones (backward=MS_PREREQ from buildsTowards, forward=MS_FORWARD).
        assert repo.progression(MS_E, "forward").case_uuid == MS_FORWARD  # type: ignore[union-attr]
    finally:
        repo.close()


def test_load_wires_through_repository(tmp_path: Path) -> None:
    # SqliteStandardsRepository.load(source) delegates to the ingester; no-arg stays a stub.
    src = tmp_path / "ca-math"
    src.mkdir()
    _write_fixture(src)
    repo = SqliteStandardsRepository(str(tmp_path / "load.db"))
    try:
        repo.load(str(src))
        assert repo.get_by_uuid(CA_C) is not None
        raised = False
        try:
            repo.load()
        except NotImplementedError:
            raised = True
        assert raised
    finally:
        repo.close()
