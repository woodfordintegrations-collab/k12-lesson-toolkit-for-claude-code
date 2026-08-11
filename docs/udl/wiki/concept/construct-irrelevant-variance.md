---
title: "Construct-Irrelevant Variance"
type: concept
sources:
  - https://www.aera.net/publications/books/standards-for-educational-psychological-testing-2014-edition
  - https://onlinelibrary.wiley.com/doi/10.1002/j.2333-8504.1994.tb01618.x
  - https://nceo.info/Assessments/general_assessment/accessibility-and-accommodations
  - sources/practice-assessment-accessibility.md
  - sources/practice-standards-alignment.md
updated: 2026-08-07
---

# Construct-Irrelevant Variance

## Summary

Construct-irrelevant variance (CIV) is the measurement-theory version of
[[firm-goals-flexible-means]], and the strongest bridge this wiki has between UDL and
psychometrics. Precisely: **variance in scores attributable to factors irrelevant to
the construct being measured, which degrades the validity of the score inferences drawn
from those scores.** The concept and its treatment come from measurement theory, not
from CAST. UDL borrows it and gives it a design mandate: eliminate CIV through better
initial design rather than compensate for it after the fact at test time.

## When to reach for it

Reach for this page when you need the construct-validity vocabulary, not the plain
pedagogical framing. If you're talking to someone with measurement training, or you're
deciding whether a specific change to an assessment is defensible, this is the
precise version.

| The actual problem | Where to go instead |
|---|---|
| You want the plain-language design move for a lesson, not the validity framing | [[firm-goals-flexible-means]] |
| You're deciding whether removing an accommodation is legally or ethically defensible | [[assuming-udl-replaces-accommodations]] |
| You want the technical/legal accessibility layer, not the validity layer | [[mistaking-udl-for-accessibility-compliance]] and [[access-to-assistive-technologies]] |
| You're building a new assessment, not diagnosing an existing one | [[design-an-accessible-assessment]] |
| You're auditing an existing lesson or assessment rather than designing one fresh | [[audit-a-lesson-for-barriers]] |
| You want to know whether "removing CIV" is a demonstrated empirical effect, not just a design principle | [[measuring-udl-implementation-fidelity]] |

## How it works

CIV is variance in test scores that reflects factors unrelated to what the test is
designed to measure, factors that cloud the assessment's ability to measure the focal
construct and adversely affect the meaningfulness and validity of the resulting score
inferences. This definition, and the framework for controlling it, comes from the
**Standards for Educational and Psychological Testing** (2014), developed jointly by
the American Educational Research Association, the American Psychological Association,
and the National Council on Measurement in Education. The 2014 revision explicitly
addresses "Minimizing Construct-Irrelevant Components Through Test Design and
Testing Adaptations."

The theoretical foundation underneath the 2014 Standards is **Messick's unified
validity framework** (1995). Messick identified six distinguishable aspects of
construct validity: content, substantive, structural, generalizability, external, and
consequential. The consequential aspect is the one that carries CIV: it explicitly
encompasses fairness and bias concerns, including sources of construct-irrelevant
variance, that threaten score validity across populations.

Typical sources of CIV: reading-comprehension demands irrelevant to the content being
assessed, ability to perform under time pressure, writing ability when writing is not
the construct, handwriting legibility, visual acuity, auditory processing speed, and
anxiety in the test-taking environment itself.

UDL's application of this is direct: **a barrier is construct-irrelevant when removing
it does not change what is being measured.** CAST states the design implication
plainly: "Universally designed assessments identify and eliminate unintended and/or
irrelevant barriers in the measurement itself." This is a measurement-first argument,
not a leniency argument. Removing CIV is not lowering standards. It's improving the
validity and fairness of the measurement.

## In practice

**The accommodation/modification distinction carries directly from this.** Both change
an assessment; they differ in what they do to the construct.

- **Accommodations** change *how* a construct is demonstrated (presentation format,
  response mode, setting, timing) while holding the construct itself constant. A valid
  accommodation removes construct-irrelevant barriers and preserves score
  comparability.
- **Modifications** change *what* is measured (reduced item difficulty, simplified
  content, narrowed scope). Modifications produce scores on a different construct, and
  those scores are generally not comparable to scores from the standard form.

