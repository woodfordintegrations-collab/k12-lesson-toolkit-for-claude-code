---
title: The shared registry and audience faceting
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - sources/k12-block-types.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/lesson_common.py
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/example_lesson.json
updated: 2026-08-08
---

# The shared registry and audience faceting

## Summary

`shared` is the top-level key that stops two documents in a package from drifting apart.
Register content once under a key you choose, pull it into each document with
`{"type": "from_shared", "key": "…"}`, and every page that pulls that key gets the same content,
faceted by the page's `audience`.

Three things about it are load-bearing and none of them is obvious from the schema fence:

1. **Eight keys are identity, not content.** `_IDENTITY_KEYS` is
   `{"grade", "subject", "duration", "curriculum", "standard_code", "standard_text",
   "prerequisite_standard", "smps"}`. Pulled with `from_shared`, an identity key renders as a
   bare paragraph of its `str()`, never as blocks.
2. **`standard` is the only special key**, and it is the one that assembles the single verbatim
   standard quotation the whole licensing layer hangs on. See [[k12-density-rules]].
3. **A missing, `None`, `""` or `[]` value returns an empty block list with no warning.** A
   misspelled key is byte-identical in its effect to a deliberate omission.

There is also a documented contradiction. On a student page, SKILL.md says the `student` facet
renders "after any `stimulus` blocks"; the code prepends it, so the order that prints is student
then stimulus. **The code governs what prints.** Both are quoted below.

## When to reach for it

Reach for this page when you are deciding **where a piece of content lives**: in `shared` or
inline in one document. The rule is mechanical, not stylistic. Anything that appears on more than
one page goes in `shared`, because that is the only thing preventing a revision from updating one
page and not the other.

Reach for it when a block you registered does not appear on the rendered page. The silent-empty
behaviour below is the first thing to check, ahead of the renderer.

Reach for it when you are writing a task that some students do orally. `student: null` is the
supported way to keep a task off the worksheet, and it is not a workaround.

## How it works

Every quotation below is staged byte-exact in `sources/k12-plugin-contract.md` and
`sources/k12-grounding-and-render.md`, from the named file and line range, read at 2026-08-07
21:15 PDT. Local files, no HTTP status. `lesson_common.py` is byte-identical under both skills at
the same line numbers.

### What the vendor publishes

`SKILL.md` lines 312 to 329, verbatim, opening and the facet rule:

> **`shared` is a content registry.** It always carries the lesson identity — `grade`,
> `subject`, `duration`, `standard_code`, `standard_text` (and `curriculum`,
> `prerequisite_standard`, `smps[]` when applicable). Beyond that, register any content that
> appears on more than one page under a key you choose: a problem as `p1`, a source as
> `stamp_act_petition`, a data set as `prices_table`. A key's
> value can be a string, a single block, a list of blocks, or a faceted object
> `{teacher: …, student: …, stimulus: [blocks]}`. On a **student** page, only the `student`
> facet (after any `stimulus` blocks) renders — a `student` of `null` means nothing prints
> there, which is how oral or teacher-led tasks stay off the worksheet. On a **teacher** page,
> both facets render: the teacher facet as plain script, then the student facet as one
> "Students see" line, so the teacher reads their own script and the exact prompt
> students will work from.

`SKILL.md` lines 345 to 350, verbatim:

> Inside any document, pull registered content with `{"type": "from_shared", "key": "…"}` —
> the same key on two pages renders the same content (faceted by audience). Adding
> `"label": "1"` to a `from_shared` block renders the pulled text as a numbered item on one
> line. Within a single document, pull each key once (a reference table, an exit-ticket
> protocol, a word list appears in one section only). Content that appears on only one page
> can be written inline.

### The eight identity keys, from the code

`scripts/lesson_common.py` lines 236 to 238, verbatim:

```python
# Keys in `shared` that are document/identity metadata, never expanded as content blocks.
_IDENTITY_KEYS = {"grade", "subject", "duration", "curriculum", "standard_code",
                  "standard_text", "prerequisite_standard", "smps"}
```

`expand_from_shared` lines 334 to 335, verbatim, is what makes them different:

```python
    if key in _IDENTITY_KEYS:
        return [{"type": "paragraph", "text": str(val)}]
```

Eight keys, spelled exactly as above. `smps` is the key name, not `smps[]`; the schema fence
writes `smps[]?` to indicate a list value, which is a type annotation and not part of the key.

