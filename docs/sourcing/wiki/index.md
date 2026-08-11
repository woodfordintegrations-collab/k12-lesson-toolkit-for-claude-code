---
title: Instructional Resource Sourcing and Formatting
type: index
updated: 2026-08-08
---

# Instructional Resource Sourcing and Formatting

A source-grounded wiki on the **rights, provenance and output shape** of instructional
material. 66 content pages across seven families.

**New here?** Go to [[when-to-use]]. It routes by the situation you are actually in
rather than by the family a page happens to live in.

## What this wiki is not

**It is not a wiki about the standards themselves.** No page here restates what a
standard says, and a page that did would be a defect rather than a bonus.

That content already exists, and it exists as a deterministic artifact rather than as
writing. `the private workspace/wiki-vaults/build_standards_vault.py` renders the standards store to
notes straight from `data/k12-lesson-toolkit.db`, and it imports the project's own placement
rule instead of reimplementing it. Its own docstring states the consequence:

> this calls `dedupe_richest` rather than reimplementing it, and a vault node is by
> construction the same node the grounding tools would return for that code

The vault therefore cannot drift from the MCP. Prose here about a standard's content
could drift, immediately and silently, and nothing downstream would flag the second copy
as the wrong one. `CLAUDE.md` records the emitted set at 812 standard pages. Read a
standard there.

What this wiki holds is everything the vault cannot: who owns the text, what you may do
with it, which node a value came from, and why an empty answer is not an absence.

## The seven families

| Family | Pages | What it holds | Group page |
|---|---|---|---|
| `source` | 16 | One rights verdict per host, with the host's own words pasted in | [[sources]] |
| `license` | 8 | One page per licence regime, including the two states that are not grants | [[licenses]] |
| `concept` | 6 | The distinctions the verdicts are made of, reusable beyond this corpus | [[concepts]] |
| `contract` | 10 | The shape the `k12-teacher-skills` plugin requires of an output package | [[contracts]] |
| `practice` | 8 | Procedures: fetch, resolve, ground, attribute, format | [[practices]] |
| `trap` | 13 | Failures with no error state, each one measured in this project | [[traps]] |
| `evidence` | 5 | Appraisals of a specific claim, including claims this project got wrong | [[evidence]] |

## The three questions this wiki answers on demand

### 1. May I put this text in a deliverable?

Start with the operation, not the licence. "Is this source open" has no answer;
"may I cite, quote, or paraphrase-and-republish it" has three.

| Where you are | Entry point |
|---|---|
| Naming the operation before anything else | [[concept-cite-quote-adapt]] |
| The host is one of the sixteen already ruled on | [[sources]], then that host's page |
| The host is new, or the verdict is older than your last fetch | [[practice-build-a-source-table]] |
| A licence name is on the table and you need what it actually forbids | [[licenses]] |
| The verdict came back `cite_only` and you want to know what survives | [[practice-cite-without-redistributing]] |
| The deliverable is finished and needs its credit files | [[practice-assemble-an-attribution-block]] |

The standing answer that catches most people: **citation is unconstrained by every source
in this corpus.** ShareAlike, NonCommercial and NoDerivatives do not touch it.

### 2. What is the grounded verbatim standard data, and which node did it come from?

A code is not a node. One code usually resolves to several framework placements, the data
is authored against some of them, and landing on the wrong one returns an empty result
that looks exactly like a correct one.

| Where you are | Entry point |
|---|---|
| Turning a code into a statement, a UUID and a jurisdiction | [[practice-resolve-a-standard-code]] |
| Grounding a whole lesson and freezing the provenance | [[practice-ground-a-lesson-end-to-end]] |
| Deciding which of several same-code placements you are on | [[concept-standard-placement-vs-code]] |
| Asking what the upstream graph even contains | [[evidence-kg-coverage-and-gaps]] |
| Asking what survived the ingest into the local store | [[evidence-store-ingest-boundary]] |
| Holding an empty result and about to write it up as a finding | [[traps]], starting at [[trap-empty-facet-reads-as-success]] |

### 3. What shape does the artifact take?

One `lesson.json` with two top-level keys becomes a rendered document set. The contract is
published in pieces across two skills and a subject reference file, and the pieces
disagree in places that matter.

