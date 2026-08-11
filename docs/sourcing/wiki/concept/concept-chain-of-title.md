---
title: Chain of title
type: concept
sources:
  - sources/host-math-mistakes.md
  - sources/host-im-task-bank.md
  - sources/host-open-middle.md
  - sources/host-learning-commons-kg.md
  - sources/host-engageny-nysed.md
  - sources/host-learnwithsap.md
  - sources/cc0-1-0.md
  - sources/cc-by-4-0.md
  - sources/verdict-twelve-host-table.md
  - https://creativecommons.org/publicdomain/zero/1.0/
updated: 2026-08-08
---

# Chain of title

## Summary

A licence footer says what the host is offering. It does not say whether the host had the material
to offer. Those are two facts, and the second one is invisible from the footer.

Chain of title is the question of whether the party granting a licence actually holds the rights it
is granting, all the way back to whoever made the thing. Where the chain is broken or undocumented,
the grant is worth less than it reads, because a licence cannot convey rights the licensor does not
hold. This is not a rare edge case in this corpus. Named hosts carrying a visible chain-of-title
problem, each evidenced below: EngageNY and NYSED, the IM task bank, Open Middle, Math Mistakes,
the Learning Commons Knowledge Graph, and the Achieve the Core Coherence Map. On the first of
those, the host states the problem itself, in writing.

The operational consequence is narrow and specific. A broken chain does not make a source unusable.
It removes the second and third of the three operations in [[concept-cite-quote-adapt]] and leaves
the first. Citation is unaffected by chain of title, because citing does not rest on any grant at
all. So the finding is always the same shape: **stop at citation, credit the party actually named,
do not reproduce, and record why.**

## When to reach for it

Reach for it whenever a licence footer reads permissively over material the host plainly did not
make. That combination is the trigger, and it is visible without a lawyer: a blanket site-wide grant
sitting above per-item bylines naming other people. Reach for it likewise before treating an
aggregator's presentation as a rights fact, because an index or a coherence map that serves someone
else's content with an attribution line and no licence statement has told you nothing.

Do **not** reach for it to resolve a chain. Every chain-of-title question in this corpus that was
worth asking turned out to be unresolvable by fetching, and the twelve-host record files them under
"not closeable by fetching, legal judgment required". The value of this page is recognising the
pattern early enough to stop, not closing it.

## How it works

### The instruments say so themselves

Creative Commons does not warrant that a licensor owned what it licensed. The CC0 1.0 deed page
carries a paragraph unique to it, verbatim:

> Creative Commons has not verified the copyright status of any work to which CC0 has been applied.
> CC makes no warranties about any work or its copyright status in any jurisdiction, and disclaims
> all liability for all uses of any work.

The CC0 legal code puts the same disclaimer on the affirmer, Section 4(c), verbatim:

> Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work
> or any use thereof, including without limitation any person's Copyright and Related Rights in the
> Work.

and the licence deeds carry it in their Notices block, verbatim: "No warranties are given. The
license may not give you all of the permissions necessary for your intended use."

A CC mark is a statement of intent by whoever applied it. It is not a title search.

### The five recognition signals

Each of these was observed on a named host in this corpus. Any one of them is enough to move a
source to `cite_only` pending resolution.

**1. The host publishes its own upstream credit next to the grant.** The material declares its
origin elsewhere while the footer asserts a blanket licence over it.

**2. Per-item bylines name individuals, with no visible assignment instrument.** The site asserts a
site-wide posture over work it collected from contributors, and nothing on the site establishes
that contributors transferred anything.

**3. The publisher states in writing that it is not the owner.** Rare, decisive, and it is present
here.

**4. The grant rests on a private permission nobody can inspect.** The public licence is real, but
the authority behind it is an unpublished agreement.

**5. A redistributor serves another party's work without surfacing that party's licence.** The
downstream presentation is clean; the upstream obligation is invisible from it.

### Why the answer is citation rather than a risk score

Naming a work, linking it and describing it in your own words needs no grant from anyone, so it is
untouched whether the chain is clean, broken or unknown. That makes "stop at citation" a decision
requiring no legal judgment, which is the property you want when the alternative is an unresolvable
question. The cost is real: it removes the material from the adaptable pool, which on this corpus is
already narrow. See [[concept-curate-and-cite]].

## In practice

**Signal 3, stated by the publisher. EngageNY and NYSED.** The archived EngageNY Terms of Use,
Wayback snapshot 2022-06-18, fetched 2026-08-08, HTTP 200, verbatim:

> Commercial use of the curricular materials is not allowed under this license. Furthermore, NYSED
> is not the copyright owner of the curricular materials but rather NYSED holds a license to use
> the materials. As such, any use of the curricular materials beyond those allowed under the
> Creative Commons license would require the express written permission of the copyright owners.

