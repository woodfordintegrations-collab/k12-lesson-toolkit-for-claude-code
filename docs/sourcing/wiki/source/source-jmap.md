---
title: "jmap.org (JMAP standard-indexed Regents worksheets)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://www.jmap.org/
  - https://www.jmap.org/htmlstandard/G.SRT.C.7.htm
  - https://jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.pdf
  - https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions2.pdf
  - https://www.nysedregents.org/
  - https://www.nysed.gov/terms-of-use
  - sources/host-jmap.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# jmap.org (JMAP standard-indexed Regents worksheets)

## Summary

JMAP indexes New York State Regents examination questions by standard code and publishes them as
per-standard worksheets in PDF, DOC and TST form, free and unauthenticated. Verdict: `cite_only`,
and it is cite-only twice over, because two separate rights layers stack here and neither one
opens.

| Layer | Host that carries the instrument | What the instrument says | Effect |
|---|---|---|---|
| JMAP's arrangement, indexing and worked answer keys | `www.jmap.org`, footer table on every page checked | `Copyright © 2004-now  JMAP, Inc. - All rights reserved` | No grant. There is no licence page, no terms page and no permissions page on this host. |
| The underlying examination items | `nysed.gov/terms-of-use`, linked from `nysedregents.org` | A grant for `personal, private and educational purposes`, with a commercial bar and a prescribed attribution template | Real, but by its own final paragraph it does not reach copies held on sites NYSED does not link, and JMAP is one. |

The mistake this page exists to prevent is treating the second layer as covering the first. A
reader who finds NYSED's permissive-sounding grant and applies it to a JMAP worksheet has moved a
grant across a boundary the grant itself closes.

**The value here is licence-free anyway, and that is the point.** What JMAP is uniquely good for is
the shape of the item bank: which of the five target standards carries many worksheets and which
carries one, what the archetypes are called, and which real examination each item came from. Item
taxonomies, relative weights and provenance tags are facts about assessment, not protected
expression. This project's own wide-sweep adjudication makes the same call in its own words: the
constraint bites on the prose of about five sources and does not bite on the design work, which is
the expensive half. Read JMAP as a blueprint. Do not put its item text in a deliverable.

## When to reach for it

Reach for the per-standard index at `htmlstandard/<CODE>.htm` when you need to size the item work
before writing any of it. All five unit standards have a page. The index gives worksheet names,
which are archetype names, and a count column paired positionally with a series column, so the
relative weight of each standard becomes visible rather than guessed.

Reach for the REF tags in a worksheet's answer section when the question is whether a standard is
actually assessed rather than merely written down. Every item carries one, of the regular form
MMYYNNxxx, naming the sitting it came from.

Reach for `G.SRT.C.7.Cofunctions2.pdf` question 1 when authoring cofunction items. JMAP's own
answer note records that a real released item was defective, which is a live authoring warning and
not a licence matter: cofunction equations have solutions outside the acute branch unless the
domain is constrained.

Do **not** reach for this host for item text, for worked solutions, or for the `.doc` and `.tst`
files as importable assets. Nothing on this host grants any of that.

Do not reach for it as a route to NYSED's own grant. If you want an item under NYSED's terms, go to
`nysedregents.org` and take it from the exam PDF there, under the attribution template in "What you
may do with it" below. That is a different act with a different provenance, and it still carries
the commercial bar.

Do not reach for it to learn what the series abbreviations mean. They are undefined in the
delivered bytes. See gotcha 5.

## What its own page says

Every quotation below was taken by a fetching agent from bytes written to disk and read back from
disk on 2026-08-08, and is staged verbatim in `sources/host-jmap.md`. No summarizing layer was used
anywhere in the chain; see [[trap-summary-layer-is-not-evidence]].

**Encoding note, load-bearing before any quotation.** JMAP serves `charset=windows-1252`. The
quotations below were taken after `iconv -f WINDOWS-1252 -t UTF-8`, which is why the copyright
symbol resolves. Read as UTF-8 the same byte is U+FFFD, and a grep run before the decode returns
zero hits, which is indistinguishable from a host with no notice at all.

