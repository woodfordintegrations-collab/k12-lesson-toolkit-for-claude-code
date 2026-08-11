---
source_url: hs-geometry-similarity-trig/sources/license-lc-kg.md
fetched: 2026-08-08
http_status: n/a (local file; the HTTP status of every upstream probe is preserved inline below)
role: primary
covers: source-learning-commons-kg, source-corestandards-nga-ccsso, concept-attribution-per-record, concept-chain-of-title, concept-standard-placement-vs-code, evidence-kg-coverage-and-gaps, evidence-store-ingest-boundary, trap-down-is-not-one-state, trap-empty-facet-reads-as-success, trap-learning-components-truncated-at-five, practice-assemble-an-attribution-block, k12-density-rules, license-cc-by, license-sharealike, license-noncommercial
---

# Learning Commons Knowledge Graph, the CASE standards export, and thecorestandards.org

## What this extract is

A normalisation of a local in-project verification report. No new fetch was performed at
staging time. Every fetch recorded below was performed by the verifying agent on **2026-08-08
(UTC)**, which the report states applies to all claims unless otherwise noted. The agent's
scope was this host only, and it was read-only on `~/Documents/k12-lesson-toolkit`.

**Read section 5 before writing any attribution line. There is no single attribution string for
this host.** Four distinct strings touch the HSG-SRT unit, and a page that invents a fifth, or
that presents any one of the four as universal, is wrong.

---

## 0. Local repo priors, recorded by the report as hypothesis and not evidence

`NOTICE` and `docs/reference/sourcing-verdict.md`
assert CC BY 4.0 and CC0. The report treats these as prior in-repo claims by an earlier agent,
as hypothesis, and verifies independently.

Internal inconsistency the report flags in that repo, explicitly marking it as outside its own
scope to fix:

- `README.md` line 22: "We do not touch the Learning Commons data."
- `NOTICE` lines 21 to 23: "The data under data/ca-math/ is a filtered derivative of the
  Learning Commons public export"
- `docs/reference/sourcing-verdict.md` lines 24 to 30 explicitly retracts the README claim.

Report's resolution: NOTICE plus sourcing-verdict are current, README is stale, and the shipped
fact is that the data IS the LC export, filtered.

Local data present: `data/raw/nodes.jsonl`, `data/raw/relationships.jsonl`,
`data/ca-math/{standards,components,progressions,misconceptions,hierarchy,crosswalk}.jsonl`.

## 1. Host reachability

| URL | Status | Date |
|---|---|---|
| https://github.com/learning-commons-org/knowledge-graph | HTTP 200 (333,439 bytes) | 2026-08-08 |
| https://raw.githubusercontent.com/.../main/LICENSE.md | HTTP 200 (512 bytes) | 2026-08-08 |
| https://raw.githubusercontent.com/.../main/README.md | HTTP 200 (9,848 bytes) | 2026-08-08 |
| https://api.github.com/repos/learning-commons-org/knowledge-graph | HTTP 200 | 2026-08-08 |

LIVE. No bot block encountered on GitHub or raw.githubusercontent.com.

## 2. Verbatim: LICENSE.md, the whole file, 512 bytes

URL: `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/LICENSE.md`
HTTP 200, fetched 2026-08-08 via curl with a browser UA.

```
Knowledge Graph code is licensed under [MIT](https://opensource.org/license/mit).

Knowledge Graph is provided by Learning Commons under the CC BY 4.0 license ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)). Learning Commons received state standards and written permission under CC BY 4.0 from 1EdTech; learning components under CC BY 4.0 from Achievement Network; and learning progressions under CC0 from Student Achievement Partners ([CC0](https://creativecommons.org/public-domain/cc0/)).
```

Report's reading: a two-layer licence. Code is MIT. Data is CC BY 4.0, with progressions carved
out as CC0.

## 3. Verbatim: README.md, the load-bearing sentences

URL: `https://raw.githubusercontent.com/learning-commons-org/knowledge-graph/main/README.md`
HTTP 200, fetched 2026-08-08.

Access tiers:

> "- **REST API**: Authenticate and make HTTP requests to retrieve academic standards directly. Best for applications that need real-time access. *(Currently available only to private beta users)*
> - **MCP Server**: AI models can reliably work with academic standards, learning components, and learning progressions. ... *(Currently available only to private beta users)*
> - **Local JSONL**: Download local JSONL files and query them directly. Best for offline access, custom processing, or complex queries. *(Publicly available)*"

