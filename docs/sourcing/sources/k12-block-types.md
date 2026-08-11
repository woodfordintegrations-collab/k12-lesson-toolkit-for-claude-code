---
source_url: k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/ and .../SKILL.md (byte-identical to the installed 0.6.0 plugin)
fetched: 2026-08-08
http_status: n/a
role: primary
covers: k12-block-types, k12-student-materials, k12-observation-template, k12-document-set, practice-format-a-lesson-package
---

# The k12 block vocabulary, and where the aliases live

Read at 2026-08-07 21:15 PDT, which is 2026-08-08 04:15 UTC. Local files, no HTTP status.
Every quotation is byte-exact from the file and line named beside it. All line numbers are
from the fork checkout, which is byte-identical to the installed plugin at
`~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/` (verified by
`diff -r -q --exclude=__pycache__`, exit 0, no output).

The two renderer scripts are shared verbatim between the two skills. Measured by `diff`:
`lesson_common.py`, `render_documents.py`, `render_lesson_docx.py`, `render_lesson_html.py`
and `theme.css` are identical under `k12-lesson-planning/scripts/` and
`k12-lesson-differentiation/scripts/`. Only `render_all.sh` differs, and only in its comments
and its `lesson.json` versus `differentiation.json` filenames.

---

## 1 · THE ANSWER: where `answer_box` and `data_table` are resolved as aliases

**File:** `k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/lesson_common.py`
**Lines:** 477 to 488.

Verbatim, including the comment above it and the function that consumes it:

```python
# Legacy block-type names -> canonical names. Keeps existing lesson JSONs rendering.
ALIASES = {"subheading": "h3", "bullets": "list", "answer_box": "workspace",
           "data_table": "table",
           # frame_bank retired as a component: legacy JSON renders as a plain
           # labeled list — sentence supports are ordinary text the model
           # composes, not a boxed special.
           "frame_bank": "list"}


def btype(blk: dict) -> str:
    t = blk.get("type") or "paragraph"
    return ALIASES.get(t, t)
```

Line by line:

| line | alias | resolves to |
|---|---|---|
| 478 | `subheading` | `h3` |
| 478 | `bullets` | `list` |
| 478 | `answer_box` | `workspace` |
| 479 | `data_table` | `table` |
| 483 | `frame_bank` | `list` |

Five aliases. `btype()` at lines 486 to 488 is the single resolution point: it also defaults
a block with no `type` key, or a falsy `type`, to `"paragraph"`.

The identical file is also at
`k12-teacher-skills/plugin/skills/k12-lesson-differentiation/scripts/lesson_common.py`,
same line numbers, and at
`~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/skills/k12-lesson-planning/scripts/lesson_common.py`,
same line numbers.

### 1.1 Both renderers dispatch through `btype`, so the aliases bind everywhere

`render_lesson_docx.py` line 25, verbatim, is the import: `    Theme, CALLOUT_KINDS, FILL_IN_CHARS, btype as _btype,`

`render_lesson_docx.py` lines 568 to 576, verbatim:

```python
def emit_block(doc, blk: dict, theme: Theme):
    fn = _EMITTERS.get(_btype(blk))
    if fn is not None:
        return fn(doc, blk, theme)
    if blk.get("text"):
        add_md(doc.add_paragraph(), blk["text"])
    elif blk.get("items"):
        for item in blk["items"]:
            add_md(doc.add_paragraph(style="List Bullet"), item)
```

`render_lesson_html.py` line 35, verbatim, is its import:
`    btype as _btype, resolve_callout_kind as _resolve_callout_kind,`

`render_lesson_html.py` lines 89 to 92, verbatim:

```python
def render_block(blk: dict, theme: Theme) -> str:
    # Adding a block type or text field? Render it in render_lesson_docx.py in
    # the same commit — the html and docx renderers must emit the same text.
    t = _btype(blk)
```

