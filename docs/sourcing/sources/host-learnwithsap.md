---
source_url: hs-geometry-similarity-trig/sources/license-learnwithsap.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-achieve-the-core-sap, license-public-domain-dedication, concept-third-party-carve-out, concept-chain-of-title, trap-down-is-not-one-state, trap-access-is-not-a-rights-fact
---

# Host extract: learnwithsap.org (Student Achievement Partners), with the achievethecore.org boundary

**Original fetch dates recorded by the evidence file: all fetches 2026-08-07**, with the server
date header reading UTC 2026-08-08. The `fetched:` field above is the staging date.

**Method recorded by the evidence file:** WebFetch first; on 403, retried with a browser user
agent via curl.

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Identity, as tested

Recorded measurements:

- DNS: `learnwithsap.com`, `.org` and `.net` all resolve (Cloudflare). `.io`, `.co.uk` and `.in`
  do not resolve.
- `learnwithsap.org` returns HTTP 200 with `<title>Home - Student Achievement Partners</title>`.
- SAP here means **Student Achievement Partners, Inc.**, 228 Park Avenue South #96810, New York
  NY 10003-1502. The evidence file records explicitly that this is NOT SAP SE the German
  software company, and that `learning.sap.com` is a different, unrelated org.
- `learnwithsap.org` is a WordPress site with the wp-json REST API open.
- The same org owns `achievethecore.org`, recorded as proven by their own Terms of Use, which
  claims "Achieve the Core" and "achievethecore.org" as SAP trademarks. `achievethecore.org` is
  live at HTTP 200.
- `learnwithsap.com` and `learnwithsap.net` also return HTTP 200 at approximately 27KB, recorded
  as much smaller and not investigated further.

## 2. Bot block, distinguished from a dead host

- `WebFetch https://learnwithsap.org/` returned **HTTP 403 Forbidden** with the default agent UA.
- `curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" https://learnwithsap.org/`
  returned **HTTP 200**, 305,636 bytes.
- Recorded reading: a Cloudflare-fronted UA bot block on the default fetcher. The site is fully
  alive. All findings in the evidence file come from browser-UA curl.
- `achievethecore.org` did not need the UA workaround for curl and returned 200 directly.

## 3. The license, verbatim

### 3a. https://learnwithsap.org/permissions/

HTTP 200, page states "Published July 16, 2024". Full body text of the page, verbatim, both
paragraphs:

> "The person who associated a work with this deed has dedicated the work to the public domain by
> waiving all of his or her rights to the work worldwide under copyright law, including all related
> and neighboring rights, to the extent allowed by law."

> "All of the content on learnwithsap.org is covered by the Creative Commons Public Domain Dedication
> License unless it is marked with the ©, which indicates that it includes content that has been
> licensed to Student Achievement Partners, Inc., from third parties."

Recorded measured caveat, preserved as the uncertainty it is: the first paragraph is the standard
CC0 1.0 deed summary text, but the page carries no hyperlink to creativecommons.org at all. A
grep for `creativecommons` in the page HTML returns ZERO hits. So the CC0 version (1.0) is never
stated and never linked. The words "Creative Commons Public Domain Dedication License" are the
whole grant.

Recorded alongside: this contradicts the common belief that Achieve the Core and SAP content is
CC BY-NC-SA 4.0. The live permissions page says public domain dedication.

### 3b. https://learnwithsap.org/terms-of-use/

HTTP 200, "Published July 16, 2024".

Copyright clause, verbatim:

> "Some material on Our Site is protected by copyright and some material has been dedicated to the
> public domain. For material protected by copyright, SAP owns or has the right to include the material
> on Our Site. Material may be used as indicated on Our Site for the particular material. You may not
> remove or modify any copyright notices, credit or other attribution associated with materials."

Trademark clause, verbatim:

> "Our name and our trademarks and service marks, including "Achieve the Core" and "achievethecore.org,"
> logos, and other indicia of source are owned by SAP (collectively, "Our Trademarks"). You may not use
> Our Trademarks without our prior written consent in each case, including in any manner that implies we
> sponsor, endorse or are otherwise the source of or affiliated with a product, service, entity, or
> activity or that would be likely to cause confusion among the public."

Framing clause, verbatim:

> "You may not "frame" the content of Our Site on any other web site (display Our Site inside the window
> or browser of another site) unless you first obtain our prior written consent in each case."

