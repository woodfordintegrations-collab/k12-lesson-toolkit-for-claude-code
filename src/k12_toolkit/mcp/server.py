"""The 7-tool stdio MCP server reproducing the Learning Commons Knowledge Graph contract.

The forked ``k12-teacher-skills`` plugin detects the connector purely by **tool
availability** (Step 0.3 probes whether ``find_standard_statement`` is registered), so this
server registers all seven tool names and implements them to the depth the skills consume.

Design:

- Every tool is a **total function**: on any miss or bad input it returns an empty/typed-empty
  result and NEVER raises. The skills forbid surfacing errors to teachers.
- Tool handlers contain no business logic beyond shaping repository results into the contract
  response. All response shaping lives in the clearly-marked section below so the field names
  can be reconciled later against the real LC export.
- The server depends only on the :class:`StandardsRepository` protocol; the concrete store is
  injected (:func:`build_server`) or built from the ``K12_TOOLKIT_DB`` env var (:func:`main`).

NOTE ON FIELD NAMES: the exact JSON field names of the real Learning Commons connector are
NOT pinned by the KG docs. The names below (``statement_text``, ``caseIdentifierUUID``,
``subStandards``, ``student_behavior``, ``teacher_move``, ``learningComponents`` …) are
reasonable defaults derived from the extracted contract (spec §3) and the fields the skills
hard-require (``shared.standard_code`` ← ``code``, ``shared.standard_text`` ← statement text).
Reconcile against the real export when it lands; change only this section.
"""

from __future__ import annotations

import functools
import os
import sys
from collections.abc import Callable
from typing import Any

from mcp.server.fastmcp import FastMCP

from k12_toolkit.model import BACKWARD, FORWARD, Standard
from k12_toolkit.repository import (
    FacetScore,
    SqliteStandardsRepository,
    StandardsRepository,
    dedupe_richest,
    select_by_code,
)

# Default sqlite store location if K12_TOOLKIT_DB is unset.
DEFAULT_DB_PATH = "standards.db"

# Contract caps (spec §3).
MAX_LEARNING_COMPONENTS = 5
# The skills select ONE lesson from this list and then fetch its materials, so a long list
# is context spent for nothing. Ranked most-directly-taught first, so the cap keeps the
# lessons that actually teach the standard.
MAX_CURRICULUM_LESSONS = 10
MAX_LESSON_MATERIALS = 25
# A keyword/topic search returns the richest matches, not the full corpus — grounding needs the
# best leaf, not hundreds. This also bounds the per-result subStandards union work.
MAX_KEYWORD_RESULTS = 25
_VALID_DIRECTIONS = frozenset({BACKWARD, FORWARD})

# ---------------------------------------------------------------------------
# RESPONSE SHAPING  (single source of contract field names — reconcile here)
# ---------------------------------------------------------------------------


def _brief(std: Standard) -> dict[str, str]:
    """The minimal standard shape shared by several tool responses."""
    return {
        "code": std.code,
        "statement_text": std.statement_text,
        "caseIdentifierUUID": std.case_uuid,
    }


def _resolve_uuid(
    repo: StandardsRepository, uuid: str, code: str | None, facet_score: FacetScore
) -> str:
    """A caller may pass a ``caseIdentifierUUID`` OR a bare ``code``.

    A non-empty uuid wins (the real connector's contract); otherwise a ``code`` resolves to the
    same-code node richest in THIS tool's facet (:func:`select_by_code`), so a caller that never
    threads a uuid still reaches the datum even when it lives on a non-representative placement.
    This removes the two-step resolve-then-call dependency that weaker models fumble.
    """
    if uuid:
        return uuid
    if code:
        rep = select_by_code(repo, code, facet_score)
        if rep is not None:
            return rep.case_uuid
    return ""


def _sub_standards(
    repo: StandardsRepository,
    std: Standard,
    academic_subject: str | None,
    jurisdiction: str | None,
    cache: dict[str, int],
) -> list[dict[str, str]]:
    """Union the children across ALL same-code placements (a placement's children can differ),
    deduped to one per child code, so subStandards never drops a sub-part held by a sibling.
    """
    same_code = [
        n for n in repo.find_by_code(std.code, academic_subject, jurisdiction) if n.code == std.code
    ]
    children: list[Standard] = []
    for node in same_code:
        children.extend(repo.children_of(node.case_uuid))
    return [_brief(child) for child in dedupe_richest(repo, children, cache=cache)]


