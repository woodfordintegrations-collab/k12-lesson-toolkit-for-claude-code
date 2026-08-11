---
title: "mathematicsvisionproject.org (ruled out under R11)"
type: source
verdict: quote_and_adapt
fetched: 2026-08-08
sources:
  - http://www.mathematicsvisionproject.org/geometry.html
  - http://www.mathematicsvisionproject.org/secondary-mathematics-ii.html
  - http://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/g1_mod4_se_82017f.pdf
  - https://creativecommons.org/licenses/by/4.0/
  - sources/host-math-vision-project.md
  - sources/cc-by-4-0.md
  - sources/verdict-twelve-host-table.md
  - Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md
updated: 2026-08-08
---

# mathematicsvisionproject.org (ruled out under R11)

## Summary

**Read the frontmatter verdict and the build ruling as two different things, because they are.**
`verdict: quote_and_adapt` is a rights finding about the Geometry route on this host, and it is
correct: `http://www.mathematicsvisionproject.org/geometry.html` and the Geometry module PDFs
themselves both state CC BY 4.0, with no ShareAlike and no NonCommercial. **Ruling R11 puts this
host out of the build anyway, on operational grounds, and the ruling is not about the licence.**
This page exists so that the ruling and its evidence stay legible rather than being re-derived as
a licensing problem it never was.

The operational grounds, and both halves of them are measured facts:

1. **`https://` fails host-wide with a TLS handshake failure.** Three independent TLS stacks fail
   identically. Plain `http://` returns HTTP 200 on every page and every PDF.
2. **The module PDFs are orphaned.** They are removed from site navigation and reachable only via
   `/sitemap.xml`. The nav-level site is now a redirect shell pointing at Open Up Resources.

| Probe, run by this project 2026-08-08 | Result |
|---|---|
| DNS, `www` and apex | 199.34.228.159 |
| WebFetch (BoringSSL) over `https://` | FAIL, `error:1000009a:...HANDSHAKE_FAILURE_ON_CLIENT_HELLO` |
| curl 8.7.1 / LibreSSL 3.3.6 over `https://` | FAIL, exit 35, `error:1404B410:SSL routines:ST_CONNECT:sslv3 alert handshake failure` |
| Python urllib / OpenSSL 3.6.3 over `https://` | FAIL, `[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE]` |
| **curl over plain `http://`** | **HTTP/1.1 200 OK on every page, every PDF** |

TCP port 443 connects, the client sends a Client Hello, and the server answers with a
handshake_failure alert. A control set run on the same machine, from the same egress, in the same
minute returned example.com 200, khanacademy.org 200, openupresources.org 301 and weebly.com 200.
This project's conclusion, quotable as this project's measurement: **not egress filtering, not a
bot block, not a dead site, but a host-specific edge TLS misconfiguration with no usable
certificate for this SNI.** Live headers over HTTP report `Server: cloudflare` and
`X-Host: blu49.sf2p.intern.weebly.net`.

**A public repository must not cite an `https://` MVP URL.** It will fail for every reader, on
every client, and it will read as a dead source rather than as a broken certificate on a live one.

## When to reach for it

Reach for this page when someone proposes MVP as a source, or when someone reads "MVP is out" and
starts looking for the licence defect that caused it. There isn't one on the Geometry route. Point
them at the two operational facts above and at R11.

Reach for it also to understand what R11 cost, which is worth stating precisely because the
replacement was mis-specified once already. R11's own text records the cost: MVP task 6.8 derives
the trig ratios from similar triangles and was the single best B.4-to-C.6 through-line this project
found. The design's stated replacement is IM Unit 4 L4 and IM task 1635, both described there as
CC BY 4.0 clean. **Task 1635 is not.** It lives on `tasks.illustrativemathematics.org`, which is
CC BY-NC-SA 4.0, so under ruling R9 it is quote-only and cannot carry an adapted through-line. The
clean adaptable through-line therefore rests on **IM Unit 4 L4 alone, on one host**. That is a
single-host dependency and it should be visible before the authoring phase rather than discovered
inside it. See [[source-im-task-bank]] and [[source-im-kendall-hunt]].

Do not reach for this host for material. Under R11 nothing here enters the build.

If a future ruling reopens R11, the entry point is the Geometry course, not Secondary Math II:
`Geometry: A Learning Cycle Approach`, Module 4, "Similarity and Right Triangle Trigonometry",
listed on `/geometry.html`, with the student edition at
`http://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/g1_mod4_se_82017f.pdf` (70pp)
and Teacher Notes at `g1_mod4_tn_82017f.pdf`. This project records Module 4 as the same tasks as
Secondary Math II Module 6 renumbered 4.x, and records that module's sequence as covering all five
target standards, with 6.8 "Are Relationships Predictable?" carrying the similarity-to-trig
derivation. Those standard tags are the host's own code forms; see [[trap-code-form-silent-zero]].

