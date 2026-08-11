---
title: "map.mathshell.org (MARS / Mathematics Assessment Project)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://map.mathshell.org/
  - https://map.mathshell.org/tasks.php?unit=HA05&collection=9
  - https://map.mathshell.org/pd.php
  - https://map.mathshell.org/stds.php?standardid=1400
  - https://creativecommons.org/licenses/by-nc-nd/3.0/
  - sources/host-mars-map.md
  - sources/cc-by-nc-nd-3-0.md
  - sources/cc-by-nc-sa-3-0.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# map.mathshell.org (MARS / Mathematics Assessment Project)

## Summary

`map.mathshell.org` publishes **four different licence regimes on one host, and says so on its own
homepage**. Verdict: `cite_only`. The site's own sentence is the headline fact:

> All our materials can be downloaded for free and may be reproduced as-is for
> non-commercial use. Precise terms vary between materials. Enquiries to:
> map.info@mathshell.org.

There is no single site-wide grant to quote, and the four regimes do not agree with each other:

| Material | Regime | Where it was read |
|---|---|---|
| Classroom Challenges | CC BY-NC-ND 3.0 Unported, "unmodified" | per-lesson page sidebox, byte-identical on 5 pages |
| Summative Assessment Tasks and Prototype Tests | CC BY-NC-ND 3.0 Unported, "unmodified" | per-task page sidebox, byte-identical on 4 pages |
| Professional Development Modules | **CC BY-NC-SA 3.0**, ShareAlike, no "unmodified" | `pd.php` |
| TRU Math Suite | **no licence statement at all** | `trumath.php`, zero hits for licence keywords |

Two further facts a reader has to carry off this page:

1. **The PDF and the web page serving it say different things.** `hopewell_geometry.pdf` carries
   "Copyright © 2011 by Mathematics Assessment Resource Service. All rights reserved." with no CC
   text anywhere, while the page that links to it grants CC BY-NC-ND 3.0. Its companion rubric PDF
   carries no notice of any kind. **The page is the evidence, so archive the page, not the file.**
2. **NoDerivatives here is stronger than its own deed makes it sound.** The deed implies you may
   modify privately so long as you do not distribute. The 3.0 legal code grants no adaptation right
   at all and reserves everything not expressly granted. That is why the verdict is `cite_only` and
   must not be softened.

## When to reach for it

Reach for it as a **design reference and a citation**, which is where its value actually is. The
Summative Assessment Tasks ship four files each: the task PDF, a rubric PDF, and two
annotated-student-work PDFs, unscored and scored. This project's own reading is that the scored
annotated student work is a genuinely unusual asset for a misconceptions section, and that reading
is this project's, not MARS's.

Reach for its **published CCSSM crosswalk**, `stds.php?standardid=1400`, which is MARS's own mapping
of its materials to G-SRT and is citable as a published alignment. Read it with its defects named:
its "Prove theorems involving similarity" cluster gives three Classroom Challenges (Rolling Cups,
Floodlight Shadows, Evaluating Statements About Length and Area), and its "Define trigonometric
ratios" cluster gives four more but includes "Solving Quadratic Equations". This project calls that
second mapping thin and partly spurious. The mapping itself is MARS's.

The strongest single item on the host for this unit is **Hopewell Geometry (HA05)**: right-triangle
earthworks, asking the hypotenuse of a 1-by-7 right triangle to one decimal place, the smallest
angle of a 3-4-5 triangle to one decimal place, and recognition of an enlargement by scale factor 3.
The rubric's answer key contains, verbatim, `sin-1 3/5 or cos-1 3/5 or tan-1 3/4`.

Do **not** reach for this host for text that will enter the repository in any form. Nothing here is
adaptable and, on this wiki's verdict, nothing here is quotable either. See
[[practice-cite-without-redistributing]] for how a source like this still shapes a build.

Do not reach for it for C.6 or C.7 lessons. The measured gap: **no Classroom Challenge states a goal
of defining sine, cosine or tangent from similarity, or of the sine and cosine complementary
relationship.** That is a fact about MARS. This project's wide sweep separately retires the
generalisation that C.7 is scarce overall.

