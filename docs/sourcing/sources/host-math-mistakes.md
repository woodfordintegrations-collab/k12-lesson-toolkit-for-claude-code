---
source_url: hs-geometry-similarity-trig/sources/license-mathmistakes.md
fetched: 2026-08-07
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-math-mistakes, trap-down-is-not-one-state, concept-chain-of-title, evidence-misconception-research-licensing, practice-build-a-source-table, license-cc-by, practice-cite-without-redistributing
---

# mathmistakes.org

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every probe recorded below was performed by the verifying agent on
**2026-08-07**, which is the fetch date the report states for itself. That is one day earlier
than the rest of this corpus, and the difference is real, not a typo to be smoothed.

**Three facts govern everything on this host and none of them may be collapsed into the
others:**

1. The live host is UP and returns HTTP 200. What it returns is a PHP fatal error as the entire
   body, on every path probed. This is neither a bot block, nor a TLS failure, nor a dead
   server, nor a soft 404.
2. **All licence evidence on this page is from Wayback.** Zero licence text is obtainable from
   the live host.
3. The CC BY 3.0 Unported grant is real and longstanding, and it does not resolve two separate
   problems that sit outside licensing: **chain of title** on teacher-submitted photographs, and
   **student privacy**. Those are unresolved independently of the grant.

---

## 1. Reachability: a live server running a dead application

Root fetch, browser UA:

```
curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ..." \
     https://mathmistakes.org/
HTTP:200  size:1830  content-type: text/html; charset=UTF-8
```

The report is explicit about what this is not: not a bot block (no 403 or 406 was served to
it), not a TLS error (the handshake was fine), not DNS-dead (the server answered in 0.88s). The
report states the three categories in its brief had no slot for what it found and calls it a
fourth thing.

**HTTP 200 with a PHP fatal error as the entire body.** Verbatim:

```
Fatal error: Uncaught ArgumentCountError: Too few arguments to function
WP_Widget::__construct(), 0 passed in /home/mathmist/public_html/wp-includes/
class-wp-widget-factory.php on line 62 and at least 2 expected in
/home/mathmist/public_html/wp-includes/class-wp-widget.php:163
Stack trace:
#2 /home/mathmist/public_html/wp-content/plugins/advanced-tag-list/
   advanced-taglist.php(12): register_widget('Advanced_Taglis...')
#6 /home/mathmist/public_html/wp-includes/widgets.php(1884): do_action('widgets_init')
thrown in /home/mathmist/public_html/wp-includes/class-wp-widget.php on line 163
```

Root cause as the report diagnoses it: the abandoned `advanced-tag-list` plugin registers a
widget whose constructor signature broke under PHP 8. ArgumentCountError was recoverable in PHP
7 and is fatal in PHP 8. It throws on `widgets_init`, which fires on EVERY WordPress request
before routing. Hence a total outage with no exceptions.

Path probe. The report's own prose says "all 13 paths return the byte-identical 1830-byte
fatal", and its table lists these rows:

| Path | HTTP | size | fatal |
|---|---|---|---|
| / | 200 | 1830 | yes |
| /about | 200 | 1830 | yes |
| /terms | 200 | 1830 | yes |
| /terms-of-use | 200 | 1830 | yes |
| /copyright | 200 | 1830 | yes |
| /permissions | 200 | 1830 | yes |
| /license | 200 | 1830 | yes |
| /faq | 200 | 1830 | yes |
| /contact | 200 | 1830 | yes |
| /feed | 200 | 1830 | yes |
| /sitemap.xml | 200 | 1830 | yes |
| /wp-json/wp/v2/posts | 200 | 1830 | yes |
| /?p=1 | 200 | 1830 | yes |
| /category/geometry | 200 | 1830 | yes |

**Number discrepancy inside the source, preserved rather than resolved:** the report's prose
states 13 paths. Its table, reproduced above exactly as it stands, lists 14 rows. That row count
is this staging pass's own count of the reproduced table, not a figure the report states. The
two do not agree and this extract does not pick a winner. If a page needs a count, write "every
path probed", or quote the report's "13" and say the table disagrees. Do not silently ship
either number as the count of paths.

RSS and the REST API are down too, so the report records that there is no machine-readable
escape hatch.

The report's verdict on its own recon hypothesis: confirmed, and current rather than stale.
**Zero licence text is obtainable from the live host today.**

## 2. Wayback: the corpus is recoverable

Availability API:

```
http://archive.org/wayback/available?url=mathmistakes.org
{"archived_snapshots": {"closest": {"status": "200", "available": true,
 "url": "http://web.archive.org/web/20260220051333/https://mathmistakes.org/",
 "timestamp": "20260220051333"}}}
```

That snapshot was fetched: **HTTP 200, 257,612 bytes, `<title>Math Mistakes</title>`, zero
"Fatal error" occurrences.** Real content. The report's conclusion: the corpus is fully
recoverable.

