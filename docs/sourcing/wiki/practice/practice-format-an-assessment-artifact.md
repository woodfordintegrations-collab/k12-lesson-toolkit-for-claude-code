---
title: Format an assessment artifact
type: practice
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - sources/k12-block-types.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md
updated: 2026-08-08
---

# Format an assessment artifact

## Summary

There is no vendor contract for a quiz, an exam or an answer key. The k12 planning skill's own
trigger description excludes them, verbatim: "Do NOT load for grading, a rubric, assessment
feedback, a quiz, or a standards lookup — answer those directly." Measured across the plugin,
neither of its two skills produces a quiz, an exam, a rubric, an answer key, or a multi-day
progression, and no `documents[]` id for any of those is named anywhere in either `SKILL.md` or
the ten `references/*.md` files.

So this page has two halves and they carry different weight. The **mechanism** half is contract:
`render_documents.py` imposes no id whitelist, any id string renders, and a `documents[]` entry
is a full page whatever it contains. The **convention** half is a project ruling from
`specs/2026-08-07-srt-unit-design.md`, and every convention below is labelled with its section.
Nothing here should be repeated to anyone as something the plugin requires.

The mistake this page exists to prevent: **five agents inventing five shapes for the same
instrument set, because the contract is silent.** Three quizzes, a final, a parallel practice
form and their keys, authored in parallel, drift apart on the first revision unless they all
reuse one registry.

The second mistake, and the one with consequences outside the artifact, is
**instrument-level policy.** A tool, read-aloud, or timing statement printed at the top of a
mixed-construct paper invalidates specific items on it, silently, and it reads as generous.

## When to reach for it

Reach for it after the construct register exists. Design §5 makes commit order the proof:
every assessable item carries a row in `alignment/construct-register.md`, "**committed before
the file containing that item exists.**" Formatting an instrument before its constructs are
committed inverts the check that the register exists to perform.

Reach for it for all five instruments at once, because the parallel form is one authoring pass
under ruling R6, not two. Reach for the keys in the same pass: they are entries in the same
file, not a separate deliverable.

Do not reach for it for a lesson. A lesson package has a real contract with prescribed
sections, and it is [[practice-format-a-lesson-package]].

Do not reach for it to decide whether an item is fair, allowable, or accommodated. That is the
construct register's job and it is upstream of formatting. This page decides shape only.

## How it works

### The mechanism half, which is contract

