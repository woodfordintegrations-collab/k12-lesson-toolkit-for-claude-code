# Sourcing Verdict — build vs adopt (2026-07-22)

Decision record for this project's standards layer. Produced by a six-angle GitHub/web
sweep + a five-gate vetting pass. Evidence verified in-session (LICENSE.md read verbatim;
export HEAD returned HTTP 200).

## Verdict

**BUILD the 7-tool MCP server. ADOPT the data.**

- The Learning Commons **connector** is closed: the REST API and MCP server are private-beta
  only, no server source is published in their public repo, and the Terms bar
  reverse-engineering. No OSS MCP reproduces the 7-tool contract (every candidate fails the
  stars + review-culture gates). → **the server is built.**
- The **data** backing the contract is published by Learning Commons as public, no-auth
  JSONL under **CC BY 4.0** (state standards via 1EdTech; learning components via Achievement
  Network) + **CC0** (progressions via Student Achievement Partners). → **the data is
  adopted, not rebuilt.**

**CONDITIONAL** (for commercial ship, not local dev): confirm the CCSS / NGA-CCSSO
primary-source + 1EdTech republication attribution terms are satisfied. See the open legal
item below.

## Correction to an earlier claim

Earlier I wrote "do not touch the KG's data; rebuild from public sources." That conflated two
things. The **gated API/connector** should not be scraped (ToS bars reverse-engineering). But
Learning Commons **separately publishes the whole graph** as an openly-licensed data product
(CC BY 4.0 / CC0) for reuse including commercial. Adopting that published export is exactly
what the license grants — so we adopt their open export (near parity with what Claude for
Teachers users get) instead of hand-aggregating CCSS-M. Better coverage, clean license.

## Adopt / borrow / build

**Adopt (data, no build):**
- `learning-commons-org/knowledge-graph` JSONL exports (CC BY 4.0 / CC0) — **PRIMARY**.
  Standards + learning components + progressions, unified as a graph. Backs
  `find_standard_statement`, `find_standards_progression_from_standard`,
  `find_learning_components_from_standard`, `list_standards_for_mathematical_practice` (and
  `find_misconceptions_for_standard` if misconceptions are present — being verified).
- `commonstandardsproject/api` (Apache-2.0 / CC BY 3.0 US) — supplementary statements + GUIDs.
- `allenai/achieve-the-core` (ODC-BY) — CCSS-Math coherence/prerequisite cross-check.

**Borrow as reference (patterns only, not forked or linked):**
- Learning Commons MIT tutorials (`compare_standards`, `generate_prereq_practice`,
  `working_with_standards`) — query logic.
- `swoopeagle/standardgraph` (MIT, Python) — MCP plumbing patterns.
- `smilne3/common-standards-mcp` (MIT) — lookup-tool slice.

**Build from scratch:**
- The entire 7-tool MCP server — no forkable server exists.
- Curriculum-lessons + materials layer (`find_curriculum_lessons` / `find_materials_for_lesson`)
  — **built.** See the correction below: the reason originally recorded for stubbing these
  was wrong, and once that was measured the join took one hop each.
- Per-record CC BY 4.0 attribution shipping (Learning Commons / 1EdTech / Achievement Network
  / Student Achievement Partners).

> **Correction, verified 2026-08-11.** This document previously said the curriculum-lessons
> and materials layer was "NOT in the public LC JSONL". That is false, and it was false when
> written. Counting `labels` across all 247,786 nodes of the v1.11.0 export:
>
> | label | count |
> |---|---|
> | `Lesson` | 2,550 |
> | `LessonGrouping` | 764 |
> | `Activity` | 8,173 |
> | `Assessment` | 4,516 |
> | `Course` | 18 |
> | **curriculum nodes, total** | **16,021** |
>
> All 2,550 `Lesson` nodes carry `license: creativecommons.org/licenses/by/4.0/` and
> `author: Illustrative Mathematics`, with `courseCode`, `curriculumLabel`, `ordinalName`
> and `gradeLevel` beside them. This is openly licensed curriculum data, sitting in the
> export this project already downloads.
>
> Both tools are now implemented against that data: `scripts/extract_curriculum.py` filters
> 3,301 lessons, 12,599 materials and 17,218 alignment edges into the shipped export, and
> `find_curriculum_lessons` / `find_materials_for_lesson` serve them.
>
> The join is one hop each. What made it look impossible was an identifier-space mismatch:
> alignment edges key on the node `identifier` while the records also carry a
> `caseIdentifierUUID`, and the two never coincide. Joining on the wrong one returns an
> empty list and raises nothing, which is indistinguishable from the data being absent.
> That is how "not in the public export" got written down as a fact.

## Ruled out (strongest failures)

| Repo | Why |
|---|---|
| `galacticpolymath/standardX` | GPL-3.0 — copyleft, hard fail for a commercial ship |
| `learning-commons-org/evaluators` | bundles CLEAR Corpus CC BY-NC-SA (NONCOMMERCIAL) — avoid |
| `GarethManning/education-agent-skills` (456★) | content CC BY-SA (share-alike) + off-target (prompts, not standards) |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | ships no standards content; depends on paid Certica/AB Connect |
| `OpenCASE`, `swoopeagle/standardgraph`, `smilne3/common-standards-mcp` | sub-threshold stars + solo maintainers — reference only |
| `commoncurriculum/*`, `achievethecore/atc-coherence-map` (code) | no LICENSE file (all-rights-reserved) and/or stale |

## License basis (verified in-session)

- LC `LICENSE.md`: *"Knowledge Graph code is licensed under MIT"* + *"provided by Learning
  Commons under the CC BY 4.0 license"* (state standards CC BY 4.0 via 1EdTech; learning
  components CC BY 4.0 via Achievement Network; learning progressions CC0 via Student
  Achievement Partners).
- LC `README.md`: *"Local JSONL … Publicly available"*; REST API + MCP Server *"available
  only to private beta users."*
- Export: `cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/{nodes,relationships}.jsonl`
  — public, no credentials (~292 MB nodes).
- Attribution string to ship (from the data itself): *"Knowledge Graph is provided by
  Learning Commons under the CC BY-4.0 license. Learning Commons received state standards and
  written permission under CC BY-4.0 from 1EdTech."*

## Open legal item (before commercial ship, not before local build)

Confirm the CCSS / NGA-CCSSO primary-source terms and 1EdTech republication terms are
satisfied for a commercial product. Local development + validation are unaffected.
