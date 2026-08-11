---
title: "accessim.org (IM TK-12 Math v.360, 2nd edition)"
type: source
verdict: quote_noncommercial
fetched: 2026-08-07
sources:
  - https://accessim.org/9-12-aga/geometry
  - https://accessim.org/9-12-aga/geometry/course-guide/attributions?a=teacher
  - https://illustrativemathematics.org/terms-of-use/
  - https://creativecommons.org/licenses/by-nc/4.0/
  - sources/host-accessim-360.md
  - sources/cc-by-nc-4-0.md
  - sources/host-im-kendall-hunt.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# accessim.org (IM TK-12 Math v.360, 2nd edition)

## Summary

`accessim.org` serves the second edition of IM's curriculum, IM TK-12 Math v.360, under CC BY-NC
4.0. Verdict: `quote_noncommercial`. The grant is uniform: 13 of 13 curriculum pages sampled carry
one CC BY-NC 4.0 notice, with zero ShareAlike, zero NoDerivatives and zero plain CC BY anywhere on
the host.

Two measurement facts about this host are worth more than the licence label, because both of them
turn a correct observation into a wrong conclusion:

1. **Every path returns HTTP 200, including paths that do not exist.**
   `/zzz-definitely-not-a-real-page-9876` returns 200 at 1,486,023 bytes. A Next.js dynamic
   catch-all swallows unknown paths into a soft 404. So a 200 on `/terms` is not evidence that
   `/terms` exists, and existence on this host has to be tested by byte-diff. See
   [[trap-soft-404-status-proves-nothing]].
2. **The word "commercial" appears zero times across all 19 pages fetched from this host.** The
   NonCommercial restriction is carried solely by the licence label and its hyperlink. A grep of
   this host for a commercial prohibition returns nothing, and that absence is a true measurement
   attached to a false conclusion. The prohibition prose exists, off-host, in IM's central Terms
   §7.2.

**Same organisation, near-identical lesson titles, a different grant from the host next door.**
`im.kendallhunt.com` is the first edition under CC BY 4.0 and is the only IM surface this repo may
adapt from; see [[source-im-kendall-hunt]]. `tasks.illustrativemathematics.org` is the 2016 task
bank under CC BY-NC-SA 4.0; see [[source-im-task-bank]]. Neither verdict transfers here, and this
one does not transfer to them.

## When to reach for it

Reach for this host when you want the second edition specifically, and say so, because it is a
different book. Geometry Unit 3 *Similarity* has **17** lessons here and Unit 4 *Right Triangle
Trigonometry* has **12**. The first edition records 16 and 11 for the same units. Those are two
editions, not a discrepancy to reconcile, and a lesson number is not portable between them.

Reach for it for **standards tags read off the host's own lesson pages**, which is a stronger class
of fact than a mapping this project inferred. Recorded from the pages themselves:

| Lesson | Standards tagged on the page |
|---|---|
| Geo U3 §C L13 *Using the Pythagorean Theorem and Similarity* | HSG-SRT.A.3, B.4, B.5 |
| Geo U4 §B L6 *Working with Trigonometric Ratios* | C.6 |
| Geo U4 §B L7 *Applying Ratios in Right Triangles* | C.8 |
| Geo U4 §B L8 *Sine and Cosine in the Same Right Triangle* | C.6, C.7 |
| Geo U4 §B L10 *Using Trigonometric Ratios to Find Angles* | C.6, C.8 |
| Geo U4 §C L11 *Solving Problems with Trigonometry* | HSG-GMD.A.1, C.8 |

Reach for it while nothing is sold. NonCommercial is dormant in a repository that charges for
nothing and becomes unlicensable the moment one is monetised, at which point every file touched by
this host has to come out. See [[license-noncommercial]].

Do **not** reach for this host when the CC BY 4.0 first edition would serve, because taking v.360
imports NC for no gain. Do not reach for it for anything behind the Kendall Hunt sign-in: the
recorded prompts are "Sign in to access protected content and invite other educators" and "Sign in
to view assessments and invite other educators", and no agent in this project registered. A sign-in
wall is an access fact, and access facts are not rights facts; see
[[trap-access-is-not-a-rights-fact]].

## What its own page says

Every quotation below is transcribed from `sources/host-accessim-360.md`, staging an evidence file
whose fetches were all made on 2026-08-07 with `curl` over raw bytes and, where noted, extraction
from raw HTML rather than a rendered DOM.

### The footer, present on every curriculum-scoped page

Raw HTML as served:

```html
<div class="im-c-footer__licensing im-u-grid--gap-lg">
<p>Illustrative Mathematics® has operated as an independent 501(c)3 non-profit organization since 2013.</p>
<p>©2024 Illustrative Mathematics®. Licensed under<!-- --> <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>.</p>
<p>The Illustrative Mathematics name and logo are not subject to the Creative Commons license and may not be used without the prior and express written permission of Illustrative Mathematics.</p>
<p>This site includes public domain images or openly licensed images that are copyrighted by their respective owners. Openly licensed images remain under the terms of their respective licenses. See the image attribution section for more information.</p>
</div>
```

Rendered, the grant is four words and a link: `©2024 Illustrative Mathematics®. Licensed under
CC BY-NC 4.0.` The link resolves to `https://creativecommons.org/licenses/by-nc/4.0/`. The
copyright year on the notice is **2024**, fetched 2026-08-07.

Note the ordering, which is the same on both IM curriculum hosts: the grant sentence, then the
trademark carve-out, then the third-party image carve-out. Those three paragraphs are one footer
block, and the two carve-outs are part of the notice rather than decoration around it. See
[[concept-third-party-carve-out]].

### Where the footer is not

The evidence file's own words:

> The homepage and privacy policy carry **no license notice at all** — the footer is
> rendered only inside the curriculum route tree. Anyone checking only `accessim.org/`
> would conclude the site is unlicensed. It isn't; you have to be on a curriculum page.

This is the third IM host on which the obvious page returns nothing. See
[[trap-license-lives-off-the-obvious-page]].

### The per-page audit, and the zero that matters

Nineteen pages were fetched and counted for `licenses/by-nc/4.0`, `by-sa`, `by-nd`, plain `by/4.0`
and the word "commercial". Thirteen curriculum pages returned exactly one `by-nc` hit each and zero
of everything else. The homepage, `/privacy-policy`, `/terms` and the bogus slug returned zero
`by-nc` hits. **"commercial" returned 0 hits on all 19.**

Zero SA and zero ND is a positive finding: adaptation is permitted here with no copyleft attached,
where the task bank permits it only at the price of relicensing and [[source-mars-map]] does not
permit it at all. Zero "commercial" is not a finding about permission at all.

### There is no terms page on this host, and the 200s do not say otherwise

The evidence file's conclusion, verbatim:

> **accessim.org has no site-wide terms-of-use, copyright, or license page.**

The paths `/terms`, `/terms-of-use`, `/terms-of-service`, `/copyright`, `/license`, `/licensing`,
`/permissions`, `/about`, `/faq`, `/attribution`, `/attributions` and `/legal` all return 200 at
approximately 1,485,7xx bytes and are the same shell. A byte-diff of `/terms` against the bogus slug
is recorded as identical except for the echoed slug in nav hrefs and the per-request Sentry trace
id. The only real distinct policy page is `/privacy-policy` at 120,462 bytes, confirmed to contain
no copyright, IP, licence, CC, permitted-use or redistribution text.

### The commercial prohibition, which lives off-host

The host agent recorded that governing terms might live on the parent site, that this was outside
its assigned scope, and that it would not borrow another agent's file. Verbatim:

> Another agent's file `im_org_tou.html` sits in this shared scratchpad with 9 hits for "commercial". It is NOT my evidence and I make no claim from it.

That discipline is correct and it leaves a gap this wiki can close from a sibling extract rather
than from memory. `sources/host-im-kendall-hunt.md` stages a fetch of
`https://illustrativemathematics.org/terms-of-use/` made on 2026-08-07, HTTP 200, header "Effective
as of May 21, 2026". Its scope clause names this host by URL, and §7.2 is the grant for this
edition. Verbatim as staged, with the elision present in the transcription:

> **7.2 Curriculum License: IM® TK–12 Math v.360 | CC BY-NC**
> The second edition of IM K–12 Math, called IM TK–12 Math v.360 ("IM v.360") (© 2024 and IM
> TK Math © 2025) curriculum is freely accessible at accessim.org by teachers, students, and
> families as an Open Education Resource and is licensed under the Creative Commons
> Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). … Commercial use of the
> IM v.360 curriculum materials and name, including but not limited to incorporation into paid
> products or services or the name used for promotional purposes of third party products or
> services, is prohibited without prior written permission from Illustrative Mathematics.

The prose the host itself does not carry is in that section, and it is broader than the CC deed's
NonCommercial condition: it reaches the **name** as well as the materials.

### Course Guide §17 "Attributions", verbatim in full

URL `https://accessim.org/9-12-aga/geometry/course-guide/attributions?a=teacher`, HTTP 200,
1,521,128 bytes. The content lives in the RSC flight payload rather than the initial DOM, so a
fetcher that reads the rendered document truncates before reaching it; this text was extracted from
raw HTML.

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

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state which standard a lesson is tagged to, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | attribution block below; NC still binds the use |
| Paraphrase and republish: rewrite its material and ship it | yes | attribution block below, and NC attaches downstream |

