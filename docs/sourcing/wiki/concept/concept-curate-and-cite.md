---
title: Curate-and-cite as the sourcing model
type: concept
sources:
  - sources/verdict-twelve-host-table.md
  - sources/verdict-wide-sweep.md
  - sources/host-open-middle.md
  - sources/host-mars-map.md
  - sources/host-eric.md
updated: 2026-08-08
---

# Curate-and-cite as the sourcing model

## Summary

Curate-and-cite is the posture a builder holds **before** any host has been fetched. It fixes the
outbound licence first and lets that decide what may come in, rather than assembling material and
asking afterwards what it costs.

Stated in four clauses:

1. **Write original expression from the standard text.** The statement text and its decomposition
   into sub-skills are cleanly licensed and are the spine.
2. **Cite everything you read.** Reading and citing are unconstrained by every source in this
   project's twelve-host sweep, so the restrictive sources stay fully available as evidence.
3. **Quote from a narrow set.** Only hosts carrying a live grant, and only with that grant's
   attribution.
4. **Adapt from a narrower one.** Under this project's Gate 1 ruling the repository ships CC BY 4.0
   and takes **no paraphrase from any ShareAlike source, ever**, which removes the copyleft hosts
   from the adaptable pool by rule rather than by case-by-case judgment.

The inversion that makes this load-bearing, and it is counter-intuitive: **the posture does not
avoid encumbered sources. It reads them.** The instinct to drop a source because its licence is
restrictive is the expensive mistake, because the most valuable thing a restrictive source usually
offers is not its prose. It is its design: item taxonomies, difficulty ladders, distractor-to-error
mappings, rubric grammars, annotated student work. Those are facts about assessment and about
students, not protected expression, and no licence reaches them.

This project made the opposite mistake and recorded it. Its own wide sweep names writing
Illustrative Mathematics off on the strength of one host's ShareAlike term, verbatim:

> I think this is the precise error that caused the earlier sweep to write IM off, and it cost us
> the single most useful source in the field.

## When to reach for it

Reach for it at the start of a build, before the first fetch, and before anyone asks "what can we
copy". The order matters: decide the outbound licence, then read widely, then let the operation
split in [[concept-cite-quote-adapt]] decide per host what may be copied.

Reach for it when someone proposes dropping a source because of its licence. That proposal is
almost always answering the wrong question, and the right question is which of the three operations
is actually needed from that source.

Reach for it when scoping effort. This posture reallocates work rather than removing it, and the
reallocation is the planning fact: less curation of item text, more authoring of item text, and much
less design work than a from-scratch estimate assumes.

Do **not** reach for it to settle what a specific host permits. That is that host's own `source`
page under the evidence floor in this wiki's `CLAUDE.md`.

## How it works

### The outbound licence is decided first

Gate 1 of this wiki records the ruling, and it is the load-bearing constraint on everything
downstream: the repository ships CC BY 4.0, and it takes no paraphrase from any ShareAlike source.
Fixing the outbound licence converts a recurring judgment into a lookup. Once CC BY 4.0 is the
output, a ShareAlike input cannot be paraphrased into it, and that is settled without re-deciding
per source. See [[license-cc-by]] and [[license-sharealike]].

### Reading is free, and that is the whole leverage

The twelve-host record states citation as permitted by every source in its table without exception.
`map.mathshell.org` is `cite_only` under NoDerivatives and its scored and unscored student-work
PDFs remain fully readable. ERIC's licence-silent PDFs are `cite_only` and remain fully readable.
`openmiddle.com` went to all rights reserved and remains fully readable. Nothing about a restrictive
licence restricts reading it.

The wide sweep states the consequence in its own "overstated" list, verbatim:

> Licensing as a blocker. Reading is unconstrained. Item taxonomies, difficulty ladders,
> distractor-to-misconception mappings, rubric grammars and misconception catalogues are **facts
> about assessment and about students**, not copyrightable expression. The constraint bites on the
> *prose* of about five sources. It does not bite on the design work, which is the expensive half.

