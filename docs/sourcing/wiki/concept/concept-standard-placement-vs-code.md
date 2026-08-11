---
title: Placement versus code, and richest-representative dedupe
type: concept
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/host-learning-commons-kg.md
  - sources/k12-lesson-toolkit-boundaries.md
  - src/k12-lesson-toolkit/repository.py
  - hs-geometry-similarity-trig/CLAUDE.md
updated: 2026-08-08
---

# Placement versus code, and richest-representative dedupe

## Summary

A standard code is not a node. It is a label that several nodes share. In the standards store, one
code usually resolves to several **framework placements**: the canonical node plus per-jurisdiction
and per-course placements. The grounding data is authored against some of those placements and not
replicated across the rest, and different facets can sit on different siblings of the same code.

Measured against `data/k12-lesson-toolkit.db`: **794** distinct non-empty codes, of which **693** resolve
to more than one placement, with a maximum of **7** placements for a single code. Multiplicity is
the normal case, not an edge case.

The consequence is that a query is not an answer. Taking whichever row comes back first, or picking
a placement by reading a table, lands on an empty placement often, and the raw ordering is not
stable across calls. The store solves this in the query layer with two deterministic selectors,
`dedupe_richest` for the representative and `select_by_code` for a single facet. This project's own
governing file states the rule as a hard rule, verbatim:

> Never re-derive standard placement by hand. Call `repository.dedupe_richest`.

The error this page prevents is a builder concluding that a standard has no prerequisites, no
sub-skills or no children, when a sibling placement of the same code holds all of them. That
conclusion is arrived at honestly, renders as a plausible empty result, and is wrong.

## When to reach for it

Reach for it before grounding any lesson, quiz or package against a standard, and before writing
any query, schema or ingest step that treats a code as a key.

Reach for it the moment a facet comes back empty. An empty progression, an empty component list or
an empty `subStandards` array is the exact symptom this page explains, and the first hypothesis
should be "I am on the wrong placement", not "the data does not exist".

Reach for it when two agents report different results for the same code. Unstable same-code ordering
is a sufficient explanation and does not require anyone to have made a mistake.

Do **not** reach for it to learn what a standard says. This wiki does not restate standard content,
which is emitted separately and machine-derived. See this wiki's `CLAUDE.md`.

## How it works

### The problem, in the repository's own words

`repository.py` carries a comment block above the selection functions. Three spans of it, each
quoted byte-exact and each stated as its own sentence in the source. On multiplicity:

> A single code usually resolves to SEVERAL same-code nodes: the canonical CCSS node plus
> multiple California framework/course placements.

On sparsity, and on facets landing on different siblings, which the source joins into one sentence:

> Data is authored against SOME of those nodes, not replicated across all

> and different facets (a prerequisite, sub-skills, subStandards, misconceptions) can live on
> DIFFERENT placements.

On what a naive query therefore does:

> Returning the raw set surfaces an empty placement first (and unstably, since same-code ties are
> unordered).

Two independent failures are named there and they need separating. **Sparsity**: the data is on some
placements only. **Instability**: same-code ties are unordered, so the first row is not even a
consistent wrong answer.

### The grounding score

`_grounding_score` ranks a node by how much grounding data it carries: one point if a backward
progression exists, one point if a forward progression exists, plus the count of its learning
components. It is memoized across the several sort passes of one request.

### The two selectors, and the exact tie-break

`dedupe_richest` collapses same-code duplicates to the single richest node per code. Its docstring
states the ordering, quoted byte-exact up to the clause break:

> Ties break deterministically: more grounding data wins, then ``prefer_jurisdiction``, then the
> lexicographically smallest ``case_uuid``

and the docstring's own next clause gives the reason, "so the choice is stable across calls."

The precedence is therefore, exactly: highest `_grounding_score`, then `jurisdiction == "California"`
ahead of anything else, then the lexicographically smallest `case_uuid`. Single-member groups skip
scoring entirely.

`select_by_code` answers a different question. Its docstring, verbatim:

> ``facet_score`` ranks nodes for a specific datum ("has a backward edge", "component count",
> "misconception count"); ties fall back to overall grounding richness, then
> ``prefer_jurisdiction``, then the smallest uuid. This lets a bare-``code`` lookup reach the
> sibling that holds the requested datum even when a DIFFERENT sibling is richer overall.

That last clause is the whole point. The overall-richest node and the node holding the datum you
asked for are frequently not the same node. The server passes one of three facet scorers depending
on the tool: a directional progression edge, a misconception count, or a learning-component count.

