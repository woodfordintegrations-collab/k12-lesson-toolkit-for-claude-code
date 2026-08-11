---
title: "im.kendallhunt.com (IM K-12 Math, 1st edition)"
type: source
verdict: quote_and_adapt
fetched: 2026-08-07
sources:
  - https://illustrativemathematics.org/terms-of-use/
  - https://im.kendallhunt.com/HS/teachers/2/3/index.html
  - https://im.kendallhunt.com/MS/teachers/3/2/1/preparation.html
  - https://creativecommons.org/licenses/by/4.0/
  - sources/host-im-kendall-hunt.md
  - sources/host-im-task-bank.md
  - sources/host-accessim-360.md
  - sources/cc-by-4-0.md
  - sources/verdict-twelve-host-table.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# im.kendallhunt.com (IM K-12 Math, 1st edition)

## Summary

`im.kendallhunt.com` serves the first edition of IM K-12 Math under CC BY 4.0. Verdict:
`quote_and_adapt`. It is the only host in this project's twelve-host sweep that clears citation,
quotation and paraphrase-and-republish with no copyleft, which is why it is the spine the
curriculum build writes from.

Two facts about where the grant lives must always travel together, because either one alone
misleads:

1. The landing page carries **no licence text at all**. This project's fetch of the root recorded
   the entire footer as `Privacy Policy | Accessibility Information`, and a grep of the root HTML
   returned zero matches for `creative commons|CC BY|licens|copyright|attribution|all rights
   reserved`, measured across 27,884 bytes.
2. The grant lives **off-host**, in Illustrative Mathematics' central Terms of Use §7.1, and is
   confirmed on the deep curriculum-page footers of this host. A page that reports only fact 1
   concludes the host is unlicensed, which this project actually did once. A page that reports
   only fact 2 hides the reason the notice is hard to find.

**One organisation, three hosts, three different grants.** Lesson titles are near-identical across
them. Resolve the host before any reuse verdict attaches to a URL.

| Host in the URL | Edition | Licence | Verdict |
|---|---|---|---|
| `im.kendallhunt.com` | 1st edition, IM K-12 Math | CC BY 4.0 | `quote_and_adapt` (this page) |
| `curriculum.illustrativemathematics.org` | 301 redirect to the above, same site | CC BY 4.0 | `quote_and_adapt` (this page) |
| `accessim.org` | 2nd edition, IM TK-12 Math v.360 | CC BY-NC 4.0 | `quote_noncommercial`, see [[source-accessim-360]] |
| `tasks.illustrativemathematics.org` | 2016 task bank | CC BY-NC-SA 4.0 | `quote_sharealike`, see [[source-im-task-bank]] |
| `illustrativemathematics.org` | corporate marketing site | all rights reserved | not a resource host |
| `k12.kendallhunt.com` | print and distribution partner | all rights reserved | not a resource host |

**The required attribution string is not one string.** High school credits Illustrative
Mathematics 2019. Grades 6 to 8 must credit Open Up Resources 2017-2019 as the base copyright
holder. Crediting only IM on a `/MS/` page is an incorrect attribution. Both strings are set out
in full under "What you may do with it", with the URL test that selects between them.

## When to reach for it

Reach for this host when you need lesson prose, activity text, cool-down statements, practice
problems or teacher narrative that the repo may rewrite and ship. Under ruling R9 the repo itself
ships CC BY 4.0 and takes no paraphrase from any ShareAlike source, so this host and the plain-BY
sources beside it are the only ones an adapted through-line can rest on.

Reach for it for HSG-SRT specifically. IM HS Geometry is course id 2 on this host: Unit 3
*Similarity* has 16 lessons and Unit 4 *Right Triangle Trigonometry* has 11. Teacher pages
(`/HS/teachers/...`) carry lesson narrative, learning goals, activity launch and synthesis, and
student-response commentary. Student pages (`/HS/students/...`) are the task statements. Both are
plain HTML, no login.

Do **not** reach for this page when the material you are holding came from a different IM host.
An IM task with a numeric id under `/content-standards/` is the 2016 task bank and carries
ShareAlike. A v.360 lesson from `accessim.org` carries NonCommercial. Neither inherits this
page's verdict.

