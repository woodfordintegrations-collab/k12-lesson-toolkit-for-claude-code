---
title: "observation_template layout"
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-block-types.md
  - sources/k12-grounding-and-render.md
  - sources/k12-lesson-toolkit-store-and-mcp.md
updated: 2026-08-08
---

# observation_template layout

## Summary

`observation_template` is the teacher's clipboard page. It is one of the three document ids
`k12-lesson-planning` names as the minimum set, its `audience` is `teacher`, and its four
sections are prescribed by the subject reference file rather than by `SKILL.md`. The headings,
byte-exact from `references/math.md`: `How to use this`, `Look-fors`, `Anticipated challenges`,
`Exit-ticket sort`.

Three things are not obvious from the vendor documentation and are why this page exists:

1. The layout block in `math.md` names **three** `from_shared` pulls. The worked example ships
   **four**, because the exit-ticket sort criteria live in a second registered key, `exit_sort`,
   that the layout block never mentions. Follow the layout literally and the three bucket
   criteria never reach the teacher.
2. `blank_rows` is not the only field the renderer accepts for the note grid. `rows` as a bare
   integer is equivalent, `cols` is honoured, and **with neither, the default is 3 rows, not 8**.
3. Every `from_shared` pull here fails silently. A misspelled or unregistered key returns an
   empty block list with no exception, no placeholder and no log line, so a look-fors section
   reduced to a blank grid renders as a finished page.

This is a shape contract, not a rights document; for what may be quoted or republished see
[[concept-cite-quote-adapt]].

## When to reach for it

Reach for it when authoring the `observation_template` entry of a `lesson.json`, when checking a
rendered package for completeness, or when a lesson's KG grounding came back thin and you need
to know what this page looks like with an empty registry key underneath it.

Reach for it also when deciding **where the sort criteria go**. `math.md` requires all three
bucket criteria to appear in the lesson plan, never truncated to labels. This page is where they
land in front of the teacher who is actually sorting the papers, and the two requirements are
not the same requirement.

Do not reach for it for the `lesson_plan` section list, which is [[k12-lesson-plan-sections]],
or for the worksheet, which is [[k12-student-materials]]. The `k12-lesson-differentiation`
skill's fixed four-document set contains no observation template at all.

## How it works

### The vendor bullet, verbatim

`k12-lesson-planning/SKILL.md` lines 338 to 339, one of the three minimum-set bullets:

> - `id: "observation_template"` (`audience: "teacher"`) — how-to-use, look-fors,
>   misconceptions, a `fill_table` for student notes, and the exit-ticket sort.

That bullet is the whole of what `SKILL.md` says. The layout is in the subject reference file,
and loading that file is mandatory; see [[k12-lesson-plan-sections]].

### The layout block, verbatim from references/math.md lines 150 to 159

> **Observation template layout** (the `id: "observation_template"` document):
>
> ```
> sections:
>   "How to use this"        one-paragraph instructions
>   "Look-fors"              from_shared:look_fors
>                            fill_table headers=[Student, Strategy seen, Next step] blank_rows=8
>   "Anticipated challenges" from_shared:misconceptions
>   "Exit-ticket sort"       from_shared:exit_ticket
> ```

### What the other three subjects change

- **ELA**, `references/ela.md` line 226, verbatim: "**Observation template layout** matches the
  math layout in `references/math.md`."
- **Social studies**, `references/social_studies.md` lines 196 to 197, verbatim:
  "**Observation template layout**: as in `references/math.md`, with `fill_table` headers
  `[Student, Evidence of thinking, Instructional move]`."
- **Science**, `references/science.md` lines 177 to 178, verbatim: "- In the observation
  template, prefix each look-for with its dimension so the teacher sees which one they're
  watching for." No header override is given.

Only social studies overrides the grid headers. Science changes the look-for text instead.

### The realised example ships four pulls, not three

`references/example_lesson.json` `documents[3]` is `audience: teacher` with the four headings
above. Its two decisive sections, reproduced from the staged extract:

```json
  {"heading": "Look-fors",
   "blocks": [{"type": "from_shared", "key": "look_fors"},
              {"type": "fill_table", "headers": ["Student", "Strategy seen", "Next step"], "blank_rows": 8, "row_height_pt": 26}]},
  {"heading": "Exit-ticket sort",
   "blocks": [{"type": "from_shared", "key": "exit_ticket"},
              {"type": "from_shared", "key": "exit_sort"}]}
```

