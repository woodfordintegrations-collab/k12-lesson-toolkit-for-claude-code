---
title: "Unmarked silence (no notice at all)"
type: license
sources:
  - https://eric.ed.gov/?copyright
  - https://files.eric.ed.gov/fulltext/ED584497.pdf
  - https://files.eric.ed.gov/fulltext/EJ1315132.pdf
  - https://files.eric.ed.gov/fulltext/EJ1274131.pdf
  - https://files.eric.ed.gov/fulltext/EJ1442215.pdf
  - https://map.mathshell.org/trumath.php
  - https://map.mathshell.org/download.php?fileid=500
  - https://discovery.ucl.ac.uk/id/eprint/10115606/3/Clark-Wilson_simsekali_ICME14%20paper.pdf
  - https://web.archive.org/web/20230607185622/https://discovery.ucl.ac.uk/id/eprint/10115606/
  - https://achievethecore.org/page/976/quadratic-equations-mini-assessment
  - https://www.mathsciteacher.com/home/open-access-policy
  - sources/host-eric.md
  - sources/host-mars-map.md
  - sources/host-achieve-the-core.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# Unmarked silence (no notice at all)

## Summary

An artifact carrying no rights notice anywhere is not unowned. Under the Berne default it
resolves to all rights reserved, which is the same destination as
[[license-all-rights-reserved]] reached without anybody saying so. Silence is the weakest
possible evidence of openness and it is routinely read as the strongest.

**It was the modal case on the host most likely to be reached for.** Of the 7 ERIC-hosted PDFs
this project actually opened, the tally is **1 CC BY, 2 explicitly restrictive, 4 completely
silent**. No file was open by default; the majority simply said nothing.

Three properties make silence harder to handle than a stated reservation:

- **It names no rights-holder.** A reservation at least tells you whom to ask. Silence leaves you
  with a byline and no licensor.
- **It renders identically to a grant you failed to find.** A silent file and a file whose grant
  lives one level up look the same in your extraction. That failure is owned by
  [[trap-license-lives-off-the-obvious-page]]; the doctrine of what silence resolves to is owned
  here.
- **It is not proof of restriction either.** This project's own recorded limit: "silent" means
  silent-in-the-copy-you-opened, not proven-restrictive. A notice rendered as an image, or
  published on the journal's site rather than in the file, would have been missed.

So the honest verdict for a silent artifact is `cite_only`, held provisionally, with a named
closing step. It is not `do_not_use`, and it is never an open grant.

## When to reach for it

Reach for this page when an extraction returns no match. Zero hits for `licen`, `Creative
Commons`, `copyright`, `©` and `rights reserved` is a result, and it needs to be recorded as a
result with the character count that proves the extraction worked. An empty grep over a failed
extraction is not the same finding at all.

Reach for it when a host offers an artifact freely and you are about to infer that free access
implies free reuse. That inference is the single most dangerous one available on ERIC by this
project's own reckoning, and it is worked in full at [[trap-access-is-not-a-rights-fact]].

Reach for it when a blanket grant on a host has been withdrawn, because every unmarked artifact
underneath it silently changes state. See [[license-withdrawn-grants]].

Do **not** reach for this page when the notice exists somewhere you did not look. Check the
serving page, the host's terms, and any off-host central terms first; see
[[trap-license-lives-off-the-obvious-page]]. Do not reach for it for a stated public-domain
dedication, which is the opposite instrument; see [[license-public-domain-dedication]].

## How it works

Copyright attaches on fixation without registration, marking, or notice, so the absence of a
notice carries no legal weight. The default is that the rights-holder keeps everything. A reuser
who wants more than citation needs an affirmative grant, and nothing in an unmarked artifact
supplies one.

The host most exposed to this in the corpus says so about itself. `https://eric.ed.gov/?copyright`,
HTTP 200, 9190 bytes, fetched 2026-08-08, under the heading "Copyright Policy", verbatim:

