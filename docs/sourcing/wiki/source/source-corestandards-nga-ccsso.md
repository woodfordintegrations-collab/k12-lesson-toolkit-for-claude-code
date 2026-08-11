---
title: "thecorestandards.org (NGA Center / CCSSO, the CCSS Public License)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/
  - https://www.thecorestandards.org/public-license/
  - https://www.corestandards.org/public-license/
  - sources/host-learning-commons-kg.md
  - sources/verdict-twelve-host-table.md
  - sources/k12-lesson-toolkit-boundaries.md
updated: 2026-08-08
---

# thecorestandards.org (NGA Center / CCSSO, the CCSS Public License)

## Summary

The NGA Center for Best Practices and the Council of Chief State School Officers own the Common
Core State Standards. Every standard statement this project reproduces is their text. They licence
it under a bespoke public licence that is **not** a Creative Commons instrument, and that carries a
**purpose limitation** CC BY 4.0 does not have, together with a **mandated verbatim notice
containing the words "All rights reserved"**, **auto-termination on breach**, and **Washington DC
law and forum**.

**Read the verdict field before you use it.** `cite_only` is the floor, not a description. The
enumerated grant is to "copy, publish, distribute, and display" the standards; adaptation is not in
that list. And whether this grant or Learning Commons' CC BY 4.0 stamp controls downstream
republication of the same statement text is an open legal question this corpus refuses to answer in
three separate places. `cite_only` records the one operation nobody disputes. It is **not** a
finding that quotation is prohibited, and it must not be read as a reason to paraphrase a standard
instead of quoting it, which would be the worse operation. What the build actually does is set out
under "What you may do with it".

**This page's evidence is second-hand and stale, and that is on its face by design.** No dedicated
host agent ever ran on this domain. Its entire evidence base is §9 of the Learning Commons
verification report, one agent working outside its assigned host. The live licence page is
Cloudflare-403 to every client tried. The only readable copy is a Wayback snapshot timestamped
**2025-12-21**, which the report records as roughly 7.5 months stale as of its own fetch date, and
which the licence's own text says may be superseded, because NGA Center and CCSSO reserve the right
to re-release under different terms. `INVENTORY.md` flags this as the thinnest row in the wiki and
two of its five listed sources are still marked `pending`.

The row is kept anyway, for one reason: this is a **different party** from Learning Commons.
Learning Commons is a redistributor stamping CC BY 4.0. NGA Center and CCSSO are the owner granting
narrower terms. Collapsing the two encodes the exact error the Learning Commons report calls the
finding that matters most. See [[source-learning-commons-kg]].

## When to reach for it

Reach for this page **whenever a Common Core statement is reproduced anywhere in a deliverable**,
which under this project's rulings is every lesson, both exams and every quiz. The reach is the
whole build. What you take from here is one line, the mandated notice, and the knowledge that it is
mandated verbatim rather than suggested.

Reach for it the moment anyone is about to write "the standards are CC BY 4.0". They are CC BY 4.0
**on the Learning Commons layer**, which is a redistributor's stamp. At the primary source they are
not Creative Commons at all.

Do **not** reach for this host for the standard text itself. It is Cloudflare-403 and the grounded,
verbatim statements with their CASE identifiers and jurisdiction come from
[[source-learning-commons-kg]] through the store. Fetching them from here is neither possible today
nor necessary.

Do **not** reach for this page as a statement of the currently effective terms, or for a legal
conclusion about which grant controls. It records what the terms said on 2025-12-21, and the
licence reserves the right to change them. Nobody in this project made the which-grant judgment,
and three separate documents record that refusal. See gotchas 3 and 9.

## What its own page says

The quotations below were retrieved from the Wayback snapshot by a verifying agent on 2026-08-08
and are staged verbatim in `sources/host-learning-commons-kg.md` §9. Nothing rests on a summarizing
layer; see [[trap-summary-layer-is-not-evidence]].

### The reachability table, because the failure mode is part of the finding

| URL | Method | Status |
|---|---|---|
| `https://www.corestandards.org/public-license/` | curl plus browser UA | **HTTP 404**, redirecting to `corestandards.org/public-license/` |
| `https://www.thecorestandards.org/public-license/` | curl plus browser UA | **HTTP 403**, body "Enable JavaScript and cookies to continue" |
| `https://www.thecorestandards.org/` (root) | curl plus browser UA | **HTTP 403** |
| `https://www.thecorestandards.org/public-license/` | WebFetch | **HTTP 403 Forbidden** |