Per-record licence fields as LC publishes them in their own example response:

> "      "author": "1EdTech",
>       "provider": "Learning Commons",
>       "license": "https://creativecommons.org/licenses/by/4.0/",
>       "attributionStatement": "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Learning Commons received state standards and written permission under CC BY-4.0 from 1EdTech.""

Disclaimer and terms rider:

> "The resources provided in this repository are made available "as-is", without warranties or guarantees of any kind. They may contain inaccuracies, limitations, or other constraints depending on the context of use. Use of these resources is subject to [our Terms of Use](https://learningcommons.org/terms-of-use/)."

> "Please refer to each resource's README, license, and associated docs for any additional limitations, attribution requirements, or guidance specific to that resource."

Public export URLs, no auth stated:

> "curl -L "https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl" -o nodes.jsonl
> curl -L "https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/relationships.jsonl?ref=gh_curl" -o relationships.jsonl"

CCSS Math framework CASE UUID published in the README: `c6496676-d7cb-11e8-824f-0242ac160002`

## 4. CDN export: live, public, no auth

`https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl?ref=gh_curl`

- HTTP 206 on a Range request, `binary/octet-stream`, 2026-08-08
- Full stream succeeded; no credential, no referer check, no bot block.

Live spot-check, streamed from the CDN 2026-08-08, the first HSG-SRT.C.8 record on the wire:

```
statementCode: HSG-SRT.C.8
jurisdiction: New Mexico
author: New Mexico Public Education Department
license: https://creativecommons.org/licenses/by/4.0/
attributionStatement: Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. New Mexico Mathematics standards provided by New Mexico Public Education Department available at http://www.corestandards.org/Math/.
dateModified: 2023-11-19
```

The report's conclusion from that check: the local 2026-07-22 copy has not drifted, with the
same licence value and the same attribution shape.

## 5. THE ATTRIBUTION STRINGS. There is no single one

The report's finding, in its own emphasis: the single "required attribution string" in
k12-lesson-toolkit's NOTICE is **wrong as a universal**. The `attributionStatement` field differs per
record.

The first sentence is constant on all records the agent examined, verbatim:

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license."

Four distinct strings touch the HSG-SRT unit. Reproduce the one that matches the record you
actually used.

### String 1: California standards records (HSG-SRT.B.4, C.6, C.8 in this unit)

Full string, first sentence plus the jurisdiction sentence, as recorded by the report:

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. California Mathematics standards provided by California Department of Education available at https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf."

Jurisdiction: California. Author field: California Department of Education.

### String 2: Multi-State standards records (HSG-SRT.B.5, C.7 in this unit)

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Common Core Mathematics standards provided by Common Good Learning Tools available at https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf."

Jurisdiction: Multi-State. Author field: Common Good Learning Tools.

### String 3: LearningComponent nodes (Achievement Network)

The report records this second sentence for all 66 learning-component nodes it sampled on trig
and similarity language, and gives it as a fragment with a leading ellipsis, so the elision is
the report's:

> "…Learning Commons received learning components under CC BY-4.0 from Achievement Network."

The constant first sentence above precedes it.

### String 4: Lesson, Activity and Assessment nodes (Illustrative Mathematics 360 scope and sequence)

> "Learning Commons received the scope and sequence of the Illustrative Mathematics 360 curriculum under CC BY-4.0 from Illustrative Mathematics."

The report records this as attached to 16,021 records, the largest single attribution block in
the export.

### The per-record table the report built, from five records opened individually

| statementCode | jurisdiction | author | attributionStatement (2nd sentence) |
|---|---|---|---|
| HSG-SRT.B.4 | California | California Department of Education | "California Mathematics standards provided by California Department of Education available at https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf." |
| HSG-SRT.B.5 | Multi-State | Common Good Learning Tools | "Common Core Mathematics standards provided by Common Good Learning Tools available at https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf." |
| HSG-SRT.C.6 | California | California Department of Education | (same as B.4) |
| HSG-SRT.C.7 | Multi-State | Common Good Learning Tools | (same as B.5) |
| HSG-SRT.C.8 | California | California Department of Education | (same as B.4) |

### Two further distinct forms, outside the unit's own path but in the same export

- The New Mexico form, from the live CDN spot-check in section 4:
  "New Mexico Mathematics standards provided by New Mexico Public Education Department
  available at http://www.corestandards.org/Math/."