The owner is named nowhere in anything this project fetched. The verifying agent grepped every
fetched resource page for "Great Minds", "Eureka" and "©" and recorded **zero hits on all three**.
The common attribution to Great Minds is folk knowledge, is not in the verified record, and is not
asserted here. See [[source-engageny-nysed]].

**Signal 1, the host's own commentary. The IM task bank.** Four HSG-SRT.B.5 tasks carry the same
blanket CC BY-NC-SA 4.0 footer as the other twenty while their own IM Commentary declares an
upstream. Verbatim from the task pages, fetched 2026-08-08:

| Task | IM Commentary, verbatim |
|---|---|
| 1002 Bank Shot | "This task was adapted from problem #12 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 1009 Tangent Line to Two Circles | "This task was adapted from problem #19 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 916 Finding triangle coordinates | "This task was adapted from problem #11 on the 2012 American Mathematics Competition (AMC) 10A Test. In the AMC exam question, the diagram was not given." |
| 918 Slope Criterion for Perpendicular Lines | "This task was adapted from problem #15 on the 2012 American Mathematics Competition (AMC) 10A Test." |

The host says nothing about the AMC or MAA rights position, and the fetching agent did not leave
the host to check, so the upstream grant is unverified from here. This project's own instruction is
to cite these four and neither reproduce nor adapt them, on the stated ground that IM's CC grant
cannot convey rights IM does not hold. The other 20 in-scope tasks state no upstream source. See
[[source-im-task-bank]].

