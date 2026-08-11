---
title: "The three reuse operations: cite, quote, paraphrase-and-republish"
type: concept
sources:
  - sources/verdict-twelve-host-table.md
  - sources/cc-by-4-0.md
  - sources/cc-by-3-0.md
  - sources/cc-by-nc-4-0.md
  - sources/cc-by-nc-sa-4-0.md
  - sources/cc-by-nc-nd-3-0.md
  - sources/cc0-1-0.md
  - sources/host-mars-map.md
  - sources/host-im-task-bank.md
  - sources/host-eric.md
  - sources/host-open-middle.md
  - https://creativecommons.org/licenses/by/4.0/
  - https://creativecommons.org/licenses/by-nc-sa/4.0/
  - https://creativecommons.org/licenses/by-nc-nd/3.0/
  - https://eric.ed.gov/?copyright
updated: 2026-08-08
---

# The three reuse operations: cite, quote, paraphrase-and-republish

## Summary

Doing something with someone else's material is not one operation. It is three, and the licence
terms constrain them very differently. Most licence anxiety in this domain comes from collapsing
them into a single question ("is this source open?") and then answering that question with a
feeling rather than a reading.

| Operation | What it is | What constrains it |
|---|---|---|
| **Cite** | Name it, link it, state what standard it addresses, describe in your own words what it does, record title, author, URL and access date | Nothing, in this entire corpus |
| **Quote** | Reproduce its exact expression, in quotation marks, with attribution | The presence of a live grant, plus that grant's attribution terms |
| **Paraphrase-and-republish** | Rewrite its material into your own words and ship the result | NoDerivatives blocks it, ShareAlike dictates the derivative's licence, NonCommercial follows it downstream |

Three consequences that a competent person gets wrong in a predictable order:

1. **Citing needs no licence at all.** Facts, titles, URLs and standards alignments are not
   protected expression. ShareAlike, NonCommercial and NoDerivatives do not touch citation. An
   all-rights-reserved host and a licence-silent PDF are both fully citable.
2. **Quoting does not trigger ShareAlike.** A quotation set inside your own prose with attribution
   is a use of the work, not an adaptation of it, so the copyleft condition has nothing to attach
   to.
3. **Paraphrase-and-republish is the operation the licences bite on,** and it is the one a
   curriculum repository actually performs. A close paraphrase that follows a specific task's
   structure, numbers and pedagogical move is an adaptation however different the wording.

The verdict vocabulary this wiki uses (`quote_and_adapt`, `quote_noncommercial`,
`quote_sharealike`, `cite_only`, `do_not_use`) is a compression of this table. Each verdict names
which of the three operations survive.

## When to reach for it

Reach for this page before writing a verdict on any host, and before accepting anyone else's
verdict on one. A sentence of the form "we cannot use MARS because it is NonCommercial" is almost
always wrong at the operation level: MARS material is citable without restriction, and the actual
blocker on that host is NoDerivatives, not NonCommercial. Reach for it likewise when a source is
described as open, closed or unavailable, because those words name access states rather than rights
states. See [[trap-access-is-not-a-rights-fact]].

Do **not** reach for this page to learn whether a specific host carries a grant. That is a fetch
against that host, and it belongs on the host's own `source` page under the evidence floor in this
wiki's `CLAUDE.md`.

## How it works

### Citing

Naming a source, linking to it, stating which standard it addresses, describing in your own words
what it does, and recording the bibliographic facts. This project's twelve-host sweep records
citation as permitted by every source in its table, without exception, which is why the
all-rights-reserved host (`openmiddle.com`), the NoDerivatives host (`map.mathshell.org`), the
withdrawn-grant host (`achievethecore.org`) and the licence-silent research PDFs on ERIC all
remain usable in a curate-and-cite build.

Two hosts in this corpus put it in writing. `https://eric.ed.gov/?copyright`, HTTP 200, fetched
2026-08-08, verbatim:

> ERIC does not retain copyright to the works indexed in the database and cannot grant permission
> to use indexed works under copyright protection.

And an all-rights-reserved paper hosted there, `files.eric.ed.gov/fulltext/EJ1064122.pdf`, HTTP
200, fetched 2026-08-08, carries an express carve-out, verbatim from the artifact:

> Using the hyperlinks to the article is not considered a violation of copyright.

Citation does carry mechanical constraints on some hosts, such as citing the page rather than the
file it serves, or citing an archive URL where the live host is broken. Those are not licence
constraints and they are executed at [[practice-cite-without-redistributing]].

### Quoting

Reproducing exact expression, in quotation marks, with attribution. Permitted wherever a live CC
grant is in force and its attribution conditions are met.

The reason quoting does not trigger ShareAlike is in the licence text, not in convention. CC
BY-NC-SA 4.0 legal code Section 3(b) opens, verbatim:

> In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the
> following conditions also apply.

and Section 1 defines its trigger term, verbatim:

> Adapted Material means material subject to Copyright and Similar Rights that is derived from or
> based upon the Licensed Material and in which the Licensed Material is translated, altered,
> arranged, transformed, or otherwise modified in a manner requiring permission under the
> Copyright and Similar Rights held by the Licensor.

An unmodified quotation is not translated, altered, arranged or transformed. No Adapted Material
exists, so Section 3(b) never fires. The same reasoning defeats NoDerivatives against a quotation,
since the quoted fragment is unmodified.

### Paraphrasing and republishing

Rewriting the material and shipping the result. Four regimes, and they are genuinely different:

- **NoDerivatives forbids it.** On `map.mathshell.org` the prohibition is stated three separate
  ways, verbatim from the host: `reproduced as-is`, `copied and distributed, unmodified`, and
  `reproduced and distributed, without modification`. The CC BY-NC-ND 3.0 legal code is stricter
  than its own deed here: Section 3 grants exactly two limbs, to reproduce and to distribute or
  publicly perform, then closes with `all rights not expressly granted by Licensor are hereby
  reserved`. Measured on the fetched bytes, the phrase `to create and Reproduce Adaptations`
  appears 1 time in the CC BY 3.0 legal code, 1 time in the CC BY-NC-SA 3.0 legal code, and
  0 times in the CC BY-NC-ND 3.0 legal code. The adaptation right is not granted at all.
- **ShareAlike permits it and dictates the output.** The derivative must ship under a Creative
  Commons licence with the same License Elements, this version or later, or a compatible licence.
  On every ShareAlike host in this corpus the elements are Attribution, NonCommercial and
  ShareAlike, so the obligation drags NonCommercial onto whatever file the derivative lands in.
- **NonCommercial permits it with no copyleft.** CC BY-NC 4.0's "Under the following terms" list
  has exactly three items: Attribution, NonCommercial and No additional restrictions. Your
  derivative does not have to ship under CC BY-NC 4.0. What travels is the NC constraint on the
  underlying material, not a licence obligation on your own contribution.
- **Plain attribution permits it cleanly.** CC BY 4.0's list has exactly two items, Attribution and
  No additional restrictions. Its only downstream rule is a floor rather than copyleft, Section
  3(a)(4), verbatim: "If You Share Adapted Material You produce, the Adapter's License You apply
  must not prevent recipients of the Adapted Material from complying with this Public License."

## In practice

**The IM task bank.** `tasks.illustrativemathematics.org` serves 24 in-scope tasks under CC
BY-NC-SA 4.0, byte-matched on all 24 task pages. Footer verbatim: "Typeset May 4, 2016 at
18:58:52. Licensed by Illustrative Mathematics under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License." Read across the three operations:
cite freely, quote freely with attribution, and do not paraphrase-and-republish, because under
design ruling R9 this repository ships CC BY 4.0 and takes no paraphrase from any ShareAlike
source. The verdict is `quote_sharealike`. See [[source-im-task-bank]].

**MARS.** `map.mathshell.org` says of itself, verbatim from the homepage sidebox: "All our
materials can be downloaded for free and may be reproduced as-is for non-commercial use. Precise
terms vary between materials." Citation is unrestricted, quotation of a short attributed span
would rest on fair use rather than on the grant, and paraphrase-and-republish is not licensed. The
verdict is `cite_only`. See [[source-mars-map]].

**Open Middle.** The site-wide footer read, verbatim on 2026-08-08 with a browser user agent,
"© 2016-2026 Glenrock Consulting, LLC. All rights reserved." Citation is unaffected by the loss of
the CC clause, because citation was never resting on it. What was lost is operations two and three.
See [[source-open-middle]] and [[license-withdrawn-grants]].

**The four AMC-derived IM tasks.** Tasks 1002, 1009, 916 and 918 sit under the same CC BY-NC-SA
footer as the other twenty, and their own IM Commentary states each was adapted from a 2012
American Mathematics Competition problem. Here the operation analysis stops early: the host's
grant cannot convey rights the host may not hold, so quotation is unavailable regardless of the
footer. That is a chain-of-title question, not a licence-term question. See
[[concept-chain-of-title]].

## Gotchas & constraints

**1. The deed is a summary and is not the licence, and on one instrument in this corpus they
disagree.** The CC BY-NC-ND 3.0 deed's NoDerivatives sentence is conditional and speaks only to
distribution, implying you may make a modified version so long as you do not distribute it. The
legal code never grants the right to make one. Write `cite_only` and do not soften it to "you may
adapt privately" on the strength of the deed.

