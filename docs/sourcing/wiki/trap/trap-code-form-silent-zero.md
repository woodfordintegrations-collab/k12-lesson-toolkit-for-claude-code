---
title: Standard code form silently returns zero rows
type: trap
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/host-learning-commons-kg.md
  - sources/host-engageny-nysed.md
  - sources/host-open-middle.md
  - sources/host-accessim-360.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# Standard code form silently returns zero rows

## Summary

**What the broken case looks like:** the tool returns `{"standards": []}`. No error, no warning,
no partial match, no diagnostic. The correct-code case and the wrong-form case are the same
bytes on the wire, and the wrong-form case is indistinguishable at the call site from a code
that genuinely has no data in the store.

Measured by this project against `data/k12-lesson-toolkit.db`, using the same predicate the
repository uses:

| Probe string | Rows returned | Distinct codes returned |
|---|---|---|
| `G-SRT.6` | 0 | none |
| `HSG-SRT.6` | 0 | none |
| `HSG-SRT.C.6` | 4 | `HSG-SRT.C.6` |
| `HSG-SRT` | 68 | `HSG-SRT.A`, `HSG-SRT.A.1`, `HSG-SRT.A.1.a`, `HSG-SRT.A.1.b`, `HSG-SRT.A.2`, `HSG-SRT.A.3`, `HSG-SRT.B`, `HSG-SRT.B.4`, `HSG-SRT.B.5`, `HSG-SRT.C`, `HSG-SRT.C.6`, `HSG-SRT.C.7` (first 12 of the set) |

Two of those three wrong-looking strings are the forms a competent person reaches for first,
because they are the forms the standards themselves are usually written in outside this store.
Both return nothing. The correct form for this project is `HSG-SRT.C.6`.

The failure is not a bug in the store. There is no code-form normalisation anywhere in the
lookup path, by design, and one California standard proves that the obvious "fix" would destroy
real data.

## When to reach for it

Reach for this page the moment a grounding step returns an empty standards result and you are
about to write "the store has no data for this standard". That sentence is the error. It is
almost never true of a real CCSS content code, and it is the single cheapest thing to get wrong
in this build because nothing in the response contradicts it.

Reach for it before writing any code that "cleans up" or normalises a standard code, including
uppercasing, stripping a leading `HS`, inserting a cluster letter, or converting dots to
hyphens. Every one of those transformations is either a no-op or destructive here.

Reach for it when you are copying a code out of a host page. External hosts write their own
forms, and none of them is this store's form. That crossing point is where the wrong string
enters a pipeline.

Do not reach for this page when the empty result came from a facet tool rather than from a
statement lookup. An empty `{"misconceptions": []}` or `{"learningComponents": []}` has its own
distinct causes, several of which are not about the code at all. See
[[trap-empty-facet-reads-as-success]].

## How it works

### The match is exact or dotted descendant, with no normalisation

`repository.py` lines 269 to 286, the sqlite implementation, as staged verbatim:

```python
        sql = "SELECT * FROM standards WHERE (code = ? OR code LIKE ? ESCAPE '\\')"
        params: list[str] = [code, _escape_like(code) + ".%"]
```

The documented semantics, `repository.py` lines 12 to 16, verbatim:

> - ``find_by_code`` is a **prefix** match on ``code``: a leaf code returns just itself; a
>   parent code (e.g. ``"2.OA"``) returns the parent AND every descendant whose code starts
>   with it. Optional ``academic_subject`` / ``jurisdiction`` filters narrow the result.

A caller's string is compared to the stored string. That is the whole mechanism. `G-SRT.6` is
not `HSG-SRT.C.6`, is not a dotted ancestor of it, and therefore matches nothing.

### The alternate code form exists upstream and is discarded at ingest

The upstream export carries two code fields. `docs/reference/lc-export-schema.md` §2.3, the
staged rows verbatim:

| `statementCode` (160,536) | **The standard CODE** e.g. `6.RP.A.2`, `HSA-CED.A`, `3.G.3` | Absent on ~28% (unlabeled sub-parts) |
| `alternateStatementCode` (20,033) | Secondary code form e.g. `6.SP.5b` for `6.SP.B.5b` | Optional |

`ingest/builder.py` line 181, verbatim:

```python
        code = props.get("statementCode") or props.get("alternateStatementCode") or ""
```

