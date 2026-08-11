---
title: student_materials layout and writing space
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-block-types.md
  - sources/k12-grounding-and-render.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/math.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/lesson_common.py
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
updated: 2026-08-08
---

# student_materials layout and writing space

## Summary

`student_materials` is the one document in the k12 set whose existence is conditional. The vendor's
condition, verbatim: "**only when students hold a printed page.**" A K-2 phonics or oral lesson may
have none, and the subject files disagree about the default: ELA says such a lesson "often has
**no `student_materials` document**", social studies says "**always include
`id: "student_materials"`**".

When it does exist, its math skeleton is warm-up, practice, exit, each writing task wrapped in a
`group` so a page break can never separate a prompt from its writing surface. The pairing also
happens automatically for five prompt types.

The writing space itself is grade-banded and **the published numbers are not the numbers the code
uses**. `SKILL.md` publishes "9-12 ~115pt". `answer_profile()` returns `116.0`. There is also an
unknown-grade fallback of `120.0` that appears in no documentation at all. If your build asserts a
box height, assert the code's number.

## When to reach for it

Reach for this page when deciding whether a lesson has a student handout at all. That decision is
made before the document set is fixed and it is the first thing this page settles.

Reach for it when laying out the worksheet: which sections, what goes in each, and which scaffolds
may be printed for students versus which stay teacher-only.

Reach for it when a printed box is the wrong size, when a prompt has been separated from its box by
a page break, or when a build needs to state a box height without guessing.

## How it works

Every quotation below is staged byte-exact in `sources/k12-plugin-contract.md` and
`sources/k12-block-types.md` from the named file and line range, read at 2026-08-07 21:15 PDT.
Local files, no HTTP status.

**Evidentiary limit.** The point values below are the return values of `answer_profile()` and
`workspace_height()` as written in the source. **No document was ever rendered**, so the printed
height of any box is unverified from here; what is verified is what the functions return. Closing
it means rendering `example_lesson.json` and measuring the output.

### The existence condition, and two subjects that disagree

`SKILL.md` lines 340 to 343, verbatim, inside the `documents[]` minimum bullet:

> - `id: "student_materials"` (`audience: "student"`) — **only when students hold a printed
>   page.** A K-2 phonics or oral lesson may have none; a source-heavy lesson may have this AND
>   a separate `id: "source_packet"`.

`references/ela.md` lines 206 to 211, verbatim:

> **Which documents to emit.** A K-2 phonemic-awareness or oral-language lesson (RF.*.2,
> RF.*.3 phonics warm-ups, listening-comprehension) often has **no `student_materials`
> document** — students hold response cards or nothing. Say so in the lesson plan's Materials
> line and in your message to the teacher. For 3–12 reading/writing lessons, emit
> `student_materials`; if the anchor text is reproduced, also emit a `source_packet` document
> containing just `from_shared:passage`.

`references/social_studies.md` lines 174 to 178, verbatim:

> **Documents to emit.** Social-studies inquiry lessons always have written analysis
> questions, so **always include `id: "student_materials"`** alongside `lesson_plan` and
> `observation_template`.

### The math skeleton

`references/math.md` lines 128 to 148, verbatim:

> **Student page layout** (the `id: "student_materials"` document) — start from this skeleton
> and adapt:
>
> ```
> sections:
>   "<warm-up heading, kid-facing>"  group[ from_shared:anchor_task, answer_box ]
>   "<practice heading>"     optional callout(student-note) — a brief reminder, only when one helps
>                            from_shared:<visual-scaffold key>   ← only when it is something
>                              students work with (blank fill_table, number_line, the data
>                              set the problems analyze) — a worked reference table is
>                              teacher-only
>                            for each problem k:
>                              group[ {type: from_shared, key: pk, label: "k"},
>                                     answer_box (bare -- it sizes to the grade band;
>                                     ruled: true when the answer is composed sentences) ]
>                            on the ONE problem whose hard part is the writing move, its
>                              group also carries the sentence support -- plain text before
>                              the answer_box (see Sentence supports in SKILL.md)
>                            page_break
>   "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
> ```

