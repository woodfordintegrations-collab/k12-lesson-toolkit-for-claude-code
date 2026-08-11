---
title: "A stale stdio MCP server verifies nothing"
type: trap
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/k12-lesson-toolkit-boundaries.md
  - .venv/bin/k12-lesson-toolkit-mcp
  - src/k12-lesson-toolkit/mcp/server.py
  - docs/acceptance/ca-math-grounding.md
updated: 2026-08-08
---

# A stale stdio MCP server verifies nothing

## Summary

The standards MCP server is a stdio process. The host spawns it once, it imports its modules
once, and nothing in it reloads. Every verification that goes through a fresh Python import of
`src/` therefore exercises a different copy of the code than the tool the build is actually
calling, and the two can disagree for the whole life of the session without any error surfacing.

The rule this produces is short: **verification runs against `.venv/bin/k12-lesson-toolkit-mcp`, never
against an in-process import.** It is recorded in the HS Geometry project's `CHEATSHEET.md` under
Grounding path, verbatim as transcribed in this wiki's `INVENTORY.md`:

> Verify any MCP change against the venv binary, never a `src` import. The stdio server is spawned
> once per session and does not hot-reload.

and again in that project's design spec as tier-2 trap 11, verbatim: "Never verify an MCP change
by importing from `src`."

The repository supplies the mechanism and, more usefully, supplies the size of the gap. All 68
tests in the repo import the module directly. The staged extract states the consequence without
hedging: the in-repo test suite proves nothing about the running server, and that is the gap the
rule exists to close.

## When to reach for it

Reach for it the moment you are about to say an MCP change is verified. That sentence is the
failure point, not the edit.

Reach for it when a tool returns an answer you believe you already fixed. The expensive version of
this trap is not a red test, it is a green one: pytest passes, a REPL import shows the new
behaviour, and the live tool keeps returning the old answer into a document that ships.

Reach for it when a tool returns empty and you are about to write down what that means. On this
server an empty result has at least three unrelated causes and the payload is identical in all
three. See the table under "In practice".

Do not reach for this page for the store's other silent-wrong-answer modes:
[[trap-code-form-silent-zero]] for a miscast code returning zero rows,
[[trap-empty-facet-reads-as-success]] for a facet empty by data or by swallowed exception, and
[[trap-learning-components-truncated-at-five]] for a list silently cut. Those are properties of the
code. This page is a property of the process.

## How it works

**The artifact that gets spawned is 217 bytes and does nothing but import.**
`.venv/bin/k12-lesson-toolkit-mcp`, mtime `2026-07-22 07:23:57`, mode `-rwxr-xr-x`. Its entire contents,
verbatim:

```python
#!.venv/bin/python
import sys
from k12-lesson-toolkit.mcp.server import main
if __name__ == '__main__':
    sys.argv[0] = sys.argv[0].removesuffix('.exe')
    sys.exit(main())
```

It is declared in `pyproject.toml`, verbatim:

```toml
[project.scripts]
k12-lesson-toolkit-mcp = "k12-lesson-toolkit.mcp.server:main"
```

**The install is editable, and that is the part people misread as safety.**
`.venv/lib/python3.12/site-packages/_editable_impl_k12-lesson-toolkit.pth` is 50 bytes and its entire
content, confirmed byte by byte with `od -c`, is one line:

```
src
```

No import hook, no compiled copy. The console script imports straight out of the working tree. The
staged extract states the consequence precisely, and it is easy to state wrong:

- A **new** spawn of `.venv/bin/k12-lesson-toolkit-mcp` picks up whatever is in `src/` at that moment.
- An **already-running** process does not. Python binds the module at import time, and nothing in
  this server reloads it.

"Editable install" therefore guarantees freshness at spawn time and guarantees nothing afterwards.
An engineer who reasons "it is editable, so it is live" has the first half right and the second
half backwards.

**Startup reads the configuration once, too.** `server.py`, verbatim:

