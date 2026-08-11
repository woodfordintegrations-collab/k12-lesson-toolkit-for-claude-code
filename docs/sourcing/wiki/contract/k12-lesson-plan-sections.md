---
title: lesson_plan section structure (math)
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/math.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/example_lesson.json
updated: 2026-08-08
---

# lesson_plan section structure (math)

## Summary

**The `lesson_plan` document's sections are not in `SKILL.md`.** They are in the subject reference
file, and loading that file is stated as mandatory: "Drafting a lesson without first reading the
subject reference is a critical failure."

For math, there are five sections. Their headings, byte-exact and in order:

| # | heading |
|---|---|
| 1 | `At a glance` |
| 2 | `Learning goal` |
| 3 | `Vocabulary & anticipated challenges` |
| 4 | `Lesson sequence` |
| 5 | `Design notes` |

Section 3 uses an ampersand, not the word "and". The five realised headings in
`example_lesson.json` `documents[0]` match this list byte for byte.

**Five is a math and ELA fact, not a plugin fact.** Science ships seven sections with different
names and no `Learning goal` at all. Social studies ships seven and is the only subject where the
exit ticket is a top-level section rather than the last phase inside `Lesson sequence`. An author
who learns "the five sections" and applies them to a science lesson has written the wrong document.

## When to reach for it

Reach for this page when you are composing the `sections[]` array of the `lesson_plan` entry, or
when a reviewer asks where a piece of content belongs. Rationale, for example, has exactly one
home: `Design notes`, last, after the exit ticket.

Reach for it before writing the practice set, because the enumeration rule that governs the
problems is stated here rather than in the student-page layout, and because the exit ticket is
selected from that same enumeration.

Do not reach for it for a subject other than math without reading the divergence table in the
gotchas first, and then the actual subject file.

## How it works

Every quotation below is staged byte-exact in `sources/k12-plugin-contract.md` from the named file
and line range, read at 2026-08-07 21:15 PDT. Local files, no HTTP status.

### The mandatory load, and the routing map

`SKILL.md` lines 61 to 67, verbatim:

> **Loading the matching reference file is mandatory.** Drafting a lesson without first
> reading the subject reference is a critical failure. The reference file carries the
> complete subject-specific instructions: clarify priorities, curriculum branching,
> grade-band structures, section structure, non-negotiables, and the lesson.json mapping.
> Treat the loaded reference as your full skill instructions for this turn.

`SKILL.md` lines 56 to 59, verbatim, is the whole routing map:

> - math → `references/math.md`
> - ELA → `references/ela.md`
> - science → `references/science.md`
> - social studies → `references/social_studies.md`

### The five math sections

`references/math.md` lines 80 to 89, verbatim:

> ### Section structure — both paths
>
> 1. **At a glance** — standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist); a one-line lesson arc naming the phases with minutes ("Launch 8 → Explore 15 → Discuss 12 → Synthesize 5 → Exit 5") so the period's shape is visible before any detail; materials — name each item plainly (e.g. "Number cards 0-20"); SMPs named
> 2. **Learning goal** — Big Idea (enduring understanding, 1 sentence); SWBAT; Prerequisite (prior standard by code + one plain sentence on what students can already do and how today builds on it)
> 3. **Vocabulary & anticipated challenges** — 3–5 key terms with brief definitions; 2–3 misconceptions each as: *What students do* / *Why it happens* / *Teacher move*
> 4. **Lesson sequence** — phases per curriculum branch above; **Discuss gets at least 10 minutes** (in a short warm-up-style request, shrink the other phases, not Discuss); in Explore: 3+ look-fors each naming the student response, why it matters, and what to do with it — and if the anchor task admits more than one correct response or equation, one look-for must say so explicitly so the teacher accepts all of them; in Discuss: at least one named student-to-student talk move (Think-Pair-Share, Turn-and-Talk, partner compare, agree/disagree) + specific discourse prompts (not generic)
> 5. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when
>    adapting, with brief reasoning, including the lesson's central representation (the visual
>    or model students work with) and its one-sentence why. Rationale lives here, after the
>    teaching path — a teacher prepping reads the arc first, the reasoning second.

### The phases inside `Lesson sequence`

Both math curriculum branches use the same five phases. `math.md` line 43 and line 49, verbatim:
"Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** exactly." (the IM-confirmed branch)
and "Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** (problem-based)." (the branch
that is not IM-confirmed).

