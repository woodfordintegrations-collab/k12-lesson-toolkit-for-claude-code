---
title: "ShareAlike (the SA rider)"
type: license
sources:
  - https://creativecommons.org/licenses/by-nc-sa/4.0/
  - https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en
  - https://creativecommons.org/licenses/by-nc-sa/3.0/
  - https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode.en
  - sources/cc-by-nc-sa-4-0.md
  - sources/cc-by-nc-sa-3-0.md
  - sources/cc-by-4-0.md
  - sources/host-im-task-bank.md
  - sources/host-engageny-nysed.md
  - sources/host-mars-map.md
  - sources/host-achieve-the-core.md
  - sources/host-learning-commons-kg.md
  - sources/host-openstax.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# ShareAlike (the SA rider)

## Summary

ShareAlike is the live constraint on this build and the only rider here whose failure mode is
silent. It blocks nothing at the moment it is violated. It changes what licence the file you wrote
must ship under, and a contaminated file is byte-indistinguishable from a clean one.

**SA does not touch citation and is not triggered by quotation.** It is triggered by
paraphrase-and-republish, which is the operation a curriculum repo actually performs. A close
paraphrase following a specific task's structure, numbers and pedagogical move is an adaptation
however different the wording.

**SA is not one instrument.** Four surfaces here carry it at three versions, and the versions
genuinely differ:

| Where | Version as measured | How the version is pinned |
|---|---|---|
| `tasks.illustrativemathematics.org` | CC BY-NC-SA **4.0** | Named in the footer prose, byte-matched on all 24 in-scope task pages |
| EngageNY resources via NYSED | **3.0 Unported** site-wide, **3.0 US** per resource | Prose names no version; the site-wide anchor is `by-nc-sa/3.0/`, every per-resource badge image is `.../3.0/us/` |
| `map.mathshell.org` PD Modules | **3.0** | Visible text carries no version at all; only the `href` says 3.0 |
| IM-authored PDFs on `achievethecore.org` | **4.0 and 3.0, in one file** | One line says 4.0 International, another says 3.0 Unported |

This project's own ruling is stricter than any of them. Recorded verbatim in `INVENTORY.md` from
the design spec §2: **"The repo ships CC BY 4.0 and writes from standard text only. No paraphrase
from any ShareAlike source, ever."** The project ruled the same on 2026-08-08.

## When to reach for it

Reach for this page the moment a source you want prose from carries an SA label, before any
drafting. The decision is cheap now and expensive once the paraphrase sits in a file with other
material.

Reach for it when you need to know whether internal drafting triggers anything. It does not, and
the deed's wording is what makes people think it does.

Reach for it when a version number is missing from a notice, because on two of the four surfaces
above it is missing from the visible text and recoverable only from an `href` or a badge path.

Do not reach for this page for the contamination mechanism or the worked instance in this
project's record. That is [[trap-sharealike-contaminates-by-paraphrase]]. This page is the
instrument and the host inventory.

## How it works

### The deed's sentence, and the two things it hides

CC BY-NC-SA 4.0 deed, verbatim:

> **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

`same license` is a hyperlink to a footnote, verbatim:

> **same license** — You may also use a license listed as compatible at https://creativecommons.org/compatiblelicenses

Both strings are byte-identical to the CC BY-NC-SA **3.0** deed, verified by extracting the
footnote from both fetched pages and comparing. Creative Commons now serves one deed template
across versions, which means **the deed cannot tell you which version's rules you are under.**

### The 4.0 licence, which says something narrower and something wider

Legal code Section 3(b), complete and verbatim:

> **ShareAlike.**
>
> In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the following conditions also apply.
>
> The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.
>
> You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.
>
> You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.

**Narrower: the trigger is Sharing, not producing.** The deed reads as though the duty attaches on
creation. The licence says `if You Share Adapted Material You produce`, and `Share` is defined as
`to provide material to the public`. An adaptation that is never shared triggers nothing. For a
repository that drafts internally before deciding what to publish, this is the most load-bearing
difference between the deed and the licence.

