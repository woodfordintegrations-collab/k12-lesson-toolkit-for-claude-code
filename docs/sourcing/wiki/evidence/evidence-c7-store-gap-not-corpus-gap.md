---
title: The C.7 scaffold gap is real in the store and was an artefact in the corpus
type: evidence
sources:
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - sources/verdict-wide-sweep.md
  - sources/verdict-twelve-host-table.md
  - sources/host-jmap.md
  - sources/host-open-middle.md
updated: 2026-08-08
---

# The C.7 scaffold gap is real in the store and was an artefact in the corpus

## Summary

This page holds both halves of a claim that was half right, because **this project asserted the
wrong half in writing and the reason it did is the durable part.**

- **The store half survives.** Measured against `data/k12-lesson-toolkit.db`, the richest placement for
  `HSG-SRT.C.7` carries **one** learning component, against 7 for B.4, 6 for B.5, 3 for C.6 and 8
  for C.8. The standard's own text is "Explain and use the relationship between the sine and
  cosine of complementary angles". The single component covers the *use* half. The verb that has
  to be adjudicated, **Explain**, has no decomposition behind it at all.
- **The corpus half was inverted.** The earlier conclusion, "C.7 is the weakest standard across
  the entire corpus", was retired on 2026-08-08 against **37 distinct C.7 sources, 24 of them
  usable treatments**, six of which are complete teachable lessons.

The error this page exists to prevent is not the belief that C.7 is scarce. It is the move that
produced that belief: **generalising from a curated-host census to the world.** Twelve OER hosts
were swept carefully and correctly, and the generalisation from them was wrong, because the
material lives in state assessment archives, a national syllabus, a federal curriculum module and
the research literature, none of which is an OER host. The second half of the diagnosis is a
search-term failure: the topic does not index under "trig identities".

A page reproducing the twelve-host coverage row without this correction repeats the error. A page
reproducing the correction without the store measurement loses a real, local finding that is still
true.

## When to reach for it

Reach for it before quoting the twelve-host table's coverage row or its closing sentence. That
sentence is the single retired claim a page in this wiki is most likely to cite by accident.

Reach for it before concluding that any standard is under-resourced. The method that produced the
false conclusion is reusable, so the correction has to be too.

Reach for it before budgeting authoring cost for C.7, and before treating a learning-component
count as a statement about how well a standard is supported anywhere outside this store.

Do **not** reach for it for a licence verdict on any named source. The wider sweep that supplies
the 37-source count fetched nothing, and its licence rows do not meet this wiki's evidence floor
on their own. Verdicts live on the `source` pages.

## The claim

Four claims. The first two survive; the third is a retirement; the fourth is why.

**C1. The store's decomposition of C.7 is one component.** For the five unit codes, the richest
placement carries: `HSG-SRT.B.4` 7, `HSG-SRT.B.5` 6, `HSG-SRT.C.6` 3, `HSG-SRT.C.7` 1,
`HSG-SRT.C.8` 8. Each of the five codes resolves to four placements, and every one of the five has
at least one placement carrying zero components. Falsifier: re-run the per-placement count against
`data/k12-lesson-toolkit.db` and get different numbers.

**C2. The one component covers "use" and not "Explain".** The standard reads "Explain and use the
relationship between the sine and cosine of complementary angles"; the store's single C.7 learning
component addresses the use half. Falsifier: a second C.7 component, or a component whose
description carries the explanatory obligation.

**C3. The scarcity claim is retired.** "C.7 has near-zero coverage" and "C.7 is the weakest
standard across the entire corpus" are retired against 37 distinct C.7 sources, 24 of them usable
treatments, where usable is defined by the adjudicating document as "something you could teach or
assess from, as opposed to a syllabus line or a gated title". Falsifier: a recount of those 37
that cannot reproduce them.

**C4. The earlier finding was an artefact of the search surface.** Falsifier: showing that a
twelve-OER-host frame, searched on the terms actually used, could have reached the state
assessment archives, NESA, EngageNY, first-edition OpenStax and the research literature.

