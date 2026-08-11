---
title: "Does UDL Improve Student Outcomes?"
type: evidence
sources:
  - https://doi.org/10.1016/j.tate.2022.103956
  - https://doi.org/10.1080/13603116.2017.1325074
  - https://doi.org/10.1080/2331186X.2023.2218191
  - sources/evidence-meta-analyses.md
  - sources/evidence-critiques.md
updated: 2026-08-07
---

# Does UDL Improve Student Outcomes?

## Summary

There is a moderate positive pooled effect for UDL instruction on academic achievement:
**g = 0.43, 95% CI [0.19, 0.67], k = 20** (King-Sears et al., 2023). That is the
strongest number in this literature and it is a real one. What it is an effect *of* is
the unsettled part: the studies pooled into it do not share an operationalization of
"UDL", and the broader review literature is dominated by one-group pre-post designs
measuring process and perception rather than learning.

## When to reach for it

Reach for this page when someone asserts that UDL is or is not evidence-based and you
need to know what the number actually is, what it was measured against, and what it
cannot carry.

| The actual question | Where to go instead |
|---|---|
| Is "scientifically valid" in federal law a research finding? | [[scientifically-valid-the-statutory-claim]] |
| Can you even tell whether UDL was implemented? | [[measuring-udl-implementation-fidelity]] |
| Is this the learning-styles hypothesis renamed? | [[udl-and-the-learning-styles-problem]] |
| Does the three-networks story hold up? | [[the-neuroscience-basis-claim]] |
| What does district-scale adoption actually run into? | [[implement-udl-at-school-scale]] |

This page is deliberately not a teacher-facing page. If you want the practice, start at
[[design-a-lesson-with-udl]]. If you want to know whether the practice is warranted by
research, you are in the right place.

## The claim

Stated so it can fail:

> **Instruction designed to UDL principles produces better academic outcomes than
> business-as-usual instruction delivered to comparable learners.**

The falsifier is a pooled estimate on achievement measures, under controlled comparison,
whose confidence interval includes zero. This is the estimand King-Sears et al. (2023)
actually targeted: the staged extract records their design as "UDL-based interventions
vs. business-as-usual control conditions, academic achievement as outcome".

The claim is made in three registers, and they are not the same claim.

**Statutory.** Federal law defines UDL rather than finding it effective. 20 U.S.C.
§ 1003(24) reads: *"'Universal design for learning' means a scientifically valid
framework for guiding educational practice that (A) provides flexibility in the ways
information is presented, in the ways students respond or demonstrate knowledge and
skills, and in the ways students are engaged..."* "Scientifically valid" sits inside a
definition, not a findings section. It is a legislative stipulation with no cited
evidentiary basis in the statute, and treating it as an empirical result is a category
error. [[scientifically-valid-the-statutory-claim]] takes this apart.

**Advocacy.** CAST's own timeline framing, quoted in the critique extract, describes
"the first 10 years of UDL implementation" as an **Advocacy Phase** in which "CAST
shared the message of UDL with substantial numbers of educators". Boysen (2024) audited
what sits behind the Guidelines and concluded that "the cited evidence behind CAST's UDL
guidelines is weak", and that "the cited studies provided little evidence for claims
about UDL, with most studies not offering a choice to learners or measuring learning".
Note what is being audited there: not whether UDL works, but whether the citations
attached to the Guidelines support the Guidelines. Those are separable questions and the
literature routinely runs them together.

**Research.** The peer-reviewed synthesis literature makes the narrowest and most
testable version, and it is the only register that reports intervals. That is the
version this page evaluates.

## What the evidence shows

### King-Sears et al. (2023): the strongest entry

King-Sears, M. E., Stefanidis, A., Evmenova, A., Rao, K., Mergen, R. L., Owen, L. S., &
Strimel, M. M. (2023). *Achievement of learners receiving UDL instruction: A
meta-analysis.* Teaching and Teacher Education, 122, 103956.