> The ERIC website contains full-text resources protected by U.S. and foreign copyright
> laws. The authors or publishers retain copyright to these works, which are used by ERIC
> with permission. All persons reproducing, redistributing, or making commercial use of
> this information are responsible for compliance with the terms and conditions asserted
> by the copyright holder. Transmission or reproduction of protected items beyond that
> allowed by fair use as defined in the copyright laws requires the written permission of
> the copyright owners. ERIC does not retain copyright to the works indexed in the
> database and cannot grant permission to use indexed works under copyright protection.

The last sentence is the operative one. ERIC hosts under permission it cannot pass on, which
means the grant is per-paper and lives inside the file. This project confirmed there is nowhere
else to look on that host: a full API field dump of one record returns exactly author,
description, id, issn, language, peerreviewed, publicationdateyear, publicationtype, publisher,
subject, title, with **no licence or rights field**, and 5 record pages were fetched in which the
only occurrence of "copyright" is the global footer nav link.

So on this host silence is not an oversight in the presentation layer. There is no presentation
layer for rights at all.

## In practice

### The four silent PDFs, with the extraction verified in each case

All fetched from `https://files.eric.ed.gov/fulltext/<ID>.pdf` with a browser user agent on
2026-08-08, all HTTP 200. The character counts matter: they are how this project distinguished
"no notice present" from "extraction failed".

| Record | What it is | Text extracted | Notice found |
|---|---|---|---|
| ED584497 | Seago 2013, PME-NA, geometric similarity | 28,370 chars, head and tail readable | none |
| EJ1315132 | Spangenberg 2021, trigonometry PCK | 104,632 chars | none |
| EJ1274131 | 2020, students' difficulties in similar triangle questions | 40,596 chars | none |
| EJ1442215 | 2024, variation theory in solving right triangles | 59,481 chars | none |

Every one of the four sits directly on this build's standards. This project's recorded line
about them is one sentence: silent is not open.

### The paper the build most wanted, and it grants nothing

"A teacher's use of dynamic digital technology to address students' misconception about additive
strategies for geometric similarity", Simsek, Hoyles and Clark-Wilson, ICME-14. It is dead centre
on the additive-versus-multiplicative similarity misconception, which this project's own sweep
calls the pedagogically central one for HSG-SRT.B.4 and B.5.

Live PDF, HTTP 200, 476,009 bytes, 4 pages, verified 2026-08-08:
`https://discovery.ucl.ac.uk/id/eprint/10115606/3/Clark-Wilson_simsekali_ICME14%20paper.pdf`

**13,348 chars extracted. "Creative Commons", "licen" and "Copyright" all NOT FOUND.** No notice
of any kind.

The repository record page is HTTP 403 live with the body "Enable JavaScript and cookies to
continue", retried with two browser user agents and still 403, which this project classifies as a
JS or cookie challenge rather than a dead page. Recovered via Wayback snapshot 20230607185622,
HTTP 200, which states verbatim:

> Additional information: This version is the author accepted manuscript. For information
> on re-use, please refer to the publisher's terms and conditions.
> Open access status: An open access version is available from UCL Discovery

"Free to read" and "re-use deferred to the publisher" in one record. The verdict recorded is
`cite_only`, and this page's job is to keep that from softening on the way into a bibliography.
See [[evidence-misconception-research-licensing]].

### Silence inside a host that grants elsewhere on the same site

MARS publishes four different regimes and says so, verbatim: `"Precise terms vary between materials."`
One of the four is no statement at all. `https://map.mathshell.org/trumath.php`, the TRU Math
Suite, HTTP 200, fetched 2026-08-08: the full page body was extracted and searched, returning
**zero hits for creativecommons, license, reproduce, or rights reserved**. Only the global
footer applies, and the global footer is a copyright assertion rather than a grant.

The same host produces silence one level further down. `hopewell_geometry_rubric.pdf`,
`https://map.mathshell.org/download.php?fileid=500`, HTTP 200, 144,913 bytes, fetched 2026-08-08,
text extracted cleanly at 36 lines with content verified readable: **zero hits for copyright,
license, creative commons, or rights reserved.** Its sibling task PDF carries a bare reservation
and the page serving both grants CC BY-NC-ND 3.0. Three artifacts in one download bundle, three
different notice states. See [[source-mars-map]].

### Silence after a blanket grant is withdrawn

