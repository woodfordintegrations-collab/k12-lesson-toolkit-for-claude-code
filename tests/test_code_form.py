"""The code-form trap: a wrong-shaped standards code returns zero rows and no error.

This is the failure mode most likely to be misread by a caller, human or model, because
nothing about it looks like a failure. `HSG-SRT.C.6` is the form the store holds. `G-SRT.6`
and `HSG-SRT.6` are the two forms people actually type -- the first is how the standard is
written in most published material, the second drops the cluster letter -- and both return
an empty list. An empty list reads as "this standard has no content", which is a statement
about the corpus. The true statement is about the query.

These tests exist so the behaviour is pinned and documented rather than rediscovered. They
do not assert that the lookup SHOULD be strict; they assert that it IS, so that any change
to that is a deliberate one with a failing test attached.
"""

from __future__ import annotations

import pytest

from tests.conftest import CA, MATH


# The forms a caller is likely to type for the same standard. Only the first exists.
CANONICAL = "6.RP.A.2"
WRONG_FORMS = [
    "6.RP.2",       # cluster letter dropped
    "RP.A.2",       # domain prefix dropped
    "6-RP-A-2",     # hyphens for dots
    "6.rp.a.2",     # lowercase, if matching is case-sensitive
]


def test_canonical_code_returns_rows(fx):
    """The control. Without this passing, every assertion below is vacuous."""
    assert fx.repo.find_by_code(CANONICAL), (
        "the canonical code returned nothing, so this whole module is testing "
        "an empty store rather than the matching behaviour"
    )


@pytest.mark.parametrize("code", WRONG_FORMS)
def test_wrong_form_returns_empty_without_raising(fx, code):
    """A mis-shaped code is silent, not loud. That is the trap, stated as a test."""
    if code.lower() == CANONICAL.lower() and code != CANONICAL:
        # Case-insensitive matching is a documented behaviour of the store; if this
        # form resolves, it resolves, and that is not the trap under test.
        pytest.skip("case-insensitivity is covered in test_repository")
    result = fx.repo.find_by_code(code)
    assert result == [], f"{code!r} unexpectedly matched; update the docs if this changed"


def test_prefix_match_is_the_intended_widening(fx):
    """The one widening the store does offer: a parent code returns its descendants.

    Worth pinning next to the trap, because it is the reason a caller may believe the
    matching is looser than it is.
    """
    parent = fx.repo.find_by_code("2.OA")
    codes = {s.code for s in parent}
    assert "2.OA.A.1" in codes and "2.OA.B.2" in codes, (
        "parent-code prefix matching stopped returning descendants"
    )


def test_filters_do_not_rescue_a_wrong_form(fx):
    """Narrowing by subject or jurisdiction cannot make a wrong code match."""
    assert fx.repo.find_by_code("6.RP.2", academic_subject=MATH) == []
    assert fx.repo.find_by_code("6.RP.2", jurisdiction=CA) == []
