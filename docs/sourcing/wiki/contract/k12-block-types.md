---
title: Block-type vocabulary and its aliases
type: contract
sources:
  - sources/k12-block-types.md
  - sources/k12-plugin-contract.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/lesson_common.py
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/render_lesson_docx.py
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/render_lesson_html.py
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-differentiation/SKILL.md
updated: 2026-08-08
---

# Block-type vocabulary and its aliases

## Summary

The renderer has **twenty** canonical block emitters. The planning skill's schema fence publishes
**eighteen** names, of which one is a pre-expansion directive and two are legacy aliases, leaving
fifteen canonical types published. Five canonical types are published nowhere in that fence:
`instructions`, `checklist`, `fill_in`, `workspace`, `labeled_box`.

Two of the eighteen published names are aliases and the vendor documentation never says so.
`answer_box` resolves to `workspace` and `data_table` resolves to `table`, in
`lesson_common.ALIASES`, before any renderer sees the block. The word "alias" appears zero times
across both `SKILL.md` files and all ten `references/*.md` files.

The consequence that matters: **an unrecognised type does not fail.** A misspelled `data_tbale`
carries no `text` and no `items`, so it prints nothing at all. The table vanishes from the page
with no error, no non-zero exit and no log line. The same is true one level down: an unrecognised
callout `kind` is silently rewritten to `student-task`, so `kind: "Teacher Note"` prints a student
task with the 📌 icon on a teacher page.

## When to reach for it

Reach for this page before writing any block into a `lesson.json`, and again when a block you
authored did not appear on the rendered page, or appeared as plain prose where a structure was
expected. Those two symptoms have one cause and it is in this page.

Reach for it when you are porting blocks between the two skills. They share one renderer and
publish two different, both incomplete, vocabularies. The union of the two published fences is
still two canonical types short.

Reach for it when you are writing a validator. The type list below is the only complete one, and
it comes from `_EMITTERS`, not from any documentation.

## How it works

Every quotation below is staged byte-exact in `sources/k12-block-types.md` from the named file and
line range, read at 2026-08-07 21:15 PDT. Local files, no HTTP status. The two renderer scripts,
`lesson_common.py`, `render_documents.py`, `render_lesson_docx.py`, `render_lesson_html.py` and
`theme.css`, were measured identical under both skills' `scripts/` directories.

**Evidentiary limit, stated plainly.** Every statement on this page about what prints is read from
the source of the renderer. **The renderer was never executed**, in this staging pass or in this
wiki, so no claim here rests on an observed rendered document. What would close it: render
`example_lesson.json` and inspect the output. Until then, treat the behaviour of the individual
`_emit_*` functions, whose bodies the staging agent did not open apart from `_emit_fill_table` and
`emit_block`, as unverified.

### The twenty canonical types

`render_lesson_docx.py` lines 542 to 565, verbatim, including its maintenance comment:

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

Twenty keys: `paragraph`, `labeled`, `h2`, `h3`, `instructions`, `list`, `checklist`, `callout`,
`cards`, `fill_in`, `phase_header`, `group`, `workspace`, `labeled_box`, `page_break`, `table`,
`columns`, `source_card`, `fill_table`, `number_line`.

The staged extract records as its own measurement that `render_lesson_html.py` implements the same
twenty and no others, in nineteen branches, because `list` and `checklist` share one.

`from_shared` is **not** an emitter in either renderer. It is expanded before dispatch by
`lesson_common.expand_blocks()` and `expand_document()`, so no `from_shared` block ever reaches
`emit_block`. See [[k12-shared-registry]].

### The five aliases

`lesson_common.py` lines 477 to 488, verbatim:

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

| legacy name | resolves to |
|---|---|
| `subheading` | `h3` |
| `bullets` | `list` |
| `answer_box` | `workspace` |
| `data_table` | `table` |
| `frame_bank` | `list` |

`btype()` is the single resolution point. It also defaults a block with no `type` key, or a falsy
`type`, to `"paragraph"`. Both renderers dispatch through it, and so does the writing-space
pairing, whose docstring says so directly: "Types are compared post-alias (btype) so canonical and
legacy names both pair."

