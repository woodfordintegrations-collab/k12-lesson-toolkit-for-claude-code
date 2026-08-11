---
source_url: hs-geometry-similarity-trig/sources/license-open-middle.md
fetched: 2026-08-08
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-open-middle, license-all-rights-reserved, license-withdrawn-grants, trap-license-withdrawn-after-citation, trap-down-is-not-one-state, trap-soft-404-status-proves-nothing, trap-compressed-body-grepped-as-text, trap-access-is-not-a-rights-fact, concept-chain-of-title, concept-curate-and-cite, practice-build-a-source-table, evidence-store-ingest-boundary
---

# openmiddle.com (www.openmiddle.com)

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every live fetch recorded below was performed by the verifying agent on
**2026-08-08 (UTC)**, which the report states applies to all live fetches. Wayback captures
carry their own snapshot dates, given inline. The report's own scope statement: this host
only, and where the agent could not verify, the item is listed under section 8 and NOT stated
as a finding.

---

## 1. Reachability: live, bot-blocked

| Probe | Result |
|---|---|
| `curl -L https://www.openmiddle.com/` default UA | **HTTP 406**, 0 redirects |
| `curl -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ..."` | **HTTP 200**, 100,227 bytes |
| WebFetch (tool default UA) | 200, content returned |

Report's finding, in its own emphasis: **the site is LIVE. The 406 is a server-side
user-agent filter, that is, a BOT BLOCK, not a dead site.**

Corroborating nuance recorded: `robots.txt` (HTTP 200) does NOT exclude general crawlers. It
allows `*` with `Crawl-delay: 2` and disallows only Baiduspider, Sosospider, and one
wp-content path. So the block is imposed at the server or WAF layer, contradicting the site's
own published crawl policy. The report notes that an automated link checker using a default UA
would misreport this host as broken.

Oddity the report records for accuracy and marks as not licence-relevant: the served robots.txt
literally begins `ser-agent: *`. The leading `U` is absent in the raw bytes, verified via xxd
(`73 65 72 2d 61 67 65 6e 74` = "ser-agent"). The first directive group is therefore malformed.

## 2. Dedicated policy pages: none exist

Probed with a browser UA. All return the site's soft-404 template (approximately 92KB, HTTP 404):

`/terms/` · `/terms-of-use/` · `/terms-of-service/` · `/copyright/` · `/permissions/` ·
`/license/` · `/licensing/` · `/faq/` · `/privacy/` · `/privacy-policy/` all **HTTP 404**.

Exist (HTTP 200): `/about/` (301 to `/about-embedding/`), `/whats-open-middle/`,
`/open-middle-team/`, `/submit/`.

Three independent confirmations recorded that no policy document exists:

1. **page-sitemap.xml (HTTP 200).** The complete page list is `/`, `/advanced-search/`,
   `/whats-open-middle/`, `/open-middle-team/`, `/submit/`, plus `es/` and `fr/` translations.
   No terms, privacy, copyright, or license page.
2. **The site's own search** (`/?s=copyright`, `?s=license`, `?s=permission`) returned zero
   content results.
3. **Wayback CDX.** Zero captures ever for `openmiddle.com/terms*`, `/copyright*`, `/license*`,
   `/privacy*`. The endpoint was proven working by control queries against `openmiddle.com`
   root and `/similar-triangles/`, which both returned capture rows.

Report's conclusion: **the ONLY licence-bearing text on this site is the footer.**

## 3. Verbatim licence evidence, live

Site-wide footer. `https://www.openmiddle.com/`, HTTP 200 (browser UA), 2026-08-08:

> © 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered
> trademark of Glenrock Consulting, LLC.

Extraction method recorded: tag-stripping the raw HTML around the matched string. The report
states this identical string appears on every page fetched, and that **no Creative Commons
string appears anywhere in any live page fetched**. `grep -c creativecommons` returned 0 for
the root, the category page, the embedding page, and all 10 problem pages.

## 4. Per-resource pages: no variation, and that is the finding

Ten problem pages opened individually, all HTTP 200, browser UA, 2026-08-08. Every one carries
the same site-wide all-rights-reserved footer and no per-resource licence notice of any kind.

