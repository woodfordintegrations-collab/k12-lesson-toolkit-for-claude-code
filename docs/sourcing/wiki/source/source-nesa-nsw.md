---
title: "curriculum.nsw.edu.au (NSW/NESA Mathematics K-10 syllabus)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/outcomes
  - https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage-5/facb3aa952
  - https://www.nsw.gov.au/education-and-training/nesa/copyright
  - sources/host-nesa-nsw.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# curriculum.nsw.edu.au (NSW/NESA Mathematics K-10 syllabus)

## Summary

This row exists for a comparison, not for content. Its finding is that the complementary-angle
relationship, which New York assesses on essentially every sitting, is named as a curricular object
in New South Wales and is absent by specification from several other national curricula this project
searched. A page that only said "NESA covers it" would not be worth writing.

Verdict: `cite_only`. NESA's material is Crown copyright, all rights reserved, with one limited
licence attached, and that licence is **closed by class of person rather than by kind of use**. It
reaches teachers employed in NSW government and registered non-government schools, and parents of
children registered for home schooling. Its own `Note:` then excludes
`private/home tutoring companies, professional learning service providers, publishers, and other
organisations`. A curriculum-resource project is not in the granted class.

**Three things this project recorded about this source turned out to be wrong or unconfirmed when
the host was actually fetched**, and naming them is most of this page's value:

1. **The URL in `INVENTORY.md` returns HTTP 404.** The live path uses `stage-5` with a hyphen and a
   different content hash.
2. **The outcome the row names, MA5-TRG-P-02, does not mention complementary angles.** Its full text
   is `establishes and applies the properties of trigonometric functions and finds solutions to
   trigonometric equations (Path: Adv)`. A grep for `complementary` over the entire 2010655-byte
   outcomes page returns **0**.
3. **The sentence this project's wide sweep quotes as NESA's, marked `VERBATIM (host)`, is not in
   the delivered bytes of the live page.** What is there is a differently worded Key ideas bullet
   inside NESA's teaching advice. See gotcha 3, which is the one to read if you read only one.

Where NESA does name the relationship, fetched and verbatim, is the title of a content group under
the Trigonometry D (Path) focus area:

> Solve trigonometric equations using exact values and the relationships between supplementary and complementary angles

and a Key ideas bullet in the teaching advice for that focus area:

> apply the relationships between the sine and cosine ratios of complementary angles in right-angled triangles

Attribute both correctly. Neither is the outcome text, and neither is one of the four syllabus
content points, which the site lazy-loads and which were not delivered.

## When to reach for it

Reach for this row when you need to say whether a standard is a real curricular object across
jurisdictions or an artefact of one standards framework. That comparative claim is what this row
carries and no other row does.

Reach for the Trigonometry D content-group title and the Key ideas bullet when you want a
non-CCSS-worded statement of the same mathematical idea, to cite as corroboration that the idea is
named independently of the US framework.

Reach for NESA's ordering when you are sequencing a lesson. This project's wide sweep records two
defensible orderings and calls NESA's the gentler ramp: exact values for 30, 45 and 60 degrees
first, then the complementary relationship, so the swap becomes visible in numbers the student has
just derived. That is a design observation, not a licence-bearing one.

Do **not** reach for this host for syllabus text to reproduce, adapt or ship. See "What you may do
with it".

Do not reach for MA5-TRG-P-02 as evidence that all NSW Stage 5 students meet this content. The `P`
in the code and the `(Path: Adv)` suffix mark it as a Path outcome. The two core Stage 5
Trigonometry outcomes are MA5-TRG-C-01 and MA5-TRG-C-02, and neither mentions complementary angles.
See gotcha 4.

Do not reach for it by grepping for `complementary`. Most hits on the Stage 5 page are probability.
See gotcha 5.

## What its own page says

Everything below came from `curl` responses written to disk and parsed from disk on 2026-08-08, and
is staged in `sources/host-nesa-nsw.md`. See [[trap-summary-layer-is-not-evidence]].

**Extraction note, load-bearing.** This site does not serve syllabus prose as HTML. It embeds a JSON
payload and renders client-side. The strings below were decoded with a real JSON string decoder, so
the apostrophes and en dashes are the source's own characters rather than artefacts.

### The URL in INVENTORY.md, and how it fails

The row cites
`https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage5/fa63d5e5b6`.
At this fetch it returns **HTTP 404**. Naming the failure mode precisely, as the retired vocabulary
requires: not a bot block (no 403, no 406), not a TLS failure, not genuinely gone. It is a
**soft-404 with a redirect**. The server redirects to `/404?path=...` and then serves a
1155830-byte fully styled site page under a genuine 404 status line. A checker asking "did bytes
come back" or "does the page render" marks this URL healthy. Only the status line reveals it.