### Children are unioned rather than selected

`subStandards` does not come from the representative. The server unions children across **all**
same-code placements and dedupes them, because a placement's children can differ. The commit that
introduced it gives the reason verbatim:

> subStandards now union children across all same-code placements (a childless placement could win
> the representative and drop the subtree; e.g. code 4.0 to []).

So three different resolution strategies coexist in one store: one representative for the statement,
a per-facet sibling for each facet, and a union for the children. A hand-written query implements at
most one of them.

## In practice

### The five unit codes, per placement, measured

Component counts per placement for the five HSG-SRT codes, each ordered by `case_uuid`, measured
against `data/k12-lesson-toolkit.db`:

| Code | Placements | Component count per placement, with jurisdiction |
|---|---|---|
| `HSG-SRT.B.4` | 4 | California 0, California 0, California 7, Multi-State 7 |
| `HSG-SRT.B.5` | 4 | California 6, California 0, Multi-State 6, California 6 |
| `HSG-SRT.C.6` | 4 | Multi-State 3, California 3, California 0, California 3 |
| `HSG-SRT.C.7` | 4 | Multi-State 1, California 0, California 1, California 0 |
| `HSG-SRT.C.8` | 4 | California 8, California 0, Multi-State 8, California 8 |

**Every one of these five codes has at least one placement carrying zero components.** Two of
`HSG-SRT.B.4`'s four placements are empty, and so are two of `HSG-SRT.C.7`'s. A hand-picked
placement is a coin flip on this unit, and the flip is not even fair, because the raw ordering is
unstable rather than random in a way anyone can reason about.

The richest placement per code carries, as measured: `HSG-SRT.B.4` 7, `HSG-SRT.B.5` 6,
`HSG-SRT.C.6` 3, `HSG-SRT.C.7` 1, `HSG-SRT.C.8` 8.

### The defect this was built to fix

The commit that introduced the selectors records what it was fixing, verbatim:

> A single standard code resolves to several same-code framework placements; data
> (prerequisite, next, sub-skills, subStandards, misconceptions) is authored against
> some placements, not all. The tools returned placements in an unstable, non-richness
> order, so grounding landed on an empty node while a rich sibling held the data. The
> live grounding test (haiku + sonnet) confirmed this on 3 of 4 HS standards.

and what the fix bought, verbatim from the same message:

> D1 find_standard_statement collapses same-code duplicates to the single richest
> node per code, deterministic (prefer California, then smallest uuid). Store-wide
> "grounds thin despite data" drops 208 codes (115 HS) to 0.

That last figure is the commit author's claim in the commit message. The agent that staged this
evidence did not independently reproduce it, and says so. Cite it as the commit's claim, not as a
measurement of the store.

### Why the multiplicity exists upstream

The store's placements are not an artifact of the store. They come from the export. Measured in the
Learning Commons v1.11.0 export, `HSG-SRT.C.6` alone appears **15 times** across jurisdictions:
California, Illinois, Michigan, Vermont, Delaware, Montana, Washington, Nevada, South Dakota, Rhode
Island, Connecticut, New Hampshire, New Mexico, Washington D.C. and Multi-State. The CA-math slice
this store ingests carries **68** HSG-SRT records across the full cluster.

That upstream multiplicity is also why each placement can require a different credit line. See
[[concept-attribution-per-record]].

## Gotchas & constraints

**1. Code matching is exact-or-dotted-descendant, with no normalisation anywhere.** A leaf code
returns itself; a parent code returns itself and every dotted descendant. A caller's string is
compared to the stored string as given. A near-miss code form returns zero rows with no error and no
diagnostic, which is a separate and silent failure held at [[trap-code-form-silent-zero]].

**2. One California code in this family is unreachable by prefix.** The full measured set of
SRT-family codes in the store includes `HSG.SRT.C.8.1`, which uses a dot where every sibling uses a
hyphen. It is a California-specific addition and a different string, so no `HSG-SRT` prefix probe
reaches it.

**3. `prefer_jurisdiction` defaults to `"California"`, and that is a configured default, not a fact
about the standard.** It is a tie-break, applied only after grounding richness. Reading it as "the
California placement is canonical" inverts the precedence.

**4. The uuid field name is misleading and the mismatch is deliberate.** The store's `case_uuid` is
the Learning Commons **node identifier**, not the external CASE identifier, and the export schema
records that the two never coincide, verbatim: "Note there are **two UUIDs per standard**:
`identifier` (the graph node id, the join spine) and `properties.caseIdentifierUUID` (the external
IMS/CASE id). **They never coincide** (0 / 222,865 equal)." The MCP nonetheless returns the node
identifier in the field it names `caseIdentifierUUID`, a decision recorded in the design spec.