`How to use this` is one `paragraph` and `Anticipated challenges` is one
`from_shared: misconceptions`.

`exit_sort` is registered separately, as a `cards` block whose three items are `Got it`,
`Almost there` and `Needs re-teaching`, each carrying a criteria sentence rather than a bare
label. `math.md` line 99 is the rule those criteria satisfy, verbatim in part: "3 sort buckets
*Got it* / *Almost there* / *Needs re-teaching*, **each with explicit criteria** describing
what a response in that bucket contains ... all three criteria appear in the lesson plan, never
truncated to labels."

## In practice

### Author it as four sections with four pulls

- `How to use this`: one `paragraph`. Under [[k12-density-rules]] a paragraph is at most three
  sentences, and the example's is three.
- `Look-fors`: `from_shared: look_fors`, then the `fill_table`. Set the row count explicitly.
- `Anticipated challenges`: `from_shared: misconceptions`.
- `Exit-ticket sort`: `from_shared: exit_ticket`, then `from_shared: exit_sort`.

### The grid's fields, from the renderer rather than the schema fence

`SKILL.md`'s schema fence publishes `{type: fill_table, headers[], blank_rows: int,
row_height_pt?}`. `render_lesson_docx._emit_fill_table` accepts more, measured from the code
staged verbatim:

| Field | In the fence | Behaviour |
|---|---|---|
| `headers[]` | yes | Column count comes from the header list |
| `blank_rows` | yes | Row count, clamped to `min(max(1, n), 50)` |
| `rows` as an int | no | Equivalent to `blank_rows`, same clamp |
| `rows` as a list | no | Renders filled cells; truncated at 50 |
| `cols` | no | Used only when `headers` is empty, capped at 12 |
| `row_height_pt` | yes | Forwarded to the table emitter |
| `empty_row_height_pt` | not for `fill_table` | Forwarded alongside `row_height_pt` |

With neither `blank_rows` nor `rows` the default is 3. The expression, verbatim from the staged
code, is `n = int(blk.get("blank_rows") or rows_val or 3)`.

### Row height on a teacher page is a flat 36 points

`lesson_common.table_row_height` returns `explicit or 36.0` for a non-student document. This
page's `audience` is `teacher`, so the grade band never sizes its rows and the 40 point floor
protecting student writing space does not apply. That is why the example can set
`row_height_pt: 26` and get 26. The same block on a student page would be floored at 40.

### Look-for row labels come from the KG, and the tool truncates

`references/learning-commons-kg.md` step 3, verbatim: "Call
`find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill
descriptions (unknown positions, problem types). Use directly as SWBAT bullets and as look-for
row labels in the observation template."

The cap lives in the MCP layer, not the store: `server.py` line 48 declares
`MAX_LEARNING_COMPONENTS = 5`, line 213 slices with it, and the response carries no count, total
or truncation flag. For this project's five codes the richest placement carries `HSG-SRT.B.4` 7,
`HSG-SRT.B.5` 6, `HSG-SRT.C.6` 3, `HSG-SRT.C.7` 1, `HSG-SRT.C.8` 8, so three of five are
silently truncated. Never state a component count from the tool response. See
[[trap-learning-components-truncated-at-five]].

## Gotchas & constraints

**1. Following `math.md` literally drops the sort criteria.** The layout block names
`from_shared:exit_ticket` and stops. `exit_ticket` is the prompt and its teacher note; the three
bucket criteria are a different key, `exit_sort`. A template built to the layout block alone
gives the teacher a prompt and no way to sort. The two vendor artifacts disagree in scope.

**2. Every pull here is silently optional.** `expand_from_shared` returns `[]` when the key is
missing, `None`, `""` or `[]`, with no warning anywhere. A typo in `look_fors` renders the
section as a bare blank grid, which looks like a deliberate design choice. See
[[trap-empty-facet-reads-as-success]].

**3. Omitting the row count gives you 3 rows for a class of 30, and `rows` is a second spelling
of the same field.** The reference says `blank_rows=8`; the renderer's default is 3; nothing
reconciles them and nothing errors. An author who writes `rows: 8` gets eight blank rows, though
the schema fence gives no reason to expect that. `rows: [[...]]` as a list is a different block
entirely, rendering filled cells.

