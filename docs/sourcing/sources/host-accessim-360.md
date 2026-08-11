---
source_url: hs-geometry-similarity-trig/sources/license-im-360.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-accessim-360, license-noncommercial, trap-soft-404-status-proves-nothing, trap-license-lives-off-the-obvious-page, concept-third-party-carve-out
---

# Host extract: accessim.org (IM TK-12 Math v.360, 2nd edition)

**Original fetch date recorded by the evidence file: 2026-08-07**, stated as covering every
fetch in the report. The `fetched:` field above is the staging date.

Assigned host in the original report: `accessim.org`, titled "Illustrative Mathematics | v.360
Curriculum". Hypothesis under test: "CC BY-NC 4.0 with an explicit commercial prohibition".

Recorded result, verbatim: "**CC BY-NC 4.0 — CONFIRMED verbatim**, uniform across 13/13
curriculum pages. But the "explicit commercial prohibition" half of the hypothesis is **NOT
corroborated as prose** — the word "commercial" appears ZERO times on every accessim.org
page I fetched. The NC restriction is carried solely by the license label + hyperlink."

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Reachability, as recorded

| probe | result |
|---|---|
| `curl -L https://accessim.org/` default UA | HTTP 200, 169,069 bytes |
| `curl -L https://accessim.org/` browser UA | HTTP 200 |
| WebFetch root | success, content returned |

Recorded characterisation: live, not bot-blocked, no TLS error, no Wayback fallback needed.
Stack recorded as Next.js App Router on Vercel (`/_next/static/...`,
`sentry-environment=vercel-production`).

Two partial failures, recorded as server-side and intermittent rather than blocks. The distinct
failure modes are preserved:

- `/9-12-aga/geometry/course-guide/lessons-by-standard?a=teacher` failed twice:
  `curl (28) Connection timed out after 40005 ms`, then `curl (35) Recv failure: Operation
  timed out` at 38.8s. HTTP 000, 0 bytes. Never retrieved.
- `/9-12-aga/geometry/unit-4/section-a/lesson-5/preparation?a=teacher`: `curl (35) Recv
  failure`, HTTP 000. Other lessons in the same unit fetched fine.

## 2. HTTP status is not an existence signal on this host

Recorded measurement: `/zzz-definitely-not-a-real-page-9876` returns **HTTP 200**, 1,486,023
bytes. The Sentry transaction on that page is `GET /[curriculum_slug]`. Unknown paths are
swallowed by a Next.js dynamic catch-all, producing a **soft 404**. A byte-diff of `/terms`
against the bogus slug is recorded as identical except for the echoed slug in nav hrefs and the
per-request sentry trace id.

Consequently, the 200s on these paths mean nothing and none of these pages exist:
`/terms /terms-of-use /terms-of-service /copyright /license /licensing /permissions
/about /faq /attribution /attributions /legal`, all approximately 1,485,7xx bytes, identical
shell.

Recorded conclusion, verbatim: "**accessim.org has no site-wide terms-of-use, copyright, or
license page.**"

The only real distinct policy page recorded is `/privacy-policy` at 120,462 bytes, and WebFetch
is recorded as confirming it contains no copyright, IP, license, CC, permitted-use or
redistribution text.

## 3. The license, verbatim

Footer, recorded as present on every curriculum-scoped page. Raw HTML as served:

```html
<div class="im-c-footer__licensing im-u-grid--gap-lg">
<p>Illustrative Mathematics® has operated as an independent 501(c)3 non-profit organization since 2013.</p>
<p>©2024 Illustrative Mathematics®. Licensed under<!-- --> <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>.</p>
<p>The Illustrative Mathematics name and logo are not subject to the Creative Commons license and may not be used without the prior and express written permission of Illustrative Mathematics.</p>
<p>This site includes public domain images or openly licensed images that are copyrighted by their respective owners. Openly licensed images remain under the terms of their respective licenses. See the image attribution section for more information.</p>
</div>
```

Link target resolves to `https://creativecommons.org/licenses/by-nc/4.0/`. Recorded reading: BY-NC,
not SA, not ND. Copyright year on the notice: **2024**.

Note the ordering again: the grant sentence is immediately followed by the trademark carve-out
and then by the third-party image carve-out. The three paragraphs are one footer block.