**2. ShareAlike's trigger is Sharing, not producing.** The legal code says `if You Share Adapted
Material You produce`, and defines Share as provision to the public. Producing an adaptation that
is never provided to the public triggers nothing. This is the load-bearing difference for a
repository that drafts internally before deciding what to publish, and the deed's wording obscures
it.

**3. "Same license" is wider than same version.** The legal code permits a Creative Commons licence
with the same License Elements, this version or later, or a compatible licence. The compatibility
list at `creativecommons.org/compatiblelicenses` was not fetched by this project, so no page here
may name which licences qualify.

**4. A format change is not an adaptation** under the 4.0 licences. Section 2(a)(4), verbatim:
"For purposes of this Public License, simply making modifications authorized by this Section
2(a)(4) never produces Adapted Material." Converting a PDF to HTML does not put you in the third
operation.

**5. Quoting from a `cite_only` source is a fair-use judgment, and this project does not make it.**
No agent in this project performed a fair-use analysis. The conservative reading is what the
verdict records.

**6. The version changes the attribution duty, so never upgrade a 3.0 label to 4.0.** Under 3.0
the indication of changes is required only when you create an adaptation, and it sits inside the
grant as a condition of the adaptation right, so failing it means the adaptation was never
licensed. Under 4.0 the indication is required whenever you Share, and you must additionally
retain any indication of previous modifications. Measured on the fetched bytes, `title of the Work`
appears 1 time in the CC BY 3.0 legal code and 0 times in the CC BY 4.0 legal code.

**7. "Citing is unconstrained by every source in this corpus" is a measurement of this corpus,
not a statement of law.** It was measured across twelve hosts by this project on 2026-08-07 and
2026-08-08. A thirteenth host could carry a contractual term that reaches citation, and two hosts
here already carry non-licence use restrictions (IM's framing bar, SAP's framing bar) that a
citation practice must respect independently.

## Related

- [[license-cc-by]], [[license-noncommercial]], [[license-sharealike]] and
  [[license-noderivatives]] hold the four regimes named above, each with its own host inventory.
  [[license-public-domain-dedication]] holds the fifth case, where none of the three operations
  carries a condition, and [[license-unmarked-silence]] and [[license-all-rights-reserved]] hold
  the two states with no grant, where only the first operation survives.
- [[concept-chain-of-title]] can withdraw an operation the licence appears to grant.
  [[concept-third-party-carve-out]] is why the operation available on a page's prose may not be the
  operation available on its figures.
- [[trap-sharealike-contaminates-by-paraphrase]] is the mechanism by which the third operation
  reaches a file the writer never intended it to touch.
- [[concept-curate-and-cite]] is the posture that follows from this split.

## Composes with

- [[practice-cite-without-redistributing]] executes the first operation as a procedure, including
  the page-versus-file and live-versus-archive choices named above.
- [[practice-build-a-source-table]] is where each host is assigned one of the five verdicts, and
  this page is the vocabulary that assignment is written in.
- [[k12-density-rules]] governs how much quoted material a shipped artifact may carry once the
  second operation is cleared.

## References

Creative Commons instruments, staged verbatim 2026-08-08 from raw fetches with no summarizing
layer, all HTTP 200. `sources/cc-by-4-0.md` (deed 32178 bytes, legal code 48970) for the two-item
conditions list, Sections 3(a)(4) and 2(a)(4), and the attribution enumeration.
`sources/cc-by-3-0.md` for the 3.0 changes-indication regime and the title requirement.
`sources/cc-by-nc-4-0.md` for the three-item conditions list and the NonCommercial definition.
`sources/cc-by-nc-sa-4-0.md` (deed 37346, legal code 53058) for Section 3(b) complete and the
Adapted Material and Share definitions. `sources/cc-by-nc-nd-3-0.md` (deed 36916, legal code 50763)
for Section 3 complete and the measured absence of the adaptation grant. `sources/cc0-1-0.md` for
the absence of any attribution condition.

Host evidence, all primary, fetched by this project 2026-08-08: `sources/host-mars-map.md` for the
homepage sidebox, the four per-collection regimes and the artifact-versus-page mismatch;
`sources/host-im-task-bank.md` for the CC BY-NC-SA 4.0 footer byte matched on all 24 in-scope task
pages and the four AMC-derived tasks with their verbatim IM Commentary; `sources/host-eric.md` for
the ERIC copyright policy and the EJ1064122 hyperlink carve-out; `sources/host-open-middle.md` for
the live all-rights-reserved footer.

This project's own adjudication, cited as this project's measurement and not as any outside party's
statement: `sources/verdict-twelve-host-table.md`, reference, Section 2, the verdict key that is
the three-operation split this page states, and its four-value verdict table, which maps one to one
onto this wiki's snake_case vocabulary except that it contains no `do_not_use` row.
