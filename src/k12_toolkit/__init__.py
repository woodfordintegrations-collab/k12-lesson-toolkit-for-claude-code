"""k12-lesson-toolkit — reproduce the Learning Commons KG 7-tool MCP contract from open data.

Schema-independent foundation: the data model, the repository interface, the 7-tool MCP
server, and contract tests. Data ingestion is a separate, later task.
"""

from k12_toolkit.model import (
    LearningComponent,
    Misconception,
    Progression,
    Standard,
)
from k12_toolkit.repository import (
    InMemoryStandardsRepository,
    SqliteStandardsRepository,
    StandardsRepository,
)

__all__ = [
    "InMemoryStandardsRepository",
    "LearningComponent",
    "Misconception",
    "Progression",
    "SqliteStandardsRepository",
    "Standard",
    "StandardsRepository",
]

__version__ = "0.1.0"