| | Value (verbatim from source) |
|---|---|
| Design | Meta-analysis; UDL-based interventions vs. business-as-usual control conditions |
| Outcome | Academic achievement |
| k | 20 studies |
| N | Not individually specified; 50 individual effects extracted from 20 studies; participants ranged pre-K to adult |
| **Overall combined effect** | **g = 0.43, 95% CI [0.19, 0.67]** |
| School-aged learners | g = 0.48 (CI not retrieved) |
| Adult learners | g = 0.28 (CI not retrieved) |
| Small-group instruction | g = 0.86 (CI not retrieved) |
| Large-group instruction | g = 0.30 (CI not retrieved) |
| Moderators | Five significant moderators found; the specific moderators were not individually retrieved into the staged source |

Two things about this table deserve to be read carefully rather than skimmed.

**Only the overall estimate carries an interval.** The subgroup values are point
estimates with no CI in the staged source. The small-group/large-group gap (0.86 vs
0.30) is the most quotable contrast on the page and it is precisely the one that cannot
be tested from what is recorded here. It is also confounded in the obvious direction:
small-group instruction is an intervention in its own right, independent of UDL.

**50 effects from 20 studies is a dependency structure.** Multiple effects per study
violate the independence assumption of a naive random-effects model, and the staged
source does not record whether a multilevel or robust-variance approach was used. That
is a gap in this page's evidence, not a defect established in the paper. Anyone leaning
hard on the interval should read the primary article for the model specification.

### Capp (2017): process improved, outcomes did not follow

Capp, M. J. (2017). *The effectiveness of universal design for learning: A meta-analysis
of literature between 2013 and 2016.* International Journal of Inclusive Education,
21(8), 791–807.

- Design: meta-analysis of empirical research with pre- and post-test measurement
- Initial search: 924 UDL articles reviewed; final inclusion: 18 studies with pre/post design
- k = 18
- N: not retrieved
- **Effect size: not reported; not retrieved into the staged source**

All 18 included studies supported that "UDL is an effective teaching methodology for
improving the learning process for all students". And then the sentence that matters
most on this whole page:

> "The impact on educational outcomes has not been demonstrated."

This is not a null result being spun. It is a review that found consistent support on
one construct and could not reach the other, because the studies it had did not measure
the other. **Learning process improved; educational outcomes were not demonstrated.**
Those are different dependent variables, and the distinction survives every later
citation of Capp as "a meta-analysis showing UDL is effective". It is effective *at the
thing the studies measured*, which was largely not achievement.

The staged source draws the inference explicitly, and it is the right one: this pattern
suggests "selection bias toward process measures in early literature".

### Almeqdad et al. (2023): a number that cannot be compared

Almeqdad, H., Alodat, A., et al. (2023). *The effectiveness of universal design for
learning: A systematic review of the literature and meta-analysis.* Cogent Education,
10, 2218191.

- Design: systematic review with meta-analysis
- Inclusion: empirical peer-reviewed research (pre- and post-design), 2015–2021, English and Arabic
- k = 13; six countries; K-12 or higher education
- N: not specified
- Effect size, verbatim: **"Total effect sizes for the identified studies were 3.56"**

**Do not put 3.56 next to 0.43.** The staged source flags the metric as ambiguous: it
"appears to be a sum or aggregated metric rather than a standardized Cohen's *d* or
Hedges' *g*", and the exact calculation method was not retrieved. A standardized mean
difference of 3.56 on educational achievement would be an extraordinary claim; the far
likelier reading is that it is not a standardized mean difference at all. Until the
metric is identified from the primary article, the number is uninterpretable rather
than large, and any comparison built on it is meaningless.

What is interpretable from this study:

- "Considerable heterogeneity was evident."
- Most included studies used one-group designs with no control condition.
- Statistically significant effect sizes were reported for one-group studies, studies
  with student participants, studies in specific (rather than generic) domains, and
  quantitative research designs.
- Studies implementing all three principles together produced higher positive
  educational gains than studies using one or two.

That last finding is interesting and weak at once. It is a between-study comparison
across a heterogeneous set, not a dismantling design, so it does not isolate an additive
effect of combining [[multiple-means-of-engagement]],
[[multiple-means-of-representation]], and
[[multiple-means-of-action-and-expression]].

### The reviews that named the operationalization problem

**Ok, M. W., Rao, K., Bryant, B. R., & McDougall, D. (2017).** *Universal design for
learning in pre-K to grade 12 classrooms: A systematic review of research.*
Exceptionality, 25(2), 116–138.

