---
title: "ERIC (eric.ed.gov / files.eric.ed.gov)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://eric.ed.gov/?copyright
  - https://files.eric.ed.gov/fulltext/EJ1184973.pdf
  - https://files.eric.ed.gov/fulltext/EJ1064122.pdf
  - https://www.mathsciteacher.com/home/open-access-policy
  - sources/host-eric.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# ERIC (eric.ed.gov / files.eric.ed.gov)

## Summary

**ERIC grants nothing, and it says so in its own words.** Verdict for the host: `cite_only`. That
is not a finding about how open or closed the research literature is. It is a finding about what
ERIC is: an index and a repository that hosts PDFs under permission it cannot pass on to you.

The reachability story here is the inverse of every other host in this batch. Nothing is blocked,
nothing is expired, nothing has moved. `eric.ed.gov`, `files.eric.ed.gov`, `?copyright`,
`?privacy`, `?selection`, `?api` and `?faq` all returned HTTP 200 to curl with a browser agent,
and the default WebFetch agent also returned content from the root and from `?copyright`. There is
no bot block and no Wayback fallback was needed. **The failure this host produces is not a fetch
failure. It is an inference failure**, and it is the most dangerous one available anywhere in this
corpus. The sentence to retire is `full text is available on ERIC`, which is a phrasing this
project has used itself and which nobody at ERIC wrote. It is an **access** fact. It means ERIC
has permission to host the file. It says nothing about whether you have permission to reuse it.
The sentence that replaces it: *ERIC hosts the full text; ERIC grants nothing, and the licence is
whatever the PDF itself says, which in 4 of 7 sampled was nothing.*

Three structural facts make that inference impossible to shortcut:

1. **There is no licence or rights field in ERIC metadata.** A full field dump of one record
   (EJ1292278) through the open, keyless API at `https://api.ies.ed.gov/eric/` returns exactly:
   author, description, id, issn, language, peerreviewed, publicationdateyear, publicationtype,
   publisher, subject, title.
2. **No record page carries a per-record rights notice.** Five record pages were fetched
   (EJ1184973, ED584497, EJ1315132, EJ1064122, EJ1249368), all HTTP 200. The only occurrence of
   "copyright" on any of them is the global footer nav link.
3. **The licence is therefore readable only from inside the PDF**, one file at a time.

Of the **7 PDFs actually opened**: **1 CC BY, 2 explicitly restrictive, 4 completely silent.**
Silence is the modal case, and under the Berne default silence means all rights reserved, not
open.

## When to reach for it

Reach for ERIC for the design rationale of this unit, not for its items. It is a research
literature index carrying pedagogy, misconception research and pedagogical content knowledge. It
is not a task bank, a worksheet source or a problem set.

Searches run and verified at HTTP 200: `title:"right triangle"` 11 · `"trigonometric ratios"` 20 ·
`title:"similar triangles"` 6 · `"geometric similarity"` 10 · `"additive strategies"` 10.

On-topic papers with ERIC-hosted full text, with the licence each one actually carries:

| Record | Paper | Standards this project maps it to | Its own notice |
|---|---|---|---|
| EJ1442215 (2024) | The Use of Variation Theory of Learning in Teaching Solving Right Triangles, MTRJ | C.6, C.7, C.8 | silent |
| EJ1315132 (2021) | Spangenberg, Manifesting of PCK on Trigonometry in Teachers' Practice | C.6, C.8 | silent |
| EJ1274131 (2020) | Students' Difficulties in Similar Triangle Questions, Cypriot J. Educational Sciences | B.4, B.5 | silent |
| ED584497 (2013) | Seago, Supporting Teachers' and Students' Knowledge of Geometric Similarity, PME-NA | B.4, B.5 | silent |
| EJ1184973 (2018) | Arican et al., Preservice Teachers' Strategies for Solving Geometric Similarity Problems | B.5 | redistribution expressly forbidden |
| EJ1064122 (2015) | Andraphanova, Geometrical Similarity Transformations in GeoGebra | B.4 | all rights reserved, with a hyperlink carve-out |