Two near-identical hostnames, two different failures. The report's classification: a **bot block on
a live site**, specifically a Cloudflare JavaScript challenge, not a dead host. The canonical host
is now `thecorestandards.org`; the bare `corestandards.org/public-license/` path 404s. Wayback CDX
confirms continuous HTTP 200 snapshots through 2025-12-21.

Source of every quotation that follows:
`https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/`,
HTTP 200, fetched 2026-08-08.

### The header

> THE COMMON CORE STATE STANDARDS ARE PROVIDED UNDER THE TERMS OF THIS PUBLIC LICENSE. THE COMMON CORE STATE STANDARDS ARE PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE COMMON CORE STATE STANDARDS OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

### The grant, with the purpose limitation the report says must not be paraphrased away

> The NGA Center for Best Practices (NGA Center) and the Council of Chief State School Officers (CCSSO) hereby grant a limited, non-exclusive, royalty-free license to copy, publish, distribute, and display the Common Core State Standards for purposes that support the Common Core State Standards Initiative. These uses may involve the Common Core State Standards as a whole or selected excerpts or portions.

> NGA Center/CCSSO shall be acknowledged as the sole owners and developers of the Common Core State Standards, and no claims to the contrary shall be made.

Four verbs are enumerated: copy, publish, distribute, display. Adaptation, modification and the
preparation of derivative works are not among them, and the header sentence above prohibits any use
not authorised by the licence or by copyright law. This page records that absence as a measurement
of the enumerated list and draws no legal conclusion from it.

### The mandated notice

> Any publication or public display shall include the following notice: '© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved.'

> States and territories of the United States as well as the District of Columbia that have adopted the Common Core State Standards in whole are exempt from this provision of the License.

### The examples carve-out

> This License extends to the Common Core State Standards only and not to the examples. A number of the examples are comprised of materials that are not subject to copyright, such as due to being in the public domain, and others required NGA Center and CCSSO to obtain permission for their use from a third party copyright holder.

> With respect to copyrighted works provided by the Penguin Group (USA) Inc., duplication, distribution, emailing, copying, or printing is allowed only of the work as a whole.

### Termination, mutability, and forum

> This License and the rights granted hereunder will terminate automatically as to a licensee upon any breach by that licensee of the terms of this License.

> NGA Center and CCSSO reserve the right to release the Common Core State Standards under different license terms or to stop distributing the Common Core State Standards at any time; provided, however that any such election will not serve to withdraw this License with respect to any person utilizing the Common Core State Standards pursuant to this License.

> This License shall be construed in accordance with the laws of the District of Columbia, without regard to conflicts principles, and as applicable, US federal law. A court of competent jurisdiction in Washington, DC shall be the exclusive forum for the resolution of any disputes regarding this License…

The trailing ellipsis is the report's own elision marker.

Page footer, as captured: "© 2021 Common Core State Standards Initiative". The notice the licence
mandates says 2010. Both are reproduced; neither is reconciled here.

## What you may do with it

| Operation | What the enumerated grant says | What this project does |
|---|---|---|
| Cite: name the standard, give its code, link the source, describe what it addresses | unconstrained; no licence is needed to cite | done everywhere |
| Quote: reproduce a statement verbatim | "copy, publish, distribute, and display" is granted, "for purposes that support the Common Core State Standards Initiative" | done **exactly once per package**, with both notices attached |
| Paraphrase and republish a standard's text | not enumerated; the header prohibits unauthorised use | **not done, and not needed** |

The frontmatter `verdict: cite_only` is the conservative floor described in the Summary. The row
above is what the document actually says. They differ because the wiki's five-term vocabulary
describes Creative Commons-shaped grants and this grant is not one; recording `quote_and_adapt`
here would assert an adaptation right the enumerated list does not contain, which is the error this
page exists to prevent.

### The notice, paste-ready

Required whenever a Common Core statement is reproduced. The wording is mandated by the licence, so
it is copied, not composed:

```
Common Core State Standards
© Copyright 2010. National Governors Association Center for Best Practices and
Council of Chief State School Officers. All rights reserved.
http://www.corestandards.org/
```

It ships **alongside**, never instead of, the Learning Commons per-record attribution string for
the record actually used. There is no single Learning Commons string; four distinct forms touch
this unit. Both notices, selected and assembled, are the job of
[[practice-assemble-an-attribution-block]].

### Why the build only ever needs one quotation