- The README's generic 1EdTech form, quoted in section 3:
  "Learning Commons received state standards and written permission under CC BY-4.0 from
  1EdTech."

### The count that governs how careful a writer must be

`HSG-SRT.C.6` alone appears **15 times** across jurisdictions in the export (California,
Illinois, Michigan, Vermont, Delaware, Montana, Washington, Nevada, South Dakota, Rhode Island,
Connecticut, New Hampshire, New Mexico, Washington D.C., Multi-State), and the report states
each has a DIFFERENT required attribution sentence.

### The discrepancy with LC's own README

The LC README example response shows `"author": "1EdTech"` for Multi-State math. The actual
v1.11.0 export says `"author": "Common Good Learning Tools"` for Multi-State math, and names
1EdTech only for certain other states and subjects (Mississippi, Nebraska, New Jersey, West
Virginia). The report's conclusion: the k12-lesson-toolkit NOTICE's attribution string, the one
ending "…written permission under CC BY-4.0 from 1EdTech", is the README's generic string, NOT
the string on the records this unit actually uses.

## 6. Per-record licence census across the whole export (247,786 nodes)

Local `data/raw/nodes.jsonl`, 292 MB, the v1.11.0 export, downloaded 2026-07-22; licence fields
re-verified live in section 4.

```
$ grep -o '"license":"[^"]*"' raw/nodes.jsonl | sort | uniq -c
247786 "license":"https://creativecommons.org/licenses/by/4.0/"
$ grep -cv '"license":' raw/nodes.jsonl
0
```

Report's finding, in its own emphasis: **every single node carries exactly one license value,
CC BY 4.0. Zero exceptions, zero nodes missing the field.**

### The CC0 claim is not supported by the data

- `grep -ic 'CC0|publicdomain'` returned 1941, but the report states **every hit is a false
  positive**, a `cc0` substring inside a UUID (`dca94a15-…-cc0ae6b54fe5`). No
  attributionStatement contains "CC0".
- `grep -ic 'Student Achievement Partners'` returned **0**.
- A relationship-type scan found no progression edges. Node labels are:
  `StandardsFrameworkItem` 222,865 · `LearningComponent` 8,686 · `Activity` 8,173 ·
  `Assessment` 4,516 · `Lesson` 2,550 · `LessonGrouping` 764 · `StandardsFramework` 214 ·
  `Course` 18.

Report's conclusion: the k12-lesson-toolkit NOTICE line "Learning progressions: CC0 1.0 (public
domain), via Student Achievement Partners (SAP)" is not reflected anywhere in the v1.11.0
export. The CC0 carve-out exists only in LICENSE.md prose. The operating assumption should be
CC BY 4.0 on everything, because that is what each record declares.

## 7. Rider: a CC BY-NC-SA carve-out inside a nominally CC BY 4.0 export

```
$ grep -o 'asserts a [^"]*license' raw/nodes.jsonl | sort | uniq -c
6214 asserts a CC BY-NC-SA license
```

The report records three variants (Math, ELA, Social Studies) and gives the Math one verbatim:

> "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Georgia Mathematics standards are provided by the Georgia Department of Education, which asserts a CC BY-NC-SA license."  (1,699 records)

The `license` field on those same records still reads `.../licenses/by/4.0/`. So the
machine-readable field and the human-readable attribution contradict each other on 6,214
records, of which Georgia math is 1,699. The report notes this is not in the unit's path, since
the unit is on Multi-State plus California, but that it proves the export is not uniformly clean
and that the `license` field alone is not a sufficient check.

## 8. Verbatim: Learning Commons Terms of Use

URL: `https://learningcommons.org/terms-of-use/`, HTTP 200, fetched 2026-08-08.
The page states: **"Last updated: July 1, 2026"**.

§3.3 Content on Learning Commons' Services:

> "Learning Commons Services facilitates the hosting, processing, and availability of Content provided by Data Providers and the development of Adapted Content by Build Partners. The Content made available through the Services is generally publicly available, such as a public domain work or Content under a Creative Commons Attribution 4.0 International license. However, certain Content may be subject to more restrictive license terms (such as Gated Content). In all cases, you agree to review any applicable license terms associated with Content before accessing or using it. You are responsible for ensuring compliance with all such terms, conditions, and licenses, if any."

> "Learning Commons has no general obligation to monitor, enforce, or ensure compliance with third-party license terms or agreements but may take action where it becomes aware of potential violations."