Do not reach for this host for assessment items behind the teacher wall. The End-of-Unit
Assessment and Check Your Readiness sit behind `/oauth_im/login`, and no agent in this project
registered or inspected them.

## What its own page says

Every quotation below was pasted by a fetching agent from live bytes on 2026-08-07 and is staged
verbatim in `sources/host-im-kendall-hunt.md`. Nothing here rests on a summarizing layer; see
[[trap-summary-layer-is-not-evidence]].

### The landing page, which says nothing about licensing

Entire root footer text, verbatim:

> Privacy Policy | Accessibility Information

`https://im.kendallhunt.com/` returned HTTP 200 with no bot block and no TLS error. `/terms`,
`/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/about` and `/faq` all returned 404 on
this host. `/privacy` and `/accessibility` returned 200 and carry no licence text. The notice is
injected into the same `<footer class="im-c-footer">` element, but only in the curriculum-content
templates. See [[trap-license-lives-off-the-obvious-page]].

### The off-host Terms of Use, which is where the grant lives

`https://illustrativemathematics.org/terms-of-use/`, HTTP 200, fetched 2026-08-07, header reads
**Effective as of May 21, 2026**. Its scope clause, verbatim, is what makes it govern this host:

> Unless otherwise noted on a particular website or service, these central terms and
> conditions of use ("Central Terms" or "Terms") apply to your use of all of the websites that
> the nonprofit corporation Illustrative Mathematics operates. These include
> https://illustrativemathematics.org , https://accessim.org , https://ca.accessim.org/,
> https://im.kendallhunt.com , together with all other subdomains thereof, (collectively, the
> "Websites"). The Terms also apply to all products, information, curriculum, and services
> provided through the Websites.

Section 7.1, the operative grant, verbatim:

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

The same document grants a **different** licence to a **different** edition on a **different**
host. Section 7.2, verbatim as staged, with the elision present in the transcription:

> **7.2 Curriculum License: IM® TK–12 Math v.360 | CC BY-NC**
> The second edition of IM K–12 Math, called IM TK–12 Math v.360 ("IM v.360") (© 2024 and IM
> TK Math © 2025) curriculum is freely accessible at accessim.org by teachers, students, and
> families as an Open Education Resource and is licensed under the Creative Commons
> Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). … Commercial use of the
> IM v.360 curriculum materials and name, including but not limited to incorporation into paid
> products or services or the name used for promotional purposes of third party products or
> services, is prohibited without prior written permission from Illustrative Mathematics.

Section 7.3, the brand carve-out, verbatim:

> Use of the Illustrative Mathematics name, brand, associated trademarks, or curriculum content
> beyond the scope of the applicable Creative Commons license requires express written
> permission from IM. Unauthorized commercial use or brand co-option is a violation of these
> Terms and may infringe IM's intellectual property rights. The Illustrative Mathematics®
> company name and associated trademarks ("IM®" and "IM Illustrative Mathematics Certified®")
> are not subject to use with Creative Commons licenses.

Section 6, reservation of rights, verbatim:

> Except as expressly stated in these Terms or in a separate written license agreement, IM
> reserves all rights in and to its intellectual property. No license or right is granted by
> implication, estoppel, or otherwise.

Section 8.3, verbatim:

> **8.3 Framing** No organization may frame any IM website or create a browser or border
> environment around any IM content without express written consent.

Section 9 prohibits, verbatim as recorded:

> Use automated tools (bots, scrapers, crawlers) to access the Websites in a manner that places excessive load on servers or circumvents technical access controls.

### The high school footer, verbatim

Recorded as present identically on every HS page sampled, for example
`https://im.kendallhunt.com/HS/teachers/2/3/index.html`, HTTP 200, fetched 2026-08-07:

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
`https://creativecommons.org/licenses/by/4.0/`. Note the ordering: the grant sentence is followed
immediately by a trademark carve-out and then by a third-party image carve-out. The three
sentences are one footer, and the two carve-outs are part of the notice, not decoration around it.

### The grades 6 to 8 footer, verbatim, and it is a different string

