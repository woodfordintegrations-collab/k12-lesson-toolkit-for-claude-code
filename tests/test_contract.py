"""Contract tests: exercise the tool ``*_impl`` handlers directly against the fixture repo.

These assert the documented response shapes (spec §3) without spinning a full MCP client.
"""

from __future__ import annotations

from k12_toolkit.mcp.server import (
    MAX_LEARNING_COMPONENTS,
    find_curriculum_lessons_impl,
    find_learning_components_from_standard_impl,
    find_materials_for_lesson_impl,
    find_misconceptions_for_standard_impl,
    find_standard_statement_impl,
    find_standards_progression_from_standard_impl,
    list_standards_for_mathematical_practice_impl,
)
from k12_toolkit.model import Standard
from k12_toolkit.repository import InMemoryStandardsRepository
from tests.conftest import (
    U_2OA,
    U_2OA_A1,
    U_6RP_A1,
    U_6RP_A2,
    U_7RP_A1,
    Fixture,
)

# --- find_standard_statement -------------------------------------------------


def test_prefix_search_returns_parent_and_children(fx: Fixture) -> None:
    result = find_standard_statement_impl(fx.repo, code="2.OA")
    codes = [s["code"] for s in result["standards"]]
    assert codes == ["2.OA", "2.OA.A.1", "2.OA.B.2"]  # parent + both children, sorted


def test_leaf_search_returns_just_the_leaf(fx: Fixture) -> None:
    result = find_standard_statement_impl(fx.repo, code="6.RP.A.2")
    assert len(result["standards"]) == 1
    entry = result["standards"][0]
    assert entry["code"] == "6.RP.A.2"
    assert entry["caseIdentifierUUID"] == U_6RP_A2
    assert "unit rate" in entry["statement_text"]
    assert entry["subStandards"] == []  # a leaf has no children


def test_substandards_populated_on_parent(fx: Fixture) -> None:
    result = find_standard_statement_impl(fx.repo, code="2.OA")
    parent = next(s for s in result["standards"] if s["code"] == "2.OA")
    sub_codes = [c["code"] for c in parent["subStandards"]]
    assert sub_codes == ["2.OA.A.1", "2.OA.B.2"]
    # subStandards carry the brief shape (code, statement_text, caseIdentifierUUID).
    assert parent["subStandards"][0]["caseIdentifierUUID"] == U_2OA_A1
    assert set(parent["subStandards"][0]) == {"code", "statement_text", "caseIdentifierUUID"}


def test_keyword_or_match_case_insensitive_and_subject_filtered(fx: Fixture) -> None:
    # OR-match: "RATIO" (uppercase) hits three math standards; the bogus term hits none;
    # the ELA standard is excluded by the subject filter even though it has other words.
    result = find_standard_statement_impl(
        fx.repo, keywords=["RATIO", "zzz-nomatch"], academicSubject="Mathematics"
    )
    codes = {s["code"] for s in result["standards"]}
    assert codes == {"6.RP.A.1", "6.RP.A.2", "7.RP.A.1"}


def test_code_miss_returns_empty(fx: Fixture) -> None:
    assert find_standard_statement_impl(fx.repo, code="9.ZZ")["standards"] == []


def test_no_code_no_keywords_returns_empty(fx: Fixture) -> None:
    assert find_standard_statement_impl(fx.repo)["standards"] == []


# --- find_standards_progression_from_standard --------------------------------


def test_progression_backward(fx: Fixture) -> None:
    result = find_standards_progression_from_standard_impl(fx.repo, U_6RP_A2, "backward")
    assert result["standard"]["code"] == "6.RP.A.1"
    assert result["standard"]["caseIdentifierUUID"] == U_6RP_A1


def test_progression_forward(fx: Fixture) -> None:
    result = find_standards_progression_from_standard_impl(fx.repo, U_6RP_A2, "forward")
    assert result["standard"]["code"] == "7.RP.A.1"
    assert result["standard"]["caseIdentifierUUID"] == U_7RP_A1


def test_progression_unknown_uuid_returns_null(fx: Fixture) -> None:
    assert find_standards_progression_from_standard_impl(
        fx.repo, "nope", "backward"
    ) == {"standard": None}


def test_progression_bad_direction_returns_null(fx: Fixture) -> None:
    assert find_standards_progression_from_standard_impl(
        fx.repo, U_6RP_A2, "sideways"
    ) == {"standard": None}


def test_progression_missing_edge_returns_null(fx: Fixture) -> None:
    # 2.OA has no progression edges.
    assert find_standards_progression_from_standard_impl(
        fx.repo, U_2OA, "backward"
    ) == {"standard": None}


# --- find_misconceptions_for_standard ----------------------------------------


def test_misconceptions_shape(fx: Fixture) -> None:
    result = find_misconceptions_for_standard_impl(fx.repo, U_6RP_A2, subject="Mathematics")
    assert len(result["misconceptions"]) == 1
    m = result["misconceptions"][0]
    assert set(m) == {"student_behavior", "teacher_move"}
    assert m["student_behavior"].startswith("Adds the two quantities")