## What its own page says

Every quotation below is transcribed from `sources/host-mars-map.md`, staging an evidence file whose
own note reads: "Every claim below is backed by a fetch performed in this session. Nothing here is
from training knowledge." All fetches 2026-08-08 UTC, server date header confirmed as
`Sat, 08 Aug 2026`.

### The global footer, which is an assertion and not a grant

Present on every page tested, verbatim:

> State, district and CCSSI standards appear courtesy of their respective
> authors. All other material Copyright © 2007-2015 Mathematics
> Assessment Resource Service, University of Nottingham.

A bare copyright assertion. The first sentence is a third-party carve-out for the CCSS text
reproduced inside MAP materials, which is not MARS's to license; see
[[concept-third-party-carve-out]].

### Classroom Challenges, per-lesson page sidebox

Byte-identical on all five lesson pages checked, all HTTP 200, verbatim:

> The *Classroom Challenges* materials may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

The link href is `http://creativecommons.org/licenses/by-nc-nd/3.0/`. No jurisdiction code, so
**Unported**. The link itself is plain `http://`.

### Summative Assessment Tasks, per-task page sidebox

Byte-identical across all four task pages checked, verbatim:

> The *Summative Assessment Tasks* may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

Same href. The Prototype Tests page states the same grant in different words, dropping "copied",
verbatim:

> The Summative Assessment Tasks may be distributed, unmodified,
> under the [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0].
> All other rights reserved. Please send any enquiries about commercial
> use or derived works to map.info@mathshell.org.
>
> **Note:** please bear in mind that these prototype materials need some further trialing
> before inclusion in a high-stakes test.

### PD Modules, the one different licence on the host

`https://map.mathshell.org/pd.php`, HTTP 200, verbatim:

> The Professional Development Modules may be distributed under the
> [Creative Commons Attribution Noncommercial Share-Alike license]. Please
> send any enquiries about commercial use to map.info@mathshell.org.

Href `http://creativecommons.org/licenses/by-nc-sa/3.0/`. Three differences from every other grant
on the host, all measured: the **visible text carries no version number** and only the href says
3.0; there is no "unmodified"; and there is no "all other rights reserved".

### TRU Math Suite, silence

`https://map.mathshell.org/trumath.php`, HTTP 200. The full page body was extracted and searched:
**zero** hits for creativecommons, license, reproduce, or rights reserved. Only the global footer
applies, and the global footer is an assertion. See [[license-unmarked-silence]].

### The index pages carry nothing, and there is no licence page

`lessons.php`, `tasks.php` and `stds.php` all return 200 with **0 hits for "creativecommons"**. The
grant appears only on individual resource pages. Fourteen policy paths were probed with a browser
user agent and all returned 404: `/terms`, `/terms-of-use`, `/terms.php`, `/copyright`,
`/copyright.php`, `/permissions`, `/permissions.php`, `/license`, `/license.php`, `/licence`,
`/about`, `/faq`, `/faq.php`, `/legal`. The About page is `/background.php`, HTTP 200, carrying no
terms text.

### The artifacts contradict the pages that serve them

**Classroom Challenge lesson PDF**, `download.php?fileid=1754`, served as `enlargements r1.pdf`,
2,745,271 bytes, agrees with its page. Cover, verbatim:

> © 2015 MARS, Shell Center, University of Nottingham
> May be reproduced, unmodified, for non-commercial purposes under the Creative Commons license
> detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/ - all other rights reserved

**Summative task PDF**, `download.php?fileid=499`, served as `hopewell_geometry.pdf`, 93,563 bytes,
does not. Both pages carry, verbatim, as a running footer:

> Copyright © 2011 by Mathematics Assessment
> Resource Service. All rights reserved.

The recorded finding: the PDF grants nothing, and the CC BY-NC-ND 3.0 grant for that file exists
only on the HTML page linking to it. Anyone who receives the PDF alone sees pure all-rights-reserved
and has no way to discover otherwise.

