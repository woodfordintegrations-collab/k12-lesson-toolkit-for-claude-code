---
title: Ground a lesson end to end
type: practice
sources:
  - sources/k12-grounding-and-render.md
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# Ground a lesson end to end

## Summary

The full grounding pass for one lesson: probe the connector, resolve the standard, batch the
dependent calls off its `caseIdentifierUUID`, then freeze the result into a bundle with provenance,
so every claim in the finished package names the node it came from.

The mistake this page exists to stop is not forgetting to call the tools. It is **finishing the pass
with a complete-looking package whose grounded sections were quietly filled from the model's prior.**
Against this store that is the default outcome, not an edge case, because four of the seven tools
return empty on every call and the skill's documented response to an empty is to draft from training
knowledge.

Measured, against this project's local store:

| Call in the mandated sequence | What it returns here | Why |
|---|---|---|
| `find_standard_statement` | real data | 2,303 standards rows |
| `find_standards_progression_from_standard` | real data | 1,454 progression rows |
| `find_learning_components_from_standard` | real data, capped at 5 | 4,203 component rows |
| `find_misconceptions_for_standard` | `{"misconceptions": []}`, always | 0 rows; source file is 0 bytes |
| `find_curriculum_lessons` | `{"lessons": []}`, always | registered stub |
| `find_materials_for_lesson` | `{"materials": []}`, always | registered stub |
| `list_standards_for_mathematical_practice` | empty, always | registered stub |

Three of the six mathematics steps therefore produce nothing to ground on. That is a documented
boundary, not a fault. It becomes a defect only when the package does not say so.

## When to reach for it

Reach for this page at the start of a lesson build, before any drafting, and again at the end when
the bundle is frozen. Those are the two moments where an ungrounded claim can still be caught.

Reach for it when an empty facet needs a decision: fill it from training knowledge and label it, fill
it from a cited outside source, or leave the section out. All three are legitimate. Doing one without
recording which is not.

Do not reach for this page for the mechanics of the first call. Code forms, the search cap, the
component slice and the placement problem are at [[practice-resolve-a-standard-code]], which this
procedure treats as its step 2 and does not repeat. Do not reach for it for the shape of the output:
the document set, the shared registry and the render invocation are at
[[practice-format-a-lesson-package]].

## How it works

**The pass is gated on a probe, not a handshake.** The skill's Step 0.3 checks whether the Learning
Commons tools are available in the conversation, and that check decides which path Step 2 takes.
`SKILL.md` Step 2, verbatim:

> **If the LC Knowledge Graph is connected:** follow the subject's section in
> `references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
> critical failure. Extract only what each call specifies, then proceed directly to Step 3 — do
> not summarize findings in chat.
>
> **If not connected:** draft from best knowledge and add this footer to the lesson plan:
> *"Generated without the Learning Commons Knowledge Graph. Standards and misconceptions reflect
> general best practice."* Do not invent KG citations or attribute content to curriculum
> materials you have not seen.

The disclaimer is a fixed string to be printed verbatim, and it is not one string. The
differentiation skill says "the Learning Commons KG" where planning says "the Learning Commons
Knowledge Graph", and science carries a third variant ending "Standards and OpenSciEd alignment
reflect general best practice." Copy the one belonging to the run you are in.

**One data dependency shapes the call graph.** The reference file's own rule, verbatim:

> The only cross-call data dependencies are the standard's `caseIdentifierUUID` (used by steps 2–5) and the `lessonIdentifier` that `find_curriculum_lessons` returns (used by `find_materials_for_lesson`). So: resolve the standard, then issue the step 2–4 calls and `find_curriculum_lessons` — each with its full parameters as specified below — as one parallel batch, then fetch materials.

One call, then a batch of four, then one. Not six in series.

**Every tool is total**, so a miss, a bad input and an internal exception all return the same typed
empty, with the exception text going to stderr only. The pass cannot detect its own failures from
the responses, which is why the checks below are positional rather than reactive.

## In practice

### Step 1. Probe, and record which path you took

Check tool availability before drafting. If the tools are absent, take the fallback path and print
the exact disclaimer string for your skill and subject. Do not invent KG citations and do not
attribute anything to curriculum materials you have not seen.

**Trap here: the probe is about availability, not about data.** A connector that is registered and
answering passes Step 0.3 while pointing at an empty database, because the server runs
`create_schema()` unconditionally at startup and then serves typed empties from every tool. Passing
the probe is not evidence that grounding will happen.

### Step 2. Resolve the standard

Full procedure at [[practice-resolve-a-standard-code]]. Come out holding three things: the verbatim
statement text, the `code`, and the `caseIdentifierUUID`.

**Trap here: this is where a whole package can be ungrounded and still render.** If the lookup fails
and nothing is written into `shared`, the renderer prints no target-standard callout at all.
`lesson_common.py` lines 324 to 329, verbatim:

```python
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
```

Either field alone produces the callout. With only a code, it prints its label and an empty
statement. With neither, the section is one block shorter and nothing marks the absence.

### Step 3. Issue the batch off the uuid

For mathematics, the reference file's numbered steps, verbatim in the parts that bind here:

> 2. **Prerequisite**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract: the single primary prerequisite standard, verbatim. Use in the LEARNING GOAL section. Non-negotiable — not naming the prior standard is a critical failure.
>
> 3. **Learning components**: Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill descriptions (unknown positions, problem types). Use directly as SWBAT bullets and as look-for row labels in the observation template. Discard the rest.
>
> 4. **Misconceptions**: Call `find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` → extract: the 3 most relevant misconceptions. For each keep only the student behavior and the teacher move, rewritten in your own words. If no results, draft 3 from training knowledge.

Issue steps 2, 3, 4 and `find_curriculum_lessons` as one parallel batch. `direction` is validated
against `frozenset({"backward", "forward"})`; anything else returns `{"standard": None}` rather than
an error.

**Trap here: "the prerequisite" is one deterministic choice among possibly several, and on this store
it is more often derived than found.** The upstream edges carry no priority ranking, so the primary
is the one with the lowest node identifier, stable across rebuilds and not pedagogically ranked. And
measured: 788 of the 1,454 progression rows are tagged
`Learning Commons KG v1.11.0 (via CA->CCSS crosswalk)` against 666 direct, because California
standards carry no forward edges of their own and reach the progression graph through a
jaccard-scored crosswalk. More than half of every prerequisite this store can serve is this repo's
own inference rather than an edge present upstream. Say so where it matters.

### Step 4. Read each empty for what it actually is

This is the step the page exists for. Three different things return `[]` here and they need three
different responses.

**Misconceptions: empty for every code, by upstream absence.** `data/ca-math/misconceptions.jsonl` is
0 bytes on disk while every sibling file in that directory is between 851,166 and 6,142,448 bytes,
and the `misconceptions` table has 0 rows. The upstream reason, from the export schema document,
verbatim:

> **Consequence:** the MCP's `find_misconceptions_for_standard` tool has no source data in the
> public export and must return empty; the skills fall back to training knowledge for
> misconceptions. `data/ca-math/misconceptions.jsonl` is written empty (0 records) as a defined,
> stable path.

So step 4's fallback clause, "If no results, draft 3 from training knowledge", fires on every
mathematics lesson built against this store. The three misconceptions in the finished package are
authored, not grounded. Label them that way in the bundle. This is the one place in the pass where a
tool reports success and the section depending on it is written entirely from the prior.

**Curriculum lessons and materials: empty by design, and the terminology rule still binds.** Both are
registered stubs, so step 5's extraction of activity names, problem types and discourse moves never
happens. What still applies is the sweep the reference file mandates when curriculum is not
confirmed, verbatim:

> **Curriculum-terminology check (if not IM-confirmed):** Before proceeding, scan your working notes and verify they contain zero mentions of "Illustrative Mathematics," "IM," any MLR name (MLR 1–8), "Compare and Connect," "Stronger and Clearer Each Time," or any IM lesson/activity title. Remove any that remain — a teacher who has not confirmed IM must not receive IM-specific terminology in the lesson or in chat (the same rule as SKILL.md's Copyright guardrail).

A stub returning nothing cannot introduce that terminology. A model drafting from its prior can, and
this sweep is the check that catches it.

**Learning components: real, and capped.** Five strings back is not a count. See
[[trap-learning-components-truncated-at-five]].

**A fourth possibility, invisible from the response: none of these.** An exception inside a handler
returns the same typed empty and nothing downstream distinguishes it. See
[[trap-empty-facet-reads-as-success]].

### Step 5. Freeze the bundle, and take its provenance from the export

Write the payload down before drafting: statement text, code, uuid, jurisdiction, prerequisite with
its direction and source stamp, components with the note that the list is capped, and an explicit
line for each empty facet naming which of the reasons above applies.

**Trap here: the store row cannot supply the attribution.** Measured, only the `standards` table has
a `source_license` column. `progressions`, `misconceptions` and `learning_components` carry a
free-text `source` string and no licence field, and **no table anywhere carries
`attributionStatement`.** The per-record attribution does not survive ingest. The repo's own `NOTICE`
states, verbatim:

> The data under data/ca-math/ is a filtered derivative of the Learning Commons public
> export, retaining each record's `license` and `attributionStatement` fields. We do not
> use the gated Learning Commons API/MCP connector; only the openly-licensed export.

Measured, that sentence is accurate about the JSONL files and not about `data/k12-lesson-toolkit.db`, which
is the artifact the MCP reads. So the attribution string comes from the export records or the staged
strings, not off the row you were served, and it differs by record type. Two of the five measured
forms, byte-exact:

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. California Mathematics standards provided by California Department of Education available at https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf.
```

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Learning Commons received learning components under CC BY-4.0 from Achievement Network.
```

The full set of five is at [[concept-attribution-per-record]]; the assembly step that ships them is
[[practice-assemble-an-attribution-block]]. Pin the export version and the fetch date alongside them,
because of the data-provider revocation rider. And note that the statement text of a CCSS standard is
not covered by the Learning Commons stamp alone: the upstream grant is narrower and mandates its own
notice. See [[source-corestandards-nga-ccsso]].

### Step 6. Verify the grounding survived into the artifact

The bundle is not the deliverable. Check that the target-standard callout is present and carries
statement text rather than only a code, that the prerequisite is named in the learning-goal section,
and that components appear as authored bullets rather than as a count.

**Trap here: a `from_shared` pointing at an unregistered key renders nothing, silently.**
`lesson_common.py` lines 331 to 335 return an empty block list for a value that is `None`, `""` or
`[]`, with no exception, no placeholder and no log. A misspelled key is indistinguishable from a
deliberate omission, and the section simply renders one block shorter.

## Gotchas & constraints

**1. The call order is mandated, not suggested.** Both skills state that not calling when connected
is a critical failure, and the differentiation skill adds that this holds however the source lesson
arrived: "Retrieving the lesson never satisfies this step."

**2. Two of the seven tools are documented as returning nothing for science, and the skill forbids
calling them.** `find_learning_components_from_standard` and
`find_standards_progression_from_standard` are named in the reference file as not returning data for
science standards. That is a documented empty-result contract, and it means the science pass is
structurally shallower than the mathematics one.

**3. `jurisdiction` is mandatory for social studies and optional elsewhere.** Social studies standards
live only under the state, never `Multi-State`. The differentiation skill's state-detection step
supplies a footer string for the science, math and ELA case where no state was found; the planning
skill has no equivalent step, and its state detection lives in each subject file's clarify section
instead.

**4. Whether this pass has ever been proven end to end is open in the record, and the two readings are
not reconciled.** The store repo's README leaves the acceptance checkbox unticked and its handoff
says, verbatim, "Not yet proven end-to-end that the skills ground". Two commits landed the same day
after those documents were frozen, both describing live grounding runs that found and fixed defects.
Neither records the acceptance procedure's four pass conditions being met. See
[[evidence-k12-lesson-toolkit-acceptance-record]].

**5. The misconception gap has a hand-authored counterpart this pass cannot reach.** Three
uncommitted files under `wiki/` in the store's repo hold hand-written misconception entries pinned to
California `case_uuid` values. The pin has no store side: 0 rows, 0 bytes. They are prose,
uncommitted, and unreachable through any tool.

**6. Nothing here was verified against the real Learning Commons connector.** Every measurement is
against this project's local store and the forked plugin files.

## Related

- [[practice-resolve-a-standard-code]] is step 2 in full, including the silent zero-row failure.
- [[trap-empty-facet-reads-as-success]] is the mechanism behind step 4: success and failure are
  identical in the response.
- [[trap-learning-components-truncated-at-five]] is why a five-item list is never a count.
- [[evidence-store-ingest-boundary]] is the census of what crosses the ingest boundary, including the
  `attributionStatement` loss step 5 works around.
- [[evidence-kg-coverage-and-gaps]] is what the upstream graph covers and where it is empty.
- [[evidence-k12-lesson-toolkit-acceptance-record]] holds the unresolved question in gotcha 4.
- [[concept-attribution-per-record]] is why the credit line is a property of the record.
- [[source-learning-commons-kg]] is the upstream grant, its version pin and its revocation rider.
- [[source-corestandards-nga-ccsso]] is the narrower upstream grant on the standard text itself.

## Composes with

- [[practice-format-a-lesson-package]] takes the frozen bundle as its input: `shared.standard_code`
  and `shared.standard_text` are the two fields the plugin's spec calls the acceptance core.
- [[practice-assemble-an-attribution-block]] consumes the per-record strings recorded in step 5 and
  turns them into the shipped attribution file.
- [[practice-format-an-assessment-artifact]] grounds on the same bundle and needs the components list
  with its truncation flag intact, because it drives item coverage.

## References

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-grounding-and-render.md`, primary. §1 the connector probe and the three verbatim
  disclaimer footers; §2.2 the mathematics call sequence, the parallel-batch rule and the terminology
  sweep; §2.4 the documented science empties; §2.5 the social-studies jurisdiction requirement; §2.7
  state detection; §3 the renderer's silent empty-value behaviour.
- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §1.3 the total-function rule and the per-tool
  empty payloads; §4 the component cap; §6.3 the unconditional `create_schema()`; §7 the direction
  validation.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §1 the row counts and per-table licence-column
  census; §2.1 the 0-byte misconceptions file and the upstream absence finding; §2.2 the four tools
  empty in v1; §2.4 the uncommitted human wiki; §3.3 the California bridge and the 788/666 split; §5
  the two readings of the acceptance record; §6.2 the five verbatim attribution strings; §6.4 the
  repo `NOTICE`.
- `sources/verdict-twelve-host-table.md`, reference. §1 row 3 for the version pin and revocation
  rider; §4.1 for the paired Learning Commons and NGA/CCSSO notices. Cited as this project's own
  adjudication, not as any outside party's statement.

Those extracts quote local files read on 2026-08-07: the k12-lesson-toolkit repository at git HEAD
`1ad5649`, and the k12-teacher-skills plugin skills tree, byte-identical to the installed 0.6.0
plugin.