### JMAP's own notice, which is the whole of its rights position

From the footer table of every JMAP page checked, being the home page and all five
`htmlstandard/` pages, byte-exact after the decode:

> Copyright © 2004-now&nbsp; JMAP, Inc. - All rights reserved

`&nbsp;` is a non-breaking space in the source HTML, so a reader sees two spaces. The separator
before `All rights reserved` is a HYPHEN-MINUS, not a dash.

The only other rights-adjacent text in the same table cell, verbatim:

> JMAP, Inc. is a 501(c)(3) New York Not-for-Profit Corporation

and immediately before it:

> Questions should be directed to JMAP's Editor, Steve Sibol or Cofounder, Steve Watson

**There is no licence page, no terms page and no permissions page.** A `grep -i` for
`copyright|©|&copy;|reserved|permission|terms|licen` over the raw bytes of
`htmlstandard/G.SRT.C.7.htm` returned, after decoding, only the footer line above.
`htmlsupport/ABOUT_JMAP.htm` is a hard Apache 404 with a 355-byte body. Nothing in this cluster
returned 403 or 406, so the absence is a real absence and not a block. See
[[trap-down-is-not-one-state]].

### What JMAP says about itself, which is JMAP's claim and not a measurement

From the promotion block at the head of every page, verbatim:

> JMAP 's first iteration began with 611 Math A Regents questions after the January 2005 Exam.

> Revised for the 2005, CC and current curricula, JMAP now offers 10,212 questions.

The banner above it reads `10,000+ Regents Questions on JMAP`, and the archive navigation labels
its three eras `CCSS (2015-2026)`, `IA/GE/A2 (2007-17)` and `Math A/B (1998-2010)`. These are
JMAP's figures about JMAP, reproduced as such.

### The one standard page reproduced in full, so the shape is legible

`https://www.jmap.org/htmlstandard/G.SRT.C.7.htm`, HTTP 200, 22793 bytes. Standard text as printed
on the page:

> Explain and use the relationship between the sine and cosine of complementary angles

| Group | Worksheet | Series | Counts | Formats |
|---|---|---|---|---|
| REGENTS WORKSHEETS | Regents-Cofunctions 1 | GEO/GEO | 3/26 | TST PDF DOC |
| REGENTS WORKSHEETS | Regents-Cofunctions 2 | B/SIII | 1/15 | TST PDF DOC |
| LINK | Wikipedia-Cofunctions | | | LINK |

C.7 is the only one of the five standards with no PRACTICE WORKSHEETS group. The staged extract
records B.4 at 7 Regents rows and 3 Practice rows, B.5 at 8 Regents rows, 16 Practice rows and
2 Journal rows, C.6 at 1 Regents row and 1 Practice row and called the thinnest of the five, and
C.8 at 12 Regents rows, 8 Practice rows and 1 Journal row and called the thickest.

### Where the underlying items' terms actually live

`https://www.nysedregents.org/`, the host that serves the exams, has no copyright, licence, terms
or permission text of its own. What it has is a footer link, verbatim from its raw HTML:

```html
 <div id="bottom_footer_link">
 <a href="http://www.nysed.gov/contact-NYSED">Contact NYSED</a> | 
 <a href="http://www.nysed.gov/about/index-a-z/">Index A - Z</a> | 
 <a href="http://www.nysed.gov/terms-of-use#Accessibility"> Accessibility</a> | 
 <a href="http://www.nysed.gov/terms-of-use">Terms of Use</a> 
 </div>
```

That link is the only bridge between the two hostnames. Say it that way rather than asserting the
two hosts are one rights domain. The exam PDFs themselves carry nothing: `pdftotext -layout` over
`geometrycc/117/geomcc12017-exam.pdf` and its rating guide, then a grep for
`copyright|reserved|reproduc|permission|©`, returned zero hits in both. The exam's last printed
line is `Printed on Recycled Paper`.

### The NYSED grant, verbatim

From `https://www.nysed.gov/terms-of-use`, HTTP 200, under the heading `Copyright`. One continuous
passage; the paragraph breaks are as rendered.

