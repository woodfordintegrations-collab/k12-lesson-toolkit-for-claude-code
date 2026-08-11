---
source_url: hs-geometry-similarity-trig/sources/license-im-kendall.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-im-kendall-hunt, license-cc-by, license-noncommercial, license-withdrawn-grants, concept-attribution-per-record, concept-third-party-carve-out, practice-assemble-an-attribution-block, trap-license-lives-off-the-obvious-page, trap-license-withdrawn-after-citation
---

# Host extract: im.kendallhunt.com (Illustrative Mathematics K-12 Math, 1st edition)

**Original fetch date recorded by the evidence file: 2026-08-07.** Every fetch in the
underlying report carries that date. The `fetched:` field above is the staging date, not the
host-fetch date.

**Method recorded by the evidence file:** all fetches via `curl` with the browser user agent
`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36`.

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Reachability, as recorded

| URL | HTTP | Note |
|---|---|---|
| https://im.kendallhunt.com/ | 200 | live, no bot block, no TLS error |
| https://curriculum.illustrativemathematics.org/ | 200 after redirect | 301 to https://im.kendallhunt.com/, same site |
| /robots.txt | 200 | only a comment line, no Disallow |
| /terms /terms-of-use /copyright /permissions /license /about /faq | 404 | none exist |
| /privacy | 200 | privacy policy; NO license text |
| /accessibility | 200 | WCAG statement; NO license text |
| /HS/index.html | 200 | |
| /HS/teachers/2/index.html (Geometry) | 200 | |

Recorded characterisation of the stack: static-HTML Rails app, content server-rendered, no JS
needed.

## 2. The root landing page carries no license notice

The evidence file records that the root landing page footer contains no license notice at all.
The entire root footer text, verbatim:

> Privacy Policy | Accessibility Information

The report adds that the footer also carries the Kendall Hunt / IM combo logo image and the "IM
Certified" badge.

Measurement recorded: a grep of the root HTML returned ZERO matches for
`creative commons|CC BY|licens|copyright|attribution|all rights reserved`.

The license notice appears only on deep curriculum pages (unit indexes, lesson pages, student
pages). The report states it is injected into the same `<footer class="im-c-footer">` element
but only in the curriculum-content templates.

## 3. Verbatim license text, HIGH SCHOOL band

Recorded as present identically on every HS page sampled. Verbatim:

> © 2019 Illustrative Mathematics®. Licensed under the Creative Commons Attribution 4.0
> license.
>
> The Illustrative Mathematics name and logo are not subject to the Creative Commons
> license and may not be used without the prior and express written consent of Illustrative
> Mathematics.
>
> This book includes public domain images or openly licensed images that are copyrighted by
> their respective owners. Openly licensed images remain under the terms of their respective
> licenses. See the image attribution section for more information.

The phrase "Creative Commons Attribution 4.0" hyperlinks to
`https://creativecommons.org/licenses/by/4.0/`.

Note the ordering: the CC BY 4.0 grant sentence is immediately followed by a trademark
carve-out and then by a third-party image carve-out. The three sentences are one footer.

## 4. Verbatim license text, GRADES 6-8 band (different, multi-party)

Source page: `/MS/teachers/3/2/1/preparation.html` (grade 8, Unit 2, dilations/similarity),
HTTP 200. Verbatim:

> IM 6–8 Math was originally developed by Open Up Resources and authored by Illustrative
> Mathematics®, and is copyright 2017-2019 by Open Up Resources. It is licensed under the
> Creative Commons Attribution 4.0 International License (CC BY 4.0). OUR's 6–8 Math
> Curriculum is available at https://openupresources.org/math-curriculum/.
>
> Adaptations and updates to IM 6–8 Math are copyright 2019 by Illustrative Mathematics, and
> are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
>
> Adaptations to add additional English language learner supports are copyright 2019 by Open
> Up Resources, and are licensed under the Creative Commons Attribution 4.0 International
> License (CC BY 4.0).
>
> The second set of English assessments (marked as set "B") are copyright 2019 by Open Up
> Resources, and are licensed under the Creative Commons Attribution 4.0 International
> License (CC BY 4.0).
>
> Spanish translation of the "B" assessments are copyright 2020 by Illustrative Mathematics,
> and are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
>
> The Illustrative Mathematics name and logo are not subject to the Creative Commons license
> and may not be used without the prior and express written consent of Illustrative Mathematics.
>
> This site includes public domain images or openly licensed images that are copyrighted by
> their respective owners. Openly licensed images remain under the terms of their respective
> licenses. See the image attribution section for more information.

Recorded finding: the same license (CC BY 4.0 throughout) but a materially different
attribution string and a different copyright holder (Open Up Resources, not Illustrative
Mathematics) for the 6-8 base content.

## 5. Per-resource samples

All HTTP 200, fetched 2026-08-07:

1. `/HS/teachers/2/3/index.html`, Unit 3 Similarity index, HS notice present
2. `/HS/teachers/2/4/index.html`, Unit 4 Right Triangle Trig index, HS notice present
3. `/HS/teachers/2/3/13/preparation.html`, "Using the Pythagorean Theorem and Similarity", HS notice
4. `/HS/teachers/2/4/4/preparation.html`, "Ratios in Right Triangles", HS notice
5. `/HS/students/2/4/6/index.html`, student page, "Working with Trigonometric Ratios", HS notice
6. `/HS/students/2/3/9/index.html`, student page, "Conditions for Triangle Similarity", HS notice
7. `/HS/teachers/2/4/10/preparation.html`, "Solving Problems with Trigonometry", HS notice
8. `/MS/teachers/3/2/1/preparation.html`, grade 8, the different Open Up Resources multi-party notice

## 6. The governing terms document, off-host

`https://illustrativemathematics.org/terms-of-use/`, HTTP 200, header reads **Effective as of
May 21, 2026**. The evidence file records that `/terms/` 302-redirects here. Scope clause,
verbatim:

> Unless otherwise noted on a particular website or service, these central terms and
> conditions of use ("Central Terms" or "Terms") apply to your use of all of the websites that
> the nonprofit corporation Illustrative Mathematics operates. These include
> https://illustrativemathematics.org , https://accessim.org , https://ca.accessim.org/,
> https://im.kendallhunt.com , together with all other subdomains thereof, (collectively, the
> "Websites"). The Terms also apply to all products, information, curriculum, and services
> provided through the Websites.

The report reads this as resolving the IM-versus-Kendall-Hunt question: IM the nonprofit
operates im.kendallhunt.com and its terms govern the curriculum; Kendall Hunt is the print
publisher and distribution partner.

### Section 7.1, verbatim, the operative grant for this host

> **7.1 Curriculum License: IM® K–12 Math | CC BY 4.0**
> The first edition of IM K–12 Math curriculum (© 2019 – 2021) is freely accessible by
> teachers, students, and families as an Open Education Resource at http://im.kendallhunt.com
> and is licensed for use under the Creative Commons Attribution 4.0 International License
> (CC BY 4.0). Under the license, users are free to share and adapt the materials for any
> purpose, including commercially, with appropriate attribution to the author, Illustrative
> Mathematics, hyperlink to the license, and indication if changes were made. A suggested
> attribution is as follows: "Based on IM® K–12 Math authored by Illustrative Mathematics and
> licensed under CC BY 4.0." See Creative Commons for more information on the conditions
> license use.

### Section 7.2, verbatim, a different edition on a different host under CC BY-NC

The evidence file's transcription contains an elision, marked in the original with `…`. It is
reproduced here as recorded; the elided span was not captured.

> **7.2 Curriculum License: IM® TK–12 Math v.360 | CC BY-NC**
> The second edition of IM K–12 Math, called IM TK–12 Math v.360 ("IM v.360") (© 2024 and IM
> TK Math © 2025) curriculum is freely accessible at accessim.org by teachers, students, and
> families as an Open Education Resource and is licensed under the Creative Commons
> Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). … Commercial use of the
> IM v.360 curriculum materials and name, including but not limited to incorporation into paid
> products or services or the name used for promotional purposes of third party products or
> services, is prohibited without prior written permission from Illustrative Mathematics.

Recorded host-to-grant mapping: im.kendallhunt.com is the 1st edition under CC BY 4.0;
accessim.org and ca.accessim.org are v.360 under CC BY-NC 4.0. Same publisher, same brand,
different grant.

### Section 7.3, verbatim, brand carve-out

> Use of the Illustrative Mathematics name, brand, associated trademarks, or curriculum content
> beyond the scope of the applicable Creative Commons license requires express written
> permission from IM. Unauthorized commercial use or brand co-option is a violation of these
> Terms and may infringe IM's intellectual property rights. The Illustrative Mathematics®
> company name and associated trademarks ("IM®" and "IM Illustrative Mathematics Certified®")
> are not subject to use with Creative Commons licenses.

### Section 6, verbatim, reservation of rights

> Except as expressly stated in these Terms or in a separate written license agreement, IM
> reserves all rights in and to its intellectual property. No license or right is granted by
> implication, estoppel, or otherwise.

### Section 8.3, verbatim, framing

> **8.3 Framing** No organization may frame any IM website or create a browser or border
> environment around any IM content without express written consent.

### Section 9, quoted fragment, automated access

Section 9 prohibits, verbatim as recorded:

> Use automated tools (bots, scrapers, crawlers) to access the Websites in a manner that places excessive load on servers or circumvents technical access controls.

The evidence file notes alongside this that `/robots.txt` carries no Disallow, and that its own
sampling was approximately 20 requests, hand-paced.

