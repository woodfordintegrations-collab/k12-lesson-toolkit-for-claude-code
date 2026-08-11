---
title: "The ingest boundary: what crosses from the Learning Commons export into the store"
type: evidence
sources:
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/host-learning-commons-kg.md
  - data/k12-lesson-toolkit.db
  - src/k12-lesson-toolkit/mcp/server.py
  - src/k12-lesson-toolkit/ingest/builder.py
  - docs/reference/sourcing-verdict.md
  - NOTICE
updated: 2026-08-08
---

# The ingest boundary: what crosses from the Learning Commons export into the store

> **Superseded in part, 2026-08-11. Kept as the record of an audit dated 2026-08-08.**
>
> This page audited a build in which three of the seven MCP tools were registered stubs. All
> three are now implemented, so the passages below describing them as stubs are history, not
> current behaviour: `find_curriculum_lessons` serves 3,301 lessons,
> `find_materials_for_lesson` serves 12,599 activities and assessments, and
> `list_standards_for_mathematical_practice` serves MP1-MP8.
>
> The page's central finding stands and is why it is kept: **an empty return is not evidence
> of an empty source.** It was right that the curriculum layer was present in the export and
> that the stated reason for stubbing it was false. It then concluded "the decision to stub
> both tools is still right. Only the stated reason is wrong" — and that conclusion was the
> last thing keeping the layer unbuilt. Once the reason was measured rather than inherited,
> the join turned out to be one hop, blocked only by an identifier-space mismatch that returns
> empty and raises nothing. See `docs/reference/sourcing-verdict.md`.

## Summary

The store the MCP reads is not the Learning Commons export. It is a filtered slice of it, run
through a four-table schema that is thinner than the records it came from. Two different things
get dropped at that boundary, and each produces a different wrong belief downstream.

**Dropped by the filter: an entire layer that exists.** 16,021 Illustrative Mathematics
curriculum-metadata nodes are in the public export and are not ingested. Four of the seven MCP
tools therefore return empty on **every** call in v1, three of them because they are constant
stubs. An empty result from those four is a boundary, not an answer about the standard.

**Dropped by the schema: the rights fields.** Only the `standards` table has a `source_license`
column. No table anywhere carries `attributionStatement`. The repository's `NOTICE` says the data
retains both fields, and that sentence is accurate about `data/ca-math/*.jsonl` and **not** about
`data/k12-lesson-toolkit.db`, which is the artifact the MCP actually reads.

The error this page exists to prevent is the one a competent reader makes from the repository's own
documentation: `docs/reference/sourcing-verdict.md` states the curriculum-lessons and materials
layer is "NOT in the public LC JSONL", and that is false as written. The metadata **is** public;
the lesson **content** is not. The decision to stub both tools is still right. Only the stated
reason is wrong, and a builder who re-derives from it concludes the layer cannot be reached at all.

## When to reach for it

Reach for it the moment a tool returns an empty list, before that emptiness gets written into a
document as a finding.

Reach for it before quoting any repository document about what is or is not in the public export.
Four separate places in that repository repeat the wrong reason.

Reach for it before building an attribution block from the store, which cannot be done: the string
you need did not survive ingest. See [[practice-assemble-an-attribution-block]] and
[[concept-attribution-per-record]].

Reach for it before reporting a component count, because the number in the table is attachments,
not components.

Do **not** reach for it for the upstream census. That is [[evidence-kg-coverage-and-gaps]]. This
page is only about what crosses.

## The claim

**C1. The filter and the counts.** The subset was produced by filtering the raw export to
`academicSubject=="Mathematics"` AND `jurisdiction` in {California, Multi-State}. The resulting
store holds `standards` 2,303, `progressions` 1,454, `learning_components` 4,203, `misconceptions`
0. Falsifier: re-run the ingest and get different counts.

**C2. Four of seven tools return empty on every call in v1.** `find_curriculum_lessons`,
`find_materials_for_lesson` and `list_standards_for_mathematical_practice` are registered stubs
returning a constant empty. `find_misconceptions_for_standard` is fully implemented and has zero
backing rows. Falsifier: any input to any of the four producing a non-empty result.

**C3. The curriculum layer's metadata is in the public export and is not ingested.** 16,021
`im:`-prefixed nodes across `Activity`, `Assessment`, `Lesson`, `LessonGrouping` and `Course`, plus
their alignment and structure edges. Falsifier: finding those nodes in the store, or finding they
are absent from the export.

**C4. The rights fields do not survive ingest intact.** `standards` carries `source_license`;
`progressions`, `misconceptions` and `learning_components` carry a free-text `source` and no
licence column. No table carries `attributionStatement`. Falsifier: `PRAGMA table_info` showing
otherwise.

