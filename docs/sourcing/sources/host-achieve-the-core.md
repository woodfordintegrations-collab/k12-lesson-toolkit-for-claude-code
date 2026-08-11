---
source_url: hs-geometry-similarity-trig/sources/license-achieve-core.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-achieve-the-core-sap, license-public-domain-dedication, license-withdrawn-grants, practice-build-a-source-table, trap-soft-404-status-proves-nothing, trap-license-withdrawn-after-citation, trap-font-notice-is-not-a-content-license, trap-compressed-body-grepped-as-text
---

# Host extract: achievethecore.org (Student Achievement Partners)

**Original fetch date recorded by the evidence file: 2026-08-08 (UTC).** Scope recorded as this
host only. The `fetched:` field above is the staging date.

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Reachability

`curl -sIL https://achievethecore.org/` returned HTTP 200 with no redirects. Recorded: site
live, not bot-blocked at root.

## 2. The site is a SPA and every URL returns HTTP 200

Recorded measurements:

- Every unknown URL returns the identical 140,749-byte homepage shell, a soft 404.
- HTTP status is recorded as useless as an existence signal on this host. Existence must be
  tested by byte size or content comparison.
- The path `/page/terms-of-use` is a shell (soft 404). The evidence file records this as the
  reason an earlier fetch "found no licensing statement": it was reading the homepage, not the
  terms.
- The real path is `/terms-of-use`, 93,954 bytes, real content.
- `/privacy-policy` is 80,465 bytes, real.
- `/ccpd` is 140,749 bytes, the shell, so the Permissions page has been removed.
- The footer HTML contains, commented out, the string
  `<!-- <li><a href="/ccpd">Permissions</a></li> -->`, recorded as appearing twice. The report
  reads this as a Permissions page that existed and was deliberately delinked.
- The footer also links the GitHub org `https://github.com/achievethecore` under "For
  Developers".

**Byte-size discrepancy to carry forward, not resolved here.** A second staged extract for the
same organisation, `host-learnwithsap.md` (from a different agent, fetch date 2026-08-07),
records the achievethecore.org homepage shell as **137,828 bytes**, where this file records
**140,749 bytes**. Both figures are reproduced as written. Do not average, reconcile or pick one
without a fresh fetch.

## 3. Verbatim license text, https://achievethecore.org/terms-of-use

HTTP 200, 2026-08-08. Recorded as verified two independent ways, WebFetch plus raw curl and
strip.

Section heading "Copyright", verbatim:

> "Some material on Our Site is protected by copyright and some material has been dedicated to
> the public domain. For material protected by copyright, SAP owns or has the right to include
> the material on Our Site. Material may be used as indicated on Our Site for the particular
> material. You may not remove or modify any copyright notices, credit or other attribution
> associated with materials."

Trademark rider, same page, section "Trademarks", verbatim:

> "Our name and our trademarks and service marks, including "Achieve the Core" and
> "achievethecore.org," logos, and other indicia of source are owned by SAP (collectively,
> "Our Trademarks"). You may not use Our Trademarks without our prior written consent in each
> case..."

Framing rider, section "Links, Frames and Metatags", verbatim:

> "You may not "frame" the content of Our Site on any other web site (display Our Site inside
> the window or browser of another site) unless you first obtain our prior written consent in
> each case."

Recorded reading: the site-wide terms explicitly decline a single license. "Material may be used
as indicated on Our Site for the particular material" makes per-resource marking the operative
grant.

## 4. The withdrawn blanket public-domain dedication

### 4a. The 2016 archived Permissions page

Wayback CDX for `achievethecore.org/ccpd` returned snapshot `20160303204431`, status 200.
Fetched `https://web.archive.org/web/20160303204431/http://achievethecore.org/ccpd`, HTTP 200,
37,273 bytes.

Verbatim from that archived 2016 Permissions page:

> "The person who associated a work with this deed has dedicated the work to the public domain by
> waiving all of his or her rights to the work worldwide under copyright law, including all related
> and neighboring rights, to the extent allowed by law. You can copy, modify, distribute and perform
> the work, even for commercial purposes, all without asking permission. Click here for more
> information."

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain
> Dedication License unless it is marked with the (c), which indicates that it includes content that
> has been licensed to Student Achievement Partners, Inc., from third parties and must be used solely
> as noted when hovering over the (c) next to the applicable content."

### 4b. The removal window, measured

The evidence file records a correction to its own first framing. Wayback CDX plus the
availability API show `/ccpd` served the dedication text continuously at these snapshots, all
status 200 with the text present:

`2016-03-03`, `2017-07-22`, `2020-04-30`, `2022-01-03`, `2024-03-23`, `2026-01-11`,
`2026-04-25`.

Latest snapshot carrying the text: `20260425161111`.

Live on 2026-08-08: `https://achievethecore.org/ccpd` is 140,749 bytes, byte-identical to the
homepage shell, and "Public Domain Dedication" occurs 0 times.

**Recorded removal window: between 2026-04-25 and 2026-08-08.**

Verbatim from `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd`
(HTTP 200). Note that this 2026 transcription uses the `©` character where the 2016
transcription used `(c)`:

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain
> Dedication License unless it is marked with the ©, which indicates that it includes content that
> has been licensed to Student Achievement Partners, Inc., from third parties and must be used
> solely as noted when hovering over the © next to the applicable content."

### 4c. Method warning recorded with the finding

Verbatim from the evidence file:

> METHOD WARNING recorded: my first pass at this snapshot used wayback `id_` raw mode WITHOUT
> `--compressed`. curl returned gzip bytes; grep found 0 matches; I nearly reported "CC0 already
> gone by April 2026". That was an artifact of binary, not a finding. Re-fetched with --compressed
> -> 1 match. Never grep a possibly-compressed body.

## 5. Per-resource samples, 3 opened, fetched 2026-08-08, all HTTP 200

The evidence file records a scope boundary: the shared scratchpad also contained `res-1..res-5.html`
written by another agent working the Illustrative Mathematics host, and those files are excluded
from these findings.

### Sample A, https://achievethecore.org/page/620/equations-of-lines

HTTP 200, 110,460 bytes. On-page: "Author: Illustrative Mathematics". Meta grades=8. No license
text in the page HTML.

Attached PDF: `/content/upload/Grade 8 IM task - equations of lines final06.26.14.pdf`,
HTTP 200, 247,201 bytes. `pdftotext` of that PDF, verbatim by line:

> line 3:   "Task by Illustrative Mathematics, annotation by Student Achievement Partners"
> line 148: "Typeset May 4, 2016 at 22:05:25. Licensed by Illustrative Mathematics under a"
> line 149: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ."
> line 172: "8.EE Equations of Lines is licensed by Illustrative Mathematics"
> line 173: "under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License"

Embedded link targets in the PDF: `http://creativecommons.org/licenses/by-nc-sa/4.0/` and
`.../deed.en_US`.

Recorded findings on this sample:
- Internal inconsistency: the same PDF states 4.0 International in one place and 3.0 Unported in
  another. Both are BY-NC-SA. The report records the version as "genuinely ambiguous on the face
  of the document."
- Mixed authorship: the task is IM (BY-NC-SA); the annotation layer is SAP (unmarked).
- The report calls this a hard counterexample to any blanket public-domain claim, because NC and
  SA riders apply.

### Sample B, https://achievethecore.org/page/976/quadratic-equations-mini-assessment

HTTP 200, 107,723 bytes. On-page: "Author: Student Achievement Partners". Meta grades=High
School. No license text on page.

Attached PDF: `/content/upload/A-REI.B.4 & A-CED.A.1 Quadratic Equations.pdf`, HTTP 200,
238,228 bytes. Recorded: `pdftotext` shows no copyright, licence, CC, or rights-reserved
statement anywhere in the document text.

Recorded verbatim, the false-positive warning:

> (The only "All Rights Reserved" strings are EMBEDDED FONT notices - Microsoft Calibri - NOT a
>  content licence. Do not mistake font metadata for a grant.)

Recorded conclusion for this sample: a SAP first-party resource ships with no licence marking at
all.

Note for anyone re-fetching: the recorded PDF URL contains a literal space and a literal `&`.

### Sample C, https://achievethecore.org/page/1100/functions-mini-assessment

HTTP 200, 107,956 bytes. On-page: Author = Student Achievement Partners, meta grades=8. No
licence text in the page HTML. The only "MIT License" string present is a normalize.css library
comment, recorded as irrelevant.

### Recorded verdict across the three samples

Verbatim: "VARIES PER RESOURCE, and most items are simply UNMARKED. The current site publishes
no blanket grant, and the per-item marking the Terms points to is frequently absent."

## 6. Coherence Map and coverage of HSG-SRT.B.4 / B.5 / C.6 / C.7 / C.8

The Coherence Map is recorded as live on the subdomain `tools.achievethecore.org`. Data file
`https://tools.achievethecore.org/coherence-map/data.js`, HTTP 200, 2,296,445 bytes, fetched
2026-08-08.

All five target standards present, keyed by numeric id rather than by code string, with the
linked-task counts as recorded:

- 612 = HSG-SRT.B.4 "Prove theorems about triangles..." 1 linked task
- 613 = HSG-SRT.B.5 "Use congruence and similarity criteria..." 5 linked tasks
- 614 = HSG-SRT.C.6 "Understand that by similarity, side ratios..." 6 linked tasks
- 615 = HSG-SRT.C.7 "Explain and use the relationship between sine and cosine..." 1 linked task
- 616 = HSG-SRT.C.8 "Use trigonometric ratios and the Pythagorean Theorem..." 3 linked tasks

Recorded: every one of the five carries `"example_problem_attribution":"Provided by Illustrative
Mathematics"`. Every `example_problem_url` points to
`s3.amazonaws.com/illustrativemathematics/...`. Every linked task points off-site to
`illustrativemathematics.org` or `tasks.illustrativemathematics.org`. Progression images are
hot-linked from `dropbox.com`, recorded as third-party hosting and fragile. The Coherence Map
page itself shows no licence, copyright or permission text at all.

**Recorded gap, measured:** ATC's own task and mini-assessment libraries contain nothing for
HSG-SRT.

- `/category/416/mathematics-tasks` shows "Results (31)", zero G-SRT items.
- `/category/1020/mathematics-assessments` shows "Results (24)", zero G-SRT items.
- Both listings recorded as K-8 dominated; the only HS math items seen are Algebra (quadratic
  equations, functions). No geometry or trigonometry mini-assessment exists.

## 7. GitHub

Footer "For Developers" links `https://github.com/achievethecore`. Recorded from
`api.github.com/orgs/achievethecore/repos`: 4 repos, every one `license=None` with no LICENSE
file: `atc-academic-word-finder`, `atc-coaching-tool`, `atc-lesson-planner`, `atc-coherence-map`
(updated 2026-05-24).

## 8. Final verdict as recorded by the evidence file

Verbatim: "VARIES PER RESOURCE, and the site-wide CC0 grant was WITHDRAWN within the last ~3
months. Safe to CITE. Do NOT rely on CC0 for copy/paraphrase-and-republish."

Recorded alongside it: "The CC0 folk knowledge is HISTORICALLY GROUNDED (2016) but the page is
GONE from the live site and its footer link is COMMENTED OUT. The current Terms of Use makes a
WEAKER, per-item claim … Do NOT state CC0 as the live site-wide license. The blanket CC0 grant
is no longer published. Third-party (c) carve-out was a rider even in 2016."

Note on vocabulary: the evidence file uses the label "CC0" throughout, while the text it quotes
from both the live terms and the archived Permissions page never uses that string. The quoted
instrument name is "Creative Commons Public Domain Dedication License", with no version stated
and no deed link recorded on this host. The version is unverified from this file.