Source page `https://im.kendallhunt.com/MS/teachers/3/2/1/preparation.html`, HTTP 200, fetched
2026-08-07:

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
> The second set of English assessments (marked as set "B") are copyright 2019 by Open
> Up Resources, and are licensed under the Creative Commons Attribution 4.0 International
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

Same licence throughout, CC BY 4.0. Different copyright holder for the base curriculum, and
therefore a materially different attribution obligation. See [[concept-attribution-per-record]].

### The corporate sites, which are not under the grant

- `https://illustrativemathematics.org/` footer, verbatim: "All products and services are offered
  throughout the United States. Content on this page is licensed. © 2026, Illustrative
  Mathematics, all rights reserved."
- `https://k12.kendallhunt.com/` footer, verbatim: "© 2026 Kendall Hunt Publishing Company .
  All rights reserved."

The CC BY 4.0 grant attaches to the curriculum at `im.kendallhunt.com`. It does not attach to
marketing copy on either corporate site.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state what standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | attribution block below |
| Paraphrase and republish: rewrite its material and ship it | yes | attribution block below, and no copyleft attaches |

CC BY 4.0's own deed states both freedoms carry "for any purpose, even commercially", and its
"Under the following terms" list has exactly two items, Attribution and No additional
restrictions. Neither ShareAlike nor NoDerivatives appears on it. See [[license-cc-by]].

### The three components attribution must carry

IM's §7.1 names all three, and CC BY 4.0's deed matches: author credit, a hyperlink to the
licence, and an indication that changes were made. The changes-made indication is the component
adapters most often drop, and under 4.0 it is required whenever you Share, not only when you
adapt. The deed's own footnote also requires you to **retain** any indication of previous
modifications.

### Which URL band are you on

Run this test before writing any credit line. It has three outcomes, not two.

- URL contains `/HS/` → use the high school block.
- URL contains `/MS/` → use the grades 6 to 8 block. Crediting only IM here is wrong.
- URL is on this host but in neither band, for example a K-5 path → **stop.** This project sampled
  8 curriculum pages, of which all 7 HS pages carried the HS notice. The K-5 footer was never
  confirmed and the guessed path 404'd. Fetch the actual page footer and read it before crediting
  anything.

### Block A, high school, IM's own suggested string

```
Based on IM® K–12 Math authored by Illustrative Mathematics and licensed under CC BY 4.0.
https://creativecommons.org/licenses/by/4.0/
Source: https://im.kendallhunt.com/HS/  · Accessed 2026-08-07.
Changes were made to the original material.
```

### Block B, grades 6 to 8, a different string

```
IM 6–8 Math was originally developed by Open Up Resources and authored by Illustrative
Mathematics®, and is copyright 2017-2019 by Open Up Resources. It is licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0). Adaptations and updates
to IM 6–8 Math are copyright 2019 by Illustrative Mathematics, and are licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).
Source: https://im.kendallhunt.com/MS/  · Accessed 2026-08-07. Changes were made.
```

### What the grant does not reach

The grant covers IM's expression on this host. It does not cover:

- **The IM name, the IM logo and the "IM Certified" badge.** Carved out by the footer itself and
  again by Terms §7.3, and they require prior express written consent. Naming Illustrative
  Mathematics as a source in a citation is ordinary nominative use and is not affected; branding
  anything with the mark or the logo is.
- **Embedded third-party images.** The footer says the book includes public domain or openly
  licensed images copyrighted by their respective owners, which remain under their own terms. The
  index those images are attributed in could not be found; see the gotcha below.
- **The corporate marketing sites**, which are all rights reserved.
- **Anything behind `/oauth_im/login`**, which no agent in this project opened.

See [[concept-third-party-carve-out]].

## Gotchas & constraints

**1. The three-host conflation, and this project has made it in both directions.** Same
organisation, near-identical lesson titles, three grants. This project's own record contains both
failure modes. In one, a design ruling named IM task 1635 as CC BY 4.0 clean, when task 1635 lives
on `tasks.illustrativemathematics.org` and carries ShareAlike, so it cannot carry an adapted
through-line. In the other, an earlier sweep wrote IM off as NonCommercial-ShareAlike on the
strength of the task bank and lost the curriculum, which the wide sweep calls the precise error
that cost it its most useful source. Neither direction is safe. Resolve the host from the URL,
every time.