[[k12-density-rules]] fixes that a standard is quoted verbatim exactly once in a whole package and
referenced by code plus a short gist everywhere after. That rule is a density rule in origin and a
licensing rule in effect: it gives the notice obligation on this page a single, findable place to
attach, instead of scattering an obligation across every document in a set. The one quotation and
the two notices travel together.

### Three conditions that are easy to miss

- **The adopting-state exemption is a real carve-out and probably is not yours.** States,
  territories and the District of Columbia that adopted the standards in whole are exempt from the
  notice provision. A private repository is not a state. Assume the notice applies.
- **The licence does not reach the examples.** It "extends to the Common Core State Standards only
  and not to the examples", some of which are third-party material cleared only for NGA Center and
  CCSSO, and one class of which, the Penguin Group works, may only be reproduced whole. If material
  from a standard's illustrative examples enters a deliverable, this grant does not cover it. See
  [[concept-third-party-carve-out]].
- **Breach terminates the grant automatically**, with no cure period and no notice requirement on
  their side. Dropping the mandated notice is a breach of the provision that mandates it.

## Gotchas & constraints

**1. This is the thinnest evidence base in the wiki and the page says so rather than reading as
firm.** No dedicated host agent ran on this domain. Everything above comes from §9 of a report
whose assigned host was Learning Commons. Two of the five sources listed on this row in
`INVENTORY.md` are marked `pending`. Treat the licence text as well evidenced for 2025-12-21 and
treat everything about its current status as open.

**2. The snapshot is stale, and the licence itself says the terms are changeable.** The capture is
2025-12-21, recorded by the report as roughly 7.5 months stale as of its 2026-08-08 fetch. The
licence reserves the right to "release the Common Core State Standards under different license
terms or to stop distributing" them at any time, with a saving clause for people already using them
under it. A grant with a re-release clause and a seven-month-old snapshot is exactly the shape of
claim that got two other grants in this corpus wrong. See [[license-withdrawn-grants]] and
[[trap-license-withdrawn-after-citation]].

**3. HTTP 403 is a block, not a death, and this one is cheaply closeable.** The body reads "Enable
JavaScript and cookies to continue", which is a Cloudflare JavaScript challenge. curl runs no
JavaScript and neither does WebFetch, so both failures are evidence about the client, not about the
site. The verdict table lists this under gaps closeable by a further fetch and names the fix: a
real browser session would clear the challenge. It was not escalated to. Until it is, no claim on
this page describes the live document. See [[trap-down-is-not-one-state]] and
[[trap-access-is-not-a-rights-fact]].

**4. The mandated notice contains the words "All rights reserved", inside a page you are
republishing.** The report flags this in those terms. It is not a contradiction and it is not an
error to be smoothed: the owner reserves rights and grants a limited licence, and the notice is the
form the reservation takes. Reproduce it exactly. Do not soften it, do not convert it to a
Creative Commons badge, and do not omit it because a nearby Learning Commons string already says
CC BY 4.0. See [[license-all-rights-reserved]].

**5. The purpose limitation has no Creative Commons analogue and nobody in this project has
measured against it.** "For purposes that support the Common Core State Standards Initiative" is a
condition on the grant. CC BY 4.0 has nothing like it; its deed says "for any purpose, even
commercially". Whether a given deliverable supports the Initiative is a judgment, and no agent in
this project made it. What is recorded is the sentence, quoted above, and the instruction not to
paraphrase it away.

**6. Two hostnames, two different failures, and the older one is dead.**
`www.corestandards.org/public-license/` returns 404. `www.thecorestandards.org/public-license/`
returns 403. A citation still pointing at the older path is pointing at nothing. The mandated
notice's own URL line is `http://www.corestandards.org/`, which is what the licence text specifies
and is reproduced above as specified rather than corrected.

**7. The PDF named inside the Learning Commons attribution string was never fetched.** Multi-State
records, which in this unit are HSG-SRT.B.5 and C.7, carry an attribution sentence pointing at
`https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf`. That URL is recorded
verbatim from the export's attribution text. No agent opened it. Whether it resolves, and what
notice it carries internally, is unverified. It is listed as `pending` on this row.

**8. The 2010 notice date and the 2021 site footer are both real.** The mandated notice says
"© Copyright 2010". The captured page footer says "© 2021 Common Core State Standards Initiative".
Ship the notice as mandated; do not update its year to match the footer, and do not treat the
mismatch as evidence the notice is obsolete.

