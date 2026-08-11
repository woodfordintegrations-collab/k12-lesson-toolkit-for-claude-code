---
title: Attribution is a per-record artifact, not a per-host one
type: concept
sources:
  - sources/host-learning-commons-kg.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/host-im-kendall-hunt.md
  - sources/host-engageny-nysed.md
  - sources/cc-by-4-0.md
  - sources/verdict-twelve-host-table.md
  - https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md
  - https://creativecommons.org/licenses/by/4.0/
updated: 2026-08-08
---

# Attribution is a per-record artifact, not a per-host one

## Summary

The required credit line is a property of the individual record you used. It is not a property of
the host you fetched it from. A build that stores one attribution string per host is wrong for most
of the material that string gets applied to, and it is wrong silently, because a plausible credit
line renders exactly like a correct one.

This is not a quirk of one data provider. It falls out of the licence text. CC BY 4.0's attribution
duty is written as a duty to **retain what the licensor supplied with that material**, Section
3(a)(1), verbatim:

> If You Share the Licensed Material (including in modified form), You must:
>
> retain the following if it is supplied by the Licensor with the Licensed Material:

Every item in the list that follows is conditioned on `if it is supplied by the Licensor`. What was
supplied is a fact about the record, so the duty is a fact about the record.

Four selectors decide which string applies, and this corpus contains an instance of each:

| Selector | Host where it is live | What changes |
|---|---|---|
| Jurisdiction | Learning Commons Knowledge Graph | The upstream standards body and its document URL |
| Node type | Learning Commons Knowledge Graph | The upstream provider (1EdTech, Achievement Network, Illustrative Mathematics) |
| Grade band | `im.kendallhunt.com` | The base copyright holder, IM or Open Up Resources |
| Per document | EngageNY and NYSED | A mandated format with the document name interpolated |

The worked failure this project actually produced is recorded below: a repository shipped a single
hard-coded attribution string that appears on **none** of the records it cites.

## When to reach for it

Reach for it before writing any `ATTRIBUTION` file, `NOTICE` file or credits block, and before
adding an attribution field to a schema. The schema decision is the expensive one: a store that has
nowhere to put a per-record string has already made the error, and no amount of care downstream
recovers it. Reach for it also when a standard code is cited in more than one jurisdiction, when a
package cites a prerequisite from a lower grade band, and when material from one host arrives
through more than one node type.

Do **not** reach for it to learn what a particular host's grant permits. That is
[[concept-cite-quote-adapt]] read against that host's own `source` page. This page assumes the grant
is settled and asks only what the credit line must say.

## How it works

### The string travels with the record, because the duty does

Under CC BY 4.0 the attribution obligation is to retain the creator identification, copyright
notice, licence notice, disclaimer notice and link to the material **as supplied with that
material**. Two records from the same export, under the same licence, from the same provider, can
therefore carry different obligations, because different things were supplied with them. The deed
compresses all of this into two words, `appropriate credit`, which is why reading the deed alone
leads a builder to expect one string per source.

The satisfaction rule that follows inside Section 3(a) is generous about form and says nothing about
uniformity, verbatim:

> You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium,
> means, and context in which You Share the Licensed Material. For example, it may be reasonable to
> satisfy the conditions by providing a URI or hyperlink to a resource that includes the required
> information.

So the shape of the credits block is yours to choose. Which strings go in it is not.

### Where the selector lives on each host

**Jurisdiction and node type, Learning Commons.** Every record in the v1.11.0 export carries an
`attributionStatement` field. Its first sentence is constant across every record the verifying agent
examined, verbatim:

> Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.

Its second sentence is not. Four distinct forms touch the HSG-SRT unit, and they are reproduced in
full under "In practice" below.

**Grade band, `im.kendallhunt.com`.** One licence, CC BY 4.0, across the whole curriculum host. Two
footers, because the base copyright holder differs by band. The high school footer credits
Illustrative Mathematics 2019; the grades 6 to 8 footer credits Open Up Resources 2017-2019 for the
base curriculum and Illustrative Mathematics 2019 for the adaptations. Crediting only IM on a `/MS/`
page is an incorrect attribution.

**Per document, EngageNY.** The archived Terms of Use mandate a format rather than a string,
verbatim:

