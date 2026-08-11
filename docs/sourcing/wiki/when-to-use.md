---
title: When to Use This Wiki
type: index
updated: 2026-08-08
---

# When to Use This Wiki

You arrive holding a situation, not a family name. This page maps situations to entry
pages. Each row says why that page and not the neighbour a reasonable person would open
instead, because in this domain the neighbour is usually the page that gives a confident
wrong answer.

Front door and full page list: [[index]].

## Rights: may I use this?

### I have a URL and want to know if I can use it

**Go to [[practice-build-a-source-table]].** It is the fetch-and-record procedure that
turns a host into a defensible verdict: raw bytes rather than a summarizing layer, HTTP
status and fetch date on every claim, existence tested by byte-diff, an explicit
unverified column.

Check [[sources]] first in case the host is one of the sixteen already ruled on. If it is,
read the fetch date on that page before you rely on it.

Not a licence page. You do not have a licence yet, you have a URL, and
[[licenses]] assumes a notice already extracted from bytes somebody read.

### I want to quote a task

**Go to [[concept-cite-quote-adapt]].** Quoting is one of three operations and the licences
constrain them very differently. A quotation set inside your own prose with attribution is
a use of the work, not an adaptation of it.

Not [[license-sharealike]], which is the page people open here and the reason quotable
material gets dropped. ShareAlike attaches to adaptation, not to quotation, and reading
the rider first produces a refusal the licence does not require. Once the operation is
settled, the host's own page carries the string you owe.

### I want to write an item inspired by one

**Go to [[trap-sharealike-contaminates-by-paraphrase]].** Rewriting a task in your own
words does not escape ShareAlike: a close paraphrase that follows a specific task's
structure, numbers and pedagogical move is an adaptation however different the wording.

Not [[concept-cite-quote-adapt]], which names paraphrase-and-republish as the bitten
operation but does not locate the moment. The trap does: the seam is crossed while you
draft with the source open, and it is invisible in the finished file afterwards.

### A source I cited last month changed

**Go to [[trap-license-withdrawn-after-citation]].** A licence verdict is a timestamped
observation, not a durable property of a source, and this page holds the re-verification
trigger plus what to do about a claim that already shipped.

Not [[license-withdrawn-grants]], which is the dated register of which grants moved and
when. Read that second, to check whether your source is one of the two measured
withdrawals, or first if you only want to know what happened rather than what to do.

### I need an attribution block for a deliverable with six sources

**Go to [[practice-assemble-an-attribution-block]].** It runs once, over the closed
used-source list, and emits the two files a reader can check against the law. Six sources
is exactly the case it is built for: it enumerates records rather than hosts.

Not [[concept-attribution-per-record]], which is the reason the procedure enumerates that
way. Open it when you hit a record whose required string is not the one on the host's
footer, which happens here by jurisdiction, node type and grade band.

## Tooling: the answer looks fine and may not be

### The tool returned an empty list

**Go to [[trap-empty-facet-reads-as-success]].** An empty payload is byte-identical to a
successful call, a crashed call and a call against an empty database. Read this before the
emptiness becomes a sentence in a document.

Then branch on what you called:

| What you called | Next page |
|---|---|
| A standards lookup by code | [[trap-code-form-silent-zero]], because a near-miss code form returns zero rows with no error |
| A lookup that matched, then a facet that came back empty | [[concept-standard-placement-vs-code]], because the first hypothesis is the wrong placement, not absent data |
| A component list that came back with five items | [[trap-learning-components-truncated-at-five]], because five is the cap, never a count |
| Anything expecting a layer the local store may not hold | [[evidence-store-ingest-boundary]], which is the census of what crosses ingest |
| A tool you believe you just fixed | [[trap-stale-stdio-mcp-server]], because a green test suite and a running connector are different claims |

### A page returned 200 but I am not sure it exists