The MARS evidence file makes the mathematical version of the same point, recorded as that agent's
own reading rather than as host text: original expression of the underlying mathematics is fine
because mathematics is not copyrightable.

### What each operation is actually for

- **Cite**: everything read, including the material that can never be copied. Cite-only sources are
  not a residue; they are the evidence base.
- **Quote**: a short attributed span where the source's exact words carry something a paraphrase
  would lose, such as a standard statement or a mandated notice. Bounded by
  [[k12-density-rules]].
- **Adapt**: reserved for the narrow set of plain-attribution hosts, and used sparingly even there,
  because a package assembled from adapted prose inherits every one of that prose's carve-outs and
  credit lines.
- **Author**: the default for items, prompts and misconception text. Written from the standard text
  and its learning components, informed by everything read.

### The cost, stated honestly

This posture is not free and should never be sold as free. The wide sweep's own estimate, which it
labels as its arithmetic rather than a measurement: direct item reuse supplies roughly **10-15%** of
the bank; item design is essentially solved, eliminating roughly **40%** of the authoring cost;
original expression is still forced for roughly **85-90%** of items; total saving on the item phase
is put at **35-45%**. That document fetched nothing and is an adjudication of eight of this
project's own sweep reports, so treat those figures as this project's planning estimate, not as a
measured result.

## In practice

**Open Middle, after its grant went away.** The site-wide CC BY-NC-SA 4.0 footer was present in the
Wayback capture of 2026-02-16 and absent in the capture of 2026-03-03. The verifying agent's own
bottom line for this model, as recorded: citing is unaffected because citation is not
redistribution and all rights reserved does not restrict it; what was lost is the fallback that
would have permitted reproduction and adaptation; the instruction is to link and cite and write our
own prompts. Under curate-and-cite the loss is real but bounded, because nothing in the plan
depended on copying that text. Under a copy-first plan the same event would have invalidated
finished work. See [[source-open-middle]] and [[license-withdrawn-grants]].

**MARS, which is cite-only and still one of the best sources here.** The host publishes four
different regimes and says so itself, verbatim: "Precise terms vary between materials." NoDerivatives
is stated three ways, so paraphrase-and-republish is unlicensed. What remains available is the part
that matters most: each summative task ships with a rubric and with both unscored and scored
annotated student work, which the verifying agent calls a genuinely unusual misconceptions asset.
That asset is read, cited and designed from, never reproduced. See [[source-mars-map]].

**ERIC, where the modal case is silence.** Of 7 PDFs actually opened by the verifying agent, 1 was
CC BY, 2 were explicitly restrictive and 4 were completely silent, and under the Berne default
silence means all rights reserved rather than open. One of the restrictive papers carries an express
carve-out for linking. Curate-and-cite absorbs this without a decision: all 7 are readable, all 7 are
citable, and only the CC BY one enters the quotable set. See [[source-eric]] and
[[license-unmarked-silence]].

**The standards spine.** Statement text and the learning-component decomposition are the one layer
that is both abundant and cleanly licensed, which is why the model puts original expression there
rather than in adapted lesson prose. That layer carries its own obligations, including a second
non-Creative-Commons notice for CCSS text, and its own resolution mechanics. See
[[concept-standard-placement-vs-code]] and [[source-corestandards-nga-ccsso]].

## Gotchas & constraints

**1. The posture is not a licence finding and does not substitute for one.** Every host still needs
a fetched, pasted, dated footer before any verdict attaches. Curate-and-cite decides what you do
with the verdict, not what the verdict is.

**2. "Cite everything" has mechanical constraints that are not licence constraints.** Cite the MARS
web page rather than the PDF it serves, because the page carries the grant and the file says all
rights reserved. Cite a Wayback URL for `mathmistakes.org` and for `engageny.org`, because the live
hosts serve a PHP fatal error and an expired certificate respectively. Cite `http://` for
`mathematicsvisionproject.org`, whose https fails host-wide.

