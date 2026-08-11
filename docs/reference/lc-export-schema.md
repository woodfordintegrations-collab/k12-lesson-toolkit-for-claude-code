# Learning Commons Knowledge Graph — Public Export Schema (v1.11.0)

A ground-truth study of the **public, no-auth Learning Commons Knowledge Graph export**,
produced by reading every record of the two export files end to end. This documents the
node & relationship schema, the California-mathematics coverage, the (non-)existence of
misconception data, and the field mapping into Overeducated's target model.

Every count and field name below was measured directly from the downloaded files, not
inferred.

---

## 1. Source, provenance, license

| File | URL | Size | Records |
|---|---|---|---|
| `nodes.jsonl` | `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl` | 292,652,341 B (~279 MiB) | 247,786 nodes |
| `relationships.jsonl` | `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/relationships.jsonl` | 520,406,049 B (~496 MiB) | 456,620 relationships |

Downloaded to `data/raw/` (gitignored). Both are newline-delimited JSON; every line parses.
License on every record: **CC BY 4.0** (`https://creativecommons.org/licenses/by/4.0/`).
The learning-progression edges (`buildsTowards`, `relatesTo`) are additionally sourced from
Student Achievement Partners under **CC0**. `provider` on all standards nodes = `Learning Commons`.
Each record carries a per-source `attributionStatement`.

---

## 2. Node schema

Top-level keys on every node: **`type`, `identifier`, `labels`, `properties`**.
`type` == `"node"` for all 247,786. `labels` is always a **single-element** array (one label
per node). `identifier` is the graph's own node id (see §2.2).

### 2.1 Distinct label sets and counts

| `labels` | Count | Role |
|---|---|---|
| `StandardsFrameworkItem` | 222,865 | A single standard / cluster / domain statement (Class A corpus) |
| `LearningComponent` | 8,686 | A deconstructed sub-skill that supports a standard (Class B) |
| `Activity` | 8,173 | Illustrative Mathematics curriculum activity (Class C) |
| `Assessment` | 4,516 | IM assessment (Class C) |
| `Lesson` | 2,550 | IM lesson (Class C) |
| `LessonGrouping` | 764 | IM unit / section (Class C) |
| `StandardsFramework` | 214 | A framework header (one per jurisdiction×subject), parent of its items |
| `Course` | 18 | IM course (Class C) |

### 2.2 Identifier scheme (prefix)

- **`StandardsFrameworkItem`, `LearningComponent`, `StandardsFramework`** and most content
  nodes use a **bare deterministic UUIDv5** as `identifier`, e.g.
  `f3d53bd1-ba39-5f22-9281-e0efb05e9862` (no prefix; 231,765 nodes).
- **Illustrative Mathematics content** (`Activity`/`Assessment`/`Lesson`/etc.) is
  provider-prefixed **`im:`**, e.g. `im:b8982b98-1078-527f-b7c7-fc974eaabf81` (16,021 nodes).
- **Relationships reference `node.identifier`** in their `source_identifier` /
  `target_identifier` (verified: relationship endpoints resolve against `node.identifier`,
  NOT against `caseIdentifierUUID`).
- Note there are **two UUIDs per standard**: `identifier` (the graph node id, the join spine)
  and `properties.caseIdentifierUUID` (the external IMS/CASE id). **They never coincide**
  (0 / 222,865 equal). `properties.identifier` duplicates the top-level `identifier`.

### 2.3 `StandardsFrameworkItem` property dictionary

All 222,865 items carry these keys (frequency in parentheses where < total):