`alternateStatementCode` is reached only when `statementCode` is absent or falsy. Measured
against `data/ca-math/standards.jsonl` by this project: 509 records carry
`alternateStatementCode`, and 509 records carry both fields. Every record in the CA-math subset
that has an alternate form also has a canonical form, so all 509 alternate forms are discarded
at ingest and none of them is queryable. Measured example pairs of
`(statementCode, alternateStatementCode)`: `('1.NBT.A.1', '1.NBT.1')`, `('HSF-LE.A.1', 'HSF-LE.1')`,
`('HSG-MG.A.1', 'HSG-MG.1')`, `('6.NS.B.2', '6.NS.2')`.

That is why `HSG-SRT.6` fails specifically. It is a real code form that the upstream data
knows about. It just is not the string this store indexed.

### The dot form that makes normalisation destructive

The full distinct set of SRT-family codes present in the store, measured:

`HSG-SRT.A`, `HSG-SRT.A.1`, `HSG-SRT.A.1.a`, `HSG-SRT.A.1.b`, `HSG-SRT.A.2`, `HSG-SRT.A.3`,
`HSG-SRT.B`, `HSG-SRT.B.4`, `HSG-SRT.B.5`, `HSG-SRT.C`, `HSG-SRT.C.6`, `HSG-SRT.C.7`,
`HSG-SRT.C.8`, `HSG-SRT.D`, `HSG-SRT.D.10`, `HSG-SRT.D.11`, `HSG-SRT.D.9`, `HSG.SRT.C.8.1`.

The last entry uses a dot where every other entry uses a hyphen. It is a California-specific
addition, it is a different string, and it is unreachable by any `HSG-SRT` prefix probe. A
normaliser that rewrites dots to hyphens does not rescue the wrong forms and does delete this
code's identity.

### What the case-insensitivity fix does not cover

The repository HEAD commit made `academicSubject` and `jurisdiction` matching case-insensitive
and added a code-only fallback when a filter empties an otherwise-valid code. Two things it
does not do, stated exactly as the staged extract states them:

1. It makes the **filter values** case-insensitive. It does not touch the `code` comparison,
   which remains byte-exact. A miscased or misformed code still returns zero rows.
2. The code-only fallback fires only when the filtered result is empty AND at least one filter
   was supplied. A code that is simply wrong returns empty from both attempts.

## In practice

### Every host writes a different code form, and none of them is the store's

This is where the wrong string gets into the pipeline. Each of these was read off the host's
own pages by an agent working that host:

| Host | Code form as the host writes it | Recorded on |
|---|---|---|
| EngageNY resource pages | `G.SRT.4`, `G.SRT.6`, `G.SRT.8` | Geometry Module 2 Topic D and E lesson pages |
| openmiddle.com problem tags | `g-srt.2`, `g-srt.5`, `g-srt.8`, `g-srt.11` | the ten problems in the similarity and right-triangle category |
| accessim.org lesson pages | `HSG-SRT.A.3`, `B.4`, `B.5`, `C.6`, `C.7`, `C.8` | Geometry Units 3 and 4 lesson pages |
| Learning Commons export | `HSG-SRT.C.8` in `statementCode` | the live CDN spot-check record |

The wide sweep's own staging rule on this, which this wiki follows: where a host or a report
writes `G.SRT.4`, `G-SRT.6` or similar, that is the external party's own code form and is
preserved as written. This project's own form is `HSG-SRT.C.7` and equivalents. Preserving a
host's form in prose is correct. Passing that form to the store is the trap.

### The check to run before believing an empty result

1. **Probe the parent.** `HSG-SRT` returns 68 rows. If the parent is populated and the leaf is
   empty, the leaf string is wrong, not the data.
2. **Read the code back out of the store, not out of your notes.** The store holds 794 distinct
   non-empty codes. The one you want is one of them, byte for byte.
3. **Check for the empty-code case before concluding anything about coverage.** 283 of 2,303
   standards rows have an empty `code`. The build handoff records the same figure in prose,
   verbatim: "283 CA/CCSS standards have no code (unlabeled sub-parts) → reachable by
   UUID/parent/progression, not by code search (correct — they have no code)." Those rows are
   real data that no code lookup can ever reach.
4. **Only then** consider that the standard may be genuinely thin, and go check the placement
   question, which is a different failure with a different shape. See
   [[concept-standard-placement-vs-code]].

## Gotchas & constraints

**1. The empty payload has more than one producer, and this one is only the first.** A
statement lookup returns `{"standards": []}` for a wrong code form. The same typed-empty
payload comes back when the MCP layer swallows an exception, and when the server is pointed at
an empty database. See [[trap-empty-facet-reads-as-success]]. Diagnosing "wrong code form" from
an empty response alone is a guess.

