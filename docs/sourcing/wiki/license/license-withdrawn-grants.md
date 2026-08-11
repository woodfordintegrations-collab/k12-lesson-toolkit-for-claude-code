---
title: "Withdrawn and mutable grants"
type: license
sources:
  - https://www.openmiddle.com/
  - https://achievethecore.org/ccpd
  - https://achievethecore.org/terms-of-use
  - https://illustrativemathematics.org/terms-of-use/
  - https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd
  - https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/
  - sources/host-open-middle.md
  - sources/host-achieve-the-core.md
  - sources/host-im-kendall-hunt.md
  - sources/host-learning-commons-kg.md
  - sources/cc0-1-0.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# Withdrawn and mutable grants

## Summary

A licence is not a property of a source. It is a property of a source **at a date**. This page is
the dated register of the grants that changed inside this corpus's own working window, and the
reason every licence claim in this wiki carries a fetch date.

**Two grants were withdrawn within six months of each other, in a twelve-host sweep.** That is
the measured base rate on the hosts this project actually opened, and it is not small.

| Host | Grant that was withdrawn | Removal window, as measured | What is live instead |
|---|---|---|---|
| `openmiddle.com` | CC BY-NC-SA 4.0, carried since 2016 | between **2026-02-16 and 2026-03-03** | all rights reserved, no policy document at all |
| `achievethecore.org` | "Creative Commons Public Domain Dedication License" over the whole host | between **2026-04-25 and 2026-08-08** | a per-item claim, usually not indicated |

A third change is a different kind of event and must not be merged into the first. Open Middle's
rights-holder changed from Open Middle Partnership to Glenrock Consulting, LLC **between
2026-03-03 and 2026-05-12**, which is separate from and later than the licence removal. Two
events, in that order.

And the strongest grant in the corpus is explicitly mutable. Illustrative Mathematics' central
Terms of Use are headed **"Effective as of May 21, 2026"**, eleven weeks before this project's
fetch, on a document that governs the host the curriculum build writes from.

**Mutable and withdrawn are two states, not one.** Every grant here is mutable. This project
counts three changes across the two hosts above. Recording which is which is the whole job of
this page; the failure a stale citation produces is worked at
[[trap-license-withdrawn-after-citation]].

## When to reach for it

Reach for this page before writing any licence claim into a durable artifact: a bibliography, a
LICENSE file, an attribution block, a source table. The question is not "what is this source
licensed under" but "what was it licensed under on the date I looked, and how old is that date
now".

Reach for it when you are about to trust a third-party OER list, a syllabus, a prior citation, or
your own memory. Both withdrawals below had been true for years first. This project's own record
of the damage, in its own words: **"Folk knowledge about open-education licensing has been
measured wrong three times in this project, not twice."**

Reach for it before publication. This project's re-verification trigger names four hosts to
re-pull before the repository ships and says to record the new fetch date in the attribution
block.

Do **not** reach for this page to decide whether material obtained under a since-withdrawn grant
remains usable. That question is open, is recorded as open, and goes to counsel. The doctrine
half sits at [[license-public-domain-dedication]] and the practical half is below.

## How it works

A grant is an offer the rights-holder publishes. Nothing obliges them to keep publishing it, and
in this corpus nobody announced when they stopped. Both withdrawals were found by comparing
archived captures against a live fetch, not by reading a notice.

Two properties make that hard to detect. **Withdrawal is silent by construction:** no host here
published a changelog, a deprecation notice, or a dated statement, so Open Middle's CC clause is
simply absent from the next capture and Achieve the Core's Permissions page simply stopped
resolving. **And a withdrawn page does not necessarily 404:** on `achievethecore.org` every
unknown URL returns HTTP 200 with a byte-identical homepage shell, so `/ccpd` today returns a
clean 200 that proves nothing, and existence has to be tested by byte comparison. See
[[trap-soft-404-status-proves-nothing]].

What survives a withdrawal, in every case here, is citation. Naming a source, linking it, and
describing what it covers needs no grant and never did. See
[[practice-cite-without-redistributing]].

## In practice

### Open Middle: the footer, capture by capture

Archived footers read from Wayback `id_` raw captures fetched with `--compressed` on 2026-08-08,
with the live fetch on the same date using a browser user agent because the default agent gets
HTTP 406:

| Snapshot | CC present | Footer fragment, verbatim as recorded |
|---|---|---|
| 2016-05-27 | yes | "Open Middle is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2019-06-03 | yes | "Open Middle ® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2023-06-01 | yes | "© 2016-2023 Open Middle Partnership. All rights reserved. ... Open Middle® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2026-01-09 | yes | "© 2016-2026 Open Middle Partnership. All rights reserved. ... licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0" |
| **2026-02-16** | yes | the last capture carrying CC |
| **2026-03-03** | no | "© 2016-2026 Open Middle Partnership. All rights reserved. Open Middle is the registered trademark of the Open Middle Partnership. Get in contact with us" |
| 2026-05-12 | no | "© 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered trademark of Glenrock Consulting, LLC." |
| 2026-08-08, live | no | same as 2026-05-12 |

Read the 2026-03-03 and 2026-05-12 rows together: the licence left first, the rights-holder
changed after. Wayback captured nothing between 2026-02-16 and 2026-03-03, so the exact removal
date is bounded and not narrowed.

The corrected form to write is: **"Open Middle was CC BY-NC-SA until between 2026-02-16 and
2026-03-03; it is now all rights reserved, rights-holder Glenrock Consulting, LLC."** See
[[source-open-middle]] and [[license-all-rights-reserved]].

### Achieve the Core: a deliberate delink, not a broken link

Wayback CDX and the availability API show `/ccpd` served the public-domain dedication
continuously at these snapshots, all HTTP 200 with the text present: `2016-03-03`, `2017-07-22`,
`2020-04-30`, `2022-01-03`, `2024-03-23`, `2026-01-11`, `2026-04-25`. The latest snapshot
carrying the text is `20260425161111`.

Live on 2026-08-08, `https://achievethecore.org/ccpd` is **140,749 bytes**, byte-identical to the
homepage shell, and "Public Domain Dedication" occurs **0 times**.

The finding that makes this an act rather than an accident is in the live markup. The footer
still contains, commented out and present twice, verbatim:

```
<!-- <li><a href="/ccpd">Permissions</a></li> -->
```

What is live in its place, from `https://achievethecore.org/terms-of-use`, HTTP 200, fetched
2026-08-08, verified two independent ways, verbatim:

> "Some material on Our Site is protected by copyright and some material has been dedicated to
> the public domain. For material protected by copyright, SAP owns or has the right to include
> the material on Our Site. Material may be used as indicated on Our Site for the particular
> material. You may not remove or modify any copyright notices, credit or other attribution
> associated with materials."

The replacement is strictly weaker: per-item rather than blanket, and this project measured the
per-item indication to be usually absent. The corrected form to write is: **"Achieve the Core
carried a blanket public-domain dedication until it was withdrawn between 2026-04-25 and
2026-08-08; what is live is a per-item claim."** See [[source-achieve-the-core-sap]] and
[[license-public-domain-dedication]].

**Byte-size discrepancy carried forward unresolved.** A second staged extract for the same
organisation, from a different agent with fetch date 2026-08-07, records the same homepage shell
as **137,828 bytes** where the extract above records **140,749 bytes**. Both figures are
reproduced as written here. Do not average, reconcile or pick one without a fresh fetch.

### Illustrative Mathematics: mutable, not withdrawn

`https://illustrativemathematics.org/terms-of-use/`, HTTP 200, fetched 2026-08-07, carries the
header **Effective as of May 21, 2026**. That is a dated, replaceable document, and it is the
sole home of the §7.1 grant under which `im.kendallhunt.com` serves the first edition of IM K-12
Math as CC BY 4.0. Its own §6 states, verbatim:

> Except as expressly stated in these Terms or in a separate written license agreement, IM
> reserves all rights in and to its intellectual property. No license or right is granted by
> implication, estoppel, or otherwise.

Nothing has been withdrawn here. What this row records is a state: the strongest source in the
corpus rests on a document that was eleven weeks old at fetch time and that reserves everything
it does not expressly grant. See [[source-im-kendall-hunt]] and [[license-cc-by]].

### The one grant in this corpus that says what happens on withdrawal

Every other licence here is silent about its own end. The NGA Center and CCSSO public licence
over the Common Core standards is not, and it is worth reading against the two withdrawals above.
Recovered verbatim from a Wayback snapshot dated 2025-12-21, because the live path is HTTP 403
behind a Cloudflare JavaScript challenge:

> "NGA Center and CCSSO reserve the right to release the Common Core State Standards under different license terms or to stop distributing the Common Core State Standards at any time; provided, however that any such election will not serve to withdraw this License with respect to any person utilizing the Common Core State Standards pursuant to this License."

Both halves matter. The grantor reserves the right to stop distributing at any time, which is the
mutable state this page is about. And the proviso says an election to do so does not withdraw the
licence from anyone already using it under those terms, which is exactly the assurance neither
Open Middle nor Achieve the Core gives. Where a grant carries such a clause, record it; where it
does not, the question in gotcha 2 stays open. See [[source-corestandards-nga-ccsso]].

### The re-verification trigger

This project's recorded instruction is to re-pull the licence surface for four rows of its
twelve-host table before the repository is published, and to record the new fetch date in the
attribution block. Those rows are `im.kendallhunt.com` and `accessim.org`, both governed by the
dated IM terms, and `openmiddle.com` and `achievethecore.org`, the two hosts that changed. See
[[practice-assemble-an-attribution-block]].

## Gotchas & constraints

**1. The exact dates are windows, and writing a point date falsifies them.** 2026-02-16 to
2026-03-03 for Open Middle; 2026-04-25 to 2026-08-08 for Achieve the Core. Wayback captured
nothing inside the first window. Neither has been narrowed, and neither operator was asked. What
would close them: more granular archive queries, or asking the operators directly.

**2. Whether material obtained under a withdrawn grant is still usable is a legal question, and
this project did not answer it.** It arises twice. For Achieve the Core, a public-domain
dedication is generally understood to be irrevocable, and CC0's own legal code uses the word
`irrevocably`, but validity, scope and the publication date of each item are facts nobody could
fetch. This project's verdict table calls it, in its own words, the single most consequential open
question in the corpus. For Open Middle, CC 4.0's own text describes the grant as irrevocable,
but whether that helps material accessed today, when no CC offer is extended, is recorded as a
counsel question rather than a research finding. The safe posture is the one that does not depend
on the answer: cite and link, write your own prose.

**3. Withdrawal is not the only way a grant becomes unreliable.** A rights-holder transfer changes
whom you attribute and whom you would ask, without touching the licence text. Open Middle's
transfer to Glenrock Consulting, LLC is exactly this, and an attribution string written in
February 2026 names an entity that no longer holds the mark. Merging the transfer into the
licence removal produces a wrong date for both. See [[concept-chain-of-title]].

**4. A grep for the grant on a Wayback raw capture will lie to you.** The Achieve the Core agent
recorded the near-miss verbatim:

> METHOD WARNING recorded: my first pass at this snapshot used wayback `id_` raw mode WITHOUT
> `--compressed`. curl returned gzip bytes; grep found 0 matches; I nearly reported "CC0 already
> gone by April 2026". That was an artifact of binary, not a finding. Re-fetched with --compressed
> -> 1 match. Never grep a possibly-compressed body.

The Open Middle agent hit the same thing on the 2026-03-03 snapshot, where it briefly appeared to
show no footer at all. Both re-fetched before concluding. See
[[trap-compressed-body-grepped-as-text]].

**5. This register is not a census, and no host announced anything.** It records the changes two
agents happened to catch by running an archive comparison where something looked wrong. This
project's own sampling note records that **no Wayback cross-check was run** on the live hosts
(`im.kendallhunt.com`, `tasks.illustrativemathematics.org`, `accessim.org`, `map.mathshell.org`,
`learningcommons.org`), because the archive step was conditioned on a site being dead or blocked.
So for those hosts, when the current footer was introduced and whether earlier snapshots carried
different terms is unknown. Two withdrawals is a floor, not a count, and re-fetching is the only
detection method available.

**6. The IM sole-discretion clause is unverified as text, and is named here as unverified.**
This project's own adjudication records that §4 of IM's Terms reserves revision at IM's sole
discretion, and that reading is repeated across its working files. **No agent pasted the §4
sentence.** What is verbatim and staged is the header "Effective as of May 21, 2026" and the §6
reservation of rights quoted above. What would close it: re-fetch
`https://illustrativemathematics.org/terms-of-use/` and paste §4. Until then, treat the
mutability of that document as evidenced by its own dated header, which is sufficient for the
re-verification trigger, and do not quote a clause nobody has pasted.

## Related