Also recorded: governing law New York; exclusive jurisdiction New York state and federal courts;
liability cap US$100.

### 3c. https://achievethecore.org/terms-of-use

HTTP 200. Recorded as carrying the same Copyright clause word for word as 3b:

> "Some material on Our Site is protected by copyright and some material has been dedicated to the
> public domain. For material protected by copyright, SAP owns or has the right to include the material
> on Our Site. Material may be used as indicated on Our Site for the particular material. You may not
> remove or modify any copyright notices, credit or other attribution associated with materials."

Extra sentence recorded as present on achievethecore.org but not on learnwithsap.org, a
clickwrap:

> "By clicking "I agree" you consent to the Privacy Statement and Terms of Use; to access certain
> portions of Our Site, you must register and indicate agreement to additional terms."

### 3d. achievethecore.org has no reachable permissions page, measured

- `https://achievethecore.org/permissions` returns HTTP 200 but the body is byte-identical to
  the homepage, recorded here as **137,828 bytes**, `<title>Achievethecore.org</title>`. A soft
  404.
- The same holds for `/license` and `/copyright`; all three files are recorded as `cmp`-identical
  to `atc-root.html`.
- The ATC footer markup still contains the text "Permissions" but the link is inside an HTML
  comment, with `-->` fragments visible in the rendered tail. Recorded reading: the permissions
  statement has been moved to `learnwithsap.org/permissions/`.

**Byte-size discrepancy to carry forward, not resolved here.** The companion staged extract
`host-achieve-the-core.md` (different agent, fetch date 2026-08-08) records the same
achievethecore.org homepage shell as **140,749 bytes**. Both figures are reproduced as written.
Do not average, reconcile or pick one without a fresh fetch.

## 4. Riders, as enumerated by the evidence file

### Rider A: the © carve-out, from 3a

Anything "marked with the ©" is third-party-licensed to SAP and is not under the public-domain
dedication. Recorded: the mark is the only signal, there is no list, and it must be checked per
artifact.

### Rider B: e² Instructional Practice Suite, all rights reserved, NC and ND and no public redistribution

`https://learnwithsap.org/e2-tools-terms-of-use/`, HTTP 200, "Last updated: Sep 8, 2025".
Verbatim:

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

### Rider C: SAP Instructional Insights platform, confidential and proprietary, login-gated

`https://learnwithsap.org/sap-instructional-insights-terms-of-use/`, HTTP 200, "Effective Date:
Jul 16, 2025". Verbatim:

> "All content, tools, and insights available within the platform are confidential and proprietary to
> SAP. You agree not to: Copy, download, or redistribute platform content; Use the platform for any
> public-facing report or presentation; Refer to the platform or SAP in marketing, publications, or
> media without written permission"

### Rider D: trademark

From 3b. "Achieve the Core" and "achievethecore.org" may not be used without written consent in
any way implying endorsement. Recorded: the public-domain content grant does not carry a
trademark grant.

### Rider E: no framing

From 3b. Their pages cannot be iframed into another site.

## 5. Per-resource samples, and the failure of the © test

All fetched 2026-08-07 local, server date header `Sat, 08 Aug 2026 01:47 GMT`.

### Sample 1, Ratios and Rates Mini-Assessment, SAP-authored

Page: `https://achievethecore.org/page/1051/ratios-and-rates-mini-assessment`, HTTP 200,
110,014 B.
PDF: `https://achievethecore.org/content/upload/6.RP.A%20Ratios%20and%20Rates.pdf`, HTTP 200,
379,893 B.

Recorded finding: no per-resource notice of any kind. `pdftotext -layout` gives 20,965 chars
containing ZERO occurrences of "copyright", "©", "licen", "Creative", "public domain", or
"rights reserved". The only byline, verbatim: "6.RP.A Application Mini-Assessment by Student
Achievement Partners". The page HTML likewise carries no notice; the footer's "Permissions" text
sits inside an HTML comment.

### Sample 2, Equations of Lines task, third-party

Page: `https://achievethecore.org/page/620/equations-of-lines`, HTTP 200, **113,219 B**.
PDF: `https://achievethecore.org/content/upload/Grade%208%20IM%20task%20-%20equations%20of%20lines%20final06.26.14.pdf`,
HTTP 200, 247,201 B, hosted on achievethecore.org.

