---
title: openmiddle.com
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://www.openmiddle.com/
  - https://www.openmiddle.com/category/high-school-geometry/similarity-right-triangles-and-trigonometry/
  - https://www.openmiddle.com/about-embedding/
  - sources/host-open-middle.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# openmiddle.com

## Summary

`openmiddle.com` is **all rights reserved**, rights-holder **Glenrock Consulting, LLC**. Verdict:
`cite_only`. Citing and linking is unaffected, because citation is not redistribution and an
all-rights-reserved assertion does not restrict it.

This page exists because two different things about this host are commonly wrong, and they fail in
opposite directions.

**It reads as dead and it is live.** A default user agent gets HTTP 406. A browser user agent gets
HTTP 200 and 100,227 bytes of page. An automated link checker running the default agent will
report this host as broken, and a research agent that stops at the 406 will record the licence as
unverifiable. The 406 is a server-side or WAF user-agent filter, which is to say a bot block, and
`robots.txt` returns 200 and does **not** exclude general crawlers: it allows `*` with
`Crawl-delay: 2` and disallows only Baiduspider, Sosospider and one `wp-content` path. The block
contradicts the site's own published crawl policy.

**It reads as CC BY-NC-SA and it is not, any more.** Open Middle carried CC BY-NC-SA 4.0 from 2016
until the CC clause was deleted from the footer **between 2026-02-16 and 2026-03-03**. Every
third-party OER list, every citation written before March 2026, and any model prior formed on that
decade still says otherwise. The correct sentence is: *Open Middle was CC BY-NC-SA 4.0 until
between 2026-02-16 and 2026-03-03; it is now all rights reserved, rights-holder Glenrock
Consulting, LLC.*

A **separate and later** event moved the rights-holder from Open Middle Partnership to Glenrock
Consulting, LLC, between 2026-03-03 and 2026-05-12. Two events, two windows, in that order. A page
that merges them into one change mis-dates both.

## When to reach for it

Reach for it to **cite and to link**, and for problem-structure inspiration you then write
yourself. The format itself is an idea rather than protected expression, and the site has an
exactly-matching category for this unit.

`https://www.openmiddle.com/category/high-school-geometry/similarity-right-triangles-and-trigonometry/`,
H1 "Similarity, Right Triangles, and Trigonometry", HTTP 200, **10 problems, no pagination**. All
10 were opened individually. Mapped against the five target standards using the site's own tags:

| Standard | Coverage on this host, by the site's own tags |
|---|---|
| B.4 | 1 problem, Law of Cosines Triangle (`g-srt.4`). This project calls it thin |
| B.5 | 1 direct, Finding the Length of a Right Triangle's Altitude (`g-srt.5`), plus 2 tagged `g-srt.2` which sit just upstream at SRT.A.2 |
| C.6 | 1 problem, Simplifying Rational Expressions (`g-srt.6`). The title is misleading against its tag |
| C.7 | **ZERO. Confirmed gap.** No `g-srt.7` tag appears on any of the 10 category members |
| C.8 | 5 problems, the strongest area: Trigonometric Ratios, Pythagorean Inequality, Three Triangles And A Wannabe, Equilateral Triangle Side Length, Finding the Length of a Right Triangle's Altitude |

Two further problems tagged `g-srt.11` sit beyond the unit. Those tag strings are the host's own
code forms, reproduced as the host writes them. This project's form is `HSG-SRT.C.6` and its
equivalents, and a near-miss form returns zero rows against this project's store with no error;
see [[trap-code-form-silent-zero]].

Do **not** reach for this host for exposition, worked examples or diagrams. Each page is a short
"Directions:" constraint task, typically of the form "using the digits 0 to 9 at most one time
each, place a digit in each box", plus a collapsible Hint, a collapsible Answer with full solution
methods, a DOK rating of DOK 2 or DOK 3, and a contributor byline. Its value here is warm-up and
closure structure for C.8, cited and linked, and nothing more.

Do not reach for it to fill C.7. It will not.

## What its own page says