A third consumer is the writing-space pairing. `lesson_common.py` lines 389 to 392, verbatim:

```python
def _pair_writing_space(blocks: list[dict]) -> list[dict]:
    """Glue a prompt block to the workspace/answer_box that follows it so a page break can
    never separate a question from its writing space (renderers keep groups together).
    Types are compared post-alias (btype) so canonical and legacy names both pair."""
```

So `answer_box` pairs with a preceding prompt exactly as `workspace` does, and a
`data_table` receives the `table` emitter's blank-cell and row-height handling exactly as a
`table` does.

### 1.2 SKILL.md never says these are aliases

`k12-lesson-planning/SKILL.md` publishes `data_table` and `answer_box` as if they were block
types in their own right. Line 370 and line 374 of the schema fence, verbatim:

```
  {type: table|data_table, headers[]?, rows[[]]}
```

```
  {type: answer_box, height_pt?, ruled?} | {type: page_break}
```

They also appear in the "Which block when" table as block names. Line 399 and line 403,
verbatim:

> | `table` / `data_table` with `headers` | Real tabular data with column labels (misconceptions, scaffolds, the data set students analyze). `display: "large"` renders cells in big centered type — a word grid young students point to and read. |

> | `answer_box` | Writing space after a task. With no `height_pt` it sizes itself to the grade band (K-2 ~200pt, 3-5 ~150pt, 6-8 ~130pt, 9-12 ~115pt). K-5 boxes draw ruled handwriting lines except in math, which defaults to open space; `ruled: true` draws lines at any grade — the surface for answers of composed sentences — and `ruled: false` gives open space for drawing or model-sketching. A task answered in a `fill_table` or on a `number_line` already has its surface. |

And in prose, line 380, verbatim: "Print-safety: never markdown pipe tables (use `table`/`data_table`); for number lines use
the `number_line` block, not a digit string."

**Measured, this project's own measurement.** Searching both `SKILL.md` files and all ten
`references/*.md` files, the word "alias" appears zero times, and `workspace` never appears
in `k12-lesson-planning/SKILL.md` as a block name (only at line 456 inside a quoted teacher
request, "more workspace on the worksheet"). Nothing in the vendor documentation tells an
author that `answer_box` and `data_table` are legacy names.

The consequence for an author: writing `answer_box` produces a `workspace` block, so
`workspace`'s fields apply. `size: small|med|large` is honoured (see §4 below) even though
the `answer_box` schema line publishes only `height_pt?` and `ruled?`.

### 1.3 `subheading`, `bullets` and `frame_bank`

Not published as types in the planning skill's fence. `bullets` IS instructed by the sibling
skill. `k12-lesson-differentiation/SKILL.md` lines 371 to 373, verbatim:

> Never write bullet characters (•, -) inside a `text` string
> — use a `bullets` block; a paragraph collapses line breaks and the bullets run together
> into one line.

`bullets` is not in that skill's own schema fence either (lines 324 to 336, reproduced in §3
below). An author following that instruction writes a `bullets` block which resolves to
`list`.

`k12-lesson-differentiation/references/social_studies.md` is not read in this extract, but
`k12-lesson-planning/references/social_studies.md` line 60, verbatim, also instructs the
legacy name: "formatting hints map to renderer block types: blockquotes → `callout` blocks, bold labels →
`labeled` blocks, lists → `bullets`)."

`frame_bank` is retired as a component per its own inline comment, quoted in §1 above. It
renders as a plain `list`, and no boxed frame-bank styling exists.

---

## 2 · The 20 canonical block types

`render_lesson_docx.py` lines 542 to 565, verbatim, including the maintenance comment:

```python
# Adding a block type or text field? Render it in render_lesson_html.py in the
# same commit — the html and docx renderers must emit the same text.
_EMITTERS = {
    "paragraph": _emit_paragraph,
    "labeled": _emit_labeled,
    "h2": _emit_heading("LC H2"),
    "h3": _emit_heading("LC H3"),
    "instructions": _emit_instructions,
    "list": _emit_list,
    "checklist": lambda d, b, t: _emit_list(d, b, t, checklist=True),
    "callout": _emit_callout,
    "cards": _emit_cards,
    "fill_in": _emit_fill_in,
    "phase_header": _emit_phase_header,
    "group": _emit_group,
    "workspace": _emit_workspace,
    "labeled_box": lambda d, b, t: _emit_workspace(d, b, t, labeled=True),
    "page_break": _emit_page_break,
    "table": _emit_table,
    "columns": _emit_columns,
    "source_card": _emit_source_card,
    "fill_table": _emit_fill_table,
    "number_line": _emit_number_line,
}
```

Twenty keys, counted from the file: `paragraph`, `labeled`, `h2`, `h3`, `instructions`,
`list`, `checklist`, `callout`, `cards`, `fill_in`, `phase_header`, `group`, `workspace`,
`labeled_box`, `page_break`, `table`, `columns`, `source_card`, `fill_table`, `number_line`.

**Measured.** `render_lesson_html.py` implements the same twenty and no others. Its
`render_block` branches, with line numbers from the file:

| line | branch |
|---|---|
| 93 | `if t == "paragraph":` |
| 95 | `if t == "labeled":` |
| 98 | `if t == "h2":` |
| 100 | `if t == "h3":` |
| 102 | `if t == "instructions":` |
| 104 | `if t in ("list", "checklist"):` |
| 111 | `if t == "callout":` |
| 123 | `if t == "cards":` |
| 132 | `if t == "fill_in":` |
| 138 | `if t == "phase_header":` |
| 143 | `if t == "group":` |
| 146 | `if t == "workspace":` |
| 148 | `if t == "labeled_box":` |
| 152 | `if t == "page_break":` |
| 154 | `if t == "table":` |
| 179 | `if t == "columns":` |
| 183 | `if t == "source_card":` |
| 191 | `if t == "fill_table":` |
| 224 | `if t == "number_line":` |

Nineteen branches covering twenty names, because `list` and `checklist` share one.

`from_shared` is NOT an emitter in either renderer. It is expanded before dispatch by
`lesson_common.expand_blocks()` (lines 368 to 383) and `expand_document()` (lines 434 to 461),
so by the time a block reaches `emit_block` no `from_shared` remains.

---

## 3 · What each SKILL.md publishes, set against the code

### 3.1 The planning skill publishes 18 names

`k12-lesson-planning/SKILL.md` lines 364 to 376, the `block types:` portion of the schema
fence, verbatim:

```
block types:
  {type: from_shared, key}
  {type: paragraph, text} | {type: labeled, label, text}
  {type: callout, kind: special|student-task|teacher-note|student-note, label, text}
  {type: h2|h3, text} | {type: list, label?, ordered?, items[]}
  {type: phase_header, name, minutes} | {type: cards, items[{title, text}]}
  {type: table|data_table, headers[]?, rows[[]]}
  {type: fill_table, headers[], blank_rows: int, row_height_pt?}
  {type: number_line, min, max, ticks?, marks[]?}
  {type: source_card, title, author?, date?, origin?, excerpt}
  {type: answer_box, height_pt?, ruled?} | {type: page_break}
  {type: group, blocks[]} | {type: columns, left[], right[]}
```

Eighteen names: `from_shared`, `paragraph`, `labeled`, `callout`, `h2`, `h3`, `list`,
`phase_header`, `cards`, `table`, `data_table`, `fill_table`, `number_line`, `source_card`,
`answer_box`, `page_break`, `group`, `columns`.

Of those eighteen: one (`from_shared`) is a pre-expansion directive, two (`data_table`,
`answer_box`) are aliases, and fifteen are canonical emitters.

### 3.2 Five canonical types the planning fence omits

