"""Tests for the richest-representative dedup (D1), keyword-container drop (D2), and the
``code`` alternative to ``caseIdentifierUUID`` (D3).

These use small inline ``InMemoryStandardsRepository`` fixtures that deliberately carry
same-code duplicates (which the shared ``fx`` fixture does not), plus blank-code containers,
to exercise the paths the live grounding test exposed.
"""

from __future__ import annotations

from k12_toolkit.mcp.server import (
    find_learning_components_from_standard_impl,
    find_misconceptions_for_standard_impl,
    find_standard_statement_impl,
    find_standards_progression_from_standard_impl,
)
from k12_toolkit.model import (
    LearningComponent,
    Misconception,
    Progression,
    Standard,
)
from k12_toolkit.repository import (
    InMemoryStandardsRepository,
    dedupe_richest,
    richest_by_code,
)

_SRC = "learning-commons-export-v1.11.0"
_LIC = "CC BY 4.0"


def _std(
    uuid: str,
    code: str,
    text: str = "stmt",
    jurisdiction: str = "California",
    parent: str | None = None,
) -> Standard:
    return Standard(
        case_uuid=uuid,
        code=code,
        statement_text=text,
        academic_subject="Mathematics",
        jurisdiction=jurisdiction,
        grade="9-12",
        parent_uuid=parent,
        source=_SRC,
        source_license=_LIC,
    )


# ---------------------------------------------------------------------------
# D1 — same-code duplicates collapse to the richest node
# ---------------------------------------------------------------------------


def _split_richness_repo() -> InMemoryStandardsRepository:
    """One code (HSA-APR.A.1) with three nodes: a thin CA node that sorts FIRST by uuid, a
    rich CA node, and a rich Multi-State node. The rich CA node must win.
    """
    thin_ca = _std("a-thin-ca", "HSA-APR.A.1")  # 'a...' sorts first naively; carries no data
    rich_ca = _std("z-rich-ca", "HSA-APR.A.1")
    rich_ms = _std("m-rich-ms", "HSA-APR.A.1", jurisdiction="Multi-State")
    prereq = _std("prereq", "8.EE.A.1")
    nxt = _std("next", "HSA-APR.D.7")
    standards = [thin_ca, rich_ca, rich_ms, prereq, nxt]
    # Rich nodes carry the same amount of data; the CA one wins on the jurisdiction tiebreak.
    progressions = [
        Progression("z-rich-ca", "prereq", "backward", _SRC),
        Progression("z-rich-ca", "next", "forward", _SRC),
        Progression("m-rich-ms", "prereq", "backward", _SRC),
        Progression("m-rich-ms", "next", "forward", _SRC),
    ]
    components = [
        LearningComponent("z-rich-ca", 1, "add polynomials", _SRC),
        LearningComponent("z-rich-ca", 2, "multiply polynomials", _SRC),
        LearningComponent("m-rich-ms", 1, "add polynomials", _SRC),
        LearningComponent("m-rich-ms", 2, "multiply polynomials", _SRC),
    ]
    return InMemoryStandardsRepository(standards, progressions, [], components)


def test_dedup_returns_richest_not_first_by_uuid() -> None:
    repo = _split_richness_repo()
    result = find_standard_statement_impl(repo, code="HSA-APR.A.1")
    assert len(result["standards"]) == 1  # collapsed, not three
    entry = result["standards"][0]
    # The thin 'a-thin-ca' would win a naive sort; the rich CA node must be chosen instead.
    assert entry["caseIdentifierUUID"] == "z-rich-ca"


def test_dedup_prefers_california_on_richness_tie() -> None:
    repo = _split_richness_repo()
    winner = richest_by_code(repo, "HSA-APR.A.1")
    assert winner is not None
    assert winner.jurisdiction == "California"
    assert winner.case_uuid == "z-rich-ca"


def test_dedup_is_deterministic_across_calls() -> None:
    repo = _split_richness_repo()
    picks = {
        find_standard_statement_impl(repo, code="HSA-APR.A.1")["standards"][0][
            "caseIdentifierUUID"
        ]
        for _ in range(5)
    }
    assert picks == {"z-rich-ca"}  # stable, never flips to a thin sibling


def test_dedup_preserves_prefix_ordering() -> None:
    # A prefix query still returns one entry per distinct child code, in code order.
    a1 = _std("u-a1", "1.G.A.1")
    a2a = _std("u-a2a", "1.G.A.2")
    a2b = _std("u-a2b", "1.G.A.2")  # duplicate of A.2, no data -> collapses away
    repo = InMemoryStandardsRepository([a1, a2a, a2b], [], [], [])
    codes = [s["code"] for s in find_standard_statement_impl(repo, code="1.G")["standards"]]
    assert codes == ["1.G.A.1", "1.G.A.2"]


# ---------------------------------------------------------------------------
# D2 — keyword hits drop blank-code containers and lead with the richest leaf
# ---------------------------------------------------------------------------


