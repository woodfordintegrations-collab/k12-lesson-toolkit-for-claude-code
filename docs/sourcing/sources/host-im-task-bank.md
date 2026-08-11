---
source_url: hs-geometry-similarity-trig/sources/license-im-tasks.md
fetched: 2026-08-08
http_status: n/a for local files
role: primary
covers: source-im-task-bank, license-sharealike, concept-cite-quote-adapt, concept-chain-of-title, concept-third-party-carve-out, practice-build-a-source-table, trap-summary-layer-is-not-evidence, trap-sharealike-contaminates-by-paraphrase, trap-license-lives-off-the-obvious-page
---

# Host extract: tasks.illustrativemathematics.org (the 2016 IM task bank)

**Original fetch date recorded by the evidence file: 2026-08-08**, with the server date header
recorded verbatim as `Sat, 08 Aug 2026 01:46:12 GMT`. The `fetched:` field above is the staging
date.

**Method recorded by the evidence file:** bash `curl` with a browser user agent, raw bytes
inspected. The report states: "Every quote below was read out of a downloaded file, not from
memory."

Every quotation below is transcribed from the evidence file named in `source_url`. No host was
re-fetched at staging time.

---

## 1. Reachability, as recorded

| URL | Status | Note |
|---|---|---|
| `https://tasks.illustrativemathematics.org/` | 200 | Cloudflare, HTTP/2. Kendall Hunt marketing landing page, NOT the task bank |
| `/content-standards` | 200 | task bank entry point, license footer present |
| `/content-standards/HSG/SRT` | 200 | domain page |
| `/content-standards/HSG/SRT/{B,C}/{4,5,6,7,8}/tasks` | 200 | task lists |
| `/content-standards/HSG/SRT/C/8/tasks/710` etc. | 200 | individual tasks |
| `/terms` `/terms-of-use` `/copyright` `/license` `/about` `/faq` `/permissions` | 404 | no dedicated terms page on this host |
| `/privacy` `/privacy.html` | 404 | root footer link is broken |
| `/sitemap.xml` | 404 | |
| `/robots.txt` | 200 | 1248 bytes, comment preamble only |
| `/content-standards/HSG-SRT` ("View all HSG-SRT Tasks") | 404 | broken link on the domain page |
| Legacy `/content-standards/HSG-SRT/B/4/tasks/1867`, `/illustrations/1867` | 404 | old URL scheme is gone |

Failure-mode discrimination recorded explicitly: no bot block anywhere. Every failure above is a
genuine 404 from the origin. `.html` suffixed paths return **308 Permanent Redirect** to the
extensionless form.

## 2. The root does not carry the license, and a summary layer said it did

The starting hypothesis under test was "a curl of the root returned the CC BY-NC-SA string." The
evidence file records that this is false for `/`. Raw byte counts on the root document,
transcribed verbatim:

```
grep -c -i "creative"  im_root.html  -> 0
grep -c -i "copyright" im_root.html  -> 0
grep -c -i "licen"     im_root.html  -> 0
```

Root visible text ends: `... Learn More Privacy Policy | Accessibility Information`.
Root `<title>` is `Illustrative Mathematics | Kendall Hunt`.

The license lives on the task-bank pages under `/content-standards`, one level in.

Recorded verbatim from the evidence file, the summary-layer failure:

> A first WebFetch of `/` returned the CC sentence anyway — i.e. the summarizing model
> produced text absent from the bytes it was given. Treated as unreliable; all findings
> below come from raw curl output only.

## 3. Verbatim license, confirmed at byte level

Recorded as identical markup on `/content-standards` and on every task page checked. Raw HTML as
served:

```html
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank"><img src="../assets/cc-88x31.png" style="float: left"></a>
    Typeset May 4, 2016 at 18:58:52. Licensed by <a href="https://www.illustrativemathematics.org" target="_blank">Illustrative Mathematics</a> under a <br>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US" target="_blank">Creative Commons
        Attribution-NonCommercial-ShareAlike 4.0 International License.</a>
```

Rendered sentence, verbatim:

> Typeset May 4, 2016 at 18:58:52. Licensed by Illustrative Mathematics under a
> Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

Recorded verdict: CC BY-NC-SA 4.0, uniform. No per-page variation found.

## 4. Per-resource sampling

Six task pages opened individually, all under `/content-standards/`:

| Task | Std | Title | Own notice? |
|---|---|---|---|
| `HSG/SRT/B/4/tasks/1095` | B.4 | Joining two midpoints of sides of a triangle | none; same footer |
| `HSG/SRT/B/4/tasks/1568` | B.4 | Pythagorean Theorem | none; same footer |
| `HSG/SRT/B/5/tasks/1591` | B.5 | How far is the horizon? | none; same footer |
| `HSG/SRT/C/6/tasks/1635` | C.6 | Defining Trigonometric Ratios | none; same footer |
| `HSG/SRT/C/7/tasks/1443` | C.7 | Sine and Cosine of Complementary Angles | none; same footer |
| `HSG/SRT/C/8/tasks/710` | C.8 | Seven Circles III | none; same footer |

Keyword sweep across all six raw files for `adapted from`, `courtesy`, `used with permission`,
`photo by`, `wikimedia`, `flickr`, `all rights reserved`, `public domain`: **zero hits**. The
only `attribut` hits outside New Relic telemetry JS are the words inside the CC license name
itself.

### All 24 in-scope tasks were then swept

Recorded: every one of the 24 returned HTTP 200 and every one carries the same CC BY-NC-SA
footer string. No task overrides the license.

The sweep turned up **four tasks that state an upstream source**, all HSG-SRT.B.5. Upstream
statements verbatim from the IM Commentary on each page:

| Task | Upstream, verbatim from the IM Commentary |
|---|---|
| 1002 Bank Shot | "This task was adapted from problem #12 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 1009 Tangent Line to Two Circles | "This task was adapted from problem #19 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 916 Finding triangle coordinates | "This task was adapted from problem #11 on the 2012 American Mathematics Competition (AMC) 10A Test. In the AMC exam question, the diagram was not given." |
| 918 Slope Criterion for Perpendicular Lines | "This task was adapted from problem #15 on the 2012 American Mathematics Competition (AMC) 10A Test." |

Recorded facts about these four: the pages assert a blanket CC BY-NC-SA footer over content they
simultaneously declare is adapted from AMC exam problems. AMC is run by the MAA. **The evidence
file records that this host says nothing about the AMC/MAA rights position, and that the agent
did not leave this host to check it, so the upstream grant is unverified from here.**

The other 20 in-scope tasks state no upstream source.

## 5. Riders, as enumerated by the evidence file

1. **NC.** CC BY-NC-SA 4.0 forbids commercial reuse of the material itself.
2. **SA, ShareAlike.** Recorded verbatim: "Citing is not redistributing and is unaffected. But
   paraphrase-and-republish at the level of an adaptation triggers SA: the derivative must ship
   under CC BY-NC-SA 4.0 (or compatible), which would license the whole repo NC. Original
   expression written from the standard, with IM cited as inspiration, avoids this. Close
   paraphrase of a specific task does not."
3. **Attribution string.** No canonical BY string is supplied by the host. The evidence file
   records the footer's own form as the best available model: attribute to "Illustrative
   Mathematics", linking `https://www.illustrativemathematics.org`, and name the license with a
   link to `https://creativecommons.org/licenses/by-nc-sa/4.0/`.
4. **Unstated photo provenance.** Task 1591 embeds photographs (`shishaldin_...jpg`,
   `Milong_...jpg`) served from `http://s3.amazonaws.com/illustrativemathematics/images/...`
   with no credit line. The page license implicitly covers them but the upstream source of the
   photographs is not stated anywhere on this host. The images are served over plain `http://`,
   so they are mixed content and may not render on the https page.
5. **Frozen archive.** "Typeset May 4, 2016". A static snapshot, not a live bank. The report
   records that nothing has been added in approximately 10 years, and that site chrome (Kendall
   Hunt header, 2019 logo) was refreshed later.
6. **robots.txt.** 1248 bytes, and it is only the Cloudflare content-signals explanatory
   comment. It declares no `User-agent` rule and no `Content-Signal` value, so no `ai-train=no`
   or `ai-input=no` restriction is expressed. It does carry a boilerplate EU DSM Article 4
   reservation-of-rights notice, but with no signal set the report records that nothing is being
   reserved by it. No crawl restriction found.
7. **Trademark.** No trademark terms found on this host.
8. **No terms-of-use page exists on this host.** Recorded verbatim: "The CC footer is the
   *entire* licensing statement available at `tasks.illustrativemathematics.org`."

## 6. What the host offers, 24 tasks in scope

