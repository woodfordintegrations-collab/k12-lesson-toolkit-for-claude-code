---
title: What the Learning Commons Knowledge Graph actually covers, and where it is empty
type: evidence
sources:
  - sources/host-learning-commons-kg.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/verdict-twelve-host-table.md
  - https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md
  - https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl
  - https://learningcommons.org/terms-of-use/
updated: 2026-08-08
---

# What the Learning Commons Knowledge Graph actually covers, and where it is empty

## Summary

The Learning Commons v1.11.0 public export holds **247,786 nodes across exactly 8 label values**.
Every one of them carries the same licence field. **None of them is a misconception.**

The error this page exists to prevent is a single sentence a builder writes without noticing:
*there are no documented misconceptions for this standard.* That sentence is what an empty
`find_misconceptions_for_standard` result looks like from the call site, and it is false in two
directions at once. The facet is empty for **every** code in the corpus, not for the one you
asked about, and misconception evidence for these standards exists in quantity outside this
export. An empty facet here is a boundary of the corpus. It is never a finding about the
standard.

The label census, as recorded verbatim in the staged extract:

| Label | Count |
|---|---|
| `StandardsFrameworkItem` | 222,865 |
| `LearningComponent` | 8,686 |
| `Activity` | 8,173 |
| `Assessment` | 4,516 |
| `Lesson` | 2,550 |
| `LessonGrouping` | 764 |
| `StandardsFramework` | 214 |
| `Course` | 18 |

Three of those labels are not what a reader assumes. `Activity`, `Assessment` and `Lesson` are
Illustrative Mathematics scope-and-sequence **metadata**, not lesson content, and none of them is
ingested into the store the tools read. That boundary is a separate page:
[[evidence-store-ingest-boundary]].

## When to reach for it

Reach for it before writing any sentence about what this corpus covers, and before reading any
empty result as an answer. It is the census that lets [[trap-empty-facet-reads-as-success]] be
diagnosed instead of believed.

Reach for it before writing an attribution line, because the uniform licence field is not a
uniform attribution string. Four distinct strings touch the five HSG-SRT codes and the operative
one is a property of the record, not of the host. See [[concept-attribution-per-record]] and
[[source-learning-commons-kg]].

Reach for it before pinning a copy, because Learning Commons' own Terms carry a revocation rider
and this export is a versioned artifact with a fetch date.

Do **not** reach for it for a count of a standard's learning components taken from the MCP. The
tool slices at five and says nothing about it: [[trap-learning-components-truncated-at-five]].

Do not reach for it to settle whether CC BY 4.0 governs the CCSS statement text downstream. The
upstream grant is narrower and is not Creative Commons at all: [[source-corestandards-nga-ccsso]].

## The claim

Four claims, each stated so it can be falsified by re-running one command against the pinned
export.

**C1. Size and shape.** The v1.11.0 export `nodes.jsonl` holds 247,786 nodes carrying exactly the
8 label values and counts in the table above. Falsifier: a ninth label, or any count that differs.

**C2. Licence uniformity in the field.** All 247,786 nodes carry
`"license":"https://creativecommons.org/licenses/by/4.0/"`, and zero nodes are missing the field.
Falsifier: one node with a different value or no field.

**C3. Misconceptions are absent by structure, not by query.** There is no `Misconception` node
label, no misconception relationship label, and no misconception discriminator on
`LearningComponent`. Falsifier: any of the three.

**C4. Attribution is per record.** The `attributionStatement` field varies by jurisdiction and by
node type. Falsifier: a single string covering the whole export.

**What these claims do not say.** They do not say CC BY 4.0 is the operative outbound grant for
the standard text a deliverable republishes; that question is open and the CCSS grant upstream is
narrower. They do not say the export is free of internal contradiction; C3 in particular sits
next to 6,214 records whose attribution prose contradicts their own licence field. They are
claims about **v1.11.0**, measured against a local copy downloaded 2026-07-22 and spot-checked
live on 2026-08-08, not about Learning Commons in general.

## What the evidence shows

### C1 and C2: the census, as run

The staged extract reproduces the commands and their output verbatim:

```
$ grep -o '"license":"[^"]*"' raw/nodes.jsonl | sort | uniq -c
247786 "license":"https://creativecommons.org/licenses/by/4.0/"
$ grep -cv '"license":' raw/nodes.jsonl
0
```

The report's own finding, in its own emphasis as transcribed: **every single node carries exactly
one license value, CC BY 4.0. Zero exceptions, zero nodes missing the field.**

The file this was run against is 292,652,341 bytes, mtime 2026-07-22, and its byte count matches
the size the upstream schema document publishes for the v1.11.0 export exactly. The live CDN was
re-fetched on 2026-08-08 and returned HTTP 206 on a Range request with no credential, no referer
check and no bot block. The first HSG-SRT.C.8 record on the wire carried
`license: https://creativecommons.org/licenses/by/4.0/`, matching the local copy.

