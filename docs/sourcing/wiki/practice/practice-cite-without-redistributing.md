---
title: Cite without redistributing
type: practice
sources:
  - sources/host-eric.md
  - sources/host-mars-map.md
  - sources/host-open-middle.md
  - sources/host-math-mistakes.md
  - sources/verdict-twelve-host-table.md
  - sources/k12-grounding-and-render.md
updated: 2026-08-08
---

# Cite without redistributing

## Summary

How to get full value out of a source you may not reproduce. A `cite_only` verdict is not a
rejection: it closes one operation and leaves two open, and the two it leaves open carry most of what
a build actually needs.

The mistake this page stops runs in both directions, and this project has made both.

**Dropping a cite-only source as unusable.** Citing is unconstrained by every source in this corpus.
Naming a source, linking it, stating what standard it addresses and describing in your own words what
it does needs no licence at all, because facts, titles, URLs and standards alignments are not
protected expression. ShareAlike, NonCommercial and NoDerivatives do not touch citation.

**Reading availability as permission.** ERIC's own copyright policy says, verbatim:

> ERIC does not retain copyright to the works indexed in the database and cannot grant permission
> to use indexed works under copyright protection.

"Full text is available" is an access fact. The rights fact lives inside the individual PDF, and of
seven sampled there, four carried no notice at all.

The operative split is three ways, not two:

| Operation | What it is | What constrains it here |
|---|---|---|
| Cite | name, link, state the alignment, describe in your own words | nothing, on every source in this corpus |
| Quote | reproduce exact expression, in quotation marks, with attribution | needs a live grant; blocked where the source is silent, all-rights-reserved or NoDerivatives |
| Paraphrase and republish | rewrite the material and ship it | the operation the licences actually bite on |

## When to reach for it

Reach for this page the moment a source table row reads `cite_only` or `do_not_use`, or carries a
NoDerivatives, all-rights-reserved or licence-silent verdict, and the question becomes what is left.

Reach for it when a source is about to be dropped from a build because of its licence. Usually the
thing being lost is available under citation and the drop is unnecessary.

Reach for it before quoting from a host whose verdict is not `quote_and_adapt`. The boundary between
quotation and adaptation is where this goes wrong, and it is not a matter of word count.

Do not reach for this page for the verdict itself: producing it is
[[practice-build-a-source-table]]. Do not reach for it for the shipped credit line, which is
[[practice-assemble-an-attribution-block]].

## How it works

**Citation is not a licensed act.** This project's verdict key states it plainly: no copyright licence
is required to cite, which is why an all-rights-reserved host, a NoDerivatives host, a
withdrawn-grant host and a set of licence-silent research PDFs all remain fully usable in a
curate-and-cite build. One source in the corpus says so about itself. From
`files.eric.ed.gov/fulltext/EJ1064122.pdf`, an otherwise all-rights-reserved paper, verbatim:

> Using the hyperlinks to the article is not considered a violation of copyright.

**Quoting is a use of a work, not an adaptation of it.** A quotation set inside your own prose with
attribution does not trigger ShareAlike, because it is not a derivative, and it does not trigger
NoDerivatives, since the fragment is unmodified. What blocks quotation is the absence of a grant, not
the presence of a rider.

**Paraphrase-and-republish is what gets people into trouble, and it is not about wording.** A close
paraphrase following a specific task's structure, numbers and pedagogical move is an adaptation
however different the sentences. That is the operation a curriculum repository performs, and it is
the one NoDerivatives forbids outright and ShareAlike permits only at the price of relicensing the
file it lands in. See [[concept-cite-quote-adapt]].

**Silence resolves to all rights reserved.** A resource with no notice is not permissively
unlicensed. Under the Berne default it is reserved, and this project's ERIC sample makes silence the
modal case rather than the exception. See [[license-unmarked-silence]].

## In practice

### Step 1. Fix which operation you need before you look at the licence

Most licence anxiety here comes from asking "may I use this source" instead of "which of the three
operations do I need from it". The three have different answers on the same host, and on some hosts
the answer differs per file. If what you need is the alignment, the sequencing, the fact that a
treatment exists, or an understanding that will inform your own original writing, you need citation,
and the licence question closes before it opens.

### Step 2. For a NoDerivatives source, quote nothing and cite the page