> From EngageNY.org of the New York State Education Department. [Name of article/document.]
> Internet. Available from [specific webpage on EngageNY.org]; accessed [date, month, year].

The bracketed slots are the record. A build that fills them once and reuses the result has produced
a false citation for every other document.

### Where the selector does not exist, and what that means

Three hosts in this corpus publish **no** canonical attribution string at all:
`tasks.illustrativemathematics.org`, `map.mathshell.org` and `mathmistakes.org`. On those, the
credit line is constructed by this project from the footer and the artifact, and that construction
is this project's own work, not the host's instruction. Say so wherever such a string is shipped.
Absence of a published string is not permission to invent a uniform one.

## In practice

### The four Learning Commons strings that touch this unit

Reproduce the one attached to the record actually used. Each is byte-exact as staged, and the
constant first sentence precedes each of them.

California standards records:

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. California
Mathematics standards provided by California Department of Education available at
https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf.
```

Multi-State standards records:

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Common Core
Mathematics standards provided by Common Good Learning Tools available at
https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf.
```

Learning-component records, staged with the report's own leading elision:

```
…Learning Commons received learning components under CC BY-4.0 from Achievement Network.
```

Lesson, Activity and Assessment records:

```
Learning Commons received the scope and sequence of the Illustrative Mathematics 360
curriculum under CC BY-4.0 from Illustrative Mathematics.
```

### The split runs through the middle of one five-standard unit

Five records were opened individually by the verifying agent and their jurisdictions recorded:

| statementCode | jurisdiction | author | Which string |
|---|---|---|---|
| HSG-SRT.B.4 | California | California Department of Education | California |
| HSG-SRT.B.5 | Multi-State | Common Good Learning Tools | Multi-State |
| HSG-SRT.C.6 | California | California Department of Education | California |
| HSG-SRT.C.7 | Multi-State | Common Good Learning Tools | Multi-State |
| HSG-SRT.C.8 | California | California Department of Education | California |

Two different credit lines are required inside a single unit of five consecutive standards. There is
no host-level string that is correct for all five. Widen the frame and it gets worse: `HSG-SRT.C.6`
alone appears **15 times** across jurisdictions in the export, and the verifying agent records that
each has a different required attribution sentence.

### The failure, as it actually happened

`NOTICE` hard-codes one string under the heading
"Attribution statement (as published in the data)", the generic 1EdTech form from Learning Commons'
own README. A second agent parsed the shipped CA-math subset record by record and recorded the
result: five distinct `attributionStatement` values cover the whole subset, and the hard-coded
1EdTech form **appears on none of the records parsed**. The parse covered `standards.jsonl` at 2303
records, `progressions.jsonl` at 1041, `components.jsonl` at 6056 and `crosswalk.jsonl` at 591, and
every record fell into one of the five measured strings.

Two contributing causes, both worth naming because both recur:

- **The provider's own documentation was not the provider's own data.** Learning Commons' README
  example response shows `"author": "1EdTech"` for Multi-State math. The v1.11.0 export says
  `"author": "Common Good Learning Tools"` for Multi-State math. The repository took its string from
  the documentation.
- **The schema had nowhere to put the alternative.** Measured on `data/k12-lesson-toolkit.db`, no table
  carries `attributionStatement` at all, and of the four tables only `standards` carries a
  `source_license` column. The per-record attribution does not survive ingest into the artifact the
  MCP actually reads. See [[evidence-store-ingest-boundary]].

## Gotchas & constraints

**1. The store cannot answer this question, so do not ask it there.** The per-record
`attributionStatement` is present in `data/ca-math/*.jsonl` and absent from `data/k12-lesson-toolkit.db`.
Any credit line assembled from the store alone is assembled from a field that was dropped. Read the
JSONL or the export.

**2. A repository's own NOTICE is a claim, not evidence.** The one examined here asserts a single
required string and asserts a CC0 layer. Both are in-repo claims by an earlier agent. Treat a NOTICE
the way you would treat any secondary source: verify against the records, then correct the file if
it is yours to correct.