**Summative task rubric PDF**, `download.php?fileid=500`, `hopewell_geometry_rubric.pdf`, 144,913
bytes. Text extracted cleanly, recorded as 36 lines with content verified readable. **Zero** hits
for copyright, license, creative commons, or rights reserved. Silent.

**Teacher guide PDF**, `docs/map_cc_teacher_guide.pdf`, 706,151 bytes, states CC BY-NC-ND 3.0 twice,
including inside front matter, verbatim:

> © 2013-2015 MARS, Shell Center, University of Nottingham.
> This document may be distributed, unmodified, under the Creative Commons Attribution, Non-
> commercial, No Derivatives License 3.0 detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/
> All other rights reserved. Please send any enquiries about commercial use or derived works to
> map.info@mathshell.org.

So of four artifacts opened, two carry the grant, one asserts all rights reserved against its own
page, and one is silent. **The regime is a property of the file, not of the host.**

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state which standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | **no**, on this wiki's verdict | see below |
| Paraphrase and republish: rewrite its material and ship it | **no** | ND grants no adaptation right at all |

### Why the ND verdict is harder than the deed reads

The deed's NoDerivatives sentence is conditional and speaks only to distribution, verbatim:

> **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material.

Read alone, that says you may make a modified version privately. The 3.0 legal code does not grant
the right to make one. Section 3, complete, verbatim:

> Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the duration of the applicable copyright) license to exercise the rights in the Work as stated below:
>
> to Reproduce the Work, to incorporate the Work into one or more Collections, and to Reproduce the Work as incorporated in the Collections;
>
> to Distribute and Publicly Perform the Work including as incorporated in Collections
>
> The above rights may be exercised in all media and formats whether now known or hereafter devised. The above rights include the right to make such modifications as are technically necessary to exercise the rights in other media and formats. Subject to Section 8(e), all rights not expressly granted by Licensor are hereby reserved, including but not limited to the rights set forth in Section 4(d).

Two limbs, reproduce and distribute, then a reservation of everything else. The measurement staged
with it: the string `to create and Reproduce Adaptations` appears once in the CC BY 3.0 legal code,
once in the CC BY-NC-SA 3.0 legal code, and **zero times here**. The only modification right granted
is technical, limited to what is necessary for a media or format shift. See
[[license-noderivatives]].

### The one thing this licence permits that the verdict does not

**Whole, unmodified, non-commercial redistribution with attribution is licensed** for the
CC BY-NC-ND materials. This wiki's `cite_only` verdict is narrower than the grant, and the narrowing
is deliberate rather than a reading of the licence.

The gap sits at fragments. The 3.0 grant runs to `the Work`; comparing the staged extracts, the
4.0 licences in this corpus grant reproduction of the Licensed Material `in whole or in part`, and
no such phrase appears in the 3.0 grant quoted above. Whether a short attributed quotation from an
ND source is inside the grant or rests on fair use is a legal judgment. **This project's own fetch
report characterises it as a fair-use call rather than a CC-granted right, and the staged deed
extract's operative reading is that you may cite and you may quote with attribution. Neither of
those settles which of the two it is.** The conservative verdict is what this wiki carries, and
the reason is recorded here so that a later reader can reopen it deliberately rather than by
accident. See [[concept-cite-quote-adapt]].

### The PD Modules are the exception, and the exception is the trap

`pd.php` is the one place on this host where derivatives are permitted, and it is therefore the one
place where taking material creates an obligation instead of just a risk. CC BY-NC-SA 3.0's
ShareAlike clause is exhaustive about what an adaptation may be licensed under, verbatim from the
legal code, whose own internal cross-reference defect is reproduced as served:

> You may Distribute or Publicly Perform an Adaptation only under: (i) the terms of this License; (ii) a later version of this License with the same License Elements as this License; (iii) a Creative Commons jurisdiction license (either this or a later license version) that contains the same License Elements as this License (e.g., Attribution-NonCommercial-ShareAlike 3.0 Unported) ("Applicable License").

Three routes, none of them compatible with a CC BY 4.0 repository. **Keep PD module text
quarantined**, and note that the deed's footnote offering a compatible-licence route is 4.0
machinery served on a 3.0 page: `compatiblelicenses` appears twice on the 3.0 deed and **zero times
in the 3.0 legal code**. See [[license-sharealike]] and
[[trap-sharealike-contaminates-by-paraphrase]].

