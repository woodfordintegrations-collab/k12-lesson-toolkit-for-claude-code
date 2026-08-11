---
source_url: hs-geometry-similarity-trig/sources/license-mars-map.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-mars-map, license-noderivatives, license-sharealike, license-all-rights-reserved, license-unmarked-silence, concept-cite-quote-adapt, concept-third-party-carve-out, concept-curate-and-cite, practice-cite-without-redistributing, trap-sharealike-contaminates-by-paraphrase, trap-font-notice-is-not-a-content-license
---

# Host extract: map.mathshell.org (MARS / Mathematics Assessment Project)

**Original fetch date recorded by the evidence file: 2026-08-08 (UTC)**, stated as covering
every claim, with the server date header confirmed as `Sat, 08 Aug 2026`. The `fetched:` field
above is the staging date.

The evidence file states: "Every claim below is backed by a fetch performed in this session.
Nothing here is from training knowledge."

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Reachability, as recorded

- `https://map.mathshell.org/` returns HTTP **301** to `https://www.map.mathshell.org/`, which
  returns HTTP **200**. The 301 fires with both plain curl and a browser user agent, recorded
  as a canonical-host redirect and explicitly **not** a bot block. No 403, no 406, no TLS error
  anywhere.
- Default-UA WebFetch also succeeded (200). The site does not gate on user agent.
- Server: `Apache/2.4.58 (Ubuntu)`. Sets a `PHPSESSID` cookie.

Recorded partial failures, each a distinct mode, preserved separately:

- `stds.php?standardid=1400&collection=9`: `curl (28)` connection timed out after 60s.
- `POST /stds.php` (collection filter): `curl (28)` timed out after 45s.
- `download.php?fileid=1754` (2.7 MB PDF): took approximately 130 s at approximately 21 KB/s;
  a first attempt at 45 s timed out mid-transfer. The server does **not** support byte ranges
  (`curl (33)`), so no resume.
- Plain page loads re-tested 3 times immediately after: 301 in 0.49 to 0.59 s each. Base site
  fine.

Recorded characterisation: "live, with an intermittently slow DB-backed query layer."

Recorded currency signal: content is frozen, the footer copyright range ends 2015 and the newest
PDF stamps are © 2015.

## 2. Probed license-page paths, all 404

All with browser UA and `-L`:

| path | status |
|---|---|
| /terms | 404 |
| /terms-of-use | 404 |
| /terms.php | 404 |
| /copyright | 404 |
| /copyright.php | 404 |
| /permissions | 404 |
| /permissions.php | 404 |
| /license | 404 |
| /license.php | 404 |
| /licence | 404 |
| /about | 404 |
| /faq | 404 |
| /faq.php | 404 |
| /legal | 404 |

The About page is `/background.php` (200) and carries no terms text, only the global footer.

## 3. Verbatim license statements

### 3a. Homepage sidebox "Free to Schools"

URL: `https://map.mathshell.org/` (301 to `https://www.map.mathshell.org/`), **HTTP 200**,
2026-08-08.

> All our materials can be downloaded for free and may be reproduced as-is for
> non-commercial use. Precise terms vary between materials. Enquiries to:
> map.info@mathshell.org.

### 3b. Global footer, present on every page tested

URL: `https://map.mathshell.org/`, **HTTP 200**, 2026-08-08.

> State, district and CCSSI standards appear courtesy of their respective
> authors. All other material Copyright © 2007-2015 Mathematics
> Assessment Resource Service, University of Nottingham.

Recorded reading: a bare copyright assertion, not a grant. The first sentence is a third-party
carve-out for the CCSS standards text reproduced inside the materials.

### 3c. Classroom Challenges (formative assessment lessons), per-lesson-page sidebox

URLs, all **HTTP 200**, 2026-08-08: `.../lessons.php?unit=9320&collection=8`, `?unit=9305`,
`?unit=9325`, `?unit=8320`, `.../lessons.php?taskid=696`.

> The *Classroom Challenges* materials may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

Href on the link text: `http://creativecommons.org/licenses/by-nc-nd/3.0/`. No jurisdiction
code, so **Unported**. The link is plain `http://`. Recorded as byte-identical on all 5 lesson
pages checked.

### 3d. Summative Assessment Tasks, per-task-page sidebox

URLs, all **HTTP 200**, 2026-08-08: `.../tasks.php?unit=HA05&collection=9`, `?unit=HE04`,
`?unit=HA13`, `?unit=HE09`.

> The *Summative Assessment Tasks* may be copied and distributed, unmodified, under the
> [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0]. All other rights
> reserved. Please send any enquiries about commercial use or derived works
> to map.info@mathshell.org.

Same href `http://creativecommons.org/licenses/by-nc-nd/3.0/`. Recorded as byte-identical across
all 4.

### 3e. Prototype Tests page, same grant, different phrasing

URL: `https://map.mathshell.org/tests.php`, **HTTP 200**, 2026-08-08.

