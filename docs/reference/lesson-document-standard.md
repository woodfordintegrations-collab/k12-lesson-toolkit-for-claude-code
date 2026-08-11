# The lesson document standard

**Every lesson plan this project produces ends as two editable Word documents: a Teacher
Edition and a Student Edition.** Markdown, JSON and register files are build inputs. A teacher
receives the documents and nothing else.

The rule behind it, as it was put during the build: *the teacher doesn't want to see process,
just inform the final results and see it then edit.*

## What the two editions are

**Teacher Edition.** Everything needed to teach: goal, materials, phase sequence with timings,
tasks with answers, the misconception to expect and the move for it, exit ticket with its key,
and for assessments the full answer key with a rationale for every distractor. The distractor
rationales are the most useful part of the document, because they tell a teacher what a wrong
answer *means* rather than only that it is wrong.

**Student Edition.** Only what a student receives: tasks, figures, workspace. No answers, no
timings, no teaching notes, no pedagogical commentary.

Both are `.docx`, because a teacher edits them. A PDF is a dead end.

## What never appears in either

Construct-register field names, item ids, commit hashes, check numbers, grep transcripts,
extrapolation ledgers, defect notes, licence verdicts, ruling numbers, slugs, file paths, or
any sentence addressed to a reviewer rather than to a teacher or a student.

The pedagogy stays. The apparatus that produced it does not.

## Producing them

```
python3 src/k12_toolkit/docgen/render_documents.py unit.json --format docx
```

`unit.json` holds one `shared` block plus a `documents` array. Each document carries an
`audience` of `teacher` or `student`, and pulls common content through
`{"type":"from_shared","key":...}` so the same text cannot drift between the two editions.

## Figures

The upstream renderer this is vendored from has **no image block of any kind**. That is
workable for prose subjects and useless for mathematics, so this project adds a `figure` block:

```json
{"type":"figure","src":"<absolute path to .svg>","caption":"Figure 3. ...",
 "alt":"<a description someone could redraw the figure from>","width_in":5.0}
```

Three things about it are deliberate:

1. **`alt` is required and it is not decoration.** It renders into the document as a visible
   description line, so a figure can be read aloud or read by someone who cannot see it.
2. **Alt text must not answer the question.** A description reading "the second rectangle is
   three times the size of the first" hands the answer to any student working from the
   description, which makes the item easier for exactly the student the description exists to
   serve. Describe what is drawn, not what it means.
3. **SVG is rasterized before embedding**, because `python-docx` cannot place an SVG.

## The rasterizer, its backend chain, and the failures it refuses

`src/k12_toolkit/docgen/rasterize.py` tries backends in order and uses the first that actually
renders: **cairosvg**, `rsvg-convert`, `resvg`, `inkscape`, then **QuickLook** on macOS. Only
the last is macOS-only, and it is last because it is the one that needs correcting.

- **QuickLook renders into a square canvas regardless of source aspect.** A 160x55 diagram
  returns as 1200x1200 with the drawing floating in white. The module crops to the ink, and
  every backend passes through that same crop so a Linux build and a macOS build agree.
- **QuickLook returns a generic document icon when it cannot read a file, silently.** That
  would put dozens of identical useless images into a deliverable while every render reported
  success. A flat single-colour image from QuickLook is refused.
- **Any backend can render a blank page**, so ink coverage is checked whatever produced it.

The single-colour check is scoped to QuickLook deliberately. Applied to every backend it
rejected correct output: cairosvg draws a plain rect on exact pixel boundaries with no
antialiasing, giving one ink colour and a perfectly good figure.

**Verified off the macOS path**, not merely coded for it: the shipped worked example was
rebuilt with QuickLook removed from the chain and produced 72 embedded images, 78 alt-text
stamps and 503 outline levels — identical on every count to the QuickLook build.

`pip install '.[docgen]'` pulls cairosvg and Pillow. cairosvg needs a native cairo
(`brew install cairo`, `apt install libcairo2`) and installs cleanly without one, failing only
at render time — which is why the chain probes by rendering rather than by importing. The HTML
output path inlines SVG directly and needs no rasterizer at all.

## Provenance

The renderer is vendored from the `k12-teacher-skills` plugin, Apache-2.0, copyright Anthropic
PBC and Learning Commons, with its per-file headers unmodified. Only the `figure` block and the
rasterizer are this project's own.