### `standard` is the only special key

`lesson_common.py` lines 324 to 329, verbatim:

```python
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
        return [{"type": "callout", "kind": "special",
                 "label": f"{shared.get('standard_code', '')} — Target standard".strip(" —"),
                 "text": shared.get("standard_text", "")}]
```

Either field alone produces the callout. With only a code, the box prints its label and no
statement. With only text, the label strips down to `Target standard`. With neither, no
target-standard callout is produced **and the package still renders complete**.

### Empty and absent values

`expand_from_shared` lines 331 to 333, verbatim:

```python
    val = shared.get(key)
    if val is None or val == "" or val == []:
        return []
```

`_as_blocks` lines 250 to 251, verbatim, does the same for a facet: `if v is None or v == "": return []`.

## In practice

**The faceted object.** A key's value may be a string, a single block, a list of blocks, or
`{teacher: …, student: … or null, stimulus?: [blocks]}`. What renders per audience:

| Audience | What prints from a faceted key |
|---|---|
| `student` | the `student` facet, then `stimulus`. Teacher script never reaches the worksheet. |
| `teacher` | `stimulus`, then the teacher facet as an `instructions` block, then the student facet as one `labeled` block whose label is the literal string `Students see`. |

`_faceted()` lines 277 to 292, verbatim, including its own docstring:

```python
def _faceted(val: dict, audience: str) -> list[dict]:
    """Expand a {teacher?, student?, stimulus?} value.

    Student pages: student facet, then stimulus — the worksheet reads task-then-surface —
    and nothing else: teacher script never reaches the worksheet, and a null/absent
    student facet renders nothing (so oral/teacher-led tasks leave no trace).

    Teacher pages: stimulus + teacher facet as plain script, then the
    student facet as ONE quoted "Students see" line — the teacher reads their own script and
    the exact prompt students will work from, the way a printed teacher edition shows both.
    Neither facet is a callout: callouts are reserved for the few moments a teacher must not
    miss, and a page where every task is boxed highlights nothing."""
    out: list[dict] = list(_as_blocks(val.get("stimulus")))
    if audience != "teacher":
        out[:0] = _as_blocks(val.get("student"))
        return out
```

**Numbering a pulled problem.** `{"type": "from_shared", "key": "p1", "label": "1"}` folds the
label into the first text-bearing block so the number and the prompt render on one line. The fold
scans past leading diagram blocks and dispatches on the block's FIELDS (`label`, `text`, `items`)
rather than on its type name, because the type name changed once before and broke the earlier
version. A label never renders alone.

**Pull each key once per document.** This is a vendor rule, quoted above, and it is the reason a
reference table or a word list appears in exactly one section of a page.

## Gotchas & constraints

**1. The facet order in the documentation contradicts the code, and the code wins.** SKILL.md
lines 318 to 319 say the student page renders "only the `student` facet (after any `stimulus`
blocks)". `_faceted()` line 291 is `out[:0] = _as_blocks(val.get("student"))`, and `out[:0] = ...`
is a **prepend**, so the printed order is student facet then stimulus. The function's own
docstring agrees with the code: "Student pages: student facet, then stimulus". Both statements
are quoted verbatim above. This is a vendor documentation defect at version `0.6.0`, recorded here
rather than resolved by preference: if you author a stimulus expecting it to sit above the task,
it will print below it.

**2. A misspelled key is indistinguishable from a deliberate omission.** A `from_shared` pointing
at a key that was never registered returns `[]`. No exception, no placeholder, no log line, no
non-zero exit. The section renders one block shorter and looks finished. `p6` written where `p5`
was registered removes a problem from the worksheet and from the plan simultaneously, which is
the failure mode `shared` was supposed to make impossible. The parallel reading error on the
grounding side, an empty MCP result that reports success, is [[trap-empty-facet-reads-as-success]].

**3. A failed standard lookup produces no target-standard callout and still renders.** With
neither `standard_code` nor `standard_text` set, `expand_from_shared` returns `[]` for the
`standard` key. The `At a glance` section simply has one fewer block. Since that callout is the
single place the standard is quoted verbatim, its absence also removes the anchor the NGA/CCSSO
notice and the per-record attribution attach to. See [[k12-density-rules]] and
[[source-corestandards-nga-ccsso]].