NoDerivatives is stated three separate ways on the one ND host in this corpus, all verbatim from that
host: "reproduced as-is", "copied and distributed, unmodified", "reproduced and distributed, without
modification". Every ND grant there also appends "All other rights reserved". What that leaves open
is unmodified redistribution of the whole artifact, non-commercially, with attribution. What it
forecloses is exactly the paraphrase-and-republish operation a build performs.

**Trap here: cite the page, not the PDF.** On that host the web page grants CC BY-NC-ND 3.0 while the
file it serves says, verbatim, "Copyright © 2011 by Mathematics Assessment Resource Service. All
rights reserved.", and the rubric file for the same task carries no notice at all. Anyone receiving
the PDF alone sees pure all-rights-reserved. The page carries the grant, so the page is what gets
cited and archived with its fetch date.

**Second trap: one corner of that host is ShareAlike, not NoDerivatives.** The PD Modules page links
`by-nc-sa/3.0/`, and its visible text carries no version number and neither the word "unmodified" nor
"all other rights reserved". That is a materially different and more permissive grant on the same
domain. It permits derivatives and attaches ShareAlike to them, so any close paraphrase from it must
be quarantined rather than mixed into repository prose. See
[[trap-sharealike-contaminates-by-paraphrase]].

**Third trap: a fourth regime on the same host has no statement at all.** The TRU Math pages return
zero hits for creativecommons, license, reproduce or rights reserved, so only the footer's bare
copyright assertion applies and the material resolves to all rights reserved. One host, four regimes,
and the host says so itself: "Precise terms vary between materials."

### Step 3. For an index or aggregator, go to the artifact, because the index grants nothing

An index hosting a file under permission cannot pass that permission on. Measured on ERIC: there is no
licence or rights field in the metadata at all. A full API field dump of one record returns exactly
author, description, id, issn, language, peerreviewed, publicationdateyear, publicationtype,
publisher, subject and title. Five record pages were fetched and the only occurrence of "copyright"
on any of them is the global footer nav link. So the licence is readable only from inside the PDF,
and the measured spread of what is inside is **1 CC BY, 2 explicitly restrictive, 4 completely silent,
of seven opened.**

**Trap here: "silent" means silent in the copy you opened.** This project's record says so directly: a
notice rendered as an image, or living on the journal's site rather than in the file, would have been
missed, and several of those journals may well be CC BY at source. Closing it means checking each
journal's own policy page. Until then the row says silent, not restrictive.

**Second trap: a version-less CC label is not a version.** One CC BY paper in that sample names "the
Creative Commons Attribution License" with no version number and no creativecommons.org URL anywhere
in the file. The version was pinned only from the journal's own open-access policy page, which links
`by/4.0/`. Do not infer 4.0 from the word "Attribution", and do not silently upgrade a 3.0 label. See
[[trap-access-is-not-a-rights-fact]].

### Step 4. For an all-rights-reserved source, cite the way the site itself credits

An all-rights-reserved host restricts nothing about citation. What it changes is the shape of the
credit. Measured on the one ARR host here: every problem carries a named individual contributor
byline while the site asserts a blanket all-rights-reserved footer, and `/submit/` presents no
copyright-assignment or licensing language, so the upstream rights chain is undocumented. The
practical consequence is that a citation carries both the contributor name and the site, matching the
site's own convention, rather than crediting the site alone.

**Trap here: a sanctioned embed is a use pathway, not a copyright licence.** That host documents an
official "Use this problem" iframe for Canvas, Google Classroom, Teams and websites. Embedding serves
content from their domain under their control. It grants no right to copy problem text into a
repository, and an iframe is a third-party dependency rather than an asset you own.

**Second trap: the trademark survives the copyright question entirely.** The footer says, verbatim,
"Open Middle is the registered trademark of Glenrock Consulting, LLC." Nominative reference in a
citation is ordinary and unaffected. Branding your own materials with the mark is a separate matter
and no copyright analysis covers it.

### Step 5. For a dead or blocked host, cite the archive, and say so in the citation