The section headings are kid-facing and authored per lesson, not fixed. The realised
`student_materials` in `example_lesson.json` has three headings, byte-exact: `Warm up together`,
`Showdown: find the price for 1`, `Show what you know`.

### The automatic pairing

`lesson_common.py` lines 386 to 404, verbatim:

```python
_PROMPT_TYPES = ("paragraph", "labeled", "callout", "list", "h3")


def _pair_writing_space(blocks: list[dict]) -> list[dict]:
    """Glue a prompt block to the workspace/answer_box that follows it so a page break can
    never separate a question from its writing space (renderers keep groups together).
    Types are compared post-alias (btype) so canonical and legacy names both pair."""
    out: list[dict] = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if (btype(b) in _PROMPT_TYPES and i + 1 < len(blocks)
                and btype(blocks[i + 1]) == "workspace"):
            out.append({"type": "group", "blocks": [b, blocks[i + 1]]})
            i += 2
            continue
        out.append(b)
        i += 1
    return out
```

Five prompt types pair: `paragraph`, `labeled`, `callout`, `list`, `h3`. `h2`, `phase_header`,
`table`, `cards` and `source_card` do not. Because the comparison runs post-alias, an `answer_box`
pairs exactly as a `workspace` does.

### The grade-band writing space, from the code

`lesson_common.py` `answer_profile()` lines 570 to 591, verbatim:

```python
def answer_profile(data: dict) -> tuple:
    """Grade-banded writing-space defaults:
    (height pt, ruled line gap pt, table-row pt, ruled by default).

    Math work space is open by default; a block's explicit `ruled: true`
    still gets the band's gap, so a grade-1 sentence answer gets K-2 pitch."""
    n = grade_number(data)
    if n is None:
        return 120.0, 22.0, 96.0, False
    shared = data.get("shared")
    shared = shared if isinstance(shared, dict) else {}
    # smps (Standards for Mathematical Practice) is the most reliable math signal — it is
    # math-only and the math reference mandates it, whereas shared.subject is often omitted.
    is_math = bool(shared.get("smps")) or "math" in " ".join(str(x or "") for x in (
        shared.get("subject"), data.get("eyebrow"), data.get("title"))).lower()
    if n <= 2:
        return 200.0, 40.0, 160.0, not is_math
    if n <= 5:
        return 150.0, 28.0, 126.0, not is_math
    if n <= 8:
        return 130.0, 24.0, 108.0, False
    return 116.0, 22.0, 96.0, False
```

| grade band | height pt | ruled gap pt | table-row pt | ruled by default |
|---|---|---|---|---|
| K to 2 | 200.0 | 40.0 | 160.0 | `not is_math` |
| 3 to 5 | 150.0 | 28.0 | 126.0 | `not is_math` |
| 6 to 8 | 130.0 | 24.0 | 108.0 | `False` |
| 9 to 12 | 116.0 | 22.0 | 96.0 | `False` |
| grade unknown | 120.0 | 22.0 | 96.0 | `False` |

Explicit sizes override the band. `lesson_common.py` lines 610 to 624, verbatim:

```python
WORKSPACE_SIZES = {"small": 70.0, "med": 130.0, "large": 220.0}
FILL_IN_CHARS = {"short": 12, "med": 28, "long": 60}  # underscore counts for non-CSS formats


def workspace_height(blk: dict, theme: Theme) -> float:
    """Resolve a workspace block's height in points (format-agnostic)."""
    h = blk.get("height_pt")
    if h is None:
        h = WORKSPACE_SIZES.get(str(blk.get("size", "")).lower())
    if h is None:
        h = theme.answer_height
    try:
        return float(h)
    except (TypeError, ValueError):
        return float(theme.answer_height)
```