```python
def _repo_from_env() -> StandardsRepository:
    """Build the default store from ``OVEREDUCATED_DB`` (a sqlite path)."""
    db_path = os.environ.get("OVEREDUCATED_DB", DEFAULT_DB_PATH)
    repo = SqliteStandardsRepository(db_path)
    repo.create_schema()  # tolerate an as-yet-unpopulated DB; ingestion is a separate task.
    return repo


def main() -> None:
    """Entry point: run the stdio MCP server over the env-configured store."""
    server = build_server(_repo_from_env())
    server.run()  # defaults to stdio transport
```

Three things follow, all measured. `OVEREDUCATED_DB` is read once, inside `main()`, so changing
the environment after spawn changes nothing. The sqlite connection is opened once in
`SqliteStandardsRepository.__init__` and held for the life of the process. And `create_schema()`
runs unconditionally, so a server pointed at a missing or empty database file **starts
successfully** and every tool then returns its typed-empty payload rather than an error.

## In practice

**The registration block names the exact artifact to exercise.** From
`docs/acceptance/ca-math-grounding.md`, verbatim:

```json
{
  "mcpServers": {
    "learning-commons-knowledge-graph": {
      "command": ".venv/bin/k12-lesson-toolkit-mcp",
      "env": { "OVEREDUCATED_DB": "data/k12-lesson-toolkit.db" }
    }
  }
}
```

That path is the thing under test. A verification is valid when it drives that command in a
process spawned **after** the edit and reads what comes back. Anything that reaches
`k12-lesson-toolkit.mcp.server` by importing it is testing a second copy.

**The repo contains no procedure for doing this, and that is worth knowing before you go looking
for one.** `tests/test_server.py` line 12 reads `from k12-lesson-toolkit.mcp.server import build_server`;
the suite exercises `build_server(...)` and the `*_impl` functions by direct import and never the
spawned binary. The one in-repo corroboration that the practice was ever followed is a commit
message, `1ad5649`, verbatim:

> Verified against the deployed console script: lowercase and mismatched subject now resolve.

That is the author asserting the verification was run, not the tests demonstrating it. Treat it as
a claim in the record, not as coverage.

**An empty payload has at least three causes and they are byte-identical.** Before writing down
what an empty result means, rule out the process cause first, because it is the only one an edit
can have introduced:

| Cause | What it means | How to discriminate |
|---|---|---|
| Stale process | your fix is in `src/`, the running server has the old import | respawn the console script and re-ask |
| Wrong or empty database | `OVEREDUCATED_DB` points somewhere that `create_schema()` happily created | check the path the process was spawned with, not the one in your shell |
| Empty by construction | four of the seven tools cannot return data in v1 | three are constant stubs returning `{"lessons": []}`, `{"materials": []}` and `{"standardsForMathematicalPractice": []}`; the fourth, misconceptions, is implemented over a table measured at 0 rows |

Only the first is fixed by restarting. The second and third are not bugs and will survive every
respawn you perform.

## Gotchas & constraints

**1. Green tests are the trap, not a defence against it.** `.venv/bin/pytest -q` returned
`68 passed in 1.14s` when this repository was staged. Every one of those tests imports the module.
A change that is correct in `src/` and absent from the running server passes all 68.

**2. The repo's own prose about its test count is stale, which is the same failure one layer up.**
`README.md` line 41 says "50 tests green" and the overnight handoff carries "50 pytest"; two later
commits record 65 and then 68, and 68 is what runs. A document describing a process that has moved
on since is exactly what a spawned server is.

**3. Two project records give the binary different dates and neither is reconciled here.** The
staged measurement is mtime `2026-07-22 07:23:57`. This wiki's `INVENTORY.md` row for the same file
records it as "dated 2026-07-23". Both are reproduced as written. Do not average them or pick one;
re-`stat` the file if the date matters to your question.