| Where you are | Entry point |
|---|---|
| Deciding how many documents the package has | [[k12-document-set]] |
| Authoring the file, start to render | [[practice-format-a-lesson-package]] |
| Writing a quiz, an exam or a key | [[practice-format-an-assessment-artifact]] |
| A block did not render, or rendered as plain prose | [[k12-block-types]] |
| The render "worked" and something is missing | [[k12-render-invocation]] |
| A standard statement is about to be pasted into a document | [[k12-density-rules]] |
| Anything visual | [[practice-place-and-alt-text-a-figure]] |

## The evidence floor

**A licence claim is valid only with a pasted verbatim footer, its URL and a fetch date.**
No exceptions. A claim missing any of the three is a memory, not a fact, and it is not
admissible on any page here.

Three measured failures put that floor where it is:

1. **Grants get withdrawn inside a working window.** Achieve the Core's blanket
   public-domain dedication went away between 2026-04-25 and 2026-08-08. Open Middle's
   CC BY-NC-SA went away between 2026-02-16 and 2026-03-03. Both are still recorded as
   live on third-party lists. See [[license-withdrawn-grants]] and
   [[trap-license-withdrawn-after-citation]].
2. **One organisation publishes under several grants.** "IM is CC BY 4.0" is three
   different grants on three hosts. Every licence statement here names the **host**, never
   the brand.
3. **A summarizing layer returned a licence sentence that was not in the bytes it was
   given.** The sentence happened to be correct. It was not evidence. Findings rest on raw
   fetch output. The worked instance is [[trap-summary-layer-is-not-evidence]].

## Every page

### Sources (16)

Verdict vocabulary: `quote_and_adapt`, `quote_noncommercial`, `quote_sharealike`,
`cite_only`, `do_not_use`. Group page: [[sources]].

- [[source-im-kendall-hunt]] · `quote_and_adapt` · IM K-12 Math 1st edition; the grant lives off-host in IM's terms, and this is the spine an adapted through-line rests on
- [[source-learning-commons-kg]] · `quote_and_adapt` · the standards graph upstream of the local store; MIT code, CC BY 4.0 data, measured uniform across the whole export
- [[source-math-mistakes]] · `quote_and_adapt` · a CC BY 3.0 Unported misconception corpus on a host that is simultaneously up and unusable
- [[source-math-vision-project]] · `quote_and_adapt` · a clean licence ruled out on operational grounds; the page exists so the ruling stays legible
- [[source-accessim-360]] · `quote_noncommercial` · IM's second edition; same publisher, near-identical lesson titles, different grant
- [[source-im-task-bank]] · `quote_sharealike` · the frozen 2016 task bank; the IM host most likely to be reached for and mistaken for the curriculum
- [[source-engageny-nysed]] · `quote_sharealike` · a retired host whose publisher states in writing that it is not the copyright owner
- [[source-openstax]] · `quote_sharealike` · the edition licence inversion, where the licence is a property of the book slug
- [[source-achieve-the-core-sap]] · `cite_only` · two domains, one withdrawn dedication, and the Coherence Map that is the real asset
- [[source-corestandards-nga-ccsso]] · `cite_only` · the upstream owner of every standard statement reproduced anywhere in a deliverable
- [[source-mars-map]] · `cite_only` · four licence regimes on one host, and the host says so itself
- [[source-eric]] · `cite_only` · an index that grants nothing and says so in one sentence
- [[source-open-middle]] · `cite_only` · all rights reserved under a new rights-holder; the page exists because everyone still cites the old grant
- [[source-jmap]] · `cite_only` · Regents items indexed by standard, with two rights layers stacked and neither open
- [[source-ohio-released-items]] · `cite_only` · per-option rationales and annotated student work, validated at scale
- [[source-nesa-nsw]] · `cite_only` · the cross-jurisdiction comparison row, held for one comparative claim

### Licences (8)

Group page: [[licenses]].

- [[license-cc-by]] · the plain-attribution regime, and the licence this repo itself ships under
- [[license-noncommercial]] · a rider, not a licence; what it deletes and what it does not touch
- [[license-sharealike]] · the live constraint on this build, and the only rider whose failure is silent
- [[license-noderivatives]] · the rider people do not expect, which forecloses paraphrase outright
- [[license-public-domain-dedication]] · the most permissive instrument here and the one handled worst
- [[license-all-rights-reserved]] · a string that appears in four structurally different positions, only one of which is a verdict
- [[license-unmarked-silence]] · no notice is not no owner; where silence resolves to
- [[license-withdrawn-grants]] · the dated register of grants that moved inside this corpus's own window

### Concepts (6)

Group page: [[concepts]].

