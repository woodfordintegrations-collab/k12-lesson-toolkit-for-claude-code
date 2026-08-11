---
title: "Learning components are truncated at five with no flag"
type: trap
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/host-learning-commons-kg.md
  - src/k12-lesson-toolkit/mcp/server.py
  - src/k12-lesson-toolkit/repository.py
  - https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md
updated: 2026-08-08
---

# Learning components are truncated at five with no flag

## Summary

`find_learning_components_from_standard` slices its result at five and returns a bare list of
strings. No count, no total, no `truncated` field, no warning. A caller that receives five
descriptions cannot tell from the response whether the standard has exactly five or forty-one.

The error this page exists to prevent is one sentence long and it looks harmless: writing "the
standard decomposes into these five components" into a shipped document, on the strength of what
the tool returned. For every standard whose richest placement carries more than five, that
sentence is false, and nothing in the response said so.

Two facts fix the size of the problem, both measured against `data/k12-lesson-toolkit.db` at staging:

- **183** placements carry more than five learning components. The maximum on a single placement
  is **41**.
- Of the five HSG-SRT unit codes, **three exceed the cap** on their richest placement:
  `HSG-SRT.B.4` at 7, `HSG-SRT.B.5` at 6, `HSG-SRT.C.8` at 8. `HSG-SRT.C.6` at 3 and
  `HSG-SRT.C.7` at 1 are returned complete.

So the failure is neither rare nor universal. It lands on the majority of this unit's standards
and not on the rest, which is exactly the shape that lets it survive a spot-check.

**Counts come from the store. Never from the tool response.** That rule is the whole page.

## When to reach for it

Reach for it before any build step prints, counts, or reasons over a component list: a lesson's
sub-skill scaffold, an objective decomposition, a "this standard has N parts" claim in a teacher
document, or a coverage table that compares standards by how many components they carry.

Reach for it when two project documents disagree about a component count, which they currently do.
The resolution procedure is in `## In practice` and it is to re-query, not to choose.

Do **not** reach for this page when the tool returned **nothing**. An empty
`{"learningComponents": []}` has two distinct causes that are byte-identical in the response, and
neither is truncation. That is [[trap-empty-facet-reads-as-success]].

Do **not** reach for this page to work out *which* node holds the components. One code resolves to
several placements and they carry different data; that is
[[concept-standard-placement-vs-code]], and the resolution it describes runs *before* the
truncation described here.

## How it works

The cap is a declared constant in the MCP layer. `server.py` lines 47 and 48, verbatim:

```python
# Contract caps (spec §3).
MAX_LEARNING_COMPONENTS = 5
```

`MAX_LEARNING_COMPONENTS = 5` is line 48. It is applied in the handler at line 213 and the result
returned at line 214, verbatim:

```python
    components = repo.learning_components(uuid)[:MAX_LEARNING_COMPONENTS]
    return {"learningComponents": [c.description for c in components]}
```

The returned value is a list of description strings and nothing else. The staged extract states the
consequence in the same terms this page does: the response "carries no count, no total, no
`truncated` flag, and no indication that a slice occurred."

The store itself truncates nothing. `repository.py` lines 340 to 353, the query, verbatim:

```python
            "SELECT * FROM learning_components WHERE case_uuid = ? ORDER BY ordinal",
```

The cap lives entirely in the MCP layer. Two things follow. First, the untruncated list is always
one query away, on the same database the server is reading. Second, because the rows come back
`ORDER BY ordinal`, a truncation always drops the **tail** of the decomposition, never a random
five. What you lose is the later, usually more advanced, sub-skills, which is the half a lesson's
extension or challenge tier would have been built from.

There is a second-order effect worth stating because it is counter-intuitive. When a caller passes
a bare `code` instead of a `caseIdentifierUUID`, the server resolves it through `_resolve_uuid`
with a facet scorer that is, `server.py` line 209, verbatim:

```python
        repo, caseIdentifierUUID, code, lambda r, s: len(r.learning_components(s.case_uuid))
```