**4. What this repository proves stops short of the rule it supports.** The staging agent's read
scope was the k12-lesson-toolkit repository only; it did not open the HS Geometry `CHEATSHEET.md` or the
design spec, so the rule text above is quoted as transcribed in `INVENTORY.md`. What the repository
itself establishes is the mechanism: the console script exists at the registered path, the install
is a bare `src` path append, and the process holds one module import and one sqlite connection for
its lifetime.

**5. Whether a held sqlite connection sees a database rebuilt underneath it was not measured.** The
record establishes only that the connection is opened once and not re-opened per call. Closing the
question would take an experiment: spawn, query, re-ingest, query again without respawning.

**6. Respawning has its own hazard.** A fresh spawn picks up whatever is in `src/` at that moment,
including edits you have not finished. The artifact under test is the working tree, not a commit,
so record the git HEAD alongside the result. At staging it was
`1ad5649dd4158c5a96a11561f678a2d877747000`, `Wed Jul 22 22:14:08 2026 -0700`, tree clean except one
untracked directory.

## Related

- [[trap-code-form-silent-zero]] is the same silent-wrongness at the query layer: an exact-match
  code lookup returning zero rows without an error.
- [[trap-empty-facet-reads-as-success]] is why an empty payload cannot be read as "there are none".
- [[trap-learning-components-truncated-at-five]] is the third of the set, where the tool returns
  data that is real but silently incomplete.
- [[evidence-store-ingest-boundary]] holds which of the seven tools are empty by construction, the
  third row of the discrimination table above.
- [[evidence-k12-lesson-toolkit-acceptance-record]] holds the standing disagreement about whether the
  grounding acceptance was ever run to its four pass conditions, which is this page's question at
  project scale: what was actually exercised.
- [[evidence-kg-coverage-and-gaps]] is the corpus census, so an empty result can be attributed to
  the data rather than to the process.
- [[concept-standard-placement-vs-code]] is why the same call can return different nodes on
  different runs, a separate reason a re-query may not reproduce.

## Composes with

- [[practice-resolve-a-standard-code]] is the call this page's rule protects: its failure modes are
  all silent, so a code-resolution result obtained from a stale process is indistinguishable from a
  correct one.
- [[practice-ground-a-lesson-end-to-end]] is where the cost lands. A grounding bundle frozen from a
  stale server carries stale provenance that looks exactly like fresh provenance.

## References

Repository artifacts, read at staging on 2026-08-07 from
``, git HEAD
`1ad5649dd4158c5a96a11561f678a2d877747000`:

- `.venv/bin/k12-lesson-toolkit-mcp`, 217 bytes, mtime `2026-07-22 07:23:57`, mode `-rwxr-xr-x`, quoted
  in full above; and `_editable_impl_k12-lesson-toolkit.pth`, 50 bytes, one line, confirmed with `od -c`.
- `src/k12-lesson-toolkit/mcp/server.py`, 14,017 bytes: `main()`, `_repo_from_env()`, `DEFAULT_DB_PATH`
  at line 45, the three constant stubs at lines 217 to 237.
- `src/k12-lesson-toolkit/repository.py`, 18,166 bytes: `SqliteStandardsRepository.__init__` lines 230 to
  233, where the connection is opened once.
- `tests/test_server.py` line 12, the direct import that makes all 68 tests blind to the spawned
  process; `.venv/bin/pytest -q` at staging returned `68 passed in 1.14s`.
- `docs/acceptance/ca-math-grounding.md`, the registration block quoted above.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §6 "The stale stdio server", including §6.4 on
  the honest limit of what the repository proves.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §2.2 the four tools empty on every call in v1, §5
  the acceptance-record contradiction.

The rule itself, quoted as transcribed in this wiki's `INVENTORY.md` rather than from the source
files, which the staging agent did not open: `Projects/HS Geometry/CHEATSHEET.md` Grounding path,
and `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md` §7 tier 2 trap 11.