**9. The upstream and downstream grants do not agree, and this project does not resolve it.**
Learning Commons stamps CCSS statement text CC BY 4.0. NGA Center and CCSSO licence the same text
under narrower terms. The report states the honest position, that the two grants do not agree and
the CCSS one is narrower, and records which controls downstream republication as a legal question
outside its competence. The verdict table repeats the refusal, listing it among questions "for
counsel, not for a fetch". Learning Commons' own Terms push the risk to you in writing: "you agree
to review any applicable license terms associated with Content before accessing or using it. You
are responsible for ensuring compliance." **The mitigation does not require the answer.** Ship both
notices; it costs one line. See [[concept-chain-of-title]] and
[[concept-attribution-per-record]].

**10. Breach terminates automatically and the forum is Washington DC.** Neither changes what you
may do; both change what happens if you get it wrong. CC BY 4.0 gives an inadvertent violator a
30-day cure window. This licence has no cure period in its text.

**11. The CCSS trademark is a separate reservation**, recorded elsewhere in this corpus as
NGA/CCSSO, all rights reserved. Citing the standards by name is ordinary nominative use; branding
something with the mark is not. See [[concept-third-party-carve-out]].

## Related

- [[source-learning-commons-kg]] is the redistributor whose CC BY 4.0 stamp sits over this text.
  The gap between the two is why both pages exist.
- [[license-all-rights-reserved]] is where the mandated notice's own words belong. This grant is
  deliberately **not** duplicated there or as a ninth `license` row; it lives here and is reached
  from that page and from [[k12-density-rules]].
- [[license-cc-by]] is the regime this grant is repeatedly mistaken for, and the comparison that
  makes the purpose limitation visible.
- [[license-withdrawn-grants]] and [[trap-license-withdrawn-after-citation]] carry the mutability
  record that dates every claim on this page.
- [[concept-chain-of-title]] is the general form of gotcha 9, and
  [[concept-attribution-per-record]] is why this notice ships beside a per-record string rather
  than instead of one.
- [[concept-third-party-carve-out]] holds the examples carve-out and the trademark reservation.
- [[trap-down-is-not-one-state]] is what keeps a 403 from being filed as a dead host, and
  [[trap-access-is-not-a-rights-fact]] is the converse: a 200 would have proved nothing either.
- [[trap-summary-layer-is-not-evidence]] is why the licence text above is a pasted archive byte.

## Composes with

- [[practice-assemble-an-attribution-block]] consumes the mandated notice above together with the
  Learning Commons per-record string into the shipped LICENSE and attribution file.
- [[k12-density-rules]] owns the quote-the-standard-verbatim-exactly-once rule, which is the single
  point in a package where this notice obligation attaches.
- [[practice-build-a-source-table]] is the fetch-and-record procedure that would close the 403 with
  a browser session and re-date this verdict.

## References

Fetched by this project on 2026-08-08:

- `https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/`
  HTTP 200. **Snapshot timestamp 2025-12-21.** The entire licence text quoted above.
- `https://www.thecorestandards.org/public-license/` HTTP 403 to curl with a browser user agent and
  HTTP 403 Forbidden to WebFetch, body "Enable JavaScript and cookies to continue".
- `https://www.thecorestandards.org/` HTTP 403.
- `https://www.corestandards.org/public-license/` HTTP 404, redirecting to
  `corestandards.org/public-license/`.
- Wayback CDX, confirming continuous HTTP 200 snapshots of the licence page through 2025-12-21.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-learning-commons-kg.md`, primary for this page. §9 is the only place in the corpus
  where this host was probed: the four-row status table, the licence text verbatim, and the
  upstream and downstream mismatch finding. §11 records what could not be verified, including
  whether the notice requirement is currently enforced.
- `sources/verdict-twelve-host-table.md`, reference. §3 correction 10 ("The CCSS text itself is not
  CC BY 4.0 at the primary source"), §4.1 the dual-notice attribution block, §6 the closeable-gap
  entry naming Playwright as the fix and the unresolved which-grant-controls question.
- `sources/k12-lesson-toolkit-boundaries.md`, reference. §6.4 the repository `NOTICE`, which already
  carries a CCSS line reading "Used under the CCSS public license", and the repository's own open
  legal item recording the same question as unresolved.

Not verified by anyone in this project, and named here so the gap is visible: the live text of the
licence, whether the 2010 notice requirement is currently enforced, whether
`Math_Standards1.pdf` resolves and what it carries, and which of the two grants controls downstream
republication of CCSS statement text. The last of these is recorded in three separate documents as
a question for counsel rather than for a fetch.
