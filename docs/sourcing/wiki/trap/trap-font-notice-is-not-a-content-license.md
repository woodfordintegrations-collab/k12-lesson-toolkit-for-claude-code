---
title: "An embedded font notice is not a content licence"
type: trap
sources:
  - https://achievethecore.org/page/976/quadratic-equations-mini-assessment
  - https://achievethecore.org/content/upload/A-REI.B.4%20%26%20A-CED.A.1%20Quadratic%20Equations.pdf
  - https://achievethecore.org/page/1100/functions-mini-assessment
  - https://map.mathshell.org/download.php?fileid=500
  - https://map.mathshell.org/download.php?fileid=499
  - sources/host-achieve-the-core.md
  - sources/host-mars-map.md
  - sources/host-open-middle.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# An embedded font notice is not a content licence

## Summary

A keyword grep is a sensor that reports string presence. It does not report which layer of the
file the string sits in, who wrote it, or whether it is a grant, a reservation, or a residual
clause. Every rights determination in this corpus that was made from a grep count alone was
wrong in one of those three ways.

The worked instance: Achieve the Core's quadratic-equations mini-assessment PDF is 238,228 bytes
and its text carries no rights statement of any kind, yet the file greps non-empty for
"All Rights Reserved". The hits are Microsoft Calibri font metadata. The staged extract records
the fetching agent's own warning verbatim:

> (The only "All Rights Reserved" strings are EMBEDDED FONT notices - Microsoft Calibri - NOT a
>  content licence. Do not mistake font metadata for a grant.)

This project's own adjudication states it as a general rule, and names the fuller string:

> **Font notices are not content licenses.** Their PDFs contain `© 2015 Microsoft Corporation. All
> Rights Reserved` as embedded Calibri metadata; a keyword grep will hit it and badly misread it.

The error runs in both directions. A font notice read as a reservation loses a document you could
have used. A stylesheet's licence comment read as a grant licenses content nobody granted. Both
happened on the same host.

## When to reach for it

Reach for this page at the moment you are about to write a verdict off a grep count, and
specifically when the count is small. A grep returning many hits on "creativecommons" with a deed
href attached is usually reading a real notice. One or two hits is the shape that fails here.

Reach for it before any PDF-borne verdict. PDFs carry embedded font descriptors, metadata and
producer strings that no HTML page does, and each can carry a copyright sentence about something
other than the document.

Reach for it when the only hit is a word rather than a licence URL. This corpus's reliable notices
all carry a link to a deed: `creativecommons.org/licenses/by/4.0/`, `by-nc/4.0/`, `by-nc-sa/4.0/`,
`by-nc-nd/3.0/`. A rights string with no instrument behind it is the class this page covers.

Do not reach for this page when the grep returns zero. Zero has two separate causes: the notice may
genuinely be absent, which is [[license-unmarked-silence]], or the bytes may not have been text,
which is [[trap-compressed-body-grepped-as-text]].

## How it works

A document is not one layer. Four distinct layers in this corpus can hold a string that looks like
a rights statement, and only one of them is a rights statement about the document: the content
text, written by its publisher. The other three are embedded font metadata, which describes a
typeface licensed to the author by its foundry; a third-party library comment, which describes a
code dependency; and a residual clause inside a grant, whose presence proves a grant exists rather
than denying one.

That last one inverts. MARS's Classroom Challenge sidebox reads, verbatim:

> The *Classroom Challenges* materials may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

A grep for "rights reserved" hits that sentence. Read as a reservation it says the host grants
nothing. Read correctly it says the host grants CC BY-NC-ND 3.0 and reserves the remainder. The
staged extract records the pattern as universal here: "all other rights reserved" is appended to
every NoDerivatives grant MARS publishes.

Elsewhere the same string is real and load-bearing. openmiddle.com's site-wide footer reads,
verbatim:

> © 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered
> trademark of Glenrock Consulting, LLC.

That is a genuine first-party reservation and the whole of that host's licence position. Three
occurrences of one phrase, three meanings, one grep.

## In practice

Every grep hit gets three questions before it becomes a finding. A hit answers all three or it is
not evidence.

1. **What layer is it in?** Content text, embedded resource metadata, or a third-party library
   comment. For PDFs the extracted text layer and the raw bytes are different populations. The ATC
   record is precise: `pdftotext` of the quadratic-equations PDF shows no copyright, licence, CC or
   rights-reserved statement anywhere in the document text, while the file still contains the
   Calibri strings. What the record does **not** say is which tool surfaced those strings, so do
   not carry a claim that a text extractor always excludes them.
2. **Who is the named party, and do they publish this document?** Microsoft did not publish an
   Achieve the Core mini-assessment; the normalize.css authors did not write ATC's page content. A
   named party who is not the publisher means you have found somebody else's notice about somebody
   else's asset.
3. **Is it a grant, a reservation, or a residual clause?** "All other rights reserved" is the third
   and it means a grant precedes it. Read the sentence, not the phrase.

The verdicts the three questions produce on the corpus's own samples:

| Artifact | Grep hit | Layer | Verdict |
|---|---|---|---|
| ATC quadratic-equations PDF, 238,228 bytes | `© 2015 Microsoft Corporation. All Rights Reserved` | Calibri font metadata | no content notice at all; routes to [[license-unmarked-silence]] |
| ATC functions mini-assessment page, 107,956 bytes | "MIT License" | normalize.css comment | no content notice; the MIT grant covers a CSS library |
| MARS `hopewell_geometry.pdf`, 93,563 bytes | `Copyright © 2011 by Mathematics Assessment Resource Service. All rights reserved.` | first-party running footer | genuine reservation in the artifact |
| MARS `hopewell_geometry_rubric.pdf`, 144,913 bytes | zero hits, all four terms | none | silent; silence is not a grant |
| MARS Classroom Challenge sidebox | "All other rights reserved" | residual clause in a grant | CC BY-NC-ND 3.0 granted, remainder reserved |