## What its own page says

Every quotation below was captured by a fetching agent on 2026-08-08 over plain HTTP and is staged
verbatim in `sources/host-math-vision-project.md`.

### There is no site-level licence page, and there never was one

`/terms`, `/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/licensing`, `/faq`,
`/legal` and `/privacy` all returned **404**. Wayback CDX over the full history of
`mathematicsvisionproject.org*` returns **zero** URLs matching `licen|terms|copyright|permission|faq|legal`.
The 11 nav-reachable pages contain zero licence or copyright language and there is no footer
copyright line.

The nav-level site is now a redirect shell. From `/resources.html` and `/curriculum.html`, HTTP
200, 2026-08-08:

> "Open Up Resources , the nonprofit provider of quality curriculum, is partnered with us to
> provide high quality mathematics curriculum for high schools and districts. You can now find the
> newest edition of the materials here . You will need to register and create an educator account
> to have access."

The spacing before punctuation is in the extracted text and is reproduced rather than corrected.

**The licence lives on the deep, unlinked curriculum pages reachable through `/sitemap.xml`, and
inside the PDFs themselves.** A clean, successful fetch of the obvious pages returns "unlicensed"
on this host, which is the same shape of failure another host in this corpus produced with a
different cause. See [[trap-license-lives-off-the-obvious-page]].

### `/geometry.html`, the clean route

HTTP 200, 2026-08-08:

> "This work is authored by Mathematics Vision Project and licensed by USOE and Learning
> Accelerator under a Creative Commons Attribution 4.0 International License . The Creative
> Commons license applies to the materials available on this page of the Mathematics Vision
> Project website."

Hyperlink on that page: `href="http://creativecommons.org/licenses/by/4.0/"`. Text and link agree.

### `/secondary-mathematics-ii.html`, the conflicted route

HTTP 200, 2026-08-08:

> "(c) 2013 Utah State Office of Education with materials authored by Mathematics Vision Project
> licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Unported License .
> The Creative Commons license applies to the materials available on this page of the Mathematics
> Vision Project website."

Hyperlink on that page: `href="http://creativecommons.org/licenses/by-nc-sa/3.0/"`.

Three things are wrong with that sentence at once, and each is independently checkable. Its text
says **4.0** while its link says **3.0**. "4.0 Unported" is not a real licence name: "Unported" is
3.0 vocabulary and 4.0 is "International". And it claims NonCommercial-ShareAlike over files whose
own covers and page footers say CC BY 4.0.

### Inside the module PDFs

Cover page, verbatim as extracted:

```
© 2017 Mathematics Vision Project
 Original work © 2013 in partnership with the Utah State Off ice of Education
 This work is licensed under the Creative Commons Attribution CC BY 4.0
```

"Off ice" is a `pdftotext` ligature artefact for "Office" and is left uncorrected here because
correcting a quotation is falsification.

Per-page footer, repeated on nearly every page:

```
Mathematics Vision Project
 Licensed under the Creative Commons Attribution CC BY 4.0
 mathematicsvisionproject.org
```

### Per-resource samples, each opened individually

All HTTP 200, 2026-08-08. Byte figures are the recorded Content-Length values, reproduced as
recorded:

| Resource | Bytes verified | Its own notice |
|---|---|---|
| `g1_mod4_se_82017f.pdf` (Geometry Mod 4 SE, 70pp) | 86,479,963 = Content-Length | CC BY 4.0 cover plus 68 footers |
| `m2_mod6_se_52017f.pdf` (Sec Math II Mod 6 SE, 69pp) | 86,508,076 = Content-Length | CC BY 4.0 cover plus 63 footers |
| `m2_mod6_tn_52017f.pdf` (Mod 6 Teacher Notes, 108pp) | 90,240,912 = Content-Length | CC BY 4.0 cover plus 97 footers |
| `m2_mod5_se_52017f.pdf` (Geometric Figures, SE) | 49,711,876 = Content-Length | CC BY 4.0 cover plus 60 footers |
| `m1_mod1_se_52016f.pdf` (Sec Math I Mod 1, 59pp) | 19,611,425 = Content-Length | CC BY 4.0 cover plus 56 footers |
| `ancillary_order_form2017.pdf` | 189,686 | **NO licence notice at all**, 0 matches |

