# Similarity to Right-Triangle Trigonometry

A complete two-week grade 9-10 geometry unit built with this toolkit. **CC BY 4.0.**

The two files beside this one are the actual deliverable. Everything else in the source
repository is how they were made.

| File | For | What is in it |
|---|---|---|
| [`Teacher-Edition.docx`](Teacher-Edition.docx) (3.4 MB) | the teacher | ten lessons, three quizzes, the final and practice exams, every answer key with per-distractor rationales, all 73 figures |
| [`Student-Edition.docx`](Student-Edition.docx) (3.2 MB) | the class | the tasks, the figures and the workspace, in teaching order, no answers |

Both are editable Word documents. Open them before reading anything else here.

**Full source, with the build record and the licence evidence:**
[woodfordintegrations-collab/hs-geometry-similarity-trig](https://github.com/woodfordintegrations-collab/hs-geometry-similarity-trig)

## What it took

Measured from commit timestamps, not recalled:

| Phase | Wall clock |
|---|---|
| Standards research, licence sweep, reference-wiki build, unit design | 6h 22m |
| Unit build — 10 lessons, 5 instruments, 73 figures | 2h 59m |
| Document rendering — both editions | 1h 05m |
| **First unit, starting from nothing** | **10h 26m** |

143 files, 285,583 words of markdown, 73 validated SVG figures, two rendered editions.

**A second unit is a projection, not a measurement.** One has been built. It would reuse the
wikis, the figure validator, the renderer, the document standard and the construct-register
schema, and none of the topic analysis, unit design or content. On that basis, roughly
**5 hours**. When a second one exists, the measured number replaces this.

## Three design decisions, and what they mean for teaching it

**Similarity comes first and Pythagoras is its payoff.** Days 1 to 4 build the similarity
criteria; Day 5 derives the Pythagorean Theorem from the altitude-to-hypotenuse configuration.
A survey of current textbooks found none that proves it this way in the lesson introducing the
theorem — so a unit taught in the conventional order satisfies every computational demand of
CCSS-M HSG-SRT.B.4 and silently misses the standard. Every student can use the theorem, none
has proved it, and nothing in the materials says so.
*So:* teaching the days out of order stops Day 5 assessing B.4. It still teaches Pythagoras.

**Tool policy belongs to the item, never to the paper.** There is no blanket "calculators
permitted" anywhere, and the reason is HSG-SRT.C.7: a formula sheet printing
`sin θ = cos(90 − θ)` **is** the thing that standard measures, so one shared sheet on an exam
invalidates every C.7 item on it.
*So:* read the per-item tool line before setting an exam policy. A department-wide "formula
sheets allowed" rule silently voids part of this assessment.

**Every figure can be read aloud.** All 73 carry a written description, 56 to 125 words, so a
student who cannot see the drawing can rebuild it. The descriptions say what is drawn and not
what it means, because a description that gives away the answer makes the item easier for
exactly the student it exists to serve.
*So:* the Student Edition can go to a student using a screen reader unedited, and the unit
prints in greyscale without losing information.

## What is verified, and what is not

| | Status |
|---|---|
| Accessibility of these two files | **Measured.** In the Teacher Edition: 503 heading-outline levels, so Word's Navigation pane and a screen reader see the structure a sighted reader does; 78 of 78 images carrying their description in the field Word reads out; 123 table header rows marked to repeat across pages. Its `.html` twin carries 377 `<th scope=>` headers. Theme colour 5.37:1 on white, above the 4.5:1 WCAG AA floor. Every one of those was zero before the renderer was re-vendored against Anthropic's 2026-08-05 accessibility release — nothing had checked until then. |
| Figures | **Checked both ways.** 73 pass clean, and known-bad fixtures stay in the source repo and must fail. A validator that has only ever printed PASS has told you nothing. |
| Standards alignment | **Authored and reviewed, not externally validated.** No external reviewer or district has signed off. |
| Classroom use | **Never taught.** No student has sat any of these items — no difficulty data, no timing evidence. Carefully designed and unpiloted. |

## Rebuilding or adapting it

Nothing to run to *use* it — the two files above are the deliverable. To change or verify the
unit, clone the source repository, open it in Claude Code, and say *"read REBUILD.md, then
&lt;what you want&gt;"*. That file carries the steps with expected output at each stage, which
files are generated, and the constraints that look like style and are not.
