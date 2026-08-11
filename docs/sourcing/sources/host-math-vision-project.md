---
source_url: hs-geometry-similarity-trig/sources/license-mvp.md
fetched: 2026-08-08
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-math-vision-project, trap-down-is-not-one-state, trap-license-lives-off-the-obvious-page, license-cc-by, license-sharealike, license-noncommercial, concept-third-party-carve-out, practice-assemble-an-attribution-block
---

# mathematicsvisionproject.org (Mathematics Vision Project, MVP)

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every probe recorded below was performed by the verifying agent on
**2026-08-08 UTC**, between 01:45 and 02:05 UTC.

Scratchpad hygiene note the report records: the shared scratchpad root was contaminated by
other agents (`p-terms.html`, `p-bogus.html`, `p-privacy-policy.html` were not that agent's;
its own path probes wrote to /dev/null). All findings were re-run in an isolated directory
`mvp-only/`.

---

## 1. Reachability: the prior "unreachable" was wrong; the TLS half was right

| Probe | Result |
|---|---|
| DNS www and apex | 199.34.228.159 |
| WebFetch (BoringSSL) https:// | FAIL `error:1000009a:...HANDSHAKE_FAILURE_ON_CLIENT_HELLO` |
| curl 8.7.1 / LibreSSL 3.3.6 https:// | FAIL exit 35 `error:1404B410:SSL routines:ST_CONNECT:sslv3 alert handshake failure` |
| Python urllib / OpenSSL 3.6.3 https:// | FAIL `[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE]` |
| **curl http:// (plain)** | **HTTP/1.1 200 OK on every page, every PDF** |

TCP port 443 connects (`* Connected to ... port 443`), then the server returns a
handshake_failure alert to the Client Hello. Three independent TLS stacks fail identically.

Control test recorded, same machine, same egress, same minute: example.com 200,
khanacademy.org 200, openupresources.org 301, **weebly.com 200**. Report's conclusion: not
egress filtering, not a bot block, not a dead site. It is a **host-specific edge TLS
misconfiguration**, with no usable cert for this SNI.

Live headers over HTTP:

```
HTTP/1.1 200 OK
Date: Sat, 08 Aug 2026 01:46:12 GMT
Server: cloudflare
CF-Ray: a27ad895cf6dad84-SJC
X-Host: blu49.sf2p.intern.weebly.net
```

Schema classification the report assigned: `partial`. Content fully live and readable over
`http://`; `https://` is broken for every client. The report's instruction: a public repo must
not cite an `https://` MVP URL.

## 2. Site-level licence: there is none

No `/terms`, `/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/licensing`, `/faq`,
`/legal`, `/privacy`. All **404**.

Wayback CDX over the full history of `mathematicsvisionproject.org*` returns **zero** URLs
matching `licen|terms|copyright|permission|faq|legal`. The report's reading: no such page ever
existed.

The 11 nav-reachable pages (index, curriculum, about, resources, store, mvp-team,
professional-learning, contact-us, curriculum-beta, mvp-overview-presentation,
past-presentations) contain **zero** licence or copyright language. No footer copyright line.

The nav-level site is now a redirect shell to Open Up Resources. Verbatim, from
`/resources.html` and `/curriculum.html`, HTTP 200, 2026-08-08:

> "Open Up Resources , the nonprofit provider of quality curriculum, is partnered with us
> to provide high quality mathematics curriculum for high schools and districts. You can
> now find the newest edition of the materials here . You will need to register and create
> an educator account to have access."

The report's headline on discoverability: the licence lives on the deep, unlinked curriculum
pages found via `/sitemap.xml`, and inside the PDFs themselves.

## 3. Verbatim licence statements, deep pages, all HTTP 200, 2026-08-08

### 3a. `/secondary-mathematics-ii.html`, the page that serves the target module

> "(c) 2013 Utah State Office of Education with materials authored by Mathematics Vision
> Project licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
> Unported License . The Creative Commons license applies to the materials available on
> this page of the Mathematics Vision Project website."

Hyperlink on that page: `href="http://creativecommons.org/licenses/by-nc-sa/3.0/"`.

The report's observation: the page's own TEXT says 4.0, its own LINK says 3.0. "4.0 Unported"
is not a real licence name, because "Unported" is 3.0 vocabulary and 4.0 is "International".
The report calls the page internally incoherent.

### 3b. `/secondary-mathematics-i.html`

> "Secondary Mathematics One: An Integrated Approach by Mathematics Vision Project is
> licensed under a Creative Commons Attribution 4.0 International License . This work is
> based upon a previous work authored by Mathematics Vision Project in cooperation with
> the Utah State Office of Education (c) 2012. The License of the prior work has been
> updated and is the same as the license for this latest revised edition. The Creative
> Commons license applies to the materials available on this page of the Mathematics
> Vision Project website."

