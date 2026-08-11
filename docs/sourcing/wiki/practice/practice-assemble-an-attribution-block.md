---
title: Assemble an attribution block for a mixed-source deliverable
type: practice
sources:
  - sources/verdict-twelve-host-table.md
  - sources/cc-by-4-0.md
  - sources/host-im-kendall-hunt.md
  - https://creativecommons.org/licenses/by/4.0/
  - https://illustrativemathematics.org/terms-of-use/
  - NOTICE
  - Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md
updated: 2026-08-08
---

# Assemble an attribution block for a mixed-source deliverable

## Summary

This is a build step that runs once, over the finished used-source list, and emits the two
files whose contents a reader can check against the law: the repo `LICENSE` and
`alignment/attribution.md`. It is not a per-file habit and it is not a bibliography.

The mistake it exists to prevent: **one credit line applied to a package that drew on several
hosts and several record classes.** A single hard-coded string is the natural thing to write
and it is wrong in four independent ways at once. It gets the copyright holder wrong when the
grade band changes, it omits the notice that is mandated verbatim, it attaches a licence line
to sources that grant nothing, and it drops the indication that changes were made.

Under ruling R9 the repo itself ships CC BY 4.0 and takes no paraphrase from any ShareAlike
source. That makes this the only procedure in the `practice` family whose failure is visible
in the shipped artifact rather than in a working note.

The staged adjudication supplies paste-ready blocks at §4.1 through §4.10. This page is the
selection procedure that decides which of them a given record needs, and in what form.

## When to reach for it

Reach for it once, at the end, when the used-source list is closed and every entry on it has
a resolved host and a fetch date. Assembling early guarantees a re-run, because a source added
in the last authoring pass changes which blocks ship.

Reach for it also on any re-publication. Two grants in this corpus were withdrawn inside six
months, so an attribution file written against a stale fetch is a claim about a page that no
longer says what it said. See [[license-withdrawn-grants]] and
[[trap-license-withdrawn-after-citation]].

Do **not** reach for it to decide whether a source may be used at all. That question is
answered upstream, per host, by [[practice-build-a-source-table]] and the `source` pages. This
page assumes the verdicts already exist and only assembles their consequences.

Do not reach for it for a deliverable that only cites. Citation needs no licence and therefore
no licence line: see [[practice-cite-without-redistributing]], and §4.10 below.

## How it works

Six passes, in this order. The order matters, because pass 2 changes what pass 3 selects.

**1. Enumerate per record, never per host.** The unit of attribution is the record used, not
the organisation that published it. A package that quotes an HS lesson and cites a grade-8
prerequisite from the same host needs two different strings. See
[[concept-attribution-per-record]].

**2. Resolve the host from the URL.** One organisation in this corpus publishes under three
grants on three hosts with near-identical lesson titles. `im.kendallhunt.com` is CC BY 4.0,
`accessim.org` is CC BY-NC 4.0, `tasks.illustrativemathematics.org` is CC BY-NC-SA 4.0. The
brand name in a working note is not enough to select a block. See [[source-im-kendall-hunt]],
[[source-accessim-360]], [[source-im-task-bank]].

**3. Select the block by record class**, from the staged §4:

| Record class | Block | Note |
|---|---|---|
| Standard statement text | §4.1 | Two notices, both required, see below |
| IM 1st edition, `/HS/` path | §4.2 | IM's own suggested string, used verbatim |
| IM 1st edition, `/MS/` path | §4.3 | A different string, Open Up Resources is the base holder |
| IM v.360 on `accessim.org` | §4.4 | NonCommercial attaches downstream |
| IM 2016 task bank | §4.5 | ShareAlike, and no canonical string is published on that host |
| EngageNY / NYSED | §4.6 | The format itself is mandated |
| Mathematics Vision Project | §4.7 | Geometry Module 4 route only |
| Math Mistakes | §4.8 | Version is 3.0, not 4.0 |
| Arhin & Hokor 2021 | §4.9 | CC BY 4.0 research paper |
| Everything cite-only | §4.10 | Bibliographic form, **no licence line** |

**4. Carry the changes-made indication.** Under CC BY 4.0 it is required whenever you Share,
not only when you adapt. The deed's own footnote, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

Two duties sit in that sentence: indicate your own modification, and **retain** any indication
of previous modifications. IM's Terms §7.1 enumerates the same component, and the staged
adjudication's own note on §4.2 calls it one of the two components "that adapters most often
drop."