- Design: systematic literature review, non-meta-analytic
- k = 13; N not specified
- Effect size, verbatim: **"Effect sizes ranging from small to large"**, with no specific
  Cohen's *d*, *g*, or CI provided
- Finding: "UDL-based instruction has the potential to increase engagement and access to
  general education curriculum for students with disabilities, and improve students'
  academic and social outcomes." Efficacy "varied considerably within and across studies."
- Limitations named: no standard formats for describing UDL operationalization;
  inconsistent research designs; no consensus on how to measure UDL implementation

**Rao, K., Ok, M. W., & Bryant, B. R. (2014).** *A review of research on Universal
Design Educational Models.* Remedial and Special Education, 35(3), 153–166.

- Design: descriptive review, narrative synthesis
- k = 13; N not specified
- Effect size: **not reported**
- Finding: "Researchers report on their application of UD principles in varied ways, with
  no standard formats for describing how UD is used."
- Diversity of designs (quasi-experimental, single-subject, qualitative) precluded effect
  size synthesis; no causal link established between UD principles and outcomes

### The reviews with no pooled estimate

Two recent systematic reviews are in the staged source and report **no effect sizes**:

| Review | Design | k | N | Effect size |
|---|---|---|---|---|
| Faculty training in UDL in higher education (2025), *International Journal for Academic Development* | Systematic review | 20 | 5,656 (363 faculty, 5,293 students) | Not reported |
| Bray, Flood, Reale & Terrenzio (2024), *British Journal of Educational Technology*, 55(1), 113–138 | Systematic review, thematic synthesis | 15 | Not specified | Not reported |

The 2025 review reports that "specific training in UDL increases teaching competence and
promotes inclusive and effective pedagogical practices" and that UDL approaches "improve
learning, accessibility, and participation for all students", as thematic findings from
a qualitative synthesis, with no quantitative estimate behind them. Its own stated
limitation is that evidence on UDL in postsecondary STEM is limited, and that it remains
open "which core UDL components require strict fidelity vs. contextual adaptation".

### The structural findings

These are findings, not caveats. They constrain what any pooled number can mean.

**1. No consensus operationalization.** Across reviews spanning 2014 to 2024, the same
defect is named: there is no standard account of what makes an instructional design a
UDL design. Ok et al. (2017) and Rao et al. (2014) both state it as "no standard formats
for describing how UD is used". The critique extract records it as agreed even by
proponents: definitional vagueness "is not disputed even by UDL proponents; their
response is typically to call for better operationalization rather than to deny the
problem". Edyburn's framing in the same extract: "Knowing what UDL looks like is an
essential step in measuring the outcomes of UDL." See
[[measuring-udl-implementation-fidelity]].

**2. One-group pre-post designs predominate.** Almeqdad et al. (2023) is explicit that
its included studies mainly used one-group quantitative designs. Capp (2017) restricted
inclusion to pre/post-test designs. Uncontrolled pre-post designs absorb maturation,
regression to the mean, testing effects, and expectancy into the estimate, and they
inflate it. King-Sears et al. (2023) is the entry that is not exposed to this, because
its comparison is against business-as-usual control conditions, which is exactly why
its smaller number is the more credible one.

**3. Outcomes skew to process and perception.** The critique extract states it plainly:
"While studies often report a positive perception of the subjects' learning process and
the teaching material, there are hardly any studies reporting on the learning gains."
This is why Capp's process/outcome split is the single most useful result here. A
literature that measures satisfaction and access, then gets cited as demonstrating
achievement, is a literature whose headline claim outruns its dependent variables.

**4. The audit of the citation base is separate and also negative.** Boysen (2024) found
the evidence cited behind the Guidelines weak, and Murphy (2021) went further: "No
rigorous published research has demonstrated any improvement in an education intervention
designed with UDL principles in mind... The only evidence-based conclusion that can be
made about UDL is that further study is required." Murphy's statement predates
King-Sears et al. (2023) and, read as written, is no longer accurate about the pooled
achievement literature. It remains accurate about the citation base behind the framework
document, which is what Boysen re-examined a year later.

### The whole picture in one table

Values are verbatim from the staged source; "not reported" and "not retrieved" mean
exactly that.

