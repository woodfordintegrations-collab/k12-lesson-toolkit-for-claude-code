---
title: "tasks.illustrativemathematics.org (the 2016 IM task bank)"
type: source
verdict: quote_sharealike
fetched: 2026-08-08
sources:
  - https://tasks.illustrativemathematics.org/content-standards
  - https://tasks.illustrativemathematics.org/content-standards/HSG/SRT/C/8/tasks/710
  - https://creativecommons.org/licenses/by-nc-sa/4.0/
  - sources/host-im-task-bank.md
  - sources/cc-by-nc-sa-4-0.md
  - sources/host-im-kendall-hunt.md
  - sources/verdict-twelve-host-table.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# tasks.illustrativemathematics.org (the 2016 IM task bank)

## Summary

`tasks.illustrativemathematics.org` serves a frozen 2016 task bank under CC BY-NC-SA 4.0. Verdict:
`quote_sharealike`. It holds 24 tasks on exactly the five HSG-SRT standards this project targets,
which makes it the IM host a builder is most likely to reach for and the one most likely to be
mistaken for the curriculum host beside it.

Three facts have to travel together, because any one alone produces a wrong answer:

1. **The licence permits paraphrase-and-republish.** ShareAlike does not forbid adaptation, it
   prices it. Under CC BY-NC-SA 4.0 you may adapt, and if you Share what you produce, your
   contributions go out under a licence carrying the same elements, which puts NonCommercial on the
   file they land in. See [[license-sharealike]].
2. **What makes this host quote-only here is a project ruling, not the licence.** Design ruling R9
   forecloses the adaptation the licence allows. Anyone who records "the licence bars adaptation"
   has attributed this project's decision to Creative Commons.
3. **Four tasks are cite-only whatever any ruling says.** Tasks 1002, 1009, 916 and 918 state in
   their own commentary that they are adapted from 2012 American Mathematics Competition problems.
   The page asserts the blanket CC footer over them anyway. A licence cannot convey rights the
   licensor does not hold, and this is a rights gap the footer cannot close.

**Resolve the host before the verdict.** One organisation publishes under three grants on three
hosts, and the lesson and task titles are close enough to swap. A numeric task id under
`/content-standards/` is this host and carries ShareAlike. The full 1st-edition curriculum at
`im.kendallhunt.com` is CC BY 4.0 and is the only IM surface cleared for adaptation; see
[[source-im-kendall-hunt]]. The 2nd edition at `accessim.org` is CC BY-NC 4.0; see
[[source-accessim-360]]. This project has recorded errors in both directions, including a design
ruling that named task 1635 as CC BY 4.0 clean when 1635 lives here.

## When to reach for it

Reach for it when you want a task statement, an IM Commentary passage or a worked solution to
**quote** inside your own prose, or to cite as a design reference. The evidence file records the IM
Commentary as the most valuable part of each page for teacher notes. Quoting is unconstrained by
ShareAlike: a quotation set in your own writing with attribution is a use of the work, not an
adaptation of it. See [[concept-cite-quote-adapt]].

Reach for it to settle provenance. If a URL, PDF or citation you are holding carries an IM task id,
this host is where you check which grant attaches to it before it enters a bibliography.

Coverage as recorded by the sweep of all 24 in-scope pages: B.4 has 2 tasks (1095, 1568), B.5 has
11 including the four AMC-derived ones below, C.6 has 2 (1635, 1904), C.7 has 2 (1443, 1902), and
C.8 has 7. **D.9, D.10 and D.11 return 0 tasks each**, so there is no law of sines or cosines here.

Do **not** reach for this host for an adapted through-line. Under R9 the repo writes original
expression from the standard text and takes no paraphrase from any ShareAlike source, so nothing
from these pages may be rewritten into shipped prose. See
[[trap-sharealike-contaminates-by-paraphrase]] for where the line between quoting and adapting
actually falls.