> The Summative Assessment Tasks may be distributed, unmodified,
> under the [Creative Commons Attribution, Non-commercial, No Derivatives License 3.0].
> All other rights reserved. Please send any enquiries about commercial
> use or derived works to map.info@mathshell.org.
>
> **Note:** please bear in mind that these prototype materials need some further trialing
> before inclusion in a high-stakes test.

Recorded difference: this wording says "distributed" only, dropping "copied". Same license URL.

### 3f. PD Modules, a different license (ShareAlike, not NoDerivatives)

URL: `https://map.mathshell.org/pd.php`, **HTTP 200**, 2026-08-08.

> The Professional Development Modules may be distributed under the
> [Creative Commons Attribution Noncommercial Share-Alike license]. Please
> send any enquiries about commercial use to map.info@mathshell.org.

Href: `http://creativecommons.org/licenses/by-nc-sa/3.0/`. Recorded: the **visible text carries
no version number**; only the href says 3.0. Also recorded: no "unmodified", and no "all other
rights reserved". The report describes this as a materially different and more permissive grant
than the rest of the site, where derivatives are allowed but a ShareAlike obligation attaches.

### 3g. TRU Math Suite, no license statement

URL: `https://map.mathshell.org/trumath.php`, **HTTP 200**, 2026-08-08. Full page body extracted
and searched: **zero** hits for creativecommons, license, reproduce, or rights reserved. Only
the global footer applies.

### 3h. Index pages carry no license block

`https://map.mathshell.org/lessons.php` (200), 0 hits for "creativecommons".
`https://map.mathshell.org/tasks.php` (200), 0 hits for "creativecommons".
`https://map.mathshell.org/stds.php` (200), 0 hits.

Recorded: the grant appears only on individual resource pages, not on the browse indexes.

## 4. The PDFs say different things than the web pages that serve them

### 4a. Classroom Challenge lesson PDF, CC BY-NC-ND on cover and back page