Reach for this page in particular before assuming a paper is on ERIC because it ought to be.
**The two papers this build actually wants are not on ERIC at all**, and both are reachable
off-host. See "What you may do with it" for their separate verdicts.

Do not reach for ERIC as a licence source. There is nothing to read there. Reach for the PDF.

## What its own page says

Every quotation below was extracted by curl plus local HTML-to-text tag-stripping, not by a
summarizing layer, and is staged verbatim in `sources/host-eric.md`. That method note is not
decoration on this host: the licence claim rests entirely on what the bytes say. See
[[trap-summary-layer-is-not-evidence]].

### The Copyright Policy

`https://eric.ed.gov/?copyright`, HTTP 200, 9190 bytes, fetched 2026-08-08. Under the heading
"Copyright Policy":

> The ERIC website contains full-text resources protected by U.S. and foreign copyright laws. The
> authors or publishers retain copyright to these works, which are used by ERIC with permission.
> All persons reproducing, redistributing, or making commercial use of this information are
> responsible for compliance with the terms and conditions asserted by the copyright holder.
> Transmission or reproduction of protected items beyond that allowed by fair use as defined in
> the copyright laws requires the written permission of the copyright owners. ERIC does not retain
> copyright to the works indexed in the database and cannot grant permission to use indexed works
> under copyright protection.

The second paragraph, which is where the public-domain assumption fails:

> Certain works, including documents, reports, and other materials authored by the U.S.
> government, reside in the public domain and may be freely distributed and copied. Works authored
> by a private contractor on behalf of the U.S. government are not necessarily in the public
> domain. Contract terms and conditions vary from one agency to another. If the copyright status
> of a particular work is uncertain, it should be verified with the sponsoring agency.

Under "Links Disclaimer":

> The ERIC website includes links or pointers to other sites. Once another site is accessed
> through a link on the ERIC website, the copyright and licensing restrictions of the new site
> apply. ERIC cannot authorize the use of copyrighted materials contained in linked websites.
> [...] Note that external sites may not abide by the same privacy provisions as those described
> in the ERIC Privacy Policy.

The bracketed `[...]` is this project's own elision marker inside that quotation.

### The three shapes a hosted PDF takes, each read from inside the file

All fetched from `https://files.eric.ed.gov/fulltext/<ID>.pdf` with a browser agent, 2026-08-08.

**Restrictive, and the journal owns the copyright.** EJ1184973, HTTP 200, IJRES 2018:

> This article may be used for research, teaching, and private study purposes. Any substantial or
> systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or
> distribution in any form to anyone is expressly forbidden. Authors alone are responsible for the
> contents of their articles. The journal owns the copyright of the articles.

**All rights reserved, with an express carve-out for linking.** EJ1064122, HTTP 200, European
Journal of Contemporary Education 2015:

> Copyright © 2015 by Academic Publishing House Researcher All rights reserved. [...] WARNING!
> Article copyright. Copying, reproduction, distribution, republication (in whole or in part), or
> otherwise commercial use of the violation of the author(s) rights will be pursued on the basis
> of Russian and international legislation. Using the hyperlinks to the article is not considered
> a violation of copyright.

That last sentence is the clearest textual support in this whole corpus for a cite-and-link model.
A rights-holder asserting all rights reserved, in capitals, with an enforcement threat, still says
linking is not infringement. See [[practice-cite-without-redistributing]].

**CC BY, with no version and no deed URL.** EJ1249368, HTTP 200, Pedagogical Research 2020:

> Copyright © 2020 by Author/s and Licensed by Modestum Ltd., UK. This is an open access article
> distributed under the Creative Commons Attribution License which permits unrestricted use,
> distribution, and reproduction in any medium, provided the original work is properly cited.

"Creative Commons Attribution License" with no version number and no `creativecommons.org` URL is
not yet a pinned licence. CC BY 1.0, 2.0, 2.5, 3.0 and 4.0 are different instruments. The version
has to be pinned at the publisher, which is exactly what the next section does for the one paper
this build can actually reuse.

