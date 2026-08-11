---
title: "EngageNY / NYSED (engageny.org to nysed.gov)"
type: source
verdict: quote_sharealike
fetched: 2026-08-08
sources:
  - https://www.nysed.gov/standards-instruction/standards-resources-and-supports
  - https://web.archive.org/web/20220618120326/https://www.engageny.org/terms-of-use
  - https://www.nysed.gov/terms-of-use
  - https://web.archive.org/web/20220130113349/https://www.engageny.org/resource/geometry-module-2-topic-e-lesson-25
  - https://creativecommons.org/licenses/by-nc-sa/3.0/
  - sources/host-engageny-nysed.md
  - sources/cc-by-nc-sa-3-0.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# EngageNY / NYSED (engageny.org to nysed.gov)

## Summary

EngageNY is retired. Its curricular documents carry a Creative Commons
Attribution-NonCommercial-ShareAlike grant and the content is reachable. Verdict:
`quote_sharealike`. The NonCommercial rider travels with that verdict even though the
single-token verdict name does not carry it, so read this page as `quote_sharealike` plus
`quote_noncommercial`, not as one or the other.

**The reachability failure is four separate facts, and collapsing them into "the site is down"
loses a live source.** The finding handed to this project's verifying agent was "HTTP 000, does
not resolve". The `000` is real. The conclusion drawn from it was wrong, and the report records
the prior finding as partially confirmed with the reason overturning the conclusion.

| Probe, run by this project 2026-08-08 | Result |
|---|---|
| `dig +short engageny.org A` | empty; the apex does NOT resolve, NXDOMAIN |
| `dig +short www.engageny.org A` | CNAME to `sedldbal.nysed.gov.` then 149.10.125.41, .40 |
| `curl https://engageny.org/` | `curl: (6) Could not resolve host`, http_code=000 |
| `curl https://www.engageny.org/` | `curl: (60) SSL certificate problem: certificate has expired`, http_code=000 |
| `curl -k https://www.engageny.org/` | 301 to `http://www.nysed.gov/curriculum-instruction/engageny` |
| `curl http://www.engageny.org/` | 301 to the same target |
| `curl -L http://www.engageny.org/` | 200, 3 redirects, final `https://www.nysed.gov/standards-instruction/standards-resources-and-supports#engageny` |

Two independent causes sit behind one status code: a dead apex and an expired TLS certificate on
`www`. A default HTTPS fetcher fails closed on both and reports the same `000`. The verifying
agent's own emphasis, quotable as this project's measurement and not as NYSED's statement: **not
dead, not bot-blocked, a live redirector with a broken cert.** Nameservers include
`srv21.nysed.gov`, so the domain was never abandoned or squatted. Wayback snapshots all return
200, which is what rules out a bot block.

Three more facts a reader has to carry off this page, because each one alone is misleading:

1. **There are two licence versions in play on this host and its successor.** Site-wide prose
   links 3.0 Unported. Every per-resource badge pins 3.0 US. Those are different legal
   instruments at different URLs.
2. **NYSED states in writing that it is not the copyright owner**, and it names no one who is.
   The widely repeated attribution to Great Minds or Eureka Math is not in this project's
   verified record and is not asserted here.
3. **Course index pages carry no Creative Commons marking at all.** The CC field is per-resource
   metadata. It is asserted only where populated, so "this host is CC BY-NC-SA" is a claim about
   individual resources and not about the host.

## When to reach for it

Reach for it for Geometry Module 2, titled "Similarity, Proof, and Trigonometry", which is
directly on this unit. The host tags the module `G.SRT.1` through `G.SRT.8` plus `G.MG.1`. Those
are the host's own code forms, recorded as the host writes them; this project's code form is
`HSG-SRT.C.6` and its equivalents, and the two are not interchangeable in a lookup. See
[[trap-code-form-silent-zero]].

Topic structure, from the Geometry course index page as this project read it:

- Topic A Scale Drawings (L1-5), Topic B Dilations (L6-11), Topic C Similarity and Dilations (L12-20)
- Topic D "Applying Similarity to Right Triangles" (L21-24), which this project maps to B.4 and B.5
- Topic E "Trigonometry" (L25-34), which this project maps to C.6, C.7 and C.8