**3. The licence field and the attribution text can disagree, on the same record.** Measured on the
full export, 6,214 records assert a CC BY-NC-SA licence in their attribution prose while the
`license` field on those same records still reads CC BY 4.0, of which 1,699 are Georgia mathematics.
Separately, all 1,041 progression records in the CA-math subset carry `license` CC BY 4.0 while
their `attributionStatement` says Learning Commons received them under CC0. Neither disagreement is
resolved by this wiki. Both mean the `license` field alone is not a sufficient check.

**4. Do not carry a string across hosts that share a brand.** The four Learning Commons strings
above include one naming Illustrative Mathematics as the upstream for scope-and-sequence metadata.
That is not the same obligation as the footer on `im.kendallhunt.com`, and neither is the same as
the footer on `tasks.illustrativemathematics.org`. Resolve the host, then the record.

**5. The number of strings is not fixed and is not a design constant.** Four forms touch this unit;
five cover the CA-math subset; the verifying agent recorded two further distinct forms in the same
export outside the unit's own path, including a New Mexico form confirmed live on the wire. Build
for a lookup, not for an enumeration.

**6. Standards text needs a second notice that has nothing to do with the record.** Where a CCSS
statement is reproduced, the NGA and CCSSO public licence mandates its own notice verbatim, and that
obligation runs alongside the Learning Commons string rather than being satisfied by it. See
[[source-corestandards-nga-ccsso]].

## Related

- [[license-cc-by]] holds the attribution regime this page's rule falls out of, including the
  three components the grant names and the difference between the 3.0 and 4.0 duties.
- [[source-learning-commons-kg]] is the host where jurisdiction and node type select the string,
  [[source-im-kendall-hunt]] the host where the grade band does, and [[source-engageny-nysed]] the
  host that mandates a per-document format rather than a string.
- [[concept-chain-of-title]] is the neighbouring question of whether the party named in the string
  is the party that actually holds the rights.
- [[concept-standard-placement-vs-code]] is why one standard code reaches several records in the
  first place, and therefore why one code can require more than one credit line.
- [[evidence-store-ingest-boundary]] measures which fields survive ingest into the local store.
- [[source-corestandards-nga-ccsso]] holds the second, non-Creative-Commons notice that standards
  text carries.

## Composes with

- [[practice-assemble-an-attribution-block]] is the procedure that consumes this rule, selecting
  one string per cited record rather than one per host.
- [[practice-ground-a-lesson-end-to-end]] is where the record identity is established, and it is
  the only point at which the correct string is still knowable cheaply.
- [[k12-density-rules]] fixes the single place in a package where a standard is quoted verbatim,
  which is the point at which that record's own credit line has to be attached.

## References

Primary evidence, fetched by this project on 2026-08-08 unless stated:
`https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md` HTTP 200,
512 bytes, the two-layer grant and the three upstream provenance clauses;
`https://creativecommons.org/licenses/by/4.0/` HTTP 200, 32178 bytes, and its legal code HTTP 200,
48970 bytes, for Section 3(a)(1) and its `if it is supplied by the Licensor` condition;
`https://im.kendallhunt.com/MS/teachers/3/2/1/preparation.html` HTTP 200, fetched 2026-08-07, for
the grades 6 to 8 footer crediting Open Up Resources 2017-2019.

Staged extracts in this wiki, all primary, staged 2026-08-08.
`sources/host-learning-commons-kg.md`: section 5, the four attribution strings and the five-record
jurisdiction table, the 15-jurisdiction count for HSG-SRT.C.6 and the README-versus-export author
discrepancy; section 7, the 6,214 CC BY-NC-SA assertions.
`sources/k12-lesson-toolkit-boundaries.md`: section 6.2, the five byte-exact strings with their record
counts; section 6.4, the NOTICE reproduced in full and the measurement that its hard-coded string
appears on none of the parsed records; section 1.1, the store schema measurement.
`sources/host-im-kendall-hunt.md`: sections 3 and 4, the two band footers verbatim.
`sources/host-engageny-nysed.md`: section 3b, the mandated attribution format.
`sources/cc-by-4-0.md`: the deed and legal code staged verbatim.

This project's own adjudication, cited as this project's measurement and not as any outside party's
statement: `sources/verdict-twelve-host-table.md`, reference, sections 4.1 through 4.10, the
paste-ready attribution blocks, including its statement that there is no single string and its
instruction to use the one attached to the record actually cited.
