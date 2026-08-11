---
title: "NonCommercial (the NC rider)"
type: license
sources:
  - https://creativecommons.org/licenses/by-nc/4.0/
  - https://creativecommons.org/licenses/by-nc/4.0/legalcode.en
  - https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en
  - https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode.en
  - sources/cc-by-nc-4-0.md
  - sources/cc-by-nc-sa-4-0.md
  - sources/cc-by-nc-sa-3-0.md
  - sources/cc-by-nc-nd-3-0.md
  - sources/cc-by-4-0.md
  - sources/host-accessim-360.md
  - sources/host-im-kendall-hunt.md
  - sources/host-engageny-nysed.md
  - sources/host-mars-map.md
  - sources/host-learnwithsap.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# NonCommercial (the NC rider)

## Summary

NC is a rider, not a licence. It rides on a CC BY baseline and does exactly one thing: it deletes
the `for any purpose, even commercially` clause from both freedoms and adds a separate condition
below. Here it appears on `accessim.org` as CC BY-NC 4.0, and again inside every BY-NC-SA and
BY-NC-ND grant in the corpus.

Two properties make NC the rider people get wrong in opposite directions at once.

**NC has no copyleft.** Under CC BY-NC 4.0 you may paraphrase and republish, and your derivative
does not have to ship under CC BY-NC 4.0. What travels downstream is the NC constraint on the
underlying material, not a licence obligation on your own contribution. Readers burned by
ShareAlike routinely assume NC behaves the same way; see [[license-sharealike]].

**NC is dormant, not absent.** It costs nothing while nothing is sold and it becomes unlicensable
the moment something is. That makes it a latent property of every file NC material lands in, and
the file will not look any different on the day the answer changes.

A third property is specific to this corpus: **the word "commercial" appears zero times across all
19 pages fetched from `accessim.org`.** The restriction is carried by the licence label and its
hyperlink alone. The prose prohibition exists only off-host, in Illustrative Mathematics' central
Terms §7.2.

## When to reach for it

Reach for this page when a source you want carries NC and nothing is currently sold, and you need
to decide whether that is a decision or a deferral. Reach for it when someone argues that a
school, a nonprofit or an internal repo is automatically non-commercial: the test is about the
intent of the use, not the tax status of the user.

Reach for it before writing "NC forbids adaptation" anywhere. It does not. NoDerivatives forbids
adaptation, and here ND rides alongside NC on `map.mathshell.org`, which is where that confusion
usually starts. See [[license-noderivatives]].

Do not reach for this page to decide whether a specific host is NC. That is a dated fetch against
the host with a pasted sentence.

## How it works

### The rider is a deletion plus a condition

CC BY-NC 4.0's freedoms, verbatim:

> **Share** — copy and redistribute the material in any medium or format

> **Adapt** — remix, transform, and build upon the material

The load-bearing fact is what is absent. Both CC BY 4.0 freedoms end `for any purpose, even
commercially`; these do not. **The NC restriction is expressed by deleting that clause, not by
negating it in place**, so a search for a "not" will not find it. The added condition, verbatim:

> **NonCommercial** — You may not use the material for commercial purposes.

### What "commercial" means, and the sentence the deed drops

The deed's footnote, verbatim:

> **commercial purposes** — A commercial use is one primarily intended for commercial advantage or monetary compensation.

The 4.0 legal code definition is longer and adds a carve-out the deed omits entirely, verbatim:

> **NonCommercial** means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.

Note `not primarily intended for or directed towards`. **The test is the intent of the use.** A
nonprofit can make a commercial use and a company can make a non-commercial one. Nothing in either
instrument turns on who the user is.

### NC sits inside the grant, so exceeding it is not a billing question

Legal code Section 2(a)(1), verbatim:

> reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
>
> produce, reproduce, and Share Adapted Material for NonCommercial purposes only.

On the deed, NonCommercial reads as a condition beside Attribution. In the licence it qualifies
the grant clause itself, in both limbs. A commercial use is therefore an unlicensed use, not a
licensed use that owes a fee. The licensor's fee position is stated separately and survives at
Section 2(b)(3), which waives royalty collection for the licensed exercise and `expressly reserves
any right to collect such royalties, including when the Licensed Material is used other than for
NonCommercial purposes`.

### The attribution machinery does not change, and 3.0 says something narrower

Section 3 of the CC BY-NC 4.0 legal code is byte-identical to Section 3 of CC BY 4.0. Measured
rather than eyeballed: both sections extracted from the fetched bytes and compared after
whitespace normalisation are 1554 characters and compare equal. Everything on [[license-cc-by]]
about what a credit line must contain applies here unchanged.