**1. An assessment instrument is an ordinary `documents[]` entry.** The published entry shape,
`SKILL.md` lines 331 to 332, verbatim: "Each entry is a full page: `{id, audience:
teacher|student, eyebrow, title, meta?, theme?, sections[{heading, blocks[]}]}`." An
instrument is that shape with `audience: "student"`; a key is that shape with `audience:
"teacher"`.

**2. Any id renders.** Measured: `render_documents.py` imposes no id whitelist. The id is
sanitized into a filename, with everything outside `[A-Za-z0-9_-]` replaced by `_`, so
`quiz-1-similarity-criteria` survives intact and `answer key (A)` becomes
`answer_key__A_.docx`. Two ids that sanitize to the same string overwrite each other with no
warning.

**3. Item text lives in `shared`, pulled into both the instrument and its key.** This is the
only structural guarantee available: `SKILL.md` lines 345 to 346, verbatim, "the same key on
two pages renders the same content (faceted by audience)." An item registered once as a faceted
value gives the student the prompt and the teacher the prompt plus the answer, from one edit
point. See [[k12-shared-registry]].

**4. The density rules still bind every text field.** They are stated as "hard requirements for
every document", not for lesson documents. A 3-sentence cap on any `paragraph` or `labeled`
block, bullets as fragments, parallel variants in one `table`. See [[k12-density-rules]].

**5. The block vocabulary is unchanged**, including that `answer_box` is an alias for
`workspace` and `data_table` an alias for `table`, and that an unrecognised type prints nothing
and exits 0. See [[k12-block-types]].

**6. Rendering and delivery proof are unchanged.** One command, then list the output directory
and confirm both `.docx` and `.html` exist per document. See [[k12-render-invocation]].

### The convention half, which is this project's ruling

**Answer keys are documents, not a schema.** Design §6, verbatim: "Answer keys are `documents[]`
entries with `id: answer_key`, `audience: teacher`, reusing the existing renderer and the
`shared` registry rather than a new schema. Keeps keys from drifting from items on the first
revision."

**Teacher and student separation is enforced twice.** Design §6, verbatim: "by `audience`
inside each document object, which is what the renderer keys on, and by the assembled `dist/`
bundles, which is what a human hands out."

**The tree the instruments land in**, design §6: `assessments/` holding
`quiz-1-similarity-criteria/`, `quiz-2-ratios-in-right-triangles/`,
`quiz-3-special-triangles-and-complements/`, `final-exam/`, `practice-exam/` and `keys/`.
`practice-exam/` is a parallel form of the final per ruling R6.

**Tool policy belongs to the item.** Design §5 check 4, verbatim: "Any instrument-level
statement ("calculators permitted", "formula sheet provided") is a defect unless every item on
that instrument carries an identical `tools` value."

**No item-selection choice.** Design §5 check 6, verbatim: "Grep for "choose any", "pick 3 of",
"select N of". Hard fail. Item-selection choice varies which construct is sampled and breaks
comparability."

## In practice

The build order that keeps the five instruments and their keys consistent:

1. Group items by construct family before adjudicating any of them. Design §5 calls this "a
   hard requirement of the blueprint, not an optimization", the families being proof,
   conceptual-invariance, procedural-ratio, modeling-applied and fluency.
2. Commit the construct register rows. Only then create the file holding those items.
3. Register every item in `shared`, keyed by item id, as a faceted value.
4. Compose each instrument as a `documents[]` entry pulling its items with `from_shared`.
5. Compose each key as a sibling entry, `audience: "teacher"`, pulling the same keys.
6. Put every tool, timing and presentation statement on the item. Nothing at the top of the
   paper.
7. Render, list the directory, confirm both extensions per document.

### The difficulty floor is inherited, not chosen

Design trap 17 states it in one line: a student holding the lesson's primary misconception must
get the exit ticket wrong, and **no quiz or exam item may read easier than it.** The exit ticket
is set by the lesson's own rules, so the assessment set does not get to pick its own floor.

### The five instruments do not each get their own item bank

The parallel practice exam exists under R6 as one authoring pass with the final. Two instruments
sampling the same constructs from two independently written banks are not parallel forms; they
are two exams. The `shared` registry is what makes a genuine parallel form checkable, because
both pull from one place.

## Gotchas & constraints

**1. One shared formula sheet on the final exam silently invalidates every C.7 item.** Design
§5, verbatim, on HSG-SRT.C.7: "A formula sheet printing `sin θ = cos(90−θ)` **is** the
construct. Hard deny, every item, no exception." The instrument-level generosity and the item
level invalidation are the same act. Design trap 4 records the class: a global tool, read-aloud,
or timing policy on a mixed-construct paper "Invalidates C.7, the C.8 modeling items, and any
fluency quiz. Silent, and it looks generous."

**2. The same artifact can be an accommodation or a modification depending on the verb in the
stem.** Design §5 on C.8, verbatim: "**On a "derive" item a special-triangle ratio table is a
modification. On a "use" item the same table is a presentation accommodation.** Same table,
opposite ruling, decided by the verb in the stem." A formatting pass that standardises
reference material across an instrument therefore cannot be safe by construction.

**3. Half of this page is convention and must be labelled as such.** The plugin does not
prescribe `id: answer_key`, does not prescribe the `assessments/` tree, and does not know what
a construct register is. Presenting any of it as the k12 contract is the attribution error F4
names. See [[k12-assessment-gap]].

**4. Rendering an assessment proves nothing about its validity.** No script checks any
consistency invariant in this toolchain, measured across both skills' `scripts/` directories.
Design trap 8 records the general shape from an earlier build: "Green lint proves structure and
nothing else. 83 UDL pages, 0 errors, while three carried the wrong legal WCAG version and nine
carried false quotations."

**5. An item registered under a misspelled key vanishes from the instrument.**
`expand_from_shared` returns an empty block list for a key that is absent, `None`, `""` or
`[]`, with no exception, no placeholder and no log. On an exam that means a missing question,
not a shorter section. See [[k12-shared-registry]].

**6. A key document that forgets `audience` prints as a teacher page by default and looks
right.** The default is `"teacher"`, so the error runs the other way: an instrument that forgets
`audience` renders every teacher facet, including answers, onto what was meant to be the student
paper.

**7. Item text is subject to the same sourcing rules as lesson text.** An exam item paraphrased
from a ShareAlike task carries the same contamination an adapted lesson passage would, and R9
forecloses it. See [[trap-sharealike-contaminates-by-paraphrase]] and
[[practice-cite-without-redistributing]].

**8. The instrument's provenance is thin by measurement, not by choice.** The staged
adjudication's headline that assessment items are scarce is marked retired in part: the wide
sweep reframes the problem as a licensing conflation rather than a scarcity. Either way, an
assessment set is the place where a wrong host verdict lands first, because a bank of items is
exactly what a repo is tempted to adapt. See [[practice-build-a-source-table]].

## Related

- [[k12-assessment-gap]] is the measured absence this page works around, and holds the record of
  what the plugin does and does not ship.
- [[k12-document-set]] is the `documents[]` contract the instruments borrow.
- [[k12-shared-registry]] is the one structural guarantee available against key-item drift.
- [[k12-density-rules]] binds every text field on an instrument as it does on a lesson page.
- [[k12-block-types]] holds the alias table and the silent unknown-type fallback.
- [[k12-render-invocation]] is the delivery proof step.
- [[practice-format-a-lesson-package]] is the same machinery where a real contract exists.
- [[trap-empty-facet-reads-as-success]] is the same shape in the grounding layer: an empty
  result that reports success and is never an absence.

## Composes with

- [[practice-format-a-lesson-package]] sets the difficulty floor this page inherits, because the
  exit-ticket bar is a lesson artifact and every item here must clear it.
- [[practice-place-and-alt-text-a-figure]] owns every diagram an item depends on, and a geometry
  instrument is mostly diagrams; the renderer draws none of them.
- [[practice-assemble-an-attribution-block]] consumes whatever sources the item bank actually
  used, which for an assessment set is the hardest list to reconstruct after the fact.

## References

Staged extracts in this wiki, all staged 2026-08-08, read against local files at 2026-08-07
21:15 PDT, so no HTTP status exists:

- `sources/k12-plugin-contract.md`, primary. §1.2 the `documents[]` entry shape and the three
  required ids, §2.1 the shared registry and faceting, §6 the density rules stated as hard
  requirements for every document, §7 the measurement that no script checks any invariant, §9
  the exclusion sentence and the measured absence of any assessment document type.
- `sources/k12-grounding-and-render.md`, primary. §3.1 the silent empty-key return, §3.5 the
  `audience` default, §4 the render invocation and the id sanitization.
- `sources/k12-block-types.md`, primary. The alias table and the unknown-type fallback that
  prints nothing.

Plugin files behind those extracts, version 0.6.0:

- `plugin/skills/k12-lesson-planning/SKILL.md`, frontmatter `description` line 4 (the exclusion
  sentence), lines 331 to 332 and 345 to 350 (the entry shape and `from_shared`), lines 212 to
  236 (density), lines 406 to 423 (render and the enumerate-the-directory instruction).

This project's own working file, cited as this project's ruling and not as any outside party's
statement. Every convention in the second half of "How it works" traces here:

- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`. §2 rulings R6 and R9; §5 the
  assessment design constraint, the eight checks, checks 4 and 6, the per-standard rulings for
  C.6, C.7 and C.8, and the construct-family cost lever; §6 the `assessments/` tree, the
  `keys/` directory, the answer-key ruling and the two-place teacher/student separation; §7
  traps 4, 8 and 17.