Per-resource variation is present and it runs along a clean line: instructional modules carry
CC BY 4.0 uniformly, and administrative documents such as the order form carry nothing at all.
Silence in the order form is not a grant; see [[license-unmarked-silence]].

## What you may do with it

This table states the rights position on the **Geometry route only**. It is not a use permission
for this build, which R11 withholds.

| Operation | Permitted on the Geometry route | Condition |
|---|---|---|
| Cite: name it, link it, state what standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | attribution block below; cite an `http://` or archive URL |
| Paraphrase and republish: rewrite its material and ship it | yes | attribution block below, no copyleft attaches |

CC BY 4.0's deed carries both freedoms with the trailing clause "for any purpose, even
commercially", and its "Under the following terms" list has exactly two items, Attribution and No
additional restrictions. Neither ShareAlike nor NoDerivatives appears on it. See
[[license-cc-by]].

### The attribution block, which this project assembled because MVP publishes none

```
Geometry: A Learning Cycle Approach, Module 4 "Similarity and Right Triangle Trigonometry."
Mathematics Vision Project (Scott Hendrickson, Joleigh Honey, Barbara Kuehl, Travis Lemon,
Janet Sutorius). © 2017 Mathematics Vision Project. Original work © 2013 in partnership with
the Utah State Office of Education. Licensed by USOE and Learning Accelerator under a
Creative Commons Attribution 4.0 International License.
https://creativecommons.org/licenses/by/4.0/
http://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/g1_mod4_se_82017f.pdf
Accessed 2026-08-08. Changes were made.
```

Note the `http://` in the source URL and the `https://` in the licence link. The first is required
because MVP's TLS is broken; the second is required because the Creative Commons deed resolves
fine. Mixing them the other way breaks the citation.

**MVP is the author but not the sole rights-holder.** `/geometry.html` names USOE and Learning
Accelerator as the licensors, and the PDF cover names the Utah State Office of Education as the
partner on the original 2013 work. A credit line naming only Mathematics Vision Project drops
parties the host itself names. See [[concept-attribution-per-record]] and
[[concept-chain-of-title]].

### What the grant does not reach

- **The embedded Flickr photographs.** Each module interleaves separately-owned photographs
  credited inline under their own per-photographer CC BY grants. This project recorded credits
  including `CC BY the kirbster "Pythagorean Theorem"`, `CC BY Stuart Heath "tree shadow"`,
  `CC BY Official U.S. Navy Page` and several more, plus a bare Flickr URL. Reusing one requires
  attributing the photographer, not MVP. The safest posture, and this project's instruction:
  reproduce no photographs. See [[concept-third-party-carve-out]].
- **The MVP name and branding.** No trademark grant appears anywhere in these notices.
- **The Secondary Math II Module 6 files**, which are covered by a page that conflicts with them.
  See gotcha 2.
- **The "newest edition" on Open Up Resources**, which is behind educator registration, sits on a
  different host, and was not opened by anyone in this project.

## Gotchas & constraints

**1. A TLS handshake failure is not a bot block and not a dead host, and the correct next move is
different for each.** For a handshake failure the move is plain HTTP, or an archive. For a 406 it
is a browser user agent. For an expired certificate it is `curl -k` or plain HTTP and follow the
redirect. All three present as "the site is down" to an agent that records only the outcome. See
[[trap-down-is-not-one-state]].

**2. Two routes, one body of content, two incompatible licence claims.** The Secondary Math II
page claims CC BY-NC-SA over `m2_mod6_se_52017f.pdf` and `m2_mod6_tn_52017f.pdf`, and those very
files say CC BY 4.0 on their covers and in their page footers. This project did not average or
resolve the conflict; it recorded it. Its mitigating reading, marked at the time as **not a
ruling**: the in-file notice is more specific to the work, is dated 2017 against the page's
"(c) 2013", and repeats on every page, and the Math I page states expressly that the prior work's
licence "has been updated", so the NC-SA block reads as stale 2013-era text never refreshed.
**Which notice legally governs is unverified and is a question for counsel, not a fetch.** The
practical consequence is simple and it costs nothing: use `g1_mod4_*`, never `m2_mod6_*`, and the
conflict is moot.

**3. Two footer counts are in this project's record, and this page reproduces both without picking
one.** The twelve-host verdict table flags "68 of 70 pages" against "63-of-69 page footers" as an
unresolved numeric discrepancy inside its own source document. The staged per-resource table above
attributes 68 footers to `g1_mod4_se_82017f.pdf` at 70pp and 63 footers to `m2_mod6_se_52017f.pdf`
at 69pp, which are two different files with two different page counts. That reading is consistent
with every figure on record, but **no agent re-opened either PDF to confirm it**, and this page
does not assert the discrepancy closed. What would close it: re-read both files.

