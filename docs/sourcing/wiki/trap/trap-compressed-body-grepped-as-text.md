---
title: "A compressed body grepped as text"
type: trap
sources:
  - https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd
  - https://achievethecore.org/ccpd
  - https://www.openmiddle.com/
  - sources/host-achieve-the-core.md
  - sources/host-open-middle.md
  - sources/host-accessim-360.md
  - sources/host-im-kendall-hunt.md
  - sources/host-im-task-bank.md
  - sources/verdict-twelve-host-table.md
  - a private project memory file (not public)
updated: 2026-08-08
---

# A compressed body grepped as text

## Summary

A Wayback `id_` raw URL returns the payload as it was originally stored, which for most captures
means gzip. Grep over gzip bytes returns zero matches. Zero matches is the same number a genuinely
absent string returns, and nothing in the output distinguishes them.

Two agents in this project, working different hosts on different days, each hit this and each
nearly filed a false licence finding from it. Neither error was caught by a reviewer. Both were
caught by the agent noticing the result was too clean and re-fetching with `--compressed`. That is
a thin defence to be running twice on the same corpus, which is why it is a page.

The rule is one line: **confirm the body is text before you read a zero.** A grep count is only
evidence about content once you know you grepped content.

## When to reach for it

Reach for it on every Wayback `id_` fetch. That URL form is the one that gives you the original
bytes, which is exactly why it is used for licence archaeology and exactly why it is compressed.

Reach for it whenever a grep returns zero on a document you expected to be non-empty, and
especially when zero is the answer you were hoping for. Both near-misses in this corpus produced a
zero that confirmed the agent's working hypothesis, which is the condition under which nobody
re-checks.

Reach for it before recording any removal window, delisting, or "the notice is gone" finding. Both
recorded near-misses landed on the snapshot that defines a window boundary, which is the single
most load-bearing measurement in [[license-withdrawn-grants]].

Do not reach for this page when the fetch failed. A body you never received is a different
problem with its own decision table: see [[trap-down-is-not-one-state]]. This page is about a
successful fetch whose bytes you then misread.

## How it works

The sensor and the question are misaligned. `grep -c` answers "how many lines of this byte stream
match this pattern". The question being asked is "does this document contain this text". Those are
the same question only when the byte stream is the document's text.

Three ways they come apart in this corpus, all measured:

| Byte stream | Grep says | Document says |
|---|---|---|
| gzip payload from a Wayback `id_` URL | 0 | the string is present, and appears once decompressed |
| a PDF's embedded font descriptors | 1 or more on "All Rights Reserved" | nothing about the document's rights |
| a WebFetch summary | the licence sentence | the fetched bytes contain no licence text at all |

Row 1 is this page. Row 2 is [[trap-font-notice-is-not-a-content-license]]. Row 3 is
[[trap-summary-layer-is-not-evidence]]. The three share one property: the number that comes back
is well formed, unremarkable, and about the wrong object.

The same class shows up outside HTTP entirely. This project's own operating memory carries a floor
bullet about a shell idiom that produces the identical failure shape:

> In bash under `set -euo pipefail`, `echo "$V" | grep -q` fails SILENTLY via SIGPIPE. Use a
> here-string. The check reports failure while the pattern is present.

A check reporting failure while the pattern is present is the definition of the hazard. The
transport differs; the epistemics do not.

## In practice

**Near-miss one, achievethecore.org.** The staged extract records the fetching agent's own warning
verbatim:

> METHOD WARNING recorded: my first pass at this snapshot used wayback `id_` raw mode WITHOUT
> `--compressed`. curl returned gzip bytes; grep found 0 matches; I nearly reported "CC0 already
> gone by April 2026". That was an artifact of binary, not a finding. Re-fetched with --compressed
> -> 1 match. Never grep a possibly-compressed body.

