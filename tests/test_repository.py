"""Repository-level semantics + store integrity, plus a sqlite read-path smoke test."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from k12_toolkit.model import Standard
from k12_toolkit.repository import InMemoryStandardsRepository, SqliteStandardsRepository
from tests.conftest import (
    U_2OA,
    U_2OA_A1,
    U_6RP_A1,
    U_6RP_A2,
    U_7RP_A1,
    Fixture,
)

# --- InMemory repository semantics -------------------------------------------


def test_find_by_code_prefix(fx: Fixture) -> None:
    assert [s.code for s in fx.repo.find_by_code("2.OA")] == ["2.OA", "2.OA.A.1", "2.OA.B.2"]


def test_find_by_code_leaf(fx: Fixture) -> None:
    assert [s.code for s in fx.repo.find_by_code("6.RP.A.2")] == ["6.RP.A.2"]


def test_find_by_code_no_sibling_overmatch_inmemory() -> None:
    # G2: "6.RP.A.1" must not also return "6.RP.A.12" (a raw prefix test would over-match).
    short = Standard("u-short", "6.RP.A.1", "short", "Mathematics", "California", "6", None,
                      "s", "CC BY 4.0")
    long_ = Standard("u-long", "6.RP.A.12", "long", "Mathematics", "California", "6", None,
                      "s", "CC BY 4.0")
    repo = InMemoryStandardsRepository([short, long_])
    assert [s.code for s in repo.find_by_code("6.RP.A.1")] == ["6.RP.A.1"]


def test_find_by_code_no_sibling_overmatch_sqlite(tmp_path: Path) -> None:
    # G2: same over-match guard, sqlite engine.
    db_path = str(tmp_path / "overmatch.db")
    repo = SqliteStandardsRepository(db_path)
    repo.create_schema()
    con = sqlite3.connect(db_path)
    con.executemany(
        "INSERT INTO standards VALUES (?,?,?,?,?,?,?,?,?)",
        [
            ("u-short", "6.RP.A.1", "short", "Mathematics", "California", "6", None, "s",
             "CC BY 4.0"),
            ("u-long", "6.RP.A.12", "long", "Mathematics", "California", "6", None, "s",
             "CC BY 4.0"),
        ],
    )
    con.commit()
    con.close()
    assert [s.code for s in repo.find_by_code("6.RP.A.1")] == ["6.RP.A.1"]
    repo.close()


def test_find_by_code_subject_filter(fx: Fixture) -> None:
    # Prefix "RL" only exists for the ELA standard; filtering to Mathematics drops it.
    assert fx.repo.find_by_code("RL", academic_subject="Mathematics") == []
    assert [s.code for s in fx.repo.find_by_code("RL")] == ["RL.6.1"]


def test_search_keywords_or(fx: Fixture) -> None:
    hits = fx.repo.search_by_keywords(["addition", "textual"])
    assert {s.code for s in hits} == {"2.OA", "2.OA.A.1", "RL.6.1"}


def test_children_of(fx: Fixture) -> None:
    assert [s.code for s in fx.repo.children_of(U_2OA)] == ["2.OA.A.1", "2.OA.B.2"]
    assert fx.repo.children_of(U_6RP_A2) == []


def test_progression_edges_resolve(fx: Fixture) -> None:
    back = fx.repo.progression(U_6RP_A2, "backward")
    fwd = fx.repo.progression(U_6RP_A2, "forward")
    assert back is not None and back.case_uuid == U_6RP_A1
    assert fwd is not None and fwd.case_uuid == U_7RP_A1


def test_learning_components_ordering(fx: Fixture) -> None:
    ordinals = [c.ordinal for c in fx.repo.learning_components(U_2OA_A1)]
    assert ordinals == sorted(ordinals) == [1, 2, 3, 4, 5, 6]


# --- store integrity ---------------------------------------------------------


def test_store_integrity_progression_endpoints_resolve(fx: Fixture) -> None:
    # Every progression target must resolve to a real Standard.
    for direction in ("backward", "forward"):
        target = fx.repo.progression(U_6RP_A2, direction)
        assert target is not None
        assert fx.repo.get_by_uuid(target.case_uuid) is not None


def test_store_integrity_fk_resolve(fx: Fixture) -> None:
    # Every misconception / component FK must point at a real Standard.
    assert fx.repo.get_by_uuid(U_6RP_A2) is not None  # misconception + component owner
    assert fx.repo.misconceptions(U_6RP_A2)
    assert fx.repo.learning_components(U_2OA_A1)


# --- sqlite read-path smoke test (ingestion is a separate task) --------------


def test_sqlite_read_path(tmp_path: Path) -> None:
    """The SqliteStandardsRepository read queries mirror the in-memory ones.

    Data is inserted directly here (a stand-in for the future ingest task) purely to
    validate the SQL read path — prefix LIKE, the progression join, ordering.
    """
    db_path = str(tmp_path / "smoke.db")
    repo = SqliteStandardsRepository(db_path)
    repo.create_schema()

    con = sqlite3.connect(db_path)
    con.executemany(
        "INSERT INTO standards VALUES (?,?,?,?,?,?,?,?,?)",
        [
            ("u-p", "2.OA", "parent", "Mathematics", "California", "2", None, "s", "CC BY 4.0"),
            ("u-c1", "2.OA.A.1", "child one", "Mathematics", "California", "2", "u-p", "s",
             "CC BY 4.0"),
            ("u-leaf", "6.RP.A.2", "unit rate", "Mathematics", "California", "6", None, "s",
             "CC BY 4.0"),
            ("u-prev", "6.RP.A.1", "ratio", "Mathematics", "California", "6", None, "s",
             "CC BY 4.0"),
        ],
    )
    con.execute(
        "INSERT INTO progressions VALUES (?,?,?,?)", ("u-leaf", "u-prev", "backward", "s")
    )
    con.commit()
    con.close()

    assert repo.get_by_uuid("u-leaf") is not None
    assert [s.code for s in repo.find_by_code("2.OA")] == ["2.OA", "2.OA.A.1"]
    assert [s.code for s in repo.find_by_code("6.RP.A.2")] == ["6.RP.A.2"]
    assert repo.find_by_code("2.OA", jurisdiction="Texas") == []
    back = repo.progression("u-leaf", "backward")
    assert back is not None and back.code == "6.RP.A.1"
    assert repo.progression("u-leaf", "forward") is None
    assert [s.code for s in repo.children_of("u-p")] == ["2.OA.A.1"]
    repo.close()


def test_sqlite_load_is_stub(tmp_path: Path) -> None:
    repo = SqliteStandardsRepository(str(tmp_path / "stub.db"))
    repo.create_schema()
    try:
        # Ingestion is deliberately not implemented in this foundation.
        raised = False
        try:
            repo.load()
        except NotImplementedError:
            raised = True
        assert raised
    finally:
        repo.close()