> "Learning Commons does not independently verify, and disclaims responsibility for, the accuracy, quality, legality, or appropriateness of Content or Adapted Content."

Restrictions:

> "You must not (a) reproduce, rent, sell, modify, translate, decompile, disassemble, or reverse engineer Learning Commons Services; misuse or infringe our or any third party's intellectual property rights or other proprietary personal or legal rights; (b) circumvent or attempt to circumvent or disable any security or technological features or measures that protect Learning Commons or otherwise compromise the security or integrity of the Services, including by introducing malware; (c) attempt to bypass rate limits, quota controls, or usage safeguards for credentials; or (d) access the Services in any way not authorized by these Terms or that violates any applicable law"

Trademark:

> "We reserve all rights, title, and interest in the Services. Using the Services does not give you any right, title, or interest in our Services, other than the right we explicitly grant you herein. The rights in trademarks, service marks, graphics, and logos used for our Services, whether registered or unregistered, are reserved by us or our licensors."

> "Use of our name, logos, or any other brand elements requires prior written permission."

Revocation, which the report flags as mattering for a public repo that pins a copy:

> "You acknowledge and agree that a Data Provider may, at its sole discretion, revoke access to any Content previously made available through the Services." … "Revocation of access applies on a prospective basis. Except as otherwise required by applicable law or expressly set forth in a separate agreement between a Data Provider and a Build Partner, revocation does not automatically require deletion of Adapted Content already created or deployed prior to such revocation."

The `…` between those two quoted passages is the report's own elision marker.

## 9. thecorestandards.org: bot-blocked, not dead, and the text recovered via Wayback

| URL | Method | Status |
|---|---|---|
| https://www.corestandards.org/public-license/ | curl plus browser UA | **HTTP 404** (redirects to corestandards.org/public-license/) |
| https://www.thecorestandards.org/public-license/ | curl plus browser UA | **HTTP 403**, body "Enable JavaScript and cookies to continue" (Cloudflare JS challenge) |
| https://www.thecorestandards.org/ (root) | curl plus browser UA | **HTTP 403** |
| https://www.thecorestandards.org/public-license/ | WebFetch | **HTTP 403 Forbidden** |

Report's classification: a bot block on a live site. The canonical host is now
`thecorestandards.org`; the bare `corestandards.org/public-license/` path 404s.

Wayback CDX confirms continuous 200 snapshots through 2025-12-21. Retrieved verbatim from
`https://web.archive.org/web/20251221152221/https://www.thecorestandards.org/public-license/`,
HTTP 200, fetched 2026-08-08:

> "THE COMMON CORE STATE STANDARDS ARE PROVIDED UNDER THE TERMS OF THIS PUBLIC LICENSE. THE COMMON CORE STATE STANDARDS ARE PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE COMMON CORE STATE STANDARDS OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED."

**The purpose limitation, verbatim. This is the sentence a page must not paraphrase away:**

> "The NGA Center for Best Practices (NGA Center) and the Council of Chief State School Officers (CCSSO) hereby grant a limited, non-exclusive, royalty-free license to copy, publish, distribute, and display the Common Core State Standards for purposes that support the Common Core State Standards Initiative. These uses may involve the Common Core State Standards as a whole or selected excerpts or portions."

> "NGA Center/CCSSO shall be acknowledged as the sole owners and developers of the Common Core State Standards, and no claims to the contrary shall be made."

The mandated notice, verbatim:

> "Any publication or public display shall include the following notice: '© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved.'"

> "States and territories of the United States as well as the District of Columbia that have adopted the Common Core State Standards in whole are exempt from this provision of the License."

> "This License extends to the Common Core State Standards only and not to the examples. A number of the examples are comprised of materials that are not subject to copyright, such as due to being in the public domain, and others required NGA Center and CCSSO to obtain permission for their use from a third party copyright holder."

> "With respect to copyrighted works provided by the Penguin Group (USA) Inc., duplication, distribution, emailing, copying, or printing is allowed only of the work as a whole."

> "This License and the rights granted hereunder will terminate automatically as to a licensee upon any breach by that licensee of the terms of this License."

> "NGA Center and CCSSO reserve the right to release the Common Core State Standards under different license terms or to stop distributing the Common Core State Standards at any time; provided, however that any such election will not serve to withdraw this License with respect to any person utilizing the Common Core State Standards pursuant to this License."