> Except as expressly provided to the contrary on any individual document(s) or material(s) published on the New York State Education Department Website, permission to copy, use, and distribute materials created by and/or credited to the New York State Education Department and contained on the New York State Education Department Website is hereby granted without fee for personal, private and educational purposes, except that reproducing materials for profit or any commercial use is strictly forbidden without express prior written permission of the New York State Education Department. Requests for permission should be sent to legal@nysed.gov. Any reproduction or distribution of such materials must expressly credit the State Education Department in a manner likely to inform any recipient as follows (Fill in information indicated by brackets and omit brackets):

> From the New York State Education Department. [Name of article/document.] Internet. Available from [specific webpage on State Education Department Website]; accessed [date, month, year].

> Permission to copy, use, and distribute materials as described above shall not extend to information housed on this Website that is credited to other sources, or to information on Websites to which this site links.

Three riders live inside that grant and must never be quoted away from it.

1. **The opening carve-out.** A per-document statement overrides the site grant. The January 2017
   exam PDF checked carries no such statement, so nothing overrides it there, but this is a
   per-document question and cannot be answered once for the archive.
2. **The commercial bar.** Reproducing for profit or any commercial use is strictly forbidden
   without express prior written permission.
3. **The third-party and linked-site exclusion.** The final paragraph withdraws the grant from
   anything credited to other sources and from information on websites this site links to. JMAP is
   a website nysed.gov does not link, and jmap.org is not the NYSED website, so the grant does not
   travel to JMAP's copies by its own terms.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name JMAP, link a standard page or worksheet, state which standard it indexes, describe in your own words what it holds | yes | none, and no licence is needed to do this |
| Quote: reproduce JMAP's item text, answer-key prose or worked solutions | no | JMAP asserts all rights reserved and grants nothing |
| Paraphrase and republish: rewrite a JMAP item and ship it | no | same, and see [[trap-sharealike-contaminates-by-paraphrase]] for why close rewriting is not an escape from a rights problem |

### The layer that needs no licence at all

Facts, titles, codes and structural observations are not protected expression, and this is where
JMAP's real value sits for a build like this one.

- Which standards carry many worksheets and which carry one, and what the archetype names are
  (`Regents-Side Splitter Theorem`, `Regents-Special Right Triangles`, `Regents-Using Trigonometry
  to Find an Angle`, and so on).
- That C.7 has no PRACTICE group while C.6 has one Regents row and C.8 has twelve.
- That items are provenance-tagged at all, and what the tag format is.
- That `.doc` and `.tst` exist alongside `.pdf`, which is a fact about the host's affordances.

Naming, linking and describing are unconstrained by every source in this corpus. See
[[concept-cite-quote-adapt]] and [[practice-cite-without-redistributing]].

### If you take an item from NYSED directly, this is the required credit

The template is prescribed, not free-form. Fill the brackets and omit them:

```
From the New York State Education Department. [Name of article/document.] Internet.
Available from [specific webpage on State Education Department Website];
accessed [date, month, year].
```

This still leaves you inside the commercial bar. Under the project's governing ruling the repository ships
CC BY 4.0, and CC BY 4.0 grants downstream use for any purpose including commercially. NYSED's
grant forbids exactly that. This project's reading, stated as this project's reading and not as
NYSED's: NYSED-granted item text cannot be folded into a CC BY 4.0 deliverable, because the
outbound licence would purport to grant what the inbound grant withholds. Citation is unaffected.

### What no grant here reaches

- JMAP's arrangement, its indexing, and its worked answer keys, which are the parts a reader is
  most tempted by.
- Anything JMAP holds that originates with a third party, since JMAP's compilation notice is an
  assertion over an arrangement and says nothing about who owns the items. See
  [[concept-chain-of-title]].
- Any commercial use of NYSED material without express prior written permission.

## Gotchas & constraints

**1. Two rights layers, and the grant does not travel between them.** This is the whole page. A
reader who finds NYSED's grant and applies it to a JMAP worksheet is applying an instrument that
excludes, in its own final sentence, information on websites NYSED links to, let alone websites it
does not. The correct move is to decide which host you are actually taking bytes from and read
that host's instrument.

