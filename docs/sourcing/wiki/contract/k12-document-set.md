---
title: The k12 document set
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - sources/k12-block-types.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/example_lesson.json
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/scripts/render_documents.py
updated: 2026-08-08
---

# The k12 document set

## Summary

One `lesson.json` holds exactly two top-level keys, `shared` and `documents`. Every page that
prints is an entry in `documents[]`, and only two of an entry's fields carry mechanical
consequences: `id` becomes the output filename, and `audience` decides which facets render.

The published minimum names three ids. It is a **minimum, not an enum**, and reading it as an
enum is the error this page exists to stop. Two facts settle it. The vendor's own text names
`source_packet` as a legitimate additional page in the same breath as the minimum, and the
worked example the vendor ships carries **four** entries, one of which (`hint_cards`) appears
nowhere in the minimum.

| `id` | `audience` | Status in the published contract |
|---|---|---|
| `lesson_plan` | `teacher` | Named in the minimum |
| `observation_template` | `teacher` | Named in the minimum |
| `student_materials` | `student` | Named in the minimum, and **conditional** on students holding a printed page |
| `source_packet` | not stated in the minimum bullet | Named in the same bullet as a legitimate additional page |
| `hint_cards` | `student` | Not named in the minimum; present in the shipped example |

`render_documents.py` imposes no id whitelist. Any id string renders, which means the contract
is enforced by the author, not by the tool. See [[k12-package-consistency]] for the other
invariants nothing checks.

## When to reach for it

Reach for this page when you are deciding **how many documents a package has** and what each one
is called: authoring a new `lesson.json`, adding a fourth or fifth page, or reconciling a
rendered output directory whose file count does not match the length of `documents[]`.

Reach for it before you hard-code three documents into any generator. A build that emits exactly
`lesson_plan`, `student_materials` and `observation_template` for every lesson is wrong in two
directions at once: it prints a worksheet for an oral lesson that should have none, and it has
no place to put a source packet, an answer key, or a hint set.

Do **not** reach for this page for the differentiation skill. `differentiation.json` ships a
fixed four-artifact set and its `id` field genuinely **is** an enum in its schema fence. The two
skills share one renderer and do not share this contract; see the gotchas.

## How it works

Every quotation below is staged byte-exact in `sources/k12-plugin-contract.md` from the named
file and line range, read at 2026-08-07 21:15 PDT. These are local files, so no HTTP status
exists. The installed plugin at version `0.6.0` and the fork checkout were measured
byte-identical by `diff -r -q --exclude=__pycache__`, exit 0, so either path cites the same bytes.

### The material source

`k12-lesson-planning/SKILL.md` lines 183 to 193, verbatim:

> The artifacts are rendered by bundled scripts from **one material-source `lesson.json`**. The JSON
> holds a `shared` block (content registered once) and a `documents[]` array (each document
> authored as free-form `sections`). A section's `heading` renders as a large title directly
> above its blocks; a block's `label` renders as a bold lead-in on the block itself.

`SKILL.md` line 310, verbatim: "Write ONE `lesson.json` with two top-level keys: `shared` and `documents`."

### The entry shape and the minimum

`SKILL.md` lines 331 to 332, verbatim:

> **`documents[]` is where you compose each page.** Each entry is a full page:
> `{id, audience: teacher|student, eyebrow, title, meta?, theme?, sections[{heading, blocks[]}]}`.
> Include at minimum:

Lines 336 to 343, the three bullets, verbatim:

> - `id: "lesson_plan"` (`audience: "teacher"`) — the subject file's section structure.
> - `id: "observation_template"` (`audience: "teacher"`) — how-to-use, look-fors,
>   misconceptions, a `fill_table` for student notes, and the exit-ticket sort.
> - `id: "student_materials"` (`audience: "student"`) — **only when students hold a printed
>   page.** A K-2 phonics or oral lesson may have none; a source-heavy lesson may have this AND
>   a separate `id: "source_packet"`. The subject file's *Student page layout* gives the
>   default skeleton; adapt it to the lesson.

The phrase "Include at minimum" and the phrase "only when students hold a printed page" are both
inside that block. An author who quotes one without the other builds the wrong document set.

