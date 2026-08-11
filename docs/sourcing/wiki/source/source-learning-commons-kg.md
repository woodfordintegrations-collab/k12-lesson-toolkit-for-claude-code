---
title: "Learning Commons Knowledge Graph (v1.11.0 public export)"
type: source
verdict: quote_and_adapt
fetched: 2026-08-08
sources:
  - https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md
  - https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/README.md
  - https://learningcommons.org/terms-of-use/
  - https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl
  - sources/host-learning-commons-kg.md
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/verdict-twelve-host-table.md
  - sources/cc-by-4-0.md
updated: 2026-08-08
---

# Learning Commons Knowledge Graph (v1.11.0 public export)

## Summary

Learning Commons publishes the standards graph this project grounds on. Two layers, two
instruments: repository code under MIT, graph data under CC BY 4.0. Verdict on the LC layer:
`quote_and_adapt`. The licence field was measured on every record of the v1.11.0 export and it is
uniform, 247,786 nodes carrying CC BY 4.0 with zero exceptions and zero records missing the field.

That measurement is the easy half. Two things sit on top of it and either one alone will get a
build wrong:

1. **There is no single attribution string.** `attributionStatement` is a per-record field that
   varies by jurisdiction and by node type. **Four distinct strings touch this unit**, and the
   report records two further distinct forms in the same export outside the unit's path. A hard
   coded credit line is wrong for most of the material it gets applied to. See
   [[concept-attribution-per-record]].
2. **The CC BY 4.0 stamp is Learning Commons' own, not the upstream owner's.** The Common Core
   statement text inside those records is separately licensed by NGA Center and CCSSO under a
   bespoke grant that is not Creative Commons and is narrower. The verifying report calls the
   mismatch the finding that matters most and states plainly that it cannot say which grant
   controls downstream republication. See [[source-corestandards-nga-ccsso]].

| Layer | Instrument as declared | What it covers |
|---|---|---|
| Repository code | MIT | the code in `github.com/learning-commons-org/knowledge-graph` |
| Graph data, every node | CC BY 4.0 | the export records as LC publishes them |
| State standards inside the data | CC BY 4.0 by LC, via 1EdTech "written permission" | the permission itself is unpublished |
| Learning components | CC BY 4.0 by LC, via Achievement Network | 8,686 `LearningComponent` nodes |
| Learning progressions | CC0 in LICENSE.md prose | see gotcha 4, the measurements do not agree |
| The CCSS statement text itself | NGA/CCSSO public licence | narrower, purpose-limited, notice-mandating |

Two riders that are not licence terms but decide how you use it: LC disclaims all verification and
pushes compliance risk to you in writing, and a Data Provider may revoke access at its sole
discretion. Both make the version pin and the fetch date part of the record.

## When to reach for it

Reach for this host for **standards grounding and objective decomposition**, which is what it is
unambiguously best at. All five HSG-SRT codes in this unit are present with full statement text in
two jurisdictions, California and Multi-State, with CASE identifiers, and with a separate `notes`
field carrying the theorem enumeration that secondary sources drop. `HSG-SRT.C.6` alone appears
**15 times** across jurisdictions in the export, which makes cross-state alignment checkable rather
than assumed. There are **68 HSG-SRT records** in the CA-math slice, covering the full cluster A.1
to D.11.

Reach for it for the Achievement Network learning components, which the report calls the genuinely
useful layer: standards decomposed into teachable sub-skills, **8,686** nodes, CC BY 4.0 clean. 66
were sampled on trigonometry and similarity language.

Do **not** reach for this host for lesson prose. Its `Lesson`, `Activity` and `Assessment` nodes
are titles and scope-and-sequence metadata, not lesson content. The report says so in those terms.
If you want IM's actual prose, go to [[source-im-kendall-hunt]] or [[source-accessim-360]] and take
that host's licence with it, because the metadata's CC BY 4.0 stamp is not a grant over IM's
curriculum text.