Two details in the redirect are diagnostic. It rewrites `learning-areas` to `learning-area`,
dropping the plural, and it drops the trailing hash; on a second probe the server substituted a
different hash of its own, `fad5496b8e`. The live path is:

```
https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage-5/facb3aa952
```

`stage-5` with a hyphen, hash `facb3aa952`. Every stage path on this site takes the same form with
its own hash, and the hashes are not stable across the site's own redirects. That is a durable
warning for any citation into this host: cite the path, expect the hash to rot.

### MA5-TRG-P-02, verbatim

Source object, byte-exact from the outcomes page:

```json
"code":{"name":"📜 Code","type":"text","value":"MA5-TRG-P-02"},
"title":{"name":"📜 Title","type":"text","value":""},
"description":{...,"name":"📜 Description","type":"rich_text",
  "value":"<p>establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations <em>(Path: Adv)</em></p>"}
```

With the HTML stripped:

> establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations (Path: Adv)

`title` is an empty string, so the code is the outcome's only name. `(Path: Adv)` is italicised in
the source. The object's `lastModified` is `2022-11-24T08:20:08.826426Z`, its `syllabus` value is
`Mathematics K–10 (2022)` with an en dash as in the source, its `stages__stages` is `Stage 5` and
its `stages__stage_years` are `9` and `10`.

**This text does not name the complementary-angle relationship**, and `complementary` occurs 0 times
in the whole outcomes page.

The other three Stage 5 Trigonometry outcomes, same extraction, for contrast:

| Code | Outcome text |
|---|---|
| MA5-TRG-C-01 | applies trigonometric ratios to solve right-angled triangle problems |
| MA5-TRG-C-02 | applies trigonometry to solve problems, including bearings and angles of elevation and depression |
| MA5-TRG-P-01 | applies Pythagoras’ theorem and trigonometry to solve 3-dimensional problems and applies the sine, cosine and area rules to solve 2-dimensional problems, including bearings (Path: Stn, Adv) |
| MA5-TRG-P-02 | establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations (Path: Adv) |

The apostrophe in `Pythagoras’` is U+2019, as in the source.

### Where the relationship actually appears

On the live Stage 5 content page, `complementary` occurs 26 times and `MA5-TRG-P-02` occurs 4 times.
The focus-area to outcome mapping was read from the payload's own links rather than inferred from
letter ordering: `MS S5 Trigonometry D (Path)` links outcome codename `ma5_trg_p_02`.

Two content groups sit under Trigonometry D. The first, `title` verbatim:

> Solve trigonometric equations using exact values and the relationships between supplementary and complementary angles

Its `content_items` field lists four children,
`ma_k_10_cp_trd_sol_stg5_01` through `_04`. **Those four objects are not in the delivered bytes.**
`linkedItems` is empty and no object with any of those codenames exists in the payload. The site
lazy-loads them, so the text of NSW's four individual content points under this group is a genuine
gap here.

What is delivered is the teaching-advice object for the focus area, whose Key ideas list is present
in full. Decoded from the payload's escapes, verbatim:

> Key ideas
> Students:
>
>   prove that the tangent ratio can be expressed as a ratio of the sine and cosine ratios
>   compare the features of sine, cosine and tangent curves from their graphs for angles of any magnitude, including negative angles
>   apply the relationships for obtuse angles
>   apply the sine rule and area rule to find angles involving the ambiguous case
>   relate the gradient of a line to its angle of inclination on the Cartesian plane
>   apply the exact sine, cosine and tangent ratios for angles of 30°, 45° and 60°
>   apply the relationships between the sine and cosine ratios of complementary angles in right-angled triangles
>   find the possible acute and/or obtuse angle(s) given a trigonometric ratio

The seventh bullet is the closest located NESA statement to the idea. It is a Key ideas bullet
inside NESA's teaching advice for Trigonometry D (Path). It is not the outcome text and it is not a
content point.

For comparison, the Trigonometry A content group present in the same payload is titled:

> Demonstrate and explain the constancy of trigonometric ratios for a given angle in right-angled triangles

### NESA's copyright terms, verbatim

The syllabus site carries no terms inline. Its footer renders only `NESA © 2026 Privacy` plus a bare
`Copyright © 2026` in the site chrome, with no named holder, and holds a weblink object whose
`link_url` is `https://www.nsw.gov.au/education-and-training/nesa/copyright`. The grant lives on a
different host entirely; see [[trap-license-lives-off-the-obvious-page]].

