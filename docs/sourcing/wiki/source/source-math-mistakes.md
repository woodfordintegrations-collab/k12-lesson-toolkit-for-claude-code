---
title: "mathmistakes.org"
type: source
verdict: quote_and_adapt
fetched: 2026-08-07
sources:
  - https://web.archive.org/web/20260220051333/https://mathmistakes.org/
  - https://mathmistakes.org/
  - http://creativecommons.org/licenses/by/3.0/deed.en_US
  - sources/host-math-mistakes.md
  - sources/cc-by-3-0.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# mathmistakes.org

## Summary

A CC BY 3.0 Unported misconception corpus on a host that is simultaneously up and unusable. Verdict
on the licence: `quote_and_adapt`. Verdict on what you should actually do with it: read it, cite
it, and reproduce none of its images. Those two sentences do not conflict, and keeping them apart
is the whole job of this page.

Three facts govern this host and none of them may be collapsed into the others.

1. **The live server is UP and returns HTTP 200. What it returns is a PHP fatal error as the entire
   body, on every path probed.** Not a bot block, not a TLS failure, not a dead server, not a soft
   404. The verifying report's own brief had three categories for a failed host and none of them
   fitted, so it named this a fourth thing. See [[trap-down-is-not-one-state]].
2. **All licence evidence on this page is from Wayback.** Zero licence text is obtainable from the
   live host today. The grant is nonetheless well evidenced: the same string was found on root
   captures across 12 years.
3. **The licence is not the binding constraint.** CC BY 3.0 carries no ShareAlike, no
   NonCommercial and no NoDerivatives, so it clears quotation, adaptation and commercial use. What
   it does not clear is **chain of title** on teacher-submitted photographs and **student privacy**.
   Both sit outside copyright and neither is resolved by a valid grant.

The project ruled that this host is in scope as **diagnostic reading**. The unit design records
the same ruling, §2 R11, verbatim: "Math Mistakes is in as diagnostic reading only. MVP is out."
Diagnostic reading means the authentic error patterns here inform original writing about
misconceptions. It does not mean the posts, and above all the photographs, enter the deliverable.

**The version is 3.0 Unported, not 4.0.** Do not silently upgrade the label. 3.0 and 4.0 impose
materially different attribution duties, set out under "What you may do with it".

## When to reach for it

Reach for this host when you need **authentic student error patterns** on similarity, right
triangles and trigonometry, to inform anticipated-misconception sections, "analyze this student's
work" warm-ups, and formative-assessment design. The site maintains a CCSS-indexed taxonomy with
200 category URLs found, including one named for exactly this domain:
`/category/high-school-geometry/similarity-right-triangles-and-trigonometry/`, titled "Similarity,
Right Triangles and Trigonometry", 2 pages. Standard-level tagging exists below it, for example
`.../g-srt-10/`.

The report places one post dead-centre on HSG-SRT.B.5: "They are not similar because you have to
add different numbers…", on additive versus multiplicative reasoning about similar figures. Others
it names as on target and Wayback-recoverable include "30/60/90 Mistakes" (2014-05-19, C.8),
"Special Right Triangles", "Decimal Misconceptions? Meet Trigonometry", "Decimal Misconceptions?
Meet similar triangles", "Comparing Parts of Sides Instead of Whole Sides", "All Ramps Are 45
Degrees + Pythagorean Theorem", and "A whole bunch of questions about right triangles".

Do **not** reach for this host for tasks or problem sets. The report is explicit that it is a
misconception corpus, not a lesson or task bank, and that it will not supply problem sets. Each
post is one photograph of real student work, one to three sentences of teacher framing, and a
comment discussion. And do not expect the store's own misconception facet to substitute: the
Learning Commons export ships `misconceptions.jsonl` at 0 bytes, which is why this host was sourced
at all. See [[evidence-kg-coverage-and-gaps]] and [[evidence-misconception-research-licensing]].

Do not reach for a bare `https://mathmistakes.org/...` URL in anything you publish. It lands the
reader on a stack trace. Cite the Wayback capture.

## What its own page says