## 7. Corporate marketing sites are not under the CC grant

- `https://illustrativemathematics.org/` footer, verbatim: "All products and services are
  offered throughout the United States. Content on this page is licensed. © 2026,
  Illustrative Mathematics, all rights reserved."
- Terms §3, verbatim (the transcription opens with an elision as recorded): "…the owner of
  United States registered trademarks Illustrative Mathematics®, IM®, IM Illustrative
  Mathematics Certified®, and the IM logo mark (U.S. Reg. Nos. 90021061 , 97412460 , 88330436 ,
  and 97412527 ) (the "Trademarks"). ALL RIGHTS RESERVED."
- `https://k12.kendallhunt.com/` footer, verbatim: "© 2026 Kendall Hunt Publishing Company .
  All rights reserved."

The evidence file states the CC BY 4.0 grant attaches to the curriculum at im.kendallhunt.com,
not to the marketing copy on either corporate site.

## 8. Access gate

Some teacher resources prompt "click here to register or sign in" with a link to
`/oauth_im/login`. The lesson `preparation.html` pages fetched fine unauthenticated. The report
records as unresolved whether full teacher materials sit behind a free teacher registration.

## 9. GAP, recorded as could not verify

The footer on every curriculum page says "See the image attribution section for more
information." The evidence file records that this section could not be located. Probed and got
404 on:

`/HS/teachers/2/attributions.html`, `/HS/teachers/2/image_attributions.html`,
`/HS/attributions.html`, `/HS/attributions/index.html`, `/attributions.html`,
`/HS/teachers/attributions.html`, `/HS/teachers/2/attributions/index.html`,
`/HS/teachers/2/8/attributions.html`.

No `href` containing "attribution" exists in any sampled page. The report notes it may live in
the print or PDF edition, or behind the teacher login.

**Recorded consequence, verbatim from the report: "the per-image license status for any specific
IM figure is UNVERIFIED from here."**

## 10. Riders, as enumerated by the evidence file

1. Attribution required, the CC BY 4.0 core obligation.
2. Trademark carve-out: the IM name and logo are excluded from the CC license and written
   consent is needed. This includes the "IM Certified" badge.
3. Third-party image carve-out: images may be public domain or separately licensed and remain
   under their own terms. The CC BY 4.0 grant does not cover them.
4. Different attribution string for grades 6-8: Open Up Resources must be credited, not IM
   alone.
5. No ShareAlike, no NonCommercial, no NoDerivatives on the HS content.

## 11. What the host offers on HSG-SRT.B.4 / B.5 / C.6 / C.7 / C.8

IM HS Geometry is course id 2 on this host.

**Unit 3 Similarity, 16 lessons**, recorded titles in order: 1 Scale Drawings · 2 Scale of the
Solar System · 3 Measuring Dilations · 4 Dilating Lines and Angles · 5 Splitting Triangle Sides
with Dilation Part 1 · 6 Connecting Similarity and Transformations · 7 Reasoning about
Similarity with Transformations · 8 Are They All Similar? · 9 Conditions for Triangle
Similarity · 10 Other Conditions for Triangle Similarity · 11 Splitting Triangle Sides with
Dilation Part 2 · 12 Practice With Proportional Relationships · 13 Using the Pythagorean
Theorem and Similarity · 14 Proving the Pythagorean Theorem · 15 Finding All the Unknown Values
in Triangles · 16 Bank Shot

**Unit 4 Right Triangle Trigonometry, 11 lessons**, recorded titles in order: 1 Angles and
Steepness · 2 Half a Square · 3 Half an Equilateral Triangle · 4 Ratios in Right Triangles ·
5 Working with Ratios in Right Triangles · 6 Working with Trigonometric Ratios · 7 Applying
Ratios in Right Triangles · 8 Sine and Cosine in the Same Right Triangle · 9 Using Trigonometric
Ratios to Find Angles · 10 Solving Problems with Trigonometry · 11 Approximating Pi

Page-type note recorded: teacher pages (`/HS/teachers/...`) include lesson narrative, learning
goals, activity launch and synthesis, and student-response commentary. Student pages
(`/HS/students/...`) are the task statements.

### Analysis recorded by the evidence file, not host text

The report, not the host, asserts the following standard mappings. Attribute them to this
project's own measurement, never to Illustrative Mathematics:

- Unit 3 maps to B.4 and B.5; lessons 5, 11, 13, 14 are called the B.4 proof spine
  (side-splitter, Pythagorean via similarity); lessons 9 and 10 are called the AA/SAS/SSS
  similarity criteria.
- Unit 4 maps to C.6, C.7 and C.8; lesson 8 is called the C.7 sine and cosine complement
  relationship; lessons 2 and 3 are called the special right triangles; lesson 4 is called the
  C.6 ratio-defined-by-similarity derivation.