**Wider: `same license` means same License Elements, this version or later.** `License Elements`
is defined as `the license attributes listed in the name of a Creative Commons Public License`,
and for this instrument they are `Attribution, NonCommercial, and ShareAlike`. The deed's word
`same` is looser than the licence, in the licensee's favour.

Whether a paraphrase is caught at all turns on the `Adapted Material` definition: material
`modified in a manner requiring permission under the Copyright and Similar Rights held by the
Licensor`. Where no permission would be required, there is no Adapted Material and SA does not
attach. That is the seam [[concept-cite-quote-adapt]] sits on, and it is a judgment rather than a
lookup.

### The 3.0 licence, which offers no compatibility route at all

**This is the divergence.** Measured on the fetched bytes: `Creative Commons Compatible License`
and `compatiblelicenses` appear **0 times** in the CC BY-NC-SA 3.0 legal code, while
`compatiblelicenses` appears **2 times** on the 3.0 deed page. **The deed offers a route the
licence it summarizes does not contain.** The 3.0 clause opens, verbatim:

> You may Distribute or Publicly Perform an Adaptation only under: (i) the terms of this License; (ii) a later version of this License with the same License Elements as this License; (iii) a Creative Commons jurisdiction license (either this or a later license version) that contains the same License Elements as this License (e.g., Attribution-NonCommercial-ShareAlike 3.0 Unported) ("Applicable License").

Three permitted Applicable Licenses, exhaustively, and no compatibility list. Do not tell a reader
they may relicense a BY-NC-SA 3.0 adaptation under something merely listed as compatible.

Two further 3.0 facts. **What the obligation covers differs**: 3.0 constrains the licence of the
Adaptation as a whole, where 4.0 constrains the Adapter's License applied to `Your contributions`.
And the served page carries a defect that survives quotation: the clause is `id="s4b"`, so it is
Section 4(b), but its own closing self-reference reads `This Section 4(d), applies to the
Adaptation` and its anchor links to `#s4d`, the attribution clause. Attribution genuinely is 4(d)
in this instrument, because ShareAlike takes 4(b) and NonCommercial takes 4(c). The
cross-reference inside 4(b) is simply wrong, and the stray comma is in the bytes.

### The measurable weight of the rider

Section 3(a) of the CC BY-NC-SA 4.0 legal code is 2136 characters against 1554 for CC BY 4.0 and
CC BY-NC 4.0. The excess is the ShareAlike subsection; Section 3(a) itself is unchanged. Section
3(b) adds a **second** licence-inclusion duty on top of Section 3(a)(1): include the underlying
licence, and separately include the Adapter's License.

One grep warning. The 4.0 legal code is inconsistent about the apostrophe in `Adapter's License`,
counted on the fetched bytes: 2 curly (U+2019) against 3 straight (U+0027). **A search for either
form alone will miss occurrences.**

## In practice

**The IM task bank, CC BY-NC-SA 4.0.** Footer, verbatim:

> Typeset May 4, 2016 at 18:58:52. Licensed by Illustrative Mathematics under a
> Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

Recorded as identical markup on `/content-standards` and on every task page checked, with all 24
in-scope tasks fetched and their footers confirmed by byte match. No task overrides it. This is
the host most likely to be reached for in this build, because it holds 24 tasks on exactly the
five target standards, and its ShareAlike term is what makes it quote-only here. See
[[source-im-task-bank]].

**EngageNY via NYSED, version disputed.** The live successor statement says files `will remain
free and licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)
license` and names no version. The anchor `href` is `by-nc-sa/3.0/`, which is Unported. Every
per-resource badge points at `i.creativecommons.org/l/by-nc-sa/3.0/us/80x15.png`, which is 3.0 US,
a different legal instrument. The per-resource anchor is misspelled `/licences/` and 404s at
Creative Commons, so **the badge image path is the reliable signal, not the link**. Container and
index pages carry no CC notice at all: `/resource/high-school-geometry` returned 0 matches on
three independent greps. See [[source-engageny-nysed]].

