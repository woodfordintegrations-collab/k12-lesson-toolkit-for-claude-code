---
title: "What the k12 contract does not cover"
type: contract
status: derived
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# What the k12 contract does not cover

## Summary

Every other `contract` page in this wiki documents something the `k12-teacher-skills` plugin
publishes. This one documents a hole, then documents what this project put in it. The two halves
have different authority and must never be cited as one thing.

**Half one, measured.** The plugin ships exactly two skills. Both exclude assessment work in
their own frontmatter. Neither produces a quiz, an exam, a rubric, an answer key, or a multi-day
progression, and no `documents[]` id for any of those appears anywhere in either `SKILL.md` or
any of the ten `references/*.md` files.

**Half two, derived by this project.** The HS Geometry unit needs a final exam, a practice exam,
three quizzes, answer keys, and a ten-day progression. This project's design spec expresses all
of them as ordinary `documents[]` entries reusing the existing renderer and the `shared`
registry, rather than as a new schema. **Those artifact shapes are this project's design
decision. The plugin does not specify them, name them, or validate them.** Anyone citing quiz
counts, exam structure, the ten-day arc, or the `answer_key` id as part of the k12 contract is
citing this project back to itself.

One mechanical fact makes half two possible: `render_documents.py` imposes **no id whitelist**.
Any id string renders. The plugin's silence about assessments is a scope decision in its
instructions, not a constraint in its code.

## When to reach for it

Reach for it before authoring any instrument for this unit, so the shape you write is the one
the spec settled and not a fresh invention.

Reach for it whenever you are about to write "the k12 plugin says" about anything with the word
quiz, exam, key, rubric or unit in it. The correct sentence is that the plugin says nothing
about those, and this project decided.

Reach for it when scoping sourcing work for assessment items, because the licensing position on
items is different from the position on lesson prose and has been restated once already in this
project's own record.

Do not reach for it for the three documents the plugin does specify, which are
[[k12-document-set]], [[k12-student-materials]] and [[k12-observation-template]].

## How it works

### Part A: what the plugin does not ship, measured

`k12-lesson-planning/SKILL.md` frontmatter `description`, line 4, the exclusion sentence
verbatim in its surrounding context:

> Use when a K-12 teacher needs a math, ELA, science, or social studies lesson built from scratch — even if grade, subject, or topic isn't yet stated. Do NOT load for grading, a rubric, assessment feedback, a quiz, or a standards lookup — answer those directly.

`k12-lesson-differentiation/SKILL.md` frontmatter `description`, line 3, the corresponding
exclusion verbatim:

> This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-planning's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.

The exclusion is symmetric. It is not a routing hint that some third skill covers assessments;
there is no third skill. Measured: the plugin ships exactly two skills, by directory,
`plugin/skills/k12-lesson-planning/` and `plugin/skills/k12-lesson-differentiation/`.

**The document-id census.** Searching the two `SKILL.md` files and all ten `references/*.md`
files, the only `documents[]` ids named anywhere are:

| id | Where it is named | Skill |
|---|---|---|
| `lesson_plan` | minimum set | planning |
| `observation_template` | minimum set | planning |
| `student_materials` | minimum set, conditional | planning |
| `source_packet` | named as a legitimate fourth | planning |
| `hint_cards` | worked example only | planning |
| `teacher_plan` | fixed four-document set | differentiation |
| `worksheet_group_a` | fixed four-document set | differentiation |
| `worksheet_group_b` | fixed four-document set | differentiation |
| `worksheet_group_c` | fixed four-document set | differentiation |

No exam. No quiz. No answer key. No rubric. No pacing or unit document. The planning skill's
scope is one lesson package; the differentiation skill's is one lesson adapted three ways.

**The one thing that is not closed.** `render_documents.py` imposes no id whitelist. The
document loop takes whatever `id` string it finds, sanitizes it into a filename, and renders.
The differentiation skill constrains its own ids only in prose: its schema fence publishes
`documents[]: {id: teacher_plan|worksheet_group_a|worksheet_group_b|worksheet_group_c, ...}` as
an enum, while the planning fence leaves `id` free. Neither enum is enforced by any code.

### Part B: how this project fills it, spec and not vendor

Everything in this part comes from `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`
and the governing rulings recorded in it. None of it is a vendor statement. It is recorded here so the
derived shapes stay stable across agents, and labelled so they never migrate into a sentence
about what the plugin provides.

The assessment and progression parts of the spec's §6 Repo shape, reproduced:

```
├── progression/
│   ├── unit-overview.md             # the 2-week arc, spiral map, prerequisite entry
│   └── pacing.md                    # day -> standard -> construct family -> assessment
├── lessons/
│   ├── day-01-scaling-and-the-additive-trap/
│   ...
│   └── day-10-angles-of-elevation-and-depression/
│       └── {lesson.json, out/{lesson_plan,student_materials,observation_template}.{docx,html}}
├── assessments/
│   ├── quiz-1-similarity-criteria/
│   ├── quiz-2-ratios-in-right-triangles/
│   ├── quiz-3-special-triangles-and-complements/
│   ├── final-exam/
│   ├── practice-exam/               # parallel form of final, per R6
│   └── keys/                        # audience: teacher
```