**2. This project's own records overstate the NYSED restriction, and that is also an error.** The
INVENTORY row for this source, and this project's wide-sweep reuse table, both describe NYSED as
`School-use reproduction only, no electronic distribution`. The fetched bytes do not support it.
The word `electronic` does not appear in the granting passage, `distribute` does appear and is
granted, and the qualifiers actually written are `personal, private and educational purposes` plus
the for-profit bar. Recorded here as **unverified and probably wrong**: the narrower claim needs a
different pasted sentence from a different NYSED instrument, and no such sentence is in the staged
corpus. Erring restrictive is still erring.

**3. The sitting-count figure is unresolved inside this project and must not be published as
either number.** This project's wide sweep records "17 distinct NY Regents administrations,
June 2015 to January 2026" in one passage and "22 NY Regents administrations from June 2015 to
June 2026" in another, and the sweep document preserves the discrepancy explicitly rather than
resolving it. INVENTORY.md repeats the first. The staged extract publishes the 29 REF codes
themselves and states that it publishes the codes and not a derived tally. Anyone who needs the
number re-decodes the worksheet and says so.

**4. Do not sum the count columns.** Items are indexed under more than one standard. The staged
extract names the instance: `Regents-Similarity 1`, series `GEO/GEO`, counts `4/26`, appears
under both B.4 and B.5. A naive total double-counts.

**5. The series abbreviations are undefined in the delivered bytes.** `GEO`, `GE`, `A`, `A2`, `B`,
`IA` and `SIII` are never expanded anywhere JMAP serves. The nearest adjacent evidence is the
archive navigation's three era labels. The REF suffixes in the worksheet PDFs are independent
evidence and correlate with the series column, but the mapping itself is inference. Treat it as
unresolved or ground it in the suffixes, and never present an expansion as JMAP's own.

**6. Two REF codes in Cofunctions 1 do not fit the format, and the century is not in the code.**
`fall1407geo` and `spr1407geo` replace the two-digit month with a season word. Separately, a
two-digit year cannot distinguish 1996 from 2096, and Cofunctions 2 contains `069621siii` and
`019729siii` alongside `010320b`. The century is recoverable only from the exam-series suffix,
which is a property of when that series existed. Any decoding that reads `96` as 2096 is unfounded.

**7. `Cofunctions2.pdf` extracts into the Unicode Private Use Area, and a grep over that is
silent.** The PDF embeds Symbol fonts as CID TrueType with Identity-H, so `pdftotext` emits
Symbol-font glyphs at Symbol code plus 0xF000: U+F02B for `+`, U+F03D for `=`, U+F0B0 for the
degree sign, U+F0D0 for the angle sign. Cofunctions 1 extracts as clean Unicode, so this is a
property of the older document and not of JMAP. The lesson generalises: an extraction that silently
loses operators looks like a document that never contained them.

**8. The defective released item, which is a design finding rather than a rights one.** Question 1
of Cofunctions 2, REF `010320b`. With the Private Use codepoints resolved, JMAP's answer note
reads:

> 6A + 9A = 90. As originally written, distractor (3) was A = 54, also a correct response.

Note what the bytes do and do not carry: there is an angle sign in the question stem before `A`
and none in the answer note, so the note reads `A = 54` and not `m∠A = 54`. Carry that into
authoring. Cofunction equations have solutions outside the acute branch unless the domain is
constrained.

**9. The format tokens are never defined either.** `TST`, `DOC`, `WS` and `TNS` appear as link
labels and in the site-wide format legend, and JMAP expands none of them. The left navigation
carries an `EXAMVIEW` link, which is adjacent evidence and not a definition.

**10. A licence that is one footer line can change without leaving a trace anywhere else.** There
is no terms page to diff and no effective date to compare against. The only re-verification
available is re-fetching the footer and recording a new date. See
[[trap-license-withdrawn-after-citation]] and [[license-withdrawn-grants]].

## Related

- [[license-all-rights-reserved]] holds the positively-asserted reservation this host carries, and
  the reasons that string is an unreliable signal in both directions.
- [[concept-chain-of-title]] is why a compilation notice over items a host did not author settles
  less than it appears to, and it is the shape of the JMAP layer exactly.