**MARS PD Modules, the one non-ND grant on that host.** Verbatim:

> The Professional Development Modules may be distributed under the
> [Creative Commons Attribution Noncommercial Share-Alike license].

`href` is `by-nc-sa/3.0`. The visible text carries no version, there is no "unmodified", and there
is no "all other rights reserved", all three unlike every other grant on that host. It is more
permissive than its neighbours and must be quarantined from repo prose for exactly that reason.
See [[source-mars-map]].

**IM-authored PDFs on `achievethecore.org`, internally inconsistent.** From
`Grade 8 IM task - equations of lines final06.26.14.pdf`, `pdftotext` output, verbatim by line:

> line 148: "Typeset May 4, 2016 at 22:05:25. Licensed by Illustrative Mathematics under a"
> line 149: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ."
> line 172: "8.EE Equations of Lines is licensed by Illustrative Mathematics"
> line 173: "under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License"

Both are BY-NC-SA; the version is recorded as genuinely ambiguous on the face of the document.
This is also the hard counterexample to the folk belief that Achieve the Core content carries a
blanket public-domain dedication. See [[source-achieve-the-core-sap]].

**An SA claim hiding inside a nominally CC BY 4.0 export.** In the Learning Commons v1.11.0
export, the `license` field reads `https://creativecommons.org/licenses/by/4.0/` on all 247,786
nodes with zero exceptions. Separately, 6,214 records carry an attribution statement asserting a
CC BY-NC-SA licence, of which Georgia mathematics is 1,699. The Math form, verbatim:

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Georgia Mathematics standards are provided by the Georgia Department of Education, which asserts a CC BY-NC-SA license."

The machine-readable field and the human-readable attribution contradict each other on those
records. They are not in this unit's path, which runs on Multi-State and California, but **the
`license` field alone is not a sufficient check on that export.** See
[[source-learning-commons-kg]] and [[concept-attribution-per-record]].

**OpenStax second-edition maths titles.** Of ten maths slugs queried on 2026-08-08, eight returned
`license_name: Creative Commons Attribution-NonCommercial-ShareAlike License` with
`license_version: 4.0`. See [[source-openstax]].

## Gotchas & constraints

**1. Citing is never affected, and quoting does not trigger SA.** A quotation set inside your own
prose with attribution is a use of the work, not an adaptation of it. Every SA source here stays
fully citable and, where a live grant exists, quotable.

**2. The failure is silent, which is why the rule is a prohibition rather than a check.** A
paraphrase from an SA source and one from a CC BY source render identically in a file. Nothing
raises an error, no lint catches it, and the consequence lands on the licence of whatever file it
went into. That is why ruling R9 forbids the operation outright rather than asking for care. See
[[trap-sharealike-contaminates-by-paraphrase]].

**3. SA drags NonCommercial with it here.** Every SA surface in this corpus is BY-NC-SA, not BY-SA.
A derivative forced under BY-NC-SA acquires an NC obligation the repo never chose. See
[[license-noncommercial]].

**4. CC BY 4.0 cannot be the Adapter's License.** Section 3(b) requires a Creative Commons licence
with the same `License Elements`, and CC BY 4.0's elements are Attribution alone. Under R9 the
repo ships CC BY 4.0, so there is no version of "we will just relicense that file" that works.

**5. Do not read the deed's compatibility footnote onto a 3.0 source.** Measured zero occurrences
in the 3.0 legal code, where the compatibility list has no effect at all.

**6. `https://creativecommons.org/compatiblelicenses` was not fetched by this project.** Neither
staged extract can name which licences are BY-NC-SA compatible, and a page must not guess. What
would close it: fetch that page and stage it with its own date.

**7. `3.0 Unported` is not `3.0 US`, and the ported legal code is not staged here.** The EngageNY
conflict above cannot be resolved from `sources/`. Whether Unported or US governs where they
conflict is carried forward as an open gap by the host report itself, and it stays open here.

