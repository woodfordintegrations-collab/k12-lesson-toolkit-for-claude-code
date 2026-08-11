---
title: Resolve a standard from a code
type: practice
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/k12-grounding-and-render.md
  - sources/k12-lesson-toolkit-boundaries.md
updated: 2026-08-08
---

# Resolve a standard from a code

## Summary

Turn a standards code into a grounded node: its verbatim statement text, its `caseIdentifierUUID`,
and the jurisdiction it was placed under. Six steps. What makes it worth a page is that every
failure along the path is silent, so the checks have to sit inside the call rather than be bolted on
downstream.

The one fact to carry away: **a zero-row result means the string you typed is not in the store. It
does not mean the standard has no data.** This project measured `G-SRT.6` at 0 rows and `HSG-SRT.6`
at 0 rows against the same store where `HSG-SRT.C.6` returns 4 rows. Neither miss raises an error, a
warning, or a partial match.

Three more silent failures on this one path: a plausible statement from the wrong grade band (the
search missed, and the skill's cap counts it as a miss); a thin node whose statement is right and
whose grounding data is empty (you landed on a placement a sibling outranks); and exactly five
sub-skills back (the tool sliced the list and said nothing). Each is handled at the step where it
bites.

## When to reach for it

Reach for this page whenever a code is about to be typed into `find_standard_statement`, and
whenever an empty grounding result has to be read as either an absence of data or an absence of a
match. Those two readings look identical at the call site, and telling them apart is the job here.

Reach for it before writing any count of a standard's components or sub-standards into a document.
The tool response is not a census.

Do not reach for this page for the wider grounding pass. The full call sequence for one lesson, the
batching rule, and what to do with facets that come back empty by design live at
[[practice-ground-a-lesson-end-to-end]]. This page ends the moment a resolved node is in hand. Do
not reach for it for what a standard says: this wiki does not restate standards content.

## How it works

**1. The match is exact-or-dotted-descendant, with no normalisation.** `repository.py` lines 269 to
286, verbatim as staged:

```python
        sql = "SELECT * FROM standards WHERE (code = ? OR code LIKE ? ESCAPE '\\')"
        params: list[str] = [code, _escape_like(code) + ".%"]
```

A leaf code returns itself; a parent returns itself plus every dotted descendant. The caller's string
is compared to the stored string, with no code-form normalisation anywhere on the path. Optional
`academicSubject` and `jurisdiction` filters narrow the result. Measured with that same predicate:
`G-SRT.6` 0 rows, `HSG-SRT.6` 0 rows, `HSG-SRT.C.6` 4 rows, `HSG-SRT` 68 rows.

**2. A code lives once, but a standard lives many times.** Measured: 794 distinct non-empty codes,
of which 693 resolve to more than one placement, with a maximum of 7. Data is authored against some
placements and not others, so a raw query can return a node whose statement is right and whose
grounding data is empty. `dedupe_richest` collapses same-code duplicates to one representative
ranked by grounding score (a backward edge, a forward edge, the component count), tie-broken by
California jurisdiction and then by the smallest `case_uuid`. `select_by_code` does the same for a
single facet, so a bare code reaches the sibling holding the datum asked for. See
[[concept-standard-placement-vs-code]].

**3. Every tool is a total function.** `server.py` lines 9 to 10, verbatim:

> - Every tool is a **total function**: on any miss or bad input it returns an empty/typed-empty
>   result and NEVER raises. The skills forbid surfacing errors to teachers.

The `_never_raise` wrapper prints the exception to stderr and hands back the per-tool empty payload,
`{"standards": []}` here. From the response alone, a genuine empty and a swallowed exception are
identical. See [[trap-empty-facet-reads-as-success]].

## In practice

### Step 1. Write the code in the store's own form, before anything else

The form this store carries for the high-school similarity family is `HSG-SRT.C.6`: hyphen after
`HSG`, cluster letter before the number.

**Trap, and it bites at the keystroke.** `G-SRT.6` and `HSG-SRT.6` both return **0 rows and no
error**, indistinguishable from a code that genuinely has no data, and both are the forms a
competent person writes from memory or copies off a publisher's page. Hosts publish their own forms:
EngageNY tags its Geometry Module 2 as `G.SRT.1-8`. That is the host's string, not the store's. See
[[trap-code-form-silent-zero]].

No fallback rescues you, because of what happens at ingest. `ingest/builder.py` line 181, verbatim:

```python
        code = props.get("statementCode") or props.get("alternateStatementCode") or ""
```

The alternate is only reached when `statementCode` is absent. Measured on the CA-math subset, 509
records carry an alternate form and all 509 also carry a canonical one, so every alternate is
discarded at ingest and none is queryable.

One measured oddity to catch by eye rather than by prefix: this store's SRT family contains
`HSG.SRT.C.8.1`, which uses a dot where every sibling uses a hyphen. It is a California-specific
addition and a different string, so no `HSG-SRT` prefix probe reaches it.

### Step 2. Call with the filters, and know what a filter can do

Call `find_standard_statement(code=<code>, academicSubject="Mathematics", jurisdiction="<state>")`.
The subject literal for ELA is `"English Language Arts"`, not `"ELA"`.

Filter values match case-insensitively, and a code-only fallback fires when a filter empties an
otherwise-valid code. Two things that fix does **not** do: the `code` comparison is untouched and
stays byte-exact, and the fallback only fires when at least one filter was supplied. A wrong code
returns empty from both attempts.

### Step 3. Read a zero result as a miss, and spend the cap deliberately

The plugin's rule, `references/learning-commons-kg.md` lines 23 to 27, verbatim:

> **Cap at 3 search attempts total.** Results from the wrong grade band or course count as
> a miss — a high-school US History request answered with elementary codes means the search
> terms missed, so spend the remaining attempts with different keywords (the course name,
> the era, the standard family) rather than falling back early. If no usable standard after
> 3 calls to `find_standard_statement`, stop searching — proceed with the best-matching
> standard from training knowledge for the grade and topic, and add the partial-coverage
> footer to the lesson plan. Never call `find_curriculum_lessons` to locate a standard.

**Trap here: a wrong-grade-band hit reads as a success and is not one.** A plausible elementary
standard returned for a high-school request has consumed one of three attempts. Keyword search is an
OR match over `statement_text`, capped at 25 results with blank-code container nodes dropped first,
so a real hit comes back carrying a real `code` you can feed straight back into a code search. That
is the intended recovery route.

Two things the cap paragraph does not supply, both measured: the "partial-coverage footer" it names
is never given as a string anywhere in the file, and `find_curriculum_lessons` returns `[]` on every
call against this store anyway.

### Step 4. Extract exactly three fields, and take the statement byte-for-byte

Take the verbatim statement text, the `code`, and the `caseIdentifierUUID`, which the plugin calls
"required for all subsequent calls". The text is safe to take literally: measured at ingest,
`html_texts_stripped: 0` for this subset, so `statement_text` is byte-identical to the export's
`properties.description` on all 2,303 rows, LaTeX included.

**Trap here: the field named `caseIdentifierUUID` is not the CASE id.** The upstream export carries
two UUIDs per standard and the schema document records that they never coincide (0 of 222,865
equal). The MCP deliberately returns the Learning Commons node `identifier` in the field it names
`caseIdentifierUUID`. It is a stable join key inside this system, and it is not the external
IMS/CASE identifier a reader will assume. Do not publish it as one.

### Step 5. Never take a count off a tool response

`server.py` line 48 declares `MAX_LEARNING_COMPONENTS = 5` and line 213 slices to it. The response is
a bare list of strings: no count, no total, no `truncated` flag. A caller holding five strings cannot
tell whether the standard has five components or forty-one.

Measured: 1,115 placements carry at least one component, 183 carry more than five, and the maximum
on one placement is 41. For the five HSG-SRT codes this project works on, the richest placement per
code carries B.4 7, B.5 6, C.6 3, C.7 1, C.8 8. Three of the five are silently truncated.

The repository layer returns everything, ordered by `ordinal`; the cap lives entirely in the MCP
layer. So a count that will appear in a document comes from the store, and it is stated as the
deduped store count rather than as "the standard has N components". See
[[trap-learning-components-truncated-at-five]].

### Step 6. Thread the uuid, or pass the bare code knowing what changes

`_resolve_uuid` accepts either. A non-empty uuid wins. Otherwise a bare code resolves per facet, so a
progression call lands on the sibling holding a directional edge while a components call lands on the
sibling holding components, which may be two different nodes. That is designed behaviour and it is
why a bare-code caller still reaches data. Record which route you took, because the two can return
facets from different placements of the same code.

## Gotchas & constraints

**1. Silence has at least three upstream causes that look the same.** A typed empty can mean a wrong
code form, a swallowed exception, or a server pointed at the wrong database. `create_schema()` runs
unconditionally at startup, so a server whose `OVEREDUCATED_DB` points at a missing or empty file
starts successfully and every tool returns its typed empty. Check the environment before concluding
anything about the data.

**2. Verification against `src` proves nothing about the running server.** The install is editable, a
bare path append to `src`. A new spawn of `.venv/bin/k12-lesson-toolkit-mcp` picks up whatever is in `src`
at that moment; an already-running process does not, because Python binds the module at import time.
The in-repo suite (68 tests, run at staging) imports `build_server` directly and never exercises the
spawned binary, so all 68 green tests say nothing about the connector a session is talking to. See
[[trap-stale-stdio-mcp-server]].

**3. Only one of the two skills on this path bounds the search.** Measured by grep across the whole
plugin skills tree, the three-attempt cap appears in exactly two lines, both in the lesson-planning
skill's KG reference. The differentiation skill's copy of the same section is word-for-word identical
through the `subStandards` paragraph and then stops: no cap, no wrong-grade-band rule, no
prohibition on `find_curriculum_lessons`. Inside a differentiation run the cap is a convention you
are choosing, not one the skill imposes.

**4. Two structural facts that stop a result being read as a gap.** `subStandards` is unioned across
all same-code placements and then deduped, because a childless placement can win the representative
and drop the subtree, so a sub-standards list is a property of the code rather than of the node. And
283 of 2,303 standards rows carry no code at all: unlabeled sub-parts, reachable by uuid, parent or
progression, never by code search.

**5. The C.7 shortfall in this store is real, local, and not a statement about the world.** The store
decomposes `HSG-SRT.C.7` into a single learning component covering "use", while the standard's own
text says "Explain and use", so the "Explain" verb has no scaffold here. That measurement is not
evidence that C.7 material is scarce, and this project made exactly that generalisation once and
retired it. See [[evidence-c7-store-gap-not-corpus-gap]].

**6. Nothing here was verified against the real Learning Commons connector.** Every measurement is
against this project's local store and the forked plugin files, and the local server's response field
names are recorded in its own source as reasonable defaults to reconcile when the real export lands.

## Related

- [[trap-code-form-silent-zero]] is step 1's failure worked through, with the ingest-level reason the
  alternate form is never indexed.
- [[trap-learning-components-truncated-at-five]] is step 5's cap, and why five items is not a count.
- [[trap-empty-facet-reads-as-success]] is the mechanism that makes success and failure identical in
  the response.
- [[trap-stale-stdio-mcp-server]] is gotcha 2: a green test suite and a running connector are
  different claims.
- [[concept-standard-placement-vs-code]] holds the placement-versus-code distinction this page
  applies.
- [[evidence-c7-store-gap-not-corpus-gap]] separates the measured local scaffold gap from the retired
  scarcity claim.
- [[source-learning-commons-kg]] is the upstream this store was built from, where the per-record
  licence and attribution live.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] opens with this procedure as its step 2 and batches every
  other call off the `caseIdentifierUUID` it returns.