**What these claims do not say.** C1 and C2 are measurements of a local SQLite store built from a
filtered Learning Commons export. They are not statements about C.7 as a standard, and not
statements about what Achievement Network authored. C3's counts come from a document whose author
states plainly "I fetched nothing", so they are this project's own adjudication of its own reports,
not a verified census. And C3 does **not** retire the per-host measurements that fed it: accessim's
one C.7 lesson, MARS's zero C.7 Classroom Challenges and Open Middle's zero C.7 problems are
correct measurements *of those hosts* and remain citable as such.

## What the evidence shows

### The store measurement, per placement

Measured in session against `data/k12-lesson-toolkit.db` opened read-only, each row ordered by
`case_uuid`:

| Code | Placements | Component count per placement, with jurisdiction |
|---|---|---|
| `HSG-SRT.B.4` | 4 | California 0, California 0, California 7, Multi-State 7 |
| `HSG-SRT.B.5` | 4 | California 6, California 0, Multi-State 6, California 6 |
| `HSG-SRT.C.6` | 4 | Multi-State 3, California 3, California 0, California 3 |
| `HSG-SRT.C.7` | 4 | Multi-State 1, California 0, California 1, California 0 |
| `HSG-SRT.C.8` | 4 | California 8, California 0, Multi-State 8, California 8 |

Two facts have to be read off that table together. C.7 is the thinnest code in the unit, and
**every** code has a zero placement, so a hand-picked or first-returned row lands on nothing with
non-trivial probability and the raw ordering is not stable. That is why the count is a property of
a resolved placement, not of a code: [[concept-standard-placement-vs-code]].

### The standard's own text, and where the gap is

Standard text as printed on the JMAP page for this code, verbatim:

> Explain and use the relationship between the sine and cosine of complementary angles

The framing that survives is recorded in this project's own adjudication, verbatim:

> the k12-lesson-toolkit store decomposes C.7 into a single learning component covering "use" while the
> standard says "Explain and use", so the "Explain" verb has no scaffold.

The build consequence was already ruled before this page existed: **author C.7, do not curate it.**
That ruling stands on the store measurement, which is local and unaffected by anything the wider
sweep found.

### The retirement, verbatim

From this project's own adjudication of eight sweep reports, dated 2026-08-08:

> **Claim retired.** An earlier twelve-host OER sweep concluded HSG-SRT.C.7 has near-zero
> coverage. A wider sweep across eight angles (US and international released assessments,
> openly licensed textbooks, interactive/visual sources, teacher-practitioner writing,
> misconception research, a dedicated C.7 dive, and applied-trigonometry sources) located
> **37 distinct C.7 sources, 24 of them usable treatments**. The earlier finding was an
> artefact of the search surface: C.7 does not live on OER *hosts*. It lives in
> (a) state released-assessment archives, (b) two open curricula (Illustrative Mathematics
> and EngageNY/Eureka), (c) first-edition OpenStax, (d) one national syllabus (NSW/NESA),
> and (e) the research literature. None of those is an "OER host", and searching for
> "trig identities" misses it entirely — the topic indexes under *cofunction* and
> *complementary angles*.

And the scope diagnosis in its own words:

> "**"Twelve curated OER hosts" is a sampling frame, not the internet.** Every C.7 source that
> matters sits outside it: state assessment archives, a national syllabus (NSW/NESA), a
> federal curriculum module (EngageNY), a peer-reviewed literature, and one
> commercial-publisher-hosted open curriculum (Kendall Hunt). None is an "OER host"."

### What the 37 located sources break down into

| Tier | n |
|---|---|
| Complete teachable lessons, read in full | 6 |
| Textbook and reference derivations | 8 |
| Interactive and figure treatments | 3 |
| Answer-keyed item banks | 8 |
| Live released assessment items opened | 7 |
| Curriculum or syllabus naming C.7 as its own object | 5 |

