---
title: "achievethecore.org and learnwithsap.org (Student Achievement Partners)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://achievethecore.org/terms-of-use
  - https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd
  - https://learnwithsap.org/permissions/
  - https://learnwithsap.org/e2-tools-terms-of-use/
  - https://tools.achievethecore.org/coherence-map/data.js
  - https://creativecommons.org/publicdomain/zero/1.0/
  - sources/host-achieve-the-core.md
  - sources/host-learnwithsap.md
  - sources/cc0-1-0.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# achievethecore.org and learnwithsap.org (Student Achievement Partners)

## Summary

Student Achievement Partners runs two domains. `achievethecore.org` carried a blanket public-domain
dedication for years and **no longer publishes one**. `learnwithsap.org` still does, and its wording
covers that domain alone. Verdict for the family: `cite_only`. ATC fetches are 2026-08-08;
learnwithsap.org fetches are 2026-08-07.

**The folk claim this page exists to kill is "Achieve the Core is CC0."** It was true for years and
it is not true of the live site. Two measurements together are what license the word *withdrawn*
rather than *broken*:

1. `https://achievethecore.org/ccpd`, the Permissions page that carried the dedication, is now
   byte-identical to the homepage shell, and `"Public Domain Dedication"` occurs **0 times** on it.
2. The live footer markup still contains the link to it, **inside an HTML comment, present twice**,
   verbatim:

   ```
   <!-- <li><a href="/ccpd">Permissions</a></li> -->
   ```

A soft-404 on its own is consistent with rot. A link an editor wrapped in a comment and left in
place is an act. The Wayback record dates it: `/ccpd` served the dedication text at snapshots on
2016-03-03, 2017-07-22, 2020-04-30, 2022-01-03, 2024-03-23, 2026-01-11 and 2026-04-25, the last of
these being `20260425161111`. **Removal window: between 2026-04-25 and 2026-08-08.**

**Do not write "CC0" unqualified about either domain.** The instrument named on the archived ATC
page and on the live learnwithsap page is `the Creative Commons Public Domain Dedication License`,
with no version stated and no link to creativecommons.org anywhere on either page. CC0 1.0 is the
obvious intent and it is an inference, not a reading. See
[[license-public-domain-dedication]].

**The two domains are one owner and the finding is the boundary between them**, which is why they
share a page. SAP's own trademark clause claims "Achieve the Core" and "achievethecore.org" on both
domains' terms pages. The surviving dedication says, by its own words, "All of the content on
**learnwithsap.org**". ATC's own `/permissions` is a soft-404. Whether the dedication reaches the
math library, which lives on ATC, is unresolved. A reader who lands on only one of the two halves
re-derives the wrong answer, and that is how the CC0 belief survived.

## When to reach for it

Reach for it for the **Coherence Map**, which is the genuinely useful and hard-to-replicate asset:
a prerequisite graph, cluster and progression narrative, and CCSSM Progressions page pointers. All
five target standards are present in `tools.achievethecore.org/coherence-map/data.js`, keyed by
numeric id rather than by code string, with the linked-task counts as recorded:

| id | Standard | Linked tasks |
|---|---|---|
| 612 | HSG-SRT.B.4 | 1 |
| 613 | HSG-SRT.B.5 | 5 |
| 614 | HSG-SRT.C.6 | 6 |
| 615 | HSG-SRT.C.7 | 1 |
| 616 | HSG-SRT.C.8 | 3 |

Reach for it as a **pointer service, not a content source**. Every one of those five carries
`"example_problem_attribution":"Provided by Illustrative Mathematics"`, every `example_problem_url`
points at IM's S3 bucket, and every linked task points off-site to an IM domain. The Coherence Map
page itself shows no licence, copyright or permission text at all.

Do **not** reach here for a task or an assessment item. The measured gap:
`/category/416/mathematics-tasks` shows "Results (31)" with **zero G-SRT items**, and
`/category/1020/mathematics-assessments` shows "Results (24)" with **zero G-SRT items**. Both
listings are K-8 dominated and the only HS math items seen are Algebra. On the other domain, the
learnwithsap.org resources post type holds 46 items and a WordPress API search for "trigon", "HSG"
and "pythagorean" returns **zero**; the single HS geometry item is a distance-formula SEAD lesson on
G.CO.A.1 and G.GPE.B.7, not SRT.

**Do not launder IM tasks through this host.** The material for these five standards is Illustrative
Mathematics content presented without its licence. Source it and clear it at IM, where it carries
ShareAlike; see [[source-im-task-bank]].

## What its own page says