**2. The attribution string differs by grade band.** HS credits Illustrative Mathematics 2019.
Grades 6 to 8 must credit Open Up Resources 2017-2019 as the base copyright holder, with IM
credited for the adaptations. A single hard-coded IM credit line applied across a package that
cites a grade-8 prerequisite is an incorrect attribution. The K-5 band was never verified at all.

**3. The image attribution index could not be found, so no specific IM figure is cleared.** Every
curriculum footer says "See the image attribution section for more information", and this project
could not locate that section. All 8 guessed paths returned 404:
`/HS/teachers/2/attributions.html`, `/HS/teachers/2/image_attributions.html`,
`/HS/attributions.html`, `/HS/attributions/index.html`, `/attributions.html`,
`/HS/teachers/attributions.html`, `/HS/teachers/2/attributions/index.html`,
`/HS/teachers/2/8/attributions.html`. No `href` containing "attribution" exists in any sampled
page. The report's recorded consequence, verbatim: **"the per-image license status for any
specific IM figure is UNVERIFIED from here."** It may live in the print or PDF edition or behind
the teacher login. What would close it: register for a teacher account and inspect, or ask IM.
Until then, treat every figure in Units 3 and 4 as uncleared and reuse IM's text without IM's
images.

**4. A clean fetch of the obvious page returns "unlicensed", and this project believed it.** The
false belief is recorded verbatim in this project's own governing design: "im.kendallhunt.com
carries no license statement on its landing page. The CC BY 4.0 claim for that host is currently
unverified." It was corrected later. The lesson generalises past this host: see
[[trap-license-lives-off-the-obvious-page]].

**5. The terms are explicitly mutable.** The Terms of Use are headed "Effective as of May 21,
2026", eleven weeks before this fetch, and §4 reserves revision at IM's sole discretion. Two
grants in this corpus were withdrawn inside six months. This project's own re-verification trigger
says to re-pull this host's licence surface before the repository is published and to record the
new fetch date in the attribution block. See [[license-withdrawn-grants]].

**6. Sampling limit, stated plainly.** 8 curriculum pages of several thousand. The HS notice was
byte-identical across all 7 HS pages, which is strong evidence of a template, not proof of a
per-page decision. No Wayback cross-check was run against this host, so when the current footer
was introduced, and whether earlier snapshots carried different terms, is unknown.

**7. Access is not a rights fact, and neither is a 200.** Teacher resources that prompt "click
here to register or sign in" link to `/oauth_im/login`. The lesson `preparation.html` pages
fetched fine unauthenticated, but whether the full teacher materials sit behind a free
registration was recorded as unresolved. See [[trap-access-is-not-a-rights-fact]].

**8. Two use restrictions that are not licence terms.** §8.3 bars framing any IM website or
creating a border environment around IM content. §9 bars automated tools that place excessive load
on servers or circumvent access controls. `/robots.txt` returned 200 with only a comment line and
no `Disallow`, and this project's own sampling was roughly 20 requests, hand-paced.

**9. `k12.kendallhunt.com` is the print and distribution partner, not a resource host.** It was
fetched and its footer reads all rights reserved. IM the nonprofit operates `im.kendallhunt.com`
and IM's terms govern the curriculum there. Do not read the Kendall Hunt name in the domain as
putting the curriculum under a publisher's reservation of rights.

**10. Do not carry a lesson count across hosts.** This host records Unit 3 at 16 lessons and Unit
4 at 11. `accessim.org` records Unit 3 at 17 and Unit 4 at 12 for the same course. They are
different editions.

**11. The standard-to-lesson mappings are this project's own measurement, not IM's.** This
project's reading is that Unit 3 maps to B.4 and B.5, with lessons 5, 11, 13 and 14 as the B.4
proof spine and lessons 9 and 10 as the AA/SAS/SSS criteria; and that Unit 4 maps to C.6, C.7 and
C.8, with lesson 8 as the C.7 sine and cosine complement relationship. Attribute those to this
project, never to Illustrative Mathematics. Where a standards tag was read off a host's own lesson
page, that is a different and better class of fact, and it was done on `accessim.org`, not here.

