---
title: Format a lesson package to the k12 contract
type: practice
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-block-types.md
  - sources/k12-grounding-and-render.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/math.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/lesson_common.py
  - Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md
updated: 2026-08-08
---

# Format a lesson package to the k12 contract

## Summary

One grounded lesson becomes a rendered document set through exactly one file. `SKILL.md` line
310, verbatim: "Write ONE `lesson.json` with two top-level keys: `shared` and `documents`."
Every page the lesson needs is an entry in `documents[]`, and anything appearing on more than
one page is registered once in `shared` and pulled in with `{"type": "from_shared", "key": …}`.

The mistake this page exists to prevent: **writing a separate file per document, or repeating
content across documents, so the pages drift the first time anything is revised.** The
`shared` registry is not a convenience. It is the entire mechanism that keeps a plan's
"Students see" line and the worksheet's prompt identical after an edit, and an author who
copies text between documents has disabled it.

A second failure sits underneath the first, and it is quieter. **No script in the toolchain
checks any of the contract's consistency rules.** Measured across both skills' `scripts/`
directories: there is no arithmetic on phase minutes, no cross-document scan, and no coverage
test anywhere in the render path. A package that violates every invariant on this page renders
cleanly, exits 0, and looks finished.

Ten parallel lesson agents are expected to produce packages that pass without a human merging
them, which is only possible if each agent applies the same rules to its own file.

## When to reach for it

Reach for it after the lesson is grounded and before any JSON is written. The subject reference
file load is mandatory and precedes this step: `SKILL.md` lines 61 to 62, verbatim, "**Loading
the matching reference file is mandatory.** Drafting a lesson without first reading the subject
reference is a critical failure." For math that file is `references/math.md`, and it, not
`SKILL.md`, carries the lesson plan's five sections. See [[k12-lesson-plan-sections]].

Reach for it per lesson, one file per agent. Trap 12 of this project's design is unconditional:
parallel agents must never share a file, and ownership is partitioned before dispatch, not
negotiated during.

Do not reach for it for a quiz, an exam or an answer key. The plugin's own trigger description
excludes them, and the shape those take is a project convention rather than a contract: see
[[practice-format-an-assessment-artifact]] and [[k12-assessment-gap]].

Do not reach for it to decide a figure's placement. The renderer cannot draw images at all,
which changes what a "package" can contain: see [[practice-place-and-alt-text-a-figure]].

## How it works

**1. One file, two top-level keys.** `shared` is a content registry; `documents[]` is an array
of full pages. `SKILL.md` lines 331 to 332, verbatim: "**`documents[]` is where you compose each
page.** Each entry is a full page: `{id, audience: teacher|student, eyebrow, title, meta?,
theme?, sections[{heading, blocks[]}]}`."

**2. Three document ids at minimum, and one of the three is conditional.** `lesson_plan`
(`audience: "teacher"`), `observation_template` (`audience: "teacher"`), and
`student_materials` (`audience: "student"`) which exists per `SKILL.md` "**only when students
hold a printed page.**" A fourth page is legitimate: `source_packet` is named in `SKILL.md`
itself, and the shipped worked example ships four documents, including a `hint_cards` page
named nowhere in the minimum set. See [[k12-document-set]].

**3. Register once, pull everywhere.** `SKILL.md` lines 345 to 350, verbatim: "Inside any
document, pull registered content with `{"type": "from_shared", "key": "…"}`. The same key on
two pages renders the same content (faceted by audience)." A key's value may be a string, a
block, a list of blocks, or a faceted object `{teacher, student, stimulus}`. Eight key names
are reserved identity metadata and render as a bare paragraph if pulled. See
[[k12-shared-registry]].

**4. Author blocks from the real vocabulary, not the published fence.** The renderer registers
20 emitters. `SKILL.md`'s schema fence publishes 18 names, of which one is a pre-expansion
directive and two are aliases. Five canonical types the fence omits are `instructions`,
`checklist`, `fill_in`, `workspace`, `labeled_box`. The five aliases, verbatim from
`lesson_common.py` lines 477 to 483:

```python
ALIASES = {"subheading": "h3", "bullets": "list", "answer_box": "workspace",
           "data_table": "table",
           # frame_bank retired as a component: legacy JSON renders as a plain
           # labeled list — sentence supports are ordinary text the model
           # composes, not a boxed special.
           "frame_bank": "list"}
```

See [[k12-block-types]].

**5. Meet the density rules in every text field.** A `paragraph` or `labeled` block is at most
3 sentences. Bullets are fragments, one idea each. Parallel variants go in ONE `table` block.
Headings use sentence case. The standard is quoted verbatim exactly once in the whole package,
by code plus a ten-word gist everywhere after. See [[k12-density-rules]].