Every quotation below was pasted by a verifying agent on **2026-08-07** and is staged verbatim in
`sources/host-math-mistakes.md`. That fetch date is one day earlier than the rest of this corpus
and the difference is real, not a rounding. Nothing here rests on a summarizing layer; see
[[trap-summary-layer-is-not-evidence]].

### What the live host says, which is a stack trace

Root fetch with a browser user agent, 2026-08-07:

```
HTTP:200  size:1830  content-type: text/html; charset=UTF-8
```

The entire body, verbatim:

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

The report's diagnosis, which is legible in the trace itself: the abandoned `advanced-tag-list`
plugin registers a widget whose constructor signature broke under PHP 8, `ArgumentCountError` was
recoverable in PHP 7 and is fatal in PHP 8, and it throws on `widgets_init`, which fires on every
WordPress request before routing. Hence a total outage with no exceptions. The report records that
`/feed` and `/wp-json/wp/v2/posts` return the same fatal, so there is no machine-readable escape
hatch either.

Path probe: every path probed returned the byte-identical 1830-byte fatal, including `/terms`,
`/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/faq` and `/about`. On how many paths
that was, see gotcha 6, which is a discrepancy inside the source that this page does not resolve.

### The licence, from the Wayback capture

Snapshot `https://web.archive.org/web/20260220051333/https://mathmistakes.org/`, HTTP 200, 257,612
bytes, `<title>Math Mistakes</title>`, zero occurrences of "Fatal error". Real content. The grant
is a sidebar text widget, present on the root and on every post sampled. Raw HTML:

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

The linked deed, `http://creativecommons.org/licenses/by/3.0/deed.en_US`, was independently
resolved: HTTP 200, redirecting to `https://creativecommons.org/licenses/by/3.0/deed.en`.

The theme-default footer sits beside it, verbatim:

> © 2026 Math Mistakes Powered by WordPress

The two coexist without conflict. A bare copyright notice is not inconsistent with a CC licence,
because the author does hold the copyright and licenses it out. The sidebar widget is the operative
grant.

### The grant is longstanding, which is what makes it attach to the 2014 posts

The same string was found on root captures across 12 years:

| Snapshot | Licence string |
|---|---|
| 20140517212051 | Creative Commons Attribution 3.0 Unported License |
| 20160524142902 | Creative Commons Attribution 3.0 Unported License |
| 20180521035129 | Creative Commons Attribution 3.0 Unported License |
| 20200518014659 | Creative Commons Attribution 3.0 Unported License |
| 20221207024233 | Creative Commons Attribution 3.0 Unported License |
| 20260220051333 | Creative Commons Attribution 3.0 Unported License |

The report's legal point: the grant was in force when the HSG-SRT posts were published in 2014, so
it attaches to that material. This is the opposite of the pattern on the withdrawn-grant hosts in
[[license-withdrawn-grants]], and it is worth stating rather than assuming.

### There is no terms page, and there never was

`/terms/`, `/contact/` and `/faq/` return **404 in Wayback**, never archived, which the report reads
as strongly suggesting they were never created. `/about/` exists. There is no `/license`,
`/copyright` or `/permissions` page anywhere in the archive. The CC BY notice is a sidebar widget,
not a formal terms-of-use document.

### No per-resource variation

Five individual posts were pulled from Wayback. Every one carries the same sidebar notice and none
carries its own or a conflicting one.

| Post | Wayback timestamp | HTTP | rel=license target |
|---|---|---|---|
| /attack-of-the-decimals-in-trigonometry/ | 20240806053559 | 200 | licenses/by/3.0 |
| /they-are-not-similar-because-you-have-to-add-different-numbers/ | 20240519053129 | 200 | licenses/by/3.0 |
| /306090-mistakes/ | 20240619233902 | 200 | licenses/by/3.0 |
| /a-whole-bunch-of-questions-about-right-triangles/ | 20240621014537 | 200 | licenses/by/3.0 |
| /similar-figures/ | 20241011181517 | 200 | licenses/by/3.0 |

Each was scanned for "all rights reserved", "used with permission", "reprinted", and per-image
credit lines. None was found on any of the five. This is not a varies-per-resource site.