**Signal 2, contributor bylines under a blanket footer. Two hosts, opposite postures, same defect.**
On `openmiddle.com`, all 10 problem pages in the matching category were opened individually on
2026-08-08 and every one carries a named individual byline ("Source: Drew Ross", "Source: Kate
Nerdypoo", and so on) beneath a site-wide all-rights-reserved footer, while `/submit/` presents no
copyright-assignment or licensing language. On `mathmistakes.org` the posture is the reverse, a
blanket CC BY 3.0 Unported grant, and the About page states the collection model verbatim:

> That student work will be posted by me, but sent in by you.

The corpus is teacher-submitted photographs. No submission agreement, rights transfer or
contributor terms exist anywhere on the site: `/terms/`, `/contact/` and `/faq/` all return 404 in
Wayback and were, on the verifying agent's reading, never created. Whether the owner had authority
to sublicense submitters' photographs under CC BY is not established by anything on the site. Note
that the direction of the defect does not matter. A blanket grant over unassigned contributions and
a blanket reservation over unassigned contributions are the same unresolved question. See
[[source-open-middle]] and [[source-math-mistakes]].

**Signal 4, a private permission. The Learning Commons Knowledge Graph.** The whole 512-byte
`LICENSE.md`, HTTP 200, fetched 2026-08-08, states verbatim that "Learning Commons received state
standards and written permission under CC BY 4.0 from 1EdTech". That written permission is a
private agreement between the two parties. It is not published and was not verifiable. The entire
CC BY 4.0 chain on the state standards layer rests on it, and this project could not inspect it.
Separately and more consequentially for this build, Learning Commons stamps CC BY 4.0 on CCSS
statement text that NGA and CCSSO licence under narrower, non-Creative-Commons terms, and the two
grants do not agree. See [[source-learning-commons-kg]] and [[source-corestandards-nga-ccsso]].

**Signal 5, an invisible upstream obligation. The Coherence Map.** `tools.achievethecore.org`
serves the full example task text and solution for all five target standards inline, each carrying
the attribution "Provided by Illustrative Mathematics" and, measured on the decoded inline HTML for
two of those ids, zero occurrences of "licen", "creative commons", "©" or "copyright". A user
relying on that presentation could never learn the ShareAlike obligation exists. This project's own
instruction is not to launder IM tasks through Achieve the Core but to source and clear them at IM.
See [[source-achieve-the-core-sap]].

## Gotchas & constraints

**1. A chain-of-title finding is not a licence finding, and must not be filed as one.** The IM task
bank's grant is CC BY-NC-SA 4.0, verified by byte match on all 24 in-scope pages. That fact is
unchanged by the AMC problem. Record the licence and the chain defect as two separate rows, because
they have different evidence, different fetch dates and different resolutions.

**2. Nothing here is a legal conclusion.** This project made none. The twelve-host record files
these questions under legal judgment, not measurement, including whether IM ever cleared the four
AMC tasks with MAA, whether Open Middle's blanket reservation binds contributor-authored problems
given no visible assignment, and whether the Math Mistakes owner had authority to sublicense. Each
would require asking a party outside every agent's scope.

**3. Student privacy is a different axis and does not resolve with the chain.** Every Math Mistakes
post is a photograph of a minor's handwritten work. A valid CC BY grant settles copyright and says
nothing about privacy exposure in a public repository. No agent opened the images, so the concern is
raised structurally rather than from inspection, and the recommendation is not to reproduce them.

**4. Absence of a byline is not evidence of a clean chain.** On `tasks.illustrativemathematics.org`
a keyword sweep of six task pages for `adapted from`, `courtesy`, `used with permission`, `photo by`
and `flickr` returned zero hits, yet task 1591 embeds photographs served from a plain-http S3 bucket
with no credit line at all. Unstated provenance is the harder case, not the safer one.

**5. Nominative use survives.** Naming Illustrative Mathematics, Open Middle or the New York State
Education Department in a citation is ordinary nominative reference and is not affected by any of
this. What is affected is reproduction. Branding your own material with someone's registered mark
is a third and separate question, held at [[concept-third-party-carve-out]].

**6. The host list in this page's summary is this project's own reading of its twelve-host sweep,
fetched 2026-08-07 and 2026-08-08.** It is not a survey of open education generally, it is not a
claim that the remaining hosts have clean chains, and the per-host sampling limits recorded in the
sweep apply to it. Read the sampling limit on each host's own page before generalising from any
row here.

## Related

- [[concept-cite-quote-adapt]] is the operation split this page's remedy is stated in: chain of
  title removes operations two and three and leaves one.
- [[concept-third-party-carve-out]] is the neighbouring failure where the host does hold rights to
  its own expression but never held rights to something embedded inside it.
- [[license-cc-by]] and [[license-sharealike]] hold the grants that appear clean on the hosts above;
  [[license-all-rights-reserved]] holds the Open Middle posture, where a blanket reservation sits
  over the same unassigned contributions.
- [[source-engageny-nysed]] carries the one host in this corpus that states the defect itself.
  [[source-im-task-bank]], [[source-open-middle]], [[source-math-mistakes]],
  [[source-learning-commons-kg]] and [[source-achieve-the-core-sap]] each carry one of the signals
  with its own verbatim evidence and fetch date.
- [[source-corestandards-nga-ccsso]] holds the upstream grant that the Learning Commons stamp does
  not agree with.

## Composes with

- [[practice-build-a-source-table]] is where a chain-of-title finding is recorded, and it is a
  separate column from the licence verdict rather than a note inside it.
- [[practice-cite-without-redistributing]] is the procedure a broken chain hands the material to.

## References

Host and rights-holder evidence, all primary, staged 2026-08-08.
`sources/host-engageny-nysed.md`, fetched 2026-08-08: the archived EngageNY Terms of Use at Wayback
snapshot 2022-06-18, HTTP 200, carrying the not-the-copyright-owner sentence, and the three-way grep
returning zero hits for the folk attribution. `sources/host-im-task-bank.md`, fetched 2026-08-08:
the four AMC-derived tasks with their verbatim IM Commentary, the full 24-task sweep, and the
unstated photo provenance on task 1591. `sources/host-open-middle.md`, fetched 2026-08-08: the 10
individually opened problem pages with their contributor bylines, and the `/submit/` page carrying
no assignment language. `sources/host-math-mistakes.md`, fetched 2026-08-07: the About page
collection model verbatim, the Wayback 404s on `/terms/`, `/contact/` and `/faq/`, and the privacy
rider stated as a separate axis. `sources/host-learning-commons-kg.md`, fetched 2026-08-08:
`LICENSE.md` HTTP 200, 512 bytes, whole file, and the record that the 1EdTech written permission is
private and not inspectable. `sources/host-learnwithsap.md`, fetched 2026-08-07: Coherence Map
`data.js` HTTP 200, ids 612 to 616, with the measured absence of any licence string on the
redistributed IM task text.

Creative Commons instruments, staged verbatim 2026-08-08: `sources/cc0-1-0.md` (deed HTTP 200,
30476 bytes; legal code HTTP 200, 32451 bytes) for the unverified-copyright-status paragraph and
Section 4(c); `sources/cc-by-4-0.md` (deed HTTP 200, 32178 bytes) for the Notices block disclaiming
that the licence gives all necessary permissions.

This project's own adjudication, cited as this project's measurement and not as any outside party's
statement: `sources/verdict-twelve-host-table.md`, reference, Section 1 rows 3, 5, 6, 8, 10 and 12
for the per-host findings; Section 3 correction 11 for the EngageNY ownership gap; Section 6, "not
closeable by fetching", for the chain questions filed as legal judgment.