**8. The version is missing from the visible text on two of the four surfaces.** On MARS PD
Modules and on the live NYSED statement, a reader transcribing only what is rendered records no
version. Read the `href`, and where a badge image exists read its path too, because on EngageNY
the two disagree.

**9. NYSED states in writing that it is not the copyright owner**, and names no one who is. A
clean SA notice does not establish that the host had the right to grant it. See
[[concept-chain-of-title]].

**10. This inventory is a snapshot.** Every row carries a fetch date because two grants in this
corpus were withdrawn inside six months. See [[license-withdrawn-grants]].

## Related

- [[trap-sharealike-contaminates-by-paraphrase]] is the mechanism and the worked instance; this
  page is the instrument and the host inventory.
- [[license-cc-by]] is the baseline SA rides on and the licence the repo ships, which is what makes
  SA material unusable for adaptation here.
- [[license-noncommercial]] arrives with SA on every surface in this corpus.
- [[license-noderivatives]] is the stricter neighbour on `map.mathshell.org`, where the PD Modules
  are the SA exception.
- [[concept-cite-quote-adapt]] decides whether SA is even in play.
- [[concept-chain-of-title]] is why a clean SA footer is not the end of the analysis.
- [[source-im-task-bank]] is the 4.0 surface and the one most likely to be reached for.
- [[source-engageny-nysed]] is the version-conflict surface.
- [[source-mars-map]] holds the PD Modules exception.
- [[source-achieve-the-core-sap]] holds the internally inconsistent PDF.
- [[source-learning-commons-kg]] holds the SA assertion inside a nominally CC BY 4.0 export.
- [[source-openstax]] is the second-edition inversion.

## Composes with

- [[practice-cite-without-redistributing]] is the operation that keeps an SA source useful without
  triggering the rider.
- [[practice-build-a-source-table]] produces the dated version pins this inventory depends on.

## References

Instruments fetched by this project 2026-08-08, `curl -sS -L`, default user agent, raw bytes
parsed locally, no summarizing layer:

- `https://creativecommons.org/licenses/by-nc-sa/4.0/` HTTP 200, 37346 bytes, 0 redirects, and
  `.../by-nc-sa/4.0/legalcode.en` HTTP 200, 53058 bytes. Section 3(b), the Section 1 definitions,
  Sections 2(a)(5)(B) and 4(b).
- `https://creativecommons.org/licenses/by-nc-sa/3.0/` HTTP 200, 37273 bytes, 0 redirects, and
  `.../by-nc-sa/3.0/legalcode.en` HTTP 200, 56255 bytes. The `s4b` clause and the measured absence
  of any compatibility language.

Staged extracts in this wiki, all staged 2026-08-08: `sources/cc-by-nc-sa-4-0.md` (primary,
Section 3(b) complete, the trigger finding, the character counts and the apostrophe measurement);
`sources/cc-by-nc-sa-3-0.md` (primary, the compatibility divergence measured at 0 occurrences and
the served-page defects preserved); `sources/cc-by-4-0.md` (primary, the contrast baseline);
`sources/host-im-task-bank.md` (primary, the verbatim footer, the all-24 byte match and rider 2);
`sources/host-engageny-nysed.md` (primary, the live statement, the archived Terms and the
per-resource sampling table); `sources/host-mars-map.md` (primary, §3f the PD Modules grant);
`sources/host-achieve-the-core.md` (primary, Sample A); `sources/host-learning-commons-kg.md`
(primary, §6 the census and §7 the 6,214 records); `sources/host-openstax.md` (primary, the CMS API
responses); `sources/verdict-twelve-host-table.md` (reference, §2 verdict key, §3 correction 5,
§4.5 the task-bank attribution block).

This project's own record, cited as this project's ruling and not as any outside party's
statement: `INVENTORY.md` quotes design spec §2 ruling R9 verbatim; the project's governing ruling records
the project ruling the same on 2026-08-08.