**The footer is the only licence-bearing text on this site, and this was confirmed three
independent ways.** All of the following returned HTTP 404 under a browser user agent, serving the
site's roughly 92KB soft-404 template: `/terms/`, `/terms-of-use/`, `/terms-of-service/`,
`/copyright/`, `/permissions/`, `/license/`, `/licensing/`, `/faq/`, `/privacy/`,
`/privacy-policy/`. What exists at HTTP 200 is `/about/` (301 to `/about-embedding/`),
`/whats-open-middle/`, `/open-middle-team/`, `/submit/`.

The three confirmations, all this project's own measurement:

1. **`page-sitemap.xml`, HTTP 200.** The complete page list is `/`, `/advanced-search/`,
   `/whats-open-middle/`, `/open-middle-team/`, `/submit/`, plus `es/` and `fr/` translations. No
   terms, privacy, copyright or license page.
2. **The site's own search.** `/?s=copyright`, `?s=license` and `?s=permission` returned zero
   content results.
3. **Wayback CDX.** Zero captures ever for `openmiddle.com/terms*`, `/copyright*`, `/license*`,
   `/privacy*`. The endpoint was proven working by control queries against the root and
   `/similar-triangles/`, which both returned capture rows.

### The live footer, verbatim

`https://www.openmiddle.com/`, HTTP 200 under a browser user agent, 2026-08-08:

> © 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered
> trademark of Glenrock Consulting, LLC.

Extraction method, recorded because a negative result depends on it: the agent tag-stripped the
raw HTML around the matched string rather than reading a fetch summary. See
[[trap-summary-layer-is-not-evidence]]. `grep -c creativecommons` returned **0** for the root, the
category page, the embedding page and all 10 problem pages.

### The per-resource pages, where the finding is the absence of variation

Ten problem pages were opened individually, all HTTP 200, browser user agent, 2026-08-08. Every
one carries the same site-wide all-rights-reserved footer and **no per-resource licence notice of
any kind**. Verified per page: `creativecommons` absent, `All rights reserved` present. Each
problem does carry a named individual contributor byline, in the site's own form "Source: Drew
Ross", "Source: Kate Nerdypoo", "Source: Robert Kaplinsky" and so on.

### The archived footers, which is where the date evidence lives

Wayback `id_` raw captures, fetched with `curl --compressed`, 2026-08-08. This project's own
measurement:

| Snapshot | CC present | Verbatim footer fragment |
|---|---|---|
| 2016-05-27 | YES | "Open Middle is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2019-06-03 | YES | "Open Middle ® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2023-06-01 | YES | "© 2016-2023 Open Middle Partnership. All rights reserved. ... Open Middle® problems are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| 2026-01-09 | YES | "© 2016-2026 Open Middle Partnership. All rights reserved. ... licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0" |
| **2026-02-16** | **YES** | the last capture carrying CC |
| **2026-03-03** | **NO** | "© 2016-2026 Open Middle Partnership. All rights reserved. Open Middle is the registered trademark of the Open Middle Partnership. Get in contact with us" |
| 2026-05-12 | NO | "© 2016-2026 Glenrock Consulting, LLC. All rights reserved. Open Middle is the registered trademark of Glenrock Consulting, LLC." |
| **2026-08-08 (live)** | **NO** | same as 2026-05-12 |

The CC deed URL as it appeared in every historical footer was
`http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US`.

Note what the 2023 and 2026-01 rows show: **"All rights reserved" and a CC grant coexisted in the
same footer for years.** The string is not a reliable signal on its own in either direction. What
changed in early 2026 is the disappearance of the second sentence, not the appearance of the
first.

### The sanctioned embed, verbatim

`https://www.openmiddle.com/about-embedding/`, HTTP 200. The site documents an official "Use this
problem" iframe embed into Canvas, Google Classroom, Microsoft Teams and elsewhere, with toggles
for title, hint and answer:

> Embedded problems allow you to add interactive problems to your Canvas page, websites, and many
> other locations.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state what standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | no | there is no grant to rely on; a short attributed quotation would rest on fair use, which is a legal judgment no agent in this project made |
| Paraphrase and republish: rewrite its material and ship it | no | same, and closer to the line than quotation |

