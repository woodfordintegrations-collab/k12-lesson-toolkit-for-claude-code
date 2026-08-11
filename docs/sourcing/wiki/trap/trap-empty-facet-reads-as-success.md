---
title: An empty facet reports success
type: trap
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/host-learning-commons-kg.md
updated: 2026-08-08
---

# An empty facet reports success

## Summary

**What the broken case looks like:** a successful tool call whose payload is
`{"misconceptions": []}`. That is exactly what a healthy call looks like, and exactly what a
crashed call looks like, and exactly what a call against an empty database looks like. The
exception text, if there was one, went to stderr. The caller got the same dict either way.

The staged extract states the consequence in one sentence: a caller cannot distinguish, from the
response alone, a genuine empty result from a swallowed exception.

There are several distinct producers of that identical payload, and only the first is what most
readers assume they are looking at:

| Producer | What it means | What the caller sees |
|---|---|---|
| The backing data is genuinely absent | `misconceptions` table has 0 rows; `data/ca-math/misconceptions.jsonl` is 0 bytes | `{"misconceptions": []}` |
| The tool is a registered stub | `find_curriculum_lessons`, `find_materials_for_lesson`, `list_standards_for_mathematical_practice` return a constant empty in v1 | `{"lessons": []}`, `{"materials": []}`, `{"standardsForMathematicalPractice": []}` |
| The handler threw and the wrapper swallowed it | `_never_raise` catches, prints to stderr, returns the typed-empty payload | the same typed-empty payload |
| The server is pointed at a missing or empty database | `create_schema()` runs unconditionally at startup, so the server starts fine | every tool returns its typed-empty payload |
| The code did not resolve to a uuid | `_resolve_uuid` returns `""` and the handler returns early | the same typed-empty payload |

Because the failure is total by design, "the tool returned nothing" is never a finding. It is
the absence of a finding.

## When to reach for it

Reach for this page before writing any sentence of the form "this standard has no
misconceptions", "no learning components exist for this code", or "the curriculum layer is
empty" on the strength of a tool response. Every one of those is a claim about the world made
from an artifact that cannot report failure.

Reach for it when a build step that consumes a facet produces an empty section and the build
reports success. That is the same event seen from one layer up: a lesson package with an empty
anticipated-misconceptions block and a green run.

Reach for it when you change the store, the ingest, or the server configuration and the tools
still answer. They will answer whatever you do to them. A server pointed at a nonexistent
database file starts successfully.

Do not reach for this page when the emptiness came from a standards lookup returning
`{"standards": []}`. That has its own dominant cause, which is a wrong code form, and its own
check. See [[trap-code-form-silent-zero]].

## How it works

### Totality is a deliberate design constraint, not an accident

`server.py` lines 9 to 10, staged verbatim:

> - Every tool is a **total function**: on any miss or bad input it returns an empty/typed-empty
>   result and NEVER raises. The skills forbid surfacing errors to teachers.

The mechanism, `server.py` lines 247 to 264, staged verbatim:

```python
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
                print(f"k12-lesson-toolkit: tool {fn.__name__} failed: {exc}", file=sys.stderr)
                return empty

        return wrapper

    return decorator
```

The decorator is applied to all seven registered tools with a per-tool empty payload, at
`server.py` lines 276, 287, 302, 315, 327, 338 and 347. The payloads, in registration order:
`{"standards": []}`, `{"standard": None}`, `{"misconceptions": []}`, `{"learningComponents": []}`,
`{"lessons": []}`, `{"materials": []}`, `{"standardsForMathematicalPractice": []}`.

This is a good decision for the teacher-facing product it was written for and a hostile one for
a verifier. Both things are true at once, and the page exists because only the second is
surprising.

The wrapper is not described in the design spec's error-handling section, which states the
total-function rule without naming a wrapper. It was introduced by a commit whose message calls
it, verbatim, "F2: MCP handlers never raise ... (makes the 'no errors to teachers' rule
structural)".