def test_keyword_drops_blank_code_containers_and_ranks_richest_leaf() -> None:
    container = _std("c-container", "", "probability domain container")
    thin_leaf = _std("l-thin", "7.SP.C.6", "probability of compound events")
    rich_leaf = _std("l-rich", "7.SP.C.5", "approximate probability of a chance event")
    prereq = _std("p", "7.SP.C.1")
    standards = [container, thin_leaf, rich_leaf, prereq]
    progressions = [Progression("l-rich", "p", "backward", _SRC)]
    components = [LearningComponent("l-rich", 1, "estimate probability from data", _SRC)]
    repo = InMemoryStandardsRepository(standards, progressions, [], components)

    result = find_standard_statement_impl(repo, keywords=["probability"])
    codes = [s["code"] for s in result["standards"]]
    assert "" not in codes  # the blank-code container is gone
    assert codes[0] == "7.SP.C.5"  # richest leaf leads
    assert set(codes) == {"7.SP.C.5", "7.SP.C.6"}


# ---------------------------------------------------------------------------
# D3 — the dependent tools accept a bare `code` (no uuid threading)
# ---------------------------------------------------------------------------


def _code_addressable_repo() -> InMemoryStandardsRepository:
    thin = _std("rp2-thin", "6.RP.A.2")  # first by naive order, empty
    rich = _std("rp2-rich", "6.RP.A.2")
    prereq = _std("rp1", "6.RP.A.1")
    nxt = _std("rp3", "7.RP.A.1")
    standards = [thin, rich, prereq, nxt]
    progressions = [
        Progression("rp2-rich", "rp1", "backward", _SRC),
        Progression("rp2-rich", "rp3", "forward", _SRC),
    ]
    misconceptions = [Misconception("rp2-rich", "adds the quantities", "double number line", _SRC)]
    components = [LearningComponent("rp2-rich", 1, "compute a unit rate", _SRC)]
    return InMemoryStandardsRepository(standards, progressions, misconceptions, components)


def test_progression_by_code_reaches_rich_node() -> None:
    repo = _code_addressable_repo()
    back = find_standards_progression_from_standard_impl(
        repo, code="6.RP.A.2", direction="backward"
    )
    assert back["standard"]["code"] == "6.RP.A.1"
    fwd = find_standards_progression_from_standard_impl(repo, code="6.RP.A.2", direction="forward")
    assert fwd["standard"]["code"] == "7.RP.A.1"


def test_components_by_code_reaches_rich_node() -> None:
    repo = _code_addressable_repo()
    result = find_learning_components_from_standard_impl(repo, code="6.RP.A.2")
    assert result["learningComponents"] == ["compute a unit rate"]


def test_misconceptions_by_code_reaches_rich_node() -> None:
    repo = _code_addressable_repo()
    result = find_misconceptions_for_standard_impl(repo, code="6.RP.A.2")
    assert len(result["misconceptions"]) == 1
    assert result["misconceptions"][0]["student_behavior"] == "adds the quantities"


def test_uuid_still_wins_when_both_given() -> None:
    repo = _code_addressable_repo()
    # Pass the prereq's uuid explicitly with a contradictory code: the uuid must win.
    result = find_learning_components_from_standard_impl(
        repo, caseIdentifierUUID="rp1", code="6.RP.A.2"
    )
    assert result["learningComponents"] == []  # 6.RP.A.1 has no components; code path not used


def test_code_miss_returns_typed_empty() -> None:
    repo = _code_addressable_repo()
    assert find_learning_components_from_standard_impl(repo, code="9.ZZ.Z.9") == {
        "learningComponents": []
    }
    assert find_standards_progression_from_standard_impl(
        repo, code="9.ZZ.Z.9", direction="backward"
    ) == {"standard": None}


def test_dedupe_richest_helper_direct() -> None:
    repo = _split_richness_repo()
    survivors = dedupe_richest(repo, repo.find_by_code("HSA-APR.A.1"))
    assert [s.case_uuid for s in survivors] == ["z-rich-ca"]


# ---------------------------------------------------------------------------
# subStandards union — a child subtree held by a NON-representative placement is not dropped
# (review finding: dedup by grounding-richness ignored children, losing subStandards for "4.0")
# ---------------------------------------------------------------------------


def test_substandards_union_across_same_code_placements() -> None:
    # Two same-code parent placements of '4.0': the childless one sorts first by uuid and would
    # become the representative; its children (held by the sibling) must still be unioned in.
    parent_thin = _std("a-parent", "4.0")  # 'a...' sorts first; no children, no data
    parent_rich = _std("z-parent", "4.0")
    c1 = _std("c1", "4.1", parent="z-parent")
    c2 = _std("c2", "4.2", parent="z-parent")
    repo = InMemoryStandardsRepository([parent_thin, parent_rich, c1, c2], [], [], [])
    result = find_standard_statement_impl(repo, code="4.0")
    assert len(result["standards"]) == 1
    sub_codes = [s["code"] for s in result["standards"][0]["subStandards"]]
    # '4.1'/'4.2' do not start with '4.0.', so only the union (not the prefix) can surface them.
    assert sub_codes == ["4.1", "4.2"]