- [[practice-format-a-lesson-package]] consumes the statement text and code as
  `shared.standard_text` and `shared.standard_code`, which the plugin's own spec calls the acceptance
  core: if those two are wrong or missing, the authored JSON breaks.

## References

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §1 the total-function rule; §2 the `find_by_code`
  SQL, the measured code probes and the alternate-code discard; §3 `dedupe_richest`,
  `select_by_code` and the measured placement multiplicity; §4 the component cap and its measured
  bite; §5 the case-sensitivity fix and its two limits; §6 the editable install and the test-suite
  gap; §7 the two-UUID note and the keyword-search caps.
- `sources/k12-grounding-and-render.md`, primary. §2.1 the three-attempt cap verbatim and the
  measured grep showing it exists in exactly two lines; §2.3 the ELA subject literal.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §1 the measured row counts; §3.4 the measured
  `html_texts_stripped: 0`.

Those extracts quote local files read on 2026-08-07 at k12-lesson-toolkit git HEAD `1ad5649`
(`repository.py`, `mcp/server.py`, `ingest/builder.py`, `data/k12-lesson-toolkit.db`) and the
k12-teacher-skills plugin skills tree, confirmed byte-identical to the installed 0.6.0 plugin by
`diff -r -q --exclude=__pycache__`, exit 0. Every number above is this project's own measurement, not
any outside party's statement.
