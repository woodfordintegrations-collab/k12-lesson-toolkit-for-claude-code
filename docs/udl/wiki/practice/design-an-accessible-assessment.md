---
title: "Design an Accessible Assessment"
type: practice
sources:
  - https://nceo.info/Assessments/universal_design
  - https://nceo.info/Assessments/general_assessment/accessibility-and-accommodations
  - https://www.aera.net/publications/books/standards-for-educational-psychological-testing-2014-edition
  - sources/practice-assessment-accessibility.md
  - sources/practice-standards-alignment.md
updated: 2026-08-07
---

# Design an Accessible Assessment

## Summary

This is the practice page for building or reviewing an assessment instrument itself,
not a lesson activity. The operating rule is one sentence: **vary how the construct is
demonstrated, never what is measured.** Everything else on this page is that rule
worked out in enough detail to apply it, grounded in measurement theory
([[construct-irrelevant-variance]]) rather than intuition about fairness.

## When to reach for it

Reach for this page when you are deciding whether a proposed change to a test,
quiz, or performance task is legitimate access work or an accidental change to what
the assessment measures.

| The actual problem | Where to go instead |
|---|---|
| You're designing a lesson, not an assessment instrument | [[design-a-lesson-with-udl]] |
| You're checking an existing lesson for barriers | [[audit-a-lesson-for-barriers]] |
| You're reading a standard's verb to find the construct it embeds | [[apply-udl-to-a-standard]] |
| You're evaluating a curriculum program, not a single assessment | [[evaluate-curriculum-materials-for-udl]] |
| The question is whether a digital assessment is legally accessible (WCAG, Section 508) | [[mistaking-udl-for-accessibility-compliance]] |
| The question is whether a student's IEP-based accommodation is still needed | [[assuming-udl-replaces-accommodations]] |
| A learner has the accommodation but can't operate the tool it depends on | [[access-to-assistive-technologies]] |

The diagnostic question for this page specifically: **does this change alter the
score's meaning, or only the path a student takes to earn it?** If you can't answer
that, you can't yet tell whether you're looking at an accommodation or a
modification, and that distinction is the whole practice.

## How it works

**Construct-irrelevant variance (CIV)** is the technical name for what UDL calls a
barrier, applied to measurement. The *Standards for Educational and Psychological
Testing* (2014, AERA/APA/NCME) devotes a section to "Minimizing Construct-Irrelevant
Components Through Test Design and Testing Adaptations." CAST's own framing of the
stakes: "Universally designed assessments identify and eliminate unintended and/or
irrelevant barriers in the measurement itself." That is a design-time claim, not a
test-time patch: CIV is something you remove by building the assessment differently,
not something you compensate for afterward with an accommodation bolted on.

This gives the field a precise, load-bearing distinction that ordinary language
("make it more accessible") does not carry:

| | Accommodations | Modifications |
|---|---|---|
| **What changes** | Presentation format, response mode, setting, or timing | The task itself: item difficulty, content, or scope |
| **What stays fixed** | The construct being measured | Nothing: the construct shifts |
| **Effect on scores** | Should not, by itself, meaningfully shift score distributions | Elevates scores by lowering cognitive demand |
| **Score comparability** | Preserved: scores remain comparable to the standard form | Not preserved: scores are not comparable to the standard form |
| **NCEO's own words** | "The purpose of an accommodation is to remove disadvantages due to conditions that are irrelevant to the construct the test is intended to measure without giving unfair advantage to those being accommodated." | Changes "what the test measures," producing scores on a different construct |

This table is the practical core of the page. Everything in **In practice** below is
either applying it or stress-testing it against a real case.

## In practice

**The operating rule, restated as a design move.** Before changing anything about an
assessment, name the construct in one sentence. Then ask of the proposed change: does
a student who lacks the construct-irrelevant thing this change addresses, but who has
the construct, now score the same as a student who never lacked it? If yes, you have
an accommodation. If the change also helps students who already had full access, or
if it changes what counts as a correct or complete answer, you are looking at a
modification, whatever it is called in the paperwork.

**The five standard accommodation categories.** NCEO groups accommodations into five
buckets. Treat this as the menu you actually design from, not an abstract idea of
"flexibility":

