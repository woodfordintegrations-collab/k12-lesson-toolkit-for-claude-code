---
source_url: hs-geometry-similarity-trig/sources/license-engageny.md
fetched: 2026-08-08
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-engageny-nysed, trap-down-is-not-one-state, trap-sharealike-contaminates-by-paraphrase, license-sharealike, license-noncommercial, concept-chain-of-title, concept-third-party-carve-out, practice-assemble-an-attribution-block, source-achieve-the-core-sap
---

# EngageNY / NYSED (engageny.org, www.engageny.org, nysed.gov)

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every fetch recorded below was performed by the verifying agent on
**2026-08-08** (probes 01:45Z to 02:05Z), which is the date the report states applies to all
of its claims. Verbatim quotations were captured by that agent from the URLs named against
each one. Where the report marks a fact unverified, this extract keeps it unverified.

The report's own framing of the sourcing model: curate-and-cite, stated as "citing is not
redistributing". The unit it was working against: HSG-SRT.B.4, B.5, C.6, C.7, C.8, similarity
and right-triangle trigonometry, grades 9 to 10.

---

## 1. Reachability: five distinct facts, and they must not be collapsed

The prior finding handed to the verifying agent was "HTTP 000, does not resolve." The report
records this as **partially confirmed, with the reason overturning the conclusion**. HTTP 000
is real, but the site is not dead.

| Probe | Result |
|---|---|
| `dig +short engageny.org A` | empty; apex does NOT resolve (NXDOMAIN) |
| `dig +short www.engageny.org A` | CNAME to `sedldbal.nysed.gov.` then 149.10.125.41, .40 |
| `curl https://engageny.org/` | `curl: (6) Could not resolve host`, http_code=000 |
| `curl https://www.engageny.org/` | `curl: (60) SSL certificate problem: certificate has expired`, http_code=000 |
| `curl -k https://www.engageny.org/` | **301** to `http://www.nysed.gov/curriculum-instruction/engageny` |
| `curl http://www.engageny.org/` | **301** to the same target |
| `curl -L http://www.engageny.org/` | **200**, 3 redirects, final `https://www.nysed.gov/standards-instruction/standards-resources-and-supports#engageny` |

Report's stated root cause of the 000: an expired TLS certificate on `www`, plus a dead apex.
Any default HTTPS fetcher fails closed and reports 000. Over plain HTTP the host answers
immediately and 301s into NYSED.

Report's verdict, in its own emphasis: **not dead, not bot-blocked. It is a live redirector
with a broken cert.** Nameservers include `srv21.nysed.gov`, so NYSED still controls the
domain; it was not abandoned or squatted.

Schema classification the report assigned: `partial`. Apex dead, www alive but TLS-broken,
content relocated and reachable at the successor.

## 2. Successor host

**nysed.gov** (New York State Education Department).
Live landing: `https://www.nysed.gov/standards-instruction/standards-resources-and-supports#engageny`, HTTP 200.
EngageNY.org support discontinued **July 7, 2022**.

## 3. Verbatim licence evidence

### 3a. Live successor, NYSED. Fetched 2026-08-08, HTTP 200

URL: `https://www.nysed.gov/standards-instruction/standards-resources-and-supports`
The report states this was confirmed from RAW HTML, not from a model summary.

> "The New York State Education Department discontinued support for the EngageNY.org
> website on July 7, 2022. The NYSED encourages educators to download any EngageNY
> content they wish to use in the future from our archive sites below. All ELA and
> mathematics curriculum files will be available at the links below, and will remain
> free and licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
> (CC BY-NC-SA) license."

The prose names NO version. The anchor href is `https://creativecommons.org/licenses/by-nc-sa/3.0/`,
which is **3.0 UNPORTED**.

### 3b. Archived EngageNY Terms of Use. Snapshot 2022-06-18, fetched 2026-08-08, HTTP 200

URL: `https://web.archive.org/web/20220618120326/https://www.engageny.org/terms-of-use`

> "The curricular documents and videos provided on EngageNY, including all materials
> linked from the curriculum page and the video library, are licensed under the Creative
> Commons Attribution Non-Commercial Share-Alike license and are subject to the copyright
> rules under that license. All documents posted on EngageNY that are subject to the
> Creative Commons Attribution Non-Commercial Share-Alike license are identified using
> this icon:"