**Go to [[trap-soft-404-status-proves-nothing]].** The server answered 200 with something
else entirely, and on one host in this corpus a path nobody has ever typed returns 200
too. Existence is tested by byte-diff against a known-nonsense path, not by status.

Not [[trap-down-is-not-one-state]], which is the taxonomy for a fetch that **failed**.
This is the opposite shape: a fetch that succeeded and should not have.

### The fetch failed and I am about to write "unavailable"

**Go to [[trap-down-is-not-one-state]].** Bot-blocked, expired certificate, TLS handshake
failure, soft 404 and genuinely gone are five findings with five remedies, and one label
loses four of them. Two reachability findings inherited in this corpus were wrong.

### I fetched the root and found no licence

**Go to [[trap-license-lives-off-the-obvious-page]].** A clean, unblocked fetch of the root
honestly reports zero on four hosts here, and all four have a grant. It is one host away,
or one level in.

Pair it with [[trap-compressed-body-grepped-as-text]] if the fetch was a Wayback `id_` URL.
Grep over gzip returns the same zero an absent string does, and two agents here nearly
shipped that zero as a finding.

## Output: what shape does it take?

### I need to format a lesson package

**Go to [[practice-format-a-lesson-package]].** It is the authoring order: load the subject
reference file first (mandatory, and the five math sections live there rather than in
`SKILL.md`), write one `lesson.json`, run the consistency pass, then render and verify the
render.

Not [[k12-document-set]], which is the contract the procedure fills in. Open that one when
the question is how many documents the package has and what each is called, rather than
what to do next.

If the render already ran and something is wrong, go straight to
[[k12-render-invocation]]: one command, six distinguishable ways it hands back something
that is not a delivered package.

### I need a quiz, an exam or a key

**Go to [[practice-format-an-assessment-artifact]].** There is no vendor contract for these
and the planning skill's own trigger text excludes them. This page is what this project
decided, which is a different kind of authority from the contract pages beside it, and
[[k12-assessment-gap]] holds that boundary.

### A block did not appear on the rendered page

**Go to [[k12-block-types]].** Twenty canonical emitters, two published vocabularies, both
incomplete, and an unknown type falls back silently to prose. That is the same cause as a
block that rendered as plain text where a structure was expected.

If the block came from `shared`, [[k12-shared-registry]] holds the silent-empty behaviour
behind a registered key that produces nothing.

## Grounding: which node did this come from?

| Situation | Entry page |
|---|---|
| I have a code and need its statement, UUID and jurisdiction | [[practice-resolve-a-standard-code]] |
| I am starting a lesson and need every claim to name its node | [[practice-ground-a-lesson-end-to-end]] |
| Two documents disagree about how many components a standard has | [[trap-learning-components-truncated-at-five]] |
| I want to know what the upstream graph contains before I ask it anything | [[evidence-kg-coverage-and-gaps]] |
| I need the attribution string and the store does not have it | [[evidence-store-ingest-boundary]] |

## Four sentences that mean you are about to be wrong

| The sentence | The page |
|---|---|
| "This source is open" | [[concept-cite-quote-adapt]]. Open for which of the three operations? |
| "IM is CC BY 4.0" | [[source-im-kendall-hunt]], [[source-im-task-bank]], [[source-accessim-360]]. One publisher, three hosts, three grants. |
| "The store has no data for this standard" | [[trap-code-form-silent-zero]], then [[trap-empty-facet-reads-as-success]]. |
| "This site is unlicensed" | [[trap-license-lives-off-the-obvious-page]], then [[license-unmarked-silence]] if the search really is exhausted. |

## The floor under all of it

A licence claim is valid only with a **pasted verbatim footer, its URL and a fetch date**.
If you cannot produce all three, the honest output is the gap and what it would take to
close it. See [[trap-summary-layer-is-not-evidence]] for the incident that made this
non-negotiable: a summarizing layer returned a licence sentence that was not in the bytes
of the document it was given, and the sentence happened to be correct.