**4. A `student` facet that is a callout does not get the "Students see" treatment.**
`_facet_text` returns the empty string unless every block in the facet is a `paragraph` or a
`list`. `example_lesson.json` registers `exit_ticket.student` as a `callout`, so here it renders
as the raw callout instead. Teacher-page rendering depends on the facet's shape, not its content.

**5. Nothing checks that the buckets partition the responses.** `SKILL.md`'s "Everything
matches" block requires each example response to fit exactly one bucket and equivalent forms of
one answer to sit together. No script in either skill enforces it. See
[[k12-package-consistency]].

**6. `audience` is a strict string test and it splits.** An omitted `audience` defaults to
`"teacher"`, but `theme.student_doc` is set by `data.get("audience") == "student"` while
`expand_document` branches on `audience != "teacher"`. Write the literal `"teacher"` here.

**7. Science's dimension prefix is an instruction about look-for text, not about the grid.**
`science.md` gives no header override, so a science observation template keeps
`[Student, Strategy seen, Next step]` unless the author decides otherwise, and that decision
is the author's, not the vendor's.

**8. Unverified from here: nothing on this page was rendered.** The staged extracts were read
from local files at 2026-08-07 21:15 PDT and no render was executed. Every claim above is a
claim about what the source code and reference files say, not about observed output. What would
close it: run `render_all.sh` on `example_lesson.json` and inspect `observation_template.docx`.

## Related

- [[k12-document-set]] holds the required ids and the `documents[]` array this is one entry of.
- [[k12-shared-registry]] holds `from_shared`, the facet rules, and the empty-value behaviour
  that makes the four pulls here silently optional.
- [[k12-block-types]] holds the block vocabulary, including `fill_table` and `cards`.
- [[k12-lesson-plan-sections]] is where the same look-fors, misconceptions and exit ticket must
  also appear in the teacher's plan, a separate obligation.
- [[k12-student-materials]] is the other faceted consumer of these keys, and where the 40 point
  row floor and grade-band sizing do apply.
- [[k12-density-rules]] binds the one-paragraph "How to use this" section.
- [[k12-package-consistency]] holds the bucket-partition rule that nothing checks.
- [[trap-empty-facet-reads-as-success]] is the worked failure behind gotcha 2.
- [[trap-learning-components-truncated-at-five]] is why a look-for count from the MCP response
  is not a count.

## Composes with

- [[practice-format-a-lesson-package]] is the end-to-end authoring procedure this document is
  one step of, and where the four-pull correction has to be applied.
- [[practice-ground-a-lesson-end-to-end]] supplies the look-fors and misconceptions this page
  pulls, and is where the truncation cap is handled before the value reaches `shared`.

## References

Staged extracts in this wiki, all staged 2026-08-08 from local files read at 2026-08-07 21:15
PDT. Local files, so no HTTP status exists.

- `sources/k12-plugin-contract.md`, primary. §1.2 the three minimum ids; §4 the layout block from
  `references/math.md` 150 to 159, the three subject overrides, and the realised `documents[3]`;
  §4.2 `_emit_fill_table` verbatim; §3.1 the `math.md` line 99 sort-bucket rule.
- `sources/k12-block-types.md`, primary. §4.2 `table_row_height`, the 36.0pt teacher constant and
  the 40.0pt student floor.
- `sources/k12-grounding-and-render.md`, primary. §2.2 the KG call naming learning components as
  look-for row labels; §3.1 the silent empty-key return; §3.4 `_facet_text` and the callout case;
  §3.5 the two different `audience` string tests.
- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §4.1 `MAX_LEARNING_COMPONENTS = 5` at line
  48, §4.2 the slice at line 213, §4.4 the per-code component counts.

Underlying vendor files, cited as the staged extracts cite them, under
`k12-teacher-skills/plugin/skills/k12-lesson-planning/`: `SKILL.md`, `references/math.md`,
`ela.md`, `science.md`, `social_studies.md`, `learning-commons-kg.md`, `example_lesson.json`,
`scripts/lesson_common.py`, `scripts/render_lesson_docx.py`. Plugin 0.6.0, measured
byte-identical to the installed copy by `diff -r -q --exclude=__pycache__`, exit 0.
