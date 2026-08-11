---
title: "Access is not a rights fact"
type: trap
sources:
  - sources/host-eric.md
  - sources/host-open-middle.md
  - sources/host-learnwithsap.md
  - sources/host-learning-commons-kg.md
  - sources/host-mars-map.md
  - sources/host-engageny-nysed.md
  - sources/verdict-twelve-host-table.md
  - https://eric.ed.gov/?copyright
  - https://files.eric.ed.gov/fulltext/EJ1184973.pdf
  - https://www.openmiddle.com/about-embedding/
  - https://learningcommons.org/terms-of-use/
updated: 2026-08-08
---

# Access is not a rights fact

## Summary

"Full text available on ERIC" means ERIC has permission to host the PDF. It does not mean you have
permission to reuse it. ERIC's own copyright policy says so in one sentence, verbatim:

> ERIC does not retain copyright to the works indexed in the database and cannot grant permission
> to use indexed works under copyright protection.

The generalisation is the page. **Every signal that you successfully obtained something is a fact
about retrieval, and none of them is a fact about rights.** Six such signals appear in this corpus
and each has been read as a grant by someone:

| Access signal | What it actually establishes |
|---|---|
| An index hosts the full text | The index cleared hosting with the rights-holder, for itself |
| HTTP 200 on a public URL, no login | The server answered |
| A public bulk download, no credential | The publisher chose not to gate distribution |
| A sanctioned iframe embed | A use pathway on the publisher's own infrastructure |
| A retrieval failure (403, 406, 000) | Something about your client, not about the grant |
| A login wall, or its absence | Where the operator put a door |

The evidence floor here is measured, not asserted. Of the **7** ERIC-hosted PDFs this project
actually opened, **1** carried CC BY, **2** were explicitly restrictive, and **4** were completely
silent. The licence is readable only from inside the artifact. There is no metadata shortcut, and
this project's own record names the ERIC inference "the single most dangerous inference available"
on that host.

## When to reach for it

Reach for it when a source has just been characterised by how it was obtained: it was free, it was
public, it downloaded without a login, it is on an open repository, the site let a bulk fetch
through. Those are the sentences this trap hides inside.

Reach for it before writing a reuse verdict for any research paper, any PDF served by a host that
did not author it, and any resource reached through an aggregator, an index, a coherence map or a
knowledge graph.

Reach for it in the opposite direction too, when a fetch failed. A 403 or a 406 is a statement
about your user agent. This project measured a live site returning **HTTP 406** to a default agent
and **HTTP 200**, 100,227 bytes, to a browser agent, on a host whose own `robots.txt` allows
general crawlers. Failure to retrieve is not evidence of anything about rights, and it is often not
even evidence about availability: see [[trap-down-is-not-one-state]].

Do **not** reach for this page to decide whether a page exists. A 200 that proves nothing about
existence is a different mechanism, the soft 404, and it belongs to
[[trap-soft-404-status-proves-nothing]].

## How it works

The mechanism is that hosting rights and reuse rights are separate grants from the same
rights-holder, and only one of them is visible to a fetcher.

**The index states the split itself.** ERIC's Copyright Policy, verbatim:

> The ERIC website contains full-text resources protected by U.S. and foreign copyright
> laws. The authors or publishers retain copyright to these works, which are used by ERIC
> with permission. All persons reproducing, redistributing, or making commercial use of
> this information are responsible for compliance with the terms and conditions asserted
> by the copyright holder.

Its Links Disclaimer extends the same logic outward, verbatim: "Once another site is accessed
through a link on the ERIC website, the copyright and licensing restrictions of the new site apply.
ERIC cannot authorize the use of copyrighted materials contained in linked websites."

**The metadata cannot carry what the host does not hold.** A full API field dump of one record,
EJ1292278, returns exactly: author, description, id, issn, language, peerreviewed,
publicationdateyear, publicationtype, publisher, subject, title. There is no licence or rights
field anywhere in ERIC metadata. Five record pages were fetched and the only occurrence of
"copyright" on any of them is the global footer navigation link.

**A downloadable file can forbid the reuse its downloadability seems to invite.** From inside
`EJ1184973.pdf`, fetched HTTP 200, verbatim:

> This article may be used for research, teaching, and private study purposes. Any
> substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing,
> systematic supply, or distribution in any form to anyone is expressly forbidden. Authors
> alone are responsible for the contents of their articles. The journal owns the copyright
> of the articles.

**A public bulk export is a distribution decision, and the operator says so.** The Learning Commons
CDN served a full JSONL export with no credential, no referer check and no bot block. That same
organisation's Terms of Use, last updated July 1, 2026, push the rights question straight back to
you, verbatim:

> In all cases, you agree to review any applicable license terms associated with Content before
> accessing or using it. You are responsible for ensuring compliance with all such terms,
> conditions, and licenses, if any.

**A sanctioned embed is infrastructure, not a licence.** Open Middle publishes an official
"Use this problem" embed, documented at `/about-embedding/`, HTTP 200, verbatim:

> Embedded problems allow you to add interactive problems to your Canvas page, websites, and many
> other locations.

That host's footer is all rights reserved. The embed serves their content from their domain under
their control. This project's reading, recorded as its own reasoning: the embed grants no right to
copy the problem text into a repository, and an iframe to a third-party host is a dependency rather
than an asset.

## In practice

**The only reliable procedure is to open the artifact and read its own notice.** Not the record
page, not the search result, not the metadata, not the aggregator's card. The file.

**What that procedure returns, measured.** Across 7 ERIC-hosted PDFs opened individually:

| Outcome | Count | Example |
|---|---|---|
| CC BY, version stated nowhere in the PDF | 1 | EJ1249368, Pedagogical Research 2020 |
| Explicitly restrictive | 2 | EJ1184973 (reuse forbidden), EJ1064122 (all rights reserved) |
| Completely silent | 4 | ED584497, EJ1315132, EJ1274131, EJ1442215 |

Silence was the modal case. Under the Berne default, silent resolves to all rights reserved rather
than to open; see [[license-unmarked-silence]].

**The mirror case, where the artifact is silent and the page holds the grant.** On
`map.mathshell.org` a summative task PDF carries, as a running footer on both pages, verbatim:
"Copyright © 2011 by Mathematics Assessment Resource Service. All rights reserved." The CC
BY-NC-ND 3.0 grant for that file exists only on the HTML page that links to it. Anyone who receives
the PDF alone sees pure all-rights-reserved. Downloading the file therefore loses the grant, and
citing the file rather than the page loses it for your reader too. Cite the page, and record it
with its fetch date.

**The worst combination, and it lands on this unit.** Achieve the Core's Coherence Map data file
served HTTP 200 at 2,296,445 bytes to an ordinary fetch and embeds the full example task text and
solution inline for all five HSG-SRT codes. A regex over the decoded inline HTML for ids 614 and
616 returned zero occurrences of "licen", "creative commons", the copyright sign, or "copyright",
and every one of the five is attributed "Provided by Illustrative Mathematics". So the material is
freely downloadable, unmarked where it sits, and authored by a third party. This project's reading,
from the one IM-authored PDF on that host it did open, is that the governing grant on that text is
IM's CC BY-NC-SA. Do not launder an IM task through Achieve the Core. Source it and clear it at IM.
See [[source-achieve-the-core-sap]] and [[concept-chain-of-title]].

**What an access fact is genuinely good for.** Citation and linking, which no source in this corpus
restricts. One artifact says so in its own words, and it is the one that otherwise reserves all
rights, `EJ1064122`, verbatim:

> Using the hyperlinks to the article is not considered a violation of copyright.

That is an access-shaped sentence that *is* a rights fact, because the rights-holder wrote it. The
distinction is authorship of the statement, not its subject matter. See [[concept-curate-and-cite]]
and [[practice-cite-without-redistributing]].

## Gotchas & constraints

**1. A 404 at `files.eric.ed.gov/fulltext/` is not a block and not a rights fact.** Two live ERIC
records, EJ1454267 and EJ1370844, simply have no ERIC-hosted full text. The record-id-to-PDF URL
pattern is not guaranteed. Absence of a file says nothing about the paper's licence.

**2. "Silent" means silent in the copy you opened.** The verifying agent recorded this limit
explicitly: it verified only that no licence text appears in the extracted text layer. A notice
rendered as an image, or living on the journal's own site rather than in the PDF, would have been
missed, and several of those journals may well be CC BY at source. So silence is not proof of
restriction any more than downloadability is proof of permission. It is an instruction to go to the
publisher, not a verdict.

**3. Seven PDFs out of millions.** The 1 CC BY, 2 restrictive, 4 silent split measures the sample,
not the population. It is enough to destroy the inference that ERIC hosting implies reuse. It is
not enough to state a rate.

**4. A login wall proves less than it looks like, in both directions.** NYSED points its EngageNY
mathematics archive at a SharePoint link that bounced an anonymous `curl` through four redirects
into `login.microsoftonline.com`. The verifying agent refused to call it gated, on the ground that
`curl` executes no JavaScript and the bounce is evidence of the client's failure rather than proof
the archive is closed. It was recorded as ambiguous. Conversely, no agent in this project registered
an account anywhere, so Illustrative Mathematics' `/oauth_im/login`, accessim's protected content and
Achieve the Core's clickwrap are all uninspected and nothing behind them is characterised here.

