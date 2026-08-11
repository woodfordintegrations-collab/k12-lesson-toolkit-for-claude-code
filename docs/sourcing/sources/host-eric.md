---
source_url: hs-geometry-similarity-trig/sources/license-eric.md
fetched: 2026-08-08
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-eric, license-unmarked-silence, license-all-rights-reserved, trap-access-is-not-a-rights-fact, trap-summary-layer-is-not-evidence, concept-cite-quote-adapt, practice-cite-without-redistributing, evidence-misconception-research-licensing, license-cc-by, license-public-domain-dedication
---

# ERIC (eric.ed.gov, files.eric.ed.gov), and the two off-ERIC papers

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every fetch recorded below was performed by the verifying agent on
**2026-08-08 UTC**, which the report states applies to all claims unless noted. The agent's
scope was ERIC only.

Method note the report records and which matters for the evidence floor: **WebFetch summarizes
rather than pastes. All verbatim quotes below were extracted by curl plus local HTML-to-text
(regex tag strip), not by the WebFetch summarizer.**

---

## 1. Reachability

| URL | Method | HTTP | Notes |
|---|---|---|---|
| https://eric.ed.gov/ | curl -L, browser UA | **200** | text/html; charset=utf-8 |
| https://files.eric.ed.gov/ | curl -L, browser UA | **200** | text/html |
| https://eric.ed.gov/?copyright | curl -L, browser UA | **200** | 9190 bytes |
| https://eric.ed.gov/?privacy | curl -L, browser UA | **200** | 9553 bytes |
| https://eric.ed.gov/?selection | curl -L, browser UA | **200** | 8287 bytes |
| https://eric.ed.gov/?api | curl -L, browser UA | **200** | 5527 bytes |
| https://eric.ed.gov/?faq | curl -L, browser UA | **200** | 17134 bytes |

Default WebFetch, no custom UA, also returned content from the eric.ed.gov root and
`?copyright`. Report's verdict: **LIVE. No bot block observed.** No Wayback fallback needed.

## 2. Site-level licence statement, verbatim

Source: `https://eric.ed.gov/?copyright`, HTTP 200, fetched 2026-08-08.

### Under the heading "Copyright Policy"

> The ERIC website contains full-text resources protected by U.S. and foreign copyright
> laws. The authors or publishers retain copyright to these works, which are used by ERIC
> with permission. All persons reproducing, redistributing, or making commercial use of
> this information are responsible for compliance with the terms and conditions asserted
> by the copyright holder. Transmission or reproduction of protected items beyond that
> allowed by fair use as defined in the copyright laws requires the written permission of
> the copyright owners. ERIC does not retain copyright to the works indexed in the
> database and cannot grant permission to use indexed works under copyright protection.

> Certain works, including documents, reports, and other materials authored by the U.S.
> government, reside in the public domain and may be freely distributed and copied. Works
> authored by a private contractor on behalf of the U.S. government are not necessarily in
> the public domain. Contract terms and conditions vary from one agency to another. If the
> copyright status of a particular work is uncertain, it should be verified with the
> sponsoring agency.

### Under the heading "Content Disclaimer"

> The opinions and positions expressed in the content in ERIC are those of the authors and
> do not necessarily represent the opinions and positions of the Institute of Education
> Sciences or the U.S. Department of Education or an endorsement of the U. S. Government.
> ERIC is a historical repository and the collection includes materials that date back
> more than a century along with current research. The works in ERIC should be viewed
> within the context of the era in which they were written and used according to the
> specific needs of the researcher. ERIC does not flag, censure, or remove content from
> the collection for outdated language or the research contained therein.

### Under the heading "Links Disclaimer"

> The ERIC website includes links or pointers to other sites. Once another site is
> accessed through a link on the ERIC website, the copyright and licensing restrictions of
> the new site apply. ERIC cannot authorize the use of copyrighted materials contained in
> linked websites. [...] Note that external sites may not abide by the same privacy
> provisions as those described in the ERIC Privacy Policy.

The bracketed `[...]` is the report's own elision marker inside that quotation.