Where the live host serves nothing, a bare link is worse than no link: it lands the reader on a stack
trace. Two hosts here need an archive URL. One returns HTTP 200 with a PHP fatal error as the entire
body on every path probed, so zero licence text and zero content is obtainable live. The other has an
expired certificate on `www` and an NXDOMAIN apex. The form is the live URL plus an "archived at"
Wayback URL with its timestamp, or the Wayback URL alone.

**Trap here: the grant on an archived page is dated, and its date is the point.** The CC BY 3.0
Unported notice on the dead host was found unchanged on root captures dated 20140517212051,
20160524142902, 20180521035129, 20200518014659, 20221207024233 and 20260220051333. That twelve-year
stability is what establishes the grant was in force when the material you are citing was published.
A single snapshot proves only that the notice existed once.

**Second trap: on that host the licence is not the binding constraint.** CC BY 3.0 clears citation,
quotation and adaptation with no rider. What blocks reproduction is two things outside licensing: the
corpus is teacher-submitted photographs over which the owner asserts a blanket grant with no
submission agreement anywhere on the site, and every post is a photograph of a minor's handwritten
work. A valid grant resolves neither. Cite the posts; do not reproduce the images.

### Step 6. Extract what does not require a grant, deliberately and by name

This is the step that makes a cite-only row worth having.

- **The standards alignment.** A host's own published crosswalk is a fact about the host, citable in
  full. One host here publishes its CCSSM crosswalk, and an honest citation of it also records this
  project's finding that part of that mapping is thin and partly spurious, since it lists an item
  outside the cluster.
- **The item design.** A cite-only bank can be a complete blueprint. This project's wide sweep records
  one host as supplying a standard-by-standard, answer-keyed, provenance-tagged bank across all five
  target standards, cite-only, including relative weights. The saving is in item design rather than
  item text. See [[source-jmap]].
- **The diagnostic reading.** Misconception corpora and annotated student work inform original writing
  without any of their expression entering the repository. One host's scored and unscored
  student-work PDFs are recorded here as a genuinely unusual asset, usable as a design reference.
- **The problem structure.** A constraint-task format is an idea, not protected expression.
- **The negative result.** "This host has zero items on this standard" is a measured fact that costs
  nothing to publish and saves the next person the search.

### Step 7. Write the bibliographic form, with no licence line

A cite-only entry carries no licence statement, because there is no grant to recite. Four paste-ready
forms are recorded in this project's attribution block and all four are bare bibliography: title,
publisher, URL, accessed date. Adding "licensed under" to a cite-only entry asserts a grant that does
not exist.

Where the host is dead or blocked, the archived URL goes in the entry. Where the host publishes no
canonical attribution string, say so rather than inventing one: two hosts here publish none, and this
project's strings for them are recorded as constructed or modelled on the host's own footer, not as
the host's mandated form.

## Gotchas & constraints

**1. The line between quotation and adaptation is not a word count.** A short passage reproduced
inside your own prose is a quotation. A rewritten task that keeps the structure, the numbers and the
pedagogical move is an adaptation even with no shared sentences. Whether the result is a version of
their work is the test.

**2. Short attributed quotation from a NoDerivatives source rests on fair use, and no agent in this
project made that call.** The conservative reading is that ND permits unmodified redistribution and
not extraction, so the verdict stands at `cite_only`. Fair use is a legal judgment, not a fetched
fact, and this project's record explicitly declines to make it.

**3. A grant cannot convey rights the grantor does not hold.** Four tasks in one ShareAlike bank carry
the site's blanket footer while their own commentary states they were adapted from competition
problems, and the host says nothing about the upstream position. Those four are cite-only regardless
of the host verdict. See [[concept-chain-of-title]].

**4. Do not launder a source through an aggregator.** Every Coherence Map example problem for the five
target standards is attributed "Provided by Illustrative Mathematics" and links off-site, while the
aggregator's own presentation carries no licence notice whatsoever, so a user relying on that
presentation could never learn a ShareAlike obligation exists. Source and clear the material at the
rights-holder, not at the pointer. See [[concept-third-party-carve-out]].

**5. The constraint reaches chat, not only documents.** The lesson-planning skill mandates a
terminology sweep before drafting whose scope is explicit: a teacher who has not confirmed a given
curriculum "must not receive IM-specific terminology in the lesson or in chat". Citation discipline
that stops at the file boundary is incomplete.

