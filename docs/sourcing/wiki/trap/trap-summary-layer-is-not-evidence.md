---
title: A summary layer is not evidence
type: trap
sources:
  - sources/host-im-task-bank.md
  - sources/host-eric.md
  - sources/host-accessim-360.md
  - sources/host-achieve-the-core.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# A summary layer is not evidence

## Summary

**What the broken case looks like:** a correct licence sentence, correctly attributed, in a
report that reads like every other report. A WebFetch of the `tasks.illustrativemathematics.org`
root returned the CC BY-NC-SA sentence. Raw byte counts on that same root document, transcribed
verbatim from the evidence file:

```
grep -c -i "creative"  im_root.html  -> 0
grep -c -i "copyright" im_root.html  -> 0
grep -c -i "licen"     im_root.html  -> 0
```

The document contains no licence text. Its visible text ends `... Learn More Privacy Policy |
Accessibility Information` and its `<title>` is `Illustrative Mathematics | Kendall Hunt`. The
summarizing layer produced a sentence that was not in the bytes it was given.

The evidence file's own record of the event, verbatim:

> A first WebFetch of `/` returned the CC sentence anyway — i.e. the summarizing model
> produced text absent from the bytes it was given. Treated as unreliable; all findings
> below come from raw curl output only.

**The licence it named was the right one.** The task bank really is CC BY-NC-SA 4.0, confirmed
later at byte level on `/content-standards` and on all 24 in-scope task pages. That is the whole
trap. A wrong summary gets caught by the next reader. A right summary is indistinguishable from
a finding, and it propagates.

The standing warning this project carried forward from that incident, verbatim from its own
adjudication:

> a WebFetch summary once returned a license sentence that was *not present in the
> bytes of the document it was given*. It happened to be the right license. It was not evidence.
> Every finding rests on raw fetch output, not on a summarizing layer.

## When to reach for it

Reach for this page before any sentence appears in quotation marks in a licence claim. Under
honesty floor F3, quoted text must be byte-exact. A summarizer's rendering of a sentence,
however faithful in substance, is not byte-exact and cannot be presented as a quotation.

Reach for it when a fetch produced a clean, quotable answer on the first try from an obvious
path. That is the shape the incident took: a root URL, a plausible sentence, no friction.

Reach for it when a report's method is not stated. If you cannot tell from the artifact whether
a quotation came from bytes or from a model, the quotation is not admissible, whatever it says.

Do not reach for this page for reachability work. A summarizing fetcher is a perfectly good
instrument for "did this return content", for navigation, and for finding which paths are worth
a raw fetch. The claim here is narrow and it is about which layer a licence sentence may come
from.

## How it works

### The wiki's evidence floor is CONFIG policy; this page is the incident behind it

The rule that a licence claim is valid only if someone fetched the page and can paste the licence
sentence verbatim, with its URL and HTTP status, lives in this wiki's `CLAUDE.md` because it
binds every page rather than being a topic within one. This page owns the worked failure that
made it non-negotiable, and [[practice-build-a-source-table]] owns the procedure that satisfies
it.

### Two failure directions, not one

The summarizing layer can produce text that is not in the document, and it can fail to reach
text that is.

**Text that is not there.** The task-bank incident above. The model filled a gap from
plausibility, and plausibility was right.

**Text that is there and unreached.** On `accessim.org`, the Course Guide attributions content
lives in the RSC flight payload rather than in the initial DOM, and the recorded extraction note
is that WebFetch truncates before reaching it; the text was extracted from raw HTML instead. A
report that stopped at the summarizer would have recorded that page as carrying no attribution
text. It carries the CCSS trademark notice, the NCTM permission that runs to IM only, and the
non-IM image paragraph.

Both directions produce a confident, well-formed negative or positive. Neither announces itself.

### The countermeasure was adopted independently, twice, and both agents wrote their method down

The ERIC agent's method note, as staged:

> WebFetch summarizes rather than pastes. All verbatim quotes below were extracted by curl
> plus local HTML-to-text (regex tag strip), not by the WebFetch summarizer.

The IM task bank agent's, as staged: bash `curl` with a browser user agent, raw bytes inspected,
and the statement "Every quote below was read out of a downloaded file, not from memory."

Two agents on two hosts arrived at the same rule without coordination. That is the strongest
evidence in this corpus that the rule is about the instrument rather than about one bad fetch.

## In practice

### What an admissible licence quotation carries

Every one of these is present on the staged extracts that pass, and absent from the fetch that
failed:

1. **The URL fetched**, exactly, including scheme and any query string.
2. **The HTTP status**, and the client used if it mattered.
3. **The fetch date.** A licence claim without one is a memory, not a fact.
4. **The extraction path**, named: raw curl plus a local strip, `pdftotext`, a byte count, a
   `grep -c` result. "WebFetch returned" is not an extraction path for a quotation.
5. **A corroborating measurement**, ideally a negative one. `grep -c -i "licen" -> 0` on a
   document is what turned the task-bank incident from an anomaly into a finding.

### Verify a claim by trying to break it, not by re-asking

The task-bank incident was caught by a grep that expected to confirm the sentence and returned
zero. That is the check: take the sentence you have been handed and go looking for it in the
bytes, with a command whose failure mode is visible. Re-fetching through the same summarizing
layer will hand you the same sentence again.

### Count the hops before you write "verbatim"