| Study | Year | Design | k | Effect size | 95% CI |
|---|---|---|---|---|---|
| King-Sears et al. | 2023 | Meta-analysis (vs. business-as-usual) | 20 | g = 0.43 | [0.19, 0.67] |
| King-Sears et al. (school-aged) | 2023 | Meta-analysis | 20 | g = 0.48 | not retrieved |
| King-Sears et al. (adult) | 2023 | Meta-analysis | 20 | g = 0.28 | not retrieved |
| King-Sears et al. (small-group) | 2023 | Meta-analysis | 20 | g = 0.86 | not retrieved |
| King-Sears et al. (large-group) | 2023 | Meta-analysis | 20 | g = 0.30 | not retrieved |
| Almeqdad et al. | 2023 | Meta-analysis, mostly one-group | 13 | 3.56 (metric ambiguous) | not retrieved |
| Capp | 2017 | Meta-analysis, pre/post only | 18 | effect size not reported | n/a |
| Ok, Rao, Bryant & McDougall | 2017 | Systematic review | 13 | "small to large" range | n/a |
| Rao, Ok & Bryant | 2014 | Descriptive review | 13 | not reported | n/a |
| Faculty training review | 2025 | Systematic review | 20 | not reported | n/a |
| Bray et al. | 2024 | Systematic review | 15 | not reported | n/a |

## Gotchas & constraints

- **A positive pooled effect over heterogeneous interventions does not identify UDL as
  the active ingredient.** This is the central constraint and it is not a rhetorical
  hedge. If the 20 studies behind g = 0.43 each call something different "UDL", the
  estimate is an average over a bundle of instructional moves (graphic organizers,
  choice, scaffolded practice, technology, small-group arrangement), most of which have
  their own independent evidence bases. Nothing in the staged source supports attributing
  the effect to the framework rather than to its constituents, and the framework's own
  reviewers say the operationalization needed to make that attribution does not exist.
  King-Sears et al. name this among their limitations: "limited specificity on which UDL
  principles or combinations drive effects".

- **Heterogeneity is stated, quantified nowhere in the staged source.** King-Sears et al.
  report "considerable heterogeneity in included studies"; Almeqdad et al. report
  "considerable heterogeneity was evident". No *I²*, *τ²*, or *Q* is recorded here for
  any of these meta-analyses. With intervals that narrow (0.19 to 0.67) and heterogeneity
  that emphatic, the prediction interval for a new study is the quantity you would
  actually want, and it is not available from this source.

- **No publication-bias diagnostic is recorded for any entry.** The staged extract
  reports no funnel plot, trim-and-fill, Egger's test, or *p*-curve for King-Sears et al.,
  Capp, or Almeqdad et al. That is an absence in this page's evidence, not a demonstrated
  absence in the papers. But note the specific direction of concern the literature does
  document: Capp's process/outcome asymmetry is described in the source as suggesting
  "selection bias toward process measures", which is a distinct and possibly larger
  problem than small-study bias. It is bias in the choice of dependent variable, not in
  which results get published.

- **The reviews are not independent replications.** Capp (2017) covers 2013–2016,
  Almeqdad et al. (2023) covers 2015–2021, and King-Sears et al. (2023) has no window
  recorded in the staged source. The overlap between their included-study sets is not
  reported anywhere in the source. Three syntheses agreeing is weak corroboration if they
  are largely reading the same primary studies, and there is no basis here for deciding
  how much they are.

- **The 3.56 must not be laundered into a comparison.** Its metric is unidentified. It is
  not evidence of a very large effect; it is evidence that the number was not reported in
  a form that can be compared to anything.

- **Higher education is thin, and postsecondary STEM thinner.** The 2025 faculty-training
  review states that evidence on UDL implementation in postsecondary STEM is limited.
  Bray et al. (2024) exists specifically because prior UDL research "focused primarily on
  higher education" at the *second level's* expense, which tells you the coverage is
  uneven by sector rather than deep anywhere. King-Sears et al. do report an adult-learner
  subgroup (g = 0.28), lower than the school-aged value (g = 0.48) and without a retrieved
  CI. Treat higher-ed claims as materially less supported than K-12 claims.

- **A defect in the staged extract, disclosed.** The extract lists DOI
  `10.1177/0741932513518980` for *both* Ok et al. (2017, *Exceptionality*) and Rao et al.
  (2014, *Remedial and Special Education*). Both cannot be correct. Verify the Ok et al.
  (2017) identifier against the journal before citing it; this page reports what the
  staged source contains rather than guessing which entry is wrong.