That page, HTTP 200, 154236 bytes, titled `NESA Copyright | NSW Government`, attributed at its head
to `© NSW Education Standards Authority`. Its full body, verbatim, headings included:

> **Copyright disclaimer**
>
> The documents on the NSW Education Standards Authority (NESA) website and the NSW Curriculum website contain material prepared by NESA for and on behalf of the Crown in right of the State of New South Wales. The material is protected by Crown copyright.
>
> These websites hold the only official and up-to-date versions of the documents available on the internet. Any other copies of these documents, or parts of these documents, that may be found elsewhere on the internet might not be current and are not authorised. You cannot rely on copies from any other source.
>
> All rights are reserved. No part of the material may be:
>
> - reproduced in Australia or in any other country by any process, electronic or otherwise, in any material form
> - transmitted to any other person or stored electronically in any form without the written permission of NESA except as permitted by the Copyright Act 1968 (Cth).
>
> When you access the material, you agree:
>
> - to use the material for research or study, criticism or review, reporting news and parody or satire
> - to use the material for information purposes only
> - not to modify the material or any part of the material without the written permission of NESA
> - to reproduce a single copy for personal bona fide study use only and not to reproduce any major extract or the entire material without the permission of NESA
> - to include this copyright notice in any copy made
> - to acknowledge that NESA is the source of the material.
>
> The documents may include third-party copyright material such as photos, diagrams, quotations, cartoons and artworks. This material is protected by Australian and international copyright laws and may not be reproduced or transmitted in any format without the copyright owner’s permission. Unauthorised reproduction, transmission or commercial use of such copyright material may result in prosecution.
>
> NESA has made all reasonable attempts to locate the owners of third-party copyright material. NESA invites anyone from whom permission has not been sought to contact the Copyright Officer.
>
> **Special arrangements applying to the NSW Curriculum Reform**
>
> As part of the NSW Curriculum Reform process, NESA grants a limited non-exclusive licence to:
>
> - teachers employed in NSW government schools and registered non-government schools
> - parents of children registered for home schooling
>
> to use, modify and adapt the NSW syllabuses for **non-commercial educational use only**. The adaptation must not have the effect of bringing NESA into disrepute.
>
> **Note:** The above arrangements do not apply to private/home tutoring companies, professional learning service providers, publishers, and other organisations.
>
> For more information on the above or for **commercial use or any other purpose**, please contact the Copyright Officer for permission.
>
> Email: copyright@nesa.nsw.edu.au

The bold is the source's own emphasis, preserved because it marks the operative restrictions. The
`lastModified` on the copyright weblink object is `2025-06-12T05:04:49.8941888Z`.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name NESA, link the syllabus, state that MA5-TRG-P-02 exists and which focus area it governs, describe in your own words what its teaching advice covers | yes | none, and no licence is needed to do this |
| Quote: reproduce outcome text, a content-group title or a Key ideas bullet inside your own prose with attribution | no grant from NESA | nothing in the passage above grants reproduction to a project like this one. Any use rests on whatever the `Copyright Act 1968 (Cth)` independently permits, which this wiki does not adjudicate |
| Paraphrase and republish: rewrite NESA syllabus material and ship it | no | `not to modify the material or any part of the material without the written permission of NESA`, and the modify-and-adapt licence is closed to organisations |

### Why the limited licence does not reach this project

Read the three riders together and in order, because separated they mislead.

1. **The baseline is all rights reserved under Crown copyright**, with a statutory carve-out for
   whatever the Copyright Act independently permits. Nothing on this host is a Creative Commons
   instrument, and no CC deed URL appears anywhere in the payload. See
   [[license-all-rights-reserved]].
2. **The Curriculum Reform licence is closed by class of person, not by kind of use.** This is the
   unusual shape and the one most likely to be misread. A reader sees `non-commercial educational
   use only` and concludes that non-commercial educational use is permitted generally. It is not.
   The permission is granted **to** two named classes, and the `Note:` excludes publishers and other
   organisations by name. Being non-commercial does not put you in the class. See
   [[license-noncommercial]] for why an NC-shaped phrase is not always an NC rider.
3. **Third-party material inside NESA documents is excluded entirely**, and NESA states it has not
   located every owner. See [[concept-third-party-carve-out]].

The access-agreement list is worth reading whole rather than cherry-picked. `criticism or review`
and `reporting news` sit alongside `to reproduce a single copy for personal bona fide study use
only`. Nothing in the passage grants redistribution, and a single personal copy is not a build
input.