**C5. 4,203 is a count of attachments.** It is component-to-placement rows: 1,853 distinct
component descriptions, 1,115 distinct placements carrying at least one. Falsifier: a distinct
count matching 4,203.

**C6. More than half the prerequisites are derived, not present upstream.** 788 of the 1,454
progression rows carry the bridged source stamp; 666 carry the direct one. Falsifier: a different
split.

**What these claims do not say.** They say nothing about whether the stub decision was correct; it
was, and it is unaffected by C3. They say nothing about the quality of the derived edges, only
about their provenance. And the 16,021 figure is a relationship between two counts stated in one
upstream document, not a number this project re-parsed from the 292 MB export.

## What the evidence shows

### What crosses: the store, measured

`data/k12-lesson-toolkit.db`, 2,342,912 bytes, mtime `2026-07-22 07:41:36`. Row counts by
`SELECT COUNT(*)`:

| Table | Rows |
|---|---|
| `standards` | 2303 |
| `progressions` | 1454 |
| `misconceptions` | 0 |
| `learning_components` | 4203 |

Standards split by jurisdiction: California 1,467, Multi-State 836, which agrees exactly with the
upstream schema document's own California and Multi-State math counts. Distinct non-empty `code`
values: 794. Rows with an empty `code`: 283, which the repository's handoff explains in prose as
unlabeled sub-parts, reachable by UUID, parent or progression but not by code search.

Every one of the 2,303 standards rows carries a single `source_license` value,
`https://creativecommons.org/licenses/by/4.0/`.

### The filter, and the six files it produced

`docs/reference/lc-export-schema.md` §7, verbatim:

> Produced by filtering the raw export to `academicSubject=="Mathematics"` AND
> `jurisdiction ∈ {California, Multi-State}` and pulling the incident edges/nodes. All files are
> JSONL of the original records (unchanged shape); join on `node.identifier`.
>
> | File | Records | Contents |
> |---|---|---|
> | `standards.jsonl` | 2,303 | StandardsFrameworkItem nodes: **1,467 California** + **836 Multi-State CCSS** math |
> | `hierarchy.jsonl` | 2,303 | `hasChild` edges touching a selected standard (parent/child → `subStandards`) |
> | `progressions.jsonl` | 1,041 | `buildsTowards` (757) + `relatesTo` (284); all `Multi-State` math endpoints |
> | `crosswalk.jsonl` | 591 | `hasStandardAlignment` CA-math → CCSS-math bridge edges (jaccard-scored) |
> | `components.jsonl` | 6,056 | 4,203 `supports` edges (LearningComponent→standard) + 1,853 distinct `LearningComponent` nodes (distinguish by `type`: `"relationship"` vs `"node"`) |
> | `misconceptions.jsonl` | 0 | Empty — no misconception data exists in the export |

Those record counts were independently re-parsed line by line at staging and hold. The ingest was
re-executed into a scratch path, leaving the repository store untouched, and its output matches the
committed store's measured rows exactly, including `standards_without_code: 283` and
`relatesto_skipped: 284`. The pipeline is reproducible.

### What does not cross: four of seven tools

Three are constant stubs. `server.py` lines 217 to 237, the docstrings verbatim:

```python
    """Registered stub: curriculum/HQIM is not in the public export (spec §5)."""
    return {"lessons": []}
    """Registered stub: instructional materials are not in the public export (spec §5)."""
    return {"materials": []}
    """Registered stub: the skills never consume the SMP list (spec §3)."""
    return {"standardsForMathematicalPractice": []}
```

The fourth, `find_misconceptions_for_standard`, is fully implemented and returns
`{"misconceptions": []}` for every input because the table has 0 rows. Its own docstring reads,
verbatim: "Return ``{student_behavior, teacher_move}`` records. Empty is tolerated."

Net: `find_standard_statement`, `find_standards_progression_from_standard` and
`find_learning_components_from_standard` can return data. The other four cannot, in v1. Because
every tool is wrapped so it never raises, a swallowed exception produces the identical typed-empty
payload, so the caller cannot tell those cases apart from the response alone. See
[[trap-empty-facet-reads-as-success]].

### The repository document that is stale on its reason

`docs/reference/sourcing-verdict.md` lines 49 to 52, verbatim:

> **Build from scratch:**
> - The entire 7-tool MCP server (k12-lesson-toolkit) — no forkable server exists.
> - Curriculum-lessons + materials layer (`find_curriculum_lessons` / `find_materials_for_lesson`)
>   — NOT in the public LC JSONL. Biggest genuine build gap; **stubbed in v1**.