def find_standard_statement_impl(
    repo: StandardsRepository,
    code: str | None = None,
    keywords: list[str] | None = None,
    academicSubject: str | None = None,
    jurisdiction: str | None = None,
) -> dict[str, Any]:
    """Prefix-code search (if ``code`` given) else keyword OR-search, with subStandards.

    Same-code duplicates collapse to the richest node per code (:func:`dedupe_richest`), so
    grounding never lands on an empty placement when a rich sibling exists. Keyword hits drop
    blank-code container nodes and lead with the richest leaf. subStandards union the children
    across all same-code placements.
    """
    cache: dict[str, int] = {}
    if code:
        found = repo.find_by_code(code, academicSubject, jurisdiction)
        if not found and (academicSubject or jurisdiction):
            # A subject/jurisdiction filter emptied an otherwise-valid code (e.g. a casing or
            # vocabulary mismatch): resolve on the code alone rather than silently return empty.
            found = repo.find_by_code(code)
        standards = dedupe_richest(repo, found, cache=cache)
    elif keywords:
        hits = [
            s
            for s in repo.search_by_keywords(keywords, academicSubject, jurisdiction)
            if s.code
        ]
        standards = dedupe_richest(repo, hits, order_by_richness=True, cache=cache)[
            :MAX_KEYWORD_RESULTS
        ]
    else:
        standards = []

    shaped: list[dict[str, Any]] = []
    for std in standards:
        entry: dict[str, Any] = _brief(std)
        entry["subStandards"] = _sub_standards(repo, std, academicSubject, jurisdiction, cache)
        shaped.append(entry)
    return {"standards": shaped}


def find_standards_progression_from_standard_impl(
    repo: StandardsRepository,
    caseIdentifierUUID: str = "",
    direction: str = "",
    code: str | None = None,
) -> dict[str, Any]:
    """Follow the single primary prerequisite/next edge. Math-only by design.

    Accepts a ``code`` in place of ``caseIdentifierUUID``; the code resolves to the same-code
    node that actually carries an edge in ``direction`` (a prerequisite and a next standard can
    live on different placements).
    """
    if direction not in _VALID_DIRECTIONS:
        return {"standard": None}
    uuid = _resolve_uuid(
        repo,
        caseIdentifierUUID,
        code,
        lambda r, s: 1 if r.progression(s.case_uuid, direction) is not None else 0,
    )
    if not uuid:
        return {"standard": None}
    target = repo.progression(uuid, direction)
    return {"standard": _brief(target) if target is not None else None}


def find_misconceptions_for_standard_impl(
    repo: StandardsRepository,
    caseIdentifierUUID: str = "",
    subject: str | None = None,
    code: str | None = None,
) -> dict[str, Any]:
    """Return ``{student_behavior, teacher_move}`` records. Empty is tolerated.

    Accepts a ``code`` in place of ``caseIdentifierUUID``; the code resolves to the same-code
    node that actually holds misconceptions (they can live on a non-representative placement).
    """
    uuid = _resolve_uuid(
        repo, caseIdentifierUUID, code, lambda r, s: len(r.misconceptions(s.case_uuid))
    )
    if not uuid:
        return {"misconceptions": []}
    return {
        "misconceptions": [
            {"student_behavior": m.student_behavior, "teacher_move": m.teacher_move}
            for m in repo.misconceptions(uuid)
        ]
    }


def find_learning_components_from_standard_impl(
    repo: StandardsRepository,
    caseIdentifierUUID: str = "",
    code: str | None = None,
) -> dict[str, Any]:
    """Up to 5 sub-skill description strings, ordered by ordinal. Empty tolerated.

    Accepts a ``code`` in place of ``caseIdentifierUUID``; the code resolves to the same-code
    node richest in components.
    """
    uuid = _resolve_uuid(
        repo, caseIdentifierUUID, code, lambda r, s: len(r.learning_components(s.case_uuid))
    )
    if not uuid:
        return {"learningComponents": []}
    components = repo.learning_components(uuid)[:MAX_LEARNING_COMPONENTS]
    return {"learningComponents": [c.description for c in components]}