Do **not** reach for this host for misconceptions. `misconceptions.jsonl` is **0 bytes**. There are
no misconception nodes in the export, and the MCP tool that queries them is therefore unbacked. An
empty result from it is a boundary of the corpus, not a fact about the standard. See
[[trap-empty-facet-reads-as-success]] and [[evidence-kg-coverage-and-gaps]].

Do not reach for the REST API or the MCP server as an access route. LC's README marks both
*(Currently available only to private beta users)*. The local JSONL export is the publicly
available tier and is the one this project uses.

## What its own page says

Every quotation below was pasted by a verifying agent from live bytes on 2026-08-08 and is staged
verbatim in `sources/host-learning-commons-kg.md`. Nothing rests on a summarizing layer; see
[[trap-summary-layer-is-not-evidence]].

### LICENSE.md, the whole file, 512 bytes

`https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md`, HTTP 200,
fetched 2026-08-08 by curl with a browser user agent. This is the entire file:

> Knowledge Graph code is licensed under [MIT](https://opensource.org/license/mit).
>
> Knowledge Graph is provided by Learning Commons under the CC BY 4.0 license ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)). Learning Commons received state standards and written permission under CC BY 4.0 from 1EdTech; learning components under CC BY 4.0 from Achievement Network; and learning progressions under CC0 from Student Achievement Partners ([CC0](https://creativecommons.org/public-domain/cc0/)).

Two sentences carry the whole grant. Note that three separate upstream chains are named in one
sentence and each one is asserted by LC rather than evidenced by LC.

### README.md, the sentences that bind

`https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/README.md`, HTTP 200,
fetched 2026-08-08. LC's own example of what a record's rights fields look like:

> "author": "1EdTech",
>       "provider": "Learning Commons",
>       "license": "https://creativecommons.org/licenses/by/4.0/",
>       "attributionStatement": "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Learning Commons received state standards and written permission under CC BY-4.0 from 1EdTech."

The disclaimer, verbatim:

> The resources provided in this repository are made available "as-is", without warranties or guarantees of any kind. They may contain inaccuracies, limitations, or other constraints depending on the context of use. Use of these resources is subject to [our Terms of Use](https://learningcommons.org/terms-of-use/).

And the sentence that tells you the repository licence is not the last word:

> Please refer to each resource's README, license, and associated docs for any additional limitations, attribution requirements, or guidance specific to that resource.

### The Terms of Use, which is where the risk allocation lives

`https://learningcommons.org/terms-of-use/`, HTTP 200, fetched 2026-08-08. The page states
**"Last updated: July 1, 2026"**. Section 3.3, verbatim:

> Learning Commons Services facilitates the hosting, processing, and availability of Content provided by Data Providers and the development of Adapted Content by Build Partners. The Content made available through the Services is generally publicly available, such as a public domain work or Content under a Creative Commons Attribution 4.0 International license. However, certain Content may be subject to more restrictive license terms (such as Gated Content). In all cases, you agree to review any applicable license terms associated with Content before accessing or using it. You are responsible for ensuring compliance with all such terms, conditions, and licenses, if any.

The two disclaimer sentences beside it, verbatim:

> Learning Commons has no general obligation to monitor, enforce, or ensure compliance with third-party license terms or agreements but may take action where it becomes aware of potential violations.

> Learning Commons does not independently verify, and disclaims responsibility for, the accuracy, quality, legality, or appropriateness of Content or Adapted Content.

The revocation clause, which is why the version pin matters. The ellipsis between the two passages
is the verifying report's own elision marker:

> You acknowledge and agree that a Data Provider may, at its sole discretion, revoke access to any Content previously made available through the Services. … Revocation of access applies on a prospective basis. Except as otherwise required by applicable law or expressly set forth in a separate agreement between a Data Provider and a Build Partner, revocation does not automatically require deletion of Adapted Content already created or deployed prior to such revocation.

Trademark, verbatim:

> Use of our name, logos, or any other brand elements requires prior written permission.

### The per-record licence census

Local `data/raw/nodes.jsonl`, the v1.11.0 export downloaded 2026-07-22, 292 MB. The commands and
their output, as the report records them:

```
$ grep -o '"license":"[^"]*"' raw/nodes.jsonl | sort | uniq -c
247786 "license":"https://creativecommons.org/licenses/by/4.0/"
$ grep -cv '"license":' raw/nodes.jsonl
0
```

Node labels and their counts, from the same census: `StandardsFrameworkItem` 222,865 ·
`LearningComponent` 8,686 · `Activity` 8,173 · `Assessment` 4,516 · `Lesson` 2,550 ·
`LessonGrouping` 764 · `StandardsFramework` 214 · `Course` 18.

A live spot-check was streamed from the CDN on 2026-08-08 against the first `HSG-SRT.C.8` record on
the wire, to test whether the local 2026-07-22 copy had drifted. It had not: same licence value,
same attribution shape. The CDN export returned HTTP 206 on a Range request with no credential, no
referer check and no bot block.

## What you may do with it

| Operation | Permitted on the LC layer | Condition |
|---|---|---|
| Cite: name it, link it, state which standard a node holds, describe it in your own words | yes | none, and no licence is needed to do this |
| Quote: reproduce a record's exact text in quotation marks | yes | the record's own attribution string, plus the CCSS notice where the text is CCSS |
| Paraphrase and republish: rewrite the material and ship it | yes on the LC layer, no copyleft | same two notices, plus the changes-made indication |

CC BY 4.0's own deed carries `for any purpose, even commercially` on both freedoms and its "Under
the following terms" list has exactly two items, Attribution and No additional restrictions. See
[[license-cc-by]].

The table above is about the **LC layer**. It is not a verdict on the CCSS statement text sitting
inside those records, which has its own upstream owner and its own narrower grant. Both notices
ship. See the next subsection and [[source-corestandards-nga-ccsso]].

### Selecting the attribution string, which is the actual work

The first sentence is constant on every record the report examined, verbatim:

> Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.

What follows it is not constant. Read the record's `jurisdiction` and its node label, then use the
matching block. These are the four that touch this unit.

**Block 1, California standards records.** In this unit: HSG-SRT.B.4, C.6, C.8. Author field reads
California Department of Education.

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
California Mathematics standards provided by California Department of Education available at
https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf.
```

**Block 2, Multi-State standards records.** In this unit: HSG-SRT.B.5, C.7. Author field reads
Common Good Learning Tools.

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
Common Core Mathematics standards provided by Common Good Learning Tools available at
https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf.
```

**Block 3, LearningComponent nodes.** All 66 components sampled on this unit's language carry it.

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
Learning Commons received learning components under CC BY-4.0 from Achievement Network.
```

**Block 4, Lesson, Activity and Assessment nodes**, the IM 360 scope and sequence. The report
records this attached to 16,021 records, the largest single attribution block in the export.

```
Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
Learning Commons received the scope and sequence of the Illustrative Mathematics 360
curriculum under CC BY-4.0 from Illustrative Mathematics.
```

Two further distinct forms exist in the same export, outside this unit's path. The New Mexico form,
recorded from the live CDN spot-check: "New Mexico Mathematics standards provided by New Mexico
Public Education Department available at http://www.corestandards.org/Math/." And the README's
generic 1EdTech form quoted above, which the report is explicit is the README's string and **not**
the string on the records this unit uses.

### The second notice, which is not optional and is not LC's

Whenever a Common Core statement is reproduced, the NGA/CCSSO public licence mandates its own
notice verbatim. Ship it alongside the LC string. It costs one line and it closes the only gap
between the two grants that a build can close without counsel:

```
Common Core State Standards
© Copyright 2010. National Governors Association Center for Best Practices and
Council of Chief State School Officers. All rights reserved.
http://www.corestandards.org/
```

The assembly step for both is [[practice-assemble-an-attribution-block]]. The single place in a
finished package where the standard is quoted verbatim, and therefore the single place both notices
attach, is fixed by [[k12-density-rules]].

### What the grant does not reach

- **The Learning Commons name, logos and brand elements**, reserved by the Terms and requiring
  prior written permission. Citing Learning Commons by name is ordinary nominative use and is
  unaffected. See [[concept-third-party-carve-out]].
- **Gated Content.** LC's own §3.3 flags that certain Content may carry more restrictive terms. The
  public JSONL export is the tier this project uses and the tier the census covers.
- **The upstream chains LC asserts.** The 1EdTech written permission is a private agreement, not
  published and not verifiable from that session, and the whole CC BY 4.0 chain on state standards
  rests on it. Achievement Network's own terms and Illustrative Mathematics' own terms for IM 360
  are likewise unverified upstream. See [[concept-chain-of-title]].
- **The CCSS statement text as against its owner.** See gotcha 3.

## Gotchas & constraints

**1. A single hard-coded attribution string is wrong, and this project shipped one.** The
k12-lesson-toolkit repository's `NOTICE` hard-codes one string under the heading "Attribution statement
(as published in the data)". A second agent parsed the store's whole CA-math subset,
`standards.jsonl` 2303 records, `progressions.jsonl` 1041, `components.jsonl` 6056 and
`crosswalk.jsonl` 591, and found that the hard-coded string, the 1EdTech form, appears on **none**
of them. Five distinct strings cover that subset, one of which is the bare first sentence alone on
all 591 crosswalk records. The lesson generalises: the field is per-record, and the count that
governs how careful you have to be is that `HSG-SRT.C.6` alone carries a different required
sentence in each of 15 jurisdictions.

**2. The licence field alone is not a sufficient check, and 6,214 records prove it.** Measured:

```
$ grep -o 'asserts a [^"]*license' raw/nodes.jsonl | sort | uniq -c
6214 asserts a CC BY-NC-SA license
```

The report gives the mathematics variant verbatim, attached to 1,699 records:

> Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Georgia Mathematics standards are provided by the Georgia Department of Education, which asserts a CC BY-NC-SA license.

The `license` field on those same records still reads CC BY 4.0. The machine-readable field and the
human-readable attribution contradict each other on 6,214 records. None is on this unit's path,
which is Multi-State plus California, so this is not a live hazard for HSG-SRT. It is proof that
reading the `license` field and stopping is not a verification. Read the attribution sentence too.
A NonCommercial term arriving through a ShareAlike assertion is exactly the contamination path
[[trap-sharealike-contaminates-by-paraphrase]] and [[license-sharealike]] describe.

**3. LC's stamp does not bind the upstream owner, and the two grants do not agree.** LC stamps
CC BY 4.0 on CCSS statement text. NGA Center and CCSSO licence the same text under a bespoke,
non-Creative-Commons grant with a purpose limitation CC BY 4.0 does not have, a mandated verbatim
"All rights reserved" notice, auto-termination on breach, and a Washington DC forum. The report
states in its own words that the two grants do not agree and that the CCSS one is narrower, and
records which of the two controls downstream republication as a legal question it cannot answer.
Collapsing the two into "the standards are CC BY 4.0" is the error the report calls the finding
that matters most. The mitigation does not require the answer: ship both notices.

**4. The CC0-for-progressions claim has two measurements that look contradictory, and this page
does not resolve them.** Both are staged in this wiki:

- The whole-export census over `nodes.jsonl` found `grep -ic 'Student Achievement Partners'`
  returned **0**, found every `cc0` substring hit to be a false positive inside a UUID, and found
  no progression edges in a relationship-type scan. Its conclusion was that the CC0 carve-out
  exists only in LICENSE.md prose.
- A second agent parsing the store's CA-math subset found the CC0 sentence present on **all 1,041**
  progression records, verbatim: "Knowledge Graph is provided by Learning Commons under the
  CC BY-4.0 license. Learning Commons received learning progressions under CC0 from Student
  Achievement Partners." The `license` field on those same 1,041 records reads CC BY 4.0.

The conflict is sharper than a file-boundary explanation covers, and this page does not paper over
it. The obvious reconciliation would be that the two agents read different files, since the census
ran over `nodes.jsonl` while `progressions.jsonl` holds 757 `buildsTowards` and 284 `relatesTo`
**edges** drawn from `relationships.jsonl`. But the census report also states that its
relationship-type scan found no progression edges, which is the same corpus the store filtered
1,041 of them out of. Both agents are recorded as parsing v1.11.0. Neither the second agent nor
this page reconciled it; the second agent's own note says the row is another agent's and the
full-export census was outside its scope.

What closes it: a census of `relationships.jsonl` by edge type against the same export, which
nobody in this project has run. Until then, treat the operating grant as CC BY 4.0 on everything,
because that is what every record's `license` field declares in both measurements, and do not rely
on a public-domain dedication whose scope nobody has measured end to end. See
[[license-public-domain-dedication]].

**5. LC's README disagrees with LC's own export.** The README example shows `"author": "1EdTech"`
for Multi-State mathematics. The v1.11.0 export says `"author": "Common Good Learning Tools"` for
Multi-State mathematics, and names 1EdTech only for certain other states and subjects, the report
listing Mississippi, Nebraska, New Jersey and West Virginia. Take the field off the record you
actually used, never off the documentation.

**6. Pin the version and the fetch date, because access is revocable and the Terms are dated.** A
Data Provider may revoke access at its sole discretion, prospectively, and the Terms themselves are
headed "Last updated: July 1, 2026", five weeks before this fetch. This project's record is
v1.11.0, downloaded 2026-07-22, licence fields re-confirmed live on the wire 2026-08-08. A
repository that pins a copy without pinning what it pinned cannot show what it was granted at the
time. Two grants elsewhere in this corpus were withdrawn inside six months; re-pull this host's
licence surface before publication. See [[license-withdrawn-grants]] and
[[trap-license-withdrawn-after-citation]].

**7. The misconception layer is empty, and the tooling reports empty as success.**
`misconceptions.jsonl` is 0 bytes, so `find_misconceptions_for_standard` returns an empty payload
with a success status for every code you give it. Nothing in the response says the backing file has
no data. See [[trap-empty-facet-reads-as-success]].

**8. The component layer is truncated at the tool boundary, not at the data boundary.** The export
holds 8,686 `LearningComponent` nodes, but the MCP tool that reads them slices its result and does
not say it truncated. A count of a standard's components must come from the store, never from the
tool response. See [[trap-learning-components-truncated-at-five]] and
[[evidence-store-ingest-boundary]].

**9. MIT covers the code and nothing this project does turns on it.** The two-layer split is real
and worth stating once so nobody applies MIT's terms to the data or CC BY's to the code. No
operation in this build consumes the repository's code.

**10. Node counts and standard placement are not the same question.** One standard code resolves to
several per-jurisdiction placement nodes carrying different facets on different siblings. The
`HSG-SRT.C.6` figure of 15 jurisdictions is that phenomenon, not a data error. Grounding collapses
them with the store's own richest-representative selection; see
[[concept-standard-placement-vs-code]] and [[practice-resolve-a-standard-code]].

## Related

- [[source-corestandards-nga-ccsso]] is the upstream owner of the CCSS statement text that this
  host stamps CC BY 4.0. Gotcha 3 is the whole reason that page exists separately from this one.
- [[concept-attribution-per-record]] is the general form of gotcha 1, and
  [[concept-chain-of-title]] is why LC's three asserted upstream chains, none of them published,
  limit this verdict rather than footnote it.
- [[license-cc-by]] holds the plain-attribution regime this host grants under and the three
  components a CC BY credit must carry.
- [[license-sharealike]] and [[trap-sharealike-contaminates-by-paraphrase]] are what the 6,214
  Georgia-style records in gotcha 2 would drag in if any of them entered a file.
- [[license-public-domain-dedication]] is where the unresolved CC0 question in gotcha 4 belongs,
  and [[license-withdrawn-grants]] carries the revocation record that dates this verdict.
- [[evidence-kg-coverage-and-gaps]] is the measured census of this export, label by label, and
  [[evidence-store-ingest-boundary]] is which of these node types cross into the k12-lesson-toolkit store.
- [[trap-empty-facet-reads-as-success]] and [[trap-learning-components-truncated-at-five]] are the
  two ways this host's tooling returns a confident wrong answer.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above is a pasted byte.
- [[source-im-kendall-hunt]] and [[source-accessim-360]] hold IM's actual curriculum prose, whose
  licence is IM's and not this host's, despite IM 360 metadata living in this export.

## Composes with

- [[practice-resolve-a-standard-code]] is the procedure that turns a code into a grounded node
  here, including the search cap that makes a wrong-grade-band hit count as a miss.
- [[practice-ground-a-lesson-end-to-end]] consumes this host through the mandated call sequence and
  freezes the payload with provenance, which is what makes the per-record attribution string
  recoverable later.
- [[practice-assemble-an-attribution-block]] consumes Blocks 1 to 4 above plus the NGA/CCSSO notice
  into the shipped LICENSE and attribution file.
- [[k12-density-rules]] fixes the single place in a package where the standard is quoted verbatim,
  which is the single place both notices attach.

## References

Rights-holder pages, fetched by this project on 2026-08-08:

- `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md`
  HTTP 200, 512 bytes. The whole two-layer grant, reproduced entire above.
- `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/README.md`
  HTTP 200, 9,848 bytes. Access tiers, the per-record rights fields, the as-is disclaimer.
- `https://learningcommons.org/terms-of-use/` HTTP 200. "Last updated: July 1, 2026"; §3.3 content
  and compliance, the verification disclaimer, the revocation clause, the trademark reservation.
- `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl`
  HTTP 206 on a Range request, no auth. The live spot-check that dated the local copy.
- `https://github.com/learning-commons-org/knowledge-graph` HTTP 200 and
  `https://api.github.com/repos/learning-commons-org/knowledge-graph` HTTP 200. Reachability only.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-learning-commons-kg.md`, primary. The reachability table, LICENSE.md and README
  verbatim, the Terms sections, §5 the four attribution strings and the 15-jurisdiction count, §6
  the whole-export census, §7 the 6,214 CC BY-NC-SA records, §9 thecorestandards.org, §10 relevance
  to the five codes, §11 what the report could not verify.
- `sources/k12-lesson-toolkit-boundaries.md`, reference. §6.1 and §6.2 the per-file licence and
  attribution measurements over the CA-math subset, §6.3 the progressions rider, §6.4 the
  repository `NOTICE` verbatim.
- `sources/verdict-twelve-host-table.md`, reference. Row 3 and its riders, §3 correction 10, §4.1
  the dual-notice attribution block, §6 the unresolved question of which grant controls.
- `sources/cc-by-4-0.md`, primary. The CC BY 4.0 deed and legal code staged verbatim.

This project's own working files, cited as this project's measurement and not as any outside
party's statement:

- `Projects/HS Geometry/sources/license-lc-kg.md`, the underlying verification report.
- `NOTICE`, the in-repository prior that gotcha 1
  corrects, and `docs/reference/sourcing-verdict.md` beside it.

Not verified by anyone in this project, and named here so the gap is visible: the 1EdTech written
permission, the California Department of Education's own terms for the CA standards PDF,
Achievement Network's own terms, Illustrative Mathematics' own terms for IM 360, and any
whole-export census of `relationships.jsonl`.