Three standard-to-lesson anchors were verified individually on the resource pages themselves,
which is a better class of fact than the topic mapping above: **L21 to G.SRT.4**, **L25 to
G.SRT.6**, **L34 to G.SRT.8**. Each lesson ships a Teacher Version and a Student Version PDF, and
the module ships full zips including Spanish and Chinese translations. Per-lesson granularity is
what makes precise citation easy here.

Reach for it to **quote and to cite**. Do not reach for it as a paraphrase-and-adapt source: the
ShareAlike rider would force the derivative under CC BY-NC-SA, and under this project's ruling R9
the repo ships CC BY 4.0 and takes no paraphrase from any ShareAlike source, ever. That ruling,
not the licence, is what fixes this host's operative use at quote-only. See
[[trap-sharealike-contaminates-by-paraphrase]].

Do not reach for it for figures. The archived terms carve out all images, and whether that
carve-out reaches images inside the CC-licensed module PDFs is unresolved. Treat module diagrams
as not cleared.

## What its own page says

Every quotation below was captured by a fetching agent on 2026-08-08 and is staged verbatim in
`sources/host-engageny-nysed.md`. The live NYSED statement was confirmed from raw HTML rather
than from a model summary; see [[trap-summary-layer-is-not-evidence]].

### The live successor statement on nysed.gov

`https://www.nysed.gov/standards-instruction/standards-resources-and-supports`, HTTP 200, fetched
2026-08-08:

> The New York State Education Department discontinued support for the EngageNY.org website on
> July 7, 2022. The NYSED encourages educators to download any EngageNY content they wish to use
> in the future from our archive sites below. All ELA and mathematics curriculum files will be
> available at the links below, and will remain free and licensed under the Creative Commons
> Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.

The prose names **no version**. The anchor `href` on that sentence is
`https://creativecommons.org/licenses/by-nc-sa/3.0/`, which is 3.0 Unported.

### The archived EngageNY Terms of Use

`https://web.archive.org/web/20220618120326/https://www.engageny.org/terms-of-use`, snapshot
2022-06-18, fetched 2026-08-08, HTTP 200. The grant:

> The curricular documents and videos provided on EngageNY, including all materials linked from
> the curriculum page and the video library, are licensed under the Creative Commons Attribution
> Non-Commercial Share-Alike license and are subject to the copyright rules under that license.
> All documents posted on EngageNY that are subject to the Creative Commons Attribution
> Non-Commercial Share-Alike license are identified using this icon:

The sentence that limits everything else on this page:

> Commercial use of the curricular materials is not allowed under this license. Furthermore,
> NYSED is not the copyright owner of the curricular materials but rather NYSED holds a license
> to use the materials. As such, any use of the curricular materials beyond those allowed under
> the Creative Commons license would require the express written permission of the copyright
> owners.

The separate, non-CC grant covering other EngageNY materials:

> Except as expressly provided to the contrary for any specific document(s) or material(s)
> published on EngageNY.org, permission to copy, use, and distribute materials created by and/or
> credited to EngageNY.org or the New York State Education Department (NYSED) and contained on
> EngageNY.org is hereby granted without fee for personal, private, and educational purposes.
> Generally, reproducing materials for profit or any commercial use is strictly forbidden.

The mandated attribution format, verbatim, including its bracketed slots:

> From EngageNY.org of the New York State Education Department. [Name of article/document.]
> Internet. Available from [specific webpage on EngageNY.org]; accessed [date, month, year].

The carve-out, verbatim:

> Permission to copy, use, and distribute materials as described above shall not extend to the
> following:  All images on EngageNY / Information housed on EngageNY.org that is credited to
> other sources / Information on websites to which this site links

The CC link href on this page is also `creativecommons.org/licenses/by-nc-sa/3.0/`, 3.0 Unported.

### The NYSED umbrella terms, which are a different and narrower grant