`instructions`, `checklist`, `fill_in`, `workspace`, `labeled_box`.

They are not absent by accident of scope: the renderer PRODUCES two of them on its own.
`lesson_common._faceted()` line 301, verbatim, manufactures an `instructions` block from a
teacher facet:

```python
            out.append({"type": "instructions", "text": t})
```

So a lesson plan authored entirely from the published fence still contains `instructions`
blocks that the author never wrote, and `_pair_writing_space` wraps prompt-plus-workspace
pairs in `group` blocks the author never wrote either.

`instructions` appears exactly once in the planning `SKILL.md`, in prose, line 227, verbatim
in context (lines 225 to 227):

> A page
> where everything is boxed highlights nothing: a phase reads as plain script with at most
> one or two callouts. Teacher asides (watch-fors, confer prompts) are `labeled` or
> `instructions` blocks.

`checklist`, `fill_in`, `labeled_box` appear zero times in `k12-lesson-planning/SKILL.md`.

### 3.3 The differentiation skill publishes a different, larger set

`k12-lesson-differentiation/SKILL.md` lines 324 to 336, verbatim:

```
     block types:
       {type: from_shared, key, label?}
       {type: labeled, label, text} | {type: paragraph, text}
       {type: callout, kind: special|student-task|teacher-note|student-note, label, text}
       {type: h2, text} | {type: h3, text} | {type: list, label?, ordered?, items[]}
       {type: checklist, label?, items[]} | {type: fill_in, label?, size: short|med|long}
       {type: phase_header, name, minutes}   (science teacher plan; supported by all renderers)
       {type: table, headers[]?, rows[[]], empty_row_height_pt?}
       {type: fill_table, headers[], blank_rows: int, row_height_pt?}
       {type: number_line, min, max, ticks?, marks[]?}
       {type: source_card, title, author?, date?, origin?, excerpt}
       {type: cards, items[{title, text}]} | {type: workspace, size: small|med|large, height_pt?}
       {type: group, blocks[]} | {type: columns, left[], right[]} | {type: page_break}
```

Nineteen names: `from_shared`, `labeled`, `paragraph`, `callout`, `h2`, `h3`, `list`,
`checklist`, `fill_in`, `phase_header`, `table`, `fill_table`, `number_line`, `source_card`,
`cards`, `workspace`, `group`, `columns`, `page_break`.

Comparing the two fences, measured:

- The differentiation fence adds `checklist`, `fill_in`, `workspace` (all canonical).
- The differentiation fence drops `data_table` and `answer_box` (both aliases), so it is the
  more accurate of the two on that point while never explaining why.
- Neither fence names `instructions` or `labeled_box`.
- Only the differentiation fence documents `from_shared`'s `label?` field, though the
  planning `SKILL.md` describes the same field in prose at lines 346 to 348.
- Only the differentiation fence documents `table`'s `empty_row_height_pt?`, though
  `render_lesson_docx._emit_fill_table` forwards it for `fill_table` too (lines 431 to 433).
- Only the differentiation fence documents `workspace`'s `size:` field.

So the union of the two published fences is still two canonical types short, and the two
skills disagree with each other about the vocabulary while sharing one renderer.

---

## 4 · Field behaviour the fences do not state

### 4.1 `workspace` height resolution

`lesson_common.py` lines 610 to 624, verbatim:

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

Exact numbers: `small` is 70.0pt, `med` is 130.0pt, `large` is 220.0pt. `fill_in`'s
underscore counts are `short` 12, `med` 28, `long` 60. Precedence is `height_pt`, then
`size`, then the grade band. An unparseable `height_pt` silently falls back to the band
rather than erroring.

The grade band, `lesson_common.answer_profile()` lines 585 to 591, verbatim:

```python
    if n <= 2:
        return 200.0, 40.0, 160.0, not is_math
    if n <= 5:
        return 150.0, 28.0, 126.0, not is_math
    if n <= 8:
        return 130.0, 24.0, 108.0, False
    return 116.0, 22.0, 96.0, False
```