- [[concept-cite-quote-adapt]] · three operations, not one question; the split every verdict is written in
- [[concept-curate-and-cite]] · the posture held before the first fetch: fix the outbound licence, then read
- [[concept-chain-of-title]] · whether the host had the material it is granting you
- [[concept-attribution-per-record]] · why one credit string per host is wrong for most of what it gets applied to
- [[concept-third-party-carve-out]] · what sits inside a licensed work without being covered by it
- [[concept-standard-placement-vs-code]] · a code is a label several nodes share, and the data is on some of them

### Contracts (10)

The `k12-teacher-skills` output contract. Group page: [[contracts]].

- [[k12-document-set]] · `shared` and `documents`, and why three is a minimum rather than the count
- [[k12-shared-registry]] · register once, facet by audience; the only thing preventing page drift
- [[k12-block-types]] · twenty canonical emitters, two incomplete published vocabularies
- [[k12-lesson-plan-sections]] · the five math sections, which live in the subject reference file rather than in `SKILL.md`
- [[k12-student-materials]] · the one document whose existence is conditional, and its writing-space rules
- [[k12-observation-template]] · the teacher's clipboard page and its four prescribed sections
- [[k12-density-rules]] · the hard caps on text, and where the quotation obligation attaches
- [[k12-package-consistency]] · the cross-document invariants, run as a pass before rendering
- [[k12-render-invocation]] · one command, and the six distinguishable ways it hands back something wrong
- [[k12-assessment-gap]] · the hole in the contract, and what this project put in it

### Practices (8)

Group page: [[practices]].

- [[practice-resolve-a-standard-code]] · a code into a node, with every silent failure checked inside the call
- [[practice-ground-a-lesson-end-to-end]] · the full grounding pass, frozen into a bundle with provenance
- [[practice-build-a-source-table]] · fetch and record so a host becomes a defensible verdict
- [[practice-cite-without-redistributing]] · getting full value from a source you may not reproduce
- [[practice-assemble-an-attribution-block]] · the once-at-the-end build step that emits the credit files
- [[practice-format-a-lesson-package]] · grounded lesson into one `lesson.json` and out through the renderer
- [[practice-format-an-assessment-artifact]] · instruments the vendor contract does not cover
- [[practice-place-and-alt-text-a-figure]] · the renderer draws nothing; where figures live and how they are described

### Traps (13)

Each one measured in this project. Group page: [[traps]].

- [[trap-code-form-silent-zero]] · a near-miss code returns zero rows with no error
- [[trap-empty-facet-reads-as-success]] · an empty payload is what success, failure and an empty database all look like
- [[trap-learning-components-truncated-at-five]] · five is a ceiling, never a count
- [[trap-soft-404-status-proves-nothing]] · HTTP 200 for a page that does not exist
- [[trap-down-is-not-one-state]] · bot-blocked, expired cert, TLS failure, soft 404 and gone are five different findings
- [[trap-license-lives-off-the-obvious-page]] · a clean fetch of the root honestly reports no licence, on four hosts that have one
- [[trap-summary-layer-is-not-evidence]] · a correct sentence that was not in the document
- [[trap-compressed-body-grepped-as-text]] · grep over gzip returns the same zero an absent string does
- [[trap-font-notice-is-not-a-content-license]] · a grep counts strings, not which layer of the file they sit in
- [[trap-access-is-not-a-rights-fact]] · free, public and downloadable are statements about access
- [[trap-license-withdrawn-after-citation]] · a stale citation renders identically to a fresh one
- [[trap-sharealike-contaminates-by-paraphrase]] · rewriting in your own words does not escape it
- [[trap-stale-stdio-mcp-server]] · a green test suite and a running connector are different claims

### Evidence (5)

Appraisals of one claim each, including two this project asserted wrongly in writing.
Group page: [[evidence]].

- [[evidence-kg-coverage-and-gaps]] · what the upstream graph covers, and the layer that is empty
- [[evidence-store-ingest-boundary]] · what crosses from the export into the local store, and what is dropped
- [[evidence-c7-store-gap-not-corpus-gap]] · a claim that was half right, and why the wrong half was asserted
- [[evidence-k12-lesson-toolkit-acceptance-record]] · three records about one date, none of them a lie
- [[evidence-misconception-research-licensing]] · the per-paper record of what each document's own notice permits

## If you only read one thing

[[concept-cite-quote-adapt]]. Almost every wrong answer in this domain is a correct answer
to a different one of the three operations.