### Citation form, and what attribution would require if anything were redistributed

No canonical attribution string is published anywhere on the site. The cite-only bibliographic form
this project uses:

```
Mathematics Assessment Project (MARS, Shell Center, University of Nottingham).
"<Resource title>." http://map.mathshell.org/<path>  · Accessed 2026-08-08.
```

If whole-file non-commercial redistribution is ever contemplated, 3.0 attribution is **not** the
same shape as 4.0. Legal code Section 4(c), opening, verbatim:

> If You Distribute, or Publicly Perform the Work or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work.

Two 3.0 features to carry: **the title of the Work is required** where 4.0 does not require it, and
there is **no indication-of-changes requirement** in 3.0's attribution clause. Section 4(a)
separately requires a copy of or URI for the licence to travel with every copy distributed. The best
available copyright line from the artifacts themselves is
`© 2015 MARS, Shell Center, University of Nottingham` plus `http://map.mathshell.org`.

## Gotchas & constraints

**1. There is no "MARS licence".** Four regimes, and the host announces the fact itself. A verdict
recorded against the host rather than against the specific resource will be wrong for at least one
of the four. Record which page you read the grant off, with its fetch date.

**2. Archive the page, not the file.** The Hopewell task PDF asserts all rights reserved with no CC
text. If the HTML page ever changes and only the PDF survives in your records, the grant is
unprovable and the artifact reads as fully reserved. See [[practice-build-a-source-table]].

**3. "All rights reserved" is not a signal on this host, in either direction.** The string sits
**inside** every ND grant as "All other rights reserved", where it means the residue after the CC
grant. It also stands alone in the Hopewell PDF, where it means what it says. A keyword grep cannot
tell them apart. See [[license-all-rights-reserved]].

**4. Silence is the fourth regime, and it is not openness.** TRU Math carries no statement and the
Hopewell rubric PDF carries none. Under this wiki's reading, an unmarked artifact resolves to all
rights reserved, not to unowned. See [[license-unmarked-silence]].

**5. The version is 3.0 Unported, and it is not 4.0.** The href carries no jurisdiction code.
3.0 Unported is a different document from 3.0 US and from 4.0, with a different attribution regime.
The deed's own banner recommending 4.0 is advice to licensors about future choices, not a withdrawal
or an expiry: material licensed under 3.0 stays under 3.0, and a 3.0 label is never silently
upgraded. See [[license-cc-by]].

**6. The 301 is a canonical redirect, not a bot block.** `https://map.mathshell.org/` returns 301 to
`https://www.map.mathshell.org/`, which returns 200, and it fires identically for plain curl and for
a browser user agent. No 403, no 406, no TLS error anywhere on the host. Recording this host as
blocked would be wrong. See [[trap-down-is-not-one-state]].

**7. The DB layer is intermittently slow, and a timeout is not an absence.** Recorded:
`stds.php?standardid=1400&collection=9` timed out at 60s; a POST to `/stds.php` timed out at 45s;
`download.php?fileid=1754` took approximately 130 s at approximately 21 KB/s and a first attempt
timed out mid-transfer. The server does **not** support byte ranges, so a failed transfer cannot be
resumed. Plain page loads immediately afterwards returned 301 in 0.49 to 0.59 s each. The
consequence for this unit: **MARS's own G-SRT-to-summative-task crosswalk was never retrieved**, so
the summative-task relevance above is a reading of fetched task content and not MARS's own standards
assignment.

**8. The site is frozen.** The footer copyright range ends 2015 and the newest PDF stamps are
© 2015. Stable to cite, and silent about whether the grants are still intended.

**9. The prototype warning is a fitness caveat, not a licence term.** MARS attaches it to the
Prototype Tests page and it says the materials need further trialing before use in a high-stakes
test. Do not fold it into the rights verdict, and do not drop it when citing a prototype item.

