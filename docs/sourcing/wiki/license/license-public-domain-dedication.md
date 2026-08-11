---
title: "Public-domain dedication (CC0-style)"
type: license
sources:
  - https://creativecommons.org/publicdomain/zero/1.0/
  - https://creativecommons.org/publicdomain/zero/1.0/legalcode.en
  - https://learnwithsap.org/permissions/
  - https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd
  - https://web.archive.org/web/20160303204431/http://achievethecore.org/ccpd
  - https://eric.ed.gov/?copyright
  - sources/cc0-1-0.md
  - sources/host-learnwithsap.md
  - sources/host-achieve-the-core.md
  - sources/host-eric.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# Public-domain dedication (CC0-style)

## Summary

A public-domain dedication is the most permissive instrument in this corpus and the one this
project has handled worst. Four facts, and any one of them alone misleads.

1. **The instrument imposes nothing.** CC0 1.0 has no conditions list, because there are no
   conditions. Measured in the staged deed: no ShareAlike, no NoDerivatives, no attribution
   requirement, commercial use permitted in terms. Do not write that CC0 "requires attribution".
2. **Neither dedication found here was written as "CC0".** Both use the phrase
   `the Creative Commons Public Domain Dedication License`, with no version number and no link
   to creativecommons.org. "CC0 1.0" is an inference nobody can read off either page.
3. **One of the two was withdrawn and the other does not reach the material.** Achieve the Core
   carried a blanket dedication over `achievethecore.org` until it was withdrawn between
   2026-04-25 and 2026-08-08. What survives is `learnwithsap.org/permissions/`, whose own scope
   sentence covers `learnwithsap.org` and, by its own words, not the domain where the maths
   library lives.
4. **Statutory public domain is a different mechanism entirely.** ERIC's Copyright Policy names
   it and bounds it in the same paragraph, and no dedication is involved. Quoted below.

The retired form is `"CC0", unqualified`. Name the instrument as the host named it, and name the
date you saw it.

## When to reach for it

Reach for this page when a host says "public domain", "dedicated", or "CC0" and you are about to
record a verdict. The verdict a dedication would earn is `quote_and_adapt` with no attribution
condition, which is the loosest outcome available, so it is the claim that most needs its
evidence pasted before it is believed. See [[practice-build-a-source-table]].

Reach for it when an attribution block tempts you to leave a source out because it is public
domain. Citation is a scholarly obligation, not a licence obligation. See
[[practice-assemble-an-attribution-block]].

Do **not** reach for this page to decide whether a withdrawn dedication still covers material
published under it. That question is open, is recorded as open on both pages, and is dated at
[[license-withdrawn-grants]]. Do not reach for it for silence either: a file with no notice is
not dedicated to anything, and that is [[license-unmarked-silence]].

## How it works

The CC0 1.0 deed and legal code were fetched with `curl -sS -L`, default user agent, on
2026-08-08: the deed HTTP 200 at 30476 bytes, the legal code HTTP 200 at 32451 bytes, no
redirect, no bot block, no soft-404.

**The deed is shaped unlike every licence deed.** The six Creative Commons licence deeds share
the headings `You are free to` / `Under the following terms` / `Notices`. This one has none of
them. Its headings are `No Copyright` and `Other Information`, and there is no conditions list.

Under `No Copyright`, verbatim:

> The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

> You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. See Other Information below.

**There is no attribution requirement, and this is the fact most often got wrong.** The deed
states no attribution condition and the legal code states none. What exists instead is a
caution, verbatim from `Other Information`:

> When using or citing the work, you should not imply endorsement by the author or the affirmer.

It says `you should not`, not `you must not`, and its own footnote grounds it in general law
rather than in CC0. Do not present it as a credit duty.

**The mechanism is a waiver with a licence fallback, which the deed does not describe.** Legal
code Section 2 is the Waiver, made `overtly, fully, permanently, irrevocably and
unconditionally`. Section 3 is the Public License Fallback, verbatim in its opening:

> Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer's express Statement of Purpose.

It then grants an unconditional licence to the same effect. Where a waiver of copyright is
impossible the outcome for a reuser is the same, but the mechanism is not what "dedication"
suggests, and the deed's own sentence bounds it with `to the extent allowed by law`.

**Four things the instrument does not reach**, each stated in the legal code and each easy to
lose because the deed compresses them. Trademark and patent, by Section 4(a). Moral rights where
applicable law makes them inalienable, which the deed does not name at all. Any warranty that the
affirmer owned the work: the deed's own `Notice` says
`Creative Commons has not verified the copyright status of any work to which CC0 has been applied`
(see [[concept-chain-of-title]]). And third-party rights inside the work, Section 4(c), verbatim:

> Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof, including without limitation any person's Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work.