| Property | Holds | Notes |
|---|---|---|
| `statementCode` (160,536) | **The standard CODE** e.g. `6.RP.A.2`, `HSA-CED.A`, `3.G.3` | Absent on ~28% (unlabeled sub-parts) |
| `alternateStatementCode` (20,033) | Secondary code form e.g. `6.SP.5b` for `6.SP.B.5b` | Optional |
| `description` (222,865) | **The verbatim STATEMENT / description text** | May contain HTML (`<div>`) in some jurisdictions |
| `jurisdiction` (222,865) | State name, `Multi-State`, or `California` | See §4 |
| `academicSubject` (222,865) | One of `Mathematics`, `English Language Arts`, `Science`, `Social Studies` | |
| `gradeLevel` (222,865) | **JSON-encoded string array**, e.g. `"[\"6\"]"`, `"[\"9\",\"10\",\"11\",\"12\"]"` | Parse as JSON to get grades; `"K"`, `"PK"` used for early grades |
| `statementType` (221,394) | Fine-grained type: `Standard`, `Cluster`, `Domain`, `Component`, `Content Standard`, `Strand`, … (60+ values) | |
| `normalizedStatementType` (221,348) | Coarse type: `Standard` (150,536), `Standard Grouping` (54,632), `Other` (16,180) | Use to separate leaf standards from groupings |
| `caseIdentifierUUID` (222,865) | External IMS/CASE item UUID | NOT the graph join key |
| `caseIdentifierURI` (222,865) | `https://satchelcommons.com/ims/case/v1p0/CFItems/<uuid>` | |
| `author` (222,865) | Source body, e.g. `California Department of Education` | |
| `adoptionStatus` (222,865) | `Adopted`, `Pending Implementation`, `Draft` | |
| `isCurrent` (222,865) | `"true"` / `"false"` (string) | |
| `inLanguage` (222,865) | `en-US` (some `es`) | |
| `provider`, `license`, `attributionStatement`, `dateModified` | Provenance | |
| `notes` (22,274) | Extra scope notes, e.g. CA's `"[Linear, quadratic, and exponential …]"` | Optional |

There is **no parent pointer inside `properties`** — the standard→sub-standard hierarchy is
carried entirely by the `hasChild` relationship (§3).

### 2.4 `LearningComponent` property dictionary

Keys: `identifier`, `description` (the sub-skill text, e.g. *"Use models, including number
lines, to add integers between -20 and 20"*), `examples` (a JSON-encoded string array, often
`"[]"`), `academicSubject`, `author` (e.g. `Learning Commons`, `Achievement Network`),
`provider`, `license`, `attributionStatement`, `inLanguage`, `dateCreated`, `dateModified`.
**There is no `type`/`kind`/`misconception` discriminator** — a LearningComponent is only a
positive sub-skill, never a misconception (see §5).

---

## 3. Relationship schema

Top-level keys on every relationship: **`type`, `identifier`, `label`, `properties`,
`source_identifier`, `source_labels`, `target_identifier`, `target_labels`**.
`type` == `"relationship"` for all 456,620. `label` is the edge type. Inside `properties`,
`sourceEntityKey` / `targetEntityKey` name which node property the graph joined on (usually
`caseIdentifierUUID`), while the top-level `source_identifier`/`target_identifier` are the
resolved **`node.identifier`** values you actually join on.

### 3.1 Distinct relationship labels and counts

| `label` | Count | source_labels → target_labels | Meaning |
|---|---|---|---|
| `hasChild` | 223,462 | SFI→SFI (222,065); StandardsFramework→SFI (1,397) | **Standard hierarchy** (parent→child; populates `subStandards`) |
| `supports` | 137,380 | LearningComponent→SFI | **Standard ↔ learning component** (component supports the standard) |
| `hasEducationalAlignment` | 52,807 | Activity/Lesson/Assessment/LessonGrouping/Course→SFI | Curriculum→standard alignment (Class C) |
| `hasStandardAlignment` | 25,113 | SFI→SFI | **State-standard → CCSS crosswalk** (evidence-based, jaccard-scored) |
| `hasPart` | 15,944 | Lesson→Activity/Assessment, LessonGrouping→Lesson… | Curriculum internal structure (Class C) |
| `buildsTowards` | 757 | SFI→SFI | **Standard→standard PROGRESSION / prerequisite** (math only) |
| `hasReference` | 472 | Lesson↔Lesson/Activity/Assessment | Curriculum "use_after" references (Class C) |
| `relatesTo` | 284 | SFI→SFI | Related standards (conceptual link, **no sequence**) |
| `hasDependency` | 209 | LessonGrouping→LessonGrouping | Curriculum unit dependency (Class C) |
| `mutuallyExclusiveWith` | 192 | Assessment→Assessment | IM assessment alternatives (Class C) |