| # | URL | Own licence notice? | Contributor byline | Standards tags |
|---|---|---|---|---|
| 1 | /similar-triangles/ | none, site ARR footer only | Source: Drew Ross | g-srt.2 |
| 2 | /similar-triangles-2/ | none, site ARR footer only | Source: Drew Ross | g-srt.2 |
| 3 | /trigonometric-ratios/ | none, site ARR footer only | Source: Thomas Derstein | g-srt.8 |
| 4 | /pythagorean-inequality/ | none, site ARR footer only | Source: Samantha Cruz | g-srt.8 |
| 5 | /finding-the-length-of-a-right-triangles-altitude/ | none, site ARR footer only | Source: Kate Nerdypoo | g-srt.5, g-srt.8, g-gpe.5, a-rei.6 |
| 6 | /three-triangles-and-a-wannabe/ | none, site ARR footer only | Source: Jonathan Lees | g-srt.8 |
| 7 | /equilateral-triangle-side-length/ | none, site ARR footer only | Source: Robert Kaplinsky | g-srt.8, 8.g.7 |
| 8 | /law-of-cosines-triangle/ | none, site ARR footer only | Source: Erick Lee | g-srt.4, g-srt.11 |
| 9 | /area-of-three-triangles/ | none, site ARR footer only | Source: Dan Wulf | g-srt.11 |
| 10 | /simplifying-rational-expressions/ | none, site ARR footer only | Source: Dwight Stephenson | g-srt.6 |

Verified per page: `creativecommons` absent, `All rights reserved` present. Report's
conclusion: the licence does not vary per resource; it is uniformly All Rights Reserved.

## 5. The critical finding: the CC licence was removed in early 2026

The report's statement: Open Middle carried **CC BY-NC-SA 4.0 for a decade and dropped it
roughly five months ago.** Anyone relying on memory, on a citation written before March 2026,
or on a third-party OER licence list will get this wrong.

Archived footers, Wayback `id_` raw captures, fetched `--compressed`, 2026-08-08:

| Snapshot | CC present | Verbatim footer fragment |
|---|---|---|
| 2016-05-27 | YES | "Open Middle is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2019-06-03 | YES | "Open Middle ® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2023-06-01 | YES | "© 2016-2023 Open Middle Partnership. All rights reserved. ... Open Middle® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2026-01-09 | YES | "© 2016-2026 Open Middle Partnership. All rights reserved. ... licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0" |
| **2026-02-16** | **YES** | same as above, and the report marks this the LAST capture with CC |
| **2026-03-03** | **NO** | "© 2016-2026 Open Middle Partnership. All rights reserved. Open Middle is the registered trademark of the Open Middle Partnership. Get in contact with us", marked the FIRST capture without CC |
| 2026-05-12 | NO | "© 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered trademark of Glenrock Consulting, LLC." |
| **2026-08-08 (LIVE)** | **NO** | "© 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered trademark of Glenrock Consulting, LLC." |

CC deed URL as it appeared in all historical footers:
`http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US`

Two separate events, in this order, as the report states them:

- **CC removal window: between 2026-02-16 and 2026-03-03.**
- **Rights-holder entity change, Open Middle Partnership to Glenrock Consulting, LLC: between
  2026-03-03 and 2026-05-12.**

Method note and near-miss the report records deliberately: the agent's first pass at the
2026-03-03 snapshot read gzip bytes as text and appeared to show "no footer at all." That was
a fetch artifact, not a finding. It was re-fetched with `curl --compressed` before any
conclusion was drawn. Raw Wayback `id_` URLs return the originally-compressed payload, so
decompress before grepping.

## 6. Riders, as the report enumerates them