**Citing is unconstrained here.** Naming the problem, naming its contributor, linking its URL and
stating which standard it is tagged to are facts and references, not protected expression. All
rights reserved does not reach them. See [[concept-cite-quote-adapt]] and
[[practice-cite-without-redistributing]].

Bibliographic form, as this project assembled it:

```
"<Problem title>", <Contributor name>. Open Middle® (Glenrock Consulting, LLC).
https://www.openmiddle.com/<slug>/  · Accessed 2026-08-08.
```

Both names belong in the line. The site itself credits an individual per problem while asserting
blanket rights corporately, and a citation that reproduces only one half misstates the record on
its face. See [[concept-attribution-per-record]].

### What is not available here

- **No CC fallback.** Any plan that involved reproducing, adapting or ShareAlike-republishing Open
  Middle problem text no longer has a licence under it. All rights reserved is strictly more
  restrictive than the CC BY-NC-SA it replaced.
- **No trademark grant.** "Open Middle is the registered trademark of Glenrock Consulting, LLC."
  Trademark is separate from copyright and survives whatever the copyright posture is. Do not
  brand this project's materials with the name or imply endorsement. Nominative reference, such as
  describing a task as being in the Open Middle format with a citation, is a different matter.
- **No right conveyed by the embed.** See gotcha 3.

## Gotchas & constraints

**1. A default user agent reports this host as broken.** HTTP 406, zero redirects, on
`curl -L https://www.openmiddle.com/` with the default agent. The same URL with a browser agent
returns HTTP 200 and 100,227 bytes. This is one of several distinct failure signatures that all
present as "down"; the correct move here is to retry with a browser agent, which is not the
correct move for an expired certificate or a TLS handshake failure. See
[[trap-down-is-not-one-state]].

**2. The soft-404 template is large enough to pass a size check.** The policy paths return the
site's full 404 template at roughly 92KB. The status code is honest here, but a probe that treats
a substantial response body as evidence a page exists would read all ten of those paths as live
policy documents. The inverse shape, where nonexistent paths return HTTP 200, is the one that
costs more; see [[trap-soft-404-status-proves-nothing]].

**3. The sanctioned embed is a use pathway, not a copyright licence.** The iframe serves content
from their domain, under their control, and can be changed or withdrawn by them. It grants no
right to copy problem text into a repository, and an iframe to a third-party host is a dependency
rather than an asset. See [[trap-access-is-not-a-rights-fact]].

**4. Raw Wayback `id_` captures return compressed bytes, and a grep over them reports a false
absence.** This project's first pass at the 2026-03-03 snapshot read gzip bytes as text and
appeared to show no footer at all. That was a fetch artefact, not a finding, and it was re-fetched
with `curl --compressed` before any conclusion was drawn. The date table above rests on the
re-fetch. See [[trap-compressed-body-grepped-as-text]].

**5. The contributor rights chain is undocumented, and the ARR footer does not settle it.** Every
problem carries a named individual byline while the site asserts blanket all-rights-reserved.
`/submit/` contains only an invitation to contribute and an externally-loaded form body reading
"Loading…", with no copyright-assignment or licensing language presented to contributors on the
page. **Whether the footer is legally effective over contributor-authored problems is
unverified**, and it is not resolvable by fetching. What would close it: the contributor terms
inside that form, or counsel. See [[concept-chain-of-title]].

**6. Whether the CC removal reaches copies obtained before 2026-02-16 is unresolved.** CC 4.0's
own text describes the grant as irrevocable. Whether that helps material accessed today, when no
CC offer is extended anywhere on the site, is a legal question, recorded by this project as a
question for counsel and not as a research finding.

**7. "C.7 = ZERO" is a measurement of this host's own tagged category and nothing more.** It is
correct about openmiddle.com. It is not evidence about C.7 in general: this project's later wide
sweep located 37 distinct C.7 sources, 24 of them usable treatments, and retired the general
scarcity claim as an artefact of the earlier sampling frame. See
[[evidence-c7-store-gap-not-corpus-gap]].