- [[trap-license-withdrawn-after-citation]] owns the mechanism: a stale citation renders identically to a fresh one, which is why nothing flags it. This page owns the dated record it is checked against.
- [[license-public-domain-dedication]] holds the instrument Achieve the Core withdrew and the irrevocability doctrine this page does not settle.
- [[license-all-rights-reserved]] is the state Open Middle is in now, and why the string sat in that footer throughout the licensed decade too.
- [[license-unmarked-silence]] is what an unmarked artifact becomes once the grant above it is gone, with no byte of the artifact changing.
- [[license-sharealike]] is the regime Open Middle used to carry.
- [[license-cc-by]] is the grant IM's mutable terms currently publish, and the one the re-verification trigger most protects.
- [[concept-chain-of-title]] is the rights-holder transfer as an event distinct from the licence change.
- [[source-open-middle]] is the host verdict holding the full footer table and the ten per-resource checks.
- [[source-achieve-the-core-sap]] is the host verdict holding the archived Permissions page and the commented-out footer link.
- [[source-im-kendall-hunt]] is the host whose grant lives in the dated, revisable off-host terms.
- [[source-corestandards-nga-ccsso]] is the one grant here that addresses its own withdrawal in writing.
- [[trap-soft-404-status-proves-nothing]] is why a withdrawn page can return HTTP 200 forever.
- [[trap-compressed-body-grepped-as-text]] is the fetch artifact that nearly turned both findings into false ones.

## Composes with

- [[practice-build-a-source-table]] is where a fetch date becomes a required column, and where the archive comparison that produced both rows of this register is a documented step.
- [[practice-assemble-an-attribution-block]] consumes the re-verification trigger: every entry carries its fetch date, and four get re-pulled before publication.
- [[practice-cite-without-redistributing]] is the posture that survives a withdrawal unchanged, and why a withdrawn grant costs this build reuse rather than access.

## References

Host pages, live and archived:

- `https://www.openmiddle.com/` HTTP 200 with a browser user agent, HTTP 406 with the default agent, fetched 2026-08-08. The current footer with no Creative Commons string anywhere on the root, the category page, the embedding page or any of the 10 problem pages.
- Wayback `id_` raw captures of `openmiddle.com`, snapshots 2016-05-27, 2019-06-03, 2023-06-01, 2026-01-09, 2026-02-16, 2026-03-03 and 2026-05-12, fetched `--compressed` on 2026-08-08. The dated footer table above.
- `https://achievethecore.org/ccpd` HTTP 200, 140,749 bytes, fetched 2026-08-08, byte-identical to the homepage shell with "Public Domain Dedication" occurring 0 times.
- `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd` HTTP 200. The last archived capture carrying the dedication, and the snapshot series 2016-03-03 through 2026-04-25 behind it.
- `https://achievethecore.org/terms-of-use` HTTP 200, fetched 2026-08-08. The per-item Copyright section that replaced the blanket dedication.
- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, fetched 2026-08-07. Header "Effective as of May 21, 2026", and §6 reservation of rights.
- `https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/` HTTP 200, fetched 2026-08-08. The CCSS Public License, including its re-release and non-withdrawal clause; the live path is HTTP 403 behind a Cloudflare JavaScript challenge.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-open-middle.md`, primary. Section 5, the dated footer table bounding both events, and the method note on decompressing raw `id_` captures before grepping.
- `sources/host-achieve-the-core.md`, primary. Section 4, the snapshot series, the removal window, the commented-out footer link, and section 4c the method warning verbatim.
- `sources/host-im-kendall-hunt.md`, primary. Section 6, the dated terms header and the §6 reservation clause.
- `sources/host-learning-commons-kg.md`, primary. Section 9, the CCSS Public License verbatim and the HTTP 403 reachability table.
- `sources/cc0-1-0.md`, primary. The `irrevocably` language in the Waiver, and the extract's own statement that it cannot date any host's dedication.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: rows 10 and 11, §3 corrections 3, 8 and 12, §6 "Not closeable by fetching", the sampling limits, and the re-verification trigger.

The underlying fetch reports, cited as this project's own measurement and not as any outside
party's statement: `Projects/HS Geometry/sources/license-open-middle.md` (§5, §8),
`Projects/HS Geometry/sources/license-achieve-core.md` (§4, §8), and
`Projects/HS Geometry/sources/source-verdict-table.md` (§3 and §6).