**4. The teacher-page rendering of a task depends on the SHAPE of the student facet, not its
content.** `_facet_text` returns `""` unless every block is a `paragraph` or a `list`. So a
`student` facet written as a `callout` block, which is exactly the shape `example_lesson.json`
uses for `exit_ticket`, does **not** get the `Students see` label on the teacher page; it renders
as the raw callout instead. Two tasks authored the same way except for facet shape print
differently on the plan.

**5. The teacher facet becomes an `instructions` block, a type the schema fence never publishes.**
`_faceted()` line 301 is `out.append({"type": "instructions", "text": t})`. A lesson authored
strictly from the published schema therefore contains block types its author never wrote. The
five canonical types the planning fence omits are listed in [[k12-block-types]].

**6. An identity key pulled as content collapses to `str(val)`.** `{"type": "from_shared",
"key": "smps"}` renders a Python list's `str()` into the document, brackets and quotes included.
Identity keys are for the renderer and for `answer_profile`, not for pulling. Note that `smps`
being truthy is also the primary math signal for grade-band writing-space sizing; see
[[k12-student-materials]].

**7. `audience` is tested two different ways, and a typo splits them.** `expand_document` tests
`audience != "teacher"` while `theme.student_doc` is a strict `== "student"`. A value of
`"Student"` is treated as non-teacher by the facet expansion and as non-student by the
writing-space and row-height logic. An omitted `audience` defaults to `"teacher"` outright. See
[[k12-document-set]].

**8. Register once is a rule the renderer cannot enforce.** Forking a `shared` key into two
variants to satisfy one document defeats the whole mechanism, and nothing detects it. The vendor's
rule is that a document-specific change goes in that document's `sections`. The consistency sweep
a `shared` edit obliges is in [[k12-package-consistency]].

## Related

- [[k12-document-set]] is the other top-level key, and the `audience` field this page's faceting
  reads.
- [[k12-block-types]] is the vocabulary a facet's blocks are drawn from, including the
  `instructions` type this mechanism manufactures.
- [[k12-density-rules]] owns the quote-the-standard-verbatim-exactly-once rule that the special
  `standard` key implements.
- [[k12-student-materials]] is where `student: null`, the `group` wrapper and the grade-band
  writing space land on a printed page.
- [[k12-observation-template]] is the document whose four sections are almost entirely
  `from_shared` pulls.
- [[k12-package-consistency]] holds the consistency sweep that a `shared` edit obliges.
- [[trap-empty-facet-reads-as-success]] is the same reading error in the standards MCP: an empty
  result that returns a success status.
- [[source-corestandards-nga-ccsso]] is the rights-holder of the text the `standard` key carries.

## Composes with

- [[practice-format-a-lesson-package]] executes the register-once decision per lesson and runs the
  post-edit consistency sweep this mechanism requires.
- [[practice-ground-a-lesson-end-to-end]] is what fills `standard_code`, `standard_text` and
  `prerequisite_standard` before any of this expands.

## References

Local plugin files, read 2026-08-07 21:15 PDT, version `0.6.0`, no HTTP status. `lesson_common.py`
is byte-identical under `k12-lesson-planning/scripts/` and `k12-lesson-differentiation/scripts/`
at the same line numbers, measured by `diff`:

- `k12-lesson-planning/SKILL.md`, 471 lines. Lines 312 to 329 the registry and the facet rule;
  lines 345 to 350 the `from_shared` pull, the `label` field and the pull-once rule.
- `k12-lesson-planning/scripts/lesson_common.py`, 763 lines. Lines 236 to 238 `_IDENTITY_KEYS`;
  250 to 251 `_as_blocks` on empty; 266 to 274 `_facet_text`; 277 to 309 `_faceted`; 312 to 365
  `expand_from_shared`, covering the `standard` special case, the empty guard, the identity branch
  and the `label` fold; 368 to 383 `expand_blocks`.
- `k12-lesson-planning/references/example_lesson.json`, 667 lines. The 18 `shared` keys in file
  order, and the faceted `exit_ticket` whose `student` facet is a `callout`.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-plugin-contract.md`, primary. §2 the registry, §2.2 the identity keys, §2.3 the
  special key, §2.4 the documented-versus-code contradiction, §2.5 teacher-page rendering, §2.6
  the label fold, §2.7 empty and absent values.
- `sources/k12-grounding-and-render.md`, primary. §3.1 to §3.5 the empty-value and audience
  behaviour in the renderer.
- `sources/k12-block-types.md`, primary. The manufactured `instructions` block and the five
  canonical types the planning fence omits.