**That spot check is one record.** It is evidence the local copy has not drifted on the field
checked. It is not a re-run of the 247,786-node census against the live stream.

### C3: the exhaustive check, verbatim

The upstream schema document's finding is reproduced in full in the staged extract because its
exhaustiveness is the point:

> ## 5. Misconceptions finding — DEFINITIVELY ABSENT
>
> Checked exhaustively:
> - **No `Misconception` node label** (the only 8 labels are listed in §2.1).
> - **No misconception relationship label** (the only 10 labels are listed in §3.1).
> - **No misconception discriminator on `LearningComponent`** (its properties are positive
>   sub-skills only; §2.4).
> - A case-insensitive scan for `misconception` finds it in **0** relationships and in **15**
>   nodes — all 15 are the ordinary English word appearing inside a standard's `description`/`notes`
>   text (e.g. *"Identify and dispel misconceptions about American Indians today"*), never a data
>   structure.

Downstream of that: `data/ca-math/misconceptions.jsonl` is **0 bytes**, every sibling file in that
directory is between 851,166 and 6,142,448 bytes, and the `misconceptions` table has **0 rows**.
The ingest builder's own docstring calls the empty file deliberate, verbatim: "``misconceptions.jsonl`` is empty
by design — no misconception data exists in the public export".

### C4: four strings, and a fifth that is quoted but appears on nothing

The first sentence is constant on every record the reporting agent examined, verbatim:

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license."

The second sentence is not. Measured on the California-math subset, the whole subset is covered by
five distinct strings, and the two that carry the unit's standard statements split by jurisdiction:
California records name the California Department of Education, Multi-State records name Common
Good Learning Tools. Learning components name Achievement Network. Crosswalk records carry the
first sentence alone.

The consuming repository's `NOTICE` hard-codes one string, the generic 1EdTech form from Learning
Commons' README. Measured across 2,303 standards records, 1,041 progression records, 6,056
component records and 591 crosswalk records, that string appears on **none** of them.

### The licence field is uniform and the rights position is not

Two measured facts sit against C2 and neither retires it.

- **6,214 records assert CC BY-NC-SA in their attribution prose while the `license` field still
  reads CC BY 4.0.** The Georgia math variant is 1,699 of them, reproduced verbatim in the staged
  extract. None is on this unit's path, which is Multi-State plus California. The conclusion the
  report draws is the one to carry: the `license` field alone is not a sufficient check.
- **The upstream CCSS grant is not Creative Commons.** NGA/CCSSO licence the same statement text
  under a bespoke grant with a purpose limitation and a mandated "All rights reserved" notice. The
  report is explicit that it cannot resolve which controls downstream republication, calls it a
  legal question rather than a measurement, and records the honest position: the two grants do not
  agree and the CCSS one is narrower. See [[source-corestandards-nga-ccsso]] and
  [[concept-chain-of-title]].

### Where CC0 does and does not appear, recorded unresolved

Learning Commons' `LICENSE.md` carves learning progressions out as CC0 from Student Achievement
Partners. Two staged measurements of that carve-out disagree, and they were run on **different
files**:

- Against the whole-export `nodes.jsonl`: a case-insensitive scan for `Student Achievement
  Partners` returned **0**, and all 1941 hits for `CC0|publicdomain` were false positives, a
  `cc0` substring inside a UUID. The report's conclusion is that the CC0 carve-out exists only in
  `LICENSE.md` prose.
- Against `data/ca-math/progressions.jsonl`: the `attributionStatement` on **all 1,041** records
  reads, verbatim, "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
  Learning Commons received learning progressions under CC0 from Student Achievement Partners.",
  and `properties.author` is `Student Achievement Partners` on all 1,041.

Progression records are edges and do not live in `nodes.jsonl`, which is what the first scan read.
The second extract records the discrepancy and states plainly that it does not resolve it, because
the full-export census was outside that agent's scope. This page carries both and resolves
neither. See [[license-public-domain-dedication]] for why an unqualified "CC0" is never enough.

## Gotchas & constraints

**1. The 15-variant figure is about C.6, and it is a property of the export.** The staged extract
records that `HSG-SRT.C.6` alone appears 15 times across jurisdictions, and names them. The
twelve-host verdict table phrases the same measurement as "HSG-SRT.C.6 exists in 15 state
variants, making cross-state alignment checkable", which reads as a property of that standard.
`INVENTORY.md`'s row for this page asserts a wider result, that all five unit standards appear in
exactly 15 jurisdictions and 17 records each. **That wider measurement is not reproduced in any
staged extract in `sources/`, and this page does not assert it.** What would close it: re-run the
per-code jurisdiction and record counts against `nodes.jsonl` and paste the output with the
command.

**2. Uniform in one field is not clean.** See the 6,214 records above. A pipeline that validates
on `license` alone passes records whose own attribution text contradicts it.