1. **Setting**: separate testing location, individual administration, small group.
2. **Timing/scheduling**: extended time, frequent breaks, alternative testing
   windows.
3. **Presentation**: questions read aloud (live, recorded, or synthesized speech),
   font enlargement, braille format, simplified formatting.
4. **Response**: dictation to a scribe, word processor instead of handwriting,
   speech-to-text, alternative keyboard.
5. **Other**: bilingual glossaries, mathematics formula sheets, when the formula
   itself is not the construct.

Every one of these leaves the construct alone. If you find yourself designing
something that doesn't fit cleanly into one of these five categories, that is a
signal to check whether you've drifted into modification territory.

**The score-distribution heuristic, and its real nuance.** The measurement principle
NCEO states directly: "a valid accommodation should not change score distributions
significantly if it truly addresses only construct-irrelevant variance. If an
accommodation causes substantial score increases, it likely introduced construct
modification rather than access." Read this precisely, because the naive version of
it is wrong. The test is not "did scores go up" in general: a genuine accommodation
is *supposed* to raise the scores of students who were blocked by the barrier it
removes. The test is whether the increase is **differential** (concentrated in
students who actually had the barrier) or **universal** (an across-the-board lift,
including students who never had it). Beddow (2011) is the empirical case for this:
modifications were shown to raise average scores across both students with and
without IEPs, because lowering item difficulty helps everyone, not just the students
the change was ostensibly designed for. A change that helps students who didn't need
help is diagnostic of a modification, not confirmation of good accommodation design.

**The seven elements of an accessible design, from the start.** NCEO frames these as
what to build in at the outset rather than retrofit later:

1. Inclusive assessment population: design for the full range of test-takers from
   the outset.
2. Precisely defined constructs: clarity about what is measured reduces
   construct-irrelevant demands.
3. Accessible, non-biased items: no unnecessarily complex language, visual
   ambiguity, or cultural assumptions.
4. Amenable to accommodations: the design permits meaningful accommodations
   (braille, speech-to-text) without compromising the construct.
5. Simple, clear, intuitive instructions and procedures.
6. Maximum readability and comprehensibility: prose minimizes cognitive load
   unrelated to the construct.
7. Maximum legibility: contrast, font, and spacing remove barriers for readers with
   low vision.

NCEO's implementation pathway sequences this as nine steps: **Plan → Define purpose →
Require design in contracts → Address design during development → Include expertise
in reviews → Test usability → Conduct tryouts → Analyze results → Monitor and
revise.** Note where "design in contracts" and "expertise in reviews" sit: before
development, not after a draft exists. Accessible assessment design is treated as a
procurement and specification discipline, not a proofreading pass.

**A worked pass.** A district math test asks students to solve word problems. The
construct is mathematical reasoning: identifying the operation and executing it
correctly. The items are written in dense paragraph form with two or three subordinate
clauses each.

A student with a print-reading disability cannot access the problem at all, not
because they lack the math but because the reading load is standing between them and
the construct. Text-to-speech or a human reader is a clean accommodation here: it
removes a barrier (decoding text) that sits entirely outside the construct (reasoning
about the operation), and a student's score should rise only if they actually have
the math and were previously blocked by the reading demand.

Now change one fact: the test is a reading-comprehension assessment and the "word
problem" format exists specifically to test whether a student can extract a
mathematical operation from prose. Here the same text-to-speech accommodation is a
modification, because decoding and parsing the prose *is* the construct. The tool
didn't change. The construct did, and that changes what the same design move counts
as. This is why "name the construct in one sentence, first" is not a formality: it
is the entire determination, and it has to happen before you evaluate any specific
accommodation.

## Gotchas & constraints