**Silent.** Four of the seven carried no licence, copyright or rights statement anywhere. The
extraction was verified good in each case rather than assumed, which matters because a failed
extraction and a genuine silence look identical: ED584497 at 28,370 chars with readable head and
tail, EJ1315132 at 104,632 chars, EJ1274131 at 40,596 chars, EJ1442215 at 59,481 chars. See
[[license-unmarked-silence]].

### The version pin for the one reusable paper, which lives at the journal

`https://www.mathsciteacher.com/home/open-access-policy`, HTTP 200, fetched 2026-08-08:

> Articles are published under the terms of the Creative Commons Attribution License
> (https://creativecommons.org/licenses/by/4.0/). Everyone can download and read the article, as
> well as share and adapt the articles, even for commercial purposes, without requesting consent
> of the author or the publisher beforehand, if appropriate credit is given to the original
> publication.

And `https://www.mathsciteacher.com/home/copyright--and-licensing`, HTTP 200:

> Articles are published under the Creative Commons Attribution License. Authors do not have to
> transfer copyright to the journal or publisher and retain ownership of their articles. [...]
> Authors are not allowed to use copyrighted material in their articles unless explicit permission
> from the copyright holder is received to reproduce the material under Creative Commons
> Attribution License. [...] As a result, everyone is free to use, copy, distribute, transmit, and
> adapt the work, if the article's original authors and citation information are acknowledged.

The bracketed `[...]` markers are this project's own elisions. Only the first of these two pages
carries the `by/4.0/` URL, and that URL is the whole of the version evidence.

## What you may do with it

**The verdict is per-resource, and the host-level verdict is only about the host.**

| Operation, on ERIC as a host | Permitted | Condition |
|---|---|---|
| Cite: name a paper, link its record, state what it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce a paper's exact expression in quotation marks | not from ERIC | ERIC cannot grant it. Read the individual PDF |
| Paraphrase and republish | not from ERIC | same |

Bibliographic form for an ERIC-indexed paper, as this project assembled it:

```
<Author> (<year>). <Title>. <Journal>. ERIC: <ID>. https://eric.ed.gov/?id=<ID>
Accessed 2026-08-08.
```

No licence line belongs in that block, because there is no host licence to name.

### The two papers this build wants, both off ERIC, with opposite verdicts

Exhaustive ERIC searches, all HTTP 200, all 2026-08-08, returned neither.
`author:"Hokor"` returned **2 records only**, both "Hokor, Evans Kofi", both on probability.
`author:"Hokor, Emmanuel Kwame"` returned 0. The title search returned 0.
`source:"Journal of Mathematics and Science Teacher"` returned **0**; the journal is not indexed by
ERIC at all. `author:"Clark-Wilson"` returned 13 records with no Simsek plus Hoyles plus
Clark-Wilson item.

**Arhin and Hokor 2021: CC BY 4.0, fully reusable.** Jacob Arhin and Evans Kofi Hokor, "Analysis
of High School Students' Errors in Solving Trigonometry Problems", *Journal of Mathematics and
Science Teacher* 2021, 1(1), em003, publisher Modestum, DOI 10.29333/mathsciteacher/11076. Live
PDF at HTTP 200, 626,803 bytes, verified 2026-08-08. Its in-PDF notice names the Creative Commons
Attribution License without a version; the journal's open-access policy, quoted above, pins 4.0.
Verdict for this paper: `quote_and_adapt`. Content confirmed on topic, covering trigonometric
ratios via right-angled triangles and errors in angle of elevation, depression and bearing.

```
Arhin, J., & Hokor, E. K. (2021). Analysis of high school students' errors in solving
trigonometry problems. Journal of Mathematics and Science Teacher, 1(1), em003.
https://doi.org/10.29333/mathsciteacher/11076
Licensed under CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
Accessed 2026-08-08.
```

**The author name recorded in this project as "Emmanuel Kwame Hokor" is wrong.** It is Evans Kofi
Hokor, with Jacob Arhin. ERIC returns zero records for the wrong name, which is the shape of
failure that makes a wrong name look like an absent paper.

**Simsek, Hoyles and Clark-Wilson: no grant at all, cite only.** "A teacher's use of dynamic
digital technology to address students' misconception about additive strategies for geometric
similarity", ICME-14, Shanghai. Live PDF at HTTP 200, 476,009 bytes, 4 pages, at
`https://discovery.ucl.ac.uk/id/eprint/10115606/3/Clark-Wilson_simsekali_ICME14%20paper.pdf`. The
PDF contains **no copyright notice and no licence statement of any kind**: 13,348 chars extracted,
searched for "Creative Commons", "licen" and "Copyright", all NOT FOUND. The UCL Discovery record
page states, in the Wayback snapshot 20230607185622 that recovered it:

> Additional information: This version is the author accepted manuscript. For information on
> re-use, please refer to the publisher's terms and conditions.
> Open access status: An open access version is available from UCL Discovery

Author accepted manuscript, free to read, re-use deferred to the publisher, Berne default all
rights reserved. Verdict for this paper: `cite_only`. It is dead centre on the
additive-versus-multiplicative similarity misconception, which is precisely the material this unit
needs and precisely the material it cannot reproduce.

## Gotchas & constraints

**1. Access is not rights, and this host is where that error is cheapest to make.** A fully
downloadable PDF that forbids the reuse its downloadability seems to invite is not a contradiction;
it is the normal case. EJ1184973 is downloadable and expressly forbids redistribution in any form
to anyone. See [[trap-access-is-not-a-rights-fact]].

**2. There is no metadata shortcut, and looking for one wastes a pass.** No rights field in the
API, no notice on record pages, and the API was cross-checked against the website UI (`?q=Hokor`
returned 2 results in both places) to confirm the API mirrors the site faithfully. Every reuse
decision requires opening the file.

**3. Silence is the modal case and it is not permission.** 4 of the 7 opened PDFs carry nothing.
Under Berne that resolves to all rights reserved. It also does not prove the paper is closed at
source: several of those journals may well publish CC BY on their own sites, exactly as
mathsciteacher.com does. **What is unverified is the licence of the ERIC-hosted copy's underlying
article, and closing it means visiting each journal.** Silent means silent in the ERIC copy, not
proven restrictive.

**4. A US government index does not make its contents public domain.** ERIC says so itself, in the
paragraph quoted above: works authored by a private contractor on behalf of the US government are
not necessarily in the public domain, and contract terms vary by agency. See
[[license-public-domain-dedication]] for what an actual dedication looks like and why this is not
one.

**5. The ID-to-PDF URL pattern is not guaranteed, and a 404 there means neither a block nor a
death.** `files.eric.ed.gov/fulltext/EJ1454267.pdf` and `.../EJ1370844.pdf` both returned HTTP
404. Both are live ERIC records for which ERIC simply holds no full text. Reading that 404 as a
bot block or a dead host would be the same category error this batch documents on three other
hosts. See [[trap-down-is-not-one-state]].

**6. A live 403 with a JavaScript challenge sits between you and one of the two target papers, and
the PDF path works anyway.** The UCL Discovery record page at
`https://discovery.ucl.ac.uk/id/eprint/10115606/` returns HTTP 403 with a body reading "Enable
JavaScript and cookies to continue", retried with two browser agents. The direct PDF path on the
same host returns 200. The record was recovered from Wayback. A host is not one reachability
state.

**7. A licence sentence with no version is not a pinned licence.** EJ1249368 and the Arhin and
Hokor PDF both name "the Creative Commons Attribution License" and neither carries a version
number or a deed URL. Pin the version at the publisher and record where you pinned it. Never
silently assume 4.0. See [[license-cc-by]].

**8. One dating discrepancy, recorded and not resolved.** The Simsek et al. PDF header reads
"Shanghai, 12th–19th July, 2020" while UCL catalogues the item as 2021 with event dates 11 July
2021 to 18 July 2021. ICME-14 was postponed. Cite the record's year and note the PDF header if it
matters.

**9. Sampling limit, stated plainly.** Seven PDFs opened from a database whose collection this
host describes as dating back more than a century. The 1-CC-BY, 2-restrictive, 4-silent split is
what those seven carried. It is not a population statistic and nothing on this page treats it as
one.

**10. A section-numbering defect in the underlying report was corrected during staging and is
noted here so citations line up.** The original fetch report numbers two consecutive sections
`## 3.`; the staged extract renumbers them 3 and 4 and shifts everything after by one. No content
was dropped or reordered, but a section number cited from the original report will be one lower
than the staged extract's number from that point on.

## Related

- [[license-unmarked-silence]] is where 4 of the 7 sampled PDFs land, and this host is that page's
  largest evidence base.
- [[license-all-rights-reserved]] holds EJ1064122, whose express hyperlink carve-out is the
  clearest permission to link in this corpus.
- [[license-cc-by]] is the regime the one reusable paper sits in, and holds the rule that a 3.0
  label is never silently upgraded, which generalises to an unversioned label never being
  silently pinned at 4.0.
- [[license-public-domain-dedication]] is the instrument the US-government assumption reaches for
  and does not find here.
- [[trap-access-is-not-a-rights-fact]] is the single most dangerous inference available on this
  host, and this page is its worked instance.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above was tag-stripped from raw
  bytes rather than read out of a fetch summary.
- [[trap-down-is-not-one-state]] covers the two `fulltext` 404s and the UCL 403 JS challenge, both
  of which read as "gone" and are not.
- [[concept-cite-quote-adapt]] is the split that keeps a host granting nothing fully usable.
- [[concept-chain-of-title]] is the general form of what ERIC states outright: a distributor
  holding permission to host and no power to sublicense.
- [[concept-curate-and-cite]] is the posture ERIC is entirely safe under.
- [[evidence-misconception-research-licensing]] holds the per-paper record for the misconception
  literature, including both off-host papers above and their opposite verdicts.
- [[source-math-mistakes]] is the other misconception source in this corpus, and the contrast is
  instructive: a live grant on a dead application, against a live application with no grant.

## Composes with

- [[practice-cite-without-redistributing]] is what this host supports end to end, and EJ1064122's
  carve-out is the sentence that page can quote to justify the model.
- [[practice-build-a-source-table]] is the procedure that produced the 7-PDF tally, and its
  open-the-file step is the only step that works on this host.

## References

Host pages and files, fetched by this project on 2026-08-08:

- `https://eric.ed.gov/?copyright` HTTP 200, 9190 bytes. The Copyright Policy, the
  US-government-contractor paragraph, the Content Disclaimer and the Links Disclaimer.
- `https://files.eric.ed.gov/fulltext/EJ1184973.pdf` HTTP 200. The in-PDF notice expressly
  forbidding substantial or systematic reproduction, redistribution and sub-licensing.
- `https://files.eric.ed.gov/fulltext/EJ1064122.pdf` HTTP 200. All rights reserved with an
  enforcement warning and an express carve-out for hyperlinks.
- `https://www.mathsciteacher.com/home/open-access-policy` HTTP 200. Where the CC BY version for
  Arhin and Hokor 2021 is pinned, and the only page in that chain linking `by/4.0/`.
- `https://api.ies.ed.gov/eric/` HTTP 200, open and keyless. The full field dump of EJ1292278 that
  establishes there is no rights field in ERIC metadata.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-eric.md`, primary. The reachability table, the site-level policy verbatim, the API
  field dump and record-page checks, all seven per-resource samples with their extraction sizes,
  both off-host papers with their live PDF URLs and verdicts, the corrected author name, the
  ICME-14 dating discrepancy, and the report's own carried-forward defect.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 9, §2 the
  verdict key and the statement that citing is unconstrained by every source in the table, §4.9 and
  §4.10 the attribution and bibliographic blocks.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-eric.md`, the underlying fetch report.