- [[concept-cite-quote-adapt]] is the three-operation split the verdict table above applies.
- [[source-engageny-nysed]] is the other place NYSED appears in this corpus, under a different
  instrument on a different host, and it carries its own pasted evidence. Do not read either page's
  licence finding onto the other.
- [[source-ohio-released-items]] is the other released-item archive in this corpus. Same verdict,
  different reason: no reuse permission for Ohio's items was located in its documents, rather than
  an asserted reservation. Those documents do carry a third-party permission sentence, and reading
  it as reaching Ohio's items is the error that page records.
- [[trap-access-is-not-a-rights-fact]] is why free, unauthenticated PDFs in three formats prove
  nothing about reuse.
- [[trap-down-is-not-one-state]] is the failure-mode vocabulary this page's 404s are named in: a
  hard Apache 404 on `ABOUT_JMAP.htm`, and two styled soft-404s on `nysed.gov`.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above is a pasted byte.
- [[trap-code-form-silent-zero]] matters here because JMAP indexes under `G.SRT.C.7`, which is not
  the canonical `HSG-SRT.C.7` form, and non-canonical forms fail silently rather than loudly.
- [[evidence-c7-store-gap-not-corpus-gap]] is where this host's item census does its real work: it
  is part of what retired this project's claim that C.7 is externally scarce.
- [[k12-assessment-gap]] is the machinery side of what JMAP's blueprint feeds.

## Composes with

- [[practice-cite-without-redistributing]] is the mechanical procedure for extracting full value
  from a cite-only host, and JMAP is the corpus's clearest case of a source worth a great deal with
  no reusable expression in it.
- [[practice-format-an-assessment-artifact]] is where the archetype names and relative weights read
  off this host become an item bank written from scratch.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict,
  and re-running it here means re-fetching one footer line, because there is no terms page.

## References

Host pages, fetched by this project on 2026-08-08, all `curl` to disk and read from disk:

- `https://www.jmap.org/` HTTP 200, 29257 bytes. The footer notice, the self-description block, the
  archive era labels.
- `https://www.jmap.org/htmlstandard/G.SRT.C.7.htm` HTTP 200, 22793 bytes, with B.4, B.5, C.6 and
  C.8 equivalents at 29688, 39460, 22869 and 39140 bytes. The per-standard worksheet index.
- `https://jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.pdf` HTTP 200, 143957 bytes. 29 REF codes and
  the answer-section prose.
- `https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions2.pdf` HTTP 200, 86192 bytes. 16 REF codes,
  the Private Use Area extraction problem, and the defective-item note.
- `https://www.jmap.org/htmlsupport/ABOUT_JMAP.htm` HTTP 404, 355-byte hard Apache body.
- `https://www.nysedregents.org/` HTTP 200, 10334 bytes, and `/geometrycc/` HTTP 200, 22598 bytes.
  Zero rights text of their own; the footer link block reproduced above.
- `https://www.nysedregents.org/geometrycc/117/geomcc12017-exam.pdf` HTTP 200, 211515 bytes, and
  its rating guide HTTP 200, 71584 bytes. Zero rights hits in either.
- `https://www.nysed.gov/terms-of-use` HTTP 200, 54267 bytes. The `Copyright` section reproduced
  above. `/copyright` and `/terms-use` both HTTP 404 with 48125-byte styled bodies.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/host-jmap.md`, primary. The fetch log, the windows-1252 decode note, the footer notice,
  all five standard tables, the 45 REF codes, the Private Use Area mapping, the defective item, and
  §7 on NYSED including §7c, which is the source of gotcha 2.
- `sources/verdict-wide-sweep.md`, reference. This project's own adjudication of eight sweep
  reports, which fetched nothing and says so: the reuse-terms table row for JMAP, the retirement of
  the assessment-item scarcity claim, and the preserved 17-versus-22 discrepancy in gotcha 3.

This project's own rulings, cited as this project's decisions and not as any outside party's:

- the project's governing ruling: the repository ships CC BY 4.0. That is what makes NYSED's
  commercial bar bite on the outbound side.