## 4. Per-page license audit

Counts of `licenses/by-nc/4.0` versus `by-sa` versus `by-nd` versus plain `by/4.0` per file, and
of the word "commercial":

| page | by-nc | by-sa | by-nd | by | "commercial" |
|---|---|---|---|---|---|
| `/` (homepage) | 0 | 0 | 0 | 0 | 0 |
| `/privacy-policy` | 0 | 0 | 0 | 0 | 0 |
| `/terms` (soft-404) | 0 | 0 | 0 | 0 | 0 |
| bogus slug (soft-404) | 0 | 0 | 0 | 0 | 0 |
| `/hs` | 1 | 0 | 0 | 0 | 0 |
| `/9-12-aga/geometry` | 1 | 0 | 0 | 0 | 0 |
| geometry `/unit-3` | 1 | 0 | 0 | 0 | 0 |
| geometry `/unit-4` | 1 | 0 | 0 | 0 | 0 |
| `/course-guide` | 1 | 0 | 0 | 0 | 0 |
| `/course-guide/attributions` | 1 | 0 | 0 | 0 | 0 |
| `/course-guide/citations` | 1 | 0 | 0 | 0 | 0 |
| U3 L13 prep | 1 | 0 | 0 | 0 | 0 |
| U4 L6 prep | 1 | 0 | 0 | 0 | 0 |
| U4 L7 prep | 1 | 0 | 0 | 0 | 0 |
| U4 L8 prep | 1 | 0 | 0 | 0 | 0 |
| U4 L10 prep | 1 | 0 | 0 | 0 | 0 |
| U4 L11 prep | 1 | 0 | 0 | 0 | 0 |
| U3 L13 `?a=student` | 1 | 0 | 0 | 0 | 0 |
| U4 `/downloads` | 1 | 0 | 0 | 0 | 0 |

Recorded: no per-resource variation. Every curriculum page carries exactly one CC BY-NC 4.0.

Two structural notes recorded, the second verbatim:

- "commercial" returns 0 hits site-wide across all 19 fetches.
- "The homepage and privacy policy carry **no license notice at all** — the footer is
  rendered only inside the curriculum route tree. Anyone checking only `accessim.org/`
  would conclude the site is unlicensed. It isn't; you have to be on a curriculum page."

## 5. Course Guide §17 "Attributions", verbatim in full

URL: `https://accessim.org/9-12-aga/geometry/course-guide/attributions?a=teacher`
HTTP 200, 1,521,128 bytes. Recorded extraction note: the content lives in the RSC flight payload,
not the initial DOM, so WebFetch truncates before reaching it; the text was extracted from raw
HTML.