**10. Sampling, stated plainly.** Five Classroom Challenge pages of approximately 100, four
summative tasks of 94, four PDFs opened. "Varies per resource" rests on the four regimes and the
artifacts, not on coverage, and the next unopened PDF could disagree with its page as Hopewell does.

## Related

- [[license-noderivatives]] is the ND rider this host carries three ways, and the reason an
  exactly-on-standard task bank is cite-only.
- [[license-noncommercial]] is the NC rider on every grant here, which most readers expect to be the
  binding term and which is not.
- [[license-sharealike]] is the rider the PD Modules carry alone, at 3.0, where the compatibility
  route the deed advertises does not exist in the licence.
- [[license-all-rights-reserved]] is why the string appearing on this host proves nothing by itself.
- [[license-unmarked-silence]] is TRU Math and the rubric PDF.
- [[license-cc-by]] holds the 3.0-is-not-4.0 rule this host's version label depends on.
- [[concept-cite-quote-adapt]] is the three-operation split, and the seam where this page's verdict
  is narrower than the grant.
- [[concept-third-party-carve-out]] is the CCSS text sitting inside MAP materials under someone
  else's rights.
- [[trap-sharealike-contaminates-by-paraphrase]] is why the PD modules are quarantined.
- [[trap-down-is-not-one-state]] is the failure-mode table that records the curl-28 timeouts here as
  a slow query layer rather than as an unavailable host.
- [[source-achieve-the-core-sap]] is the other host in this batch where the artifact and the page
  disagree about rights, by a different mechanism.

## Composes with

- [[practice-cite-without-redistributing]] is the working procedure for this host: its student work,
  its rubrics and its crosswalk shape the build without any of its expression entering the repo.
- [[practice-build-a-source-table]] is where "archive the page, not the file" becomes a step, and
  where the fetch date on a page-only grant is recorded.

## References

Host pages and artifacts, fetched by this project on 2026-08-08:

- `https://map.mathshell.org/` HTTP 301 to `https://www.map.mathshell.org/` HTTP 200. The
  "Free to Schools" sidebox and the global footer.
- `https://map.mathshell.org/tasks.php?unit=HA05&collection=9` HTTP 200. The Hopewell Geometry
  summative task page carrying the CC BY-NC-ND 3.0 grant its own PDF does not.
- `https://map.mathshell.org/pd.php` HTTP 200. The single ShareAlike grant on the host.
- `https://map.mathshell.org/trumath.php` HTTP 200. Zero licence keywords.
- `https://map.mathshell.org/stds.php?standardid=1400` HTTP 200. MARS's own published G-SRT CCSSM
  crosswalk.
- `download.php?fileid=499` (93,563 bytes), `fileid=500` (144,913 bytes), `fileid=1754` (2,745,271
  bytes) and `docs/map_cc_teacher_guide.pdf` (706,151 bytes), all HTTP 200. The four artifacts.
- `https://creativecommons.org/licenses/by-nc-nd/3.0/` HTTP 200, 36916 bytes, and its `legalcode.en`
  HTTP 200, 50763 bytes. The deed and legal code behind the NoDerivatives quotations.
- `https://creativecommons.org/licenses/by-nc-sa/3.0/` HTTP 200, 37273 bytes, and its `legalcode.en`
  HTTP 200, 56255 bytes. The PD-module instrument.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-mars-map.md`, primary. Reachability and its distinct failure modes, the 14 probed
  404 paths, all four regimes verbatim, the four artifacts, the riders, and the crosswalk reading.
- `sources/cc-by-nc-nd-3-0.md`, primary. Deed and legal code verbatim, including the measured
  absence of any adaptation grant.
- `sources/cc-by-nc-sa-3-0.md`, primary. The PD-module instrument, including the measured absence of
  a compatibility route in the 3.0 legal code.
- `sources/verdict-twelve-host-table.md`, reference. Row 7, §2 verdict key, §4.10 the cite-only
  bibliographic form, and §6 the sampling limits and unretrieved crosswalk.

This project's own working files, cited as this project's measurement and not as any outside party's
statement: `Projects/HS Geometry/sources/license-mars-map.md`, the underlying fetch report, whose
§7 applies these grants to the repo and is that agent's judgment rather than host text.