Verbatim from the PDF cover: "Sample task from achievethecore.org / Task by Illustrative
Mathematics, annotation by Student Achievement Partners"

Verbatim from inside the same PDF, two different license lines on different pages:

> "8.EE Equations of Lines Typeset May 4, 2016 at 22:05:25. Licensed by Illustrative Mathematics under
> a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License."

> "8.EE Equations of Lines is licensed by Illustrative Mathematics under a Creative Commons
> Attribution-NonCommercial-ShareAlike 3.0 Unported License"

Recorded findings:

- (a) A file served from achievethecore.org is CC BY-NC-SA, not public domain. The site-wide
  dedication does not reach it.
- (b) The PDF is internally inconsistent: 4.0 International in one place, 3.0 Unported in
  another.
- (c) Verbatim: "**The © heuristic from /permissions/ FAILS HERE.** The PDF contains no "©"
  character anywhere (measured: zero hits). Per the permissions page's own rule this file would
  read as public domain. It is not. => "unless it is marked with the ©" is NOT a reliable test
  for third-party content."

**Page byte-size discrepancy to carry forward, not resolved here.** The companion staged extract
`host-achieve-the-core.md` records the same page `/page/620/equations-of-lines` as
**110,460 bytes** on 2026-08-08, where this file records **113,219 B** on 2026-08-07. Both are
reproduced as written.

### Sample 3, HS.G.CO.A.1 and HS.G.GPE.B.7 SEAD Lesson

`https://learnwithsap.org/resources/hs-g-co-a-1-hs-g-gpe-b-7-lesson-with-social-emotional-and-academic-development-sead-theme/`,
HTTP 200 with browser UA, 307,751 B. Recorded as the only HS geometry item on learnwithsap.org.

Recorded finding: no per-resource licence notice. Byline verbatim: "By: Student Achievement
Partners, Colleen McDaniel • Published March 10, 2022". Body verbatim, a third-party dependency:
"This task utilizes the lesson planning template from Stride 3: A Pathway to Equitable Math
Instruction: Creating Conditions to Thrive." No license is stated for that template.

### Sample 4, Coherence Map data file

`https://tools.achievethecore.org/coherence-map/data.js`, HTTP 200, 2,296,445 B. The Coherence
Map UI at `tools.achievethecore.org/coherence-map/HS/116/<id>/<id>` is recorded as a JS SPA,
10,085 B shell with no content in the HTML; content comes from this data.js.

For every one of the five target standards it embeds the full example task text and solution
inline:

- id 612 = HSG-SRT.B.4, task "Pythagorean Theorem", attribution "Provided by Illustrative Mathematics"
- id 613 = HSG-SRT.B.5, task "Bank Shot", attribution "Provided by Illustrative Mathematics"
- id 614 = HSG-SRT.C.6, task "Defining Trigonometric Ratios", attribution "Provided by Illustrative Mathematics"
- id 615 = HSG-SRT.C.7, task "Sine and Cosine of Complementary Angles", attribution "Provided by Illustrative Mathematics"
- id 616 = HSG-SRT.C.8, task "Setting Up Sprinklers", attribution "Provided by Illustrative Mathematics"
- ids 617 and 618 = SRT.D.10 and SRT.D.11 have EMPTY attribution and EMPTY example task

Recorded finding, measured with a regex over the decoded inline HTML for ids 614 and 616: zero
occurrences of "licen", "creative commons", "©", or "copyright". SAP redistributes the full IM
task and solution with an attribution string and no license statement. The report's own reading,
given Sample 2, is that the governing license on that text is IM's CC BY-NC-SA, which the
Coherence Map does not surface.

### Sample 5, the example-task PDFs the Coherence Map points at

`data.js` `example_problem_url` values for ids 612 to 616 all point at IM's own bucket, for
example
`http://s3.amazonaws.com/illustrativemathematics/attachments/000/009/374/original/public_task_1635.pdf?1462396486`.

Recorded fetch result, with the failure mode kept distinct: connection TIMEOUT, no HTTP
response. Tried twice (45s path-style https, 20s http, 20s virtual-host style https), curl exit
28 every time, `http_code 000`.

Control recorded: `https://s3.amazonaws.com/` from the same shell returns HTTP 307, so S3 egress
works. Verbatim: "the specific object does not answer. I could NOT distinguish "bucket deleted"
from "blackholed". NOT reported as a 404."

