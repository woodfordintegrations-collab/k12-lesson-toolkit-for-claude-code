---
title: "All rights reserved (asserted)"
type: license
sources:
  - https://www.openmiddle.com/
  - https://files.eric.ed.gov/fulltext/EJ1064122.pdf
  - https://files.eric.ed.gov/fulltext/EJ1184973.pdf
  - https://map.mathshell.org/download.php?fileid=499
  - https://map.mathshell.org/tasks.php?unit=HA05&collection=9
  - https://map.mathshell.org/
  - https://illustrativemathematics.org/
  - https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/
  - sources/host-open-middle.md
  - sources/host-learning-commons-kg.md
  - sources/host-eric.md
  - sources/host-mars-map.md
  - sources/host-im-kendall-hunt.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# All rights reserved (asserted)

## Summary

"All rights reserved" is a positively asserted reservation of copyright, and in this corpus the
string is **not a reliable signal in either direction**. It appears in four structurally
different positions, and only one of them is a rights verdict:

| Where the string sits | What it means there | Worked instance |
|---|---|---|
| A site footer with no grant anywhere on the host | the verdict: nothing is licensed | `openmiddle.com`, since early 2026 |
| Appended to a Creative Commons grant as "all **other** rights reserved" | the CC grant is live; this reserves what the grant does not give | every MARS NoDerivatives notice |
| Inside an artifact whose serving page grants CC | unresolved conflict between file and page | `hopewell_geometry.pdf` |
| Mandated **inside** a work you are permitted to publish | a notice obligation, not a prohibition on you | the CCSS public licence notice |

And a fifth position that is not a rights fact at all: embedded font metadata. That false
positive is owned by [[trap-font-notice-is-not-a-content-license]], not by this page.

Two consequences follow, and they pull in opposite directions. Finding the string does not mean
the material is closed, because it coexisted for a decade with Open Middle's own CC BY-NC-SA
inside a single footer. Not finding it does not mean the material is open, because silence
resolves to the same place; see [[license-unmarked-silence]].

**What an asserted reservation never restricts is citation.** Naming a source, linking it, and
stating what standard it addresses needs no licence, and one artifact in this corpus says so in
its own words. See [[concept-cite-quote-adapt]].

## When to reach for it

Reach for this page when a fetch returns "All rights reserved" and you are about to write
`do_not_use` or `cite_only`. Read the sentence the string sits in before the string itself. The
word `other` changes the verdict completely, and it is one word.

Reach for it when a PDF and the web page serving it disagree. That is a live, unresolved conflict
in this corpus and the mitigation is procedural rather than legal: archive the page with its
fetch date, and treat the material as `cite_only` regardless of which notice governs.

Reach for it before writing an attribution block that reproduces standards text, because the
CCSS public licence mandates an "All rights reserved" sentence inside your own published work.
See [[practice-assemble-an-attribution-block]].

Do **not** reach for this page for the absence of any notice. That is a different state with a
different evidentiary problem; it is [[license-unmarked-silence]]. Do not reach for it to decide
whether a grant used to exist; that is [[license-withdrawn-grants]].

## How it works

An assertion of reserved rights is a statement of the Berne default rather than an instrument.
It grants nothing and it takes nothing away that copyright did not already reserve. Its practical
value to a reader is evidentiary: it tells you the rights-holder considered the question and
declined to grant, which is a stronger negative signal than silence, and it usually names the
rights-holder, which silence does not.

That is the whole mechanism. Everything difficult about the string is positional.

**Position 1, the bare assertion, is the only one that is a verdict.** Site-wide footer of
`https://www.openmiddle.com/`, HTTP 200 with a browser user agent, fetched 2026-08-08:

> © 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered
> trademark of Glenrock Consulting, LLC.

