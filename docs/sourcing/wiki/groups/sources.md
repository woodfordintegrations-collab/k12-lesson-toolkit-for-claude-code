---
title: "source: the sixteen host verdicts"
type: group
updated: 2026-08-08
---

# source

Sixteen pages, one per host. Each one answers a single question about a single domain: **what may
this repository do with material taken from here, and what is the pasted evidence for that
answer.** You arrive holding a URL, a PDF or a citation, and you leave with a verdict and a fetch
date.

The verdict vocabulary is five tokens, from loosest to tightest:

| Verdict | What it clears |
|---|---|
| `quote_and_adapt` | cite, quote, and paraphrase-and-republish into shipped prose |
| `quote_noncommercial` | cite and quote; adaptation is clear until something is sold |
| `quote_sharealike` | cite and quote; adaptation is licensed but foreclosed by ruling R9 |
| `cite_only` | cite and link, and nothing that reproduces expression |
| `do_not_use` | nothing; **no host in this corpus carries it** |

**Read the verdict as a floor, not a description.** It is one token and several of these hosts
carry riders it does not name. `source-engageny-nysed` is `quote_sharealike` **plus** NonCommercial.
`source-openstax` is a deliberately restrictive host-level default over a per-book answer that is
sometimes looser. `source-math-vision-project` is `quote_and_adapt` on rights and out of the build
on operational grounds. `source-corestandards-nga-ccsso` is `cite_only` because that is the one
operation nobody disputes, not because quotation was found to be prohibited. The verdict gets you
to the right page in one hop; the page is where the rider lives.

**Resolve the host before the verdict.** One organisation runs three of these hosts under three
different grants with near-identical lesson titles, and this project has recorded errors in both
directions. A verdict attaches to a domain, and often to a book slug or a record inside it, never
to a publisher's name.

Every claim on these pages carries a fetch date because two grants in this corpus were withdrawn
inside six months. A verdict older than its host's last change is a memory. See
[[license-withdrawn-grants]] and [[trap-license-withdrawn-after-citation]] before reusing any row
below without refetching.

## Pick a host

**Ordering: by how often a build actually lands on the host, most-reached first.** The top four are
touched by nearly every lesson and every document; the bottom four are reached once, to settle a
question, and then not again.

| Host page | Verdict | What error it prevents |
|---|---|---|
| [[source-im-kendall-hunt]] | `quote_and_adapt` | Concluding the host is unlicensed because its landing page carries no notice at all. The grant lives off-host in IM's Terms §7.1 and is confirmed on every deep curriculum footer. |
| [[source-learning-commons-kg]] | `quote_and_adapt` | Hard-coding one attribution string for the whole graph. `attributionStatement` is per record, and four distinct strings touch this unit. |
| [[source-corestandards-nga-ccsso]] | `cite_only` | Writing "the standards are CC BY 4.0". That is a redistributor's stamp; the owner's grant is bespoke, purpose-limited, and mandates an "All rights reserved" notice verbatim. |
| [[source-im-task-bank]] | `quote_sharealike` | Treating a numeric IM task id as covered by the curriculum host's CC BY 4.0. It carries ShareAlike, and four AMC-derived tasks are cite-only whatever the footer asserts. |
| [[source-accessim-360]] | `quote_noncommercial` | Reading HTTP 200 as proof a path exists on a host where every path returns 200, and importing NonCommercial when the CC BY 4.0 first edition would have served. |
| [[source-openstax]] | `quote_sharealike` | "OpenStax is CC BY 4.0." Eight of ten maths slugs checked returned CC BY-NC-SA 4.0, and the newer edition is the restricted one. |
| [[source-engageny-nysed]] | `quote_sharealike` | Writing off a live source from "HTTP 000". The apex is NXDOMAIN and `www` has an expired certificate; the licence is live at NYSED. |
| [[source-achieve-the-core-sap]] | `cite_only` | "Achieve the Core is CC0." The blanket dedication was withdrawn between 2026-04-25 and 2026-08-08, and what survives covers `learnwithsap.org` by its own words. |
| [[source-ohio-released-items]] | `cite_only` | Reading the document's one "Permission to reproduce" sentence as Ohio's grant. It closes a reproduced third-party matrix; the items begin on the next page under no grant. |
| [[source-math-mistakes]] | `quote_and_adapt` | Citing a bare `mathmistakes.org` URL. The live host returns HTTP 200 with a PHP fatal error as the entire body, so every citation must point at a Wayback capture. |
| [[source-mars-map]] | `cite_only` | Assuming one site-wide grant. Four regimes run on this host, and it is NoDerivatives, not NonCommercial, that makes it cite-only. |
| [[source-open-middle]] | `cite_only` | "Open Middle is CC BY-NC-SA." The CC clause was deleted between 2026-02-16 and 2026-03-03, and a separate later event moved the rights-holder. |
| [[source-jmap]] | `cite_only` | Applying NYSED's permissive-sounding grant to a JMAP worksheet. That grant does not reach copies on sites NYSED does not link, and JMAP itself grants nothing. |
| [[source-eric]] | `cite_only` | "Full text is available on ERIC" read as permission. ERIC grants nothing in its own words, and 4 of 7 sampled PDFs carried no notice at all. |
| [[source-math-vision-project]] | `quote_and_adapt` | Hunting for the licence defect behind "MVP is out". There is none on the Geometry route: R11 is operational, and the replacement it names, task 1635, is not CC BY 4.0. |
| [[source-nesa-nsw]] | `cite_only` | Quoting this project's own recorded NESA sentence. It is not in the delivered bytes, and the outcome the row names does not mention complementary angles. |

## Where this family ends

A `source` page tells you what one host permits **at one date**. It does not tell you what the
instrument itself means, what to do next, or how the reading fails.

- What the instrument does, host-independently: [[licenses]]
- What the verdict lets you actually do with the material: [[concepts]] and [[practices]]
- How a correct-looking reading of a host goes silently wrong: [[traps]]
- Whether a fetch counts as evidence at all: the evidence floor in this wiki's `CLAUDE.md`
