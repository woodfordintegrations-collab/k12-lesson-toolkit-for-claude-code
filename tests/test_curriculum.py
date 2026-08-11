"""The curriculum layer: the join, its dedup, and the key mismatch that broke it twice.

This join returned an empty list twice during development, both times because two identifier
spaces were confused, and both times the empty result raised nothing and looked exactly like
"the curriculum data does not exist in the public export" -- which is the false conclusion
this project carried for three weeks.

So the first test here is a control. If the fixture's alignment rows stop matching the
fixture's standards, every other assertion in this module becomes vacuously true, and the
control is what fails instead of the suite going quietly green.
"""

from __future__ import annotations

import sqlite3

import pytest

from k12_toolkit.ingest.builder import _bridged_alignments
from k12_toolkit.mcp.server import (
    find_curriculum_lessons_impl,
    find_materials_for_lesson_impl,
)
from k12_toolkit.repository import SqliteStandardsRepository

STD = "std-uuid-1"
OTHER = "std-uuid-2"
LIC = "https://creativecommons.org/licenses/by/4.0/"
ATTR = "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license."


@pytest.fixture
def repo(tmp_path):
    r = SqliteStandardsRepository(str(tmp_path / "t.db"))
    r.create_schema()
    c: sqlite3.Connection = r._conn
    c.executemany(
        "INSERT INTO curriculum_lessons VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        [
            ("L1", "Proving the Pythagorean Theorem", "d", "Illustrative Mathematics",
             "Lesson", "im360:Geo", "Unit 3", "Lesson 11", "9-12", LIC, ATTR),
            ("L2", "Angles and Steepness", "d", "Illustrative Mathematics",
             "Lesson", "im360:Geo", "Unit 4", "Lesson 1", "9-12", LIC, ATTR),
            ("L3", "Someone Else's Lesson", "d", "Other Publisher",
             "Lesson", "xx:1", "Unit 1", "Lesson 1", "9-12", LIC, ATTR),
        ],
    )
    c.executemany(
        "INSERT INTO lesson_alignments VALUES (?,?,?,?,?)",
        [
            # L1 aligns to STD twice, through two different edges. This is the real shape
            # of the export and the reason the query groups rather than joining plainly.
            (STD, "L1", "teaches", "addressing", None),
            (STD, "L1", "buildsToward", "building_toward", None),
            (STD, "L2", "buildsToward", "building_toward", None),
            (STD, "L3", "teaches", "addressing", None),
            (OTHER, "L2", "teaches", "addressing", None),
        ],
    )
    c.executemany(
        "INSERT INTO lesson_materials VALUES (?,?,?,?,?,?,?,?,?,?)",
        [
            ("L1", "A1", "Notice and Wonder", "d", "Activity", "Activity 1", "instruction",
             "False", LIC, ATTR),
            ("L1", "A2", "Cool-down", "d", "Activity", "Activity 2", "instruction",
             "True", LIC, ATTR),
            ("L1", "S1", "End of Unit Assessment", "d", "Assessment", "Assessment 1",
             "assessment", "False", LIC, ATTR),
        ],
    )
    c.commit()
    return r


def test_control_the_fixture_actually_joins(repo):
    """Without this, an identifier-space mistake makes every test below pass on empty."""
    out = find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD)
    assert out["lessons"], "the fixture's alignments no longer reach its lessons"


def test_a_lesson_aligned_twice_appears_once(repo):
    out = find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD)
    ids = [entry["lessonIdentifier"] for entry in out["lessons"]]
    assert len(ids) == len(set(ids)), f"duplicate lessons in the result: {ids}"
    assert ids.count("L1") == 1


def test_teaches_outranks_builds_toward(repo):
    """A lesson that teaches the standard must come before one that builds toward it."""
    out = find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD,
                                       author="Illustrative Mathematics")
    assert [e["lessonIdentifier"] for e in out["lessons"]] == ["L1", "L2"]


def test_author_filter_excludes_other_publishers(repo):
    out = find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD,
                                       author="Illustrative Mathematics")
    assert "L3" not in [e["lessonIdentifier"] for e in out["lessons"]]


def test_unknown_standard_is_empty_not_everything(repo):
    assert find_curriculum_lessons_impl(repo, caseIdentifierUUID="nope") == {"lessons": []}


def test_licence_and_attribution_travel_with_every_row(repo):
    """Dropping these would make the reuse obligation invisible downstream."""
    for entry in find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD)["lessons"]:
        assert entry["license"] == LIC
        assert entry["attributionStatement"] == ATTR
    for m in find_materials_for_lesson_impl(repo, lessonIdentifier="L1")["materials"]:
        assert m["license"] == LIC and m["attributionStatement"] == ATTR