Note what rows 3 and 4 do together. Two files from the same task package on the same host: one
asserts all rights reserved, the other says nothing. Neither is the licence the host actually
publishes for them, which lives on the HTML page that serves both. See
[[trap-license-lives-off-the-obvious-page]].

## Gotchas & constraints

**1. The false positive is the more dangerous direction.** Reading a font notice as a reservation
costs you a source. Reading normalize.css's MIT comment as a grant over page content puts
unlicensed material into a deliverable under a permissive label. Only one of those errors is
recoverable after publication.

**2. Character-marker tests are the same failure in miniature, and this corpus has one that is
broken.** Student Achievement Partners' public-domain dedication scopes itself, verbatim as
recorded, to content "unless it is marked with the ©". This project's adjudication measured the
test against a real artifact and recorded it failing: the Equations of Lines PDF on
achievethecore.org contains zero `©` characters and is nonetheless explicitly CC BY-NC-SA. The
adjudication's conclusion, recorded as this project's own: the mark is not a reliable test and
every artifact must be opened. See [[license-public-domain-dedication]].

**3. Absence of a mark is not an affirmative grant.** The same adjudication records that 2 of the
3 ATC resources opened carry no marking at all, and that where a marking is present on a maths
resource it is CC BY-NC-SA rather than the dedication people remember. With the blanket backstop
withdrawn, an unmarked ATC item has no grant behind it. See [[trap-license-withdrawn-after-citation]].

**4. Two records of the Calibri finding differ in scope, and neither is adjusted here.** The
host-level extract records it for one sampled PDF, Sample B. This project's adjudication
generalises to "their PDFs" without stating how many were checked; three ATC resources were opened
in total. The mechanism is established, the frequency is unmeasured.

**5. The URL of the sampled PDF is hostile to transcription.** The fetching agent recorded it with
a literal space and a literal `&`: `/content/upload/A-REI.B.4 & A-CED.A.1 Quadratic Equations.pdf`.
The percent-encoded form is in this page's frontmatter. If a re-fetch 404s, try both before
recording the file as gone, and see [[trap-down-is-not-one-state]] for the rest of that discipline.

**6. This page does not tell you a document's licence,** only when a grep result is not one. An
artifact whose hits fail the three questions still needs its rights position established elsewhere:
the page that serves it, an off-host terms document, or a recorded absence.

## Related

- [[license-unmarked-silence]] is where a document lands once its only grep hits are disqualified,
  and it is the modal outcome of applying this page.
- [[license-all-rights-reserved]] holds the string itself and why it is unreliable in both
  directions, including the residual clause inside every MARS grant.
- [[license-public-domain-dedication]] holds the SAP dedication whose own `©` marker test is
  measurably broken, which is gotcha 2.
- [[concept-third-party-carve-out]] holds the two classes of embedded material that genuinely do
  sit outside a work's grant, images and marks. A font notice is a different object: not a rider on
  your reuse, but a statement about something that is not the content.
- [[trap-compressed-body-grepped-as-text]] is the inverse sensor failure, a zero count over bytes
  that were never text.
- [[trap-summary-layer-is-not-evidence]] is the third member of the set: text that was never in the
  document at all.
- [[trap-license-lives-off-the-obvious-page]] is why the MARS task PDF and the page serving it
  disagree, and which one carries the grant.
- [[source-achieve-the-core-sap]] and [[source-mars-map]] hold the two host verdicts the samples
  above came from. [[source-open-middle]] holds the genuine reservation the same grep matches.

## Composes with

- [[practice-build-a-source-table]] is the fetch-and-record procedure this page is a filter inside.
  The three questions run where that procedure turns a raw fetch into a verdict row, and a hit that
  fails them is recorded as no evidence rather than as a licence.

## References

Host artifacts, fetched by this project on 2026-08-08:

- `https://achievethecore.org/page/976/quadratic-equations-mini-assessment` HTTP 200, 107,723
  bytes, no licence text on page. Its attached PDF
  `/content/upload/A-REI.B.4 & A-CED.A.1 Quadratic Equations.pdf` HTTP 200, 238,228 bytes, the
  Calibri false positive.
- `https://achievethecore.org/page/1100/functions-mini-assessment` HTTP 200, 107,956 bytes. The
  normalize.css "MIT License" false positive.
- `https://map.mathshell.org/download.php?fileid=499` (`hopewell_geometry.pdf`) HTTP 200, 93,563
  bytes, the genuine first-party reservation; `?fileid=500`
  (`hopewell_geometry_rubric.pdf`) HTTP 200, 144,913 bytes, zero hits on all four terms.
- `https://www.openmiddle.com/` HTTP 200 with a browser user agent, the genuine site-wide
  reservation.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-achieve-the-core.md`, primary. Step 5 samples A, B and C.
- `sources/host-mars-map.md`, primary. §3c and §3d the sidebox grants, §4b and §4c the two Hopewell
  PDFs, rider 4 the residual clause.
- `sources/host-open-middle.md`, primary. §3, the live footer verbatim.
- `sources/verdict-twelve-host-table.md`, reference. Row 11 riders, where "Font notices are not
  content licenses" is stated as this project's own adjudication, and Row 12 riders, where the
  `©` marker test is measured and found broken.