The 3.0 instruments word the restriction differently, and **the hyphenation defect `con-nection`
is in the served bytes**, reproduced exactly rather than corrected:

> You may not exercise any of the rights granted to You in Section 3 above in any manner that is primarily intended for or directed toward commercial advantage or private monetary compensation. The exchange of the Work for other copyrighted works by means of digital file-sharing or otherwise shall not be considered to be intended for or directed toward commercial advantage or private monetary compensation, provided there is no payment of any monetary compensation in con-nection with the exchange of copyrighted works.

`private monetary compensation` in 3.0 where 4.0 says `monetary compensation`. The same clause,
with the same typo, sits at Section 4(c) of the CC BY-NC-SA 3.0 legal code.

## In practice

| Host or artifact | Regime | How NC is carried | Recorded |
|---|---|---|---|
| `accessim.org`, IM TK-12 Math v.360 | CC BY-NC 4.0 | Label and `href` only. Footer "©2024 Illustrative Mathematics®. Licensed under CC BY-NC 4.0", uniform on 13 of 13 curriculum pages sampled | 2026-08-07 |
| `illustrativemathematics.org/terms-of-use/` §7.2 | prose prohibition for the above | The only place that prose exists, and it is off-host | 2026-08-07 |
| `tasks.illustrativemathematics.org` | CC BY-NC-SA 4.0 | Footer, byte-matched on all 24 in-scope task pages | 2026-08-08 |
| EngageNY resources via NYSED | CC BY-NC-SA, version disputed | Site-wide prose plus a per-resource badge, and a separate non-CC prose bar | 2026-08-08 |
| `map.mathshell.org` | CC BY-NC-ND 3.0, and BY-NC-SA 3.0 on PD Modules | Homepage sidebox says "non-commercial use" in plain English | 2026-08-08 |
| `learnwithsap.org` e² Instructional Practice Suite | not a CC licence at all | Bespoke terms: NC plus ND plus a public-redistribution bar | 2026-08-07 |

IM Terms §7.2, verbatim as staged, with the elision present in the transcription:

> **7.2 Curriculum License: IM® TK–12 Math v.360 | CC BY-NC**
> The second edition of IM K–12 Math, called IM TK–12 Math v.360 ("IM v.360") (© 2024 and IM
> TK Math © 2025) curriculum is freely accessible at accessim.org by teachers, students, and
> families as an Open Education Resource and is licensed under the Creative Commons
> Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). … Commercial use of the
> IM v.360 curriculum materials and name, including but not limited to incorporation into paid
> products or services or the name used for promotional purposes of third party products or
> services, is prohibited without prior written permission from Illustrative Mathematics.

The archived EngageNY Terms carry a second commercial bar in their own words, verbatim:
"Commercial use of the curricular materials is not allowed under this license." Their separate
non-CC permission clause adds: "Generally, reproducing materials for profit or any commercial use
is strictly forbidden." **Two grants on one page, and only one of them is Creative Commons.** See
[[source-engageny-nysed]].

Where nothing is sold, NC is satisfied. Every host report here that reached NC recorded the same
posture: not binding while nothing is monetised, live on any future monetisation. That is this
project's own reading of its own position, not a statement by any rights-holder.

## Gotchas & constraints

**1. NC is not copyleft and does not force your licence.** The only downstream rule in CC BY-NC
4.0 is Section 3(a)(4): `the Adapter's License You apply must not prevent recipients of the
Adapted Material from complying with this Public License`. That constrains the adapter's licence;
it does not dictate it. Contrast BY-NC-SA 4.0 Section 3(b), which requires a CC licence with the
same `License Elements` or a `BY-NC-SA Compatible License`. Collapsing the two is the most common
error in this family.

**2. NC is not NoDerivatives.** Under CC BY-NC 4.0 the `Adapt` freedom is present. Under CC
BY-NC-ND 3.0 there is no `Adapt` freedom on the deed at all: measured, that list has exactly two
items where every other deed in the cluster has three. On `map.mathshell.org` it is ND, not NC,
that makes the host cite-only.

**3. A licence label with no prose is still the licence.** On `accessim.org` "commercial" returned
0 hits across all 19 fetched pages. This project's own prior belief in an "explicit commercial
prohibition" on that host is recorded as **not corroborated as prose**. Both halves must travel
together: the grant is real, and the on-host prose a reader would look for is not there.

**4. The NC host's homepage carries no notice at all.** On `accessim.org` the footer renders only
inside the curriculum route tree, so a reader checking the root would conclude the site is
unlicensed. The same structural failure produced a false "unlicensed" reading of
`im.kendallhunt.com` in this project's record. See [[trap-license-lives-off-the-obvious-page]].