### The misconception layer is empty everywhere, not empty for your standard

`data/ca-math/misconceptions.jsonl` is 0 bytes. Every sibling file in that directory is between
851,166 and 6,142,448 bytes. The `misconceptions` table has 0 rows.

The upstream reason, from `docs/reference/lc-export-schema.md` §5, is an exhaustive negative
check: no `Misconception` node label among the eight labels that exist, no misconception
relationship label among the ten that exist, and no misconception discriminator on
`LearningComponent`, whose properties are positive sub-skills only. A case-insensitive scan for
`misconception` found it in 0 relationships and in 15 nodes, all 15 being the ordinary English
word inside a standard's description or notes text rather than a data structure. The document's
own stated consequence, verbatim:

> **Consequence:** the MCP's `find_misconceptions_for_standard` tool has no source data in the
> public export and must return empty; the skills fall back to training knowledge for
> misconceptions.

So the honest sentence is "the public export contains no misconception data for any standard",
which is a strong and useful fact. The sentence the empty payload invites is "this standard has
no known misconceptions", which is false about the world and unsupported by the response.

### Four of the seven tools cannot return data in v1

Three are constant stubs. `server.py` lines 217 to 237, staged verbatim in part:

```python
def find_curriculum_lessons_impl(...) -> dict[str, Any]:
    """Registered stub: curriculum/HQIM is not in the public export (spec §5)."""
    return {"lessons": []}
```

The fourth, `find_misconceptions_for_standard`, is fully implemented and has no backing rows.
Net, as the staged extract puts it: `find_standard_statement`,
`find_standards_progression_from_standard` and `find_learning_components_from_standard` can
return data. The other four cannot, in v1.

### A wrong database path is indistinguishable from an empty world

`create_schema()` runs unconditionally at startup, with the comment, verbatim: "tolerate an
as-yet-unpopulated DB; ingestion is a separate task." The sqlite connection is opened once in
`SqliteStandardsRepository.__init__` and held for the life of the process. A server started
against a missing or empty file therefore starts cleanly, registers all seven tools, and answers
every call with its typed-empty payload. `DEFAULT_DB_PATH = "k12-lesson-toolkit.db"` is a bare
relative path, so the working directory of the spawn decides which file that is.

## In practice

### The three checks that separate the producers

1. **Read stderr.** It is the only channel the swallowed exception uses. If the process is
   spawned by a client that discards stderr, the diagnostic is gone before anyone can see it.
   Capture it deliberately before deciding a facet is empty.
2. **Prove the store is the store you think it is.** Confirm the `OVEREDUCATED_DB` value the
   server was started with, and confirm that file's row counts directly. Measured for the
   committed store: `standards` 2303, `progressions` 1454, `misconceptions` 0,
   `learning_components` 4203. A store answering with all four at 0 is a wrong path, not an empty
   world.
3. **Query the repository, not the tool.** The store's own methods return everything they hold.
   The MCP layer is where caps, stubs and swallowed exceptions live. Any count of anything must
   come from the store. See [[trap-learning-components-truncated-at-five]] for the case where the
   tool's answer is non-empty and still wrong.

### How to write the finding once you have checked

Correct: "The v1.11.0 public export contains no misconception nodes at all, verified by an
exhaustive label and relationship scan, so `find_misconceptions_for_standard` returns empty for
every code. Misconceptions in this build are authored and cited, not retrieved."

Incorrect: "The knowledge graph returned no misconceptions for HSG-SRT.C.6."

The second sentence is true of the bytes and misleading about everything the reader will do
next with it.

## Gotchas & constraints

**1. The two ways a facet can be empty are not the same kind of fact, and one of them is a
project asset.** A definitively absent upstream layer is a measured, reusable finding. A
swallowed exception is a bug in your call. Collapsing them into "the tool returned empty" throws
away the distinction that makes the first one worth recording.