1. **Registered trademark.** "Open Middle is the registered trademark of Glenrock Consulting,
   LLC." Titles render as "Open Middle®". Trademark is separate from copyright and survives
   regardless of the copyright posture. The report's instruction: do not use "Open Middle" as
   the name of our materials or imply endorsement. Nominative reference ("problems in the Open
   Middle format", with citation) is treated as a different matter from branding.
2. **Third-party contributor chain.** Every problem carries a named individual byline
   ("Source: Drew Ross", "Source: Kate Nerdypoo", and so on) while the site asserts blanket
   all-rights-reserved. The report's guidance: whatever is cited should carry BOTH the
   contributor name and openmiddle.com, matching the site's own convention.
3. **No contributor-terms document.** `/submit/` contains only "We are always looking for new
   problems to add to this website... please fill out the form below" and an externally-loaded
   form ("Loading…"). No copyright-assignment or licensing language is presented to
   contributors on the page. The upstream rights chain is therefore not publicly documented.
4. **Sanctioned embedding is a use pathway, NOT a copyright licence.** `/about-embedding/`
   (HTTP 200) documents an official "Use this problem" embed: iframes into Canvas, Google
   Classroom, Microsoft Teams, "websites, and many other locations", with toggles for title,
   hint, answer. Verbatim: "Embedded problems allow you to add interactive problems to your
   Canvas page, websites, and many other locations." The report's reading: this is content
   served from their domain under their control. It grants no right to copy problem text into
   our repository, and an iframe to a third-party host is a dependency, not an asset.
5. **No NonCommercial or ShareAlike obligation applies going forward**, because there is no
   licence at all now. All rights reserved is more restrictive than the CC BY-NC-SA it replaced.
6. **Crawl-delay: 2** declared in robots.txt, and the server additionally 406s non-browser UAs.

## 7. Relevance to the unit (HSG-SRT.B.4, B.5, C.6, C.7, C.8)

The site has an exactly-matching category:
`https://www.openmiddle.com/category/high-school-geometry/similarity-right-triangles-and-trigonometry/`
H1 "Similarity, Right Triangles, and Trigonometry", HTTP 200, **10 problems, no pagination.**

Mapped against the five target standards, using the site's own tags:

- **B.4** (prove theorems about triangles): 1 problem, Law of Cosines Triangle (g-srt.4). The
  report calls this thin.
- **B.5** (use congruence or similarity criteria to solve problems or prove): 1 direct,
  Finding the Length of a Right Triangle's Altitude (g-srt.5). Plus 2 tagged g-srt.2 (Similar
  Triangles, Similar Triangles 2), which the report places just upstream at SRT.A.2.
- **C.6** (side ratios and trig ratios from similarity): 1 problem, Simplifying Rational
  Expressions (g-srt.6). The report notes the title is misleading; it is tagged to C.6.
- **C.7** (sine and cosine of complementary angles): **ZERO problems. Confirmed gap.** No
  g-srt.7 tag appears on any of the 10 category members.
- **C.8** (Pythagorean plus trig ratios to solve right triangles, applied): the strongest
  area, 5 problems, namely Trigonometric Ratios, Pythagorean Inequality, Three Triangles And A
  Wannabe, Equilateral Triangle Side Length, Finding the Length of a Right Triangle's Altitude.

Also present but beyond the unit: 2 problems tagged g-srt.11 (Law of Sines and Cosines).

Format recorded: each page is a short "Directions:" constraint task (typically "using the
digits 0 to 9 at most one time each, place a digit in each box…"), plus a collapsible Hint, a
collapsible Answer with full solution methods, a DOK rating (DOK 2 or DOK 3), and a contributor
byline. An `/advanced-search/` page exists for standard-based lookup.

The report's judgment of what the host is good for in this unit: problem-structure inspiration
for C.8 and warm-up or closure tasks. It is not a source of exposition, worked examples, or
diagrams, and it will not cover C.7 at all.

## 8. Unverified, carried forward as gaps

The report marks these as not findings.

- **Whether the CC removal retroactively affects copies obtained before 2026-02-16.** CC 4.0's
  own text describes the grant as irrevocable, but whether that helps material accessed today,
  when no CC offer is extended, is a legal question the agent did not and could not resolve by
  fetching. Recorded as a counsel question, not a research finding.
- **Why the licence changed**, and the nature of the Open Middle Partnership to Glenrock
  Consulting, LLC transfer. No announcement post was located. The `/category/articles/` archive
  was not exhaustively searched.
- **The exact CC removal date** beyond the 2026-02-16 to 2026-03-03 window. Wayback captured
  nothing between those dates.
- **Contributor-side terms.** The `/submit/` form body loads externally and was not opened, so
  any assignment or licensing language it may contain is unseen.
- **Whether the all-rights-reserved footer is legally effective over contributor-authored
  problems** given no visible assignment. Not resolvable by fetching.
- **Fair-use analysis** for quoting a one-sentence "Directions:" line. Recorded as a counsel
  question, not a fetched fact. The report adds a practical point and explicitly flags it as
  reasoning rather than a verified finding: these prompts are 1-2 sentences, and the format (an
  open-middle constraint task) is an idea, not protected expression.
- **The 5 problems not opened individually** are the 5 non-SRT sidebar links. All 10 actual
  category members were opened.

## 9. The report's bottom line for the curate-and-cite model

Citing openmiddle.com is unaffected, because citation is not redistribution and all rights
reserved does not restrict it. What changed as of early 2026 is that **the CC BY-NC-SA 4.0
fallback is gone.** Any plan that involved reproducing, adapting, or ShareAlike-republishing
Open Middle problem text no longer has a licence to rely on. The report's instruction: link and
cite; write our own prompts.