- **The tension with standardized accountability testing is real and this page does
  not resolve it.** Large-scale accountability assessments are built for inexpensive
  delivery, standardization across conditions, and cost-efficient scoring, which
  historically produces multiple-choice, paper-and-pencil formats with simple scoring
  algorithms. UDL's flexibility pulls the opposite direction. Four specific
  frictions: **format rigidity** (recognition/recall items are cheap to score;
  sophisticated cognitive tasks are expensive to develop and score at scale),
  **timing constraints** (universal administration windows resist the flexible
  scheduling that would reduce time pressure as a barrier), **scoring algorithms**
  (automated correct/incorrect scoring can't absorb complex, multidimensional
  response formats), and **comparability demands** (high-stakes testing needs scores
  comparable across cohorts and demographic groups, which pushes toward homogeneous
  item sets rather than diverse ones). NCEO's own conclusion: "universally designed
  assessments will not eliminate the need for all accommodations. However, they may
  reduce the need for them." Federal guidance echoes this by requiring UDL principles
  in state assessment design "to the extent practicable," a phrase that concedes the
  limit rather than closing it. Full UDL flexibility and standardized accountability
  testing are not fully reconcilable goals, and no amount of good design on this page
  makes that tension disappear.
- **Technical accessibility (WCAG, Section 508) and UDL design are different
  obligations with different tests.** WCAG 2.2 is a binary, testable standard: a
  success criterion is met or it isn't. UDL has no success criteria at all. A test can
  conform fully to WCAG AA and still be pedagogically rigid (multiple-choice only,
  no alternative response formats, high time pressure), and a pedagogically rich
  UDL-designed assessment can fail technical accessibility (images with no
  alternative text) despite good pedagogical design. Neither substitutes for the
  other. See [[mistaking-udl-for-accessibility-compliance]] and
  [[access-to-assistive-technologies]].
- **Practitioners routinely fail to distinguish accommodations from modifications.**
  Research (Cisar, 2004) found special educators and administrators scoring
  significantly higher than general-education and elective teachers at telling the
  two apart and applying them correctly, a gap that has held up in later studies.
  This is not a fringe confusion; it is the default state of general-education
  assessment practice, which is exactly why the table above is worth keeping
  visible rather than assumed.
- **Good accommodation design does not retire the underlying entitlement.** An
  individual student's IEP- or 504-plan-based right to a specific accommodation is a
  legal matter, not a UDL design choice. See
  [[assuming-udl-replaces-accommodations]].
- **This page is a design procedure, not an outcomes claim.** UDL's outcome evidence
  is moderate and how to operationalize it is contested, and fidelity to a UDL
  procedure is itself hard to measure. See [[does-udl-improve-student-outcomes]] and
  [[measuring-udl-implementation-fidelity]]. Neither caveat undercuts the
  accommodation/modification distinction above, which rests on measurement theory,
  not on UDL's outcome literature.
- **AI and generative tools in assessment design are unconfirmed territory.** As of
  the sources staged for this page, no standards body (AERA, APA, NCME, CAST, NCEO)
  has issued authoritative guidance on generative AI in assessment design or
  materials accessibility. What exists is emerging practice research: AI can help
  generate alt-text and image descriptions when given explicit accessibility
  instructions, but unconfigured generative tools reliably produce accessible text
  while often producing inaccessible images, diagrams, and interaction patterns.
  Whether AI-generated assessment items introduce or reduce construct-irrelevant
  variance is, per the staged source, simply not known yet. Treat AI-generated
  assessment materials with the same validation and technical-accessibility audit
  as any human-authored material, not less.

## Related

[[construct-irrelevant-variance]]
[[firm-goals-flexible-means]]
[[access-to-assistive-technologies]]
[[mistaking-udl-for-accessibility-compliance]]
[[assuming-udl-replaces-accommodations]]
[[apply-udl-to-a-standard]]
[[lowering-rigor-in-the-name-of-flexibility]]
[[scientifically-valid-the-statutory-claim]]
[[does-udl-improve-student-outcomes]]
[[measuring-udl-implementation-fidelity]]

## Composes with

_Reserved for a later composition phase._

## References

1. [NCEO: Universal Design of Assessments](https://nceo.info/Assessments/universal_design)
2. [NCEO: Accessibility & Accommodations for General Assessments](https://nceo.info/Assessments/general_assessment/accessibility-and-accommodations)
3. [Standards for Educational and Psychological Testing (2014) (AERA)](https://www.aera.net/publications/books/standards-for-educational-psychological-testing-2014-edition)
4. `sources/practice-assessment-accessibility.md` (staged research synthesis, fetched 2026-08-07)
5. `sources/practice-standards-alignment.md` (staged research synthesis, fetched 2026-08-07)