- **What this page does not license.** It does not license "UDL is evidence-based" as an
  unqualified claim, and it does not license "UDL is pseudoscience" either. The defensible
  reading is narrower and duller than both: instruction that researchers labelled UDL
  outperformed business-as-usual on achievement by roughly two-fifths of a standard
  deviation across 20 studies, in a literature that cannot yet say what the label denotes.
  The pairing of a real effect with an undetermined construct is the finding.

- **Effect sizes are not accessibility.** None of this bears on legal obligation. A
  positive *g* does not make a material accessible, and no UDL result substitutes for
  Section 504, ADA, or WCAG conformance. See
  [[mistaking-udl-for-accessibility-compliance]] and
  [[assuming-udl-replaces-accommodations]].

## Related

[[measuring-udl-implementation-fidelity]]
[[scientifically-valid-the-statutory-claim]]
[[udl-and-the-learning-styles-problem]]
[[the-neuroscience-basis-claim]]
[[learner-variability]]
[[construct-irrelevant-variance]]
[[multiple-means-of-engagement]]
[[multiple-means-of-representation]]
[[multiple-means-of-action-and-expression]]
[[implement-udl-at-school-scale]]

## Composes with

_Reserved for a later composition phase._

## References

1. King-Sears, M. E., Stefanidis, A., Evmenova, A., Rao, K., Mergen, R. L., Owen, L. S.,
   & Strimel, M. M. (2023). Achievement of learners receiving UDL instruction: A
   meta-analysis. *Teaching and Teacher Education*, 122, 103956.
   https://doi.org/10.1016/j.tate.2022.103956
2. Capp, M. J. (2017). The effectiveness of universal design for learning: A
   meta-analysis of literature between 2013 and 2016. *International Journal of Inclusive
   Education*, 21(8), 791–807. https://doi.org/10.1080/13603116.2017.1325074
3. Almeqdad, H., Alodat, A., et al. (2023). The effectiveness of universal design for
   learning: A systematic review of the literature and meta-analysis. *Cogent Education*,
   10, 2218191. https://doi.org/10.1080/2331186X.2023.2218191
4. Ok, M. W., Rao, K., Bryant, B. R., & McDougall, D. (2017). Universal design for
   learning in pre-K to grade 12 classrooms: A systematic review of research.
   *Exceptionality*, 25(2), 116–138. (DOI as staged conflicts with reference 5; see
   Gotchas.)
5. Rao, K., Ok, M. W., & Bryant, B. R. (2014). A review of research on Universal Design
   Educational Models. *Remedial and Special Education*, 35(3), 153–166.
   https://doi.org/10.1177/0741932513518980 (DOI as staged; the same identifier is
   staged for reference 4, so it is reproduced here unverified. See Gotchas.)
6. Bray, A., Flood, M., Reale, J., & Terrenzio, S. (2024). What next for Universal Design
   for Learning? A systematic literature review of technology in UDL implementations at
   second level. *British Journal of Educational Technology*, 55(1), 113–138.
   https://doi.org/10.1111/bjet.13328
7. Transforming higher education: a systematic review of faculty training in UDL and its
   benefits. (2025). *International Journal for Academic Development*.
   https://www.tandfonline.com/doi/full/10.1080/13562517.2025.2465994
8. Boysen, G. A. (2024). A critical analysis of the research evidence behind CAST's
   universal design for learning guidelines. *Policy Futures in Education*.
   https://doi.org/10.1177/14782103241255428
9. Murphy, M. P. A. (2021). Belief Without Evidence? A Policy Research Note on Universal
   Design for Learning. *Policy Futures in Education*, 19(1), 12–27.
   https://eric.ed.gov/?id=EJ1283755
10. Higher Education Opportunity Act, Public Law 110-315; UDL definition at 20 U.S.C.
    § 1003(24). https://www.govinfo.gov/content/pkg/PLAW-110publ315/html/PLAW-110publ315.htm
11. `sources/evidence-meta-analyses.md`: staged extract, fetched 2026-08-07
12. `sources/evidence-critiques.md`: staged extract, fetched 2026-08-07
13. `sources/policy-legal-status.md`: staged extract, fetched 2026-08-07 (statutory text only)