**There is no copyleft here.** CC BY-NC 4.0's "Under the following terms" list has exactly three
items, `Attribution`, `NonCommercial` and `No additional restrictions`, measured on the fetched
deed. You may adapt, and your derivative does not have to ship under CC BY-NC 4.0. What travels
downstream is the NC constraint on the underlying material, not a licence obligation on your own
contribution. The single downstream-licence rule is legal code Section 3(a)(4), verbatim:

> If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

That is a materially weaker obligation than ShareAlike, and the two are routinely collapsed. Compare
[[license-sharealike]], where the adapter's licence is dictated rather than merely constrained.

**NC is written into the grant, not bolted onto it.** Legal code Section 2(a)(1), verbatim:

> reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
>
> produce, reproduce, and Share Adapted Material for NonCommercial purposes only.

The deed's own definition, verbatim: "A commercial use is one primarily intended for commercial
advantage or monetary compensation." The test is the intent of the use, not the tax status of the
user.

Practically, for a repository that ships CC BY 4.0, taking adapted material from here is what
breaks. A CC BY 4.0 file cannot carry material whose underlying grant is NonCommercial without the
NC term following it. See [[license-cc-by]].

### Attribution block

No canonical attribution string is prescribed anywhere on this site. This project's block:

```
©2024 Illustrative Mathematics®. Licensed under CC BY-NC 4.0.
https://creativecommons.org/licenses/by-nc/4.0/
Source: https://accessim.org/9-12-aga/geometry  · Accessed 2026-08-07. Changes were made.
```

Under 4.0 the changes-made indication is required whenever you Share, not only when you adapt. See
[[concept-attribution-per-record]] for why the string belongs to the record rather than to the host.

### What the grant does not reach

- **The IM name and logo**, carved out by the footer itself and again by central Terms §7.3, and
  requiring prior express written permission. Naming Illustrative Mathematics in a citation is
  ordinary nominative use and is unaffected; branding anything with the mark is not.
- **The Common Core State Standards trademarks**, which §17 attributes to the NGA Center and CCSSO
  with all rights reserved. Those are not IM's to sublicense.
- **The NCTM marks "Notice and Wonder" and "I Notice/I Wonder"**, used by IM with permission. §17
  says "used here with permission", and a permission that runs to IM does not run to a downstream
  reuser. This is the carve-out most likely to be missed, because the phrase reads like ordinary
  pedagogical vocabulary rather than a mark.
- **Non-IM images**, which §17 places in the public domain or under CC BY with their own citation.
  Note the direction: that is **looser** than the site's own BY-NC, not stricter, which inverts what
  a carve-out usually signals. It is still a separate grant with separate terms, and the footer
  points at an "image attribution section" that has no hyperlink anywhere on the host.

## Gotchas & constraints

**1. A 200 proves nothing here, and this is the host that proves it.** The measured control is
`/zzz-definitely-not-a-real-page-9876` at HTTP 200 and 1,486,023 bytes, with the Sentry transaction
on that page recorded as `GET /[curriculum_slug]`. Any existence claim about a path on this host has
to be a byte-diff claim.

**2. "No commercial prohibition on this host" is true and misleading.** Zero hits across 19 pages.
The prohibition is real, it is at central Terms §7.2, and a reader who greps only this host and
concludes NC is unenforced has drawn the wrong inference from a correct measurement.

**3. Do not carry a lesson count, a lesson number or a unit structure across editions.** 17 and 12
lessons here against 16 and 11 on the first edition. Section structure is recorded here as U3 §A
1-5, §B 6-12, §C 13-16, §D 17, and U4 §A 1-5, §B 6-10, §C 11-12. Citing "IM Geometry Unit 4 Lesson
8" without naming the edition and the host identifies two different lessons.

**4. C.7 is the thinnest seam on this host, and that is all it is.** C.7 was found tagged on exactly
one lesson, U4 L8. That measurement is correct about accessim.org. This project's later wide sweep
retires the generalisation that C.7 is scarce in the corpus, having found 37 distinct C.7 sources.
Cite the host-level count, never the general claim.

**5. Two fetches failed server-side, and neither was a block.**
`/9-12-aga/geometry/course-guide/lessons-by-standard?a=teacher` failed twice, `curl (28) Connection
timed out after 40005 ms` then `curl (35) Recv failure: Operation timed out` at 38.8s, HTTP 000, and
was never retrieved. A lesson preparation page in Unit 4 failed the same way while its siblings
fetched fine. The complete standards-to-lesson alignment table is therefore **unread**, and the
per-lesson tags in the table above are what was read off individual pages instead. See
[[trap-down-is-not-one-state]].