### 3.2 The four standard-relevant edges (with direction encoding)

**PROGRESSION — `buildsTowards` (757).** SFI→SFI. Its own `description`:
*"proficiency in one entity supports the likelihood of success in another, capturing a
directional progression without requiring strict prerequisite order."* Author: **Student
Achievement Partners** (the achievethecore CCSS coherence map), CC0.
**Direction: `source` is the earlier/prerequisite standard, `target` is the later standard it
builds toward** (verified: `8.SP.A.4` [grade 8] → `HSS-ID.B.5` [high school]).
- Prerequisites *of* a standard X = edges where `target_identifier == X` (sources are earlier).
- What X leads to = edges where `source_identifier == X`.
- **All 757 endpoints are `Multi-State` (CCSS) math** — progressions do NOT attach to any
  state jurisdiction (including California) directly. See §4.3 for the bridge.

Example record:
```json
{"label":"buildsTowards","source_identifier":"db51575f-e92e-5a08-904b-66b7b1a5a656",
 "target_identifier":"827a633a-b88a-5ce9-8a7a-18369c547363",
 "properties":{"relationshipType":"buildsTowards","author":"Student Achievement Partners",
   "sourceEntityKey":"caseIdentifierUUID","targetEntityKey":"caseIdentifierUUID", ...}}
```

**HIERARCHY — `hasChild` (223,462).** SFI→SFI (and StandardsFramework→top SFI).
`source` = parent, `target` = child. This is what populates a standard's `subStandards`.
Example: parent `82e186cf-…` →child `69da1959-…`.

**LEARNING COMPONENTS — `supports` (137,380).** **LearningComponent→SFI**. The component is
the source, the standard is the target. To find components for a standard X: edges where
`target_identifier == X`. California math standards ARE covered (2,406 such edges land on CA
math). Example: LC `2b76452f-…` supports SFI `11a0ef2b-…`.

**CROSSWALK — `hasStandardAlignment` (25,113).** SFI→SFI, `source` = a state standard,
`target` = the CCSS (`Multi-State`) standard. Its `description`: *"connects a State standard
to a CCSS standard when the two are supported by overlapping sets of Learning Components …
expressed through properties such as `jaccard` and LC counts. It does not imply sequence,
dependency, or pedagogical progression."* Extra properties: `jaccard`, `stateLCCount`,
`sharedLCCount`, `ccssLCCount`. This is the **bridge** that lets a California standard reach
the CCSS-side progression graph (§4.3).

### 3.3 MISCONCEPTIONS — none

There is **no standard→misconception relationship** and **no misconception node label**.
`find_misconceptions_for_standard` has no backing data in this export (see §5).

---

## 4. California mathematics coverage

### 4.1 California is its own jurisdiction AND its own framework

`jurisdiction == "California"` exists as a first-class value: **5,053** StandardsFrameworkItem
nodes total, broken down by subject:

| California subject | Items |
|---|---|
| English Language Arts | 1,501 |
| **Mathematics** | **1,467** |
| Science | 1,398 |
| Social Studies | 687 |

California math items belong to a **distinct framework node**, not to the Multi-State one:

- **California**: `StandardsFramework` `adccbae4-ff3a-5b87-b5f1-508324c2f6a4`, name
  *"California Common Core State Standards - Mathematics"*, author *California Department of
  Education*, sourced from `cde.ca.gov/…/ccssmathstandardaug2013.pdf`,
  `caseIdentifierUUID c6487102-d7cb-11e8-824f-0242ac160002`.
- **Multi-State**: `StandardsFramework` `6becf2d7-2232-5ead-983f-9f0a4de24ab7`, name
  *"Common Core State Standards for Math"*, author *Common Good Learning Tools*, sourced from
  `corestandards.org/…/Math_Standards1.pdf`,
  `caseIdentifierUUID c6496676-d7cb-11e8-824f-0242ac160002`.