The report's reading, labelled as such: ERIC is a repository and index, not a licensor. It
asserts no licence of its own. Full-text PDF availability on files.eric.ed.gov means "ERIC has
permission to host it", NOT "you have permission to reuse it." The grant is per-paper and lives
with the author or publisher. The starting hypothesis ("not one license but a host of many") is
recorded as confirmed at the site level by the sentence "ERIC does not retain copyright to the
works indexed in the database and cannot grant permission to use indexed works under copyright
protection."

## 3. Metadata and record-page checks

API note: `https://api.ies.ed.gov/eric/` is open, no key, HTTP 200. A full field dump of one
record (EJ1292278) returns exactly: author, description, id, issn, language, peerreviewed,
publicationdateyear, publicationtype, publisher, subject, title.

**There is NO license or rights field in ERIC metadata.** The agent cross-checked API against
the website UI (`?q=Hokor` returned 2 results in both places) and states the API faithfully
mirrors the site.

Record-page check: 5 record pages fetched (EJ1184973, ED584497, EJ1315132, EJ1064122,
EJ1249368), all HTTP 200. The only occurrence of "copyright" on any record page is the global
footer nav link. **No record page carries a per-record rights notice.**

Consequence the report draws: the licence is readable ONLY from inside the PDF. It is not in
the metadata, not on the record page, and not inferable from "full text available on ERIC".

## 4. Per-resource licence samples, which the report calls the real finding

All PDFs fetched from `https://files.eric.ed.gov/fulltext/<ID>.pdf`, browser UA, 2026-08-08.

### 4.1 EJ1184973, HTTP 200, IJRES 2018. Restrictive; the journal owns copyright

> This article may be used for research, teaching, and private study purposes. Any
> substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing,
> systematic supply, or distribution in any form to anyone is expressly forbidden. Authors
> alone are responsible for the contents of their articles. The journal owns the copyright
> of the articles.

### 4.2 EJ1064122, HTTP 200, European Journal of Contemporary Education 2015. All rights reserved

> Copyright © 2015 by Academic Publishing House Researcher All rights reserved.
> [...] WARNING! Article copyright. Copying, reproduction, distribution, republication (in
> whole or in part), or otherwise commercial use of the violation of the author(s) rights
> will be pursued on the basis of Russian and international legislation. Using the
> hyperlinks to the article is not considered a violation of copyright.

Rider the report flags: an explicit hyperlink carve-out. Linking is expressly not infringement.
The report calls this directly supportive of a cite-and-link model and nothing more.

### 4.3 EJ1249368, HTTP 200, Pedagogical Research 2020 (Hokor). CC BY

> Copyright © 2020 by Author/s and Licensed by Modestum Ltd., UK. This is an open access
> article distributed under the Creative Commons Attribution License which permits
> unrestricted use, distribution, and reproduction in any medium, provided the original
> work is properly cited.

Rider the report flags: "Creative Commons Attribution License" with NO version number and NO
creativecommons.org URL in the PDF. The version must be pinned at the journal, not from ERIC.

### 4.4 ED584497, HTTP 200, PME-NA 2013 (Seago, geometric similarity). Silent

Extraction verified good: 28,370 chars of clean text, readable head and tail. **No licence,
copyright, or rights statement anywhere in the document.** The report's line: silent is not open.

### 4.5 EJ1315132, HTTP 200, J. Pedagogical Research 2021 (Spangenberg, trigonometry PCK). Silent

Extraction verified good: 104,632 chars. **No licence or copyright keyword present.**

### 4.6 EJ1274131, HTTP 200, Cypriot J. Educational Sciences 2020 (similar triangles). Silent

40,596 chars extracted. No licence or copyright statement found.

### 4.7 EJ1442215, HTTP 200, Mathematics Teaching Research Journal 2024 (solving right triangles). Silent

59,481 chars extracted. No licence or copyright statement found.

### 4.8 EJ1454267 and EJ1370844: HTTP 404 at files.eric.ed.gov/fulltext/