`https://www.nysed.gov/terms-of-use`, HTTP 200, fetched 2026-08-08. `/terms-use` and
`/about/terms-use` were both tried and both returned 404. This page never mentions Creative
Commons at all:

> Except as expressly provided to the contrary on any individual document(s) or material(s)
> published on the New York State Education Department Website, permission to copy, use, and
> distribute materials created by and/or credited to the New York State Education Department and
> contained on the New York State Education Department Website is hereby granted without fee for
> personal, private and educational purposes, except that reproducing materials for profit or any
> commercial use is strictly forbidden without express prior written permission of the New York
> State Education Department. Requests for permission should be sent to legal@nysed.gov.

Its own attribution format:

> From the New York State Education Department. [Name of article/document.] Internet. Available
> from [specific webpage on State Education Department Website]; accessed [date, month, year].

Its own carve-out:

> Permission to copy, use, and distribute materials as described above shall not extend to
> information housed on this Website that is credited to other sources, or to information on
> Websites to which this site links.

**Do not read the umbrella terms as the curriculum grant.** They cover NYSED's own website
material, they say nothing about Creative Commons, and they permit less. The CC grant on the
curriculum is asserted by the retired EngageNY terms and by the live successor sentence, not by
this document.

### The per-resource marking, which is where the version is actually pinned

Five resource pages were opened, all HTTP 200, all Wayback snapshots, all this project's own
measurement:

| Resource page (snapshot) | Own licence notice | Standard as the host tags it |
|---|---|---|
| `/resource/geometry-module-2` (20220703) | CC BY-NC-SA 3.0 US badge plus link | G.SRT.1-8, G.MG.1 |
| `/resource/geometry-module-2-topic-d-lesson-21` (20220130) | CC BY-NC-SA 3.0 US | G.SRT.4 |
| `/resource/geometry-module-2-topic-e-lesson-25` (20220130) | CC BY-NC-SA 3.0 US | G.SRT.6 |
| `/resource/geometry-module-2-topic-e-lesson-34` (20220128) | CC BY-NC-SA 3.0 US | G.SRT.8 |
| `/resource/high-school-geometry` (20220514) | NONE, zero CC markings | course index |

Method, recorded because the negative result depends on it: the agent grepped raw HTML for
`creativecommons.org`, for the `i.creativecommons.org` badge image, and for the literal string
"Creative Commons". The high school Geometry index returned **0 matches on all three**, which the
report calls a verified negative rather than a parse artefact. See [[license-unmarked-silence]]
for what an unmarked page resolves to.

The badge on the marked pages links `i.creativecommons.org/l/by-nc-sa/3.0/us/80x15.png`. The
visible anchor beside it is misspelled `/licences/` in the British form, so the href itself 404s
at Creative Commons. **The badge image path is the reliable signal on these pages; the anchor is
broken.**

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state what standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | attribution block below; NonCommercial attaches; quoting does not trigger ShareAlike |
| Paraphrase and republish: rewrite its material and ship it | by the licence, yes | the derivative must ship under the same CC BY-NC-SA terms, which drags NonCommercial into whatever file it lands in. Ruling R9 forbids this for this repo outright |

Quoting is a use of the work, not an adaptation of it, so ShareAlike does not attach to a
quotation set inside your own prose with attribution. A close paraphrase that follows a specific
lesson's structure, numbers and pedagogical move is an adaptation however different the wording,
and that is the operation the rider bites on. See [[concept-cite-quote-adapt]].

### The attribution string this host mandates

Unlike most hosts in this corpus, EngageNY specified its own format rather than leaving one to be
constructed. Use the format above, filled in, and add the version pin:

```
From EngageNY.org of the New York State Education Department. [Name of article/document.]
Internet. Available from [specific webpage on EngageNY.org]; accessed [date, month, year].
Licensed under CC BY-NC-SA (see resource page badge: 3.0 US).
```

Worked example, as this project assembled it:

```
From EngageNY.org of the New York State Education Department. Geometry Module 2, Topic E,
Lesson 25. Internet. Available from
https://www.engageny.org/resource/geometry-module-2-topic-e-lesson-25 (archived at
https://web.archive.org/web/20220130113349/https://www.engageny.org/resource/geometry-module-2-topic-e-lesson-25);
accessed 8 August, 2026.
```