> "This License shall be construed in accordance with the laws of the District of Columbia, without regard to conflicts principles, and as applicable, US federal law. A court of competent jurisdiction in Washington, DC shall be the exclusive forum for the resolution of any disputes regarding this License…"

Page footer: "© 2021 Common Core State Standards Initiative"

### The upstream and downstream mismatch, which the report calls the finding that matters most

The CCSS Public License is **not a Creative Commons licence.** It is a bespoke NGA/CCSSO grant
with two things CC BY 4.0 does not have:

1. **A purpose limitation**, "for purposes that support the Common Core State Standards
   Initiative."
2. **A mandated exact notice**, "© Copyright 2010. National Governors Association Center for
   Best Practices and Council of Chief State School Officers. All rights reserved." The report
   notes: "All rights reserved", inside a page you are republishing.

Learning Commons stamps CCSS-derived standard statements CC BY 4.0. NGA/CCSSO licence the same
text under narrower, different terms. The report is explicit that it cannot resolve which
controls downstream republication of the statement text, calling that a legal question and not
a measurement, and states the honest position: **the two grants do not agree, and the CCSS one
is narrower.** It quotes LC's own Terms pushing that risk downstream: "you agree to review any
applicable license terms associated with Content before accessing or using it. You are
responsible for ensuring compliance."

Safe posture the report recommends for the unit: the NGA/CCSSO notice costs one line. Ship it
alongside the LC attribution rather than relying on LC's CC BY 4.0 stamp to cover the CCSS text.

## 10. Relevance to HSG-SRT.B.4, B.5, C.6, C.7, C.8

The report's framing: this host is the strongest of the sourced hosts for standards grounding,
and it is not a lesson-content source in any usable-prose sense.

- **Standard statements.** All five codes present, with full statement text plus a `notes` field
  carrying the theorem list. For example HSG-SRT.B.4 has description "Prove theorems about
  triangles." plus notes "Theorems include: a line parallel to one side of a triangle divides
  the other two proportionally, and conversely; the Pythagorean Theorem proved using triangle
  similarity." Both California and Multi-State variants are available.
- **68 HSG-SRT records** in the CA-math slice, covering the full cluster A.1 to D.11.
- **LearningComponent nodes (Achievement Network, CC BY 4.0)**, which the report calls the
  genuinely useful layer: standards decomposed into teachable sub-skills. 66 were sampled on
  trig and similarity language, for example "Use the Pythagorean Theorem and its converse to
  show whether a triangle is a right triangle or not", "Apply relationships in special right
  triangles to solve real-world problems", "Use congruence and similarity criteria for triangles
  to solve problems geometrically". All 66 carry attribution String 3 above.
- **Lesson, Activity and Assessment nodes.** 62 Lesson nodes match trig and similarity
  ("Revisiting Right Triangles", "Connecting Similarity and Transformations", "More Applications
  of the Pythagorean Theorem"). The report states these are titles and scope-and-sequence
  metadata only, not lesson content, and that they carry attribution String 4 above, on 16,021
  records. It notes this contradicts `docs/reference/sourcing-verdict.md` lines 51 to 52, which
  claims the curriculum-lessons layer is "NOT in the public LC JSONL"; metadata for it IS in the
  public export.
- **Misconceptions.** `data/ca-math/misconceptions.jsonl` is **0 bytes**. No misconception nodes
  in the export. The report's conclusion: that tool is unbacked.

## 11. What the report could not verify

- **The 1EdTech "written permission"** cited in LC's LICENSE.md is a private agreement between
  LC and 1EdTech. Not published, not verifiable from that session. The report notes the whole
  CC BY 4.0 chain on state standards rests on it.
- **Whether CC BY 4.0 (LC) or the NGA/CCSSO Public License controls** the CCSS statement text
  downstream. Recorded as a legal question, unresolved and outside the agent's competence.
- **Whether NGA/CCSSO's 2010 notice requirement is currently enforced.** The live site is
  403-blocked; the text is a 2025-12-21 Wayback snapshot, which the report records as roughly
  7.5 months stale as of its own fetch date.
- **California Department of Education's own terms** for the CA math standards PDF (cde.ca.gov).
  Out of the agent's assigned scope, not fetched.
- **Illustrative Mathematics' own terms** for IM 360. Out of scope; the CC BY 4.0 claim there is
  LC's assertion, unverified upstream.
- **Achievement Network's own terms.** Same, unverified upstream.