This project verified the negative rather than assuming it. `grep -c creativecommons` returned 0
on the root, the category page, the embedding page and all 10 problem pages, each opened
individually, and every one carries this footer with no per-resource notice. Dedicated policy
paths all returned HTTP 404, and three independent checks (the page sitemap, the site's own
search, and Wayback CDX) confirm no policy document has ever existed. The footer is the only
licence-bearing text on that site. See [[source-open-middle]].

**Position 2, "all other rights reserved", is a rider on a live grant.** The MARS Summative
Assessment Task sidebox, `https://map.mathshell.org/tasks.php?unit=HA05&collection=9`, HTTP 200,
fetched 2026-08-08, byte-identical across the four task pages checked:

> The *Summative Assessment Tasks* may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

Reading the closing sentence alone inverts the verdict. The grant is live; what is reserved is
everything the CC BY-NC-ND 3.0 Unported grant does not convey, which is chiefly derivative works
and commercial use. This project records "All other rights reserved" as appended to every one of
that host's NoDerivatives grants. See [[license-noderivatives]].

**Position 3, the artifact and the page disagreeing.** `hopewell_geometry.pdf`, served from
`https://map.mathshell.org/download.php?fileid=499`, HTTP 200, `application/pdf`, 93,563 bytes,
fetched 2026-08-08, carries this as a running footer on both pages:

> Copyright © 2011 by Mathematics Assessment
> Resource Service. All rights reserved.

The PDF contains no CC text at all, while the web page that links it grants CC BY-NC-ND 3.0.
Anyone who receives the file alone sees a pure reservation. This project's own record puts the
question of which notice governs into the "not closeable by fetching" column, with the mitigation
stated: archive the page, not just the file. The companion rubric PDF for the same task is a
third state again, carrying no notice whatsoever. See [[source-mars-map]] and
[[license-unmarked-silence]].

**Position 4, the mandated notice.** The NGA Center and CCSSO public licence, verbatim:

> "Any publication or public display shall include the following notice: '© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved.'"

Here the string appears inside material you are licensed to publish, and shipping it is
compliance rather than an admission that you may not. States and territories that adopted the
standards in whole are exempt from that provision by the licence's own words; a curriculum repo
is not.

**Evidence status, stated because it matters:** that licence text was read from a Wayback
snapshot dated 2025-12-21. The live canonical path returns HTTP 403 with the body "Enable
JavaScript and cookies to continue" to curl with a browser user agent and to WebFetch alike,
which is a bot block on a live site rather than a death, and the old `www.corestandards.org`
path now 404s. See [[source-corestandards-nga-ccsso]].

## In practice

### The string and a CC grant lived in the same footer for a decade

Open Middle's archived footers, read from Wayback `id_` raw captures fetched with `--compressed`
on 2026-08-08, show both statements coexisting. The 2023-06-01 capture, verbatim as recorded:

> "© 2016-2023 Open Middle Partnership. All rights reserved. ... Open Middle® problems are
> licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
> License"

An agent grepping that page for "All rights reserved" and stopping there would have concluded the
site was closed while a CC BY-NC-SA 4.0 grant sat in the same sentence. The reverse error is
available today: the live footer keeps the reservation and has dropped the grant. Only the
dates distinguish them. That dating lives on [[license-withdrawn-grants]].

### An artifact that reserves everything and then carves out linking

`https://files.eric.ed.gov/fulltext/EJ1064122.pdf`, HTTP 200, fetched 2026-08-08, European
Journal of Contemporary Education 2015, verbatim with the report's own elision marker preserved:

> Copyright © 2015 by Academic Publishing House Researcher All rights reserved.
> [...] WARNING! Article copyright. Copying, reproduction, distribution, republication (in
> whole or in part), or otherwise commercial use of the violation of the author(s) rights
> will be pursued on the basis of Russian and international legislation. Using the
> hyperlinks to the article is not considered a violation of copyright.

The final sentence is the most useful line in this family. A rights-holder asserting the maximum
reservation available, with an enforcement warning attached, still states expressly that linking
is not infringement. It is direct support for the curate-and-cite posture and for nothing beyond
it. See [[practice-cite-without-redistributing]] and [[source-eric]].

