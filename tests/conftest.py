"""Shared fixture: a small California-math ``InMemoryStandardsRepository``.

Shape seeded (spec §8):
- a ``2.OA`` parent with children ``2.OA.A.1`` and ``2.OA.B.2`` (prefix + subStandards);
- a leaf ``6.RP.A.2`` with a backward progression to ``6.RP.A.1`` and a forward to
  ``7.RP.A.1``;
- one misconception + three learning components on ``6.RP.A.2``;
- six (out-of-order) learning components on ``2.OA.A.1`` to exercise the cap-at-5 + ordering;
- one non-math (ELA) standard to exercise the subject filter.
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest

from k12_toolkit.model import (
    LearningComponent,
    Misconception,
    Progression,
    Standard,
)
from k12_toolkit.repository import InMemoryStandardsRepository

# --- stable UUIDs (readable stand-ins for the LC node identifiers) ----------
U_2OA = "uuid-2oa"
U_2OA_A1 = "uuid-2oa-a1"
U_2OA_B2 = "uuid-2oa-b2"
U_6RP_A1 = "uuid-6rp-a1"
U_6RP_A2 = "uuid-6rp-a2"
U_7RP_A1 = "uuid-7rp-a1"
U_ELA = "uuid-rl-6-1"

MATH = "Mathematics"
ELA = "English Language Arts"
CA = "California"
_SRC = "learning-commons-export-v1.11.0"
_LIC = "CC BY 4.0"


def _std(
    uuid: str,
    code: str,
    text: str,
    subject: str = MATH,
    grade: str | None = None,
    parent: str | None = None,
) -> Standard:
    return Standard(
        case_uuid=uuid,
        code=code,
        statement_text=text,
        academic_subject=subject,
        jurisdiction=CA,
        grade=grade,
        parent_uuid=parent,
        source=_SRC,
        source_license=_LIC,
    )


@dataclass(frozen=True)
class Fixture:
    repo: InMemoryStandardsRepository


@pytest.fixture
def fx() -> Fixture:
    standards = [
        _std(U_2OA, "2.OA", "Represent and solve problems involving addition and subtraction.",
             grade="2"),
        _std(U_2OA_A1, "2.OA.A.1",
             "Use addition and subtraction within 100 to solve word problems.",
             grade="2", parent=U_2OA),
        _std(U_2OA_B2, "2.OA.B.2",
             "Fluently add and subtract within 20 using mental strategies.",
             grade="2", parent=U_2OA),
        _std(U_6RP_A1, "6.RP.A.1",
             "Understand the concept of a ratio and use ratio language.", grade="6"),
        _std(U_6RP_A2, "6.RP.A.2",
             "Understand the concept of a unit rate a/b associated with a ratio a:b.",
             grade="6"),
        _std(U_7RP_A1, "7.RP.A.1",
             "Compute unit rates associated with ratios of fractions.", grade="7"),
        _std(U_ELA, "RL.6.1", "Cite textual evidence to support analysis of the text.",
             subject=ELA, grade="6"),
    ]
    progressions = [
        Progression(from_uuid=U_6RP_A2, to_uuid=U_6RP_A1, direction="backward", source=_SRC),
        Progression(from_uuid=U_6RP_A2, to_uuid=U_7RP_A1, direction="forward", source=_SRC),
    ]
    misconceptions = [
        Misconception(
            case_uuid=U_6RP_A2,
            student_behavior="Adds the two quantities in a ratio instead of comparing them.",
            teacher_move="Use a double number line to show the multiplicative relationship.",
            source=_SRC,
        ),
    ]
    components = [
        # Three (in-order) components on the leaf.
        LearningComponent(U_6RP_A2, 1, "Interpret a ratio as a comparison of quantities.", _SRC),
        LearningComponent(U_6RP_A2, 2, "Compute a unit rate from a ratio.", _SRC),
        LearningComponent(U_6RP_A2, 3, "Apply unit rates to solve problems.", _SRC),
        # Six out-of-order components on 2.OA.A.1 to exercise ordering + cap-at-5.
        LearningComponent(U_2OA_A1, 3, "component-ord-3", _SRC),
        LearningComponent(U_2OA_A1, 1, "component-ord-1", _SRC),
        LearningComponent(U_2OA_A1, 5, "component-ord-5", _SRC),
        LearningComponent(U_2OA_A1, 2, "component-ord-2", _SRC),
        LearningComponent(U_2OA_A1, 6, "component-ord-6", _SRC),
        LearningComponent(U_2OA_A1, 4, "component-ord-4", _SRC),
    ]
    repo = InMemoryStandardsRepository(standards, progressions, misconceptions, components)
    return Fixture(repo=repo)