Both are live ERIC records with no ERIC-hosted full text. 404 means no such PDF. The report is
explicit that this is NOT a block and NOT a dead site: the ID-to-PDF URL pattern is not
guaranteed.

**Tally of the 7 fetched PDFs, as the report states it: 1 CC BY, 2 explicitly restrictive,
4 completely silent.** The report adds that silence is the modal case, and that under the Berne
default silent means all rights reserved.

## 5. The two papers the build needs: both absent from ERIC

Exhaustive ERIC searches, all HTTP 200, all 2026-08-08:

- `author:"Hokor"` returned **2 records only**, both "Hokor, Evans Kofi", both on PROBABILITY
  (EJ1249368 2020, EJ1334619 2022). Confirmed identical on the website UI.
- `author:"Hokor, Emmanuel Kwame"` returned 0. The report notes the hint's given name is wrong;
  it is Evans Kofi.
- `"Analysis of High School Students Errors in Solving Trigonometry Problems"` returned 0.
- `source:"Journal of Mathematics and Science Teacher"` returned **0**; the journal is not
  indexed by ERIC.
- `author:"Clark-Wilson"` returned 13 records, with no Simsek plus Hoyles plus Clark-Wilson 2020 item.
- `title:"dynamic digital technology"` returned 0. `"Cornerstone Maths"` returned 2, neither of
  which is it.

Report's conclusion: neither target paper is on ERIC or files.eric.ed.gov. Both exist elsewhere.

### 5.1 Arhin and Hokor 2021: confirmed, off-ERIC, CC BY 4.0

Jacob Arhin (Kumasi Anglican SHS, Ghana) and Evans Kofi Hokor (St. Teresa's College of
Education, Hohoe, Ghana), "Analysis of High School Students' Errors in Solving Trigonometry
Problems", *Journal of Mathematics and Science Teacher* 2021, 1(1), em003, e-ISSN 2752-6054,
publisher Modestum. DOI 10.29333/mathsciteacher/11076.

Live PDF, HTTP 200, 626,803 bytes, verified 2026-08-08:
`https://www.mathsciteacher.com/download/analysis-of-high-school-students-errors-in-solving-trigonometry-problems-11076.pdf`

In-PDF statement, verbatim:

> Copyright © 2021 by Author/s and Licensed by Modestum. This is an open access article
> distributed under the Creative Commons Attribution License which permits unrestricted
> use, distribution, and reproduction in any medium, provided the original work is properly
> cited.

Version pinned at `https://www.mathsciteacher.com/home/open-access-policy` (HTTP 200), which
links `https://creativecommons.org/licenses/by/4.0/`. Verbatim:

> Articles are published under the terms of the Creative Commons Attribution License
> (https://creativecommons.org/licenses/by/4.0/). Everyone can download and read the
> article, as well as share and adapt the articles, even for commercial purposes, without
> requesting consent of the author or the publisher beforehand, if appropriate credit is
> given to the original publication.

And `https://www.mathsciteacher.com/home/copyright--and-licensing` (HTTP 200), verbatim:

> Articles are published under the Creative Commons Attribution License. Authors do not
> have to transfer copyright to the journal or publisher and retain ownership of their
> articles. [...] Authors are not allowed to use copyrighted material in their articles
> unless explicit permission from the copyright holder is received to reproduce the
> material under Creative Commons Attribution License. [...] As a result, everyone is free
> to use, copy, distribute, transmit, and adapt the work, if the article's original authors
> and citation information are acknowledged.

The bracketed `[...]` markers are the report's own elisions.

Report's verdict: **CC BY 4.0.** No NC, no ND, no SA. Quotable, adaptable, redistributable with
attribution. Content confirmed on topic: trigonometric ratios via right-angled triangles, and
"angle of elevation, depression and bearing" errors.

### 5.2 Simsek, Hoyles and Clark-Wilson: confirmed, off-ERIC, no licence grant

"A teacher's use of dynamic digital technology to address students' misconception about
additive strategies for geometric similarity", ICME-14, Shanghai.

Live PDF, HTTP 200, 476,009 bytes, 4 pages, verified 2026-08-08:
`https://discovery.ucl.ac.uk/id/eprint/10115606/3/Clark-Wilson_simsekali_ICME14%20paper.pdf`

**The PDF contains NO copyright notice and NO licence statement of any kind.** 13,348 chars
extracted; searched "Creative Commons", "licen", "Copyright", all NOT FOUND.

The UCL Discovery record page `https://discovery.ucl.ac.uk/id/eprint/10115606/` is **HTTP 403
live**, body reading "Enable JavaScript and cookies to continue". The report classifies this as
a JS or cookie bot challenge, NOT a dead page, and records that it was retried with two browser
UAs and still returned 403. Recovered via Wayback snapshot 20230607185622 (HTTP 200), which
states verbatim:

> Additional information: This version is the author accepted manuscript. For information
> on re-use, please refer to the publisher's terms and conditions.
> Open access status: An open access version is available from UCL Discovery

Date discrepancy the report flags: the PDF header reads "Shanghai, 12th–19th July, 2020" but
UCL catalogues it as **(2021)** with event dates "11 July 2021 - 18 July 2021". ICME-14 was
postponed by COVID. The hint's "2020" traces to the PDF header; the record says 2021.

Report's verdict, in its own words: **no licence granted. Author accepted manuscript, free to
read, re-use deferred to the publisher (ICME-14 / East China Normal University). Berne default
= all rights reserved. CITE ONLY. Do not paraphrase-and-republish, do not quote beyond fair use.**

## 6. Relevance to HSG-SRT.B.4, B.5, C.6, C.7, C.8

The report's framing: ERIC is a research-literature index carrying pedagogy and misconception
research, NOT classroom tasks, worksheets, or problem sets. Useful for the unit's design
rationale, not its items.

Verified searches, HTTP 200: `title:"right triangle"` 11 · `"trigonometric ratios"` 20 ·
`title:"similar triangles"` 6 · `"geometric similarity"` 10 · `"additive strategies"` 10.

Confirmed ERIC-hosted full text (HTTP 200), on topic:

- EJ1442215 (2024) The Use of Variation Theory of Learning in Teaching Solving Right Triangles,
  MTRJ, C.6/C.7/C.8, PDF silent on licence
- EJ1274131 (2020) Students' Difficulties in Similar Triangle Questions, B.4/B.5, silent
- EJ1315132 (2021) Spangenberg, Manifesting of PCK on Trigonometry in Teachers' Practice,
  C.6/C.8, silent
- ED584497 (2013) Seago, Supporting Teachers' and Students' Knowledge of Geometric Similarity,
  B.4/B.5, silent
- EJ1184973 (2018) Arican et al., Preservice Teachers' Strategies for Solving Geometric
  Similarity Problems, B.5, redistribution expressly forbidden
- EJ1064122 (2015) Andraphanova, Geometrical Similarity Transformations in GeoGebra, B.4,
  all rights reserved

Record-only, no ERIC PDF (404): EJ1454267, EJ1370844.

## 7. The report's bottom line

ERIC grants nothing. It is an index that hosts PDFs under permission it cannot pass on. "Full
text available on ERIC" is an ACCESS fact, not a RIGHTS fact, and the report names this as the
single most dangerous inference available on this host. Every reuse decision requires opening
the individual PDF and reading its own notice, and 4 of 7 sampled PDFs have no notice at all,
which under Berne means all rights reserved, not open.

For the curate-and-cite model the report calls ERIC entirely safe: citing and linking is
unrestricted, and the European Journal of Contemporary Education says so explicitly. Quoting or
paraphrase-and-republish is per-resource.

## 8. Defect in the underlying report, carried forward

The report numbers two consecutive sections `## 3.` The first (a stub reading "in progress",
holding the API note and the record-page check) and the second ("Per-resource license samples").
This extract renumbers them 3 and 4 and shifts the following sections by one. No content was
dropped or reordered. Section numbers cited from the original report will therefore be one
lower than the numbers used here from that point on.