**4. The PDFs are orphaned from navigation, and their future availability is unverified.** They
are live and unauthenticated today, reachable through `/sitemap.xml`, and delinked from every nav
page. Whether MVP intends them to stay public is unknown. This project's instruction was to
archive them at the point of citation rather than rely on the path.

**5. `robots.txt` does not exclude the content.** It disallows `/ajax/` and `/apps/`, fully
disallows `NerdyBot`, and sets a crawl-delay of 10 for `dotbot`. `/uploads/` and the content pages
are not disallowed.

**6. The https failure was tested from one egress only.** Three independent TLS stacks failed
identically and a control set passed in the same minute, which makes a client-side cause unlikely,
but whether HTTPS works from another network is **unverified**. What would close it: test from a
second network.

**7. Do not read the frontmatter verdict as a use ruling, and do not read R11 as a licence
finding.** Collapsing an operational exclusion into a rights verdict is the specific error this
page exists to prevent, in both directions. On the rights axis this is one of the cleanest hosts
in the corpus. On the operational axis it is out.

## Related

- [[license-cc-by]] holds the plain-attribution regime the Geometry route grants under, including
  the changes-made component of the attribution obligation.
- [[license-sharealike]] and [[license-noncommercial]] hold the riders the Secondary Math II page
  claims, and are why that route is quarantined rather than merely untidy.
- [[license-unmarked-silence]] is what the unmarked order form falls to.
- [[trap-down-is-not-one-state]] is the failure signature this host contributes: a handshake
  failure with a clean same-minute control set.
- [[trap-license-lives-off-the-obvious-page]] is the discoverability failure here, where no licence
  page ever existed and the grant survives only on delinked deep pages and inside the files.
- [[trap-code-form-silent-zero]] is why MVP's `G.SRT.4` tag form will not resolve against this
  project's store.
- [[concept-third-party-carve-out]] is the embedded Flickr photographs, which sit outside the
  grant while inside the file.
- [[concept-chain-of-title]] and [[concept-attribution-per-record]] are why USOE and Learning
  Accelerator belong in the credit line.
- [[concept-cite-quote-adapt]] is the three-operation split the verdict table above applies.
- [[source-im-kendall-hunt]] is the host the B.4-to-C.6 through-line now rests on alone, and
  [[source-im-task-bank]] is the ShareAlike host that R11's stated replacement wrongly treated as
  clean.

## Composes with

- [[practice-assemble-an-attribution-block]] consumes the block above, and this host is its
  hardest case: a constructed string, multiple named licensors, and a scheme constraint on the
  source URL.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced the probe table
  and the control set, and it is what distinguishes a TLS failure from a death.

## References

Host pages and files, fetched by this project on 2026-08-08 over plain HTTP:

- `http://www.mathematicsvisionproject.org/geometry.html` HTTP 200. The clean route's licence
  statement, `href` to `by/4.0/`, naming USOE and Learning Accelerator as licensors.
- `http://www.mathematicsvisionproject.org/secondary-mathematics-ii.html` HTTP 200. The conflicted
  route: CC BY-NC-SA claimed in prose reading "4.0 Unported", against an `href` of
  `by-nc-sa/3.0`.
- `http://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/g1_mod4_se_82017f.pdf`
  HTTP 200, 86,479,963 bytes as recorded, 70pp. Geometry Module 4 "Similarity and Right Triangle
  Trigonometry"; CC BY 4.0 on the cover and in 68 page footers; reachable only via `/sitemap.xml`;
  embeds separately-licensed Flickr photographs credited inline.
- `https://creativecommons.org/licenses/by/4.0/` HTTP 200, fetched 2026-08-08, 32178 bytes. The
  deed behind the attribution obligation above.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-math-vision-project.md`, primary. The four-probe TLS table and its control set, the
  no-licence-page finding, all verbatim licence statements above, the six-file per-resource table,
  the Flickr credit list, the Module 6 task sequence, and the five carried-forward gaps.
- `sources/cc-by-4-0.md`, primary. The CC BY 4.0 deed and legal code staged verbatim, including the
  measurement that ShareAlike and NoDerivatives appear zero times in the deed's terms list.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: row 2 and its
  flagged numeric discrepancy, §3 correction 9, §4.7 the attribution block, and §6 the untested
  second egress.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-mvp.md`, the underlying fetch report.
- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 ruling R11 and the paragraph
  recording what it costs, and §2 ruling R9, which is why task 1635 cannot stand in for MVP 6.8.