**6. Render with one command, then prove delivery by looking.** `SKILL.md` §5b, verbatim:

> ```bash
> bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
> ```

and, verbatim, "Then list `$OUTPUT_DIR` and confirm every document has both its `.docx` and
`.html`; if either is missing or tiny, rerun the script." That instruction is the vendor's own,
and it is there because the failure signature is a directory full of real files. See
[[k12-render-invocation]].

**7. Run the consistency sweep before rendering, and again after any edit.** `SKILL.md` §5d,
verbatim: "**Consistency sweep after any context/number/task change:** after editing `shared`,
re-read every prose block in every `documents[]` entry and update every sentence that still
mentions the old context, names, or numbers." Its own closing clause names the cost of skipping
it: "stale prose is the most common consistency failure."

## In practice

Three orderings are not free choices, because each one constrains what comes after it.

**Enumerate the structural cases before writing any problem.** `references/math.md`, verbatim,
requires the set to be written "so EVERY enumerated case is a numbered, required problem (or the
exit ticket), with its case named in that problem's `teacher` facet." A case named only in prose
does not count: "A structural case that appears only in prose — the SWBAT, an anticipated
challenge, a teacher move, or the Discuss notes — does NOT count as covered." Writing problems
first and enumerating afterwards produces a set that reads complete and is not.

**Register in `shared` before composing any document.** Every problem, the anchor task,
vocabulary, misconceptions, look-fors, the exit ticket, the exit sort and the visual scaffold go
in first. A document composed against inline text is a document that has to be rewritten to be
made consistent, not edited.

**Set `audience` on every entry as it is created**, not in a pass at the end. The default is
`"teacher"` and the failure is invisible, per gotcha 3.

### The bidirectional alignment check, run by hand

Trap 16 of this project's design states it in one line: every plan task needs a printed student
block, and every printed student task must be named in the plan. The sibling differentiation
skill spells out the same check as its O6 and calls both directions explicitly, including that
"a plan line naming a task or organizer no tier document prints" fails. Nothing enforces it.
See [[k12-package-consistency]].

### The exit ticket is a bar, not a slot

`references/math.md`, verbatim, requires the exit ticket to be "the **structurally hardest
enumerated case**", picked with the misconception test: "a student who holds the lesson's
primary anticipated misconception must get the exit ticket WRONG." That bar is inherited
upward, per trap 17: no quiz or exam item may read easier than it.

## Gotchas & constraints

**1. An unknown block type prints nothing and exits 0.** The emitter lookup misses, then
`blk["text"]` prints as a bare paragraph, or `blk["items"]` as bullets, or nothing at all. The
HTML renderer states the reason in its own comment, verbatim: "NEVER dump raw JSON into the
page. A printed worksheet with {"type": ...} on it is a blocking print-safety failure (seen in
real model output: "list" and "labeled_box")." Consequence: a `data_tbale` typo carries no
`text` and no `items`, so the table vanishes with no error, no non-zero exit and no log line.

**2. A missing `shared` key is indistinguishable from a deliberate omission.**
`expand_from_shared` lines 331 to 333, verbatim:

```python
    val = shared.get(key)
    if val is None or val == "" or val == []:
        return []
```

No exception, no placeholder, no log. The section renders one block shorter, and a misspelled
key is indistinguishable from a deliberate omission. See [[k12-shared-registry]].

**3. A forgotten `audience` renders teacher script onto the worksheet.**
`render_lesson_docx.render` line 582, verbatim: `data = expand_document(data,
data.get("audience", "teacher"))`. The default is `"teacher"`. Worse, `theme.student_doc` is a
strict equality against the literal `"student"`, while `expand_document` tests `audience !=
"teacher"`, so `"Student"` or `"students"` splits the two checks and produces a page that is
non-teacher for faceting and non-student for sizing.

**4. An unrecognised callout `kind` is silently rewritten to `student-task`.** Four canonical
kinds, nine aliases, and anything else falls through, so `kind: "Teacher Note"` renders as a
student task on a teacher page with no warning.

**5. The renderer rewrites your blocks before printing them.** Four repair passes run on every
document in both formats, then a heading-echo strip. A fifth conditional pass **appends a
sentence the author never wrote**, verbatim `*The symbol ■ stands for the unknown number.*`, if
`■` appears anywhere undefined. The blocks that print are not always the blocks written.

**6. `SKILL.md` tells you its schema is sufficient and instructs you not to read the scripts.**
Line 352, verbatim: "**Schema** — sufficient on its own; do not read any other file for the
schema:". This project measured that claim false in three respects: the fence omits five
canonical types, two names it publishes are aliases, and its facet-order sentence contradicts
the code. The instruction is the vendor's; the measurement is this project's.