### The unknown-type fallback

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

The HTML renderer does the same and states why, lines 255 to 262, verbatim:

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

## In practice

**Write the canonical name, not the legacy one.** `workspace` and `table`, never `answer_box` or
`data_table`, even though the planning fence publishes the latter two. Writing the canonical name
costs nothing and makes the block's real field set legible: `workspace` honours
`size: small|med|large`, which the `answer_box` schema line does not publish at all.

**The callout kinds.** `lesson_common.py` lines 491 to 508, verbatim:

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

Four canonical kinds, nine kind aliases, three accepted field names (`kind`, `role`, `style`, in
that precedence order), value lowercased.

**Blocks you did not write will be on the page.** Five render-time passes run on every document in
both formats, after `from_shared` expansion:

1. `_repair_enum_breaks` inserts a newline before mid-prose `(a)` or `(2)` markers, and before
   `A.`/`B.` enumerations only when both `A` and `B` are present.
2. `_repair_pipe_tables` converts a markdown pipe-table run of two or more non-separator lines
   inside a `paragraph`, `labeled`, `callout`, `list` or `checklist` into a real `table` block.
3. `_repair_inline_bullets` splits a prose block containing bullet-marked lines into prose plus a
   `list` block.
4. `_pair_writing_space` wraps a prompt plus the following workspace in a `group`.
5. `_strip_heading_echo` deletes a leading repeat of the section heading from the first text block.

The bullet markers pass 3 matches, `lesson_common.py` line 43, verbatim:

```python
_BULLET_LINE = re.compile(r"^\s*(?:[•▪‣◦]|[-–])\s+")
```

A sixth, conditional pass appends a sentence the author never wrote. If `■` appears anywhere in a
document and no defining sentence is found, the renderer appends, verbatim,
`*The symbol ■ stands for the unknown number.*` to the first section that uses it.

**Text is normalised before parsing.** A run of 3 to 9 underscores becomes exactly 6, and a spaced
pipe becomes a middot. The mini-markdown parser recognises only `**bold**`, `*italic*` and a bare
newline as a line break.

## Gotchas & constraints

**1. A misspelled type prints nothing and reports success.** `data_tbale` misses the emitter
lookup, carries no `text` and no `items`, and therefore emits nothing. The table simply is not on
the page. The staged extract records the consequence in these terms: no error, no non-zero exit,
and no log line. This is the single most consequential fact on this page: **the renderer's failure
mode for a typo is silence, not an error.**

**2. A misspelled callout `kind` is not silence, it is a wrong-looking box.** Any `kind` that is
neither a canonical kind nor one of the nine aliases becomes `"student-task"`. `kind: "teachernote"`
and `kind: "Teacher Note"` both do this, because the space is not stripped. The result is a
student task with the 📌 icon printed on a teacher page. `teacher-note` and `student-note` share
the same ✋ icon and differ only in CSS class, so a wrong choice between those two is nearly
invisible on the page as well.

**3. The vendor tells you not to read the scripts, and the schema fence is incomplete.** `SKILL.md`
lines 195 to 200 say "**Do not open, cat, head, or grep the renderer scripts**", and line 352 says
the schema is "sufficient on its own; do not read any other file for the schema". The staged
extract records this as measurably false: five canonical types are missing from that fence, two
published names are aliases, and `fill_table` accepts `rows` and `cols` the fence does not list.
Following the instruction produces authors who cannot name `workspace`.

**4. The two skills publish different vocabularies over one renderer.** The differentiation fence
adds `checklist`, `fill_in` and `workspace`, all canonical, and drops `data_table` and
`answer_box`, both aliases, which makes it the more accurate of the two while never explaining why.
Neither fence names `instructions` or `labeled_box`. Only the differentiation fence documents
`from_shared`'s `label?` field, `table`'s `empty_row_height_pt?` and `workspace`'s `size:` field.
Do not carry a field's presence in one fence as evidence of its absence in the other renderer:
there is only one renderer.