Do not reach for tasks 1002, 1009, 916 or 918 for anything past citation, and do not treat that as
a ShareAlike consequence. It is a chain-of-title consequence, which is a different mechanism with a
different fix. See [[concept-chain-of-title]].

## What its own page says

Every quotation below is transcribed from `sources/host-im-task-bank.md`, which stages an evidence
file whose own method note reads that every quote in it "was read out of a downloaded file, not
from memory". Original fetch date 2026-08-08, server date header recorded verbatim as
`Sat, 08 Aug 2026 01:46:12 GMT`, method `curl` with a browser user agent over raw bytes.

### The footer, which is the entire licensing statement on this host

Raw HTML as served, recorded as identical markup on `/content-standards` and on every task page
checked:

```html
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank"><img src="../assets/cc-88x31.png" style="float: left"></a>
    Typeset May 4, 2016 at 18:58:52. Licensed by <a href="https://www.illustrativemathematics.org" target="_blank">Illustrative Mathematics</a> under a <br>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US" target="_blank">Creative Commons
        Attribution-NonCommercial-ShareAlike 4.0 International License.</a>
```

Rendered sentence, verbatim:

> Typeset May 4, 2016 at 18:58:52. Licensed by Illustrative Mathematics under a
> Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

The sweep covered **all 24 in-scope task pages**, not a sample. Every one returned HTTP 200 and
every one carries that string. No task overrides it. Six pages were additionally opened one by one
and swept for `adapted from`, `courtesy`, `used with permission`, `photo by`, `wikimedia`,
`flickr`, `all rights reserved` and `public domain`: **zero hits**.

`/terms`, `/terms-of-use`, `/copyright`, `/license`, `/about`, `/faq` and `/permissions` all return
404. The evidence file's conclusion, verbatim:

> The CC footer is the *entire* licensing statement available at `tasks.illustrativemathematics.org`.

### The root carries no licence, and a summary layer supplied one anyway

Raw byte counts on the root document, transcribed verbatim:

```
grep -c -i "creative"  im_root.html  -> 0
grep -c -i "copyright" im_root.html  -> 0
grep -c -i "licen"     im_root.html  -> 0
```

The root's visible text ends `... Learn More Privacy Policy | Accessibility Information` and its
`<title>` is `Illustrative Mathematics | Kendall Hunt`. The licence lives one level in, under
`/content-standards`. See [[trap-license-lives-off-the-obvious-page]].

The summary-layer failure recorded on this host, verbatim:

> A first WebFetch of `/` returned the CC sentence anyway — i.e. the summarizing model
> produced text absent from the bytes it was given. Treated as unreliable; all findings
> below come from raw curl output only.

That single event is why this wiki's evidence floor exists. See
[[trap-summary-layer-is-not-evidence]].

### The four tasks that name an upstream the footer does not account for

All four are HSG-SRT.B.5. Upstream statements verbatim from the IM Commentary on each page:

| Task | Upstream, verbatim from the IM Commentary |
|---|---|
| 1002 Bank Shot | "This task was adapted from problem #12 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 1009 Tangent Line to Two Circles | "This task was adapted from problem #19 on the 2012 American Mathematics Competition (AMC) 10B Test." |
| 916 Finding triangle coordinates | "This task was adapted from problem #11 on the 2012 American Mathematics Competition (AMC) 10A Test. In the AMC exam question, the diagram was not given." |
| 918 Slope Criterion for Perpendicular Lines | "This task was adapted from problem #15 on the 2012 American Mathematics Competition (AMC) 10A Test." |

The staged extract records that AMC is run by the MAA, that this host says nothing about the AMC or
MAA rights position, and that the agent did not leave this host to check it, so **the upstream
grant is unverified from here**. The other 20 in-scope tasks state no upstream source.

### What the central IM terms do and do not say about this host

This host has no terms page of its own. IM's central Terms of Use, staged verbatim in
`sources/host-im-kendall-hunt.md` from a fetch of `https://illustrativemathematics.org/terms-of-use/`
on 2026-08-07, open with a scope clause that reads on subdomains:

> Unless otherwise noted on a particular website or service, these central terms and
> conditions of use ("Central Terms" or "Terms") apply to your use of all of the websites that
> the nonprofit corporation Illustrative Mathematics operates. These include
> https://illustrativemathematics.org , https://accessim.org , https://ca.accessim.org/,
> https://im.kendallhunt.com , together with all other subdomains thereof, (collectively, the
> "Websites"). The Terms also apply to all products, information, curriculum, and services
> provided through the Websites.

Neither §7.1 nor §7.2 of that document mentions the task bank. §7.1 grants CC BY 4.0 to the first
edition at `im.kendallhunt.com`; §7.2 grants CC BY-NC 4.0 to v.360 at `accessim.org`. §6 then
reserves everything not expressly granted, verbatim:

> Except as expressly stated in these Terms or in a separate written license agreement, IM
> reserves all rights in and to its intellectual property. No license or right is granted by
> implication, estoppel, or otherwise.

**Read that as this project's own reading, not as IM's statement about this host.** The reading is
that the on-page CC BY-NC-SA footer is the only grant reaching the task bank, and that the two
curriculum grants stop at the two hosts they name. The host agent recorded the question of whether
the parent site's terms supersede or add to this footer as explicitly unverified from its scope,
and no agent has since fetched the parent site with this host in mind.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name it, link it, state which standard it addresses, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | attribution block below; ShareAlike is not triggered |
| Paraphrase and republish: rewrite a task's structure and ship it | by licence yes, **by R9 no** | see below |

### The two different reasons this host is quote-only

Do not merge them. They fail differently and they would be lifted differently.

**Reason one, the licence, applies to everyone.** CC BY-NC-SA 4.0 permits adaptation. Its
ShareAlike section, verbatim from the staged legal code:

> In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the following conditions also apply.
>
> The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.

Two details a page must not lose. The trigger is **Sharing**, not producing, where the deed's
wording reads as attaching on creation. And the obligation attaches to **your contributions**, not
to the whole work you place them in.

**Reason two, the ruling, applies only to this repo.** This project's HS Geometry unit design fixes
the operative posture, verbatim from ruling R9:

> The repo ships CC BY 4.0 and writes from standard text only. No paraphrase from any ShareAlike source, ever.

and, in the same row:

> Quoting is permitted (it does not trigger SA); adaptation is not.

R9 is stricter than the licence. A repository willing to ship NonCommercial could adapt these tasks
lawfully; this one cannot, because its own outbound grant is CC BY 4.0. If R9 were ever revisited,
the licence question would still have to be answered separately, and this host would still be
adaptable only at the price of relicensing whatever it touched.

### Attribution block

No canonical attribution string is published anywhere on this host. This project's block is modelled
on the host's own footer, and the fact that it is modelled rather than mandated is part of the
record:

```
Licensed by Illustrative Mathematics (https://www.illustrativemathematics.org) under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
https://creativecommons.org/licenses/by-nc-sa/4.0/
Task <id> "<title>", https://tasks.illustrativemathematics.org/content-standards/HSG/SRT/<cluster>/<n>/tasks/<id>
Accessed 2026-08-08.
```

Do **not** apply this block to tasks 1002, 1009, 916 or 918 as a basis for reproduction or
adaptation. Those are cite-only.

Under 4.0 the changes-made indication is required whenever you Share, not only when you adapt. The
deed's footnote, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

### What the grant does not reach

- **The four AMC-derived tasks**, for the reason set out above.
- **The photographs on task 1591**, which the evidence file records as served from
  `http://s3.amazonaws.com/illustrativemathematics/images/...` with no credit line and no stated
  upstream. The page licence covers them implicitly and their provenance is unstated. See
  [[concept-third-party-carve-out]].