### What the About page says about where the material comes from

The submission model, verbatim from the About page:

> That student work will be posted by me, but sent in by you.

That one sentence is the reason gotcha 2 below exists. It establishes that the corpus is
teacher-submitted photographs of other people's students, over which the site owner asserts a
blanket CC BY.

## What you may do with it

| Operation | Permitted by the licence | Permitted by this project |
|---|---|---|
| Cite: name a post, link its Wayback capture, describe the error pattern in your own words | yes | yes, this is the intended use |
| Quote: reproduce the teacher framing or a commenter's words in quotation marks | yes, attribution below | teacher framing yes; comments see gotcha 4 |
| Paraphrase and republish: rewrite its text and ship it | yes, no copyleft | permitted but unnecessary, and R11 scopes this host to diagnostic reading |
| Reproduce the photographs of student work | not resolved by the licence | **no.** See gotchas 2 and 3 |

CC BY 3.0's deed carries `for any purpose, even commercially` on both freedoms and its "Under the
following terms" list has exactly two items, Attribution and No additional restrictions. Neither
ShareAlike nor NoDerivatives appears. The report's own conclusion is that the licence clears the
curate-and-cite model completely and would also clear paraphrase-and-republish and direct
quotation, and that the binding constraints here are riders 3 and 4, not the licence text.

### The attribution block, which had to be constructed

No attribution string is specified anywhere on the site. The site offers a bare CC BY widget with
no "please cite as". The author handle is `mpershan`, at `/author/mpershan/`, Michael Pershan. The
verdict table states in its own words that the following string was **constructed** by this project
rather than taken from the host:

```
"<Post title>", Michael Pershan, Math Mistakes.
Licensed under a Creative Commons Attribution 3.0 Unported License.
http://creativecommons.org/licenses/by/3.0/
Archived at https://web.archive.org/web/<timestamp>/https://mathmistakes.org/<slug>/
(the live site has been returning a PHP fatal error on all paths as of 2026-08-07).
Accessed 2026-08-07.
```

### What CC BY 3.0 requires that CC BY 4.0 does not

This is why the label is never upgraded. Three duties in the 3.0 legal code have no 4.0
counterpart.

- **The title of the Work.** Section 4(b)(ii) requires `the title of the Work if supplied`. The
  phrase appears 1 time in the CC BY 3.0 legal code and 0 times in the CC BY 4.0 legal code. The
  block above carries the post title first for this reason.
- **A credit identifying the use, if you adapt.** Section 4(b)(iv) requires, for an adaptation, `a
  credit identifying the use of the Work in the Adaptation`, with worked examples. The deed does
  not mention this at all.
- **The changes-made indication is a condition of the adaptation right, not an attribution
  nicety.** In 3.0 it sits inside the grant, Section 3(b), verbatim:

  > to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work.

  Fail it and the adaptation was never licensed, rather than merely credited badly. The deed's own
  footnote on `indicate if changes were made` closes with the qualifier, verbatim:

  > In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

Running the other way, 3.0 imposes no duty to retain an indication of previous modifications;
measured, the phrase `previous modifications` appears 0 times in its legal code. See
[[license-cc-by]], which holds both versions side by side.

### What the grant does not reach

The photographs, whose chain of title is undocumented (gotcha 2); the people in them, since
copyright and privacy are different axes (gotcha 3); and the comment threads, whose status under
"This work" is unstated (gotcha 4). On trademark, nothing was found either way, which the report
says plainly rather than reading silence as permission. See [[concept-third-party-carve-out]] and
[[practice-cite-without-redistributing]].

## Gotchas & constraints

**1. "The site is down" is the wrong record, and this host is why.** A 406 user-agent filter, a 403
JavaScript challenge, an expired certificate, a TLS handshake failure, an NXDOMAIN apex, a
server-side timeout and this, a PHP fatal served as HTTP 200, all read alike from a distance and
each has a different correct next move. Here the correct move was Wayback, and it recovered the
entire corpus. Recording this host as "unavailable" would have lost a live, longstanding CC BY
grant. See [[trap-down-is-not-one-state]].