Bulk download for the whole HSG category, linked from the domain page:
`https://s3.amazonaws.com/illustrativemathematics/attachments/zipped_files/grade_HSG.zip`
(recorded as link only, not downloaded).

**HSG-SRT.B.4 (2)**, `/content-standards/HSG/SRT/B/4/tasks`
- 1095 Joining two midpoints of sides of a triangle
- 1568 Pythagorean Theorem

**HSG-SRT.B.5 (11)**, `/content-standards/HSG/SRT/B/5/tasks`
- 1002 Bank Shot · 1009 Tangent Line to Two Circles · 1302 Unit Squares and Triangles
- 1517 Points from Directions · 1572 Extensions, Bisections and Dissections in a Rectangle
- 1591 Is this a rectangle? · 1685 Congruence of parallelograms
- 1876 Folding a square into thirds · 651 How far is the horizon?
- 916 Finding triangle coordinates · 918 Slope Criterion for Perpendicular Lines

  Recorded note: list order and id order differ; ids are the authoritative set.

**HSG-SRT.C.6 (2)**, `/content-standards/HSG/SRT/C/6/tasks`
- 1635 Defining Trigonometric Ratios
- 1904 Tangent of Acute Angles

**HSG-SRT.C.7 (2)**, `/content-standards/HSG/SRT/C/7/tasks`
- 1443 Sine and Cosine of Complementary Angles
- 1902 Trigonometric Function Values

**HSG-SRT.C.8 (7)**, `/content-standards/HSG/SRT/C/8/tasks`
- 1345 Setting Up Sprinklers · 1638 Seven Circles III · 1905 Coins in a circular pattern
- 607 Shortest line segment from a point P to a line L · 710 Neglecting the Curvature of the Earth
- 720 Ask the Pilot · 962 Constructing Special Angles

Adjacent clusters recorded: **HSG-SRT.A.1 (1)** Dilating a Line · **A.2 (4)** Are They Similar?,
Similar Quadrilaterals, Similar Triangles, Congruent and Similar Triangles · **A.3 (1)** Similar
triangles. **HSG-SRT.D.9 / D.10 / D.11 return 0 tasks each (empty).**

Page composition recorded: each task page carries the problem statement, an IM Commentary, and
worked solutions.

**Two id-to-title conflicts inside the evidence file itself, preserved rather than resolved.**
Both are between the six-page sampling table in section 4 and the full task inventory in this
section. Do not assert either pairing without re-fetching the task page.

1. Task **1591**. The sampling table gives `HSG/SRT/B/5/tasks/1591` the title "How far is the
   horizon?". This section's B.5 list gives 1591 the title "Is this a rectangle?" and gives
   "How far is the horizon?" to task **651**. Rider 4 in section 5 attributes the embedded
   photographs to task 1591.
2. Task **710**. The sampling table gives `HSG/SRT/C/8/tasks/710` the title "Seven Circles III".
   This section's C.8 list gives 710 the title "Neglecting the Curvature of the Earth" and gives
   "Seven Circles III" to task **1638**.

## 7. Recorded as unverified by the evidence file

- Whether `www.illustrativemathematics.org` (a different host, out of that agent's scope)
  publishes terms that supersede or add to this footer.
- Provenance of the embedded photographs.
- Contents of `grade_HSG.zip`, not downloaded.
- **The AMC/MAA upstream position on tasks 1002, 1009, 916, 918.** Recorded as "the one
  materially open question. Resolving it requires a host outside my scope."
- Whether the four AMC-derived tasks were cleared with MAA. The pages assert CC BY-NC-SA without
  mentioning any permission grant.

Recorded as closed: all 24 in-scope task pages were fetched and their footers confirmed by byte
match, so the earlier 6-of-24 inference gap no longer stands.

## 8. Analysis recorded by the evidence file, not host text

Attribute the following to this project's own measurement, never to Illustrative Mathematics:

- The report advises treating the four AMC-derived tasks as higher risk than the other twenty:
  cite them, do not paraphrase-and-republish them, and if one is wanted as a model problem,
  source the AMC original and clear it separately. Its stated reason: "IM's CC grant cannot
  convey rights IM does not hold."
- The report calls task 1568 "similar-triangle proof via the altitude", and describes it as the
  B.4 to C.8 bridge. It calls task 1635 the C.6 keystone because it builds the ratios from
  similarity. These are the report's characterisations, not host labels.
- The report advises not reusing the task 1591 photographs.