- **Anything in `grade_HSG.zip`**, the bulk download linked from the domain page. The link was
  recorded, the archive was not downloaded, so whether the bundled files carry the same footer is
  unknown.

Unlike the curriculum hosts, **no trademark terms were found on this host**; the evidence file
searched and recorded none. The IM name and marks are still carved out by the central Terms §7.3,
which is a different document. Do not read the absence of a local trademark notice as a licence to
brand anything.

## Gotchas & constraints

**1. A task id is not a curriculum reference.** The most expensive error on this host is silent.
This project's own design ruling once named IM task 1635 as CC BY 4.0 clean; 1635 is
`/content-standards/HSG/SRT/C/6/tasks/1635` on this host and carries ShareAlike, so it cannot carry
an adapted through-line. The inverse error also happened: an earlier sweep read the task bank's
licence as IM's licence and wrote the whole organisation off, which the wide sweep records verbatim
as "the precise error that caused the earlier sweep to write IM off, and it cost us the single most
useful source in the field".

**2. The four AMC tasks are a rights gap, not a licence term.** IM asserts a blanket footer over
material its own commentary says it adapted from someone else's exam. Nothing on this host mentions
a permission from the MAA, and no agent in this project has asked. The mitigation recorded by the
evidence file is to cite these four, never paraphrase-and-republish them, and if one is wanted as a
model problem, source the AMC original and clear it separately. **This is the one materially open
question on the host**, and closing it requires a host outside the one this evidence covers.

**3. The evidence file disagrees with itself about two task titles, and this page preserves the
disagreement rather than picking a side.** Both conflicts are between the six-page sampling table
and the full task inventory in the same document.

- Task **1591**: the sampling table titles it "How far is the horizon?"; the B.5 list titles it "Is
  this a rectangle?" and gives "How far is the horizon?" to task **651**. The photograph rider is
  recorded against 1591.
- Task **710**: the sampling table titles it "Seven Circles III"; the C.8 list titles it
  "Neglecting the Curvature of the Earth" and gives "Seven Circles III" to task **1638**.

Do not assert either pairing in a bibliography without re-fetching the task page. An attribution
block carries a title, so this is not a cosmetic gap.

**4. A clean fetch of the root returns "unlicensed".** Three counts of zero on the root document,
and a WebFetch that produced the licence sentence regardless. The licence is real and it is one
level in.

**5. NonCommercial rides alongside ShareAlike and is dormant, not absent.** It costs nothing while
nothing is sold and becomes unlicensable the moment something is. The deed's own definition ties it
to intent, verbatim: "A commercial use is one primarily intended for commercial advantage or
monetary compensation." See [[license-noncommercial]].

**6. The bank is frozen, and the freeze is stamped on every page.** "Typeset May 4, 2016". The
evidence file records nothing added in approximately 10 years, with the site chrome refreshed later.
A frozen host is stable to cite and gives no signal about whether the grant is still intended.

**7. The URL scheme changed and the site's own navigation did not keep up.** The live form is
`/content-standards/HSG/SRT/<cluster>/<n>/tasks/<id>`. The legacy `/content-standards/HSG-SRT/...`
and `/illustrations/<id>` forms are 404. The domain page's own "View all HSG-SRT Tasks" link is
404. `.html` suffixed paths return 308 Permanent Redirect to the extensionless form. Every one of
those failures was discriminated explicitly as a genuine origin 404 with no bot block anywhere,
which is what stops a broken internal link being written up as an unreachable host. See
[[trap-down-is-not-one-state]].

**8. `robots.txt` reserves nothing, despite appearances.** It returns 200 at 1248 bytes and is only
the Cloudflare content-signals explanatory comment. No `User-agent` rule, no `Content-Signal` value,
so no `ai-train=no` or `ai-input=no` restriction is expressed. It carries a boilerplate EU DSM
Article 4 reservation notice, but with no signal set the evidence file records that nothing is being
reserved by it.

