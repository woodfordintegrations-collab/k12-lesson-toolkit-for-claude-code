---
title: Build a source table with verbatim evidence
type: practice
sources:
  - sources/host-im-task-bank.md
  - sources/host-achieve-the-core.md
  - sources/host-open-middle.md
  - sources/host-math-mistakes.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# Build a source table with verbatim evidence

## Summary

The fetch-and-record procedure that turns a host into a defensible rights verdict: raw bytes rather
than a summarizing layer, HTTP status and fetch date on every claim, a path probe for the terms page,
existence tested by byte-diff rather than by status code, an explicit unverified column, and a
re-verification trigger before publication.

The bar is not "did you find the licence". It is: **can someone who was not there re-run your work
and land on the same verdict?**

Two failures this procedure is built around, both of which happened in this project and neither of
which announced itself:

1. **A WebFetch summary returned a licence sentence that was not present in the bytes of the document
   it was given.** It happened to be the correct licence. It was not evidence.
2. **A grep of a Wayback `id_` capture returned zero matches because the body was gzip.** The agent
   nearly reported a public-domain dedication as withdrawn four months before it actually was.
   Re-fetched with `--compressed`, the string was there.

Neither error is detectable from its output. Both are prevented by method, not by care.

## When to reach for it

Reach for this page before the first fetch on a new host, and again before a repository that cites
that host is published. The second exists because grants move: this project measured two withdrawals
inside six months in one twelve-host corpus.

Reach for it when a host looks dead, blocked, empty or unlicensed. Four of those five words name
different states with different remedies, and the fifth is usually wrong.

Do not reach for this page for what the verdict then permits: the three-operation split and the
per-host mechanics of using a source you may not reproduce are at
[[practice-cite-without-redistributing]]. Do not reach for it for the shipped credit line, which is
[[practice-assemble-an-attribution-block]].

## How it works

**The column set is the contract.** This project's twelve-host sweep fixed its row as: Host,
Reachable, Licence (verified), Safe to quote, Riders, Relevance, Fetch date. Dropping "Fetch date"
turns a verdict into a memory. Dropping "Riders" loses the trademark carve-outs, third-party images
and version numbers, which is where most of the real constraint lives. Dropping "Reachable" hides the
difference between a source that is gone and one that refused your user agent.

**Verbatim beats summary, always.** The rule this project ended up with, recorded verbatim in the
task-bank report:

> A first WebFetch of `/` returned the CC sentence anyway — i.e. the summarizing model
> produced text absent from the bytes it was given. Treated as unreliable; all findings
> below come from raw curl output only.

So a row rests on a pasted sentence from bytes you fetched, with its URL and HTTP status, never on a
description of what a page says. See [[trap-summary-layer-is-not-evidence]].

**Status codes are a signal, not a fact.** Measured on four hosts in this corpus, HTTP 200 meant four
different things: a real page, a soft 404 from a single-page app, a soft 404 from a framework
catch-all route, and a PHP fatal error served as the entire body.

**Absence of a licence is a finding, and it is not absence of evidence.** "No notice on this page" is
a measurement. "No notice on this host" needs the path probe. "No grant" needs both plus the archive.
Say which one you did.

## In practice

### Step 1. Fetch raw, with a browser user agent, and keep the bytes

Use a client that returns bytes, not a summary. Save the response; every later claim gets grepped out
of the saved file and the grep count goes in the record beside the claim.

**Trap here, before you have looked at anything.** A summarizing layer can hand you a sentence the
document does not contain. The task-bank report's counter-evidence, transcribed verbatim, is the
shape of what a real negative looks like:

```
grep -c -i "creative"  im_root.html  -> 0
grep -c -i "copyright" im_root.html  -> 0
grep -c -i "licen"     im_root.html  -> 0
```

Three counts, named file, all zero. That is a measurement. "The page has no licence text" is not.

**Second trap at the same step: never grep a body that may be compressed.** The method warning
recorded with the Achieve the Core finding, verbatim:

> METHOD WARNING recorded: my first pass at this snapshot used wayback `id_` raw mode WITHOUT
> `--compressed`. curl returned gzip bytes; grep found 0 matches; I nearly reported "CC0 already
> gone by April 2026". That was an artifact of binary, not a finding. Re-fetched with --compressed
> -> 1 match. Never grep a possibly-compressed body.

The same near-miss happened independently on Open Middle's 2026-03-03 snapshot, where the first pass
appeared to show no footer at all. Two agents, two hosts, one artifact. See
[[trap-compressed-body-grepped-as-text]].

### Step 2. Classify reachability, and name the state rather than the outcome