The spec's own sentence on keys, verbatim: "Answer keys are `documents[]` entries with
`id: answer_key`, `audience: teacher`, reusing the existing renderer and the `shared` registry
rather than a new schema. Keeps keys from drifting from items on the first revision."

And on separation, verbatim: "Teacher/student separation is enforced twice: by `audience` inside
each document object, which is what the renderer keys on, and by the assembled `dist/` bundles,
which is what a human hands out."

Governing ruling R6, recorded in the spec's §2 table, verbatim: "Practice exam is a **parallel
form** of the final, one authoring pass."

## In practice

### The derived artifact set, with its provenance stamped on every row

| Artifact | Count | Shape | Provenance |
|---|---|---|---|
| Quizzes | 3 | Ordinary `documents[]` entries; one directory each under `assessments/` | derived, spec §6 |
| Final exam | 1 | Ordinary `documents[]` entries under `assessments/final-exam/` | derived, spec §6 |
| Practice exam | 1 | Parallel form of the final, authored in the same pass | derived, ruling R6 |
| Answer keys | per instrument | `id: answer_key`, `audience: teacher`, reusing `shared` | derived, spec §6 |
| Ten-day progression | 10 lesson directories plus `progression/` | Each day a full `lesson.json` package | derived, spec §6 |
| Unit overview and pacing | 2 markdown files | Arc, spiral map, prerequisite entry; day to standard to assessment mapping | derived, spec §6 |

Nothing in that table is inherited. What **is** inherited is the machinery each row runs on: the
`documents[]` array ([[k12-document-set]]), the `shared` registry and its facets
([[k12-shared-registry]]), the block vocabulary ([[k12-block-types]]), the density and
quote-once rules ([[k12-density-rules]]), the consistency invariants
([[k12-package-consistency]]), and the render command ([[k12-render-invocation]]). An assessment
authored this way is structurally a lesson package, which is the point of the decision.

### Consequences of reusing the lesson machinery

- **The quote-once rule now spans a unit, not one lesson.** Each instrument is its own package
  with its own `shared`, so each carries its own target-standard callout. Decide deliberately
  whether "exactly once" is scoped per package or per unit, and record the answer. The plugin's
  rule is written for a single package and does not settle the unit case.
- **Answer keys reuse `shared`, so an item edited there updates its key.** That is the stated
  reason for the decision, and it holds only if items live in `shared` rather than inline.
- **Every consistency invariant applies and still nothing checks it.** More documents means more
  surfaces for the same unchecked rules.
- **Id collisions become a live risk.** The vendor's three ids are distinct by construction;
  the ids invented by this project are not, and two that sanitize alike overwrite each
  other silently.

### The difficulty bar the items inherit

`references/math.md` line 95 sets the exit-ticket bar, verbatim in part: "It IS the
**structurally hardest enumerated case** ... Pick it with the **misconception test**: a student
who holds the lesson's primary anticipated misconception must get the exit ticket WRONG."

That is the vendor's rule about one lesson's exit ticket. This project's design spec files it as
trap 17 and extends it so that no quiz or exam item may read easier than the exit ticket. **The
extension is this project's ruling**, because the plugin has no quizzes or exams to extend it
to. Attribute it accordingly.

### Where the items come from, and the correction that must travel with it

This project's twelve-host adjudication originally concluded, verbatim: "**Net (as written):
there is no host in this table that supplies a clean, adaptable bank of assessment items for
all five standards.** Assessment items should be **authored original from the standard text and
the learning components (row 3)**, with IM/MARS tasks cited as design precedent."

**That sentence is retired**, and the staged record marks it so. The retraction, verbatim in
part: "The wide sweep's finding: (a) JMAP supplies a standard-by-standard, answer-keyed,
provenance-tagged bank across all five standards, cite-only but a complete blueprint including
relative weights; (b) IM/Kendall Hunt supplies openly licensed practice sets, cool-down
statements and activity problems across Units 3 and 4. The wide sweep still puts direct item
reuse at only ~10-15% of the bank, so the "budget for authoring" advice survives in weakened
form. It reframes the saving as being in item *design* rather than item *text*."

So the honest position is: authoring is still the plan for most of the bank, the saving is in
design rather than in text, and the reason a clean adaptable bank looked absent was a licensing
conflation as much as a scarcity. See [[source-jmap]] and [[source-im-kendall-hunt]].

Ruling R9 is what closes the cheaper path: the repo ships CC BY 4.0 and takes no paraphrase from
any ShareAlike source, ever. Quoting does not trigger ShareAlike; adaptation does. The IM task
bank's on-target tasks are CC BY-NC-SA 4.0, so they can be quoted and cited and cannot be
adapted into this repo. See [[license-sharealike]] and
[[trap-sharealike-contaminates-by-paraphrase]].

## Gotchas & constraints

**1. The two halves have different authority and the split is the point.** Part A is a
measurement of vendor files. Part B is this project's design decision. A reader who collapses
them will report that `k12-teacher-skills` specifies a three-quiz, two-exam, ten-day structure.
It does not. Nothing in the plugin knows those numbers exist.