The snapshot in question is `20260425161111`, and it is the **last** capture carrying the
public-domain dedication text. Had the zero been filed, the continuous snapshot series would have
been broken at its final member: `2016-03-03`, `2017-07-22`, `2020-04-30`, `2022-01-03`,
`2024-03-23`, `2026-01-11`, `2026-04-25` all carry the text. The recorded removal window, between
2026-04-25 and 2026-08-08, depends entirely on that last snapshot being read correctly.

**Near-miss two, openmiddle.com.** A different agent, a different host. Its first pass at the
2026-03-03 capture read gzip bytes as text and appeared to show, in the staged extract's words,
"no footer at all." It was re-fetched with `curl --compressed` before any conclusion was drawn.

That snapshot is the **first** capture without the Creative Commons clause, and its footer is not
absent, it reads:

> © 2016-2026 Open Middle Partnership. All rights reserved. Open Middle is the registered
> trademark of the Open Middle Partnership. Get in contact with us

The false reading would have cost two separate facts, not one. The CC removal window closes at
2026-03-03 because the footer is present and CC-free on that date; "no footer at all" cannot
support that boundary. And the rights-holder is still Open Middle Partnership in that capture,
which is what dates the later transfer to Glenrock Consulting, LLC to somewhere between 2026-03-03
and 2026-05-12. A blank reading erases the sequencing of two events.

**The check, and where it goes.** Before a zero becomes a finding:

1. Fetch with `curl --compressed` on any Wayback `id_` URL, unconditionally. The staged extracts
   record this as the fix in both cases, and it costs nothing when the body was already plain.
2. Confirm the received body is text before counting. This corpus has twice used byte-level
   inspection to settle what is actually present: `xxd` established that openmiddle.com's
   robots.txt literally begins `ser-agent: *` with the leading `U` absent, and `od -c` confirmed a
   50-byte path file in the k12-lesson-toolkit venv one byte at a time. That is the class of check.
3. Prove the sensor works on this document. A control pattern that must match, for example the
   host's own name or a tag you can see in the rendered page, turns "zero matches" from an
   ambiguous result into a discriminating one. If the control also returns zero, you are not
   grepping text.
4. Only then read the count.

Step 3 is the one that generalises past compression. It is the same move the Open Middle report
used against Wayback CDX itself: zero captures for `/terms*`, `/copyright*`, `/license*` and
`/privacy*` became usable negative evidence only because control queries against the root and
`/similar-triangles/` returned capture rows and proved the endpoint working.

## Gotchas & constraints

**1. Two independent agents hit this, which makes it structural rather than careless.** Different
hosts, different days, different snapshots, same failure, same near-miss recovery. Anything that
catches an error twice by the operator's own vigilance will eventually not catch it.

**2. Both near-misses were confirmations, not surprises.** The ATC agent's zero supported an
earlier CC0 removal; the Open Middle agent's blank supported a footer that had changed. A result
that agrees with the hypothesis is the one nobody re-runs, and it is the one both agents did
re-run. Treat a clean confirmation as the trigger for step 3 above, not as the end of the work.

**3. `--compressed` fixes the transport, not the sensor.** It tells curl to advertise and decode
content encodings. A body that is compressed at rest in some other way, an artifact that is a PDF
or a binary blob rather than markup, or a page whose text is assembled client-side, will still
return zeros over bytes that are not the document's prose. accessim.org is the recorded instance
of the last of those: its Course Guide attributions text lives in the RSC flight payload, not the
initial DOM, so a summarizing fetch truncated before reaching it and the text had to be pulled from
raw HTML.

**4. This page does not tell you the notice is present.** It tells you the zero was not evidence.
After decompressing you may well find a genuine zero, and that is a real finding with its own
consequences, which route to [[license-unmarked-silence]] for artifacts and to
[[trap-license-lives-off-the-obvious-page]] for hosts.