Also recorded: these are plain `http://` links inside an `https://` page, so mixed content.

## 6. GitHub, no license files

`https://api.github.com/repos/achievethecore/{atc-coherence-map, atc-lesson-planner,
atc-coaching-tool, atc-academic-word-finder}`: all HTTP 200, all return `"license": null`.

Last pushes recorded: coherence-map 2022-12-09, lesson-planner 2021-06-02, coaching-tool
2014-12-19, academic-word-finder 2014-12-19. No LICENSE file. The site footer links this org
under "For Developers".

## 7. Coverage of HSG-SRT.B.4 / B.5 / C.6 / C.7 / C.8

What is there, measured:

- The Coherence Map carries all five standards with full statement text, cluster and progression
  narrative, connections to prior standards, and one worked example task plus solution each (see
  Sample 4).
- HS.G-SRT.A.3 progression note, verbatim: "[S]tudents can see that two figures which are similar
  according to the traditional notion are also similar according to the transformation definition by
  deriving the AA criterion for similarity of triangles."
- SRT.C.6 statement, verbatim: "Understand that by similarity, side ratios in right triangles are
  properties of the angles in the triangle, leading to definitions of trigonometric ratios..."

What is not there, measured:

- Mathematics mini-assessments at `/category/1020`: **28 items listed, NONE geometry**. HS items
  recorded as Quadratic Equations, Micro-Models and Reasoned Estimates, Functions, Simultaneous
  Linear Equations, Equations Procedural Skill and Fluency. Zero SRT, zero geometry.
- The learnwithsap.org resources post type: 46 total. Searching the WordPress API for "trigon",
  "HSG" and "pythagorean" returns ZERO. The single HS geometry item is the CO.A.1 / GPE.B.7
  distance-formula SEAD lesson of Sample 3, not SRT.
- Recorded conclusion: the only SRT-relevant material on this host is the Coherence Map, and its
  substance is Illustrative Mathematics content, not SAP content.

**Count discrepancy to carry forward, not resolved here.** The companion staged extract
`host-achieve-the-core.md` records `/category/1020/mathematics-assessments` as showing "Results
(24)" on 2026-08-08, where this file records 28 items on 2026-08-07. Both are reproduced as
written.

## 8. Recorded as could not verify

- **Which version of the public-domain instrument.** The words "Creative Commons Public Domain
  Dedication License" appear with no version and no link (zero `creativecommons` strings in the
  page HTML). The report states CC0 1.0 is the obvious intent and that it is NOT stated.
- **Whether the dedication on learnwithsap.org/permissions/ extends to achievethecore.org.**
  Verbatim: "The page says "All of the content on learnwithsap.org" — by its own words it does
  NOT cover achievethecore.org, and ATC's own /permissions is a soft 404. This is a real gap."
- Whether any specific SRT artifact is © marked. The Coherence Map has no © field at all.
- Whether the IM S3 example-task PDFs are dead or merely unreachable from that shell.
- The report did not enumerate all 46 learnwithsap resource pages, nor the full ATC task library.
  The `/category/416` listing is paginated and filtered client-side; the agent saw 35 links of an
  unknown total.
- `learnwithsap.com` and `learnwithsap.net`, both HTTP 200 at approximately 27KB, were not
  investigated.
- The Wayback Machine was not queried by this agent, on the recorded ground that nothing was dead
  or blocked in a way that required it, the one 403 being a UA bot block solved by a browser-UA
  retry.

## 9. Analysis recorded by the evidence file, not host text

Attribute the following to this project's own measurement, never to Student Achievement Partners:

- The report's §9 "Safe to quote?" is that agent's application of these grants to the HS Geometry
  repo. Its stated positions: SAP's own prose is dedicated to the public domain by the
  /permissions/ page, so quoting is safe and republishing would be permitted by that grant, with
  citation anyway; the HSG-SRT example tasks are Illustrative Mathematics and the one IM file
  opened states CC BY-NC-SA, so they are cite-only, cited to IM rather than SAP, and not to be
  paraphrased and republished; e² Tools are cite-only with no derivatives, no public
  redistribution and no AI training datasets; Instructional Insights is not to be touched; and
  the "Achieve the Core" and "achievethecore.org" marks are never to be used in a way implying
  endorsement.