**9. The census is complete about the footer and about nothing else.** All 24 in-scope pages were
fetched and byte-matched, which is rare in this corpus and makes the licence finding a census rather
than a sample. It says nothing about the other clusters on the host, the zip contents, or the
images.

## Related

- [[source-im-kendall-hunt]] is the 1st-edition curriculum under CC BY 4.0, the only IM host cleared
  for adaptation, and the host this one is most often confused with.
- [[source-accessim-360]] is the 2nd edition under CC BY-NC 4.0, the third IM grant.
- [[license-sharealike]] holds the SA rider across every host in this corpus that carries it, at
  which version, and the project rule that is stricter than any of them.
- [[license-noncommercial]] holds the NC rider that rides beside SA here.
- [[license-cc-by]] is the plain-attribution regime this repo itself ships under, and therefore the
  reason a ShareAlike derivative cannot be mixed into it.
- [[concept-cite-quote-adapt]] is the three-operation split this page's verdict table applies.
- [[concept-chain-of-title]] is the mechanism behind the four AMC tasks: a host licensing material
  it may not have cleared.
- [[concept-third-party-carve-out]] covers the unattributed photographs on task 1591.
- [[trap-sharealike-contaminates-by-paraphrase]] is the working test for when a rewrite has crossed
  from use into adaptation.
- [[trap-summary-layer-is-not-evidence]] is the failure this host produced and the reason every
  quotation above is a pasted byte.
- [[trap-license-lives-off-the-obvious-page]] is the root-carries-nothing pattern, of which this
  host is one of three instances.
- [[trap-down-is-not-one-state]] is the failure-mode discrimination that records this host's dead
  paths as genuine origin 404s rather than as a block.

## Composes with

- [[practice-cite-without-redistributing]] is the procedure this host is run through in practice:
  everything on it is quotable, none of it is adaptable here, and the value is extracted by citation
  and quotation.
- [[practice-assemble-an-attribution-block]] consumes the block above, and is where the per-task
  title and id are resolved, including the two unresolved title conflicts in gotcha 3.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that produced this verdict,
  and the census of all 24 pages is what it looks like when it is run to completion.

## References

Host pages, fetched by this project on 2026-08-08:

- `https://tasks.illustrativemathematics.org/content-standards` HTTP 200. The task-bank entry point
  and the licence footer, byte-matched against all 24 in-scope task pages.
- `https://tasks.illustrativemathematics.org/content-standards/HSG/SRT/C/8/tasks/710` HTTP 200. An
  individual task page under HSG-SRT.C.8, establishing the live URL scheme and confirming no
  per-task override.
- `https://tasks.illustrativemathematics.org/` HTTP 200. The root, whose three licence-keyword greps
  all return zero.
- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, fetched 2026-08-07, header
  "Effective as of May 21, 2026". The scope clause, §6, §7.1 and §7.2, quoted here from a staged
  extract rather than from any fetch made for this host.
- `https://creativecommons.org/licenses/by-nc-sa/4.0/` HTTP 200, 37346 bytes, and its
  `legalcode.en` HTTP 200, 53058 bytes. The deed and legal code behind the ShareAlike quotations.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-im-task-bank.md`, primary. Reachability, the byte-level footer, the root-grep
  counts, the summary-layer failure, the four AMC admissions, the 24-task inventory, the empty D.9
  to D.11 clusters, and the two internal title conflicts.
- `sources/cc-by-nc-sa-4-0.md`, primary. Deed and legal code verbatim.
- `sources/host-im-kendall-hunt.md`, primary. The central IM Terms.
- `sources/verdict-twelve-host-table.md`, reference. Row 6, §2 verdict key, §3 correction 5, §4.5.
- `sources/verdict-wide-sweep.md`, reference. The write-IM-off error, verbatim.

This project's own working files, cited as this project's measurement and not as any outside party's
statement: `Projects/HS Geometry/sources/license-im-tasks.md`, the underlying fetch report, and
`Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 ruling R9, quoted above.