NCEO's formal statement of the same line: "The purpose of an accommodation is to remove
disadvantages due to conditions that are irrelevant to the construct the test is
intended to measure without giving unfair advantage to those being accommodated."

**The empirical signature is the useful part for a measurement-trained reader.**
Beddow (2011) found that modifications raised average scores across both students with
IEPs and students without them, by altering the cognitive demand of the items rather
than simply removing a barrier to access. Score elevation of that kind is the signature
of construct shift, not barrier removal. This gives a working test: a valid
accommodation that only addresses CIV should not, on its own, produce a large score
increase. If it does, it likely modified the construct rather than granting access to
it.

NCEO groups accommodations into five categories, useful as a checklist when auditing
whether a proposed change is construct-preserving:

1. **Setting**: separate location, individual administration, small group.
2. **Timing/scheduling**: extended time, frequent breaks, alternative windows.
3. **Presentation**: questions read aloud, font enlargement, braille, simplified
   formatting.
4. **Response**: dictation to a scribe, word processor instead of handwriting,
   speech-to-text, alternative keyboard.
5. **Other**: bilingual glossaries, formula sheets when the formula itself is not the
   construct.

**A worked case.** A word problem is meant to measure whether a student can perform a
given arithmetic operation. The reading demand needed to extract the relevant
quantities from the text is CIV relative to that construct, and reading the problem
aloud is a legitimate accommodation. If the same problem is meant to measure whether a
student can extract relevant quantities from a text themselves, the reading demand is
now part of the construct, and reading it aloud would be a modification. Same
accommodation, same test item, opposite classification, because the construct changed.

## Gotchas & constraints

- **This is a real, documented gap in practice, not a hypothetical.** Cisar (2004)
  found that special educators and administrators scored significantly higher than
  general-education and elective teachers at distinguishing accommodations from
  modifications and at applying the distinction appropriately, a finding that has held
  across subsequent studies. Reading a definition is not the same as being able to
  apply it under the pressure of a real classroom decision.
- **CIV is a validity concept, not a legal-accessibility concept, and the wiki keeps
  that line visible on purpose.** WCAG conformance is necessary but not sufficient for
  CIV elimination: a test can be technically screen-reader accessible while still
  bundling irrelevant reading demand into a math score, and a pedagogically excellent,
  CIV-free assessment can still fail a screen reader on technical grounds. See
  [[mistaking-udl-for-accessibility-compliance]].
- **Large-scale standardized testing has a genuine, unresolved tension with this.**
  NCEO's own assessment: "universally designed assessments will not eliminate the need
  for all accommodations. However, they may reduce the need for them." Comparability
  demands across cohorts and demographic groups push accountability testing toward
  homogeneous, standardized formats that resist the flexibility CIV elimination would
  otherwise call for. Universal design reduces CIV within these constraints; it does
  not resolve the constraints.
- **The whole exercise depends on a precisely defined construct.** If the thing being
  measured is vague, "construct-irrelevant" has nothing to be irrelevant to, and the
  distinction collapses. This is the same precondition [[firm-goals-flexible-means]]
  runs into from the design side.

## Related

[[firm-goals-flexible-means]]
[[design-an-accessible-assessment]]
[[access-to-assistive-technologies]]
[[mistaking-udl-for-accessibility-compliance]]
[[apply-udl-to-a-standard]]
[[assuming-udl-replaces-accommodations]]
[[measuring-udl-implementation-fidelity]]

## Composes with

_Reserved for a later composition phase._

## References

1. [Standards for Educational and Psychological Testing (2014)](https://www.aera.net/publications/books/standards-for-educational-psychological-testing-2014-edition) (AERA/APA/NCME)
2. [Messick, S., Unified Validity Framework (1995)](https://onlinelibrary.wiley.com/doi/10.1002/j.2333-8504.1994.tb01618.x)
3. [NCEO, Accessibility & Accommodations for General Assessments](https://nceo.info/Assessments/general_assessment/accessibility-and-accommodations)
4. [Beddow (2011)](https://nceo.info/references/article-journal/11951) (via NCEO reference database)
5. `sources/practice-assessment-accessibility.md`: staged extract, fetched 2026-08-07
6. `sources/practice-standards-alignment.md`: staged extract, fetched 2026-08-07