That picks the same-code placement holding the **most** components, and then line 213 slices it to
five. **This project's reading of those two lines, not a statement by the repo:** the resolver is
optimising for richness immediately before the cap discards the surplus, so the truncation is most
likely to bite precisely on the codes that were worth grounding on.

## In practice

**The check.** Do not count the response. Query the store directly for the placement you resolved,
using the same predicate the repository uses, and compare its row count to the length of the list
the tool gave you. If the store returns more than five, the tool's answer was a sample and the
document must not describe it as a decomposition.

**The measured numbers for this unit**, from the staged extract, at the `case_uuid` (placement)
grain:

| Measurement | Value |
|---|---|
| Placements carrying at least one learning component | 1,115 |
| Placements carrying more than five | 183 |
| Maximum components on a single placement | 41 |

Per-placement counts for the five unit codes, each ordered by `case_uuid`:

| Code | Placements | Component count per placement, with jurisdiction |
|---|---|---|
| `HSG-SRT.B.4` | 4 | California 0, California 0, California 7, Multi-State 7 |
| `HSG-SRT.B.5` | 4 | California 6, California 0, Multi-State 6, California 6 |
| `HSG-SRT.C.6` | 4 | Multi-State 3, California 3, California 0, California 3 |
| `HSG-SRT.C.7` | 4 | Multi-State 1, California 0, California 1, California 0 |
| `HSG-SRT.C.8` | 4 | California 8, California 0, Multi-State 8, California 8 |

Every one of these five codes has at least one placement carrying zero components. A hand-picked
placement can return an empty list while a sibling holds seven.

**The two-document conflict, and how it resolves.** `INVENTORY.md` records that `CHEATSHEET.md` in
the HS Geometry project puts `HSG-SRT.B.4` at 14 components and `HSG-SRT.C.8` at 24, while that
project's design spec §7 trap 23 puts them at 7 and 8. The staging agent re-measured the store and
got **B.4 = 7 and C.8 = 8** on the richest placement, agreeing with the design spec. That is this
project's own measurement of its own store, not a statement by Learning Commons. Treat the
`CHEATSHEET.md` figures as unreconciled and re-query before using either. Do not average them and
do not pick the larger because it looks more thorough.

**The attribution that travels with a component.** Learning Commons' `LICENSE.md`, fetched
2026-08-08 and staged verbatim, states that Learning Commons "received ... learning components
under CC BY 4.0 from Achievement Network". All 66 component nodes the verifying agent sampled on
trigonometry and similarity language carried the second sentence, given as a fragment with the
report's own leading ellipsis:

> …Learning Commons received learning components under CC BY-4.0 from Achievement Network.

The export holds **8,686** `LearningComponent` nodes. Quoting a component description is quoting
Achievement Network through Learning Commons, and the credit line is the record's own
`attributionStatement`, not the host's name. See [[concept-attribution-per-record]] and
[[source-learning-commons-kg]].

## Gotchas & constraints

**1. Five means "five or more", and that is the only reading available.** There is no response
field that distinguishes a complete list of five from a slice of forty-one. Any prose that treats a
five-item response as exhaustive is asserting something the tool did not say.

**2. Empty and truncated are different failures that share a surface.** `{"learningComponents": []}`
is returned both when a placement genuinely has none and when the `_never_raise` wrapper swallows a
store exception. Neither is truncation, and none of the three is distinguishable from the response
alone. [[trap-empty-facet-reads-as-success]] owns that pair.

**3. The truncation is ordinal, so it is the tail that goes.** Rows come back `ORDER BY ordinal`.
A reader who sees components 1 to 5 of 8 has the early, foundational sub-skills and none of the
later ones, which reads as a coherent short list rather than as a fragment.

**4. Do not over-apply this to the whole unit.** `HSG-SRT.C.6` (3) and `HSG-SRT.C.7` (1) are
returned complete. C.7's single component is a genuine finding about the store's coverage, not an
artefact of this cap, and it is held by [[evidence-c7-store-gap-not-corpus-gap]]. Reporting a
complete list as "probably truncated" is the mirror-image error and it is just as wrong.