**6. No PDF was opened.** The Unit 4 `/downloads` HTML page carries the CC BY-NC 4.0 footer, but no
actual PDF was downloaded, so whether the downloadable artifacts carry the same notice is
unverified. On another host in this corpus the artifact and the page serving it say different
things, which is why this gap is worth naming; see [[source-mars-map]].

**7. Scope was Geometry only.** K-5, grades 6 to 8, Algebra 1 and 2, and Integrated 1 to 3 are
recorded as carrying the identical footer template, but the count was taken on `/hs` and the
Geometry tree. Course Guide §18 Citations returned 200 and its body did not extract, so it was never
read. No individual image citation inside a Unit 3 or Unit 4 lesson was opened.

**8. The notice reads 2024 and the fetch is 2026-08-07.** Whether a newer notice exists elsewhere on
the host is recorded as unknown. IM's central Terms are revisable at IM's sole discretion and were
headed "Effective as of May 21, 2026", eleven weeks before that fetch. Two grants in this corpus
were withdrawn inside six months; see [[license-withdrawn-grants]].

**9. The trademark carve-out is called the sharpest rider here by this project, not by IM.** So is
the reading that C.7 coverage on this host is thin, and the reading that NC is satisfied while
nothing is sold. Those are this project's characterisations of host text, and they must not be
quoted as Illustrative Mathematics' own statements.

## Related

- [[source-im-kendall-hunt]] is the first edition under CC BY 4.0, the host whose verdict is the one
  people mean when they say "IM is CC BY", and the only IM surface this repo adapts from.
- [[source-im-task-bank]] is the 2016 task bank under CC BY-NC-SA 4.0, the third IM grant.
- [[license-noncommercial]] holds the NC rider, and this host is its cleanest instance: a
  restriction carried entirely by a label and a hyperlink.
- [[license-cc-by]] is the outbound grant this repo ships, and the reason NC material cannot be
  folded into it.
- [[license-sharealike]] is the stronger obligation this licence does **not** carry, kept next to it
  because the two get collapsed.
- [[concept-third-party-carve-out]] is the three classes of thing outside the grant here: the marks,
  the CCSS and NCTM third-party trademarks, and the images.
- [[concept-attribution-per-record]] is why the credit line belongs to the record.
- [[trap-soft-404-status-proves-nothing]] is the failure mode this host demonstrates most cleanly.
- [[trap-license-lives-off-the-obvious-page]] is the root-carries-nothing pattern across all three
  IM hosts.
- [[trap-access-is-not-a-rights-fact]] covers the Kendall Hunt sign-in wall.
- [[trap-down-is-not-one-state]] is why the two HTTP 000 results here are timeouts, not blocks.
- [[license-withdrawn-grants]] holds the mutability record that dates this verdict.

## Composes with

- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict, and
  the byte-diff existence test in gotcha 1 is one of its steps.
- [[practice-assemble-an-attribution-block]] consumes the block above, and is where a v.360 record is
  kept out of a file that must stay commercially clean.

## References

Host pages, fetched by this project on 2026-08-07:

- `https://accessim.org/9-12-aga/geometry` HTTP 200. The curriculum footer in raw HTML, uniform
  across all 13 curriculum pages sampled and absent from the homepage and privacy policy.
- `https://accessim.org/9-12-aga/geometry/course-guide/attributions?a=teacher` HTTP 200, 1,521,128
  bytes. Course Guide §17, quoted in full above.
- `https://accessim.org/` HTTP 200, 169,069 bytes with the default user agent, and
  `/zzz-definitely-not-a-real-page-9876` HTTP 200, 1,486,023 bytes. The soft-404 control.
- `https://accessim.org/privacy-policy` HTTP 200, 120,462 bytes. The only real distinct policy page.
- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, header "Effective as of May 21,
  2026". §7.2, quoted here from a staged extract fetched for a sibling host, not for this one.
- `https://creativecommons.org/licenses/by-nc/4.0/` HTTP 200, 35485 bytes, and its `legalcode.en`
  HTTP 200, 50209 bytes, fetched 2026-08-08.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-accessim-360.md`, primary. The soft-404 measurement, the 19-page licence audit,
  Course Guide §17, the per-lesson standards tags, the riders, and the unverified list.
- `sources/cc-by-nc-4-0.md`, primary. Deed and legal code verbatim, including the measured absence
  of ShareAlike and NoDerivatives.
- `sources/host-im-kendall-hunt.md`, primary. The central IM Terms, source of §7.2 above.
- `sources/verdict-twelve-host-table.md`, reference. Row 4, §3 correction 2, §4.4 the attribution
  block, and the partial retirement of the C.7 scarcity claim.

This project's own working files, cited as this project's measurement and not as any outside party's
statement: `Projects/HS Geometry/sources/license-im-360.md`, the underlying fetch report.