The same reason is repeated in the design spec twice, in the handoff once, and in the code's own
stub docstring. Against it, the upstream schema document's own label census lists `Activity` 8,173,
`Assessment` 4,516, `Lesson` 2,550, `LessonGrouping` 764 and `Course` 18, and states that
Illustrative Mathematics content is provider-prefixed `im:` at **16,021 nodes**. It also lists the
edges structuring that layer: `hasEducationalAlignment` 52,807, `hasPart` 15,944, `hasReference`
472, `hasDependency` 209, `mutuallyExclusiveWith` 192.

A third repository document characterises the same layer as public but deferred, verbatim: "Public
(CC BY) but highest effort; safe to defer."

The reconciliation the staged extract states, without editing either document: what is public is
the curriculum layer's **metadata**, and the lesson **content** is not. That is why one document
calls it high effort and another calls it absent. The v1 decision to stub is unaffected. A second,
independent report reached the same contradiction from the rights side, measuring the same 16,021
records as the largest single attribution block in the export.

### What the schema drops, and why it is a rights problem

`PRAGMA table_info` on each table, measured columns:

| Table | Columns |
|---|---|
| `standards` | `case_uuid`, `code`, `statement_text`, `academic_subject`, `jurisdiction`, `grade`, `parent_uuid`, `source`, `source_license` |
| `progressions` | `from_uuid`, `to_uuid`, `direction`, `source` |
| `misconceptions` | `case_uuid`, `student_behavior`, `teacher_move`, `source` |
| `learning_components` | `case_uuid`, `ordinal`, `description`, `source` |

`NOTICE` lines 21 to 23, verbatim:

> The data under data/ca-math/ is a filtered derivative of the Learning Commons public
> export, retaining each record's `license` and `attributionStatement` fields. We do not
> use the gated Learning Commons API/MCP connector; only the openly-licensed export.

Measured: that sentence is accurate about `data/ca-math/*.jsonl`, which are the original records
unchanged in shape. It is not accurate about `data/k12-lesson-toolkit.db`. The design spec asserts the
stronger claim, §4 line 116, verbatim: "Every record carries `source` + `source_license` for
attribution compliance." Three of the four tables have no `source_license` column at all.

The consequence is operational: an attribution block cannot be assembled from the store. It has to
be built from the JSONL records, or from the host, and the string is per record.

### The California bridge, which is where most prerequisites come from

`ingest/builder.py` module docstring, verbatim:

> - **California bridge** — CA standards carry no ``buildsTowards`` (all 757 endpoints are
>   Multi-State CCSS). A CA standard C reaches the progression graph via the crosswalk
>   ``C --hasStandardAlignment--> E`` (highest ``jaccard`` first): backward-of(C) = prereq-of(E),
>   forward-of(C) = forward-of(E). If the chosen CCSS neighbour has exactly one CA standard that
>   crosswalks to it (a clean reverse crosswalk) we return that CA equivalent; otherwise the CCSS
>   neighbour verbatim. These rows are tagged ``source = SOURCE_BRIDGED``.

Measured: 788 bridged rows against 666 direct. And the primary-edge rule, verbatim:

> - **Primary edge selection** — ``buildsTowards`` carries no priority ranking, so when a node has
>   several prerequisites/next-standards the primary is the one with the lowest node identifier
>   (deterministic and stable across rebuilds). The store returns a single primary anyway.

So "the prerequisite" is one arbitrary-but-stable choice among possibly several, selected by
lexicographic identifier order. It is stable. It is not pedagogically ranked.

Separately, `relatesTo` edges are skipped and counted rather than mapped, because the model has
only backward and forward and no related-edge table. Measured at ingest: 284, matching the upstream
count exactly.

## Gotchas & constraints

**1. An empty result has several producers and they look identical.** Genuinely absent data, a
registered stub, a swallowed exception, and a server pointed at the wrong database file all return
the same typed-empty payload. Diagnose before recording. See [[trap-empty-facet-reads-as-success]].

**2. Never report 4,203 as a number of learning components.** It is attachments. The distinct
description count is 1,853, over 1,115 placements, with 41 as the maximum on any single placement.
Which number is right depends on the sentence, and the sentence has to say which grain it means.

**3. The MCP caps components at five with no flag, so the tool is not a census either.** See
[[trap-learning-components-truncated-at-five]] and [[concept-standard-placement-vs-code]].

**4. Do not attribute the derived prerequisites upstream.** More than half of every prerequisite
this store can serve is an edge this repository inferred through a jaccard-scored crosswalk. A page
saying "the store's prerequisites come from Student Achievement Partners" is imprecise: the
CCSS-side edge does, the California-side attachment does not.