**5. Standards text triggers two notices, and they are not interchangeable.** The NGA/CCSSO
notice is mandated verbatim by the CCSS public license, per the staged extract: "Any
publication or public display shall include the following notice...". The Learning Commons
statement is separate, and there is no single form of it. The staged source states plainly:
"**There is no single string**; use the one attached to the record actually cited," and records
four forms, keyed to Multi-State/CCSS records, California records, learning-component records,
and lesson-metadata records. See [[source-corestandards-nga-ccsso]] and
[[source-learning-commons-kg]].

**6. Stamp every entry with its fetch date.** The staged framing of §4 says entries carry the
fetch date "because several of these terms are explicitly mutable." An entry without one is a
memory, not a claim.

## In practice

A working precedent for the same assembly already exists in this project's own tooling. The
`k12-lesson-toolkit` repo's `NOTICE` is one block per source, each retaining that source's own
licence and attribution statement rather than flattening them. Its Learning Commons entry
splits three grants inside one source, verbatim:

> ```
>     - State academic standards: CC BY 4.0, via 1EdTech.
>     - Learning components: CC BY 4.0, via Achievement Network (ANet).
>     - Learning progressions: CC0 1.0 (public domain), via Student Achievement Partners (SAP).
> ```

That is the shape to copy: one entry per rights position, not one entry per project.

### The URL band test, run per record

For any `im.kendallhunt.com` record, before a credit line is written:

- URL contains `/HS/` → §4.2. Credits Illustrative Mathematics.
- URL contains `/MS/` → §4.3. Must credit Open Up Resources as the 2017-2019 copyright holder
  of the base curriculum, with IM credited for the adaptations. Crediting only IM here is an
  incorrect attribution.
- Neither band, for example a K-5 path → **stop and fetch that page's own footer.** The K-5
  band was never sampled by this project and its footer is unverified.

### The two forms that look alike and are not

§4.2, IM's own suggested string, to be used verbatim:

```
Based on IM® K–12 Math authored by Illustrative Mathematics and licensed under CC BY 4.0.
https://creativecommons.org/licenses/by/4.0/
Source: https://im.kendallhunt.com/HS/  · Accessed 2026-08-07.
Changes were made to the original material.
```

§4.3, the grades 6-8 string, which names a different copyright holder for the base work:

```
IM 6–8 Math was originally developed by Open Up Resources and authored by Illustrative
Mathematics®, and is copyright 2017-2019 by Open Up Resources. It is licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0). Adaptations and updates
to IM 6–8 Math are copyright 2019 by Illustrative Mathematics, and are licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).
Source: https://im.kendallhunt.com/MS/  · Accessed 2026-08-07. Changes were made.
```

Same licence throughout, different holder, therefore a materially different obligation.

## Gotchas & constraints

**1. A licence line on a cite-only source is a false claim about that source.** §4.10 gives
four bibliographic forms with no licence line at all, covering MARS, Open Middle, Achieve the
Core and ERIC records. Writing "Licensed under..." beside a host that grants nothing asserts a
grant that does not exist. See [[license-unmarked-silence]] and [[license-all-rights-reserved]].

**2. The task-bank string must not be applied to four specific tasks.** The staged note on §4.5
is explicit: do not apply it "to tasks 1002, 1009, 916 or 918 as a basis for reproduction or
adaptation", because those are adapted from 2012 AMC 10A/10B problems and MAA's position is
unaddressed. A host's grant cannot convey rights the host does not hold. See
[[concept-chain-of-title]].

**3. The ShareAlike blocks are a warning, not a permission slip.** §4.5 exists so that a
ShareAlike record can be quoted and cited correctly. Under R9 nothing in this repo paraphrases
from a ShareAlike source at all, so if a §4.5 entry is being written for an adapted passage,
the adaptation is the defect and the attribution line will not repair it. See
[[trap-sharealike-contaminates-by-paraphrase]] and [[license-sharealike]].

**4. Three of the ten blocks were constructed, not published.** The staged source says of §4.5
that "No canonical string is published anywhere on that host"; of §4.7 that "No canonical
string is published"; and of §4.8 that "No attribution string is specified; the site offers a
bare CC BY widget. The document states this string was constructed." Those three are this
project's assembly from the host's own footer and copyright page, and a page that presents them
as the rights-holder's mandated wording misattributes them. §4.2 and §4.6 are the opposite
case: those two ARE the rights-holder's own published wording, IM's suggested string and
NYSED's mandated format.