Phases are `phase_header` blocks, whose `minutes` must sum to `shared.duration`. That arithmetic
is an invariant nothing checks; see [[k12-package-consistency]].

### The problem set is enumerated from the standard, not chosen

`math.md` lines 57 to 64, verbatim:

> Before writing the practice problems (`shared.p1`..`pN`), ENUMERATE the standard's structural cases — the full span
> from the baseline case (the one every student must clear) to the structurally hardest case
> (the one students most often get wrong: start-unknown for K–2 story problems; a product
> smaller than both factors for decimal multiplication; the missing-leg case for the
> Pythagorean theorem; a midpoint or just-below-boundary number for rounding; a
> linear-but-not-proportional relationship for proportionality; and so on for other
> standards). Then write the set so EVERY enumerated case is a numbered, required problem (or
> the exit ticket), with its case named in that problem's `teacher` facet.

The first of the four coverage rules that follow, verbatim:

> A structural case that appears only in prose — the SWBAT, an anticipated challenge, a teacher
> move, or the Discuss notes — does NOT count as covered. If the plan's prose names a case, a
> numbered problem must present it to students.

### The exit ticket is selected, not written

`math.md` line 95, verbatim:

> - It IS the **structurally hardest enumerated case** (from the problem-set enumeration above; K–2: start-unknown or change-unknown), never a mid-difficulty stand-in. Pick it with the **misconception test**: a student who holds the lesson's primary anticipated misconception must get the exit ticket WRONG. If that student would get it right, you picked an affirming instance — swap it for the discriminating one (a lesson distinguishing X from not-X exits on the not-X case; a lesson fixing a placement habit exits where that habit produces a wrong answer). Name the case in `shared.exit_ticket.teacher`.

`math.md` line 99, verbatim:

> - 3 sort buckets — *Got it* / *Almost there* / *Needs re-teaching* — **each with explicit criteria** describing what a response in that bucket contains (e.g. "Got it: correct equation with the unknown where it lives in the story", not the bare label); all three criteria appear in the lesson plan, never truncated to labels.

## In practice

**Order of writing, which is not the order of sections.** The enumeration comes first, because
three later sections depend on it:

1. Enumerate the standard's structural cases, baseline to hardest.
2. Write `shared.p1`..`pN` so every case is a numbered required problem, each case named in that
   problem's `teacher` facet.
3. Pick the exit ticket as the hardest case, and run the misconception test against the primary
   misconception you wrote in section 3.
4. Write the three sort-bucket criteria in full. They land in the lesson plan and again on the
   observation template; see [[k12-observation-template]].
5. Now write sections 1 to 5 in order.

**Where each thing goes.** The four placements a reviewer will actually check:

| Content | Section |
|---|---|
| The one verbatim standard quotation, as a `special` callout | 1, `At a glance` |
| The prior standard, by code plus one plain sentence | 2, `Learning goal` |
| Misconceptions, each as *What students do* / *Why it happens* / *Teacher move* | 3, `Vocabulary & anticipated challenges` |
| Look-fors, 3 or more, inside Explore | 4, `Lesson sequence` |
| Rationale of any kind | 5, `Design notes`, last |

The standard quotation is pulled with the special `standard` key, which assembles
`standard_code` and `standard_text` into the callout. If both are absent no callout is produced
and the section renders one block shorter with no error; see [[k12-shared-registry]].

**The grounding that fills section 2 is a separate step.** The prerequisite standard is a Learning
Commons call, and the plugin states that not naming the prior standard is a critical failure. The
call sequence and its caps are [[practice-ground-a-lesson-end-to-end]] and
[[practice-resolve-a-standard-code]].

## Gotchas & constraints

**1. The section count and the section names differ by subject, and two of the four diverge
sharply.** Measured by this project's staging pass across the four reference files:

| subject | sections | notable divergence |
|---|---|---|
| math | 5 | the list above |
| ELA | 5 | section names byte-identical to math's five |
| science | 7 | no `Learning goal`; section 2 is `Three-dimensional learning targets`; `Vocabulary` is its own section 4; misconceptions are section 5 under `Anticipated student ideas & misconceptions` |
| social studies | 7 | `Exit ticket` is a top-level section 6, not the last phase in `Lesson sequence` |

Math, ELA and science all place the exit ticket as the last phase inside `Lesson sequence`, pulled
with `from_shared:exit_ticket` under its phase header. Social studies alone does not.