Precedence: explicit `height_pt`, then the named `size`, then the grade band.

## In practice

**Decide existence first, then layout.** Ask whether students write, mark, or read from paper. If
they do not, emit no `student_materials`, say so in the lesson plan's Materials line, and say so
plainly to the teacher. The vendor supplies the wording for that message in the render step: "This
lesson is oral, so there's no student handout".

**Build each writing task as a `group`.** Write it explicitly rather than relying on the automatic
pass, for two reasons: the automatic pass only fires when the workspace immediately follows one of
the five prompt types, and an explicit group also holds the sentence support, the stimulus and the
box together as one unit.

**Which scaffolds may be printed.** The reference draws the line at whether students work with it:
a blank `fill_table`, a `number_line`, or the data set the problems analyse may go on the student
page. **A worked reference table is teacher-only.** This is a layout rule, not a preference, and it
is the one place where pulling a `shared` key onto the wrong page changes what the lesson teaches.

**Sentence supports go on exactly one task.** `SKILL.md` lines 272 to 279, verbatim:

> **Sentence supports** are plain text where students write: a starter to begin from
> ("One central idea is…") or a fill-in frame with blanks sized for the student's handwriting.
> A support helps the student start, not answer — it never pre-fills what the task asks for.
> Place each one on the specific task whose writing move is hardest — including the
> explain-why beside a math equation — never one bank copied across problems. K-2 students
> and multilingual learners get a support on every task that asks for composed sentences.
> Tasks that take only a number, a single word, or a drawing need none.

**Leave the box bare unless you have a reason.** A bare `workspace` sizes itself to the grade band.
Set `ruled: true` when the answer is composed sentences, `ruled: false` for drawing or model
sketching, and `height_pt` or `size` only when the band is genuinely wrong for the task.

## Gotchas & constraints

**1. The published grade-band numbers do not match the code, and one is unpublished.** `SKILL.md`
line 403 publishes "K-2 ~200pt, 3-5 ~150pt, 6-8 ~130pt, 9-12 ~115pt". The code returns
`116.0` for grades 9 to 12, and returns `120.0` when the grade cannot be parsed at all. The
unknown-grade fallback is published nowhere. Any assertion about box height must come from
`answer_profile`, not from the SKILL.md line.

**2. `is_math` is detected by substring, so an unrelated word turns ruling off.** The signal is
`shared.smps` being truthy, **or** the literal substring `math` appearing in the lowercased join of
`shared.subject`, the document's `eyebrow` and its `title`. An ELA lesson whose eyebrow reads
`Grade 3 · Reading · Mathematical vocabulary` matches, and its K-5 boxes lose their ruled
handwriting lines. The `ruled` default is `not is_math` for K-2 and 3-5 only; grades 6 to 8, 9 to
12 and the unknown-grade fallback all return `False` unconditionally, so the math carve-out applies
only below grade 6.

**3. `size` works on `answer_box` but is not published for it.** `answer_box` resolves to
`workspace` through `ALIASES` before `workspace_height` runs, so `size: small|med|large` is
honoured even though the planning skill's `answer_box` schema line publishes only `height_pt?` and
`ruled?`. Only the differentiation skill documents `size`. See [[k12-block-types]].

**4. An unparseable `height_pt` falls back silently.** `float(h)` inside a `try` returns the band
height on `TypeError` or `ValueError`. A height of `"120pt"` as a string produces a band-sized box
and no error.

**5. The same table block prints at different heights on the plan and the worksheet.**
`table_row_height` floors an explicit height at 40.0pt on a student page, gives a fully blank row
the band height and a partially filled row `0.45 * band`, and gives a teacher page with no explicit
height a flat 36.0pt regardless of grade. `theme.student_doc` is set from
`data.get("audience") == "student"`, so this behaviour hangs on the exact audience string.