**2. "The plugin does not support assessments" is also wrong, in the other direction.** The
exclusion sits in the skills' trigger descriptions, which govern when a skill loads. The
renderer imposes no id whitelist and renders an exam document exactly as happily as a lesson
plan. The gap is in the instructions, not the code, and "unsupported" overstates it.

**3. The absence is measured by search, and a search has a surface.** The id census comes from
two `SKILL.md` files and ten `references/*.md` files. The staged extract records four
differentiation files **not** read in full: its `references/ela.md`, `science.md`,
`social_studies.md`, and `example_differentiation.json`. A quiz-shaped id hiding in one would
not have been caught. What would close it: a whole-tree grep for `"id":` across the plugin.
Until then this is a strong negative, not a proven one.

**4. `status: derived` is on the frontmatter for a reason.** This is the only content page in
this wiki whose subject is partly the project's own intention rather than an existing artifact.
If the spec changes, this page is wrong and the plugin is unaffected.

**5. Item-level assessment design is out of scope here.** The design spec carries a separate §5
constraint set on construct registers, accommodation categories and per-item tool policy,
including a ruling that one shared formula sheet on the final exam would invalidate every
HSG-SRT.C.7 item. That is a validity question, not an artifact-shape question, and no page in
this wiki's inventory covers it. Do not read this page as having settled it.

**6. Do not cite the twelve-host "Net" line alone.** It is the superseded claim a page is most
likely to pick up by accident, because it is quotable and confident, and it is marked retired in
the staged source. Carry the correction in the same breath or do not carry the claim.

**7. Unverified from here: no instrument has been authored.** At this date the `assessments/`
and `progression/` trees are a spec drawing, not files on disk. Every claim in Part B is about
an intention recorded on 2026-08-07, not about an artifact that exists.

## Related

- [[k12-document-set]] holds the `documents[]` contract every derived instrument is expressed in,
  and the three ids that actually are required.
- [[k12-shared-registry]] is the mechanism that keeps an answer key bound to its item.
- [[k12-block-types]] holds the vocabulary an exam item is built from.
- [[k12-density-rules]] holds the quote-once rule whose unit-level scope this page flags as
  unsettled.
- [[k12-package-consistency]] holds the invariants that grow with the document count.
- [[k12-render-invocation]] holds the id-sanitization and collision behaviour that becomes a live
  risk once ids are invented rather than inherited.
- [[k12-lesson-plan-sections]] holds the enumerate-the-structural-cases rule the exit ticket, and
  therefore every derived item, descends from.
- [[source-jmap]] is the answer-keyed, provenance-tagged item bank the retraction names, and it
  is cite-only.
- [[source-im-kendall-hunt]] is the openly licensed practice-set source the retraction names.
- [[license-sharealike]] and [[trap-sharealike-contaminates-by-paraphrase]] are why the IM task
  bank cannot supply adapted items under ruling R9.
- [[concept-cite-quote-adapt]] makes "cite-only but a complete blueprint" coherent rather than
  contradictory.

## Composes with

- [[practice-format-an-assessment-artifact]] is the procedure that turns the derived shapes on
  this page into rendered documents, and is where the provenance labels have to survive.
- [[practice-format-a-lesson-package]] is its lesson-side twin, and the ten-day progression is
  ten runs of it.

## References

Staged extracts in this wiki, all staged 2026-08-08. The plugin extracts were read from local
files at 2026-08-07 21:15 PDT, so no HTTP status exists for them.

- `sources/k12-plugin-contract.md`, primary. §9 both skills' frontmatter exclusions verbatim, the
  two-skill directory measurement, the document-id census across two `SKILL.md` files and ten
  `references/*.md` files, and the no-id-whitelist statement; §9.1 the differentiation
  four-document set and its id enum; §10 the files not read in full, which bounds gotcha 3;
  §3.1 the `math.md` line 95 exit-ticket bar.
- `sources/k12-grounding-and-render.md`, primary. §4.3(d) the id sanitization and silent
  overwrite on collision; §4.5 the §5e escape hatch.
- `sources/verdict-twelve-host-table.md`, reference. §5 "Assessment items: THIN" with the
  original "Net" sentence and its `[RETIRED, see verdict-wide-sweep.md §6.2]` retraction
  verbatim, and the §5 headline's partial retirement.

This project's own working files, cited as this project's measurement and its own design
decisions, never as any outside party's statement:

- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §6 Repo shape (the `assessments/`,
  `progression/` and `lessons/` trees, the `answer_key` sentence, the double teacher/student
  separation), §2 rulings R6 and R9, and §7 Tier 3 trap 17.
- `Projects/HS Geometry/sources/source-verdict-table.md`, the underlying twelve-host adjudication.

Underlying vendor files, cited as the staged extracts cite them, under
`k12-teacher-skills/plugin/skills/`: `k12-lesson-planning/SKILL.md`, `references/math.md`,
`scripts/render_documents.py`, and `k12-lesson-differentiation/SKILL.md`. Plugin 0.6.0.