A quotation on a page of this wiki is typically several transcriptions away from the wire, and
each staged extract says so in its own words. Every host extract in `sources/` opens with a
statement that no host was re-fetched at staging time, and that every quotation is transcribed
from a named local evidence file. The verdict tables add another layer: they are this project's
own adjudication, assembled from twelve agents' reports, and one of them says explicitly that a
page must not cite it as though it were an authority.

So the honest form for a page is the golden page's form: name the host as the speaker, give its
URL and fetch date, and name the staged extract as the transcription you actually read.

## Gotchas & constraints

**1. The failure is silent because the output is correct.** No lint catches it. No reviewer
catches it. The only signal available is provenance, which is why provenance is the thing this
wiki records rather than confidence.

**2. Transcription drift is real, and this project has an instance of it.** Two of this
project's own records quote the ERIC agent's method note differently. `sources/host-eric.md`
renders it "extracted by curl plus local HTML-to-text (regex tag strip)". `INVENTORY.md` renders
the same sentence "extracted by curl + local HTML-to-text". Both are presented as verbatim from
§1 of the same underlying report. At least one is not byte-exact, and the underlying report was
not opened at the writing of this page. The substance is unaffected and the F3 point is not: a
sentence can drift across a hop while every hop believes it is quoting.

**3. Elision markers belong to whoever made them, and several in this corpus belong to the
staging layer rather than to the host.** `sources/host-eric.md` records that the `[...]` inside
its ERIC quotations is the report's own elision marker. `sources/host-learning-commons-kg.md`
records the same about a `…` between two quoted passages. An unattributed ellipsis inside a
quoted licence sentence is a hole of unknown size, and in a licence sentence the missing clause
is exactly what a reader needed.

**4. The same shape appears wherever an intermediate layer stands between you and the bytes.**
A compressed body grepped as text returned zero matches and nearly produced a wrong withdrawal
date on `achievethecore.org`; the method warning that agent recorded ends "Never grep a
possibly-compressed body." See [[trap-compressed-body-grepped-as-text]]. In the tooling half of
this wiki, a test suite that imports `src` proves nothing about a running server binary. See
[[trap-stale-stdio-mcp-server]].

**5. This is not an argument against summarizing fetchers.** It is an argument about
admissibility. A summarizer is fine for orientation and useless as a witness, and the corpus
uses it for the first constantly.

**6. A model's own prior is the same failure without the fetch.** The retired-vocabulary table
in this wiki's synthesis brief exists because folk knowledge about open-education licensing has
been measured wrong three times in this project. Prior knowledge and a summary layer fail in the
same direction, plausibly and confidently, and the corpus treats training knowledge as
inadmissible for exactly that reason.

**7. The incident's own resolution is worth carrying: the licence really was CC BY-NC-SA 4.0,
and it lives one level in.** The root carries nothing; `/content-standards` and every task page
carry the footer, and no task overrides it. Being right about the licence and wrong about the
evidence are independent. See [[trap-license-lives-off-the-obvious-page]].

## Related

- [[source-im-task-bank]] is the host the incident happened on, and where the byte-level
  confirmation of the same licence was later recorded across all 24 in-scope task pages.
- [[source-eric]] is where the independently-adopted countermeasure is stated as a method note,
  and where 4 of 7 sampled PDFs turned out to carry no notice at all, a negative that only a raw
  read can support.
- [[source-accessim-360]] is the opposite direction of the same failure: content present in the
  bytes and unreachable by the summarizing layer.
- [[source-im-kendall-hunt]] is the page whose every quotation is a pasted byte, and the model
  this wiki writes to.
- [[trap-compressed-body-grepped-as-text]] is the same shape in the extraction layer, where a
  present string measures as absent.
- [[trap-stale-stdio-mcp-server]] is the same shape in the tooling layer, where a passing test
  says nothing about the artifact that actually runs.
- [[trap-license-lives-off-the-obvious-page]] is why the root returned nothing in the first
  place, and why a clean fetch of the obvious page is its own hazard.
- [[trap-down-is-not-one-state]] covers the reachability work a summarizing fetcher is
  legitimately good for, and where its verdicts still need a named client.
- [[concept-cite-quote-adapt]] separates the three reuse operations; quoting is the one that
  requires byte-exact reproduction, so it is the operation this trap attacks directly.

## Composes with

- [[practice-build-a-source-table]] owns the fetch-and-record procedure that satisfies the
  evidence floor; the five fields under "What an admissible licence quotation carries" are the
  columns that procedure must fill before a licence sentence may be quoted anywhere in this wiki.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-im-task-bank.md`, primary. §2 the three zero-match grep counts on the root
  document, the root's visible text and title, the verbatim record of the summary-layer failure,
  and the statement that the licence lives one level in; §1 the stated method, raw bytes via
  curl with a browser user agent; §3 the byte-level confirmation of the actual licence footer.
- `sources/host-eric.md`, primary. The method note adopting the same countermeasure
  independently; §2 the elision-marker attribution; §4 the seven per-PDF licence reads, including
  four documents verified silent by direct extraction with their character counts.
- `sources/host-accessim-360.md`, primary. §5 the RSC flight-payload extraction note, where the
  summarizing layer truncates before reaching the attributions text present in the raw HTML.
- `sources/host-achieve-the-core.md`, primary. §4c the compressed-body method warning and the
  near-miss it prevented.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: the
  standing warning carried forward from the task-bank report, and the "HOW TO CITE THIS" section
  ruling that the adjudication itself is secondary and must never be cited as an authority.

The wiki-wide admissibility rule these extracts implement is CONFIG policy and lives in this
wiki's `CLAUDE.md`, not on a content page. Everything above is this project's own record of its
own instruments. No host said any of it.