**3. Pin the version and the fetch date.** Learning Commons' Terms, page stating "Last updated:
July 1, 2026", carry a revocation rider, verbatim: "You acknowledge and agree that a Data Provider
may, at its sole discretion, revoke access to any Content previously made available through the
Services." Revocation is prospective and does not require deletion of adapted content already
created, but a claim about this export with no version and no date is not a claim. See
[[license-withdrawn-grants]].

**4. Learning Commons verifies nothing and says so.** Terms §3.3, verbatim: "In all cases, you
agree to review any applicable license terms associated with Content before accessing or using
it. You are responsible for ensuring compliance with all such terms, conditions, and licenses, if
any." And: "Learning Commons does not independently verify, and disclaims responsibility for, the
accuracy, quality, legality, or appropriateness of Content or Adapted Content." The CC BY 4.0
stamp is a redistributor's assertion, not an adjudication.

**5. The whole chain rests on a document nobody can read.** `LICENSE.md` cites written permission
from 1EdTech. It is a private agreement, not published, and the report records it as unverifiable
from that session. This is the base of the standards layer's title.

**6. Never count components from the tool.** The MCP slices at five with no flag. Any count of a
standard's decomposition comes from the store, not from a tool response.
See [[trap-learning-components-truncated-at-five]] and [[concept-standard-placement-vs-code]].

**7. Absence of a label is not absence of evidence.** The misconception facet being structurally
empty here says nothing about whether misconception research exists for these standards. It does,
it is licence-mixed, and the per-paper record is [[evidence-misconception-research-licensing]].

**8. This is a census of a downloaded copy.** Every count above was measured against a local file
dated 2026-07-22, by the reporting agent, and re-confirmed live on exactly one record. This page's
counts are this project's own measurement, not a figure Learning Commons publishes.

## Related

- [[source-learning-commons-kg]] is the rights verdict on this host: the two-layer MIT plus
  CC BY 4.0 grant, and the reachability record behind the fetches quoted here.
- [[evidence-store-ingest-boundary]] is the other half of this census: which of these labels cross
  into the store the MCP reads, and which of the seven tools are therefore empty by construction.
- [[trap-empty-facet-reads-as-success]] is the failure mode this census exists to make diagnosable.
- [[trap-learning-components-truncated-at-five]] is why a component count never comes from a tool
  response.
- [[concept-attribution-per-record]] is why *the attribution string for this host* is a category
  error, and this export is the corpus that proves it.
- [[source-corestandards-nga-ccsso]] holds the upstream grant that disagrees with the CC BY 4.0
  stamp on the standard statements counted here.
- [[license-cc-by]] is the regime the licence field asserts, and its three mandatory attribution
  components.
- [[license-public-domain-dedication]] is why the CC0 carve-out cannot be shipped as "CC0"
  unqualified.
- [[evidence-misconception-research-licensing]] holds what exists where this export is empty.
- [[concept-standard-placement-vs-code]] is why one code resolves to several nodes, which is what
  makes a per-code count of anything here a question with a method rather than an answer.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] consumes this census as its map of what can and cannot
  be grounded, and is where an empty facet gets recorded as a boundary rather than silently
  absorbed.
- [[practice-assemble-an-attribution-block]] consumes the per-record attribution finding: the
  block is built from the string on the record actually used, never from the host.

## References

Rights-holder and host surfaces, fetched by this project on 2026-08-08:

- `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md`
  HTTP 200, 512 bytes. The whole two-layer grant, including the CC0 carve-out for progressions.
- `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl`
  HTTP 206 on a Range request, public, no auth. The live spot check of one HSG-SRT.C.8 record.
- `https://learningcommons.org/terms-of-use/` HTTP 200, page stating "Last updated: July 1, 2026".
  §3.3 content and compliance, the no-verification disclaimer, the Data Provider revocation rider.
- `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/README.md`
  HTTP 200, 9,848 bytes. The access tiers and the generic 1EdTech attribution example.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-learning-commons-kg.md`, primary. §5 the four attribution strings and the 15
  jurisdictions carrying C.6; §6 the whole-export licence census and the CC0 scan; §7 the
  CC BY-NC-SA rider on 6,214 records; §10 the per-label relevance to the five unit codes and the
  0-byte misconceptions file; §11 what the report could not verify.
- `sources/k12-lesson-toolkit-boundaries.md`, primary. §2.1 the exhaustive misconception check quoted in
  full; §6.1 and §6.2 the per-file licence and attribution measurements on the California-math
  subset; §7 the upstream file table and byte counts.
- `sources/verdict-twelve-host-table.md`, reference. Row 3, this project's own adjudication of the
  host, including the "15 state variants" phrasing this page corrects and the upstream conflict
  with the NGA/CCSSO grant.

This project's own measurement, cited as this project's and not as any outside party's statement:
the label census, the licence census, the CC0 scans, the per-file attribution counts, and the
0-byte and 0-row misconception findings. `INVENTORY.md`'s row for this page additionally asserts a
per-code jurisdiction count that no staged extract carries; gotcha 1 records it as unverified.
