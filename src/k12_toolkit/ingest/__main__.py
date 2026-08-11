"""CLI: build the sqlite store from the CA-math export.

    python -m k12_toolkit.ingest --source data/ca-math --db data/standards.db
"""

from __future__ import annotations

import argparse
from dataclasses import asdict

from k12_toolkit.ingest.builder import build_database


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m k12_toolkit.ingest",
        description="Ingest the Learning Commons CA-math export into the sqlite store.",
    )
    parser.add_argument(
        "--source",
        default="data/ca-math",
        help="Directory of *.jsonl export files (default: data/ca-math).",
    )
    parser.add_argument(
        "--db",
        default="data/standards.db",
        help="Path to the sqlite DB to build (default: data/standards.db).",
    )
    args = parser.parse_args()

    stats = build_database(args.source, args.db)
    print(f"Built {args.db} from {args.source}")
    for key, value in asdict(stats).items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