Licence-compatible with a CC BY 4.0 repository, as that document records them: IM Geometry Unit 4
Lesson 8 and Unit 4 Lesson 4 activity 4.3 on `im.kendallhunt.com`; OpenStax Algebra and
Trigonometry **1e** §7.2 and Precalculus **1e** §5.4; then two with caveats, NZ Maths (CC BY 3.0 NZ,
but the licence statement came from a third party's index card and not from the resource) and
Arhin and Hokor 2021. See [[source-im-kendall-hunt]], [[source-openstax]] and
[[evidence-misconception-research-licensing]].

### The standard is live, with numbers

Decoding JMAP's REF codes across the first 17 answers of its Cofunctions 1 worksheet yields 17
distinct NY Regents administrations, range stated as June 2015 to January 2026, glossed as roughly
one C.7 item per sitting for a decade. One agent cross-validated REF `012304geo` against the
primary NYSED PDF.

Difficulty, which no other source in the sweep publishes: Florida BEST 2025 reports **40%** correct
on a cofunction item, and **36%** and **31%** on its other two trig items, against a whole-test
range of roughly **21-81%**.

### Where C.7 genuinely is absent, which is the useful part

The absence is real and it is by specification, not oversight. AQA GCSE 8300 rows G19 to G22
contain no complementary-angle content at all; ACARA v9 Years 9 and 10, Ontario Grades 9 and 10,
and Singapore E-Math are the same. Only NSW names it. In the current NCERT Class 10 Chapter 8 an
agent grepped the Reprint 2026-27 PDF and found the word "complementary" **zero** times; the
section was cut in the 2023 rationalisation.

That absence is why UK resources teach the content unknowingly as a memory trick, and why the
adjudication calls it the hook a C.7 lesson exists to fix. See [[source-nesa-nsw]].

### The item-bank corollary, retired with it

The same twelve-host table concluded, verbatim, that "there is **no host in this table that
supplies a clean, adaptable bank of assessment items** for all five standards". The wider sweep
calls that false twice over: JMAP supplies a standard-by-standard, answer-keyed,
provenance-tagged bank across all five standards, cite-only but complete as a blueprint including
relative weights; and IM/Kendall Hunt supplies openly licensed practice sets, cool-down statements
and activity problems across Units 3 and 4.

The correction is partial, and the weakened form is what to carry: direct item reuse is still put
at only about **10-15%** of the bank, so the advice to budget for authoring survives. What changes
is where the saving is. It is in item *design*, because item taxonomies, difficulty ladders and
distractor-to-misconception mappings are facts about assessment rather than copyrightable
expression, and reading them needs no licence. See [[source-jmap]] and [[k12-assessment-gap]].

## Gotchas & constraints

**1. The sentence most likely to be cited by accident.** The twelve-host table's closing sentence
under its coverage table reads, verbatim: "**C.7 is the weakest standard across the entire
corpus**: one IM lesson, one accessim lesson, two IM tasks, zero MARS lessons, zero Open Middle
problems, zero misconception sources. Plan to author C.7 material rather than curate it." The
census inside it is correct **of those twelve hosts**. The generalisation is retired. If you quote
it, carry the correction in the same breath, and note that its final instruction still holds for a
different reason: the store's scaffold gap, not corpus scarcity.

**2. Do not read a component count as a coverage fact.** C1 measures what Achievement Network
authored against the placements in one filtered export, as loaded into one local store. It is a
statement about a decomposition artifact. It is not a statement about how much teachable material
exists for the standard, and the two were conflated once already.

**3. C.7's tool output is complete, which makes it look more authoritative.**
The MCP slices learning components at five with no flag. B.4 (7), B.5 (6) and C.8 (8) are silently
truncated; C.6 (3) and C.7 (1) are not. So the thinnest code is one where the tool response
happens to be the whole truth, and the richest codes are the ones where it is not. A reader
comparing tool outputs across codes is comparing a complete answer with three truncated ones. See
[[trap-learning-components-truncated-at-five]].

**4. The 37 and the 24 do not meet this wiki's evidence floor as licence facts.** The adjudicating
document states in its own opening, verbatim: "I fetched nothing. Every claim below traces to a
report". Its reuse-terms table carries no HTTP status and no pasted footer for any row. Three rows
name a verification method. Cite the counts as this project's sweep record. Take licence verdicts
from the `source` pages, which carry pasted footers with URLs and fetch dates.

**5. An internal discrepancy in the JMAP figures, preserved unresolved.** The body of the
adjudication says 17 administrations, June 2015 to January 2026. Its own prescribed page text says
45 items spanning 22 administrations, June 2015 to June 2026. Both are reproduced as written in the
staged extract. Neither is computed or reconciled here. A page asserting either must say which
passage it took it from, or re-decode the worksheet.

**6. Two naming defects in the prescribing document, recorded not corrected.** It specifies content
for a page it calls `evidence-c7-coverage-floor`, which is not this page's approved slug, and it
forward-references `evidence-b4-proof-gap`, which is not a row in `INVENTORY.md` at all. The
finding that page would have held is real and has nowhere to live: no current textbook opened
anywhere in that sweep proves Pythagoras via similarity in the lesson that introduces the theorem.
That is called the real content gap, and it sits under B.4, not C.7.

**7. Where C.7 material is cite-only, it is decisive anyway.** EngageNY Geometry Module 2 Lesson 27
is named the most complete single teacher document and is CC BY-NC-SA 3.0; JMAP is a compilation
copyright, all rights reserved; Ohio, Florida and Louisiana have no located grant. All of them are
readable, citable and usable as design evidence without any licence at all. See
[[concept-cite-quote-adapt]] and [[source-engageny-nysed]].

**8. Search terms are part of the method.** The topic indexes under *cofunction* and *complementary
angles*. A sweep that searches "trig identities" returns a true negative about its own query and a
false negative about the world.

## Related

- [[trap-learning-components-truncated-at-five]] is why a count taken from the tool is not the
  store's count, and why C.7's completeness is a coincidence rather than a signal.
- [[concept-standard-placement-vs-code]] is why the count of C.7's components is a question
  with a method, and why every one of the five codes has a zero placement.
- [[evidence-store-ingest-boundary]] is what did and did not cross into the store that C1 measures.
- [[evidence-kg-coverage-and-gaps]] is the upstream census, including the absent misconception
  layer that made the C.7 evidence question feel starker than it was.
- [[source-im-kendall-hunt]] holds the one CC BY 4.0 host carrying a complete C.7 lesson, and is
  the source the earlier framing cost this project.
- [[source-jmap]] is the cite-only item bank whose REF provenance supplies the decade of
  administrations quoted above.
- [[source-openstax]] holds the edition trap: 1e is CC BY 4.0, every 2e maths title checked is
  CC BY-NC-SA 4.0.
- [[source-nesa-nsw]] is the one national syllabus that names this content as its own object.
- [[source-open-middle]] and [[source-mars-map]] hold the per-host C.7 zeroes that remain correct
  measurements of those hosts.
- [[concept-curate-and-cite]] is the posture this page's item-bank corollary was merged out of.
- [[k12-assessment-gap]] is where the authoring-versus-curation budget lands in the contract.

## Composes with

- [[practice-build-a-source-table]] is the procedure whose sampling frame produced the retired
  claim, and this page is the worked instance of why the frame has to be recorded alongside the
  finding.

## References

Local artifacts measured by this project, read-only, at staging on 2026-08-07:

- `data/k12-lesson-toolkit.db`. The per-placement
  learning-component counts for the five unit codes, the four-placements-per-code finding, and the
  zero placement on every code.
- `src/k12-lesson-toolkit/mcp/server.py`.
  `MAX_LEARNING_COMPONENTS = 5` declared line 48 and applied at the slice on line 213, which is why
  B.4 and C.8 truncate and C.7 does not.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §3.6 the per-placement component table
  reproduced above; §4.1 to §4.4 the cap, its application and how often it bites.
- `sources/verdict-wide-sweep.md`, reference. §1 the retirement and the byte-exact replacement
  text; the tier table; the JMAP REF decoding with its preserved internal discrepancy; the Florida
  difficulty figures; §2 the item-bank correction and the savings estimate; §6 items 1, 2, 5, 8, 9
  and 18; the staging notes recording the slug mismatches.
- `sources/verdict-twelve-host-table.md`, reference. §5 the standard-by-standard coverage table,
  its closing sentence, and the inline retirement markers that point back to the wide sweep.
- `sources/host-jmap.md`, primary. §2a, the C.7 standard text as printed on the host page and the
  worksheet inventory, including that C.7 is the only one of the five with no PRACTICE WORKSHEETS
  group.
- `sources/host-open-middle.md`, primary. The C.7 zero, confirmed on the exactly-matching category.

This project's own measurement and adjudication, cited as this project's and not as any outside
party's statement: the store counts, the twelve-host census, the wide-sweep counts, and the
retirement itself.