**5. HTTP status proves nothing about existence there.**
`accessim.org/zzz-definitely-not-a-real-page-9876` returns HTTP 200 at 1,486,023 bytes, and
`/terms`, `/copyright`, `/license`, `/permissions` and `/attributions` all return 200 while none
exists. Existence is tested by byte-diff, not by status. See
[[trap-soft-404-status-proves-nothing]].

**6. NC also appears outside Creative Commons, and the deed's definition does not reach it.** The
`learnwithsap.org` e² Tools terms grant `a limited, non-exclusive, non-transferable, revocable
license` for `internal, non-commercial educational purposes`, then bar public redistribution
`(including websites, social media, marketplaces, or AI training datasets)`, derivative works, and
`commercial purposes, including resale, fee-based training, or incorporation into paid platforms`.
None of the CC machinery on this page interprets that document. See
[[source-achieve-the-core-sap]].

**7. The 3.0 wording is not the 4.0 wording**, and 3.0 Unported is not 3.0 US. Where a host pins a
version, use that version's text.

**8. NC attaches to the file, and the file is where it will be forgotten.** A quotation from an NC
source carries the constraint on that material for as long as it is in the deliverable. Under
ruling R9 the repo ships CC BY 4.0, whose `No additional restrictions` condition bars applying
legal terms that restrict what that licence permits. Keeping NC material out of the adapted
through-line is cheaper than tracking it. See [[practice-cite-without-redistributing]].

**9. Citing is never touched by NC.** Naming a source, linking it, stating which standard it
addresses and describing in your own words what it does needs no licence at all, without exception
across every NC source here. See [[concept-cite-quote-adapt]].

## Related

- [[license-cc-by]] is the baseline this rider rides on and holds the attribution machinery NC
  leaves untouched.
- [[license-sharealike]] is the rider NC is most often confused with.
- [[license-noderivatives]] is why the most on-standard NC host here is still cite-only.
- [[license-all-rights-reserved]] is a positively asserted reservation, a different state from NC.
- [[source-accessim-360]] is the CC BY-NC 4.0 host where label-only carriage was measured.
- [[source-im-task-bank]] and [[source-engageny-nysed]] are where NC and SA arrive together.
- [[source-mars-map]] is where NC and ND arrive together.
- [[concept-cite-quote-adapt]] separates what NC touches from what it does not.
- [[trap-soft-404-status-proves-nothing]] is the measurement trap on the primary NC host.

## Composes with

- [[practice-assemble-an-attribution-block]] consumes the accessim.org credit line and version pin.
- [[practice-cite-without-redistributing]] is the operation that keeps NC material out of the file
  it would otherwise attach to.

## References

Instruments fetched by this project 2026-08-08, `curl -sS -L`, default user agent, raw bytes
parsed locally, no summarizing layer:

- `https://creativecommons.org/licenses/by-nc/4.0/` HTTP 200, 35485 bytes, 0 redirects. This fetch
  closed an `INVENTORY.md` gap: the deed had been recorded only as an `href` target, never fetched.
- `.../by-nc/4.0/legalcode.en` HTTP 200, 50209 bytes. The NonCommercial definition, Sections
  2(a)(1), 2(b)(3), 3 and 4(a).
- `.../by-nc-sa/4.0/legalcode.en` HTTP 200, 53058 bytes, and `.../by-nc-nd/3.0/legalcode.en`
  HTTP 200, 50763 bytes, the source of the 3.0 clause with the `con-nection` defect.

Staged extracts in this wiki, all staged 2026-08-08: `sources/cc-by-nc-4-0.md` (primary, the
deletion finding and the byte-identical Section 3 measurement); `sources/cc-by-nc-sa-4-0.md` and
`sources/cc-by-nc-sa-3-0.md` (primary, NC alongside ShareAlike at both versions);
`sources/cc-by-nc-nd-3-0.md` (primary, NC alongside NoDerivatives); `sources/cc-by-4-0.md`
(primary, the baseline whose commercial clause NC deletes); `sources/host-accessim-360.md`
(primary, the verbatim footer, the 19-page audit table and the soft-404 measurement);
`sources/host-im-kendall-hunt.md` (primary, IM Terms §7.2); `sources/host-engageny-nysed.md`
(primary, the archived Terms with two grants on one page); `sources/host-mars-map.md` (primary,
the homepage sidebox and four per-collection regimes); `sources/host-learnwithsap.md` (primary,
Rider B verbatim); `sources/verdict-twelve-host-table.md` (reference, §2 verdict key, §3
correction 2, §4.4 the accessim.org attribution block).