> "Commercial use of the curricular materials is not allowed under this license.
> Furthermore, NYSED is not the copyright owner of the curricular materials but rather
> NYSED holds a license to use the materials. As such, any use of the curricular materials
> beyond those allowed under the Creative Commons license would require the express
> written permission of the copyright owners."

(The report bolds "NYSED is not the copyright owner ... would require the express written
permission of the copyright owners." Emphasis is the report's, not the source's.)

> "Except as expressly provided to the contrary for any specific document(s) or material(s)
> published on EngageNY.org, permission to copy, use, and distribute materials created by
> and/or credited to EngageNY.org or the New York State Education Department (NYSED) and
> contained on EngageNY.org is hereby granted without fee for personal, private, and
> educational purposes. Generally, reproducing materials for profit or any commercial use
> is strictly forbidden."

Required attribution string, verbatim:

> "From EngageNY.org of the New York State Education Department. [Name of article/document.]
> Internet. Available from [specific webpage on EngageNY.org]; accessed [date, month, year]."

Carve-out, verbatim:

> "Permission to copy, use, and distribute materials as described above shall not extend
> to the following:  All images on EngageNY / Information housed on EngageNY.org that is
> credited to other sources / Information on websites to which this site links"

Link href on this page: `creativecommons.org/licenses/by-nc-sa/3.0/`, which is **3.0 UNPORTED**.

### 3c. NYSED umbrella Terms of Use. Fetched 2026-08-08, HTTP 200

URL: `https://www.nysed.gov/terms-of-use`
Recorded as tried and failed: `/terms-use` and `/about/terms-use` both **404**.

The report states this page never mentions Creative Commons. It is a separate, narrower grant.

> "Except as expressly provided to the contrary on any individual document(s) or material(s)
> published on the New York State Education Department Website, permission to copy, use, and
> distribute materials created by and/or credited to the New York State Education Department
> and contained on the New York State Education Department Website is hereby granted without
> fee for personal, private and educational purposes, except that reproducing materials for
> profit or any commercial use is strictly forbidden without express prior written permission
> of the New York State Education Department. Requests for permission should be sent to
> legal@nysed.gov."

> "From the New York State Education Department. [Name of article/document.] Internet.
> Available from [specific webpage on State Education Department Website]; accessed
> [date, month, year]."

> "Permission to copy, use, and distribute materials as described above shall not extend to
> information housed on this Website that is credited to other sources, or to information on
> Websites to which this site links."

## 4. Per-resource sampling: 5 pages opened, and the marking varies

| Resource page (Wayback snapshot) | HTTP | Own licence notice | Standard |
|---|---|---|---|
| `/resource/geometry-module-2` (20220703) | 200 | CC BY-NC-SA 3.0 US badge plus link | G.SRT.1-8, G.MG.1 |
| `/resource/geometry-module-2-topic-d-lesson-21` (20220130) | 200 | CC BY-NC-SA 3.0 US | G.SRT.4 |
| `/resource/geometry-module-2-topic-e-lesson-25` (20220130) | 200 | CC BY-NC-SA 3.0 US | G.SRT.6 |
| `/resource/geometry-module-2-topic-e-lesson-34` (20220128) | 200 | CC BY-NC-SA 3.0 US | G.SRT.8 |
| `/resource/high-school-geometry` (20220514) | 200 | NONE, zero CC markings | (course index) |

Method recorded: grepped raw HTML for `creativecommons.org`, the `i.creativecommons.org` badge
img, and the literal "Creative Commons". HS-Geometry returned **0 matches on all three**,
which the report calls a verified negative, not a parse artifact.

Two variations the report found:

1. **Container and index pages carry no CC notice**; individual modules and lessons do. The CC
   field is per-resource Drupal metadata, so it is only asserted where populated.
2. **Version discrepancy.** Site-wide statements (both the 2022 terms and the live NYSED page)
   link **3.0 unported**. Every per-resource badge links **3.0 US (ported)** at
   `i.creativecommons.org/l/by-nc-sa/3.0/us/80x15.png`. The report states these are different
   legal instruments and that resource-level markings are more specific and pin 3.0 US. Minor
   defect noted by the report: the resource-page anchor is misspelled `/licences/` (British
   spelling) so the href itself 404s at CC; the badge IMAGE path is the reliable signal.

## 5. The successor archive is behind a login wall

NYSED points math files at:
`https://nysed.sharepoint.com/:f:/s/P12EngageNY-Math-EXTA/En7SIs8H6v5PlQbP8fYWQbkBvFl7pdadxm5WQe2RYn6C_Q?e=aA13JQ`

Anonymous `curl -L`: 302, then 4 redirects, then **final 200 at
`login.microsoftonline.com/.../oauth2/authorize`**. The report's framing: the material NYSED
calls "free" is, to an anonymous non-JS client, gated behind Microsoft SSO.

Caveat recorded by the report, and it must travel with the fact: curl executes no JS, so the
agent could not tell whether a real browser with the sharing token gets in anonymously.
**Reported as ambiguous, NOT as "gated".**

## 6. Riders, as the report enumerates them

1. **NonCommercial.** Bars commercial use. The report notes nothing was being sold in that
   project, so it treated the rider as not binding there.
2. **ShareAlike.** Binds derivative works. The report's reading: paraphrase-and-republish of
   module prose could trigger it; original expression plus citation does not.
3. **Attribution.** A specific string is mandated (section 3b above).
4. **NYSED IS NOT THE COPYRIGHT OWNER.** The report calls this the single most important
   rider. NYSED holds only a licence. Anything beyond the CC grant needs the upstream owner's
   written permission, and NYSED does not name that owner anywhere the agent fetched.
5. **All images carved out** of the "Other EngageNY materials" grant. The report is precise
   about placement: this carve-out sits under the non-CC "Other EngageNY materials" clause,
   not literally under the CC curricular-documents clause. Its reach over images inside
   CC-licensed module PDFs is called genuinely ambiguous. The report's practical instruction:
   treat module diagrams as not-cleared.
6. **Third-party-credited content carved out**, as is anything on linked sites.
7. **Version ambiguity, 3.0 unported versus 3.0 US** (section 4).
8. Resource pages carry: "Resources may contain links to sites external to EngageNY.org ...
   and in such cases NYSED is not responsible for its content."

## 7. Relevance to the unit

Geometry Module 2 is titled "Similarity, Proof, and Trigonometry." Module-level CCLS tags are
G.SRT.1 through G.SRT.8 plus G.MG.1, which are New York's labels for the target cluster.

Topic structure, from the Geometry course index page:

- Topic A Scale Drawings (L1-5), Topic B Dilations (L6-11), Topic C Similarity and Dilations (L12-20)
- Topic D "Applying Similarity to Right Triangles" (L21-24), mapping to B.4 and B.5
- Topic E "Trigonometry" (L25-34), mapping to C.6, C.7, C.8

Verified standard-to-lesson anchors recorded by the report:

- L21 to G.SRT.4, "Prove theorems about triangles..." (equals HSG-SRT.B.4)
- L25 to G.SRT.6, "Understand that by similarity, side..." (equals HSG-SRT.C.6)
- L34 to G.SRT.8, "Use trigonometric ratios and the Pythagorean Theorem to solve right
  triangles in applied problems.★" (equals HSG-SRT.C.8)

Each lesson ships a Teacher Version and a Student Version PDF; the module ships full zips
including Spanish and Chinese translations.

## 8. Unverified, carried forward as gaps

The report lists these explicitly and they are not findings.

- **The identity of the actual copyright owner.** The terms say it is not NYSED. The agent
  grepped all fetched resource pages for "Great Minds", "Eureka", and "©": **zero hits**. The
  widely repeated folk attribution to Great Minds / Eureka Math is not confirmed by anything
  fetched, so the report does not assert it.
- Whether 3.0 unported or 3.0 US governs where they conflict.
- Whether the image carve-out reaches images inside CC-licensed module PDFs.
- Whether the SharePoint archive is anonymously openable in a real browser.
- No module PDF itself was opened. Per-document copyright pages inside the PDFs were not
  inspected and may name the owner.
- The Wayback CDX API timed out twice at 60s, so the agent used the `available` endpoint
  instead. The sample is 5 hand-picked pages, not an exhaustive crawl.