# ---------------------------------------------------------------------------
# Per-facet resolution — a bare `code` reaches the sibling that holds THIS tool's datum,
# even when a DIFFERENT sibling is richer overall (review findings 1 + 5).
# ---------------------------------------------------------------------------


def test_progression_by_code_reaches_directional_edge_on_sibling() -> None:
    # '6.RP.A.2' split: node A carries FORWARD + a component (richer overall); node B carries
    # only the BACKWARD edge. A backward lookup must reach B, not be shadowed by A.
    a_fwd = _std("a-fwd", "6.RP.A.2")
    b_back = _std("b-back", "6.RP.A.2")
    prereq = _std("rp1", "6.RP.A.1")
    nxt = _std("rp3", "7.RP.A.1")
    progressions = [
        Progression("a-fwd", "rp3", "forward", _SRC),
        Progression("b-back", "rp1", "backward", _SRC),
    ]
    components = [LearningComponent("a-fwd", 1, "unit rate", _SRC)]
    repo = InMemoryStandardsRepository([a_fwd, b_back, prereq, nxt], progressions, [], components)
    back = find_standards_progression_from_standard_impl(
        repo, code="6.RP.A.2", direction="backward"
    )
    assert back["standard"]["code"] == "6.RP.A.1"
    fwd = find_standards_progression_from_standard_impl(repo, code="6.RP.A.2", direction="forward")
    assert fwd["standard"]["code"] == "7.RP.A.1"


def test_misconceptions_by_code_reaches_sibling() -> None:
    # Reviewer's repro: progression+component on 'a-prog' (richest), the misconception on 'z-misc'.
    a_prog = _std("a-prog", "6.RP.A.3")
    z_misc = _std("z-misc", "6.RP.A.3")
    pre = _std("pre", "6.RP.A.2")
    progressions = [Progression("a-prog", "pre", "backward", _SRC)]
    components = [LearningComponent("a-prog", 1, "comp", _SRC)]
    misconceptions = [Misconception("z-misc", "adds the quantities", "double number line", _SRC)]
    repo = InMemoryStandardsRepository(
        [a_prog, z_misc, pre], progressions, misconceptions, components
    )
    result = find_misconceptions_for_standard_impl(repo, code="6.RP.A.3")
    assert len(result["misconceptions"]) == 1
    assert result["misconceptions"][0]["student_behavior"] == "adds the quantities"


def test_components_by_code_reaches_sibling() -> None:
    # 'R' is richer overall (backward + forward, no components); 'C' holds the components.
    r_node = _std("r-edges", "8.EE.A.1")
    c_node = _std("c-comps", "8.EE.A.1")
    pre = _std("pre2", "7.EE.B.4")
    nxt2 = _std("nxt2", "8.EE.A.2")
    progressions = [
        Progression("r-edges", "pre2", "backward", _SRC),
        Progression("r-edges", "nxt2", "forward", _SRC),
    ]
    components = [
        LearningComponent("c-comps", 1, "cc1", _SRC),
        LearningComponent("c-comps", 2, "cc2", _SRC),
    ]
    repo = InMemoryStandardsRepository([r_node, c_node, pre, nxt2], progressions, [], components)
    result = find_learning_components_from_standard_impl(repo, code="8.EE.A.1")
    assert result["learningComponents"] == ["cc1", "cc2"]


# ---------------------------------------------------------------------------
# academicSubject / jurisdiction matching is case-insensitive, with a code-only fallback
# (follow-up test: lowercase 'mathematics' silently emptied a filtered resolve).
# ---------------------------------------------------------------------------


def test_academic_subject_match_is_case_insensitive() -> None:
    repo = InMemoryStandardsRepository([_std("u1", "6.RP.A.2")], [], [], [])  # subject Mathematics
    lower = find_standard_statement_impl(repo, code="6.RP.A.2", academicSubject="mathematics")
    upper = find_standard_statement_impl(repo, code="6.RP.A.2", academicSubject="Mathematics")
    assert [x["code"] for x in lower["standards"]] == ["6.RP.A.2"]
    assert lower["standards"] == upper["standards"]


def test_keyword_subject_match_is_case_insensitive() -> None:
    s = _std("u1", "7.SP.C.5", "approximate the probability of a chance event")
    repo = InMemoryStandardsRepository([s], [], [], [])
    res = find_standard_statement_impl(
        repo, keywords=["probability"], academicSubject="mathematics"
    )
    assert [x["code"] for x in res["standards"]] == ["7.SP.C.5"]


def test_code_resolve_falls_back_when_subject_filter_empties() -> None:
    repo = InMemoryStandardsRepository([_std("u1", "6.RP.A.2")], [], [], [])  # subject Mathematics
    # A subject the store does not carry would empty a filtered resolve; fall back to code alone.
    res = find_standard_statement_impl(repo, code="6.RP.A.2", academicSubject="Science")
    assert [x["code"] for x in res["standards"]] == ["6.RP.A.2"]