def find_curriculum_lessons_impl(
    repo: StandardsRepository,
    caseIdentifierUUID: str | None = None,
    ordinalName: str | None = None,
    lessonName: str | None = None,
    author: str | None = None,
) -> dict[str, Any]:
    """Published curriculum lessons aligned to a standard, most directly-taught first.

    Every row carries its own ``license`` and ``attributionStatement``. That is not
    decoration: the export's attribution string varies by node type and provider, so anyone
    reproducing this owes the record's own string and not a general one. Dropping the fields
    here would make the obligation invisible to everything downstream.
    """
    if not caseIdentifierUUID:
        return {"lessons": []}
    query = getattr(repo, "curriculum_lessons", None)
    if query is None:  # a store built before the curriculum layer existed
        return {"lessons": []}
    rows = query(
        caseIdentifierUUID, author=author, ordinal_name=ordinalName, lesson_name=lessonName
    )[:MAX_CURRICULUM_LESSONS]
    return {
        "lessons": [
            {
                "lessonIdentifier": r.lesson_id,
                "lessonName": r.name,
                "description": r.description,
                "author": r.author,
                "entity": r.entity,
                "courseCode": r.course_code,
                "curriculumLabel": r.curriculum_label,
                "ordinalName": r.ordinal_name,
                "gradeLevel": r.grade,
                "license": r.source_license,
                "attributionStatement": r.attribution,
                # Absent when the export aligns this lesson to the queried standard itself.
                # Present when it was reached through the crosswalk to a Multi-State CCSS
                # standard, which is how a state's own standards reach any curriculum at all.
                # An inferred alignment must never read as a stated one.
                **({"alignedVia": r.bridged_from} if r.bridged_from else {}),
            }
            for r in rows
        ]
    }


def find_materials_for_lesson_impl(
    repo: StandardsRepository,
    lessonIdentifier: str = "",
    materialSource: list[str] | None = None,
) -> dict[str, Any]:
    """The activities and assessments a lesson is made of, in sequence."""
    if not lessonIdentifier:
        return {"materials": []}
    query = getattr(repo, "materials_for_lesson", None)
    if query is None:
        return {"materials": []}
    rows = query(lessonIdentifier, material_source=materialSource)[:MAX_LESSON_MATERIALS]
    return {
        "materials": [
            {
                "materialIdentifier": r.material_id,
                "materialName": r.name,
                "description": r.description,
                "materialSource": r.entity.lower(),
                "ordinalName": r.ordinal_name,
                "educationalUse": r.educational_use,
                "isOptional": r.is_optional,
                "license": r.source_license,
                "attributionStatement": r.attribution,
            }
            for r in rows
        ]
    }


def list_standards_for_mathematical_practice_impl(
    repo: StandardsRepository,
) -> dict[str, Any]:
    """MP1-MP8: the eight Standards for Mathematical Practice, one entry each.

    This was a registered stub returning `[]`, on the reasoning that the skills never consume
    the list. That reasoning was about the *consumer* and never about the data, and the data
    was in the shipped export the whole time. A tool that returns an empty list is
    indistinguishable from a subject that genuinely has no practice standards, so it is
    answered from the store rather than left looking like an absence.

    A non-mathematics slice legitimately returns `[]` here, and that is the correct answer
    rather than a stub: only mathematics has practice standards of this kind.
    """
    return {
        "standardsForMathematicalPractice": [
            {
                "caseIdentifierUUID": s.case_uuid,
                "statementCode": s.code,
                "statementText": s.statement_text,
                "academicSubject": s.academic_subject,
                "jurisdiction": s.jurisdiction,
                "license": s.source_license,
            }
            for s in repo.standards_for_mathematical_practice()
        ]
    }


# ---------------------------------------------------------------------------
# SERVER WIRING
# ---------------------------------------------------------------------------

_ToolFn = Callable[..., dict[str, Any]]


def _never_raise(empty: dict[str, Any]) -> Callable[[_ToolFn], _ToolFn]:
    """Wrap a tool handler so an underlying exception returns ``empty`` instead of raising.

    The skills forbid surfacing errors to teachers, so every tool must be total.
    """

    def decorator(fn: _ToolFn) -> _ToolFn:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> dict[str, Any]:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                print(f"k12-standards-mcp: tool {fn.__name__} failed: {exc}", file=sys.stderr)
                return empty

        return wrapper

    return decorator