**5. Do not port the fix as a superstition.** "Always pass `--compressed`" is correct and cheap.
"A zero always means compression" is not. In this corpus a zero has been the correct reading of a
genuinely licence-free root on three separate hosts: im.kendallhunt.com's root returned zero
matches for `creative commons|CC BY|licens|copyright|attribution|all rights reserved` across
27,884 bytes; the tasks.illustrativemathematics.org root returned 0 for each of "creative",
"copyright" and "licen"; and accessim.org's homepage and privacy policy carry zero licence hits
against a per-page audit where every curriculum page carries exactly one. Those measurements are
load-bearing and they are all zeros.

**6. Neither near-miss produced a filed error, so nothing here is a correction to a shipped
claim.** Both are self-reported catches inside the fetching agents' own method notes. That is why
they were recoverable at all, and it is the reason this project's evidence files record method
warnings alongside findings rather than only the findings.

## Related

- [[trap-summary-layer-is-not-evidence]] is the sibling admissibility failure: text that was never
  in the bytes, rather than bytes that were never text.
- [[trap-font-notice-is-not-a-content-license]] is the third: a real string in the real bytes that
  is about the wrong object.
- [[trap-soft-404-status-proves-nothing]] is the same shape one layer up, where the HTTP status is
  the well formed number answering the wrong question.
- [[trap-down-is-not-one-state]] covers the failures that happen before you have a body at all, and
  is what to read when the fetch itself did not succeed.
- [[trap-license-withdrawn-after-citation]] is the finding class both near-misses threatened, where
  a dated window is the whole content of the claim, and [[license-withdrawn-grants]] is the
  register those windows feed.
- [[license-unmarked-silence]] is where a genuine zero lands once the sensor has been cleared.
- [[source-achieve-the-core-sap]] holds the host of the first near-miss and its snapshot series;
  [[source-open-middle]] holds the second, and the two-event sequence a blank reading would have
  erased.

## Composes with

- [[practice-build-a-source-table]] carries the fetch-and-record procedure this check belongs
  inside. The check runs at the point where a raw fetch becomes a recorded count, and the
  procedure's raw-bytes-over-summaries rule is what makes it necessary: once you are reading bytes
  yourself, you own the question of what those bytes are.

## References

Live and archived fetches by this project, 2026-08-08:

- `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd` HTTP 200. The
  snapshot where the first near-miss occurred; returns the public-domain dedication text only when
  fetched with `--compressed`. Recorded as the latest capture carrying that text.
- `https://achievethecore.org/ccpd` live, 140,749 bytes, byte-identical to the homepage shell, with
  "Public Domain Dedication" occurring 0 times.
- Wayback captures of `openmiddle.com`, fetched `--compressed`: 2016-05-27, 2019-06-03, 2023-06-01
  and 2026-01-09 carry the Creative Commons clause; 2026-02-16 is the last that does; 2026-03-03 is
  the first that does not and is the capture the second near-miss landed on.
- `https://www.openmiddle.com/` HTTP 200 with a browser user agent. The live footer, all rights
  reserved under Glenrock Consulting, LLC.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-achieve-the-core.md`, primary. §4b the snapshot series and the measured removal
  window, §4c the method warning quoted verbatim above.
- `sources/host-open-middle.md`, primary. §5 the snapshot table with both verbatim footers and the
  method note recording the second near-miss, §2 the Wayback CDX control queries that make its
  negative evidence usable, §1 the `xxd` byte check on robots.txt.
- `sources/host-accessim-360.md`, primary. §2 the soft-404 measurement, §4 the per-page licence
  audit whose zeros on the homepage and privacy policy are correct readings, and §5 the RSC flight
  payload that a summarizing fetch truncates before reaching.
- `sources/host-im-kendall-hunt.md`, primary. §2, the root-footer grep returning zero matches.
- `sources/host-im-task-bank.md`, primary. §2, the three transcribed zero counts on the root
  document.
- `sources/verdict-twelve-host-table.md`, reference. §3 corrections 3 and 8, the two withdrawal
  findings that rest on the snapshots in question, and Row 1 where the 27,884-byte root measurement
  is recorded.

This project's own operating memory, cited as this project's record rather than any outside
party's statement:

- A private engineering note recording the same SIGPIPE floor
  bullet quoted above.