**CDX API unavailable**, and the report is precise about the failure mode:
`web.archive.org/cdx/search/cdx` returned 503 Service Unavailable on 4 attempts, then 504
Gateway Time-out. The report attributes this to an Internet Archive infrastructure problem on
their end, noting the availability API and individual snapshot replay both worked fine
throughout. Consequence: the agent could NOT enumerate the full capture history or pin the exact
outage onset date.

A trap the report records deliberately: probing `/web/2025/` and `/web/2026xxxx/` returned a
46,860-byte page. It is not a capture. It is HTTP 403 with
`<title>Visitor anti-robot validation</title>`, replayed from snapshot 20260104191043. That is
an anti-bot WAF challenge which mathmistakes.org's host served to the Internet Archive crawler
in January 2026 and which got archived as content. The report's line: reporting that as "the
site was blocked in 2025" would have been wrong in two ways at once. Some 2026 snapshots are WAF
pages; 20260220051333 is clean.

Outage bounded by the report: good capture **2026-02-20**, broken **2026-08-07** (its own fetch
date).

## 3. The licence, verbatim

A sidebar text widget, present on the root and on every post sampled. Raw HTML from snapshot
20260220051333:

```html
<div class="textwidget">
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">
<img alt="Creative Commons License" style="border-width:0"
     src="https://i0.wp.com/i.creativecommons.org/l/by/3.0/88x31.png?w=580"/></a>
<br/>This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">
Creative Commons Attribution 3.0 Unported License</a>.
</div>
```

The licence sentence, exactly:

> This work is licensed under a Creative Commons Attribution 3.0 Unported License.

Linked deed: `http://creativecommons.org/licenses/by/3.0/deed.en_US`. The agent verified that
deed URL resolves: **HTTP 200**, redirecting to
`https://creativecommons.org/licenses/by/3.0/deed.en`.

Footer, separately, theme default, snapshot 20260220051333:

> © 2026 Math Mistakes Powered by WordPress

The report's note on the two coexisting: the footer © and the sidebar CC BY coexist; the CC BY
widget is the operative grant, and a bare © notice is not inconsistent with a CC licence,
because the author does hold copyright and licenses it out.

### The grant is longstanding, not a recent addition

The same string was found on root captures across 12 years:

| Snapshot | Licence string |
|---|---|
| 20140517212051 | Creative Commons Attribution 3.0 Unported License |
| 20160524142902 | Creative Commons Attribution 3.0 Unported License |
| 20180521035129 | Creative Commons Attribution 3.0 Unported License |
| 20200518014659 | Creative Commons Attribution 3.0 Unported License |
| 20221207024233 | Creative Commons Attribution 3.0 Unported License |
| 20260220051333 | Creative Commons Attribution 3.0 Unported License |

Why the report says this matters legally: the grant was in force when the SRT posts were
published in 2014, so it attaches to that material.

### No dedicated terms page exists

`/terms/`, `/contact/`, `/faq/` all return **404 in Wayback**, never archived, which the report
reads as strongly suggesting they were never created. `/about/` exists. The CC BY notice is a
sidebar widget, not a formal terms-of-use document. There is no `/license`, `/copyright`, or
`/permissions` page in the archive.

## 4. Per-resource check: no variation found

Five individual posts pulled from Wayback. Every one carries the same sidebar notice; none
carries its own or a conflicting notice.

| Post | Wayback ts | HTTP | own notice | rel=license target |
|---|---|---|---|---|
| /attack-of-the-decimals-in-trigonometry/ | 20240806053559 | 200 | CC BY 3.0 Unported (site-wide widget) | licenses/by/3.0 |
| /they-are-not-similar-because-you-have-to-add-different-numbers/ | 20240519053129 | 200 | CC BY 3.0 Unported | licenses/by/3.0 |
| /306090-mistakes/ | 20240619233902 | 200 | CC BY 3.0 Unported | licenses/by/3.0 |
| /a-whole-bunch-of-questions-about-right-triangles/ | 20240621014537 | 200 | CC BY 3.0 Unported | licenses/by/3.0 |
| /similar-figures/ | 20241011181517 | 200 | CC BY 3.0 Unported | licenses/by/3.0 |

Each was scanned for "all rights reserved", "used with permission", "reprinted", and per-image
credit lines: **none found on any of the five.** Category page 2 of the SRT category
(ts 20240522153900) also carries the notice.

Report's conclusion: this is not a varies-per-resource site. One uniform grant.

## 5. Riders, as the report enumerates them

1. **Attribution required (the BY term), and NO attribution string is specified.** The site
   gives a bare CC BY widget with no "please cite as…". The author handle is `mpershan`
   (`/author/mpershan/`), Michael Pershan. The report's instruction: a citer must construct a
   reasonable credit consisting of title, author, source URL, licence.
2. **The version is 3.0 Unported, not 4.0.** The report notes 3.0 lacks 4.0's 30-day cure period
   for inadvertent violations and handles attribution and moral rights differently. Its
   instruction: do not silently label this "CC BY 4.0".