def build_server(repo: StandardsRepository) -> FastMCP:
    """Build a FastMCP server whose 7 tools delegate to ``repo``.

    Tool handlers are thin wrappers around the ``*_impl`` functions above (which the tests
    exercise directly). Handler parameter names match the contract verbatim.
    """
    mcp: FastMCP = FastMCP("k12-standards")

    @mcp.tool()
    @_never_raise({"standards": []})
    def find_standard_statement(
        code: str | None = None,
        keywords: list[str] | None = None,
        academicSubject: str | None = None,
        jurisdiction: str | None = None,
    ) -> dict[str, Any]:
        """Resolve standards by code (prefix) or keywords; returns statement text + UUID."""
        return find_standard_statement_impl(repo, code, keywords, academicSubject, jurisdiction)

    @mcp.tool()
    @_never_raise({"standard": None})
    def find_standards_progression_from_standard(
        caseIdentifierUUID: str = "",
        direction: str = "",
        code: str | None = None,
    ) -> dict[str, Any]:
        """Return the single prerequisite (backward) or next (forward) standard.

        Pass ``caseIdentifierUUID`` (as the real connector does) or a bare ``code``.
        """
        return find_standards_progression_from_standard_impl(
            repo, caseIdentifierUUID, direction, code
        )

    @mcp.tool()
    @_never_raise({"misconceptions": []})
    def find_misconceptions_for_standard(
        caseIdentifierUUID: str = "",
        subject: str | None = None,
        code: str | None = None,
    ) -> dict[str, Any]:
        """Return common misconceptions and the teacher move for each.

        Pass ``caseIdentifierUUID`` or a bare ``code``.
        """
        return find_misconceptions_for_standard_impl(repo, caseIdentifierUUID, subject, code)

    @mcp.tool()
    @_never_raise({"learningComponents": []})
    def find_learning_components_from_standard(
        caseIdentifierUUID: str = "",
        code: str | None = None,
    ) -> dict[str, Any]:
        """Return up to 5 sub-skill component descriptions for the standard.

        Pass ``caseIdentifierUUID`` or a bare ``code``.
        """
        return find_learning_components_from_standard_impl(repo, caseIdentifierUUID, code)

    @mcp.tool()
    @_never_raise({"lessons": []})
    def find_curriculum_lessons(
        caseIdentifierUUID: str | None = None,
        ordinalName: str | None = None,
        lessonName: str | None = None,
        author: str | None = None,
    ) -> dict[str, Any]:
        """Curriculum lessons aligned to a standard, most directly-taught first.

        Each carries its own licence and attribution string; reproduce those, not a general one.
        """
        return find_curriculum_lessons_impl(
            repo, caseIdentifierUUID, ordinalName, lessonName, author
        )

    @mcp.tool()
    @_never_raise({"materials": []})
    def find_materials_for_lesson(
        lessonIdentifier: str,
        materialSource: list[str] | None = None,
    ) -> dict[str, Any]:
        """The activities and assessments a lesson is made of, in sequence."""
        return find_materials_for_lesson_impl(repo, lessonIdentifier, materialSource)

    @mcp.tool()
    @_never_raise({"standardsForMathematicalPractice": []})
    def list_standards_for_mathematical_practice() -> dict[str, Any]:
        """The eight Standards for Mathematical Practice, MP1 to MP8."""
        return list_standards_for_mathematical_practice_impl(repo)

    return mcp


def _repo_from_env() -> StandardsRepository:
    """Build the default store from ``K12_TOOLKIT_DB`` (a sqlite path)."""
    db_path = os.environ.get("K12_TOOLKIT_DB", DEFAULT_DB_PATH)
    repo = SqliteStandardsRepository(db_path)
    repo.create_schema()  # tolerate an as-yet-unpopulated DB; ingestion is a separate task.
    return repo


def main() -> None:
    """Entry point: run the stdio MCP server over the env-configured store."""
    server = build_server(_repo_from_env())
    server.run()  # defaults to stdio transport


if __name__ == "__main__":
    main()