Quotations below are transcribed from two staged extracts written by two different agents,
`sources/host-achieve-the-core.md` (ATC, fetched 2026-08-08) and `sources/host-learnwithsap.md`
(learnwithsap.org and the ATC boundary, fetched 2026-08-07). Where the two disagree on a
measurement, both figures are reproduced and neither is reconciled; see gotcha 8.

### The live ATC terms, which decline a single licence

`https://achievethecore.org/terms-of-use`, HTTP 200, 2026-08-08, verified two independent ways
(WebFetch plus raw curl and strip). Section "Copyright", verbatim:

> "Some material on Our Site is protected by copyright and some material has been dedicated to
> the public domain. For material protected by copyright, SAP owns or has the right to include
> the material on Our Site. Material may be used as indicated on Our Site for the particular
> material. You may not remove or modify any copyright notices, credit or other attribution
> associated with materials."

That last clause makes **per-resource marking the operative grant**. Section "Trademarks",
verbatim:

> "Our name and our trademarks and service marks, including "Achieve the Core" and
> "achievethecore.org," logos, and other indicia of source are owned by SAP (collectively,
> "Our Trademarks"). You may not use Our Trademarks without our prior written consent in each
> case..."

Section "Links, Frames and Metatags", verbatim:

> "You may not "frame" the content of Our Site on any other web site (display Our Site inside
> the window or browser of another site) unless you first obtain our prior written consent in
> each case."

The same Copyright clause appears word for word on `https://learnwithsap.org/terms-of-use/`, page
"Published July 16, 2024". ATC's version carries one extra sentence, a clickwrap, verbatim:

> "By clicking "I agree" you consent to the Privacy Statement and Terms of Use; to access certain
> portions of Our Site, you must register and indicate agreement to additional terms."

Those additional terms were never read: no agent registered.

### The withdrawn dedication, and what it said

The 2016 Permissions page, `web.archive.org/web/20160303204431/http://achievethecore.org/ccpd`,
HTTP 200, 37,273 bytes. Verbatim:

> "The person who associated a work with this deed has dedicated the work to the public domain by
> waiving all of his or her rights to the work worldwide under copyright law, including all related
> and neighboring rights, to the extent allowed by law. You can copy, modify, distribute and perform
> the work, even for commercial purposes, all without asking permission. Click here for more
> information."

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain
> Dedication License unless it is marked with the (c), which indicates that it includes content that
> has been licensed to Student Achievement Partners, Inc., from third parties and must be used solely
> as noted when hovering over the (c) next to the applicable content."

The last snapshot carrying it, `web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd`,
HTTP 200. Note that this 2026 transcription uses the `©` character where the 2016 transcription used
`(c)`:

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain
> Dedication License unless it is marked with the ©, which indicates that it includes content that
> has been licensed to Student Achievement Partners, Inc., from third parties and must be used
> solely as noted when hovering over the © next to the applicable content."

Live on 2026-08-08: that URL returns the homepage shell and the phrase is gone.

### The surviving dedication, on the other domain

`https://learnwithsap.org/permissions/`, HTTP 200 with a browser user agent, page "Published July
16, 2024". Full body text of the page, both paragraphs, verbatim:

> "The person who associated a work with this deed has dedicated the work to the public domain by
> waiving all of his or her rights to the work worldwide under copyright law, including all related
> and neighboring rights, to the extent allowed by law."

> "All of the content on learnwithsap.org is covered by the Creative Commons Public Domain Dedication
> License unless it is marked with the ©, which indicates that it includes content that has been
> licensed to Student Achievement Partners, Inc., from third parties."

The first paragraph is the standard CC0 1.0 deed summary text. **A grep for `creativecommons` on
that page returns zero hits.** No version, no deed link. Note also what the 2026 ATC snapshot had
that this page does not: the sentence "You can copy, modify, distribute and perform the work, even
for commercial purposes, all without asking permission" is present in the archived ATC text quoted
above and absent from the live learnwithsap body.

### The e² rider, which is the opposite of a dedication

`https://learnwithsap.org/e2-tools-terms-of-use/`, HTTP 200, "Last updated: Sep 8, 2025". Verbatim:

> "All e² Tools and related materials are the intellectual property of SAP. SAP retains all rights,
> title, and interest in these materials, including any updates or modifications."
> "SAP grants you a limited, non-exclusive, non-transferable, revocable license to: Download and use
> the e² Tools for internal, non-commercial educational purposes within your school, district, or
> organization. Share the unmodified files internally (e.g., within a private LMS, shared drive, or
> PLC) provided this Terms of Use notice and copyright footer remain intact."
> "You may not: Post or redistribute the e² Tools publicly (including websites, social media,
> marketplaces, or AI training datasets). Modify, adapt, translate, or create derivative works from
> the e² Tools without SAP's prior written permission. Use the e² Tools for commercial purposes,
> including resale, fee-based training, or incorporation into paid platforms."
> "When using or sharing the e² Tools internally, you must include the following attribution:
> "© 2025 Student Achievement Partners. e² Instructional Practice Framework and e² Tools used with
> permission." Any public use (e.g., presentations, publications, or conference materials) requires
> prior written consent from SAP and must include mutually approved attribution language."
> "© 2025 Student Achievement Partners, Inc. All rights reserved."

A separate platform, SAP Instructional Insights, is login-gated and stricter still.
`https://learnwithsap.org/sap-instructional-insights-terms-of-use/`, HTTP 200, "Effective Date:
Jul 16, 2025", verbatim:

> "All content, tools, and insights available within the platform are confidential and proprietary to
> SAP. You agree not to: Copy, download, or redistribute platform content; Use the platform for any
> public-facing report or presentation; Refer to the platform or SAP in marketing, publications, or
> media without written permission"

### The © test, measured against a real file, fails

Sample: `https://achievethecore.org/page/620/equations-of-lines`, an IM-authored task with a SAP
annotation layer, whose PDF is hosted on achievethecore.org. `pdftotext` of that PDF, verbatim by
line as recorded:

> line 3:   "Task by Illustrative Mathematics, annotation by Student Achievement Partners"
> line 148: "Typeset May 4, 2016 at 22:05:25. Licensed by Illustrative Mathematics under a"
> line 149: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ."
> line 172: "8.EE Equations of Lines is licensed by Illustrative Mathematics"
> line 173: "under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License"

The recorded consequence, verbatim:

> **The © heuristic from /permissions/ FAILS HERE.** The PDF contains no "©" character anywhere (measured: zero hits). Per the permissions page's own rule this file would read as public domain. It is not. => "unless it is marked with the ©" is NOT a reliable test for third-party content.

The same file also states **two different CC versions**, 4.0 International and 3.0 Unported, which
the report records as "genuinely ambiguous on the face of the document".

Two other per-resource samples were opened on ATC and neither carried any notice at all: a
SAP-authored quadratic-equations mini-assessment and a SAP-authored functions mini-assessment. The
recorded verdict across the three, verbatim:

> "VARIES PER RESOURCE, and most items are simply UNMARKED. The current site publishes no blanket grant, and the per-item marking the Terms points to is frequently absent."

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state which standard a Coherence Map node addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | **no** | no live grant reaches the material this unit needs |
| Paraphrase and republish: rewrite its material and ship it | **no** | same |

The verdict is not a reading of a restrictive licence. It is the consequence of there being **no
locatable affirmative grant** over the material in scope, which is a different situation and has a
different fix: find the rights-holder, which here is Illustrative Mathematics.

Work the decision in this order:

1. **Which domain is the artifact served from?** The live dedication covers `learnwithsap.org` by
   its own words. Nothing live covers `achievethecore.org`.
2. **Who authored it?** Every Coherence Map example problem for the five target standards is
   attributed to Illustrative Mathematics, and the one ATC-hosted math PDF that carries any licence
   at all is CC BY-NC-SA. SAP's dedication cannot reach material SAP did not author; see
   [[concept-chain-of-title]].
3. **Do not use the © mark as the test.** It is measurably broken, in the direction that matters:
   a file with no © read as public domain when it was ShareAlike.
4. **Is it an e² tool or an Instructional Insights artifact?** Those carry explicit
   all-rights-reserved terms with no public redistribution, no derivatives, and an express bar on
   AI training datasets.

### Citation form

```
Achieve the Core (Student Achievement Partners). Coherence Map, standard <code>.
https://tools.achievethecore.org/coherence-map/  · Accessed 2026-08-08.
```

Where the substance being cited is an IM task surfaced by the Coherence Map, **cite it to
Illustrative Mathematics and to the IM host it came from**, not to SAP. SAP redistributes the full
task text and solution with an attribution string and no licence statement, so a user relying on
SAP's presentation could never learn the ShareAlike obligation exists.

Two obligations survive the absence of a grant. The Terms bar removing or modifying any copyright
notice, credit or attribution associated with materials. And "Achieve the Core" and
"achievethecore.org" are trademarks requiring prior written consent, so they may be named as a
source in ordinary nominative use and not used in any way implying endorsement. See
[[concept-third-party-carve-out]].