**2. Chain of title is undocumented, and the report calls this the big one.** The corpus is
teacher-submitted photographs of student work. The site owner asserts a blanket CC BY over material
he did not author and did not photograph. There is no visible submission agreement, no rights
transfer, and no contributor terms anywhere on the site, because no `/terms` page was ever created.
Whether he had authority to sublicense submitters' photographs under CC BY is **not established by
anything on the site**, and the verdict table records that it is unresolvable from the site: it
would require asking the owner, which is outside every agent's scope. A clean licence footer is not
the end of the analysis. See [[concept-chain-of-title]].

**3. Student privacy, independent of copyright.** Every post is a photograph of a minor's
handwritten work, and some images may carry names or identifying marks. A valid CC BY grant does
not resolve privacy or FERPA-adjacent exposure in a public-facing repository. The record is
explicit that **no agent opened the images**, so this rider is raised structurally, from what the
posts are, not from inspection of what any particular image shows. The standing instruction is not
to reproduce them, and to inspect before any reproduction if that instruction is ever revisited.

**4. The substance is in the comments, and their status is unstated.** The site's design puts the
pedagogical analysis in third-party comment threads. Whether "This work" in the sidebar widget
extends to commenter text is not specified anywhere. Treat commenter text as outside the grant
until someone establishes otherwise.

**5. Cite the archive, not the host.** Any citation must point at a Wayback URL, for example
`https://web.archive.org/web/20260220051333/https://mathmistakes.org/`, or carry an "archived at"
note. This is a mechanical constraint, not a licence constraint, and it is shared with
[[source-engageny-nysed]] for a different reason.

**6. A number discrepancy inside the source, preserved rather than resolved.** The verifying
report's prose says 13 paths returned the identical fatal. The table it prints lists 14 rows. The
two do not agree, the staged extract declines to pick a winner, and this page declines too. Where a
count is needed, write "every path probed". Do not ship either number as the count of paths. Note
that `INVENTORY.md`'s one-line definition for this row does ship "13" without the caveat.

**7. An archived page is not necessarily an archived capture of the site.** Probing `/web/2025/`
and `/web/2026xxxx/` returned a 46,860-byte page that is not a capture at all: HTTP 403 with
`<title>Visitor anti-robot validation</title>`, a WAF challenge the host served to the Internet
Archive crawler in January 2026 and which got archived as content. Reporting that as "the site was
blocked in 2025" would have been wrong in two ways at once. Some 2026 snapshots are WAF pages;
`20260220051333` was verified clean by a zero-count on "Fatal error".

**8. The capture history could not be enumerated, so the outage onset is unknown.** The Wayback CDX
API returned 503 on 4 attempts and then 504. The report attributes that to an Internet Archive
infrastructure problem rather than a block, noting the availability API and individual snapshot
replay both worked throughout. Consequences: the outage is bounded only between a good capture on
**2026-02-20** and the broken fetch on **2026-08-07**, and the HSG-SRT post count is an estimate.
The verdict table says so in those words: the count "roughly 17" is an estimate. Do not harden it.

**9. It is 3.0 Unported, not 3.0 US.** Those are different documents at different URLs, and neither
is 4.0. Worse, the Creative Commons page documenting CC BY 3.0 is itself published under CC BY
**4.0**, so the version numbers are a confusion hazard on the very page you would go to check.

**10. The corpus is finite, static and finished.** The archives dropdown ends **February 2021**,
with 42 pages of posts site-wide. The report's reading is that the blog is finished, not merely
broken. Nothing new will arrive, which makes a pinned Wayback timestamp a durable citation.

**11. The part you may not use is the part carrying the information.** The images are what each
post actually is, and they are served via `i0.wp.com`, a Jetpack or Photon CDN, with originals
under `mathmistakes.org/wp-content/uploads/`, currently reachable only through Wayback. Gotchas 2
and 3 put them out of reach. That is why the ruling is diagnostic reading: the licence would permit
more, and the project's governing ruling and design ruling R11 do not. Read the posts, write original
misconception prose, cite what you read. See [[concept-curate-and-cite]], and
[[practice-place-and-alt-text-a-figure]] for how a figure that **is** cleared gets into a package.