def test_misconceptions_unknown_uuid_empty(fx: Fixture) -> None:
    assert find_misconceptions_for_standard_impl(fx.repo, "nope") == {"misconceptions": []}


# --- find_learning_components_from_standard ----------------------------------


def test_learning_components_ordered_and_capped(fx: Fixture) -> None:
    # 2.OA.A.1 has six components with out-of-order ordinals; expect first five, in order.
    result = find_learning_components_from_standard_impl(fx.repo, U_2OA_A1)
    comps = result["learningComponents"]
    assert len(comps) == MAX_LEARNING_COMPONENTS == 5
    assert comps == [
        "component-ord-1",
        "component-ord-2",
        "component-ord-3",
        "component-ord-4",
        "component-ord-5",
    ]


def test_learning_components_three_ordered(fx: Fixture) -> None:
    result = find_learning_components_from_standard_impl(fx.repo, U_6RP_A2)
    comps = result["learningComponents"]
    assert len(comps) == 3
    assert comps[0].startswith("Interpret a ratio")


def test_learning_components_unknown_uuid_empty(fx: Fixture) -> None:
    assert find_learning_components_from_standard_impl(fx.repo, "nope") == {
        "learningComponents": []
    }


# --- curriculum tools, and the one remaining stub -----------------------------


def test_curriculum_lessons_empty_without_uuid(fx) -> None:
    """No uuid means no answer, rather than the whole corpus."""
    assert find_curriculum_lessons_impl(fx.repo, caseIdentifierUUID="") == {"lessons": []}


def test_curriculum_lessons_unknown_uuid_is_empty(fx) -> None:
    assert find_curriculum_lessons_impl(fx.repo, caseIdentifierUUID="no-such-uuid") == {
        "lessons": []
    }


def test_curriculum_tools_tolerate_a_store_without_the_layer(fx) -> None:
    """The in-memory fixture store has no curriculum layer at all.

    A store built before scripts/extract_curriculum.py existed must degrade to empty rather
    than raise, because the skills forbid surfacing an error to a teacher.
    """
    assert find_curriculum_lessons_impl(fx.repo, caseIdentifierUUID="anything") == {"lessons": []}
    assert find_materials_for_lesson_impl(fx.repo, lessonIdentifier="anything") == {
        "materials": []
    }


def test_materials_empty_without_lesson_id(fx) -> None:
    assert find_materials_for_lesson_impl(fx.repo, lessonIdentifier="") == {"materials": []}


# --- list_standards_for_mathematical_practice --------------------------------
# Was a registered stub whose test asserted it returned []. The stub was justified by the
# consumer ("the skills never read this list") rather than by the data, and the data -- MP1
# through MP8 with their full statements -- was in the shipped export the whole time.


def _smp_repo() -> InMemoryStandardsRepository:
    """MP1-MP8 as the export actually holds them: once per jurisdiction, same text."""
    practices = [
        Standard(case_uuid=f"mp-{jur[:2].lower()}-{n}", code=f"MP{n}",
                 statement_text=f"practice {n} statement", academic_subject="Mathematics",
                 jurisdiction=jur, grade=None, parent_uuid=None, source="test",
                 source_license="https://creativecommons.org/licenses/by/4.0/")
        for n in range(1, 9)
        for jur in ("Multi-State", "California")
    ]
    decoy = Standard(case_uuid="not-a-practice", code="MPX9",
                     statement_text="not a practice code", academic_subject="Mathematics",
                     jurisdiction="California", grade=None, parent_uuid=None, source="test",
                     source_license="lic")
    return InMemoryStandardsRepository([*practices, decoy], [], [], [])


def test_smp_returns_the_eight_practices_once_each() -> None:
    entries = list_standards_for_mathematical_practice_impl(
        _smp_repo())["standardsForMathematicalPractice"]
    assert [e["statementCode"] for e in entries] == [f"MP{n}" for n in range(1, 9)]
    assert all(e["statementText"] for e in entries), "every practice carries its statement"
    assert all(e["license"] for e in entries), "licence travels with every row"


def test_smp_prefers_the_adopting_state_over_the_multi_state_copy() -> None:
    """A teacher owes their own state's attribution, not the Multi-State record's."""
    entries = list_standards_for_mathematical_practice_impl(
        _smp_repo())["standardsForMathematicalPractice"]
    assert {e["jurisdiction"] for e in entries} == {"California"}


def test_smp_ignores_codes_that_merely_begin_with_mp() -> None:
    """`code LIKE 'MP%'` alone would sweep in anything else starting MP."""
    entries = list_standards_for_mathematical_practice_impl(
        _smp_repo())["standardsForMathematicalPractice"]
    assert "MPX9" not in [e["statementCode"] for e in entries]


def test_smp_on_a_subject_without_practices_is_empty(fx: Fixture) -> None:
    """The default fixture holds no MP codes; [] is then the right answer, not a stub."""
    assert list_standards_for_mathematical_practice_impl(fx.repo) == {
        "standardsForMathematicalPractice": []
    }