Hyperlink: `href="http://creativecommons.org/licenses/by/4.0/"`.

### 3c. `/geometry.html`, the traditional Geometry course, which the report calls the clean path

> "This work is authored by Mathematics Vision Project and licensed by USOE and Learning
> Accelerator under a Creative Commons Attribution 4.0 International License . The Creative
> Commons license applies to the materials available on this page of the Mathematics Vision
> Project website."

Hyperlink: `href="http://creativecommons.org/licenses/by/4.0/"`.

### 3d. Inside every module PDF, on the cover page and in a repeated per-page footer

Cover:

```
© 2017 Mathematics Vision Project
 Original work © 2013 in partnership with the Utah State Off ice of Education
 This work is licensed under the Creative Commons Attribution CC BY 4.0
```

The report annotates: "Off ice" is a pdftotext ligature artifact for "Office".

Per-page footer, repeated on nearly every page:

```
Mathematics Vision Project
 Licensed under the Creative Commons Attribution CC BY 4.0
 mathematicsvisionproject.org
```

## 4. The conflict, which the report calls the headline finding

`/secondary-mathematics-ii.html` claims **BY-NC-SA** over its materials, and directly links
`m2_mod6_se_52017f.pdf` and `m2_mod6_tn_52017f.pdf`. Those very files say **CC BY 4.0** on
their cover and in 63 of 69 and 97 of 108 page footers respectively.

The report's statement: the same file family is claimed under two incompatible licences by the
same publisher. Not averaged, not resolved there, reported as the finding.

Mitigating reading the report gives, explicitly marked NOT a ruling: the in-file notice is
(a) more specific to the work, (b) dated 2017 versus the page's "(c) 2013", and (c) repeated on
every page. The Math I and Geometry pages both settled on plain CC BY 4.0, and the Math I page
explicitly says the prior work's licence "has been updated." The NC-SA text on the Math II page
reads to the agent as a stale 2013-era block that was never refreshed.

Practical consequence the report draws: avoid the Secondary Math II Module 6 route. Use the
Geometry course Module 4 route, which is the same content under an unconflicted CC BY 4.0.

## 5. Per-resource samples, each opened individually

| Resource | HTTP | Bytes verified | Its own notice |
|---|---|---|---|
| `m2_mod6_se_52017f.pdf` (Sec Math II Mod 6 SE, 69pp) | 200 | 86,508,076 = Content-Length | CC BY 4.0 cover plus 63 footers |
| `m2_mod6_tn_52017f.pdf` (Mod 6 Teacher Notes, 108pp) | 200 | 90,240,912 = Content-Length | CC BY 4.0 cover plus 97 footers |
| `g1_mod4_se_82017f.pdf` (Geometry Mod 4 SE, 70pp) | 200 | 86,479,963 = Content-Length | CC BY 4.0 cover plus 68 footers |
| `m2_mod5_se_52017f.pdf` (Geometric Figures, SE) | 200 | 49,711,876 = Content-Length | CC BY 4.0 cover plus 60 footers |
| `m1_mod1_se_52016f.pdf` (Sec Math I Mod 1, 59pp) | 200 | 19,611,425 = Content-Length | CC BY 4.0 cover plus 56 footers |
| `ancillary_order_form2017.pdf` | 200 | 189,686 | **NO licence notice at all** (0 matches) |

Report's conclusion: per-resource variation IS present. Instructional modules carry CC BY 4.0
uniformly; administrative documents such as the order form carry nothing.

## 6. Riders, as the report enumerates them

1. **Third-party photographs embedded with individual CC BY credits.** Each module interleaves
   Flickr-sourced photos credited inline. In `m2_mod6_se` the report records:
   `CC BY the kirbster "Pythagorean Theorem"`, `CC BY Stuart Heath "tree shadow"`,
   `CC BY Jorge Jaramillo "depth . . ."`, `CC BY Jacque Davis "origami birds"`,
   `CC BY Official U.S. Navy Page`, `CC BY Lidyanne Aquino`, `CC BY Andi Saleh`,
   `CC BY Hammad Kahn`, `CC BY Barkbud`, `CC BY pbemjestes`, and a bare flickr URL
   `https://www.flickr.com/photos/mypubliclands/14937644058`.
   These are separately-owned images under their own CC BY grants. Reusing a page image
   requires attributing the photographer, not MVP. The report's safest posture: do not
   reproduce the photos.