> The Common Core State Standards are trademarks of the Common Core State Standards
> Initiative. © Copyright 2010. National Governors Association Center for Best Practices
> and Council of Chief State School Officers. All rights reserved.
> http://www.corestandards.org/
>
> The 5 Practices are from Smith, M. S., & Stein, M. K. (2011). *5 practices for
> orchestrating productive mathematics discussions*. National Council of Teachers of
> Mathematics.
>
> *Notice and Wonder* and *I Notice/I Wonder* are trademarks of the National Council of
> Teachers of Mathematics, reflecting approaches developed by the Math Forum
> (https://imk12.org/MathForum), and used here with permission.
>
> Images that are not the original work of Illustrative Mathematics are in the public
> domain or released under a Creative Commons Attribution (CC-BY) license, and include an
> appropriate citation. Images that are the original work of Illustrative Mathematics do
> not include such a citation.
>
> Reference links are provided as a convenience for informational purposes only and were
> active and accurate at the time of publication. They do not constitute an endorsement or
> approval by Illustrative Mathematics of any products, services, or opinions of the
> corporation, organization, or individual. Illustrative Mathematics is not responsible for
> the content of external sites.

## 6. Riders, as enumerated by the evidence file

1. **NonCommercial (NC).** Blocks commercial reuse.
2. **Attribution (BY).** Required. `©2024 Illustrative Mathematics®` plus the CC BY-NC 4.0
   link. Recorded: no canonical attribution string is prescribed anywhere on the site.
3. **Trademark carve-out.** The IM name and logo are expressly carved out of the CC grant and
   need prior written permission.
4. **CCSS trademark, third party.** "trademarks of the Common Core State Standards Initiative …
   All rights reserved." NGA Center and CCSSO, recorded as not IM's to sublicense.
5. **NCTM trademarks, third party.** "Notice and Wonder" and "I Notice/I Wonder" are NCTM marks
   used by IM with permission. Recorded: that permission runs to IM, not downstream.
6. **Image carve-out.** Non-IM images are public domain or CC-BY, recorded as a different and
   looser license than the site's BY-NC, and keep their own terms plus citation.
7. **No ShareAlike, no NoDerivatives.**
8. **Sign-in wall.** Recorded strings: "Sign in to access protected content and invite other
   educators" and "Sign in to view assessments and invite other educators", a Kendall Hunt
   account. Assessments unexamined.

## 7. Standards coverage as tagged on the host's own lesson pages

Recorded as read off the lesson pages themselves:

| lesson | standards tagged on page |
|---|---|
| Geo U3 §C L13 *Using the Pythagorean Theorem and Similarity* | HSG-SRT.A.3, B.4, B.5 |
| Geo U4 §B L6 *Working with Trigonometric Ratios* | C.6 |
| Geo U4 §B L7 *Applying Ratios in Right Triangles* | C.8 |
| Geo U4 §B L8 *Sine and Cosine in the Same Right Triangle* | C.6, C.7 |
| Geo U4 §B L10 *Using Trigonometric Ratios to Find Angles* | C.6, C.8 |
| Geo U4 §C L11 *Solving Problems with Trigonometry* | HSG-GMD.A.1, C.8 |

Recorded structure: Unit 3 Similarity has 17 lessons (§A Properties of Dilations 1-5;
§B Similarity Transformations and Proportional Reasoning 6-12; §C Similarity in Right Triangles
13-16; §D 17). Unit 4 Right Triangle Trigonometry has 12 lessons (§A Angles and Steepness /
Defining Trigonometric Ratios 1-5; §B 6-10; §C Let's Put It to Work 11-12).

Recorded as also available per unit and course: `/downloads`, `/glossary`,
`/learning-targets`, course-guide `/standards-by-lesson`, `/lessons-by-standard`. The last of
these never loaded; see the two HTTP 000 timeouts in section 1.

Note that the lesson counts on this host differ from the 1st-edition counts on
im.kendallhunt.com. Do not carry a count across hosts.

## 8. Recorded as not verified by the evidence file

- **No `/terms` exists on accessim.org.** Governing terms may live on the parent site
  `illustrativemathematics.org`, recorded as out of that agent's assigned scope and not fetched
  by it. The report explicitly declines to use another agent's file: "Another agent's file
  `im_org_tou.html` sits in this shared scratchpad with 9 hits for "commercial". It is NOT my
  evidence and I make no claim from it."
- The footer says "See the image attribution section" but supplies no hyperlink. The report read
  Course Guide §17 Attributions and states it cannot confirm that is the section meant, and that
  §17 holds no per-image citation list.
- No individual image citation inside a U3 or U4 lesson was opened.
- **No PDF opened.** The U4 `/downloads` HTML page was fetched with the CC BY-NC 4.0 footer
  present, but no actual PDF was downloaded, so whether the PDFs carry the same notice is
  unverified.
- Content behind the Kendall Hunt sign-in (assessments, "protected content") unexamined.
- Course-guide §18 Citations: page fetched at HTTP 200 but its body did not extract; not read.
- The copyright notice reads 2024 and was fetched 2026-08-07. Whether a newer notice exists
  elsewhere is recorded as unknown.
- Only the Geometry course was audited. K-5, 6-8, Algebra 1/2 and Integrated 1-3 pages are
  recorded as carrying the identical footer template, but the count was taken only on `/hs` and
  the Geometry tree.

## 9. Analysis recorded by the evidence file, not host text

Attribute to this project's own measurement, never to Illustrative Mathematics:

- The report calls the trademark carve-out "the sharpest rider" and observes that naming
  Illustrative Mathematics as a source in a citation is nominative use and normal, while
  branding with the mark or logo is not.
- The report characterises C.7 coverage on this host as "the thinnest (one lesson, U4 L8)".
- The report characterises the NC rider as satisfied where nothing is sold, and as a live
  constraint on any future monetisation.