`https://achievethecore.org/page/976/quadratic-equations-mini-assessment`, HTTP 200, 107,723
bytes, fetched 2026-08-08. On-page author is Student Achievement Partners, and the page HTML
carries no licence text. Its attached PDF, HTTP 200, 238,228 bytes, shows no copyright, licence,
Creative Commons, or rights-reserved statement anywhere in the document text. A first-party
resource from the rights-holder itself, shipped unmarked.

While that host published a blanket public-domain dedication, an unmarked file read as dedicated.
The dedication was withdrawn between 2026-04-25 and 2026-08-08, and what replaced it is a per-item
claim, verbatim: `"Material may be used as indicated on Our Site for the particular material."`
The artifact did not change. Its state did. This project's recorded reading is that absence of a
mark is not an affirmative grant now that the blanket backstop is gone. See
[[license-withdrawn-grants]] and [[license-public-domain-dedication]].

### The closing step, worked

Silence is provisional, and the way to close it is to leave the host and go to the publisher.
This project did it once and it worked. The Hokor 2020 PDF on ERIC names
`"the Creative Commons Attribution License"` with no version number and no creativecommons.org
URL: unversioned rather than silent, but unusable as written either way. The companion paper by
the same author was pinned at the journal instead, at
`https://www.mathsciteacher.com/home/open-access-policy`, HTTP 200, which links
`https://creativecommons.org/licenses/by/4.0/` and states verbatim:

> Articles are published under the terms of the Creative Commons Attribution License
> (https://creativecommons.org/licenses/by/4.0/). Everyone can download and read the
> article, as well as share and adapt the articles, even for commercial purposes, without
> requesting consent of the author or the publisher beforehand, if appropriate credit is
> given to the original publication.

That is the closing move: identify the publisher from the file, fetch the publisher's own policy
page, pin the version there. It is the only route this project found that turns a silent or
unversioned research PDF into a usable grant. See [[license-cc-by]].

## Gotchas & constraints

**1. "Silent" is a statement about the copy you opened, not about the work.** This project's own
recorded caveat: verified only that no licence text appears in the extracted text layer, and a
notice rendered as an image, or living on the journal's site rather than in the PDF, would have
been missed. Several of those journals may well be CC BY at source. What would close it: check
each journal's own policy page, as worked above. Until then the verdict is `cite_only` and the
reason is recorded as unresolved rather than as a finding.

**2. An empty grep over a failed extraction is not evidence of anything.** Every silent finding in
this corpus is paired with a character count and a readability check, because a scanned PDF, a
compressed body, or a truncated download all produce zero matches too. The compressed-body case
actually happened here and nearly shipped as a finding; see
[[trap-compressed-body-grepped-as-text]].

**3. The absence of a licence field is not the absence of a licence.** ERIC has no rights field
in its metadata and no notice on its record pages. That is a property of ERIC's schema, not of
the papers. Do not record "no licence" when what you measured is "no licence surfaced by this
host". The two are different findings and only the second one is yours.

**4. Silence and a hidden grant are indistinguishable at the artifact.** The mirror-image case,
where the grant is real but lives on the central terms page of another domain, is worked at
[[trap-license-lives-off-the-obvious-page]]. Rule out that case before recording silence: this
project once concluded a host was unlicensed on a clean fetch of its landing page, and the host
was CC BY 4.0 all along.

**5. Sampling limit, stated plainly, and it is severe.** 7 PDFs out of millions on ERIC. The
1 CC BY, 2 restrictive, 4 silent split measures that sample and not the population. "Silence was
the modal case" is a true statement about 7 files this project opened on this build's standards,
and it is not a base rate for education research.

**6. Do not let an access fact stand in for a rights fact in the write-up.** HTTP 200, a working
download link and an institutional repository listing are statements about availability, and one
of the papers above is simultaneously open access and unlicensed for reuse. The phrase to avoid
is "full text is available on ERIC" doing the work of a rights claim. The corrected form: ERIC
hosts the full text, ERIC grants nothing, and the licence is whatever the PDF itself says, which
in 4 of 7 sampled was nothing. See [[trap-access-is-not-a-rights-fact]].

## Related

- [[license-all-rights-reserved]] is the same outcome asserted rather than defaulted, and why the presence of the string is no more informative than its absence.
- [[license-public-domain-dedication]] is the opposite instrument, and the state an unmarked file falsely appears to be in while a blanket dedication is in force.
- [[license-withdrawn-grants]] is why an unmarked artifact can change state without changing a byte.
- [[license-cc-by]] is what the closing step resolves to when it succeeds.
- [[concept-cite-quote-adapt]] is why a silent artifact still supports the entire citation layer of a build.
- [[concept-chain-of-title]] is the deeper version of the "names no rights-holder" problem.
- [[source-eric]] is the host verdict where silence was measured and where the access-versus-rights inference is named as the most dangerous one available.
- [[source-mars-map]] publishes four regimes including no statement at all, and one download bundle there carries three notice states.
- [[source-achieve-the-core-sap]] is the first-party unmarked resource and the withdrawn backstop above it.
- [[trap-license-lives-off-the-obvious-page]] owns the case this page must be ruled out against.
- [[trap-access-is-not-a-rights-fact]] owns the inference that turns availability into permission.
- [[trap-compressed-body-grepped-as-text]] owns the fetch artifact that manufactures false silence.
- [[evidence-misconception-research-licensing]] appraises what this build can do with the silent and cite-only research literature.

## Composes with

- [[practice-build-a-source-table]] is where a silent finding is recorded with its character count, its extraction check and its named closing step, rather than as a blank cell.
- [[practice-cite-without-redistributing]] is the posture that keeps every silent artifact here fully usable to the build.

## References

Host pages and artifacts:

- `https://eric.ed.gov/?copyright` HTTP 200, 9190 bytes, fetched 2026-08-08. The Copyright Policy, Content Disclaimer and Links Disclaimer.
- `https://files.eric.ed.gov/fulltext/ED584497.pdf`, `.../EJ1315132.pdf`, `.../EJ1274131.pdf` and `.../EJ1442215.pdf`, all HTTP 200, fetched 2026-08-08. The four silent PDFs with their extracted character counts.
- `https://discovery.ucl.ac.uk/id/eprint/10115606/3/Clark-Wilson_simsekali_ICME14%20paper.pdf` HTTP 200, 476,009 bytes, fetched 2026-08-08, and the record page recovered at `https://web.archive.org/web/20230607185622/https://discovery.ucl.ac.uk/id/eprint/10115606/` HTTP 200 because the live record is HTTP 403 behind a JavaScript challenge.
- `https://map.mathshell.org/trumath.php` HTTP 200 and `https://map.mathshell.org/download.php?fileid=500` HTTP 200, 144,913 bytes, both fetched 2026-08-08. TRU Math and the rubric PDF, both extracted cleanly with zero hits.
- `https://achievethecore.org/page/976/quadratic-equations-mini-assessment` HTTP 200, 107,723 bytes, and its attached PDF HTTP 200, 238,228 bytes, fetched 2026-08-08. A first-party resource with no notice anywhere.
- `https://www.mathsciteacher.com/home/open-access-policy` HTTP 200, fetched 2026-08-08. The publisher policy page that pins the version the PDF omits.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-eric.md`, primary. Section 2 the site-level policy verbatim, section 3 the metadata and record-page checks, section 4 the seven samples and the tally, section 5.2 the ICME-14 paper, section 7 the bottom line.
- `sources/host-mars-map.md`, primary. Sections 3g, 4c and 3a.
- `sources/host-achieve-the-core.md`, primary. Sample B, and section 4 the withdrawal that changed what an unmarked file means on that host.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 9 and its "THE TRAP" rider, row 11 on absence of a mark, §6 the ERIC closing step, and the sampling limits.

The underlying fetch reports, cited as this project's own measurement and not as any outside
party's statement: `Projects/HS Geometry/sources/license-eric.md` (the four silent PDFs, the
bottom line, and the limit that "silent" means silent-in-the-ERIC-copy),
`Projects/HS Geometry/sources/license-mars-map.md` (§3g, §4c), and
`Projects/HS Geometry/sources/source-verdict-table.md` (§5 and §6).