### The layer that needs no licence at all

The comparative finding this row exists for is a fact about curricula, not an expression owned by
anyone: that NSW names the complementary relationship as a curricular object, at Stage 5, inside a
Path focus area, while several other national curricula do not. Stating that, naming the outcome
code, linking the page and describing the teaching advice in your own words is unconstrained. See
[[concept-cite-quote-adapt]] and [[practice-cite-without-redistributing]].

## Gotchas & constraints

**1. The INVENTORY.md URL is dead and fails in the way that is hardest to notice.** HTTP 404 under a
1155830-byte fully rendered page. Reported here rather than fixed, since INVENTORY.md is not this
page's to edit. The live path is given above. The site's own hashes moved between two probes in the
same session, so a hash-bearing citation into this host should be expected to rot and should carry
the human-readable path alongside it. See [[trap-soft-404-status-proves-nothing]], which carries the
mirror image of this failure: there a 200 was returned for a page that did not exist, here a full
page body is returned under a 404. In both directions the body is not the evidence and the status
line is. See also [[trap-down-is-not-one-state]].

**2. The outcome does not say what this project's row says it says.** The INVENTORY row describes
MA5-TRG-P-02 as "naming the complementary relationship explicitly". Against the fetched bytes it
does not, and `complementary` appears 0 times on the outcomes page. The claim is true of the content
group under the outcome's focus area and of a Key ideas bullet in its teaching advice, which is a
weaker and differently located fact. **Recorded as a correction, not a fix.**

**3. Two different NESA strings are in circulation inside this project, and only one of them was
fetched.** This is the gotcha to carry away. This project's wide-sweep adjudication quotes NESA as
saying, marked `VERBATIM (host)`:

> Verify and use the relationships between the sine and cosine ratios of complementary angles: sin A = cos(90° − A) and cos A = sin(90° − A).

and

> Derive and apply the exact sine, cosine and tangent ratios for 30°, 45° and 60°

The direct fetch of the live page found neither. What it found were the Key ideas bullets
`apply the relationships between the sine and cosine ratios of complementary angles in right-angled
triangles` and `apply the exact sine, cosine and tangent ratios for angles of 30°, 45° and 60°`.
Different verbs, different qualifiers, no formulae. The likeliest reconciliation is that the sweep's
strings are the syllabus **content points**, which sit under this same content group and which the
site lazy-loads and did not deliver, so the two sets of strings would be two different NESA objects
rather than a contradiction. **That is a reconciliation, not a measurement, and it is not confirmed
here.** Under honesty floor F3 neither pair may be presented as the other. What would close it:
fetch the four content-point objects `ma_k_10_cp_trd_sol_stg5_01` through `_04` and paste their
text. Until then, quote only the Key ideas bullet, and say it is teaching advice.

**4. Path outcome, not core.** MA5-TRG-P-02 carries `P` in its code and `(Path: Adv)` in its text.
The core Stage 5 Trigonometry outcomes are MA5-TRG-C-01 and MA5-TRG-C-02, and neither mentions
complementary angles. Whether a Path outcome is elective for a given NSW student is **unresolved**:
the syllabus's own definition of a Path outcome was not fetched. So "NSW requires this of all Stage 5
students" is not supported by anything here, and the safe form of the claim is that NSW names it as
a curricular object at Stage 5 on the Advanced path.

**5. A keyword search for `complementary` on this host returns probability by a wide margin.** Of
the 26 hits on the Stage 5 page, most are `complementary events`: a Stage 4 outcome
`Determine probabilities for complementary events`, three separate Key terms lists, and background
knowledge. Two further hits are Stage 4 geometry. A grep-driven survey of this host will conclude
the trigonometric relationship is everywhere and be measuring the wrong word.

**6. The comparative half of this row's value is this project's own adjudication, not a fetch.** The
claim that the relationship is absent by specification from AQA GCSE 8300, ACARA v9 Years 9 and 10,
Ontario Grades 9 and 10, Singapore E-Math and the post-2023 NCERT comes from this project's
wide-sweep document, whose adjudicating agent states in its opening paragraph that it fetched
nothing and that every claim traces to a report. The staged NESA extract fetched nothing about any
of those jurisdictions either. **Recorded as unverified at this wiki's evidence floor.** What would
close it: fetch each syllabus document and record the measurement per jurisdiction, in the manner of
the NCERT check the sweep does describe, where an agent grepped the Reprint 2026-27 Class 10
Chapter 8 PDF and found `complementary` zero times. Cite the comparison as "this project's wide
sweep recorded", never as a property of those authorities.