**5. The repository document is wrong on its reason and this wiki does not fix it.** Record the
measured boundary, name the document as stale on this point, and leave the k12-lesson-toolkit repository
alone. Whether the correction is scheduled is the owner's call and belongs in that repository's own
commit. Same posture as [[evidence-k12-lesson-toolkit-acceptance-record]].

**6. Absence by filter is not absence of data.** The store holds California and Multi-State
mathematics only. A code from another jurisdiction or another subject is missing by construction,
and a lookup that returns nothing for it is reporting the filter, not a gap in the corpus.

**7. The 16,021 is a stated figure, not this project's re-parse.** Both it and the five label
counts come from the same upstream document, measured by its author from the raw export. The
staging agent did not re-parse the 292 MB `nodes.jsonl` to re-verify either. A page needing that
number independently should re-run the count and paste the command.

**8. `statement_text` is byte-identical to the export on this subset, and only on this subset.**
Measured `html_texts_stripped: 0`, so no record in the California or Multi-State math slice needed
HTML stripping. The upstream schema notes HTML does occur in other jurisdictions, so the guarantee
does not travel outside the filter.

**9. 283 standards rows have no code.** They are reachable by UUID, parent or progression and not
by code search, which is correct behaviour and not a defect. Do not read a code-search miss on
those as a store failure. See [[trap-code-form-silent-zero]].

## Related

- [[evidence-kg-coverage-and-gaps]] is the upstream side of this boundary: the whole-export label
  census, the licence census, and the structurally absent misconception layer.
- [[trap-empty-facet-reads-as-success]] owns the failure mode; this page owns the census that makes
  it diagnosable.
- [[trap-learning-components-truncated-at-five]] is the second reason a tool response is never a
  count.
- [[concept-standard-placement-vs-code]] is why a code resolves to several placements and why any
  per-code figure needs its resolution rule stated.
- [[trap-code-form-silent-zero]] is why a code lookup can return nothing without an error, which is
  the other way this boundary gets misread.
- [[concept-attribution-per-record]] is what the schema drop above makes structurally impossible to
  do from the store.
- [[source-learning-commons-kg]] is the rights verdict on the upstream export, including the
  revocation rider that makes a pinned local copy a dated artifact.
- [[evidence-k12-lesson-toolkit-acceptance-record]] is the same do-not-repair posture applied to a
  different stale repository document.
- [[trap-stale-stdio-mcp-server]] is why a change to any of this has to be verified against the
  spawned binary rather than an in-process import.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] consumes this boundary as its map of which calls can
  return data at all, and is where an empty result gets recorded as a boundary rather than written
  up as a finding.
- [[practice-assemble-an-attribution-block]] cannot be executed from the store, and this page is
  the measurement that says why: the per-record attribution string does not survive ingest.

## References

Local artifacts measured read-only by this project at staging on 2026-08-07, repository HEAD
`1ad5649dd4158c5a96a11561f678a2d877747000`:

- `data/k12-lesson-toolkit.db`. Row counts, jurisdiction
  split, distinct and empty code counts, the per-table column lists, and the bridged versus direct
  progression split.
- `src/k12-lesson-toolkit/mcp/server.py`. The three
  constant stubs at lines 217 to 237, the misconception handler, and the `_never_raise` wrapper
  applied to all seven registered tools.
- `src/k12-lesson-toolkit/ingest/builder.py`. The module
  docstring: the five populated files, the California bridge, the primary-edge rule, and the
  skipped `relatesTo` edges.
- `docs/reference/lc-export-schema.md`. §2.1 the
  label census, §2.2 the `im:` prefix and the 16,021 figure, §3.1 the edge counts, §7 the file
  table quoted above.
- `docs/reference/sourcing-verdict.md` lines 49 to
  52. The stale reason.
- `NOTICE` lines 21 to 23. The retention claim that
  is true of the JSONL and not of the database.
- The ingest re-run, executed into a scratch path at staging, whose counters match the committed
  store exactly.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/k12-lesson-toolkit-boundaries.md`, primary. §1 the store measurement and §1.1 the schema
  thinning; §2 what the store does not contain, including the three stubs verbatim; §3 the filter,
  the reproducible ingest run, the California bridge and the text handling; §4 the curriculum-layer
  contradiction with both readings and their reconciliation; §6 the per-layer attribution
  measurement.
- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §1 the seven-tool contract and the total-function
  rule; §2 code-form conventions and the 283 empty-code rows; §4 the component cap.
- `sources/host-learning-commons-kg.md`, primary. §10, the independent measurement of the same
  16,021-record Illustrative Mathematics attribution block and the contradiction it creates with
  the repository document named above.

This project's own measurement, cited as this project's and not as any outside party's statement:
every row count, column list, split and re-run counter above.