**Verdict:** California adopts CCSS, but the data models it as a **separate California-jurisdiction
framework** (its own CASE UUIDs, its own node ids, some California-only additions such as
`HSG.GPE.A.3.1`), NOT as rows of the shared `Multi-State` CCSS framework. Every state is modeled
this way — one framework per state, plus one canonical `Multi-State` CCSS framework.

### 4.2 Counts

- **California math StandardsFrameworkItem = 1,467** (`jurisdiction=="California"` AND
  `academicSubject=="Mathematics"`); 1,276 have a `statementCode`.
- **Multi-State CCSS math StandardsFrameworkItem = 836** (`jurisdiction=="Multi-State"` AND
  `academicSubject=="Mathematics"`); 744 have a `statementCode`. These carry the Standards for
  Mathematical Practice (codes like `HS.MP2`, `3.MP8`) and the canonical CCSS content codes.

### 4.3 Example codes + grade spans

California math (code, gradeLevel):
`HSA-CED.A` (9–12), `HSA-CED.A.1` (9–12), `HSF-IF.C.8` (9–12), `HSF-IF.C.8.b` (9–12),
`HSG-CO.C` (9–12), `HSG-SRT.B` (9–12), `HSA-REI.C` (9–12), `HSG-C.A.4` (9–12),
`HSF-BF.A.1` (9–12), `HSG.GPE.A.3.1` (9–12, a California-specific addition),
plus K–8 items such as `8.SP.A.4` (grade 8), `5.NF.5.b` (grade 5).
Multi-State CCSS math: `1.NBT.A.1` (1), `5.NF.A` (5), `8.G.A` (8), `HSF-LE.A.1` (9–12),
`HSA-APR.B` (9–12), and the practice standards `HS.MP2`, `2.MP3`, `4.MP2`.

### 4.4 How California standards reach progressions (the bridge)

Because `buildsTowards` lives only on `Multi-State` nodes, a California standard reaches the
progression graph via the crosswalk:

```
CA SFI --hasStandardAlignment--> CCSS(Multi-State) SFI --buildsTowards--> CCSS(Multi-State) SFI
```

Verified example:
`8.SP.A.4` [California] → (crosswalk, jaccard≈1.0, identical code) `8.SP.A.4` [Multi-State]
→ (buildsTowards) `HSS-ID.B.5` [Multi-State]. There are **591** CA-math → CCSS-math crosswalk
edges (of 1,467 CA items; crosswalks exist at the leaf-`Standard` grain, not for
clusters/components). California's own learning components attach directly (2,406 `supports`
edges), so `find_learning_components_from_standard` works on CA nodes without the bridge.

---

## 5. Misconceptions finding — DEFINITIVELY ABSENT

Checked exhaustively:
- **No `Misconception` node label** (the only 8 labels are listed in §2.1).
- **No misconception relationship label** (the only 10 labels are listed in §3.1).
- **No misconception discriminator on `LearningComponent`** (its properties are positive
  sub-skills only; §2.4).
- A case-insensitive scan for `misconception` finds it in **0** relationships and in **15**
  nodes — all 15 are the ordinary English word appearing inside a standard's `description`/`notes`
  text (e.g. *"Identify and dispel misconceptions about American Indians today"*), never a data
  structure.

**Consequence:** the MCP's `find_misconceptions_for_standard` tool has no source data in the
public export and must return empty; the skills fall back to training knowledge for
misconceptions. `data/ca-math/misconceptions.jsonl` is written empty (0 records) as a defined,
stable path.

---

## 6. Field mapping — LC export → Overeducated target model

`Standard` (join spine = `node.identifier`):