That last one is the CC0 counterpart of a third-party carve-out, and on this corpus it lands
hard: every Coherence Map example problem for HSG-SRT.B.4, B.5, C.6, C.7 and C.8 carries the
attribution `"Provided by Illustrative Mathematics"` and no licence statement, while the one IM
file opened from that family is CC BY-NC-SA. A dedication over the wrapper says nothing about the
contents. See [[concept-third-party-carve-out]].

## In practice

### The live dedication, and what it does not say

`https://learnwithsap.org/permissions/`, HTTP 200, page states "Published July 16, 2024",
fetched 2026-08-07 with a browser user agent because the default agent gets HTTP 403 from
Cloudflare on that host. The full body is two paragraphs. The second is the grant, verbatim:

> "All of the content on learnwithsap.org is covered by the Creative Commons Public Domain Dedication License unless it is marked with the ©, which indicates that it includes content that has been licensed to Student Achievement Partners, Inc., from third parties."

The first paragraph is the CC0 deed's own `No Copyright` sentence, reproduced without
attribution to Creative Commons and without its second sentence.

**A grep for `creativecommons` in that page's HTML returns zero hits.** No version, no deed link,
no chooser badge. The words quoted above are the whole grant. Whether the intended instrument is
CC0 1.0, the Public Domain Mark, or something else is unverified from the page, and the deed
extract staged here notes that PDM and the CC0 chooser are different things at different URLs.

### The © test the page sets for itself, and the file that defeats it

The page makes the © character the sole signal separating dedicated content from third-party
content. This project opened a file that breaks the test, recorded verbatim:

> "The © heuristic from /permissions/ FAILS HERE. The PDF contains no "©" character anywhere (measured: zero hits). Per the permissions page's own rule this file would read as public domain. It is not."

The file is the Grade 8 IM Equations of Lines task PDF served from achievethecore.org, whose own
text reads, on two different pages:

> "8.EE Equations of Lines Typeset May 4, 2016 at 22:05:25. Licensed by Illustrative Mathematics under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License."

> "8.EE Equations of Lines is licensed by Illustrative Mathematics under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License"

So a file with no © is not public domain, it is ShareAlike, and it is internally inconsistent
about its own version. Open the artifact. See [[license-sharealike]].

### The withdrawn dedication, and the sentence that replaced it

`achievethecore.org/ccpd` carried a parallel dedication naming its own host. The last archived
capture carrying it is `20260425161111`, verbatim:

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain Dedication License unless it is marked with the ©, which indicates that it includes content that has been licensed to Student Achievement Partners, Inc., from third parties and must be used solely as noted when hovering over the © next to the applicable content."

Note the trailing clause, which the surviving learnwithsap.org text does not carry. What is live
in its place is the Copyright section of the Terms of Use, HTTP 200, fetched 2026-08-08,
verbatim:

> "Some material on Our Site is protected by copyright and some material has been dedicated to the public domain. For material protected by copyright, SAP owns or has the right to include the material on Our Site. Material may be used as indicated on Our Site for the particular material. You may not remove or modify any copyright notices, credit or other attribution associated with materials."

That sentence moves the grant from blanket to per-item, and this project measured the per-item
indication to be usually absent: of three resource pages opened on that host, two carried no
marking at all, and the one marked maths resource was CC BY-NC-SA rather than dedicated. The
dating, the removal window and the commented-out footer link live on
[[license-withdrawn-grants]]; the host verdict lives on [[source-achieve-the-core-sap]].

### Statutory public domain, which ERIC bounds in the same paragraph

`https://eric.ed.gov/?copyright`, HTTP 200, fetched 2026-08-08, verbatim:

> Certain works, including documents, reports, and other materials authored by the U.S.
> government, reside in the public domain and may be freely distributed and copied. Works
> authored by a private contractor on behalf of the U.S. government are not necessarily in
> the public domain. Contract terms and conditions vary from one agency to another. If the
> copyright status of a particular work is uncertain, it should be verified with the
> sponsoring agency.

A federally funded education report is not automatically free, and ERIC says so on its own
copyright page. See [[source-eric]].

## Gotchas & constraints

**1. The corpus contains zero verified instances of CC0 1.0.** Two hosts named a public-domain
dedication in prose. Neither named a version and neither linked a deed. Writing "CC0 1.0" on
either is an upgrade this project cannot support. What would close it: ask Student Achievement
Partners which instrument `learnwithsap.org/permissions/` intends, or find a chooser badge or
deed link anywhere on that host.

**2. The scope sentence names a domain, and the maths is on the other one.** This project's own
record, verbatim: `"The page says "All of the content on learnwithsap.org" — by its own words it does NOT cover achievethecore.org, and ATC's own /permissions is a soft 404. This is a real gap."`
Do not carry a dedication across a domain boundary because the two sites share an owner.