2. **ShareAlike plus NonCommercial** attach if the Secondary Math II page notice governs (see
   section 4). That would constrain paraphrase-and-republish. Avoided by using Geometry Mod 4.
3. **Attribution string for CC BY 4.0**, as the report constructs it: credit "Mathematics
   Vision Project", the authors (Scott Hendrickson, Joleigh Honey, Barbara Kuehl, Travis Lemon,
   Janet Sutorius), the © year (2017), and note the original work © 2013 in partnership with
   the Utah State Office of Education. `/geometry.html` adds "licensed by USOE and Learning
   Accelerator".
4. **Third-party co-licensors named.** Utah State Office of Education (USOE) and Learning
   Accelerator are named as licensors on the Geometry page. MVP is the author but not the sole
   rights-holder.
5. **No trademark grant anywhere.** "Mathematics Vision Project" and "MVP" branding is not
   licensed by these notices.
6. **robots.txt**: `Disallow: /ajax/`, `/apps/`; `NerdyBot` fully disallowed; `dotbot`
   crawl-delay 10. `/uploads/` and content pages are NOT disallowed.

## 7. Relevance to HSG-SRT.B.4, B.5, C.6, C.7, C.8: the report calls it very high, with two routes

**Preferred, clean CC BY 4.0: Geometry: A Learning Cycle Approach, Module 4, "Similarity and
Right Triangle Trigonometry".**
`http://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/g1_mod4_se_82017f.pdf`
(SE, 70pp) and `g1_mod4_tn_82017f.pdf` (Teacher Notes, 90,847,857 bytes). Honors variants
`g1_mod6h_*` also exist. Listed on `/geometry.html`, which states CC BY 4.0 International.

**Same content, conflicted page: Secondary Math II Module 6.** `m2_mod6_se_52017f.pdf`,
`m2_mod6_tn_52017f.pdf`, plus a Spanish edition `m2_mod6_se_1_2018span.pdf`.

Task sequence, from the Module 6 table of contents. The report states Geometry Mod 4 is the
same tasks renumbered 4.x:

- 6.1 Photocopy Faux Pas, essential features of a dilation (G.SRT.1)
- 6.2 Triangle Dilations, proportionality in similar triangles (G.SRT.2, **G.SRT.4**)
- 6.3 Similar Triangles and Other Figures, definitions of similarity (G.SRT.2, G.SRT.3)
- 6.4 Cut by a Transversal, proportional segments, parallel lines (**G.SRT.4**)
- 6.5 Measured Reasoning, theorems on lines, angles, proportion (G.CO.9, G.CO.10, **G.SRT.4, G.SRT.5**)
- 6.6 Yard Work in Segments, partitioning a segment in a ratio (G.GPE.6)
- 6.7 Pythagoras by Proportions, similar triangles to prove the Pythagorean theorem plus geometric means (**G.SRT.4, G.SRT.5**)
- 6.8 Are Relationships Predictable?, right-triangle trig from similarity (**G.SRT.6, G.SRT.8**)
- 6.9 Relationships with Meaning, sine and cosine relationship, Pythagorean identity (**G.SRT.6, G.SRT.7**, F.TF.8)
- 6.10 Finding the Value of a Relationship, solving for unknowns with trig ratios (**G.SRT.7, G.SRT.8**)
- 6.11 Solving Right Triangles Using Trigonometric Relationships, real-world modeling (**G.SRT.6, G.SRT.7**, F.TF.8)

Report's summary: every one of B.4, B.5, C.6, C.7, C.8 is explicitly covered, with C.6
developed from similarity in 6.8. Teacher Notes editions give the pedagogical rationale.
Homework is the "READY, SET, GO" structure. Also adjacent: `/secondary-mathematics-ii.html`
Mod 5 (Geometric Figures) for proof groundwork, and `core_align_geometry.pdf` for standards
correlation.

## 8. Unverified and open, carried forward as gaps

- Which notice legally governs the Sec Math II Module 6 files, the page NC-SA or the in-file
  CC BY. Recorded as not resolvable from published text; would need MVP to confirm.
- The "newest edition" on Open Up Resources is behind educator registration and was NOT opened.
  The report gives its reasons: different host, out of that agent's scope, and registration
  would be a credential step.
- Whether MVP intends the `/uploads/` PDFs to remain public now that nav links are removed.
  They are live and unauthenticated today, but unlinked from nav.
- Whether the CC BY 4.0 in-file notice covers the embedded third-party photos. The report's
  own judgment, marked as such: almost certainly not, since they carry their own credits.
- Whether HTTPS works from other networks. The agent could only test from one egress, though it
  notes three TLS stacks and a clean control set make a client-side cause unlikely.