and the unknown-grade case, line 577 to 578, verbatim:

```python
    n = grade_number(data)
    if n is None:
        return 120.0, 22.0, 96.0, False
```

The tuple is documented in the function's own docstring, lines 571 to 572, verbatim:
`"""Grade-banded writing-space defaults:` / `    (height pt, ruled line gap pt, table-row pt, ruled by default).`

The 9-to-12 height is **116.0**, against SKILL.md line 403's published "9-12 ~115pt". The
unknown-grade fallback of **120.0** is published nowhere.

### 4.2 `table` and `fill_table` row heights

`lesson_common.table_row_height()` lines 713 to 730, verbatim:

```python
def table_row_height(blk: dict, theme: Theme, *, full_blank: bool) -> float:
    """Minimum height (pt) for a table row containing empty writing-space cells.
    An explicit empty_row_height_pt / row_height_pt wins (floored at the 40pt
    writable minimum the deterministic checks enforce) — a sort grid whose cells
    take an X is deliberately shorter than a sentence row, and flooring it to
    the grade band printed near-blank pages of grid. The band sizes rows only
    when the model didn't say."""
    try:
        explicit = float(blk.get("empty_row_height_pt")
                         or blk.get("row_height_pt") or 0)
    except (TypeError, ValueError):
        explicit = 0.0
    band = theme.answer_row
    if theme.student_doc:
        if explicit:
            return max(explicit, 40.0)
        return band if full_blank else 0.45 * band
    return explicit or 36.0
```

Exact numbers: the student-page floor is 40.0pt; a partially-filled row on a student page
gets `0.45 * band`; a teacher page with no explicit height gets a flat 36.0pt regardless of
grade. `theme.student_doc` is set from `data.get("audience") == "student"`
(`render_lesson_docx.render`, quoted in `k12-grounding-and-render.md`), so the SAME table
block renders at different heights on a teacher page and a student page.

`fill_table` additionally accepts `cols` and a `rows` int, neither published. See
`k12-plugin-contract.md` §4.2 for the verbatim `_emit_fill_table`.

### 4.3 `number_line`

`render_lesson_html.py` lines 225 to 234, verbatim:

```python
        lo, hi = blk.get("min", 0), blk.get("max", 10)
        try:
            raw_ticks = None if blk.get("ticks") is None else int(blk.get("ticks"))
        except (TypeError, ValueError):
            raw_ticks = None
        # An explicit 0 means "blank line — students partition it themselves": the
        # bar and its end labels still draw, but with no tick marks at all.
        is_blank = raw_ticks == 0
        ticks = 10 if raw_ticks is None else raw_ticks
        ticks = min(max(1, ticks), 100)
```

Defaults: `min` 0, `max` 10, `ticks` 10 when absent, clamped to the range 1 to 100.
`ticks: 0` is the documented blank-line case. SKILL.md line 401 states the same behaviour,
verbatim: "| `number_line` | A drawn number line (`min`, `max`, `ticks`, optional `marks`). `ticks` omitted defaults to 10 evenly spaced segments; `ticks: 0` draws a bare line with only the `min`/`max` end labels and no tick marks, for students to partition themselves. |"

A mark at either endpoint is silently dropped. Lines 241 to 243, verbatim:

```python
        eps = abs(span) * 0.002
        marks = [(v, lab) for v, lab in marks
                 if abs(v - lo_f) > eps and abs(v - hi_f) > eps]
```

`coerce_marks` (lines 594 to 607) accepts a bare number or a dict keyed `position`, `value`
or `x`; anything else in the `marks` list is dropped without notice.

---

## 5 · Callout kinds, and the silent rewrite of an unknown kind

`lesson_common.py` lines 491 to 508, verbatim:

```python
# Callout kinds: semantic name -> (icon, css class). Legacy `style`/`role` values map in.
CALLOUT_KINDS = {
    "special":      ("⭐", "special"),
    "student-task": ("📌", "task"),
    "teacher-note": ("✋", "tnote"),
    "student-note": ("✋", "snote"),
}
CALLOUT_ALIASES = {
    "accent": "special", "standard": "special",
    "info": "student-task", "activity": "student-task",
    "note": "teacher-note", "tip": "teacher-note",
    "warning": "teacher-note", "caution": "teacher-note", "important": "special",
}


def resolve_callout_kind(blk: dict) -> str:
    raw = str(blk.get("kind") or blk.get("role") or blk.get("style") or "student-task").lower()
    return raw if raw in CALLOUT_KINDS else CALLOUT_ALIASES.get(raw, "student-task")
```

Four canonical kinds. Nine kind aliases. Three field names are accepted (`kind`, `role`,
`style`), in that precedence order, and the raw value is lowercased.

**The fallback is silent and lossy.** Any `kind` string that is neither a canonical kind nor
one of the nine aliases becomes `"student-task"`. A typo such as `kind: "teachernote"` or
`kind: "Teacher Note"` (the space is not stripped) renders as a student task, with the 📌
icon, on a teacher page, with no warning anywhere. `teacher-note` and `student-note` share
the same ✋ icon and differ only in CSS class.

Neither `SKILL.md` documents the `role`/`style` field names, the nine aliases, or the
fallback. The planning skill's "Which block when" table (lines 390 to 392) documents only
three of the four kinds; `student-note` appears in the schema fence's enum at line 367 but
has no row in the table. The differentiation skill's block table (lines 356 to 359)
documents all four, and its `student-note` row reads verbatim:

> | `callout` `kind: student-note` | A reminder students read on their worksheet: a hint card, a key fact. (A sentence support students write from is plain text near its task, not a callout.) |

---

## 6 · The unknown-type fallback prints prose, it does not fail

An unrecognised block type reaching `emit_block` is not an error. `render_lesson_docx.py`
lines 569 to 576, verbatim (already quoted in §1.1): the emitter lookup misses, then
`blk["text"]` is printed as a bare paragraph, or `blk["items"]` as bullets, or nothing.

The HTML renderer does the same and states why. `render_lesson_html.py` lines 255 to 262,
verbatim:

```python
    # NEVER dump raw JSON into the page — a printed worksheet with {"type": ...} on it is a
    # blocking print-safety failure (seen in real model output: "list" and "labeled_box").
    if blk.get("text"):
        return f"<p>{md(blk.get('text'))}</p>"
    if blk.get("items"):
        return "<ul>" + "".join(f"<li>{md(i)}</li>" for i in blk.get("items", [])) + "</ul>"
    # Unknown type with no renderable content: emit nothing. (No debug comment — the type
    # string is model-controlled and could contain "-->" to break out of an HTML comment.)
```

Consequence for a contract author: a misspelled block type produces a document that looks
finished. A `data_tbale` typo prints its `rows` value not at all (no `text`, no `items`), so
the table simply vanishes from the page with no error, no non-zero exit, and no log line.

---

## 7 · Render-time repair passes that rewrite an author's blocks

These run on every document in both formats, after `from_shared` expansion. They mean the
blocks that print are not always the blocks the author wrote.

`lesson_common.expand_document()` lines 442 to 452, verbatim:

```python
    # Print-safety repair pass — post-expansion so it covers model prose AND shared content,
    # in every artifact and both output formats (HTML and docx render through here).
    doc["sections"] = [
        {**s, "blocks": _pair_writing_space(
            [rb for b in s.get("blocks", [])
             for eb in _repair_enum_breaks(b)
             for tb in _repair_pipe_tables(eb)
             for rb in _repair_inline_bullets(tb)])}
        for s in doc["sections"]
    ]
    doc["sections"] = [_strip_heading_echo(s) for s in doc["sections"]]
```