The neighbouring restrictive artifact on that host phrases it differently and reaches further,
verbatim from EJ1184973:

> This article may be used for research, teaching, and private study purposes. Any
> substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing,
> systematic supply, or distribution in any form to anyone is expressly forbidden. Authors
> alone are responsible for the contents of their articles. The journal owns the copyright
> of the articles.

Both are `cite_only`. Neither is silence, and both name a rights-holder, which is exactly the
information a silent file withholds.

### One organisation reserving on one host and granting on another

`https://illustrativemathematics.org/` footer, HTTP 200, fetched 2026-08-07, verbatim:
`"All products and services are offered throughout the United States. Content on this page is licensed. © 2026, Illustrative Mathematics, all rights reserved."`
`https://k12.kendallhunt.com/` likewise reads `"© 2026 Kendall Hunt Publishing Company . All rights reserved."`
Meanwhile the same organisation's curriculum host serves the first edition of IM K-12 Math under
CC BY 4.0. Both reservations are real and both are scoped to marketing copy. Resolve the host
before the string. See [[source-im-kendall-hunt]].

## Gotchas & constraints

**1. One word inverts the verdict.** "All rights reserved" and "all other rights reserved" differ
by `other` and mean opposite things. Quote the whole sentence into your source table, never the
matched fragment. See [[practice-build-a-source-table]].

**2. A reservation is not evidence that a grant never existed.** Open Middle asserted all rights
reserved throughout the decade in which it also granted CC BY-NC-SA 4.0. The presence of the
string tells you nothing about the licence history of the host, and this project's dated register
exists because of that.

**3. The string is not reachable by a default fetcher on the host that most needs it.**
`https://www.openmiddle.com/` returns HTTP 406 to a default user agent and HTTP 200 at 100,227
bytes to a browser user agent, while its own `robots.txt` returns HTTP 200 and does not exclude
general crawlers. An automated link checker would misreport the host as broken. Distinguish the
failure mode before recording it; see [[trap-down-is-not-one-state]].

**4. Trademark survives the copyright posture and is a separate right.** `"Open Middle is the registered trademark of Glenrock Consulting, LLC."`
Nominative reference in a citation is ordinary use. Branding your own materials with the mark is
not, and that would remain true if the CC grant were restored tomorrow.

**5. A blanket reservation over contributor-authored work is not self-proving.** Every Open
Middle problem carries a named individual byline ("Source: Drew Ross", "Source: Kate Nerdypoo"),
while the site asserts blanket all rights reserved and its `/submit/` page presents no
copyright-assignment or licensing language. Whether the footer binds contributor-authored
problems is recorded in this project as not resolvable by fetching. It does not change the
verdict, which is `cite_only` either way, and this project's recorded convention is to credit
both the contributor and the host. See [[concept-chain-of-title]].

**6. Font metadata will match your grep and is not a licence.** Owned in full by
[[trap-font-notice-is-not-a-content-license]]: a SAP mini-assessment PDF carries
`© 2015 Microsoft Corporation. All Rights Reserved` as embedded Calibri metadata while the
document itself has no content notice at all.

**7. Sampling limits, stated plainly.** Open Middle is the strongest evidence here: 10 of 10
category members opened individually, uniform. MARS is weaker: 4 of 94 summative tasks and 5 of
roughly 100 Classroom Challenges. ERIC is weakest: 7 PDFs, which measures the sample and not the
population. Uniformity across a sample is evidence of a template, not proof of a per-resource
decision.

## Related