"The source is unavailable" is not a row entry. These are, each one measured somewhere in this
corpus:

| State | Signature measured here |
|---|---|
| Live, uniform | HTTP 200 on every path tried |
| Bot-blocked by user agent | HTTP 406 on the default UA, HTTP 200 and 100,227 bytes on a browser UA |
| Bot-blocked by JS challenge | HTTP 403 with a body reading "Enable JavaScript and cookies to continue" |
| Certificate expired | `curl (60)` on https, with the apex separately NXDOMAIN at `curl (6)` |
| TLS handshake failure | `handshake_failure` on three independent stacks, clean control set the same minute |
| Soft 404, single-page app | every unknown path returns a byte-identical 140,749-byte homepage shell |
| Soft 404, framework catch-all | HTTP 200 for `/zzz-definitely-not-a-real-page-9876` |
| Live server, dead application | HTTP 200 with a 1,830-byte PHP fatal error as the entire body |
| Server-side timeout | `curl (28)` on one query path while plain page loads return in 0.49 to 0.59 s |
| Genuine origin 404 | a real 404, distinguishable because other paths on the host resolve |

**Trap here: the remedy differs by state, and picking the wrong one loses the host.** A bot-blocked
host is fetched with a browser UA. A dead-application host is fetched from the archive. A TLS-failed
host is fetched over plain http and cited that way. A soft-404 host cannot be probed by status at
all. Reading any of these as "gone" writes the source out of the build, and this project did exactly
that once, recording a host as "HTTP 000, does not resolve" when the cause was an expired
certificate. See [[trap-down-is-not-one-state]].

Record it when the host contradicts itself: Open Middle's `robots.txt` returns 200 and does not
exclude general crawlers while the server 406s non-browser agents, so the block sits at the server or
WAF layer against the site's own published crawl policy.

### Step 3. Probe the policy paths, and probe them by name

Try at minimum `/terms`, `/terms-of-use`, `/copyright`, `/permissions`, `/license`, `/about`, `/faq`,
and record every status. This is the step that decides whether "no licence page" is a claim you can
make.

Measured outcomes worth knowing first: on the IM task bank all seven returned genuine 404s and the CC
footer is the entire licensing statement available on that host. On MARS, fourteen probed paths
returned 404 and the About page turned out to be `/background.php`. On Open Middle every policy slug
returned the soft-404 template, and three independent checks confirmed no policy document has ever
existed: the page sitemap enumerates five pages, the site's own search returns nothing, and Wayback
CDX shows zero captures ever for any of those paths.

**Trap here: one wrong path can manufacture a false negative that survives for months.** On
achievethecore.org, `/page/terms-of-use` is a soft 404 while `/terms-of-use` is 93,954 bytes of real
content, and the evidence file records that this is precisely why an earlier fetch "found no
licensing statement": it had read the homepage.

**And the mirror-image trap: a clean 404 on every obvious path does not mean there is no grant.** On
im.kendallhunt.com the same probe returns 404 across the board while the grant is real, sitting
off-host in the operator's central terms. See [[trap-license-lives-off-the-obvious-page]].

### Step 4. Test existence by byte-diff, never by status

On a soft-404 host, compare the response against the known shell. Achieve the Core's shell is 140,749
bytes and `/ccpd` is byte-identical to it, which is how the removal of the Permissions page was
established; real pages on the same host measured 93,954, 110,460, 107,723 and 107,956 bytes.
Corroborate with the markup where it says something. That host's footer carries, twice:

```
<!-- <li><a href="/ccpd">Permissions</a></li> -->
```

A commented-out link is a deliberate act, and it distinguishes a removed page from a broken one.

**Trap here: two agents can measure the same shell at different sizes.** A second staged extract
records that homepage shell as 137,828 bytes against this file's 140,749. Both are reproduced as
written in the staged corpus and neither was reconciled. Carry the discrepancy; do not pick a winner
without a fresh fetch. See [[trap-soft-404-status-proves-nothing]].

### Step 5. Open the artifact as well as the page, because they disagree

A grant on a web page does not travel with the file that page serves. Measured on MARS,
`hopewell_geometry.pdf` carries on both pages, verbatim, as a running footer:

> Copyright © 2011 by Mathematics Assessment
> Resource Service. All rights reserved.

while the HTML page linking it grants CC BY-NC-ND 3.0, and the rubric PDF for the same task carries
no notice at all. So the evidence for the grant on that file is the page, and the page is what gets
archived with its fetch date.

**Trap here: a PDF can hit your keyword grep for a reason unrelated to its licence.** From the
Achieve the Core sampling, verbatim:

> (The only "All Rights Reserved" strings are EMBEDDED FONT notices - Microsoft Calibri - NOT a
>  content licence. Do not mistake font metadata for a grant.)

Check what a match is attached to before it enters a row. See
[[trap-font-notice-is-not-a-content-license]].

**Second trap: an artifact can state two versions of its own licence.** One IM-authored PDF hosted on
Achieve the Core names a "4.0 International" licence at line 149 and a "3.0 Unported" one at line
173. The evidence file calls the version "genuinely ambiguous on the face of the document"
and does not resolve it. Record both.

### Step 6. Date the window when a grant has moved, and bound it rather than guessing

When the archive shows a change, give the two adjacent captures and let the window stand. Measured:

- Achieve the Core's `/ccpd` served the blanket dedication continuously at snapshots dated
  2016-03-03, 2017-07-22, 2020-04-30, 2022-01-03, 2024-03-23, 2026-01-11 and 2026-04-25, the last
  being `20260425161111`. Live on 2026-08-08 the path is the homepage shell and "Public Domain
  Dedication" occurs 0 times. **Removal window: between 2026-04-25 and 2026-08-08.**
- Open Middle's footer carried CC BY-NC-SA 4.0 in the capture of **2026-02-16** and did not in the
  capture of **2026-03-03**, and Wayback captured nothing between those dates. A separate, later
  event, the rights-holder change to Glenrock Consulting, LLC, falls between 2026-03-03 and
  2026-05-12.

**Trap here: an archived page is not necessarily an archived capture of the site.** Probing
mathmistakes.org at `/web/2025/` returned a 46,860-byte page that is not a capture: it is HTTP 403
with the title "Visitor anti-robot validation", replayed from snapshot `20260104191043`. It is the
host's own anti-bot challenge, served to the Internet Archive crawler and archived as content.
Reporting it as "the site was blocked in 2025" would have been wrong twice over.

Record when the archive itself is what failed. On the same host the CDX API returned 503 four times
and then 504, so the capture history could not be enumerated and the outage onset could not be
pinned. That is Internet Archive infrastructure failing, not a block: the availability API and
snapshot replay both worked throughout.

### Step 7. Write the unverified column, and say what would close each entry

An honest gap is a finished row. A guess is not. Separate two lists, because a reader needs to know
which gaps are laziness and which are law.

- **Closeable by a further fetch.** The IM image attribution index, where all eight guessed paths 404,
  leaving every IM figure in the target units uncleared; the live text of the CCSS public license,
  where the host is a Cloudflare 403 to every client tried and the only readable copy is a Wayback
  snapshot dated 2025-12-21; the contents of a bulk task archive, linked but never downloaded.
- **Not closeable by fetching.** Whether material published under a withdrawn public-domain dedication
  remains dedicated; whether a site owner had authority to sublicense contributor-submitted
  photographs; whether short attributed quotation from a NoDerivatives source is acceptable. These go
  to counsel, and this project's record says so rather than answering them.

### Step 8. State the sampling limit, then set the re-verification trigger

"The licence is uniform across this host" means different things depending on how much of the host
you saw. This project's own limits, recorded plainly: im.kendallhunt.com, 8 curriculum pages of
several thousand, with the notice byte-identical across all 7 high-school pages sampled, which is
strong evidence of a template rather than proof of a per-page decision; map.mathshell.org, 5 of
roughly 100 Classroom Challenges and 4 of 94 summative tasks; achievethecore.org, 3 resource pages
and 2 PDFs, so "varies per resource" is established by counterexample and not by census; ERIC, 7
PDFs, whose 1 CC BY, 2 restrictive, 4 silent split measures the sample and not the population.

The one closed claim in the corpus is tasks.illustrativemathematics.org: all 24 in-scope task pages
fetched individually, a full sweep, with the footer confirmed by byte match on every one. That is
what a closed claim looks like. The others are open and their rows say so.

Then name the rows to re-pull and the event that fires it. This project's trigger names four hosts
and fires before the repository is published, on the ground that three grants in the corpus changed
within the six months before the fetch and one operator's terms reserve revision at sole discretion.
Record the new fetch date in the attribution block when it fires.

## Gotchas & constraints

**1. Preserve discrepancies rather than resolving them.** Three sit inside this project's own record
and all three are carried unreconciled: a page-footer count given as 68 of 70 in one section and 63
of 69 in another; a report whose prose says 13 probed paths while its own table lists 14 rows; and
the two homepage-shell byte counts above. A table that silently picks one number has manufactured a
fact.