| Target field | LC source | Exact name / notes |
|---|---|---|
| `case_uuid` | `node.identifier` | Bare UUIDv5; the value relationships join on. (The external CASE id is `properties.caseIdentifierUUID` — keep as a secondary id if you need IMS/CASE interop.) |
| `code` | `properties.statementCode` | e.g. `HSA-CED.A`; fall back to `properties.alternateStatementCode` when absent |
| `statement_text` | `properties.description` | Verbatim; strip HTML for jurisdictions that embed `<div>` |
| `academic_subject` | `properties.academicSubject` | `"Mathematics"` |
| `jurisdiction` | `properties.jurisdiction` | `"California"` / `"Multi-State"` |
| `grade` | `properties.gradeLevel` | JSON-decode the string array (`"[\"9\",\"10\",\"11\",\"12\"]"` → `["9","10","11","12"]`) |
| `parent` / `subStandards` | `hasChild` edge | parent = `source_identifier`, child = `target_identifier`; a node's parent = the `hasChild` edge whose `target_identifier` is that node; its `subStandards` = edges whose `source_identifier` is that node |
| `statement_type` | `properties.statementType` / `properties.normalizedStatementType` | use `normalizedStatementType` to split leaf `Standard` from `Standard Grouping` |

Edges / other classes:

| Target concept | LC source | Direction / notes |
|---|---|---|
| **Progression edge** | `buildsTowards` relationship | `source_identifier` = prerequisite/earlier, `target_identifier` = builds-toward/later. Math-only, `Multi-State` endpoints only. For a CA standard, hop via `hasStandardAlignment` first. |
| Related-standard edge | `relatesTo` relationship | non-directional conceptual link; `Multi-State` math only (284) |
| **CA→CCSS crosswalk** | `hasStandardAlignment` relationship | `source` = CA standard, `target` = CCSS standard; carries `jaccard`, `stateLCCount`, `sharedLCCount`, `ccssLCCount` |
| **LearningComponent** | `LearningComponent` node + `supports` relationship | component text = `LearningComponent.description`; link = `supports` edge with `source_identifier` = component, `target_identifier` = standard. `examples` = JSON array string. |
| **Misconception** | — | **No source in the public export.** Return empty; fall back to training knowledge. |
| Curriculum (IM) | `Activity`/`Lesson`/`Assessment`/`LessonGrouping`/`Course` nodes + `hasEducationalAlignment`/`hasPart`/`hasReference` | Class C; deferred for the CA-math v1 vertical |

---

## 7. Extracted California-math subset (`data/ca-math/`)

Produced by filtering the raw export to `academicSubject=="Mathematics"` AND
`jurisdiction ∈ {California, Multi-State}` and pulling the incident edges/nodes. All files are
JSONL of the original records (unchanged shape); join on `node.identifier`.

| File | Records | Contents |
|---|---|---|
| `standards.jsonl` | 2,303 | StandardsFrameworkItem nodes: **1,467 California** + **836 Multi-State CCSS** math |
| `hierarchy.jsonl` | 2,303 | `hasChild` edges touching a selected standard (parent/child → `subStandards`) |
| `progressions.jsonl` | 1,041 | `buildsTowards` (757) + `relatesTo` (284); all `Multi-State` math endpoints |
| `crosswalk.jsonl` | 591 | `hasStandardAlignment` CA-math → CCSS-math bridge edges (jaccard-scored) |
| `components.jsonl` | 6,056 | 4,203 `supports` edges (LearningComponent→standard) + 1,853 distinct `LearningComponent` nodes (distinguish by `type`: `"relationship"` vs `"node"`) |
| `misconceptions.jsonl` | 0 | Empty — no misconception data exists in the export |

Integrity (verified): all `buildsTowards` endpoints are present in `standards.jsonl`; all 591
crosswalk edges are CA-source & Multi-State-target; all 4,203 `supports` targets are in
`standards.jsonl` and every referenced LearningComponent node is present; all 2,303 standards
have a parent edge in `hierarchy.jsonl`.

> Note on scope: `hierarchy.jsonl` and `crosswalk.jsonl` are beyond the four originally-named
> output files but are load-bearing for the 7-tool MCP — `subStandards` (part of
> `find_standard_statement`) needs `hasChild`, and CA progressions
> (`find_standards_progression_from_standard`) are unreachable without the crosswalk. Both are
> included so the CA-math subset is self-contained for the MCP.