**5. The dedication that names its own domain does not travel.** Student Achievement Partners'
public-domain dedication is published on `learnwithsap.org/permissions/` and its own text covers,
verbatim, "All of the content on learnwithsap.org". Achieve the Core's own permissions path is a
soft 404. Whether the dedication reaches the material on the other domain is recorded by this
project as a real gap, unresolved. Reaching a file from a domain is not the same as the file being
under that domain's grant.

**6. Bulk availability can carry a revocation clause.** Learning Commons' Terms state, verbatim:
"You acknowledge and agree that a Data Provider may, at its sole discretion, revoke access to any
Content previously made available through the Services." A pinned local copy of a public export is
an access artefact whose upstream grant can move underneath it. See
[[trap-license-withdrawn-after-citation]].

**7. The failure signature you get is a property of your client.** 403 from a JavaScript challenge,
406 from a user-agent filter, 000 from an expired certificate, a 200 carrying a PHP fatal error.
Each was met in this corpus on a live site. None of them told anyone anything about a licence. See
[[trap-down-is-not-one-state]].

## Related

- [[source-eric]] is the host this trap is named after and the rights verdict on it.
- [[source-open-middle]] is the sanctioned-embed case, and [[source-achieve-the-core-sap]] is the
  host that redistributes another party's task text, unmarked, over a public URL.
- [[source-learning-commons-kg]] is the public bulk export with a revocation clause and a
  responsibility-shifting terms page.
- [[source-mars-map]] is the mirror case where the artifact reserves rights and the page grants
  them; [[source-engageny-nysed]] is the archive whose gating could not be established from a
  non-JavaScript client.
- [[license-unmarked-silence]] is what a silent artifact resolves to, and
  [[license-all-rights-reserved]] is the positively asserted case whose string is unreliable in both
  directions.
- [[concept-chain-of-title]] is the pattern behind the Coherence Map case, and
  [[concept-cite-quote-adapt]] is the operation split that decides what an access fact licenses.
- [[trap-down-is-not-one-state]] is the inverse trap, where a retrieval failure gets read as a fact
  about the source, and [[trap-soft-404-status-proves-nothing]] is where a 200 is not even evidence
  of existence.
- [[trap-license-withdrawn-after-citation]] is why an artefact obtained today can outlive the grant
  it was obtained under.
- [[evidence-misconception-research-licensing]] is the per-paper record this trap's procedure
  produced for the research literature on these five standards.

## Composes with

- [[practice-build-a-source-table]] is the procedure that replaces the access inference with a
  verdict: raw bytes, HTTP status, fetch date, and an explicit unverified column.
- [[practice-cite-without-redistributing]] is what to do with everything this page has just ruled
  out of reuse, which in this corpus is most of the research literature.

## References

Primary evidence, fetched by this project 2026-08-08 and staged verbatim in this wiki:

- `https://eric.ed.gov/?copyright` HTTP 200, 9190 bytes. The Copyright Policy and the Links
  Disclaimer quoted above.
- `https://files.eric.ed.gov/fulltext/EJ1184973.pdf` HTTP 200. The in-PDF prohibition on
  reproduction and redistribution.
- `https://www.openmiddle.com/about-embedding/` HTTP 200 with a browser user agent.
- `https://learningcommons.org/terms-of-use/` HTTP 200, page states "Last updated: July 1, 2026".

Staged extracts, all staged 2026-08-08:

- `sources/host-eric.md`, primary. §2 the site-level policy verbatim, §3 the API field dump and the
  five record pages, §4 the seven per-PDF samples and the 1/2/4 tally, §7 the report's bottom line
  naming the access-to-rights inference the most dangerous one on that host.
- `sources/host-open-middle.md`, primary. §1 the 406-to-200 user-agent measurement, §3 the live
  footer, §6 rider 4 on sanctioned embedding.
- `sources/host-learnwithsap.md`, primary. §3a the dedication naming its own domain, §5 sample 4 the
  Coherence Map data file and its measured absence of any licence string, §8 the recorded gap
  between the two domains.
- `sources/host-learning-commons-kg.md`, primary. §4 the uncredentialed CDN export, §8 the Terms of
  Use passages quoted above.
- `sources/host-mars-map.md`, primary. §4b the task PDF whose own footer reserves all rights while
  the linking page grants CC BY-NC-ND 3.0.
- `sources/host-engageny-nysed.md`, primary. §5 the SharePoint bounce and the agent's refusal to
  call it gated.

This project's own adjudication, cited as this project's reasoning and not as any outside party's
statement: `sources/verdict-twelve-host-table.md` §1 rows 9, 10 and 11, and §6 the sampling limits
and the registration-gated surfaces no agent opened.