**6. An omitted or mis-cased `audience` breaks the worksheet two different ways.** The default is
`"teacher"`, which puts every teacher facet onto the page you intended as a handout.
`"Student"` with a capital S passes the facet expansion's `!= "teacher"` test but fails
`theme.student_doc`'s strict `== "student"`, so student facets print with teacher writing-space
sizing. See [[k12-document-set]] and [[k12-shared-registry]].

**7. A `student` facet of `null` leaves no trace, by design and without warning.** That is the
supported way to keep an oral or teacher-led task off the worksheet. It is also what a typo in a
`shared` key produces. The two are byte-identical in the output.

**8. Science ships no student-page skeleton at all.** `references/science.md` lines 180 to 181 are
the whole of it, verbatim:

> - Student-page section headings in plain inquiry language ("What do you notice?",
> "Investigation") — you compose them directly in the document's sections.

ELA and social studies ship their own skeletons and neither matches math's. Do not port the math
skeleton across subjects.

**9. A figure cannot be placed by this contract.** The renderer cannot draw images, so a diagram is
named in Materials and in the phase script rather than embedded. The procedure for getting one onto
a page is [[practice-place-and-alt-text-a-figure]].

## Related

- [[k12-document-set]] holds this document's conditional place in the set, and the `id` and
  `audience` fields that decide its filename and its facets.
- [[k12-shared-registry]] is where `anchor_task`, `p1`..`pN` and `exit_ticket` are registered, and
  where `student: null` and the facet order are defined.
- [[k12-block-types]] holds `workspace`, `group`, `fill_table`, `number_line` and the alias that
  makes `answer_box` a `workspace`.
- [[k12-lesson-plan-sections]] is the teacher-facing counterpart, and the section that enumerates
  the structural cases these problems must present.
- [[k12-observation-template]] is the third document, and the other consumer of the exit ticket.
- [[k12-density-rules]] governs the length of every block that lands on this page.
- [[k12-package-consistency]] holds the both-directions rule that a task in the plan must be
  printed here and a task printed here must be named in the plan.
- [[practice-place-and-alt-text-a-figure]] covers the diagrams this renderer cannot draw.

## Composes with

- [[practice-format-a-lesson-package]] executes the exists-or-not decision and this skeleton for
  each lesson, and is where the printed page is checked against the plan.

## References

Local plugin files, read 2026-08-07 21:15 PDT, version `0.6.0`, no HTTP status. `lesson_common.py`
is byte-identical under both skills at the same line numbers, measured by `diff`:

- `k12-lesson-planning/references/math.md`, 161 lines, read in full. 128 to 148 the student page
  layout, the visual-scaffold rule and the one-problem sentence support.
- `k12-lesson-planning/scripts/lesson_common.py`, 763 lines, read in full. 386 to 404
  `_PROMPT_TYPES` and `_pair_writing_space`; 570 to 591 `answer_profile`; 610 to 624
  `WORKSPACE_SIZES`, `FILL_IN_CHARS` and `workspace_height`; 713 to 730 `table_row_height`;
  477 to 488 the `answer_box` alias.
- `k12-lesson-planning/SKILL.md`, 471 lines. 340 to 343 the existence condition; 272 to 279
  sentence supports; 403 the published `answer_box` row and its grade-band numbers.
- `references/ela.md` 206 to 224, `references/social_studies.md` 174 to 191, `references/science.md`
  180 to 181. The three other student-page rules.
- `k12-lesson-planning/references/example_lesson.json`, 667 lines. `documents[1]` and its three
  byte-exact section headings.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-plugin-contract.md`, primary. §5 `student_materials`, §5.1 the four skeletons, §5.2
  the group wrapper and the automatic pairing, §5.3 grade-band sizing with the exact numbers, §5.4
  sentence supports.
- `sources/k12-block-types.md`, primary. §4.1 workspace height resolution, §4.2 table and
  fill_table row heights.
- `sources/k12-grounding-and-render.md`, primary. §3.3 `student: null`, §3.5 the audience default
  and the split equality test.