**2. A leaf code does not over-match a longer sibling, and that is deliberate.** The
self-or-dotted-descendant rule came from a commit whose message records the case verbatim: "F1:
code prefix match is self-or-dotted-descendant (leaf 6.RP.A.1 no longer matches 6.RP.A.12);
both engines, with LIKE-metachar escaping." Do not reintroduce a bare `LIKE code%`.

**3. Do not write a normaliser.** Every wrong form in the measured table above fails for a
different reason: `G-SRT.6` is missing the `HS` prefix and the cluster letter, `HSG-SRT.6` is
missing only the cluster letter. A rule that repairs one does not repair the other, and the
dot-form rule destroys `HSG.SRT.C.8.1`. The correct move is to resolve the code once against
the store and carry the resolved string.

**4. The line ranges cited for `find_by_code` are not consistent across this project's own
records.** The staged extract gives `repository.py` lines 269 to 286 for the sqlite
implementation. `INVENTORY.md` cites lines 269 to 298 for the same function. This page uses the
staged extract's range because that is the artifact whose bytes were read at staging. Neither
was re-checked against the repository here.

**5. This is all measured against one store at one commit.** The staging measurements were run
against `data/k12-lesson-toolkit.db` at git HEAD `1ad5649dd4158c5a96a11561f678a2d877747000`, dated
`Wed Jul 22 22:14:08 2026 -0700`, read on 2026-08-07. A rebuild from a newer export could
change which codes are present. It will not change the mechanism, because the mechanism is a
string comparison.

**6. Verifying a fix by importing `src` proves nothing about the running server.** The whole
in-repo test suite exercises `build_server(...)` and the `*_impl` functions by direct import,
never the spawned binary. See [[trap-stale-stdio-mcp-server]].

## Related

- [[practice-resolve-a-standard-code]] is the procedure that turns a code string into a resolved
  store record, and is where the parent probe in "In practice" is executed.
- [[trap-empty-facet-reads-as-success]] holds the other producers of an identical empty payload,
  including the wrapper that swallows exceptions and returns the same typed-empty dict.
- [[concept-standard-placement-vs-code]] is why a code that does resolve can still land on a
  placement carrying no data, which looks like the same emptiness from one step further in.
- [[trap-learning-components-truncated-at-five]] is the opposite shape on the same server: a
  non-empty response that is silently incomplete.
- [[source-learning-commons-kg]] is the upstream export the two code fields come from, and where
  the per-record attribution obligations live.
- [[evidence-store-ingest-boundary]] holds the ingest census, including which upstream fields
  survive into the store and which are dropped.
- [[trap-stale-stdio-mcp-server]] is why a code-form fix must be verified against the venv
  binary rather than a `src` import.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] runs a code lookup as its first step, so this trap is
  the first thing that can silently unground the rest of that procedure while every later step
  reports success.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §2.1 the `find_by_code` SQL and its
  documented prefix semantics; §2.2 the four measured probes and the full SRT code set including
  `HSG.SRT.C.8.1`; §2.3 `builder.py` line 181, the 509 records carrying both code fields, and the
  upstream field definitions; §5 the case-insensitivity fix and the two things it does not do;
  §6.4 the gap between the test suite and the running binary.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §1 the store census, including 794 distinct
  non-empty codes and 283 rows with an empty code; §3.2 the re-executed ingest run whose
  `standards_without_code: 283` matches the store.
- `sources/host-learning-commons-kg.md`, primary. §4 the live CDN spot-check record carrying
  `statementCode: HSG-SRT.C.8`; §5 the per-record attribution table keyed by `statementCode`.
- `sources/host-engageny-nysed.md`, primary. §4 the per-resource sampling table, where the
  standard tags are written `G.SRT.4`, `G.SRT.6` and `G.SRT.8`.
- `sources/host-open-middle.md`, primary. §4 the ten-problem table, where the site's own tags are
  written `g-srt.2`, `g-srt.5`, `g-srt.8` and `g-srt.11`.
- `sources/host-accessim-360.md`, primary. §7 the lesson-to-standard table as tagged on the
  host's own lesson pages.
- `sources/verdict-wide-sweep.md`, reference. Staging note 5, the rule that an external party's
  code form is preserved as written while this project's own form is `HSG-SRT.C.7`.

Every probe result, row count and record count above is this project's own measurement against
its local store and its local copy of the export. None of it is a statement by Learning Commons,
by any state education department, or by any host named in the table.
