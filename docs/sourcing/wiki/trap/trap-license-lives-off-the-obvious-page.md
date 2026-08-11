---
title: "The licence does not live on the obvious page"
type: trap
sources:
  - https://im.kendallhunt.com/
  - https://illustrativemathematics.org/terms-of-use/
  - https://accessim.org/
  - https://tasks.illustrativemathematics.org/
  - http://www.mathematicsvisionproject.org/resources.html
  - https://achievethecore.org/terms-of-use
  - sources/host-im-kendall-hunt.md
  - sources/host-accessim-360.md
  - sources/host-im-task-bank.md
  - sources/host-math-vision-project.md
  - sources/host-achieve-the-core.md
  - sources/host-open-middle.md
  - sources/host-mars-map.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# The licence does not live on the obvious page

## Summary

A clean, successful, unblocked fetch of a host's root returns "no licence found" on four of the
hosts in this corpus, and on all four the grant exists. The failure has no error state: HTTP 200,
no bot block, no TLS problem, a real document, and a grep that honestly reports zero.

This project made the error and wrote it into its own governing design. Recorded verbatim from
`specs/2026-08-07-srt-unit-design.md` §3:

> im.kendallhunt.com carries no license statement on its landing page. The CC BY 4.0 claim for that
> host is currently unverified.

Both sentences are true as written. The conclusion drawn from them was wrong. The grant was live
the whole time, in a terms document on a different domain, and confirmed on every deep curriculum
page of the host itself. This project's adjudication later called it, verbatim, "the worked
instance of a grant that does not live on the obvious page."

The rule: **a root fetch is a place you looked, not a verdict.** A host is recorded as
unlicensed only after the four locations below have been checked and the search can be shown to
have been exhaustive.

## When to reach for it

Reach for it before writing "no licence found", "unlicensed", or "unverified" against any host.
That sentence is the output this page exists to block until the work behind it is done.

Reach for it when the root fetch is clean and short. im.kendallhunt.com's entire root footer is
`Privacy Policy | Accessibility Information`, and tasks.illustrativemathematics.org's root visible
text ends `... Learn More Privacy Policy | Accessibility Information`. That is a marketing
template, and it says nothing about the content tree behind it.

Reach for it when a probe of `/terms`, `/license`, `/copyright` and `/permissions` returns 404
across the board. On im.kendallhunt.com every one was a genuine 404 while the grant existed
off-host the entire time; a same-host probe is structurally incapable of finding it.

Do not reach for this page to explain a fetch that failed, or one whose 200 is meaningless. Those
are [[trap-down-is-not-one-state]] and [[trap-soft-404-status-proves-nothing]], and both must be
settled before this page's search means anything.

## How it works

There are four places a grant lives in this corpus, and the root landing page is the least likely
of them. Search in this order.

**1. The root and its policy paths.** Cheap, and in this corpus usually empty. Measured:
im.kendallhunt.com's root returned zero matches for
`creative commons|CC BY|licens|copyright|attribution|all rights reserved` across 27,884 bytes.
tasks.illustrativemathematics.org's root returned `grep -c -i` counts of 0 for "creative", 0 for
"copyright" and 0 for "licen". accessim.org's homepage and privacy policy return zero licence hits
on a per-page audit where every curriculum page returns exactly one.

**2. Deep content pages, one or more levels in.** Where four of these hosts put it, by template
decision rather than oversight. On im.kendallhunt.com the notice is injected into the same
`<footer class="im-c-footer">` element as the root's, but only in the curriculum-content templates.
accessim.org has the same shape, with the consequence recorded verbatim:

> Anyone checking only `accessim.org/` would conclude the site is unlicensed. It isn't; you have to
> be on a curriculum page.

On tasks.illustrativemathematics.org the licence sits under `/content-standards`, one level in. On
map.mathshell.org it appears only on individual resource pages and never on the browse indexes:
`/lessons.php`, `/tasks.php` and `/stds.php` all return zero hits for "creativecommons".

**3. Off-host, in the operator's central terms, with a scope clause that names this host.** This is
the location a same-host search cannot reach at all. Illustrative Mathematics' Terms of Use scope
clause, verbatim:

> Unless otherwise noted on a particular website or service, these central terms and
> conditions of use ("Central Terms" or "Terms") apply to your use of all of the websites that
> the nonprofit corporation Illustrative Mathematics operates. These include
> https://illustrativemathematics.org , https://accessim.org , https://ca.accessim.org/,
> https://im.kendallhunt.com , together with all other subdomains thereof, (collectively, the
> "Websites"). The Terms also apply to all products, information, curriculum, and services
> provided through the Websites.