**Cite the archived URL, or cite the nysed.gov successor.** A bare `https://www.engageny.org/...`
link lands a reader on an expired certificate warning, and a bare `https://engageny.org/...` link
does not resolve at all. This is a mechanical constraint on citation, not a licence constraint.

### What the grant does not reach

- **Anything beyond the CC terms.** NYSED holds a licence and says so. It cannot grant you more
  than it has, and the party who could is named nowhere. See [[concept-chain-of-title]].
- **All images on EngageNY**, carved out by the archived terms. See
  [[concept-third-party-carve-out]].
- **Anything credited to other sources**, and anything on sites EngageNY links to.
- **Course index pages**, which carry no CC assertion at all and therefore fall to the default.

## Gotchas & constraints

**1. Four failure signatures, one status code.** NXDOMAIN on the apex and an expired certificate
on `www` both surface as `http_code=000` to a default HTTPS client. Neither means the content is
gone. The correct next moves differ: for the apex, use `www`; for `www`, drop to plain HTTP or
`curl -k` and follow the 301; for a citation, use the successor URL or an archive URL. Writing
"the source is unavailable" here would have cost this project a directly on-target module. See
[[trap-down-is-not-one-state]].

**2. The version is genuinely ambiguous and this page does not resolve it.** Site-wide statements
link 3.0 Unported. Per-resource badges pin 3.0 US. The staged deed extract for 3.0 Unported states
plainly that the ported US legal code is a different document at a different URL and is not staged
in this wiki, so a 3.0 US question cannot be answered from what is here. Resource-level markings
are more specific and this project treats them as pinning 3.0 US, but which instrument governs
where they conflict is **unverified**. What would close it: fetch the 3.0 US legal code and read
both against a specific reuse. See [[license-sharealike]] and [[license-noncommercial]].

**3. Do not label it 4.0.** Everything on this host and its successor points at a 3.0 instrument.
Silently upgrading a 3.0 label to 4.0 changes the legal text you are claiming to comply with.

**4. NYSED is not the copyright owner, and the owner is unnamed.** This is the single most
important rider on the host. Any use beyond the CC grant requires the express written permission
of parties this project could not identify. A grep across every fetched resource page for "Great
Minds", "Eureka" and "©" returned **zero hits on all three**, so the common folk attribution has
no support in the verified record and is not asserted here.

**5. The image carve-out's reach is unresolved.** The carve-out sits under the non-CC "Other
EngageNY materials" clause rather than literally under the CC curricular-documents clause. Whether
it reaches images inside CC-licensed module PDFs is genuinely ambiguous on the text. This
project's practical instruction is to treat module diagrams as not cleared. What would close it:
open a module PDF and read its own front matter.

**6. The successor archive bounced an anonymous non-JS client to Microsoft SSO, and that is not
the same as "gated".** NYSED points math files at a `nysed.sharepoint.com` sharing link. Anonymous
`curl -L` returned 302, then four redirects, then a final 200 at
`login.microsoftonline.com/.../oauth2/authorize`. curl executes no JavaScript, so whether a real
browser holding the sharing token gets in anonymously was **not determined**. The report records
this as ambiguous and so does this page. Access state is not a rights fact in either direction;
see [[trap-access-is-not-a-rights-fact]].

**7. No module PDF was ever opened.** Every licence fact on this page comes from web-page metadata
and terms pages. Per-document copyright pages inside the module PDFs were not inspected, and this
project names that as the highest-value remaining probe on this host, because those pages very
likely name the upstream owner and may carry notices differing from the web-page metadata.

**8. Sampling limit, stated plainly.** Five hand-picked resource pages, not a crawl. The Wayback
CDX API timed out twice at 60s, so the agent used the `available` endpoint instead. The uniformity
of the 3.0 US badge across four marked pages is evidence of a template, not proof of a per-page
decision.

**9. NonCommercial is dormant, not absent.** Nothing in this project is being sold, so the rider
binds nothing today. It becomes permanent the moment anything derived from this host enters a paid
workshop or a paid product. That is a property of the material, not of the current build.

