"""CA-math ingestion: turn the adopted Learning Commons JSONL export into the sqlite store.

Public entry points:

- :func:`~k12_toolkit.ingest.builder.build_database` — create schema + ingest a source dir.
- :func:`~k12_toolkit.ingest.builder.ingest_into_connection` — ingest into an open connection.
- :func:`~k12_toolkit.ingest.builder.build_rows` — the pure transform (no sqlite), for tests.

CLI: ``python -m k12_toolkit.ingest --source data/ca-math --db data/standards.db``.
"""

from __future__ import annotations

from k12_toolkit.ingest.builder import (
    IngestStats,
    build_database,
    build_rows,
    ingest_into_connection,
)

__all__ = [
    "IngestStats",
    "build_database",
    "build_rows",
    "ingest_into_connection",
]