## Related

- [[source-im-task-bank]] is the 2016 IM task bank on a different host under CC BY-NC-SA 4.0. The
  first place the conflation in gotcha 1 lands.
- [[source-accessim-360]] is the IM 2nd edition under CC BY-NC 4.0. The second place it lands, and
  the host where HTTP status proves nothing.
- [[license-cc-by]] holds the plain-attribution regime this host grants under, and the outbound
  obligation the repo takes on by shipping CC BY 4.0 itself.
- [[license-sharealike]] and [[license-noncommercial]] hold the riders the other two IM hosts
  carry, and are the reason their material cannot be mixed into a file with this host's.
- [[concept-attribution-per-record]] is why the credit line is a property of the record and the
  grade band, not of the host.
- [[concept-third-party-carve-out]] is the two classes of thing sitting outside the grant here:
  the embedded images, and the name and marks.
- [[concept-cite-quote-adapt]] is the three-operation split this page's verdict table applies.
- [[trap-license-lives-off-the-obvious-page]] is the worked failure this host produced.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above is a pasted byte rather than
  a fetch summary.
- [[trap-access-is-not-a-rights-fact]] covers the login wall and the plain-HTML availability.
- [[license-withdrawn-grants]] holds the mutability record that dates this verdict.

## Composes with

- [[practice-assemble-an-attribution-block]] consumes Block A and Block B above into the repo's
  shipped LICENSE and attribution file, and is where the URL-band test is executed per record.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict
  and is what re-running it before publication looks like.

## References

Host and rights-holder pages, fetched by this project on 2026-08-07:

- `https://illustrativemathematics.org/terms-of-use/` HTTP 200. §7.1 the operative CC BY 4.0
  grant, §7.2 the v.360 CC BY-NC grant, §7.3 trademark carve-out, §6 reservation of rights,
  §8.3 framing, §9 automated load; header "Effective as of May 21, 2026".
- `https://im.kendallhunt.com/HS/teachers/2/3/index.html` HTTP 200. Geometry Unit 3 Similarity
  index; the verbatim HS footer notice with its trademark and third-party image paragraphs.
- `https://im.kendallhunt.com/MS/teachers/3/2/1/preparation.html` HTTP 200. Grade 8 Unit 2
  preparation page; the different multi-party attribution string crediting Open Up Resources
  2017-2019.
- `https://im.kendallhunt.com/` HTTP 200. The root, whose entire footer is
  `Privacy Policy | Accessibility Information`.
- `https://illustrativemathematics.org/` and `https://k12.kendallhunt.com/` HTTP 200. The two
  all-rights-reserved corporate footers.
- `https://creativecommons.org/licenses/by/4.0/` HTTP 200, fetched 2026-08-08, 32178 bytes, and
  `https://creativecommons.org/licenses/by/4.0/legalcode.en` HTTP 200, 48970 bytes. The deed and
  legal code behind the attribution obligations above.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-im-kendall-hunt.md`, primary. Reachability table, the root-footer measurement, the
  two verbatim band footers, the Terms sections, the 8 sampled pages, and the image-attribution
  gap.
- `sources/host-im-task-bank.md`, primary. The CC BY-NC-SA 4.0 footer on the task bank, byte
  matched on all 24 in-scope task pages.
- `sources/host-accessim-360.md`, primary. The CC BY-NC 4.0 footer on v.360, and the soft-404
  measurement on that host.
- `sources/cc-by-4-0.md`, primary. The CC BY 4.0 deed and legal code staged verbatim.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 1, §3
  corrections 1, 5 and 6, §4.2 and §4.3 attribution blocks, §6 sampling limits and the
  re-verification trigger.
- `sources/verdict-wide-sweep.md`, reference. This project's own adjudication of eight sweep
  reports, recording the write-IM-off error and the four independent readings of the HS footer.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-im-kendall.md`, the underlying fetch report.
- `Projects/HS Geometry/sources/source-verdict-table.md`, the twelve-host adjudication.
- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 ruling R9, and §3 where the
  recorded false belief about this host's landing page lives.
