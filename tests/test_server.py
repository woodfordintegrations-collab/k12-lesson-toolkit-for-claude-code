"""MCP wiring test: all seven tools register, and a call round-trips through FastMCP."""

from __future__ import annotations

import asyncio
import json
from typing import Any

import pytest
from mcp.types import TextContent

from k12_toolkit.mcp.server import build_server
from k12_toolkit.model import LearningComponent, Misconception, Standard
from k12_toolkit.repository import InMemoryStandardsRepository
from tests.conftest import U_6RP_A2, Fixture

EXPECTED_TOOLS = {
    "find_standard_statement",
    "find_standards_progression_from_standard",
    "find_misconceptions_for_standard",
    "find_learning_components_from_standard",
    "find_curriculum_lessons",
    "find_materials_for_lesson",
    "list_standards_for_mathematical_practice",
}


def test_server_registers_exactly_seven_tools(fx: Fixture) -> None:
    server = build_server(fx.repo)
    tools = asyncio.run(server.list_tools())
    assert {t.name for t in tools} == EXPECTED_TOOLS
    assert len(tools) == 7


def _call(server: Any, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    result = asyncio.run(server.call_tool(name, arguments))
    # FastMCP returns either a Sequence[ContentBlock] or (content, structured) tuple.
    content = result[0] if isinstance(result, tuple) else result
    block = content[0]
    assert isinstance(block, TextContent)
    parsed: dict[str, Any] = json.loads(block.text)
    return parsed


def test_find_standard_statement_round_trip(fx: Fixture) -> None:
    server = build_server(fx.repo)
    payload = _call(server, "find_standard_statement", {"code": "6.RP.A.2"})
    assert payload["standards"][0]["code"] == "6.RP.A.2"
    assert payload["standards"][0]["caseIdentifierUUID"] == U_6RP_A2


def test_progression_round_trip(fx: Fixture) -> None:
    server = build_server(fx.repo)
    payload = _call(
        server,
        "find_standards_progression_from_standard",
        {"caseIdentifierUUID": U_6RP_A2, "direction": "backward"},
    )
    assert payload["standard"]["code"] == "6.RP.A.1"


def test_stub_tool_round_trip(fx: Fixture) -> None:
    server = build_server(fx.repo)
    payload = _call(server, "find_curriculum_lessons", {"caseIdentifierUUID": U_6RP_A2})
    assert payload == {"lessons": []}


# --- G3: never-raise through the MCP boundary --------------------------------


class _RaisingRepo:
    """A StandardsRepository whose every method raises, to exercise the F2 error net."""

    def get_by_uuid(self, uuid: str) -> Standard | None:
        raise RuntimeError("boom")

    def find_by_code(
        self,
        code: str,
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        raise RuntimeError("boom")

    def search_by_keywords(
        self,
        keywords: list[str],
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        raise RuntimeError("boom")

    def children_of(self, uuid: str) -> list[Standard]:
        raise RuntimeError("boom")

    def progression(self, uuid: str, direction: str) -> Standard | None:
        raise RuntimeError("boom")

    def misconceptions(self, uuid: str) -> list[Misconception]:
        raise RuntimeError("boom")

    def learning_components(self, uuid: str) -> list[LearningComponent]:
        raise RuntimeError("boom")


def test_call_tool_typed_empty_on_miss(fx: Fixture) -> None:
    # A code miss, a bad direction, and an unknown UUID all return typed-empty via call_tool.
    server = build_server(fx.repo)
    assert _call(server, "find_standard_statement", {"code": "9.ZZ"}) == {"standards": []}
    assert _call(
        server,
        "find_standards_progression_from_standard",
        {"caseIdentifierUUID": U_6RP_A2, "direction": "sideways"},
    ) == {"standard": None}
    assert _call(
        server,
        "find_standards_progression_from_standard",
        {"caseIdentifierUUID": "nope-unknown-uuid", "direction": "backward"},
    ) == {"standard": None}


@pytest.mark.parametrize(
    ("tool_name", "arguments", "expected"),
    [
        ("find_standard_statement", {"code": "6.RP.A.2"}, {"standards": []}),
        (
            "find_standards_progression_from_standard",
            {"caseIdentifierUUID": "u", "direction": "backward"},
            {"standard": None},
        ),
        ("find_misconceptions_for_standard", {"caseIdentifierUUID": "u"}, {"misconceptions": []}),
        (
            "find_learning_components_from_standard",
            {"caseIdentifierUUID": "u"},
            {"learningComponents": []},
        ),
    ],
)
def test_repo_exception_returns_typed_empty(
    tool_name: str, arguments: dict[str, Any], expected: dict[str, Any]
) -> None:
    # A repository method that raises must never surface an error through the MCP boundary.
    server = build_server(_RaisingRepo())
    assert _call(server, tool_name, arguments) == expected


# --- G4: jurisdiction filter on the tool path ---------------------------------


def test_find_standard_statement_filters_by_jurisdiction() -> None:
    ca = Standard("g4-ca", "9.G.A.1", "ca standard", "Mathematics", "California", "9", None,
                  "s", "CC BY 4.0")
    tx = Standard("g4-tx", "9.G.A.1", "tx standard", "Mathematics", "Texas", "9", None,
                  "s", "CC BY 4.0")
    server = build_server(InMemoryStandardsRepository([ca, tx]))
    payload = _call(
        server, "find_standard_statement", {"code": "9.G.A.1", "jurisdiction": "California"}
    )
    assert [s["caseIdentifierUUID"] for s in payload["standards"]] == ["g4-ca"]