## Related

- [[trap-down-is-not-one-state]] is the decision table this host's fourth failure state produced,
  and the page that keeps a live licence from being recorded as unverifiable.
- [[concept-chain-of-title]] is the general form of gotcha 2: a clean footer on a host that is
  licensing material it never cleared.
- [[license-cc-by]] holds CC BY 3.0 Unported beside CC BY 4.0, including the title and
  adaptation-credit duties that exist only in 3.0.
- [[license-withdrawn-grants]] is the contrast case: here the grant is stable across 12 years, and
  that is what makes it attach to material published in 2014.
- [[evidence-misconception-research-licensing]] is the per-paper record of the rest of the
  misconception literature, and [[evidence-kg-coverage-and-gaps]] is the 0-byte facet that made
  this host necessary in the first place.
- [[practice-cite-without-redistributing]] is how to get full value from material you may read and
  may not reproduce, and [[concept-curate-and-cite]] is the default posture R11 applies here.
- [[concept-third-party-carve-out]] covers the classes of thing sitting outside a work's own grant.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above is a pasted byte, and
  [[trap-compressed-body-grepped-as-text]] is the neighbouring Wayback failure mode where a raw
  archive fetch returns gzip and a grep over it reports a false absence.

## Composes with

- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict,
  and the one whose path-probing and archive fallback steps this host stress-tested.
- [[practice-cite-without-redistributing]] consumes the constructed attribution block above and the
  Wayback-only citation rule into the per-source citation discipline.

## References

Fetched by this project on 2026-08-07:

- `https://mathmistakes.org/` HTTP 200, 1830 bytes, `text/html; charset=UTF-8`. The PHP fatal
  reproduced above, byte-identical on every path probed including `/terms`, `/license` and
  `/wp-json/wp/v2/posts`.
- `https://web.archive.org/web/20260220051333/https://mathmistakes.org/` HTTP 200, 257,612 bytes,
  zero occurrences of "Fatal error". The sidebar CC BY 3.0 widget and the theme footer.
- `http://archive.org/wayback/available?url=mathmistakes.org` returning that snapshot as closest.
- Five individual post captures and one category-page capture, listed in the per-resource table
  above, each carrying the same notice.
- Root captures at 20140517212051, 20160524142902, 20180521035129, 20200518014659 and
  20221207024233, all carrying the same licence string.
- `http://creativecommons.org/licenses/by/3.0/deed.en_US` HTTP 200, redirecting to
  `https://creativecommons.org/licenses/by/3.0/deed.en`.
- `https://web.archive.org/cdx/search/cdx` 503 on 4 attempts then 504. Recorded as an Internet
  Archive infrastructure failure, not a block.

Staged extracts in this wiki:

- `sources/host-math-mistakes.md`, primary, staged 2026-08-08 from a report fetched 2026-08-07. §1
  reachability and the path table, §2 the Wayback recovery and the WAF-challenge trap, §3 the
  licence verbatim and the 12-year snapshot table, §4 the per-resource check, §5 riders 1 to 7, §6
  relevance and the named posts, §7 the citation constraint.
- `sources/cc-by-3-0.md`, primary, fetched 2026-08-08. The CC BY 3.0 Unported deed (HTTP 200, 32052
  bytes) and legal code (HTTP 200, 51333 bytes) staged verbatim, including Sections 3, 4(a) and
  4(b) quoted above.
- `sources/verdict-twelve-host-table.md`, reference. Row 8 and its four riders, §4.8 the
  constructed attribution block, §5 the misconception-research assessment, §6 the CDX gap and the
  two unresolvable questions.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-mathmistakes.md`, the underlying verification report.
- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 R11 and §2 R3.
- the project's governing ruling, which admits this host as diagnostic reading.

Not verified by anyone in this project, and named here so the gap is visible: whether the site
owner had authority to sublicense contributor-submitted photographs, whether any image carries
student-identifying information, whether the widget's "This work" reaches commenter text, the
complete capture history, and the date the outage began.