**3. Original expression is not a loophole around ShareAlike.** Writing from the standard text with
a source cited as inspiration avoids the trigger. Close paraphrase of a specific task does not, and
the difference is one of degree that a writer can talk themselves across. See
[[trap-sharealike-contaminates-by-paraphrase]].

**4. The bimodal reading of the corpus is half retired and must be carried with its correction.**
The twelve-host record's headline was that prose is abundant and cleanly licensed while assessment
items are thin and encumbered. The first half stands. The second half is superseded: the wide sweep
calls the "no host supplies a clean adaptable bank" claim false twice over, and reframes the problem
as a licensing conflation rather than a scarcity. Do not quote the older half without the newer.

**5. Nothing here is a fair-use position.** Short attributed quotation from a cite-only source would
rest on fair use. No agent in this project made that judgment and this wiki does not make it.

**6. The posture assumes nothing is sold.** NonCommercial riders are satisfied while nothing is
monetised and become live constraints the moment that changes. The sources that are usable only
because of that assumption should be identifiable in the source table rather than discovered later.

**7. Reading widely has its own limits, and they are not legal ones.** Two hosts in this corpus bar
framing, one bars automated tools that place excessive load on servers, and several bot-block
default user agents. A citation practice must respect those independently of any licence.

## Related

- [[concept-cite-quote-adapt]] is the mechanics this posture is built out of: this page chooses
  which operation to default to, that page defines what each one is.
- [[license-cc-by]] holds both the grant most of the quotable set carries and the obligation this
  repository takes on by shipping under it. [[license-sharealike]] holds the rider the Gate 1 ruling
  excludes from the adaptable pool, [[license-unmarked-silence]] the modal case on the research
  literature, and [[license-withdrawn-grants]] the reason a plan must not depend on a grant staying
  in place.
- [[concept-chain-of-title]] and [[concept-third-party-carve-out]] are the two ways a source that
  passes the licence check still fails the reuse check.
- [[source-mars-map]], [[source-eric]] and [[source-open-middle]] are the three cite-only hosts
  whose value this posture preserves.
- [[evidence-c7-store-gap-not-corpus-gap]] measures the one gap on this unit that is real and local
  rather than a sampling artifact.
- [[k12-density-rules]] bounds how much quoted material a shipped artifact may carry.

## Composes with

- [[practice-build-a-source-table]] is the first step of the model in procedure form, and it is what
  turns "read everything" into a dated, verdicted record.
- [[practice-cite-without-redistributing]] is the default operation executed, including the
  page-versus-file and live-versus-archive choices.
- [[practice-ground-a-lesson-end-to-end]] is where original expression is written from the standard
  spine rather than adapted from lesson prose.

## References

This wiki's own ruling record: the project's governing ruling, ruled 2026-08-08. The
repository ships CC BY 4.0 and takes no paraphrase from any ShareAlike source, ever.

Host evidence, all primary, fetched by this project 2026-08-08 and staged 2026-08-08.
`sources/host-mars-map.md`: section 3a, the homepage sidebox including "Precise terms vary between
materials"; section 5, riders 1 and 6; section 6, the four-file shape of each summative task;
section 7, the agent's own bottom line for this model. `sources/host-open-middle.md`: section 5, the
dated Wayback footer table pinning the removal window; section 9, the agent's own bottom line for
this model. `sources/host-eric.md`: section 2, the ERIC copyright policy; section 4, the 7-PDF tally
of 1 CC BY, 2 restrictive and 4 silent; section 7, the access-versus-rights distinction.

This project's own adjudications, cited as this project's measurement and not as any outside party's
statement. `sources/verdict-twelve-host-table.md`, reference: section 2's closing paragraph, the
safe default this page states; section 5, the usable set, carried with its inline retirement
markers. `sources/verdict-wide-sweep.md`, reference: the "overstated" list on licensing as a
blocker; the savings estimate and its stated arithmetic basis; the record of the write-IM-off error.
That document states that its adjudicating agent fetched nothing, so every claim in it is a
report-of-a-report and it does not meet this wiki's evidence floor for a licence finding on its own.