If the dedication is ever relied on for learnwithsap.org content, note what CC0 does and does not
require. The staged CC0 1.0 extract is explicit that there is **no attribution condition**: the
deed states none and the legal code states none. What remains is a caution, verbatim: "When using
or citing the work, you should not imply endorsement by the author or the affirmer." That is
`should not`, grounded in general law, and it is not a duty to credit. Citation here is scholarly
practice, never licence compliance.

## Gotchas & constraints

**1. "Withdrawn" is a claim with two legs, and both were measured.** The soft-404 alone would be
consistent with a broken route. The commented-out footer link, present twice in the live markup, is
what makes it an intentional delinking. Anyone re-verifying this should check both, and record the
snapshot timestamp `20260425161111` as the last known live text. See
[[trap-license-withdrawn-after-citation]] and [[license-withdrawn-grants]].

**2. The evidence file's own vocabulary is looser than its evidence.** It uses the label "CC0"
throughout, while the text it quotes from both the live terms and the archived Permissions page
never uses that string. The quoted instrument name is "Creative Commons Public Domain Dedication
License", with no version and no deed link recorded on either domain. **The version is unverified
from these sources.** Reproducing the label without that caveat is the error the retired-vocabulary
rule exists to stop.

**3. Every URL returns HTTP 200 on achievethecore.org.** Unknown paths return an identical homepage
shell. `/page/terms-of-use` is a shell and `/terms-of-use` is the real page at 93,954 bytes; the
evidence file records this as the reason an earlier fetch "found no licensing statement", because it
was reading the homepage. Existence has to be tested by byte size or content comparison. See
[[trap-soft-404-status-proves-nothing]].

**4. learnwithsap.org is a Cloudflare bot block, not a dead host.** WebFetch with the default agent
returns **HTTP 403**; `curl` with a browser user agent returns **HTTP 200** at 305,636 bytes. ATC
needed no such workaround. Recording a 403 as unavailability would have lost the only live
dedication in the family. See [[trap-down-is-not-one-state]].

**5. A grep over a compressed body nearly produced a false withdrawal date.** Recorded verbatim:

> METHOD WARNING recorded: my first pass at this snapshot used wayback `id_` raw mode WITHOUT `--compressed`. curl returned gzip bytes; grep found 0 matches; I nearly reported "CC0 already gone by April 2026". That was an artifact of binary, not a finding. Re-fetched with --compressed -> 1 match. Never grep a possibly-compressed body.

See [[trap-compressed-body-grepped-as-text]].

**6. Font metadata is not a content licence, and this host is where it bites.** The only "All Rights
Reserved" strings in the ATC quadratic-equations PDF are embedded Microsoft Calibri notices; the only
"MIT License" string on another ATC page is a normalize.css library comment. Both are keyword-grep
hits and neither is a rights determination. See [[trap-font-notice-is-not-a-content-license]].

**7. The Coherence Map's example problems for two of the five standards were checked for licence
text and there is none.** A regex over the decoded inline HTML for ids 614 and 616 returned zero
occurrences of "licen", "creative commons", "©" or "copyright". The `example_problem_url` values for
ids 612 to 616 all point at IM's S3 bucket over plain `http://` inside an `https://` page, so they
are mixed content, and a fetch of one of them timed out with no HTTP response on every attempt. The
recorded discipline on that failure, verbatim: "the specific object does not answer. I could NOT
distinguish "bucket deleted" from "blackholed". NOT reported as a 404." Ids 617 and 618, SRT.D.10 and
D.11, have empty attribution and empty example task.

**8. Three measurements disagree across the two agents, and this page does not reconcile them.**
Both figures are reproduced as written, and none should be averaged or picked without a fresh fetch.

| What | 2026-08-08 extract | 2026-08-07 extract |
|---|---|---|
| ATC homepage shell | 140,749 bytes | 137,828 bytes |
| `/page/620/equations-of-lines` | 110,460 bytes | 113,219 B |
| `/category/1020` listing | "Results (24)" | 28 items |

The listing figures were also taken through different surfaces, and `/category/416` is paginated and
filtered client-side, with one agent recording that it saw 35 links of an unknown total.

**9. GitHub carries no grant either.** The footer's "For Developers" link goes to
`https://github.com/achievethecore`, whose four repos (`atc-academic-word-finder`,
`atc-coaching-tool`, `atc-lesson-planner`, `atc-coherence-map`) all return `license: null` with no
LICENSE file. An open repository is not a licensed one. See [[license-unmarked-silence]].

**10. What is still unresolved, stated plainly.** Whether the learnwithsap.org dedication extends to
achievethecore.org, recorded verbatim as "This is a real gap". Which version of the public-domain
instrument is meant. Whether any specific SRT artifact is © marked, the Coherence Map having no ©
field at all. Whether the IM S3 example-task PDFs are dead or merely unreachable. The full ATC task
library and all 46 learnwithsap resources were never enumerated, and `learnwithsap.com` and
`.net`, both HTTP 200 at approximately 27KB, were not investigated. Closing the first of these needs
a written answer from SAP, not another fetch.