3. **Chain of title is undocumented, and the report calls this the big one.** The About page
   states the model verbatim: *"That student work will be posted by me, but sent in by you."*
   The corpus is teacher-submitted photographs of student work. The site owner asserts a blanket
   CC BY over material he did not author or photograph, and there is no visible submission
   agreement, rights transfer, or contributor terms anywhere on the site, since no `/terms` page
   exists. Whether he had authority to sublicense submitters' photographs under CC BY is **not
   established by anything on the site.**
4. **Student privacy, independent of copyright.** Every post is a photo of a minor's handwritten
   work. Some images may carry names or identifying marks. The report's statement: a valid CC BY
   grant does not resolve privacy or FERPA-adjacent exposure in a public-facing repo. This is a
   separate axis from licensing.
5. **Comments are where the substance lives, and their status is unstated.** The site's design
   puts the pedagogical analysis in third-party comment threads. Whether "This work" in the
   widget extends to commenter text is not specified.
6. **Images are served via `i0.wp.com`** (Jetpack or Photon CDN) with the originals at
   `mathmistakes.org/wp-content/uploads/`. The report marks this as not a licence rider per se,
   but notes the images ARE the substance of every post and are currently only reachable through
   Wayback.
7. **No trademark terms found.** Nothing was located either way.

## 6. Relevance to HSG-SRT.B.4, B.5, C.6, C.7, C.8

The report calls the fit strong and unusually well targeted. The site maintains a CCSS-indexed
taxonomy, with 200 category URLs found, including a category that is literally the assigned
domain:

- `/category/high-school-geometry/similarity-right-triangles-and-trigonometry/`, 2 pages,
  approximately 17 posts. Title: "Similarity, Right Triangles and Trigonometry".
- `/category/high-school-geometry/similarity-right-triangles-and-trigonometry/g-srt-10/`,
  showing standard-level tagging exists.
- `/category/geometry/similar-figures/`, 7 posts
- `/category/geometry/right-triangles/`, 6 posts
- `/category/geometry/pythagorean-theorem/`, `/category/geometry/congruent-triangles/`,
  `/category/trigonometry/` (plus law-of-sines, law-of-cosines, inverse-trig subcategories)

Named on-target posts, all Wayback-recoverable:

- "Decimal Misconceptions? Meet Trigonometry." `/attack-of-the-decimals-in-trigonometry/`
- "30/60/90 Mistakes" `/306090-mistakes/` (2014-05-19), special right triangles, C.8
- "Special Right Triangles" `/special-right-triangle/`
- "They are not similar because you have to add different numbers…", additive versus
  multiplicative reasoning on similar figures, which the report places dead-centre on B.5
- "People Often Use Additive Instead of Multiplicative Reasoning"
- "Comparing Parts of Sides Instead of Whole Sides"
- "Decimal Misconceptions? Meet similar triangles."
- "Scaling by 1/2", "Similar Figures", "Using a bad base"
- "All Ramps Are 45 Degrees + Pythagorean Theorem"
- "Trigonometry: find the missing angle" `/trigonometry-find-the-missing-angle/`
- "All the sides in the 6-8-10 triangle are equal"
- "A whole bunch of questions about right triangles"

What the report says each post actually is: one photo of real student work, 1 to 3 sentences of
teacher framing, and a comment discussion. Example, from
`/attack-of-the-decimals-in-trigonometry/`, verbatim excerpt:

> "A reflection from the submitter: I think this 10th grader is saying
> .174>.34>.5. … It's best to see this not as a failure of decimal knowledge…"

The report's characterisation: this is a misconception corpus, not a lesson or task bank. Its
value to the unit is diagnostic, supplying authentic student error patterns to inform
anticipated-misconception sections, warm-up "analyze this work" prompts, and formative-assessment
design. It will NOT supply problem sets or tasks.

Publishing cadence: the archives dropdown ends **February 2021**, with 42 pages of posts
site-wide. The report's reading: the blog is finished, not merely broken, and the corpus is
finite and static.

## 7. The report's practical note

Because the live host serves nothing, any citation must point at a Wayback URL, for example
`https://web.archive.org/web/20260220051333/https://mathmistakes.org/`, or carry an "archived
at" note. A bare `https://mathmistakes.org/...` link in a public repo will land readers on a PHP
stack trace.

The report's licence conclusion, and its boundary: CC BY 3.0 clears the project's
curate-and-cite model completely, and would also clear paraphrase-and-republish and direct
quotation, with no ShareAlike, no NonCommercial, no NoDerivatives. **The binding constraints
here are riders 3 and 4, the undocumented chain of title on third-party submissions and student
privacy, not the licence text.**

## 8. Scratchpad hygiene note the report records

The scratchpad directory was shared with sibling agents. `cat_srt.html` in it was an Open Middle
page written by another agent at 18:49, not this agent's. The agent states it caught the file
via a glob and excluded it, and that all subsequent reads used explicit filenames plus a
`mathmistakes.org` host-count assertion per file. No other host's data entered these findings.