- [[license-unmarked-silence]] is the same destination reached without an assertion, and the reason the absence of this string proves nothing.
- [[license-withdrawn-grants]] dates the footer that carried both a reservation and a CC grant, and the day the grant left.
- [[license-noderivatives]] is the grant "all other rights reserved" is appended to throughout the MARS host.
- [[license-noncommercial]] and [[license-sharealike]] are the other two riders whose grants carry a reservation clause alongside them.
- [[license-cc-by]] is the regime on the host whose corporate sibling reserves everything, which is the conflation the fourth example guards against.
- [[concept-cite-quote-adapt]] is why a reservation closes quotation and paraphrase and leaves citation untouched.
- [[concept-chain-of-title]] is the contributor-byline problem underneath the Open Middle footer.
- [[source-open-middle]] is the host verdict where the bare assertion is the whole licence surface.
- [[source-mars-map]] is where the artifact and the page disagree, and where "all other rights reserved" is the normal case.
- [[source-eric]] holds the two restrictive artifacts, including the hyperlink carve-out.
- [[source-corestandards-nga-ccsso]] is the licence that requires you to publish the string yourself.
- [[source-im-kendall-hunt]] is the curriculum host whose corporate sibling reserves everything.
- [[trap-font-notice-is-not-a-content-license]] owns the embedded-font false positive.
- [[trap-down-is-not-one-state]] is why the HTTP 406 here is a bot block rather than a death.

## Composes with

- [[practice-build-a-source-table]] is where the whole-sentence rule from gotcha 1 is executed and the fetch date recorded.
- [[practice-cite-without-redistributing]] is the posture EJ1064122's hyperlink carve-out expressly permits.
- [[practice-assemble-an-attribution-block]] consumes the mandated CCSS notice, the one place this string is something you write.

## References

Rights-holder pages and artifacts:

- `https://www.openmiddle.com/` HTTP 200 with a browser user agent, HTTP 406 with the default agent, 100,227 bytes, fetched 2026-08-08. The site-wide footer, the trademark sentence, and the zero-hit `creativecommons` grep on the root, the category page, the embedding page and all 10 problem pages.
- `https://files.eric.ed.gov/fulltext/EJ1064122.pdf` and `.../EJ1184973.pdf`, both HTTP 200, fetched 2026-08-08. The reservation with its enforcement warning and hyperlink carve-out, and the second restrictive artifact.
- `https://map.mathshell.org/download.php?fileid=499` HTTP 200, `application/pdf`, 93,563 bytes, fetched 2026-08-08. The `hopewell_geometry.pdf` running footer with no CC text.
- `https://map.mathshell.org/tasks.php?unit=HA05&collection=9` HTTP 200, fetched 2026-08-08. The sidebox granting CC BY-NC-ND 3.0 and appending "All other rights reserved".
- `https://map.mathshell.org/` HTTP 301 to `www.`, then HTTP 200, fetched 2026-08-08. The global copyright assertion and its CCSS third-party carve-out.
- `https://illustrativemathematics.org/` and `https://k12.kendallhunt.com/` HTTP 200, fetched 2026-08-07. The two corporate reservations.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-open-middle.md`, primary. The live footer, the ten-page per-resource table, the three-way confirmation that no policy document exists, the archived footers, riders 1 to 3.
- `sources/host-mars-map.md`, primary. The four regimes verbatim, rider 4, and rider 6, the artifact and page mismatch.
- `sources/host-eric.md`, primary. Sections 4.1 and 4.2.
- `sources/host-im-kendall-hunt.md`, primary. Section 7, the corporate footers outside the CC grant.
- `sources/host-learning-commons-kg.md`, primary. Section 9, the CCSS Public License recovered verbatim from Wayback, its mandated notice, the adopting-state exemption, and the HTTP 403 reachability table.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: rows 7, 9 and 10, §2 on citation, §4.1 the mandated CCSS notice, §6 the artifact-versus-page question, and the sampling limits.

The underlying fetch reports, cited as this project's own measurement and not as any outside
party's statement: `Projects/HS Geometry/sources/license-open-middle.md` (§3, §4, §6),
`Projects/HS Geometry/sources/license-mars-map.md` (§3d, §4b, §5), and
`Projects/HS Geometry/sources/license-eric.md` (the per-resource samples).