**7. NESA's own assessment materials were not fetched.** Nothing here says whether or how the
relationship is examined in New South Wales. The contrast with New York, where this project's JMAP
extract carries provenance-tagged items across a decade of sittings, is therefore a contrast between
a syllabus statement and an item record, not between two item records. See [[source-jmap]].

**8. The whole rights surface is off-host, and the on-host chrome names no holder.** The syllabus
site renders `NESA © 2026 Privacy` and a bare `Copyright © 2026`. Everything operative is on
`nsw.gov.au`. An agent that fetched only `curriculum.nsw.edu.au` would record this host as carrying
an unattributed reservation and would miss both the Crown copyright framing and the limited licence.

**9. The terms carry their own date.** The copyright weblink object's `lastModified` is
`2025-06-12T05:04:49.8941888Z`, against a page that renders a 2026 copyright year. Two grants in
this corpus were withdrawn inside six months. See [[license-withdrawn-grants]].

## Related

- [[license-all-rights-reserved]] is the baseline regime this host asserts, and the page that holds
  why the string is unreliable as a signal in both directions.
- [[license-noncommercial]] is where the phrase `non-commercial educational use only` would normally
  point. It does not point there here, because the restriction that actually binds is the class of
  person, and reading it as an NC rider is the misreading this page names.
- [[concept-third-party-carve-out]] holds the class of material NESA excludes from its own documents
  and admits it has not fully traced.
- [[concept-chain-of-title]] is the general form of that admission: a publisher licensing, or
  reserving, material it did not clear.
- [[trap-license-lives-off-the-obvious-page]] is why the syllabus site's own footer is not where the
  terms are.
- [[trap-soft-404-status-proves-nothing]] and [[trap-down-is-not-one-state]] are where the dead
  INVENTORY URL is named correctly instead of being recorded as unavailable.
- [[trap-summary-layer-is-not-evidence]] is why the JSON payload above was decoded rather than
  summarised, and it is the discipline that surfaced gotcha 3.
- [[source-jmap]] is the New York half of the comparison, where the same standard is
  provenance-tagged across a decade of sittings.
- [[source-ohio-released-items]] is the other jurisdiction in this corpus that assesses it and
  publishes why students get it wrong.
- [[evidence-c7-store-gap-not-corpus-gap]] is where this row's comparative finding does its work, as
  part of what retired this project's claim that the standard is externally scarce.

## Composes with

- [[practice-cite-without-redistributing]] is the whole of the permitted use here: the comparative
  fact is free, the syllabus expression is not, and the two must not be allowed to blur in a
  deliverable.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict, and
  this host is its strongest argument for path-probing before citing, since the recorded URL was
  dead and reported healthy by every check except the status line.

## References

Fetched by this project on 2026-08-08, `curl` to disk and parsed from disk:

- `.../mathematics-k-10-2022/content/stage5/fa63d5e5b6` **HTTP 404**, redirected to
  `/404?path=...`, 1155830-byte styled body. The dead URL from INVENTORY.md.
- `.../mathematics-k-10-2022/content/stage5` **HTTP 404**, same shape, server-substituted hash
  `fad5496b8e`.
- `.../mathematics-k-10-2022/outcomes` HTTP 200, 2010655 bytes. The MA5-TRG-P-02 object, its
  taxonomy fields, the other three Stage 5 Trigonometry outcomes, and the zero-hit `complementary`
  measurement.
- `.../mathematics-k-10-2022/content/stage-5/facb3aa952` HTTP 200, 7597010 bytes. The live Stage 5
  content page: the focus-area to outcome mapping, the two Trigonometry D content groups, the four
  undelivered content-point codenames, and the Key ideas list.
- `.../mathematics-k-10-2022` HTTP 200, redirected to `.../overview`, 1531022 bytes.
- `https://www.nsw.gov.au/education-and-training/nesa/copyright` HTTP 200, 154236 bytes. The full
  copyright body reproduced above.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/host-nesa-nsw.md`, primary. The fetch log, the 404 analysis and live path, the outcome
  objects, the focus-area mapping, the content-group titles, the undelivered content points, the
  Key ideas list, the copyright body, the three riders, and §5 on what is not established.
- `sources/verdict-wide-sweep.md`, reference. This project's own adjudication of eight sweep
  reports, which fetched nothing and says so: the two NESA strings in gotcha 3, the two documented
  lesson orderings, and the jurisdiction comparison recorded in gotcha 6 as unverified at this
  wiki's floor.