### The shipped example carries four

`references/example_lesson.json`, parsed by the staging agent. Top-level keys are exactly `shared`
and `documents`. `documents[]` has FOUR entries, in this order:

| index | `id` | `audience` | `eyebrow` |
|---|---|---|---|
| 0 | `lesson_plan` | `teacher` | `Grade 6 · Mathematics · Ratios and Rates` |
| 1 | `student_materials` | `student` | `Grade 6 Mathematics · Student Materials` |
| 2 | `hint_cards` | `student` | `Grade 6 Mathematics · Hint Cards` |
| 3 | `observation_template` | `teacher` | `Grade 6 Mathematics · Observation Template` |

`lesson_plan.meta` is the string `Grade 6 · 50 minutes · 6.RP.A.2`. `student_materials.meta` is
the string `Name: ____________________    Date: ____________    Partner: ____________________`.
`hint_cards` and `observation_template` carry no `meta` key at all, so `meta` is optional in
practice as well as in the schema.

### `id` becomes a filename, through a rewrite

`scripts/render_documents.py` lines 78 to 84, verbatim:

```python
    for i, doc in enumerate(docs):
        # Sanitize the document id before it becomes a filename: the id comes from generated
        # JSON, so strip path separators and anything outside [A-Za-z0-9_-].
        doc_id_raw = str(doc.get("id") or f"document_{i + 1}")
        doc_id = re.sub(r"[^A-Za-z0-9_\-]", "_", Path(doc_id_raw).name) or f"document_{i + 1}"
        if args.only and doc_id_raw not in args.only and doc_id not in args.only:
            continue
```

The id you write is not always the filename you get. `student materials` sanitizes to
`student_materials`. `answer key (A)` sanitizes to `answer_key__A_`. A missing or falsy `id`
becomes `document_1`, `document_2` and so on by position.

## In practice

**Decide the set from the lesson, then name the ids.** The three questions in order:

1. Does the teacher work from a plan? Always yes, so `lesson_plan`, `audience: "teacher"`.
2. Do students hold a printed page? If yes, `student_materials`, `audience: "student"`. If no,
   emit none and say so plainly to the teacher. If the anchor text or the sources are reproduced,
   add `source_packet` as its own entry.
3. Does the teacher circulate and record? Yes for every lesson in this contract, so
   `observation_template`, `audience: "teacher"`. Its layout is [[k12-observation-template]].

Anything beyond that is an ordinary entry. The project's ruling that quizzes, exams, answer keys
and the multi-day progression are expressed as further `documents[]` entries reusing `shared`,
rather than as a new schema, is recorded in [[k12-assessment-gap]].

**The two namespaces do not collide.** In the shipped example, `hint_cards` is both a `shared`
registry key and a `documents[]` id. This is legal because ids become filenames while keys are
looked up in `shared`. It is also confusing to read, so name them apart unless you have a reason.

**Prove delivery by enumerating the output directory.** `SKILL.md` lines 406 to 416, verbatim:

> ```bash
> bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
> ```
>
> This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
> `$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
> `source_packet.docx`), plus `.html` and `lesson.json` working files.

One `.docx` per entry is the intent, not a guarantee. The count can come back lower than the
length of `documents[]`, and the reasons are in [[k12-render-invocation]].

## Gotchas & constraints

**1. "Include at minimum" is not a closed set, and the vendor's own example proves it.** Three
ids are the floor. `source_packet` is named legitimate in the same bullet, `hint_cards` ships in
`example_lesson.json` without appearing in the minimum at all, and the staged extract records as
its own measurement that `render_documents.py` imposes no id whitelist: any id string renders.

**2. `student_materials` is conditional, and the subject files disagree about when.** The
existence condition is "**only when students hold a printed page.**" `references/ela.md` lines
206 to 211 give the explicit no-document case ("often has **no `student_materials`
document**"). `references/social_studies.md` lines 174 to 178 give the opposite ("**always
include `id: "student_materials"`**"). Neither is a default you can carry across subjects. Read
the subject file; [[k12-student-materials]] holds both quotations and the skeletons.

**3. Two ids that sanitize to the same string overwrite each other, silently.** The write loop
calls `path.write_text(...)` and `render_docx(full, str(path))` unconditionally with no
collision check. `answer key A` and `answer_key_A` both become `answer_key_A`, and the second
entry silently replaces the first. Nothing exits non-zero.

**4. A missing `audience` defaults to `teacher`, so the worksheet fills with teacher script.**
`render_lesson_docx.py` lines 581 to 586, verbatim:

```python
def render(data: dict, out_path: str) -> int:
    data = expand_document(data, data.get("audience", "teacher"))
    theme = Theme(data.get("theme"))
    (theme.answer_height, theme.answer_gap,
     theme.answer_row, theme.ruled_default) = answer_profile(data)
    theme.student_doc = data.get("audience") == "student"