**2. A hand-authored file can carry a pin to a store side that does not exist.** The
k12-lesson-toolkit repository holds three untracked files under `wiki/`, dated 2026-07-23, one of
which states verbatim that "Each entry carries the California `case_uuid` so the human wiki and
the machine store (`data/ca-math/misconceptions.jsonl`) stay pinned to the same standard and
cannot drift." The pin has no store side: that file is 0 bytes and the table has 0 rows. Those
entries are hand-authored prose, uncommitted, and not reachable through any MCP tool.

**3. The empty payload is not the only silent shape on this server.** The component tool
truncates at five with no flag, which is a non-empty response that is also unreliable as a
count. See [[trap-learning-components-truncated-at-five]].

**4. Do not read this page as an argument to remove the wrapper.** The rule it enforces is a
product requirement: errors must not surface to teachers. The correct countermeasure is on the
verifier's side, in what is checked before an empty result becomes a written claim.

**5. Line numbers here are staged, not re-read.** All `server.py` line references above come
from the staged extract, which read the repository at git HEAD
`1ad5649dd4158c5a96a11561f678a2d877747000` on 2026-08-07. `INVENTORY.md` cites a `return
{"misconceptions": []}` at line 189 that the staged extract does not confirm at that line; the
staged extract places the misconceptions handler at lines 174 to 195. This page cites only what
the staged extract records.

**6. Whether the acceptance run ever exercised any of this end to end is contested inside the
repository itself.** The README's acceptance checkbox is unticked and the handoff says the
skills are not yet proven to ground, while two later commits describe live grounding sessions
that found and fixed defects the same day. See [[evidence-k12-lesson-toolkit-acceptance-record]].

## Related

- [[trap-code-form-silent-zero]] is the other producer of an empty payload, upstream of this one:
  a code that never matched anything in the first place.
- [[trap-learning-components-truncated-at-five]] is the mirror failure on the same server, where
  the response is non-empty and silently incomplete.
- [[trap-stale-stdio-mcp-server]] is why a fix to any of this must be verified against the spawned
  binary rather than an import of `src`.
- [[evidence-kg-coverage-and-gaps]] holds the coverage census: which layers of the upstream graph
  carry data and which are empty.
- [[evidence-store-ingest-boundary]] holds the ingest measurements behind the row counts used in
  the checks above, and the boundary between the export's record shape and the store's schema.
- [[evidence-k12-lesson-toolkit-acceptance-record]] holds the contested question of whether the
  grounding acceptance was ever run to its four documented pass conditions.
- [[source-learning-commons-kg]] is the upstream whose exhaustive misconception check is the
  evidentiary basis for the layer being absent rather than merely unfetched.
- [[license-unmarked-silence]] is the licensing analogue on the rights side of this wiki: an
  artifact that says nothing about its licence, where silence resolves to all rights reserved
  rather than to a grant. The shared shape is that absence of a statement is not a statement of
  absence.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] consumes several of these facets in sequence, so an
  unchecked empty at any step produces a package that is missing a section and reports success.
- [[practice-resolve-a-standard-code]] is where check 3 above is executed, because it is the step
  that goes to the store rather than to the tool.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §1.3 the total-function rule, the
  `_never_raise` source, the seven per-tool empty payloads and their line numbers, and the
  commit that introduced the wrapper; §6.3 `create_schema()` at startup, the single held sqlite
  connection, and `DEFAULT_DB_PATH`.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §1 the four table row counts; §2.1 the 0-byte
  `misconceptions.jsonl`, the sibling file sizes, and the exhaustive upstream absence check
  quoted in full; §2.2 the three constant stubs and the net statement of which tools can return
  data; §2.4 the three untracked `wiki/` files and the pin with no store side; §5 the two
  readings of the acceptance record.
- `sources/host-learning-commons-kg.md`, primary. The export's own licence and attribution
  census, and the live CDN spot-check confirming the local copy has not drifted.

Every row count, byte size and file measurement above is this project's own measurement against
its local repository and its local copy of the public export, read on 2026-08-07. Quotations
attributed to repository documents are that repository's own words, transcribed at staging.
