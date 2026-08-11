"""Domain entities for the CASE-shaped standards store.

Four immutable entities, one store. ``case_uuid`` adopts the Learning Commons node
``identifier`` (stable graph ids), so it satisfies the skills' ``caseIdentifierUUID``
contract directly with no minting. Every record carries ``source`` + ``source_license``
for attribution compliance.

See ``docs/superpowers/specs/2026-07-22-standards-resource-design.md`` §4.
"""

from __future__ import annotations

from dataclasses import dataclass

# Progression edge directions.
BACKWARD = "backward"  # prerequisite
FORWARD = "forward"  # next standard


@dataclass(frozen=True, slots=True)
class Standard:
    """A single academic standard (a node in the CASE graph).

    ``parent_uuid`` (nullable) builds the ``subStandards`` tree: a standard whose
    ``parent_uuid`` points at another standard is one of that standard's children.
    """

    case_uuid: str
    code: str
    statement_text: str
    academic_subject: str
    jurisdiction: str
    grade: str | None
    parent_uuid: str | None
    source: str
    source_license: str


@dataclass(frozen=True, slots=True)
class Progression:
    """A directed prerequisite/next edge between two standards (math-only by design).

    ``direction`` is one of ``"backward"`` (prerequisite) or ``"forward"`` (next).
    """

    from_uuid: str
    to_uuid: str
    direction: str
    source: str


@dataclass(frozen=True, slots=True)
class Misconception:
    """A common student misconception plus the teacher move that addresses it."""

    case_uuid: str
    student_behavior: str
    teacher_move: str
    source: str


@dataclass(frozen=True, slots=True)
class LearningComponent:
    """A sub-skill component of a standard, ordered by ``ordinal``."""

    case_uuid: str
    ordinal: int
    description: str
    source: str


@dataclass(frozen=True, slots=True)
class CurriculumLesson:
    """A published curriculum lesson (or lesson grouping) aligned to a standard.

    ``source_license`` and ``attribution`` are carried per record rather than assumed
    globally, because the export's attribution string varies by node type and provider.
    A consumer that reproduces any of this owes the record's own string, not a general one.
    """

    lesson_id: str
    name: str
    description: str | None
    author: str | None
    entity: str
    course_code: str | None
    curriculum_label: str | None
    ordinal_name: str | None
    grade: str | None
    source_license: str
    attribution: str
    # NULL when the export aligns this lesson to the queried standard directly. Otherwise the
    # Multi-State CCSS standard it was reached through. The curriculum aligns only to
    # Multi-State nodes, so without that bridge a state's own standards return nothing at all.
    bridged_from: str | None = None


@dataclass(frozen=True, slots=True)
class LessonMaterial:
    """An activity or assessment that is part of a lesson."""

    lesson_id: str
    material_id: str
    name: str
    description: str | None
    entity: str
    ordinal_name: str | None
    educational_use: str | None
    is_optional: str | None
    source_license: str
    attribution: str
