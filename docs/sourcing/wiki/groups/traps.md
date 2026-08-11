---
title: "trap: the thirteen silent failures"
type: group
updated: 2026-08-08
---

# trap

Thirteen pages, and one property is common to all of them: **the broken case and the working case
are the same bytes.** No error, no warning, no non-zero exit, no partial match. The tool returns an
empty list. The fetch returns 200. The grep returns zero. The render exits 0 and the directory
fills with real files. Every page here names one such pair and gives the check that tells them
apart.

That is why this is the largest family in the wiki. A failure that announces itself does not need a
page. These are the ones a competent, careful person walks into, which is the only kind worth
writing down, and most of them were walked into inside this project rather than imagined for it.

You want this family at the moment you are **about to write something down**. That is the shared
trigger. Not at the moment of the call, not at the moment of the fetch, but at the sentence: "the
store has no data for this standard", "no licence found", "the site is unreachable", "the standard
decomposes into these five components", "verified". Each of those sentences is a trap's output, and
once it is in a table nobody re-probes it.

Ten of the thirteen were measured in this corpus with the host, the byte count and the date
recorded. The remaining three generalise a measured instance to the class of thing it belongs to.
None of them is hypothetical.

## Pick a trap

**Ordering: by how many chances it gets to fire, grouped by where.** The grounding-path traps fire
on every lesson, the rights traps on every source, the measurement traps on every fetch, and the
last one only when someone changes the server code.

| Page | Fires on | What error it prevents |
|---|---|---|
| [[trap-code-form-silent-zero]] | every standards lookup | Writing "the store has no data for this standard" from `{"standards": []}`, which is byte-identical to the payload a wrong code form returns. |
| [[trap-empty-facet-reads-as-success]] | every facet call | Reading an empty facet as a fact about the standard. A genuine empty, a registered stub and a swallowed exception produce the identical payload. |
| [[trap-learning-components-truncated-at-five]] | every component list | Writing "the standard decomposes into these five components". The tool slices at five with no count, no total and no `truncated` field. |
| [[trap-access-is-not-a-rights-fact]] | every source verdict | Reading free, public, unauthenticated or HTTP 200 as permission, and reading a 403 or 406 as a fact about rights rather than about your client. |
| [[trap-sharealike-contaminates-by-paraphrase]] | every sentence drafted with a source open | Both directions at once: "I reworded it, so it is mine", and "this host is ShareAlike, so I cannot use it". |
| [[trap-license-withdrawn-after-citation]] | every licence claim not made from a fetch this session | Treating a verdict as durable. A stale licence label renders identically to a fresh one, and nothing re-checks it. |
| [[trap-license-lives-off-the-obvious-page]] | every host root fetch | Recording "no licence found" from a clean, unblocked root fetch. Four hosts here return that result and on all four the grant existed. |
| [[trap-down-is-not-one-state]] | every failed fetch | Collapsing a UA block, an expired certificate, a TLS handshake failure, NXDOMAIN and a PHP fatal error into "unreachable". Each has a different next move. |
| [[trap-soft-404-status-proves-nothing]] | every path probe | Recording "no terms page exists", or "the terms page said nothing about licensing", from a 200 that served the homepage shell. |
| [[trap-summary-layer-is-not-evidence]] | every quoted licence sentence | Quoting a summarizer's rendering. One returned a correct licence sentence that was not in the bytes of the document it was given. |
| [[trap-font-notice-is-not-a-content-license]] | every verdict written off a grep count | Reading embedded Calibri font metadata as a content reservation, or a stylesheet's licence comment as a grant. Both happened on one host. |
| [[trap-compressed-body-grepped-as-text]] | every Wayback `id_` fetch | Reading a zero from a gzip body. Two agents on different hosts each nearly filed a false licence finding from it. |
| [[trap-stale-stdio-mcp-server]] | every claim that an MCP change is verified | Verifying against an in-process `src` import. The stdio server is spawned once per session and never reloads, and all 68 repo tests import the module directly. |

## Where this family ends

- The doctrine each trap violates, stated positively: [[concepts]] and [[licenses]].
- The procedure whose checks exist because of these: [[practices]], especially [[practice-build-a-source-table]].
- The host where a given trap was actually measured: that host's page in [[sources]].
- The measured census a trap's empty result is a boundary of, not a finding about: [[evidence]].