Four rewrites, in order:

1. `_repair_enum_breaks` (lines 66 to 79) inserts a newline before mid-prose `(a)`/`(2)`
   markers, and before `A.`/`B.` capital-letter enumerations but only when both `A` and `B`
   are present (lines 58 to 62, so an initial like "Emmett J. Scott" does not trigger it).
2. `_repair_pipe_tables` (lines 137 to 215) converts a markdown pipe-table run inside a
   `paragraph`, `labeled`, `callout`, `list` or `checklist` into a real `table` block. A
   run of two or more non-separator pipe lines is required (line 204).
3. `_repair_inline_bullets` (lines 82 to 134) splits a prose block containing bullet-marked
   lines into prose plus a `list` block. The bullet markers matched are, from line 43,
   verbatim: `_BULLET_LINE = re.compile(r"^\s*(?:[•▪‣◦]|[-–])\s+")`
4. `_pair_writing_space` (lines 389 to 404) wraps a prompt plus following workspace in a
   `group`.

Then `_strip_heading_echo` (lines 407 to 431) deletes a leading repeat of the section heading
from the first text block.

There is a fifth, conditional pass. `expand_document` lines 453 to 460, verbatim:

```python
    text = _doc_text(doc["sections"])
    if UNKNOWN_SYMBOL in text and not _UNKNOWN_DEFINED.search(text):
        for s in doc["sections"]:
            if UNKNOWN_SYMBOL in _doc_text([s]):
                s.setdefault("blocks", []).append(
                    {"type": "paragraph",
                     "text": "*The symbol ■ stands for the unknown number.*"})
                break
```

`UNKNOWN_SYMBOL` is `"■"` (line 26). If that character appears anywhere in a document and
the regex at lines 27 to 29 finds no defining sentence, the renderer APPENDS a sentence the
author never wrote, verbatim `*The symbol ■ stands for the unknown number.*`, to the first
section that uses it.

Also format-agnostic and applied to every text field before markdown parsing,
`normalize_text` lines 643 to 648, verbatim:

```python
def normalize_text(text) -> str:
    """Format-agnostic text fixups applied before any inline-markdown parse."""
    t = str(text)
    t = re.sub(r"(?<!_)_{3,9}(?!_)", "______", t)
    t = re.sub(r"\s+\|\s+", " · ", t)
    return t
```

A run of 3 to 9 underscores is normalised to exactly 6, and a spaced pipe becomes a middot.
The mini-markdown parser `md_tokens` (lines 654 to 672, driven by the `_MD_TOKEN` regex at
line 651) recognises only `**bold**`, `*italic*` and a bare newline as a line break.
`label_sep` (lines 633 to 640) appends a period after a numeric label and a colon after a
word label.

---

## 8 · Files read for this extract

All read in full unless a range is given, all under
`k12-teacher-skills/plugin/skills/`:

- `k12-lesson-planning/scripts/lesson_common.py` (763 lines, full)
- `k12-lesson-planning/scripts/render_lesson_docx.py` (636 lines; lines 409 to 442 and 530 to 600 read directly, plus grep-located definitions)
- `k12-lesson-planning/scripts/render_lesson_html.py` (331 lines; lines 85 to 262 read directly, plus grep-located branch index)
- `k12-lesson-planning/SKILL.md` (471 lines, full)
- `k12-lesson-differentiation/SKILL.md` (503 lines, full)
- `k12-lesson-planning/references/social_studies.md` (200 lines, full)
- `k12-lesson-differentiation/scripts/` compared to `k12-lesson-planning/scripts/` by `diff`, per-file

Not read, and therefore not a basis for any claim here: `theme.css` (both copies, confirmed
identical by `diff` but never opened), and the bodies of the individual `_emit_*` functions
in `render_lesson_docx.py` other than `_emit_fill_table` and `emit_block`.