**8. The served `robots.txt` is malformed, and it is not licence-relevant.** The raw bytes begin
`ser-agent: *`; the leading `U` is absent, verified with `xxd`
(`73 65 72 2d 61 67 65 6e 74` = "ser-agent"). The first directive group is therefore malformed.
Recorded for accuracy so nobody re-derives it as a finding.

**9. The exact removal date is not knowable from here.** Wayback captured nothing between
2026-02-16 and 2026-03-03, so the window is the finding and a single date would be an invention.
Why the licence changed, and the nature of the Open Middle Partnership to Glenrock Consulting
transfer, are both **unverified**: no announcement post was located, and the `/category/articles/`
archive was not exhaustively searched.

**10. Re-verify before anything publishes.** This host is the reason this corpus counts folk
knowledge about open-education licensing as measured wrong three times rather than twice. A
verdict here is a timestamped observation, and this one is dated 2026-08-08. See
[[license-withdrawn-grants]] and [[trap-license-withdrawn-after-citation]].

## Related

- [[license-all-rights-reserved]] is the regime this host now sits in, and this footer is one of
  its three worked instances.
- [[license-withdrawn-grants]] is the dated register both of this host's events belong to.
- [[trap-license-withdrawn-after-citation]] is the mechanism: a citation recorded in 2025 still
  renders its CC BY-NC-SA label today, and nothing in the artifact re-checks it.
- [[trap-down-is-not-one-state]] is the 406 and its six siblings, each with a different correct
  next move.
- [[trap-soft-404-status-proves-nothing]] carries this host's 404 template as the inverse of the
  200-for-everything shape on another host.
- [[trap-compressed-body-grepped-as-text]] is the gzip near-miss behind the snapshot table above.
- [[trap-access-is-not-a-rights-fact]] holds the sanctioned-embed rider: a working retrieval path
  is not a grant.
- [[trap-code-form-silent-zero]] is why the site's `g-srt.7` tag form will not resolve against
  this project's store.
- [[concept-chain-of-title]] is the contributor-byline problem stated generally.
- [[concept-cite-quote-adapt]] is the split that makes an all-rights-reserved host still fully
  usable in a curate-and-cite unit.
- [[concept-curate-and-cite]] is the posture this host is the strongest argument for.
- [[source-achieve-the-core-sap]] is the other withdrawn grant in this corpus, inside the same
  six-month window.
- [[evidence-c7-store-gap-not-corpus-gap]] carries the correction to the C.7 scarcity reading.

## Composes with

- [[practice-cite-without-redistributing]] is the whole of what this host supports, and the
  bibliographic block above is its worked output here.
- [[practice-build-a-source-table]] is the procedure that produced the dated snapshot table, and
  the re-verification step it names is what keeps this page's verdict from going stale.

## References

Live host pages, fetched by this project on 2026-08-08 with a browser user agent:

- `https://www.openmiddle.com/` HTTP 200, 100,227 bytes. The site-wide all-rights-reserved and
  trademark footer. HTTP 406 with the default agent.
- `https://www.openmiddle.com/category/high-school-geometry/similarity-right-triangles-and-trigonometry/`
  HTTP 200. The exactly-matching category, 10 problems, no pagination, and the per-standard tally
  above.
- `https://www.openmiddle.com/about-embedding/` HTTP 200. The sanctioned "Use this problem" iframe
  embed and its verbatim description.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-open-middle.md`, primary. The reachability table, the three independent
  confirmations that no policy document exists, the live footer, the 10-page per-resource table
  with contributor bylines and tags, the dated Wayback footer table with both event windows, the
  six riders, and the seven carried-forward gaps.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 10, §2
  the verdict key and the statement that citing is unconstrained by every source in the table, §3
  correction 8, §4.10 the cite-only bibliographic form, and the inline retirement marker on the
  C.7 reading.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-open-middle.md`, the underlying fetch report.