File: `download.php?fileid=1754`, served as `enlargements r1.pdf` ("Evaluating Statements About
Enlargements"), **HTTP 200**, `Content-Type: application/pdf`, 2,745,271 bytes, 2026-08-08.
Text extracted via `pdftotext -layout`.

Cover page (p.1), verbatim:

> © 2015 MARS, Shell Center, University of Nottingham
> May be reproduced, unmodified, for non-commercial purposes under the Creative Commons license
> detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/ - all other rights reserved

Final page, verbatim:

> © 2015 MARS, Shell Center, University of Nottingham
> This material may be reproduced and distributed, without modification, for non-commercial purposes,
> under the Creative Commons License detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/
> All other rights reserved.
> Please contact map.info@mathshell.org if this license does not meet your needs.

### 4b. Summative task PDF, no CC at all, "All rights reserved"

File: `download.php?fileid=499`, served as `hopewell_geometry.pdf`, **HTTP 200**,
`application/pdf`, 93,563 bytes, 2026-08-08. Both pages carry, verbatim, as a running footer:

> Copyright © 2011 by Mathematics Assessment
> Resource Service. All rights reserved.

Recorded finding: the PDF grants nothing. The CC BY-NC-ND 3.0 grant for this file exists only on
the HTML page that links to it (3d above). Anyone who receives the PDF alone sees pure
all-rights-reserved.

### 4c. Summative task rubric PDF, no notice of any kind

File: `download.php?fileid=500`, served as `hopewell_geometry_rubric.pdf`, **HTTP 200**, 144,913
bytes, 2026-08-08. Text extracted cleanly, recorded as 36 lines with content verified readable.
**Zero** hits for copyright, license, creative commons, or rights reserved. Recorded as silent.

### 4d. Teacher guide PDF, CC BY-NC-ND 3.0 stated twice

File: `https://map.mathshell.org/docs/map_cc_teacher_guide.pdf`, **HTTP 200**, 706,151 bytes,
2026-08-08.

Cover:

> May be reproduced, unmodified, for non-commercial purposes under the Creative Commons license
> detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/ - all other rights reserved

Inside front matter:

> © 2013-2015 MARS, Shell Center, University of Nottingham.
> This document may be distributed, unmodified, under the Creative Commons Attribution, Non-
> commercial, No Derivatives License 3.0 detailed at http://creativecommons.org/licenses/by-nc-nd/3.0/
> All other rights reserved. Please send any enquiries about commercial use or derived works to
> map.info@mathshell.org.

## 5. Riders, as enumerated by the evidence file

1. **NoDerivatives (ND).** Every grant except PD Modules requires "unmodified", "without
   modification", or "as-is".
2. **NonCommercial (NC).** On all grants.
3. **ShareAlike (SA) on PD Modules only**, `by-nc-sa/3.0`. Derivatives allowed but the
   derivative inherits BY-NC-SA.
4. **"All other rights reserved"** is appended to every ND grant.
5. **CCSS third-party carve-out**, from the footer: "State, district and CCSSI standards appear
   courtesy of their respective authors." The report records that the standards text quoted
   inside MAP materials is not MARS's to license, and attributes CCSS to NGA Center and CCSSO
   under its own public-license terms.
6. **Artifact and page mismatch.** The summative task PDFs say "All rights reserved" with no CC.
   The evidence for the CC grant on a task PDF is the web page, not the file.
7. **Version 3.0 Unported, not 4.0.** The href has no jurisdiction code. The report notes 3.0
   Unported has a weaker attribution and DRM regime than 4.0 and no 30-day cure period for
   violations.
8. **Attribution string.** No canonical string is published anywhere on the site. BY requires
   attribution but MARS does not specify the form. Recorded best available from the artifacts:
   "© 2015 MARS, Shell Center, University of Nottingham" plus `http://map.mathshell.org`.
9. **Trademark.** No trademark terms found anywhere on the site; searched, zero hits.
10. **Prototype-status warning** on Prototype Tests (3e), recorded as a use-fitness caveat MARS
    attaches rather than a license term.

## 6. What the host offers on HSG-SRT.B.4 / B.5 / C.6 / C.7 / C.8

The site publishes its own CCSSM crosswalk at `stds.php`. Recorded node ids: Geometry is
`standardid=1367`; the G-SRT node is `https://map.mathshell.org/stds.php?standardid=1400`
(HTTP 200, 2026-08-08).

MARS's own mapping, read off that page:

**Cluster "Prove theorems involving similarity"**, to Classroom Challenges:
- Modeling Motion: Rolling Cups, `lessons.php?taskid=690`
- Deducting Relationships: Floodlight Shadows, `lessons.php?taskid=691`
- Evaluating Statements About Length and Area, `lessons.php?taskid=692`

**Cluster "Define trigonometric ratios and solve problems involving right triangles"**, to
Classroom Challenges:
- Solving Quadratic Equations, `lessons.php?taskid=685`
- Inscribing and Circumscribing Right Triangles, `lessons.php?taskid=696`
- Solving Problems with Circles and Triangles, `lessons.php?taskid=697`
- Calculating Volumes of Compound Objects, `lessons.php?taskid=699`

Other on-topic HS Classroom Challenges from `lessons.php` (HTTP 200): Evaluating Statements
About Enlargements (9320), Proving the Pythagorean Theorem (9325), Evaluating Conditions for
Congruency (9315), Transforming 2D Figures (9365). Grade 8 feeders: Identifying Similar
Triangles (8320), Discovering the Pythagorean Theorem (8315).

**Summative Assessment Tasks** (`tasks.php?collection=9`, HTTP 200) recorded as directly
on-standard:
- **Hopewell Geometry (HA05).** Task text fetched: right-triangle earthworks; Q1 asks the
  hypotenuse of a 1-by-7 right triangle to one decimal place; Q2 asks the smallest angle of a
  3-4-5 triangle to one decimal place; Q3 tests recognizing an enlargement by scale factor 3.
  The rubric PDF's own answer key uses, verbatim: `sin-1 3/5 or cos-1 3/5 or tan-1 3/4`.
- Proofs Of The Pythagorean Theorem? (HE04), compares three attempted proofs.
- Temple Geometry (HA13), Edo-period sangaku puzzle.
- Triangular Frameworks (HE09), triangle construction under constraints.
- Pythagorean Triples (HE08), Sidewalk Patterns (HA06), recorded as adjacent.
- Trigonometric Functions (HN09), recorded as F-TF territory, not G-SRT.

Recorded file set: each task ships 4 files, the task PDF, a rubric PDF, and two
annotated-student-work PDFs (`un` for unscored, `sc` for scored).

**Recorded gap:** there is no Classroom Challenge whose stated goal is defining sine, cosine or
tangent from similarity (C.6), or the sine and cosine complementary relationship (C.7).

## 7. Analysis recorded by the evidence file, not host text

Attribute the following to this project's own measurement, never to MARS:

- The report calls the "Precise terms vary between materials" clause "itself the headline
  finding", on the ground that the site refuses to make a single sitewide grant.
- The report reads "as-is" in the homepage sidebox as no-derivatives stated in plain English.
- The report characterises the MARS C.6 to C.8 lesson mapping as "thin and partly spurious"
  because it lists "Solving Quadratic Equations", and notes explicitly that this mapping is
  MARS's own and not the agent's.
- The report calls the Hopewell Geometry task "the strongest single hit" and reads it as
  G-SRT.C.8 with a G-SRT.B.5 similarity item in the same task.
- The report calls the scored annotated student work "genuinely useful for a misconceptions
  section".
- The report's §7 "Bottom line for the repo" is that agent's application of these grants to the
  HS Geometry repo, not host text. Its stated positions: curate-and-cite is fully clear because
  linking and citing is not redistribution and ND and NC do not reach it; verbatim
  redistribution of a whole unmodified lesson or task PDF is licensed non-commercially with
  attribution; paraphrase-and-republish is not licensed because ND blocks it, while original
  expression of the underlying mathematics is fine because mathematics is not copyrightable;
  PD Modules are the one exception at BY-NC-SA 3.0 and should be quarantined; TRU Math is
  treated as all rights reserved and cite-only; short attributed quotation is characterised as a
  fair-use call rather than a CC-granted right; NC is satisfied while nothing is sold and would
  break on any future monetisation.