**6. NonCommercial is dormant, not absent.** An NC rider is irrelevant while nothing is sold and
permanent if a repository ever monetises. It is not a reason to drop a source, and it is a reason to
keep NC-derived and non-NC material in separate files. See [[license-noncommercial]].

**7. A cite-only verdict can become a do-not-use one, and the trigger is upstream rather than
licensing.** Student privacy on photographs of minors' work, and an undocumented chain of title on
third-party submissions, both sit outside the licence and both survive a permissive grant intact.

**8. What is unverified here.** Whether a public-domain dedication survives the withdrawal of the page
that published it is recorded in this project's own account as the single most consequential open
question in the corpus, and it goes to counsel before anyone relies on it. Whether an
all-rights-reserved footer binds contributor-authored problems given no visible assignment instrument
is likewise unresolved. Neither is answerable by fetching, and neither is answered here.

## Related

- [[concept-cite-quote-adapt]] is the three-operation split this page applies.
- [[concept-curate-and-cite]] is the sourcing posture that makes a cite-only row worth keeping.
- [[license-noderivatives]] is the rider behind step 2 and why paraphrase is foreclosed there.
- [[license-unmarked-silence]] is why a resource with no notice is reserved rather than open.
- [[license-all-rights-reserved]] is step 4's regime, positively asserted.
- [[license-sharealike]] and [[trap-sharealike-contaminates-by-paraphrase]] cover the one corner of an
  otherwise-ND host that needs quarantine.
- [[trap-access-is-not-a-rights-fact]] is step 3's core failure: availability read as permission.
- [[source-eric]] is the index that grants nothing and says so.
- [[source-mars-map]] is the four-regime host behind step 2, including the page-versus-file mismatch.
- [[source-open-middle]] is step 4's host, its embed pathway and its trademark.
- [[source-math-mistakes]] is step 5's dead host, where the licence is not the binding constraint.
- [[source-jmap]] is the cite-only bank whose value is its blueprint rather than its text.

## Composes with

- [[practice-build-a-source-table]] produces the verdict this page consumes, and its unverified column
  decides whether a row is `cite_only` by measurement or by default.
- [[practice-assemble-an-attribution-block]] takes step 7's bibliographic forms into the shipped file,
  and is where a cite-only entry must be kept free of a licence line.
- [[practice-format-an-assessment-artifact]] is where step 6's design-precedent extraction lands:
  items authored original from standard text, with cite-only banks used as blueprints.

## References

Staged extracts in this wiki, staged 2026-08-08 unless noted:

- `sources/host-eric.md`, primary. §2 the site-level copyright policy verbatim; §3 the API field dump
  and the record-page check; §4 the seven per-resource samples with the 1 CC BY, 2 restrictive, 4
  silent tally and the hyperlink carve-out; §5.1 the version pinned at the journal rather than in the
  file; §5.2 the author accepted manuscript with no grant; §7 the access-versus-rights bottom line.
- `sources/host-mars-map.md`, primary. §3a to §3h the four regimes verbatim, including the PD Modules
  ShareAlike exception and the TRU Math silence; §4b the summative-task PDF's all-rights-reserved
  footer against its page's CC grant; §5 the riders; §6 the host's own CCSSM crosswalk; §7 the
  analysis attributed to this project rather than to the host.
- `sources/host-open-middle.md`, primary. §3 the footer verbatim; §4 the ten problem pages and their
  contributor bylines; §6 the trademark, the undocumented contributor chain and the embed pathway;
  §8 the gaps carried forward; §9 the bottom line for the curate-and-cite model.
- `sources/host-math-mistakes.md`, staged 2026-08-07, primary. §3 the licence verbatim with its
  twelve-year snapshot stability table; §5 riders 3 and 4, chain of title and student privacy; §7 the
  archive-citation note.
- `sources/verdict-twelve-host-table.md`, reference. §2 the verdict key and its three operations,
  including the two mechanical citation constraints and the fair-use position; §4.10 the four
  cite-only bibliographic forms; §5 the usable set with its inline retirement notes, where the
  cite-only blueprint finding is recorded. Cited as this project's own adjudication, never as a
  rights-holder's statement.
- `sources/k12-grounding-and-render.md`, primary. §2.2 the curriculum-terminology sweep, whose scope
  includes chat.