**2. A blanket footer over acknowledged third-party content is an unresolved question, not a grant.**
Four tasks in the IM task bank carry the site's CC BY-NC-SA footer while their own commentary states,
verbatim, "This task was adapted from problem #12 on the 2012 American Mathematics Competition (AMC)
10B Test." The host says nothing about the upstream position and the fetching agent did not leave the
host to check, so the row records it as unverified. A grant cannot convey rights the grantor does not
hold. See [[concept-chain-of-title]].

**3. Do not build a table from a summarizing layer even once.** The failure is not that summaries are
often wrong. It is that the one recorded instance produced the *correct* licence, so nothing flagged
it. A method that is right by luck is indistinguishable from one that is right by construction, until
it is not.

**4. Scratchpad hygiene is part of the method when agents run in parallel.** Two host reports in this
corpus record catching another agent's files in a shared scratchpad: an Open Middle page picked up by
a glob during the mathmistakes run, and five IM response files present during the Achieve the Core
run. Both agents excluded them explicitly and said so. This class of contamination produces a licence
finding attributed to the wrong host, and nothing downstream would catch it.

**5. The finished table is secondary evidence about itself.** It is this project's own adjudication,
not a rights-holder's statement. What is authoritative is the pasted host sentence it carries. Write
"this project's sweep recorded", never "the verdict table says the host is CC BY".

**6. Registration-gated material is out of scope unless the project decides otherwise.** No agent in
this corpus registered and none solicited or used a credential, so nothing behind a login wall is in
any row. That is a scope boundary and it belongs in the table.

## Related

- [[trap-summary-layer-is-not-evidence]] is the worked instance behind step 1.
- [[trap-compressed-body-grepped-as-text]] is the gzip artifact that nearly produced two false
  findings on two hosts.
- [[trap-down-is-not-one-state]] is step 2's taxonomy and why one "unavailable" label loses sources.
- [[trap-soft-404-status-proves-nothing]] is step 4, where status stops being an existence signal.
- [[trap-license-lives-off-the-obvious-page]] is step 3's mirror image: a clean 404 on the terms path
  with a real grant one host away.
- [[trap-font-notice-is-not-a-content-license]] is the embedded-metadata false positive in step 5.
- [[trap-license-withdrawn-after-citation]] is why step 6 exists and what a dated citation protects.
- [[license-withdrawn-grants]] is the dated register of the two withdrawals measured here.
- [[concept-chain-of-title]] is gotcha 2: what a blanket footer can and cannot convey.
- [[source-achieve-the-core-sap]], [[source-open-middle]], [[source-im-task-bank]] and
  [[source-math-mistakes]] are finished rows this procedure produced.

## Composes with

- [[practice-cite-without-redistributing]] takes the finished verdict and turns it into what may
  actually be done with the host, including the mechanical citation rules a `cite_only` row implies.
- [[practice-assemble-an-attribution-block]] consumes the used-source subset into the shipped licence
  and attribution file, and re-runs step 8's trigger before publication.

## References

Staged extracts in this wiki, staged 2026-08-08 unless noted:

- `sources/host-im-task-bank.md`, primary. §1 reachability and failure-mode discrimination; §2 the
  root-carries-no-licence measurement with its three grep counts and the summary-layer failure
  verbatim; §4 the four AMC-derived tasks; §7 what the report records as unverified.
- `sources/host-achieve-the-core.md`, primary. §2 the single-page-app soft 404, the byte sizes and the
  commented-out footer link; §4b the dated removal window; §4c the compressed-body method warning
  verbatim; §5 the per-resource samples, the two-version PDF and the Calibri false positive.
- `sources/host-open-middle.md`, primary. §1 the 406-versus-200 block and the robots.txt
  contradiction; §2 the three confirmations that no policy document exists; §5 the dated Wayback
  footer table and the gzip near-miss; §8 the gaps carried forward as not-findings.
- `sources/host-math-mistakes.md`, staged 2026-08-07, primary. §1 the live-server dead-application
  state and the path probe; §2 the archived WAF challenge and the CDX 503/504 failure; §3 the
  twelve-year snapshot stability table.
- `sources/verdict-twelve-host-table.md`, reference. §1 the column set; §6 what remains unverified,
  split into closeable and legal, plus the sampling limits and the re-verification trigger. Cited as
  this project's own adjudication, never as a rights-holder's statement.

Those extracts normalise twelve per-host verification reports under
`hs-geometry-similarity-trig/sources/`, each written by a separate
agent on 2026-08-07 or 2026-08-08, each recording its own fetch dates and HTTP statuses inline.