**3. Irrevocability is a counsel question here, not a fetched fact.** A public-domain dedication
is generally understood to be irrevocable, and CC0's own Section 2 uses the word `irrevocably`.
Whether that helps material published under Achieve the Core's former dedication turns on
whether the dedication was validly made, over which items, and on what date each item was
published. This project's verdict table names it, in its own words, the single most consequential
open question in the corpus and sends it to counsel. Do not resolve it in either direction on the
strength of this page.

**4. Absence of a mark is not an affirmative grant.** The © test above is the corpus's worked
counterexample, and it fails in the direction that costs you: an unmarked file read as dedicated
when it was ShareAlike. Once a blanket dedication is withdrawn, an unmarked artifact is silent
rather than free. See [[license-unmarked-silence]].

**5. The page documenting CC0 is not itself CC0.** The deed page's site footer, verbatim:
`Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license.`
A reuser of the deed page owes attribution under [[license-cc-by]]. Do not read that footer as
evidence about the instrument the page documents.

**6. Sampling limit, stated plainly.** Three resource pages and two PDFs on achievethecore.org,
one live permissions page on learnwithsap.org. This project records that "varies per resource" on
that host is established by counterexample rather than by census, that the marked-to-unmarked
proportion is unknown, and that with no sitemap and no robots.txt the URL space could not be
enumerated, so a permissions page under an unguessed path cannot be ruled out.

## Related

- [[license-withdrawn-grants]] dates the Achieve the Core withdrawal. This page holds the instrument and the open irrevocability question.
- [[license-unmarked-silence]] is the state an artifact falls into when a blanket dedication goes away.
- [[license-all-rights-reserved]] is the other end of the same axis, and the Berne default.
- [[license-cc-by]] is what the Creative Commons deed pages are themselves published under.
- [[license-sharealike]] is what the file that defeated the © test actually carries.
- [[concept-cite-quote-adapt]] is why a dedication changes the quote and paraphrase answers and never the citation answer.
- [[concept-third-party-carve-out]] is the Section 4(c) problem worked in general.
- [[concept-chain-of-title]] is the "Creative Commons has not verified the copyright status of any work" problem, sharper here because there is no licensor left to ask.
- [[source-achieve-the-core-sap]] is the host verdict for both domains in this family.
- [[source-eric]] is where the statutory public-domain paragraph lives and where it is bounded.
- [[trap-license-withdrawn-after-citation]] is the failure a recorded CC0 citation produces once the page is gone.
- [[trap-soft-404-status-proves-nothing]] is why `achievethecore.org/permissions` returning HTTP 200 does not mean a permissions page exists.

## Composes with

- [[practice-build-a-source-table]] is the procedure that runs before a dedication becomes a verdict, and would have caught the missing version string.
- [[practice-assemble-an-attribution-block]] consumes the finding that a dedication carries no attribution condition.
- [[practice-cite-without-redistributing]] is the posture that stays correct whether or not the irrevocability question is ever answered.

## References

Rights-holder and instrument pages:

- `https://creativecommons.org/publicdomain/zero/1.0/` HTTP 200, 30476 bytes, and `.../legalcode.en` HTTP 200, 32451 bytes, both fetched 2026-08-08. The deed's two headings, the absent conditions list, the non-endorsement caution, and legal code Sections 2, 3, 4(a), 4(c), 4(d).
- `https://learnwithsap.org/permissions/` HTTP 200, browser user agent, fetched 2026-08-07, "Published July 16, 2024". The live dedication and the © carve-out.
- `https://achievethecore.org/terms-of-use` HTTP 200, fetched 2026-08-08. The per-item claim that replaced the dedication.
- `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd` HTTP 200, and `https://web.archive.org/web/20160303204431/http://achievethecore.org/ccpd` HTTP 200, 37273 bytes. The last and the first archived captures of the withdrawn dedication.
- `https://eric.ed.gov/?copyright` HTTP 200, 9190 bytes, fetched 2026-08-08. The statutory public-domain paragraph and its private-contractor bound.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/cc0-1-0.md`, primary. The deed and legal code verbatim, with the measured absences.
- `sources/host-learnwithsap.md`, primary. The permissions page verbatim, the zero-hit `creativecommons` grep, the Cloudflare 403, the © test failure at Sample 2, the recorded scope gap.
- `sources/host-achieve-the-core.md`, primary. The archived dedication and the three per-resource samples behind the "usually absent" finding.
- `sources/host-eric.md`, primary. The Copyright Policy verbatim.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: §3 corrections 3, 4 and 7, and §6 where the irrevocability question is recorded as counsel's.

The underlying fetch reports, cited as this project's own measurement and not as any outside
party's statement: `Projects/HS Geometry/sources/license-learnwithsap.md` (§3a, Rider A, §6
Sample 2), `Projects/HS Geometry/sources/license-achieve-core.md` (§4), and
`Projects/HS Geometry/sources/source-verdict-table.md` (§3 and §6).