Section 7.1 of that document is the operative CC BY 4.0 grant for im.kendallhunt.com and §7.2 is a
different grant for a different edition on a different host. Neither sentence appears anywhere on
the host they govern.

**4. Inside the artifact.** MVP's instructional modules carry `This work is licensed under the
Creative Commons Attribution CC BY 4.0` on the cover and repeat it in a per-page footer; the
staged samples record 63 of 69, 97 of 108 and 68 of 70 pages. MARS's teacher guide states
CC BY-NC-ND 3.0 twice. The file and the page that serves it can disagree, and on both hosts they
do.

## In practice

**The discovery aids that actually worked**, all recorded in the staged extracts:

- `/sitemap.xml`. MVP's licence lives on deep curriculum pages unlinked from navigation, and the
  sitemap is how they were found. The nav-level site is now a redirect shell whose `/resources.html`
  and `/curriculum.html` say only that Open Up Resources is "partnered with us" and that you "will
  need to register and create an educator account to have access."
- `page-sitemap.xml`, which on openmiddle.com enumerated the complete page list and proved no
  policy page exists.
- Wayback CDX over the host's full history. On MVP it returned zero URLs matching
  `licen|terms|copyright|permission|faq|legal`, which is how "no such page ever existed" became
  sayable rather than assumed.
- The host's own site search. openmiddle.com's `/?s=copyright`, `?s=license` and `?s=permission`
  returned zero content results.

**What an exhaustive negative looks like.** openmiddle.com is the host where the answer really is
"the footer is all there is", and the report earned that conclusion three independent ways:
sitemap enumeration, site search, and Wayback CDX with control queries against the root and
`/similar-triangles/` that returned capture rows and proved the endpoint working. That is the
standard. A negative supported only by a root fetch and a handful of 404s is not the same claim.

**The near-miss path shapes.** On achievethecore.org, `/page/terms-of-use` is a soft-404 shell and
`/terms-of-use` is 93,954 bytes of real content. The staged extract records that the shell is the
reason an earlier fetch "found no licensing statement": it was reading the homepage. One path
segment separates a real terms page from a confident false negative.

## Gotchas & constraints

**1. The corporate root of the same brand is a different rights surface from the terms document it
hosts.** illustrativemathematics.org's own footer reads, verbatim: "All products and services are
offered throughout the United States. Content on this page is licensed. © 2026, Illustrative
Mathematics, all rights reserved." That is the marketing site's posture, and it is not the grant.
The grant is a separate document at `/terms-of-use/` whose scope clause names the content hosts.
Reading the corporate footer as the governing licence gets the answer exactly backwards.

**2. Brand in the URL is not host.** `curriculum.illustrativemathematics.org` 301s to
im.kendallhunt.com and is the same site. `k12.kendallhunt.com` is a print and distribution partner
whose footer is all rights reserved and is not a resource host at all. Resolve the host you landed
on before attaching any verdict, per [[source-im-kendall-hunt]].

**3. A deep grant is not automatically a site-wide grant.** map.mathshell.org publishes four
different regimes on one host: NoDerivatives on Classroom Challenges and Summative Tasks,
ShareAlike on the PD Modules, nothing at all on TRU Math, and a bare copyright assertion in the
global footer. Its own homepage sidebox says so, verbatim: "Precise terms vary between materials."
Finding one deep notice tells you about that resource family and no other.

**4. Depth can produce a conflict rather than an answer.** MVP's `/secondary-mathematics-ii.html`
claims CC BY-NC-SA over files whose covers and page footers say CC BY 4.0, and its text says
"4.0 Unported" while its own hyperlink points at `by-nc-sa/3.0`. MARS's summative task PDF carries
an all-rights-reserved running footer while the page linking it grants CC BY-NC-ND 3.0. Record both
readings and say which you rely on; do not average them.

**5. A 404 sweep and a soft-404 sweep are different measurements.** On im.kendallhunt.com the
policy-path 404s are genuine. On accessim.org the same paths return HTTP 200 at roughly 1,485,7xx
bytes each and none of those pages exist. Establish which regime a host is in before reading its
path probes at all. See [[trap-soft-404-status-proves-nothing]].

**6. The first fetch of this class here was rescued by a summarizing layer telling the truth, which
is not a repeatable defence.** A WebFetch of the task bank root returned the CC BY-NC-SA sentence
while the root's bytes contained zero licence text. It happened to name the host's actual licence.
It was not evidence, and the licence was still one level in. See
[[trap-summary-layer-is-not-evidence]].

**7. This page raises the cost of a negative finding on purpose.** Four locations, a discovery-aid
sweep and a control-checked archive query is a lot of work to record "nothing here". It is the
correct amount, because the cheap version cost this project its strongest source until it was
corrected.

## Related

- [[source-im-kendall-hunt]] is the worked instance: empty root, genuine 404 sweep, grant off-host
  in §7.1 and on every deep curriculum footer.
- [[source-accessim-360]] is the host where the root is empty and the path probes lie, so this
  page's search and the soft-404 test are both needed at once.
- [[source-im-task-bank]] is the host whose licence sits exactly one level in, under
  `/content-standards`, behind a root that markets a different company.
- [[source-math-vision-project]] is the host with no licence page in its recorded history, where
  the grant survives on nav-delinked deep pages and inside the PDFs.
- [[source-achieve-the-core-sap]] is where a near-miss path shape produced the false negative.
- [[source-open-middle]] is where "the footer is all there is" is correct, and the model for what
  an exhaustive negative has to show.
- [[source-mars-map]] publishes four regimes on one host and is the reason a deep grant does not
  generalise.
- [[trap-soft-404-status-proves-nothing]] and [[trap-down-is-not-one-state]] must both be settled
  first, or this page's path probes are meaningless.
- [[trap-summary-layer-is-not-evidence]] is why the deep notice gets pasted from raw bytes once
  found.
- [[license-unmarked-silence]] is where a host lands when the full search genuinely comes back
  empty, which is a real outcome rather than a failure of the search.

## Composes with

- [[practice-build-a-source-table]] carries the path-probing and soft-404 steps this page's search
  belongs inside, and its explicit unverified column is where a host goes when the four locations
  have been checked and the answer is still not settled.
- [[practice-assemble-an-attribution-block]] is downstream: the notice you find deep is the one the
  credit line has to match, and on im.kendallhunt.com which deep page you found it on decides which
  of two attribution strings applies.

## References

Host fetches by this project, 2026-08-07 for the Illustrative Mathematics hosts and 2026-08-08 for
the rest:

- `https://im.kendallhunt.com/` HTTP 200. Root footer entire text
  `Privacy Policy | Accessibility Information`; zero grep matches across 27,884 bytes;
  `/terms`, `/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/about` and `/faq` all 404;
  `/privacy` and `/accessibility` 200 with no licence text.
- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, header "Effective as of May 21,
  2026". The scope clause quoted above, §7.1 the operative grant, §7.2 a different grant for the
  second edition.
- `https://accessim.org/` HTTP 200, and `https://tasks.illustrativemathematics.org/` HTTP 200 with
  root `<title>` `Illustrative Mathematics | Kendall Hunt`. Both roots licence-free; both grants one
  or more levels in.
- `http://www.mathematicsvisionproject.org/resources.html` and `/curriculum.html` HTTP 200, the
  redirect-shell text quoted above. Note the scheme: this host's https fails with a TLS
  handshake_failure on three independent stacks, so an https URL must not be cited.
- `https://achievethecore.org/terms-of-use` HTTP 200, 93,954 bytes of real content, against
  `/page/terms-of-use`, the 140,749-byte homepage shell.
- `https://map.mathshell.org/lessons.php`, `/tasks.php` and `/stds.php` HTTP 200, zero hits for
  "creativecommons" on each.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-im-kendall-hunt.md`, primary. §2 the root measurement and template mechanism, §6
  the off-host terms document and its scope clause.
- `sources/host-accessim-360.md`, primary. §4 the per-page audit and the verbatim consequence.
- `sources/host-im-task-bank.md`, primary. §1 reachability, §2 the root grep counts.
- `sources/host-math-vision-project.md`, primary. §2 the absent licence page and the Wayback CDX
  negative, §3 the deep-page grants, §4 the page-versus-file conflict.
- `sources/host-achieve-the-core.md`, primary. §2 the shell-versus-real terms path.
- `sources/host-open-middle.md`, primary. §2 the three independent confirmations of absence.
- `sources/host-mars-map.md`, primary. §2 the fourteen 404s, §3 the per-resource grants and the
  empty browse indexes.
- `sources/verdict-twelve-host-table.md`, reference. Row 1, where this project's own adjudication
  records the 27,884-byte measurement and names this the worked instance.

This project's own working file, cited as this project's record rather than any outside party's
statement, and quoted as transcribed in this wiki's `INVENTORY.md`:
`Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md` §3, where the false belief above is
written into the governing design, corrected later at `verdict-twelve-host-table.md` §3
correction 1.