def test_materials_come_back_in_order(repo):
    out = find_materials_for_lesson_impl(repo, lessonIdentifier="L1")
    assert [m["materialIdentifier"] for m in out["materials"]] == ["A1", "A2", "S1"]


def test_material_source_filter(repo):
    only_act = find_materials_for_lesson_impl(repo, lessonIdentifier="L1",
                                              materialSource=["activity"])
    assert {m["materialSource"] for m in only_act["materials"]} == {"activity"}
    only_ass = find_materials_for_lesson_impl(repo, lessonIdentifier="L1",
                                              materialSource=["assessment"])
    assert {m["materialSource"] for m in only_ass["materials"]} == {"assessment"}


# --- the crosswalk bridge -----------------------------------------------------
# Measured on the v1.11.0 export: all 561 standards carrying a curriculum alignment are
# Multi-State CCSS nodes and ZERO are California's. Built and unbridged, these two tools
# answered every lookup of a state's own standard with an empty list -- indistinguishable
# from "no lessons exist for this standard", which is the failure this module opens on.


def _crosswalk(*edges: tuple[str, str, str]) -> list[dict]:
    return [{"source_identifier": s, "target_identifier": t, "properties": {"jaccard": j}}
            for s, t, j in edges]


def test_a_state_standard_inherits_its_ccss_twins_lessons() -> None:
    direct = [("ccss-1", "L1", "teaches", "addressing", None)]
    bridged = _bridged_alignments(_crosswalk(("ca-1", "ccss-1", "0.9")), direct)
    assert bridged == [("ca-1", "L1", "teaches", "addressing", "ccss-1")]


def test_a_bridged_row_records_what_it_came_through() -> None:
    """A caller must be able to tell an inferred alignment from a stated one."""
    bridged = _bridged_alignments(
        _crosswalk(("ca-1", "ccss-1", "0.9")), [("ccss-1", "L1", "teaches", None, None)])
    assert bridged[0][4] == "ccss-1"


def test_a_standard_with_its_own_alignments_is_not_overwritten() -> None:
    direct = [("ca-1", "L9", "teaches", None, None), ("ccss-1", "L1", "teaches", None, None)]
    bridged = _bridged_alignments(_crosswalk(("ca-1", "ccss-1", "0.9")), direct)
    assert bridged == [], "a stated alignment must win over an inferred one"


def test_the_highest_jaccard_neighbour_with_curriculum_wins() -> None:
    direct = [("ccss-weak", "L-weak", "teaches", None, None),
              ("ccss-strong", "L-strong", "teaches", None, None)]
    bridged = _bridged_alignments(
        _crosswalk(("ca-1", "ccss-weak", "0.2"), ("ca-1", "ccss-strong", "0.8")), direct)
    assert [row[1] for row in bridged] == ["L-strong"]


def test_a_neighbour_without_curriculum_is_skipped_not_treated_as_a_dead_end() -> None:
    """Ordering by jaccard alone would stop at the best neighbour even when it has nothing."""
    direct = [("ccss-has", "L1", "teaches", None, None)]
    bridged = _bridged_alignments(
        _crosswalk(("ca-1", "ccss-empty", "0.9"), ("ca-1", "ccss-has", "0.3")), direct)
    assert [row[1] for row in bridged] == ["L1"]


def test_only_one_neighbour_is_inherited_from() -> None:
    """Otherwise a standard crosswalked to three CCSS nodes inherits three curricula at once."""
    direct = [("ccss-a", "La", "teaches", None, None), ("ccss-b", "Lb", "teaches", None, None)]
    bridged = _bridged_alignments(
        _crosswalk(("ca-1", "ccss-a", "0.9"), ("ca-1", "ccss-b", "0.8")), direct)
    assert [row[1] for row in bridged] == ["La"]


def test_the_tool_marks_bridged_lessons_and_leaves_direct_ones_unmarked(repo) -> None:
    conn = repo._conn
    conn.execute("INSERT INTO lesson_alignments VALUES (?,?,?,?,?)",
                 ("bridged-std", "L2", "teaches", "addressing", "ccss-source"))
    conn.commit()
    bridged = find_curriculum_lessons_impl(repo, caseIdentifierUUID="bridged-std")["lessons"]
    assert bridged and bridged[0]["alignedVia"] == "ccss-source"
    for entry in find_curriculum_lessons_impl(repo, caseIdentifierUUID=STD)["lessons"]:
        assert "alignedVia" not in entry, "a stated alignment must not look inferred"


def test_unrecognised_material_source_returns_nothing(repo):
    """Filtering to nothing beats silently widening to everything.

    A caller who asks for a source we do not model should get an empty list, not the whole
    lesson, because they cannot tell the difference between "no such material" and "here is
    material you did not ask for".
    """
    out = find_materials_for_lesson_impl(repo, lessonIdentifier="L1",
                                         materialSource=["nonsense"])
    assert out == {"materials": []}