## Related

- [[license-sharealike]] holds the SA rider this host carries, the version inventory behind it,
  and what the 3.0 legal code actually says.
- [[license-noncommercial]] holds the NC rider that travels with it and that the verdict token
  does not name.
- [[license-unmarked-silence]] is what the unmarked course index pages fall to, and why "no
  notice" is not "no owner".
- [[concept-chain-of-title]] is the general shape of the problem this host states outright: a
  publisher distributing under a licence it does not own.
- [[concept-third-party-carve-out]] is the images clause and the credited-to-other-sources clause.
- [[concept-attribution-per-record]] is why the credit line here is a property of the individual
  lesson page and its badge, not of the host.
- [[concept-cite-quote-adapt]] is the three-operation split the verdict table above applies.
- [[trap-down-is-not-one-state]] is the failure this host produced, and it is the reason this page
  leads with a probe table rather than a licence sentence.
- [[trap-sharealike-contaminates-by-paraphrase]] is the mechanism that makes this host quote-only
  under R9.
- [[trap-access-is-not-a-rights-fact]] covers the SharePoint SSO bounce and why an unopened door
  proves nothing about permission.
- [[trap-code-form-silent-zero]] is why `G.SRT.6` as this host writes it will not resolve against
  this project's store.
- [[trap-summary-layer-is-not-evidence]] is why the live NYSED sentence above was taken from raw
  HTML.
- [[source-im-task-bank]] is the other ShareAlike host in this corpus and carries the same
  quote-yes, adapt-no shape under R9.

## Composes with

- [[practice-assemble-an-attribution-block]] consumes the mandated format above, which is one of
  the few strings in this corpus the rights-holder published rather than leaving to be built.
- [[practice-cite-without-redistributing]] is the operation this host is actually good for, and
  the archive-URL rule above is a worked instance of its mechanics.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced the probe
  table above, including the step that turns a `000` into four distinguishable facts.

## References

Live and archived host pages, fetched by this project on 2026-08-08:

- `https://www.nysed.gov/standards-instruction/standards-resources-and-supports` HTTP 200. The
  live successor statement, confirmed from raw HTML; prose names no version, anchor href is
  `by-nc-sa/3.0/` Unported.
- `https://web.archive.org/web/20220618120326/https://www.engageny.org/terms-of-use` HTTP 200. The
  archived EngageNY Terms of Use: the CC grant on curricular documents, the not-the-copyright-owner
  sentence, the mandated attribution format, and the images carve-out.
- `https://www.nysed.gov/terms-of-use` HTTP 200. The umbrella terms, a separate and narrower grant
  that never mentions Creative Commons. `/terms-use` and `/about/terms-use` both 404, recorded as
  tried and failed.
- `https://web.archive.org/web/20220130113349/https://www.engageny.org/resource/geometry-module-2-topic-e-lesson-25`
  HTTP 200. Topic E Lesson 25, tagged G.SRT.6; the CC BY-NC-SA 3.0 US badge that contradicts the
  site-wide 3.0 Unported link, and the misspelled `/licences/` anchor.
- `https://creativecommons.org/licenses/by-nc-sa/3.0/` HTTP 200, fetched 2026-08-08, 37273 bytes.
  The deed those site-wide hrefs resolve to.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-engageny-nysed.md`, primary. The seven-probe reachability table, all verbatim
  licence text above, the five-page per-resource sample and its grep method, the SharePoint SSO
  bounce, the riders, and the eight carried-forward gaps.
- `sources/cc-by-nc-sa-3-0.md`, primary. The 3.0 Unported deed and legal code staged verbatim,
  including the statement that the ported US legal code is a different document and is not staged
  here.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 5, §2 the
  verdict key, §3 correction 11 on the unnamed copyright owner, §4.6 the attribution block, §6 the
  unopened module PDFs as the highest-value remaining probe.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-engageny.md`, the underlying fetch report.
- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 ruling R9, which fixes this
  host's operative use at quote-only regardless of what the licence permits.