**5. `bullets` is actively instructed by the vendor even though it is legacy.**
`k12-lesson-differentiation/SKILL.md` lines 371 to 373, verbatim:

> Never write bullet characters (•, -) inside a `text` string
> — use a `bullets` block; a paragraph collapses line breaks and the bullets run together
> into one line.

`k12-lesson-planning/references/social_studies.md` line 60 also instructs it. Both produce a
`list`. The instruction is not wrong, only misnamed.

**6. `frame_bank` is retired as a component, not merely aliased.** Its own inline comment says so.
It renders as a plain `list`, and no boxed frame-bank styling exists anywhere. Sentence supports
are ordinary text; see [[k12-student-materials]].

**7. A block's rendered height depends on the page it is on.** `table_row_height` returns a flat
36.0pt on a teacher page with no explicit height, and on a student page returns the grade band for
a fully blank row, `0.45 * band` for a partially filled one, with an explicit height floored at
40.0pt. The same block therefore prints differently in the plan and on the worksheet.

**8. Two block types silently drop content.** A `number_line` mark at either endpoint is removed
by an epsilon test, and `coerce_marks` drops any entry that is neither a bare number nor a dict
keyed `position`, `value` or `x`, without notice. `fill_table` truncates a `rows` list at 50 and
clamps `cols` at 12.

## Related

- [[k12-shared-registry]] is where `from_shared` is expanded away before dispatch, and where the
  `instructions` block this fence omits is manufactured.
- [[k12-document-set]] is the array these blocks are composed into, and the `audience` field that
  changes how several of them render.
- [[k12-student-materials]] covers `workspace` sizing, the `group` wrapper and the automatic
  prompt-to-writing-space pairing.
- [[k12-observation-template]] covers `fill_table` and `cards` as that document actually uses them.
- [[k12-density-rules]] governs how many callouts a phase may carry and how long a `paragraph` or
  `labeled` block may run.
- [[k12-render-invocation]] is where a silent block failure becomes a silent package failure.
- [[k12-package-consistency]] is the set of invariants that would catch a vanished table, and that
  no script performs.

## Composes with

- [[practice-format-a-lesson-package]] is the authoring procedure that has to choose from this
  vocabulary and verify the result, since the renderer will not.

## References

Local plugin files, read 2026-08-07 21:15 PDT, version `0.6.0`, no HTTP status. Line numbers are
from the fork checkout, measured byte-identical to the installed plugin by
`diff -r -q --exclude=__pycache__`, exit 0:

- `k12-lesson-planning/scripts/lesson_common.py`, 763 lines, read in full. 477 to 488 `ALIASES`
  and `btype`; 491 to 508 the callout kinds; 389 to 404 `_pair_writing_space`; 442 to 460 the
  repair passes; 643 to 648 `normalize_text`; 713 to 730 `table_row_height`.
- `k12-lesson-planning/scripts/render_lesson_docx.py`, 636 lines. 542 to 565 `_EMITTERS`;
  568 to 576 `emit_block`; 409 to 434 `_emit_fill_table`.
- `k12-lesson-planning/scripts/render_lesson_html.py`, 331 lines. 89 to 92 the dispatch; the
  nineteen-branch index; 225 to 243 `number_line`; 255 to 262 the fallback.
- `k12-lesson-planning/SKILL.md`, 471 lines, and `k12-lesson-differentiation/SKILL.md`, 503 lines.
  The two schema fences, the two block tables, and the do-not-read-the-scripts rule.

Not read by the staging agent, and therefore not a basis for any claim here: `theme.css`, and the
bodies of the individual `_emit_*` functions other than `_emit_fill_table` and `emit_block`.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-block-types.md`, primary. §1 the aliases, §2 the twenty emitters, §3 the two
  fences set against the code, §4 field behaviour, §5 callout kinds, §6 the unknown-type fallback,
  §7 the render-time repair passes.
- `sources/k12-plugin-contract.md`, primary. §4.2 `fill_table`'s undocumented fields, §8.6 the
  do-not-read-the-scripts rule and the three respects in which it is measurably false.