## Related

- [[license-public-domain-dedication]] is the instrument as it actually appears here, unversioned
  and unlinked, against CC0 1.0 as it actually reads.
- [[license-withdrawn-grants]] is the dated register this host's removal window belongs to.
- [[license-unmarked-silence]] is the modal state of resources on this host, and of its repositories.
- [[license-sharealike]] is what the one marked math resource actually carries, and what the
  Coherence Map does not surface.
- [[source-im-task-bank]] is where the material this host points at actually lives, under
  CC BY-NC-SA 4.0.
- [[source-open-middle]] is the other grant withdrawn inside this corpus's six-month window.
- [[concept-chain-of-title]] is the mechanism: a host presenting material it did not author and
  cannot license.
- [[concept-third-party-carve-out]] covers the trademark and the third-party material the dedication
  never reached, even in 2016.
- [[trap-license-withdrawn-after-citation]] is the mechanism page for a grant that moves under a
  citation that does not.
- [[trap-soft-404-status-proves-nothing]] is the SPA shell on this host.
- [[trap-down-is-not-one-state]] is the 403-versus-dead distinction on learnwithsap.org.
- [[trap-compressed-body-grepped-as-text]] is the near-miss on the Wayback snapshot.
- [[trap-font-notice-is-not-a-content-license]] is the Calibri false positive measured here.
- [[source-mars-map]] is the other host in this batch where an artifact and its page disagree about
  rights, by a different mechanism.

## Composes with

- [[practice-build-a-source-table]] is the procedure that produced this verdict, and the Wayback
  dating step in gotcha 1 is how a withdrawal is turned into a window rather than an impression.
- [[practice-cite-without-redistributing]] is how the Coherence Map's prerequisite graph shapes
  sequencing without any SAP or IM expression entering the repo.

## References

Live and archived pages, fetched by this project on the dates given:

- `https://achievethecore.org/terms-of-use` HTTP 200, 93,954 bytes, 2026-08-08. The Copyright,
  Trademarks and Links/Frames/Metatags clauses.
- `https://achievethecore.org/ccpd` HTTP 200, 140,749 bytes, 2026-08-08. The homepage shell, with
  "Public Domain Dedication" occurring 0 times.
- `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd` HTTP 200,
  2026-08-08. The last snapshot carrying the blanket dedication.
- `https://web.archive.org/web/20160303204431/http://achievethecore.org/ccpd` HTTP 200, 37,273
  bytes, 2026-08-08. The 2016 Permissions page.
- `https://learnwithsap.org/permissions/` HTTP 200 with a browser user agent, 2026-08-07. The
  surviving dedication, "Published July 16, 2024".
- `https://learnwithsap.org/terms-of-use/`, `/e2-tools-terms-of-use/` and
  `/sap-instructional-insights-terms-of-use/`, all HTTP 200, 2026-08-07.
- `https://tools.achievethecore.org/coherence-map/data.js` HTTP 200, 2,296,445 bytes, 2026-08-08.
- `https://achievethecore.org/page/620/equations-of-lines` and its attached PDF, HTTP 200. The
  broken-© sample and the internally inconsistent version statement.
- `https://creativecommons.org/publicdomain/zero/1.0/` HTTP 200, 30476 bytes, and its `legalcode.en`
  HTTP 200, 32451 bytes, fetched 2026-08-08.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-achieve-the-core.md`, primary. The SPA soft-404 method, the live terms, the
  Wayback dating of the removal window, the commented-out footer link, the three per-resource
  samples, the Coherence Map ids and the measured G-SRT gap.
- `sources/host-learnwithsap.md`, primary. The identity test, the Cloudflare 403, the surviving
  dedication, the e² and Instructional Insights riders, the failure of the © test, and the
  measured absences.
- `sources/cc0-1-0.md`, primary. CC0 1.0 deed and legal code verbatim, including the absence of any
  attribution condition and the waiver-then-fallback structure the deed does not describe.
- `sources/verdict-twelve-host-table.md`, reference. Rows 11 and 12, §3 corrections 3, 4 and 7, and
  §4.10 the cite-only bibliographic form.

This project's own working files, cited as this project's measurement and not as any outside party's
statement: `Projects/HS Geometry/sources/license-achieve-core.md` and
`Projects/HS Geometry/sources/license-learnwithsap.md`, the two underlying fetch reports.