**7. Documented order and code order disagree on the student page.** `SKILL.md` says the
student facet renders "(after any `stimulus` blocks)". `_faceted()` uses `out[:0] = ...`, a
prepend, so the code renders student facet then stimulus, matching its own docstring. Both are
quoted exactly in the staged extract. The code governs what prints.

**8. Render can hand back a populated directory that is not the deliverable.** `render_all.sh`
pip-installs `python-docx==1.1.2` at render time with `|| true` swallowing every failure, then
on failure renders HTML only, prints to stderr and exits 1. The `.html` twin is always written
before the `.docx` is attempted, so `X.html` proves nothing about `X.docx`. Under `set -euo
pipefail` a crash on document 3 of 4 leaves documents 1 and 2 on disk looking correct.

**9. The `id` becomes the filename after sanitization.** Anything outside `[A-Za-z0-9_-]`
becomes `_`; a missing id becomes `document_1` by position; two ids that sanitize to the same
string overwrite each other with no warning. The delivered filename is not always the id
written, and the file count can be lower than the `documents[]` count.

**10. Writing-space sizes are grade-banded, and the published numbers are not exact.**
`answer_profile()` returns `116.0` for grades 9 to 12 against the "9-12 ~115pt" `SKILL.md`
publishes, and `120.0` when the grade cannot be read at all. See [[k12-student-materials]].

## Related

- [[k12-document-set]] is the `lesson.json` contract this procedure fills in.
- [[k12-shared-registry]] is the faceting mechanism step 3 depends on.
- [[k12-block-types]] is the alias table and the five omitted canonical types.
- [[k12-lesson-plan-sections]] holds the five math sections and the rules deciding their content.
- [[k12-student-materials]] holds the skeleton, the `group` wrapper and the grade-band sizing.
- [[k12-observation-template]] holds the four prescribed sections of the third required document.
- [[k12-density-rules]] and [[k12-package-consistency]] are the two rule sets no script checks.
- [[k12-render-invocation]] is the single command and its four failure signatures.
- [[trap-empty-facet-reads-as-success]] is the same failure shape one layer up, in the grounding
  call rather than the renderer, and it is why an empty result is never read as an absence.
- [[practice-format-an-assessment-artifact]] is the same machinery used where no contract exists.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] produces the grounded standard text, prerequisite and
  learning components this procedure registers in `shared`. Formatting a package whose
  grounding step returned empty produces a complete-looking document with no target-standard
  callout at all.
- [[practice-place-and-alt-text-a-figure]] owns everything the renderer cannot draw, which is
  every image in the package.
- [[practice-cite-without-redistributing]] governs what may appear in the text fields this
  procedure formats, and the copyright guardrail it enforces binds chat messages as well as
  documents.

## References

Staged extracts in this wiki, all staged 2026-08-08, read at 2026-08-07 21:15 PDT against local
files, so no HTTP status exists:

- `sources/k12-plugin-contract.md`, primary. §1 the document set and the schema fence, §2 the
  shared registry and the facet-order contradiction, §3.1 the math sections, §6 density rules,
  §7 the package-consistency invariants and the measurement that no script checks them, §8.6
  the do-not-read-the-scripts rule.
- `sources/k12-block-types.md`, primary. §1 the verbatim `ALIASES` dict, §2 the 20 emitters,
  §3.2 the five omitted canonical types, §5 the silent callout-kind rewrite, §6 the unknown-type
  fallback, §7 the five render-time repair passes.
- `sources/k12-grounding-and-render.md`, primary. §3 empty-facet behaviour and the `audience`
  default, §4 the render invocation and the four ways it hands back something unfinished.

The plugin files behind those extracts, at plugin version 0.6.0, measured byte-identical
between the fork checkout and the installed copy by `diff -r -q --exclude=__pycache__`, exit 0:

- `plugin/skills/k12-lesson-planning/SKILL.md`, lines 61 to 67, 212 to 263, 310 to 376, 406 to
  423 and 444 to 461.
- `plugin/skills/k12-lesson-planning/references/math.md`, the section structure, the problem-set
  coverage rules and the exit-ticket bar.
- `plugin/skills/k12-lesson-planning/scripts/lesson_common.py`, lines 236 to 238, 277 to 335,
  386 to 404, 434 to 461, 477 to 488 and 570 to 591.
- `plugin/skills/k12-lesson-planning/references/example_lesson.json`, the four-document worked
  set. Confirmed present and parsed structurally in the staged extract; not opened by this page.

This project's own working file, cited as this project's measurement:

- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §4 phase 6b (ten packages, one
  file per agent), §7 traps 12, 14, 15, 16, 17, 18, 19, 20.