**5. The attribution block does not clear embedded images.** Every IM curriculum footer says
"See the image attribution section for more information", and this project could not locate
that section: all 8 guessed paths returned 404 and no `href` containing "attribution" exists in
any sampled page. The recorded consequence is verbatim: **"the per-image license status for any
specific IM figure is UNVERIFIED from here."** Text attribution assembled correctly says nothing
about a figure. See [[concept-third-party-carve-out]].

**6. Names and marks sit outside the block.** IM's Terms §7.3 and the curriculum footer both
carve out the name, the logo and the "IM Certified" badge. Nominative citation is unaffected;
reproducing the logo in an attribution file is not covered by the grant it cites.

**7. Assembling from memory of a licence is the failure mode this whole wiki exists for.** The
entry that goes in the file is copied from the staged verbatim extract, which was copied from
raw fetch bytes. A summary layer once returned a licence sentence that was not present in the
document it was given. See [[trap-summary-layer-is-not-evidence]].

**8. Two of the ten blocks carry an unresolved question inside them.** The staged §3 correction
10 records that the Learning Commons CC BY 4.0 stamp and the NGA/CCSSO bespoke grant "do not
agree, and the CCSS one is narrower", and correction 12 lists which grant controls downstream
republication of CCSS statement text as unresolved. Shipping both notices, which §4.1 requires,
is the response to that; it is not a resolution of it.

## Related

- [[concept-attribution-per-record]] is the reason step 1 enumerates records rather than hosts.
- [[concept-cite-quote-adapt]] is the three-operation split that decides whether a record needs
  a licence line at all.
- [[concept-third-party-carve-out]] holds the two classes sitting outside a grant: embedded
  images, and names and marks.
- [[license-cc-by]] holds the attribution obligation this repo both consumes and takes on.
- [[license-sharealike]] and [[license-noncommercial]] are the riders that change what a block
  means downstream.
- [[license-withdrawn-grants]] is why every entry carries a fetch date.
- [[source-im-kendall-hunt]], [[source-accessim-360]] and [[source-im-task-bank]] are the three
  hosts the band test separates.
- [[source-corestandards-nga-ccsso]] and [[source-learning-commons-kg]] are the two parties
  whose notices §4.1 ships together.
- [[practice-cite-without-redistributing]] is the discipline for the records that never reach
  this file.

## Composes with

- [[practice-build-a-source-table]] produces the used-source list and the fetch dates this
  procedure consumes. Running this page against a stale source table produces a confident
  attribution file about pages that have changed.
- [[practice-format-a-lesson-package]] and [[practice-format-an-assessment-artifact]] are where
  the records get used, and therefore where the used-source list is actually written.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/verdict-twelve-host-table.md`, reference. §4 THE ATTRIBUTION BLOCK reproduced
  byte-exact, §4.1 through §4.10; §2 the verdict key and the three operations; §3 corrections
  5, 6, 10 and 12.
- `sources/cc-by-4-0.md`, primary. The deed's Attribution clause, its `indicate if changes were
  made` footnote, and legal code Section 3(a)(1). Deed fetched 2026-08-08, HTTP 200, 32178
  bytes; legal code HTTP 200, 48970 bytes, by `curl -sS -L` with raw bytes parsed locally.
- `sources/host-im-kendall-hunt.md`, primary. The two verbatim band footers, the Terms §7.1 and
  §7.3 text, and the image-attribution gap with its 8 recorded 404 paths.

Rights-holder pages behind those extracts:

- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, fetched 2026-08-07, header
  "Effective as of May 21, 2026". §7.1 the CC BY 4.0 grant and its suggested attribution
  string; §7.3 the trademark carve-out.
- `https://creativecommons.org/licenses/by/4.0/` HTTP 200, fetched 2026-08-08.

This project's own working files, cited as this project's measurement rather than any outside
party's statement:

- `NOTICE`, read in full 2026-08-08. The
  one-block-per-source precedent, including the three-way split inside the Learning Commons
  entry.
- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §2 ruling R9 and §6 the
  `alignment/attribution.md` slot in the repo tree.