```

Worse, `theme.student_doc` is a strict equality against the literal string `"student"`, while
`expand_document` tests `audience != "teacher"`. A value of `"Student"` or `"students"` passes
one test and fails the other, so the page renders student facets with teacher writing-space
behaviour. The two checks are not the same test. See [[k12-shared-registry]] for what the facet
side of that split does.

**5. The differentiation skill's `id` field genuinely is an enum, and the two contracts are not
interchangeable.** `k12-lesson-differentiation/SKILL.md` lines 321 to 323, verbatim:

```
documents[]: {id: teacher_plan|worksheet_group_a|worksheet_group_b|worksheet_group_c,
              audience: teacher|student, eyebrow, title, meta,
              sections[]: {heading, blocks[]}}
```

Four fixed ids, `meta` no longer optional. The two skills share `lesson_common.py`,
`render_documents.py`, `render_lesson_docx.py`, `render_lesson_html.py` and `theme.css`
verbatim, which makes it easy to assume they share this contract too. They do not.

**6. The `.html` twin is written before the `.docx` is attempted, so its presence proves
nothing.** Checking that a document exists means checking both extensions for every entry. This
is the vendor's own instruction and the mechanism is in [[k12-render-invocation]].

**7. The vendor forbids reading the renderer, and the published schema is incomplete.** `SKILL.md`
line 352 calls the schema fence "sufficient on its own; do not read any other file for the
schema". The staged extract records that claim as measurably false in three respects; the block
vocabulary is [[k12-block-types]].

## Related

- [[k12-shared-registry]] is the other top-level key, and the mechanism that keeps two documents
  in this set from drifting apart.
- [[k12-block-types]] is what goes inside a `sections[].blocks[]` array, and where the published
  vocabulary is wrong.
- [[k12-lesson-plan-sections]] is the internal structure of the `lesson_plan` entry, which lives
  in the subject reference file rather than in the schema.
- [[k12-student-materials]] holds the existence condition for the conditional third document and
  its per-subject skeletons.
- [[k12-observation-template]] holds the fourth document's four prescribed sections.
- [[k12-render-invocation]] is the single command that turns this array into files, and the four
  ways it hands back something that looks finished.
- [[k12-assessment-gap]] is what this document set does not ship, and how this project fills it
  with further `documents[]` entries rather than a new schema.
- [[k12-package-consistency]] holds the cross-document invariants that no script checks.

## Composes with

- [[practice-format-a-lesson-package]] is the authoring procedure that starts by choosing this
  document set and ends at the rendered output tree.

## References

Local plugin files, read 2026-08-07 21:15 PDT, version `0.6.0`, no HTTP status. Line ranges are
given inline above; the files are:

- `k12-lesson-planning/SKILL.md` (471 lines), `references/example_lesson.json` (667 lines, parsed),
  `references/ela.md`, `references/social_studies.md`.
- `k12-lesson-planning/scripts/render_documents.py` (108 lines),
  `scripts/render_lesson_docx.py` (636 lines).
- `k12-lesson-differentiation/SKILL.md` (503 lines), for the contrasting id enum.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-plugin-contract.md`, primary. §0 provenance and the byte-identical measurement,
  §1 the document set, §9 the measured id census.
- `sources/k12-grounding-and-render.md`, primary. §3.5 the audience default and the split
  equality test, §4 the render invocation.
- `sources/k12-block-types.md`, primary. The shared-renderer measurement between the two skills.