**5. Whether the real Learning Commons connector truncates is unverified.** The local server
reproduces a contract extracted from a design spec whose own table specifies "up to 5 sub-skill
description strings" for this tool. The upstream REST and MCP tiers are, per Learning Commons'
README, "Currently available only to private beta users", and `server.py` lines 17 to 23 state
plainly that the response field names are "reasonable defaults derived from the extracted contract"
and are "NOT pinned by the KG docs". So the cap is verified for the server this project actually
calls, and unverified as a property of Learning Commons' own connector. What would close it: access
to the private beta connector and a call against a standard known to hold more than five components.

**6. A verification of any change to this behaviour must run against the spawned binary.** The
in-repo test suite imports `build_server` directly and never exercises the console script, so it
proves nothing about the running server. See [[trap-stale-stdio-mcp-server]].

**7. This is not the only silent cap in the file.** `MAX_KEYWORD_RESULTS = 25`, `server.py` line
51, bounds keyword search the same way. The rule generalises: an MCP response is a sample of the
store, not a census of it.

## Related

- [[trap-empty-facet-reads-as-success]] is the empty-payload twin of this trap, and the two are
  usually met in the same debugging session.
- [[concept-standard-placement-vs-code]] is the placement multiplicity that runs before the slice,
  and the reason a zero result and a seven result can both be correct for one code.
- [[trap-code-form-silent-zero]] is the third silent-empty mechanism on this store, upstream of
  both: a wrong code form never reaches a placement at all.
- [[evidence-kg-coverage-and-gaps]] is the measured census of the export this cap crops, including
  the 8,686 component nodes.
- [[evidence-c7-store-gap-not-corpus-gap]] holds the one unit code whose short component list is a
  real gap and not this cap.
- [[source-learning-commons-kg]] is the rights verdict on the corpus these components come from,
  and where the Achievement Network attribution string lives.
- [[concept-attribution-per-record]] is why the credit line for a quoted component belongs to the
  record rather than to the host.
- [[trap-stale-stdio-mcp-server]] is why a fix to this cap has to be verified against the spawned
  console script.

## Composes with

- [[practice-resolve-a-standard-code]] is where the resolve happens, and the natural place to run
  the store-side count check before a component list is handed downstream.
- [[practice-ground-a-lesson-end-to-end]] consumes this tool inside its batch call sequence and
  freezes a component list into a grounding bundle, which is the last point at which a truncated
  list can still be caught.

## References

Every code quotation above is transcribed from `sources/k12-lesson-toolkit-store-and-mcp.md`, which
records the repository at git HEAD `1ad5649dd4158c5a96a11561f678a2d877747000`, dated
`Wed Jul 22 22:14:08 2026 -0700`, read on 2026-08-07. All numeric measurements are that agent's,
produced in-session against `data/k12-lesson-toolkit.db` opened read-only. This page opened no repository
file directly.

- `src/k12-lesson-toolkit/mcp/server.py`, quoted through the staged extract: line 48 the constant, line
  209 the component facet scorer, line 213 the slice, line 214 the return, lines 17 to 23 the
  field-name disclaimer, lines 247 to 264 the `_never_raise` wrapper.
- `src/k12-lesson-toolkit/repository.py`, quoted through the staged extract: lines 340 to 353 the
  untruncated `learning_components` query.
- `sources/host-learning-commons-kg.md`, primary. §2 the verbatim `LICENSE.md` naming Achievement
  Network; §5 String 3 and the 66 sampled component nodes; §6 the node-label census carrying
  `LearningComponent` 8,686.
- `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md`,
  HTTP 200, 512 bytes, fetched by this project 2026-08-08.
- `INVENTORY.md`, the row for this page, which records the `CHEATSHEET.md` against design-spec
  count conflict resolved by measurement above. Cited as this project's own record.