**2. Science's phase names differ by grade band, and none of them is Launch.** The four bands are
`Launch Phenomenon → Investigation → Sensemaking Discussion → Model/Representation → Exit Ticket`
for K to 2, and three further variants for 3 to 5, 6 to 8, and 9 to 12. Carrying math's
`Launch → Explore → Discuss → Synthesize → Exit Ticket` into a science lesson is wrong at every
band.

**3. A structural case named only in prose is not covered.** This is the rule that fails a plan
that reads well. If the SWBAT, an anticipated challenge, a teacher move or the Discuss notes names
a case, a numbered problem must present it to students. The check runs both directions and is
author-enforced only; the full set is [[k12-package-consistency]].

**4. `Discuss gets at least 10 minutes` is a floor, and shortening a lesson shrinks the other
phases.** The reference states this inline, in bold, with the instruction to shrink the other
phases rather than Discuss when the request is a short warm-up-style one.

**5. The three sort buckets appear in full or they are wrong.** The requirement is explicit
criteria describing what a response in that bucket contains, and "all three criteria appear in the
lesson plan, never truncated to labels." A plan carrying only the labels `Got it`, `Almost there`,
`Needs re-teaching` has not met the contract, and the observation template that pulls them inherits
the gap.

**6. Section 5 is last, after the exit ticket, and this is a hard ordering.** The reference states
the reason in the same sentence: "a teacher prepping reads the arc first, the reasoning second."
Rationale placed anywhere else, including a "why this works" note inside a phase, breaks the read.

**7. The heading strings are byte-exact and one of them is easy to get wrong.**
`Vocabulary & anticipated challenges` uses `&`. Sentence case is a density rule for every heading
in the package; see [[k12-density-rules]]. The differentiation skill uses Title Case section names
and does not share this convention, which is a trap when porting.

**8. Nothing validates any of this.** The staged extract records as this project's own measurement
that no script in either skill's `scripts/` directory performs any of these checks: there is no
arithmetic on `minutes`, no cross-document scan, and no coverage test anywhere in the render path.
A plan with four sections, no look-fors and a mid-difficulty exit ticket renders like any other.

## Related

- [[k12-document-set]] is the entry this document is, and the two fields that decide its filename
  and audience.
- [[k12-shared-registry]] is where the standard callout, the problems, the misconceptions, the
  look-fors and the exit ticket are registered so the plan and the worksheet cannot disagree.
- [[k12-block-types]] is the vocabulary these sections are built from, including `phase_header`.
- [[k12-density-rules]] holds the sentence-case heading rule, the half-page restructure rule, and
  the quote-the-standard-once rule that section 1 implements.
- [[k12-student-materials]] is the printed counterpart of the problem set enumerated here.
- [[k12-observation-template]] consumes the look-fors, the misconceptions and the three sort
  buckets this document defines.
- [[k12-package-consistency]] holds the coverage and arithmetic invariants that no script checks.
- [[k12-assessment-gap]] is why the exit-ticket difficulty bar set here is inherited by every quiz
  and exam item this project authors.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] supplies the verbatim standard statement, the
  prerequisite standard and the learning components that sections 1 and 2 require.
- [[practice-format-a-lesson-package]] is the authoring procedure that turns these five sections
  into a rendered document set.

## References

Local plugin files, read 2026-08-07 21:15 PDT, version `0.6.0`, no HTTP status:

- `k12-lesson-planning/references/math.md`, 161 lines, read in full. 40 to 54 curriculum branching
  and the phase names; 55 to 79 the enumeration and the four coverage rules; 80 to 89 the five
  sections; 91 to 100 the exit-ticket guidance and the three sort buckets.
- `k12-lesson-planning/SKILL.md`, 471 lines. 44 to 68 Step 0 Route, the routing map and the
  mandatory-load sentence.
- `k12-lesson-planning/references/example_lesson.json`, 667 lines. `documents[0]` section headings,
  confirmed byte-exact against the reference.
- `references/ela.md` 170 to 178, `references/science.md` 138 to 151 plus 69, 86, 104, 122, and
  `references/social_studies.md` 74 to 113. The three other subjects' sections and phase names.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/k12-plugin-contract.md`, primary. §3 the per-subject section structures with all four
  reproduced verbatim, §3.1 math, and §7 the invariants no script checks.
- `sources/k12-grounding-and-render.md`, primary. §1 and §2 the Step 2 grounding calls that fill
  sections 1 and 2, including the prerequisite call the plugin marks non-negotiable.