**5. A tool response cannot tell you it failed.** Every tool is a total function and returns a
typed-empty result rather than raising, so a genuine empty and a swallowed exception are
byte-identical at the call site. Resolving the placement correctly does not remove that ambiguity.
See [[trap-empty-facet-reads-as-success]].

**6. The component count you see is capped and the count you need is not.** The MCP layer caps
learning components at five while the repository returns everything. Three of the five unit codes
exceed the cap on their richest placement. Any count of a standard's components must come from the
store, never from the tool response. See [[trap-learning-components-truncated-at-five]].

**7. Two project documents disagree with the store on component counts, and the disagreement is
recorded rather than resolved.** `INVENTORY.md` records that a HS Geometry `CHEATSHEET.md` says
B.4 has 14 components and C.8 has 24, while the HS Geometry design spec says B.4 has 7 and C.8 has
8. The staging agent's own measurement against the store gives B.4 = 7 and C.8 = 8 on the richest
placement, agreeing with the design spec, and it did not open either HS Geometry document.

**8. The measurements above are of one artifact at one commit.** They were taken against
`data/k12-lesson-toolkit.db` with the repository at HEAD `1ad5649dd4158c5a96a11561f678a2d877747000`, dated
`Wed Jul 22 22:14:08 2026 -0700`, read on 2026-08-07. A rebuild against a newer export changes every
count on this page.

## Related

- [[trap-code-form-silent-zero]] is the failure one level earlier: the code string never matched
  anything, so there is no placement to choose between. [[trap-empty-facet-reads-as-success]] is the
  failure one level later: the placement is right and the empty result still cannot be trusted.
  [[trap-learning-components-truncated-at-five]] is the cap that sits on top of a correct
  resolution.
- [[concept-attribution-per-record]] is why the same multiplicity that scatters the data also
  scatters the credit line.
- [[source-learning-commons-kg]] is the upstream export the placements come from.
  [[evidence-kg-coverage-and-gaps]] records what the graph covers and where it is empty, and
  [[evidence-store-ingest-boundary]] which fields survive the export-to-store ingest.
- [[evidence-c7-store-gap-not-corpus-gap]] is the one place where a thin result on this unit is a
  real gap in the store rather than a placement artifact.

## Composes with

- [[practice-resolve-a-standard-code]] is the procedure that applies this model, and it is the only
  supported way to get from a code to a node.
- [[practice-ground-a-lesson-end-to-end]] is where the resolved node is threaded through the
  remaining tool calls, and where passing a uuid rather than re-resolving a code matters.

## References

Primary artifacts, read in place on the dates stated. These are this project's own systems, cited as
this project's measurement and not as any outside party's statement. In
``, read 2026-08-07 at git HEAD
`1ad5649dd4158c5a96a11561f678a2d877747000`: `src/k12-lesson-toolkit/repository.py` for the
richest-representative comment block, `_grounding_score`, `dedupe_richest`, `select_by_code` and
`richest_by_code`; `src/k12-lesson-toolkit/mcp/server.py` for `_resolve_uuid`, the three facet scorers at
their call sites, `_sub_standards` and the `MAX_LEARNING_COMPONENTS` declaration;
`data/k12-lesson-toolkit.db`, opened read-only, for the placement counts, the per-code component table and
the SRT-family code set. Commit `b8fd521c46f7ff73ae3663492b9e242b205e0cc1`,
`Wed Jul 22 19:38:37 2026 -0700`, for the message body quoted above, including the 208-codes claim
and the subStandards union reason.
`hs-geometry-similarity-trig/CLAUDE.md`, Hard rules, for the
never-re-derive-by-hand rule quoted in the summary.

Staged extracts in this wiki, all primary, staged 2026-08-08.
`sources/k12-lesson-toolkit-store-and-mcp.md`: section 2 on code forms and the measured probe table;
section 3 in full, including 3.6 the multiplicity measurement and 3.7 the commit record; section 4.4
on how often the component cap bites and the two disagreeing project documents.
`sources/k12-lesson-toolkit-boundaries.md`: section 1 on the component grain, and section 1.1 on the store
schema being thinner than the export it came from. `sources/host-learning-commons-kg.md`: section 5
for the 15-jurisdiction count on `HSG-SRT.C.6`, section 10 for the 68 HSG-SRT records in the CA-math
slice.
