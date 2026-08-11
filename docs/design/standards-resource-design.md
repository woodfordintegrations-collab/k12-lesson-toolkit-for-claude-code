# Overeducated — Standards Resource (v1) Design

**Design record.** Written 2026-07-22, before the build. Kept as the rationale for the
shape the MCP server ended up with, not as a live plan.
**Ratified decisions this builds on:** store-plus-MCP reframe (yes), v1 tool cut (yes, corrected below against the extracted contract).
**Sourcing:** build the server, adopt the data — see `docs/reference/sourcing-verdict.md`.

---

## 1. Goal

Reproduce the functionality of the **Learning Commons Knowledge Graph** (a
Claude-for-Teachers-only MCP connector) from **openly-licensed** data, so the forked
`k12-teacher-skills` plugin runs **grounded** without a Claude for Teachers account.

Success for v1 is concrete: with our MCP registered, the planning skill run on a
California-math request grounds against our data (resolves a real CA standard, names a
real prerequisite) and its teacher-plan footer flips from *"Generated without the Learning
Commons KG…"* to a positive provenance stamp.

Constraint (corrected): **openly-licensed sources only, and never the gated connector.**
We do not scrape or reverse-engineer the private-beta Learning Commons API/MCP (its Terms
bar that). We DO adopt Learning Commons' separately-published open-data export (CC BY 4.0 /
CC0), which they release for exactly this reuse, with attribution. See
`docs/reference/sourcing-verdict.md` for the verified decision and license basis.

---

## 2. Shape: one store, two faces

```
        openly-licensed sources (Learning Commons KG export, CCSP, achieve-the-core)
                                   │  ingest
                                   ▼
                    ┌──────────────────────────────┐
                    │   CASE-shaped standards store  │   case_uuid == LC node identifier
                    │   (Standard / Progression /    │
                    │    Misconception / Component)  │
                    └───────────────┬───────────────┘
                        ┌───────────┴───────────┐
                        ▼                       ▼
             machine face: MCP server     human face: wiki (read view)
             (7-tool KG contract)         rendered from the same store
                        │
                        ▼
        forked k12-teacher-skills (unchanged) ground at Step 2
```

The MCP is what actually replaces the connector (the skills call tools, not a website).
The wiki is a rendered read-view of the identical store, so the human reference and the
skill-grounding data cannot drift. **v1 builds the store + MCP; the wiki is a thin,
deferred read view** (minimal or stubbed in v1).

---

## 3. The contract to reproduce (from the extracted KG contract)

The skills detect the connector purely by **tool availability** — Step 0.3 checks whether
`find_standard_statement` (and siblings) are registered in the conversation. There is no
handshake payload. So our MCP **registers all seven tool names** to read as "connected,"
and implements them to the depth below.

| Tool | v1 depth | Params | Must return |
|---|---|---|---|
| `find_standard_statement` | **Full** | `code` *or* `keywords[]`; `academicSubject="Mathematics"`; `jurisdiction="California"` | `standards[]`, each `{code, statement_text (verbatim), caseIdentifierUUID, subStandards[]}`. Code search is **prefix match** (leaf → itself; parent `2.OA` → `2.OA` + all `2.OA.*`). Keyword search matches if ANY keyword appears. |
| `find_standards_progression_from_standard` | **Full** | `caseIdentifierUUID`; `direction="backward"\|"forward"` | The single primary prerequisite (`backward`) / forward (`forward`) standard, verbatim (code + text). **Math-only** by design. |
| `find_misconceptions_for_standard` | **Best-effort** | `caseIdentifierUUID`; `subject="Mathematics"` | ≥3 misconceptions, each `{student_behavior, teacher_move}`. Empty is tolerated (skill drafts 3 from training knowledge). |
| `find_learning_components_from_standard` | **Best-effort** | `caseIdentifierUUID` | up to 5 sub-skill description strings. Empty tolerated. |
| `find_curriculum_lessons` | **Implemented** | `caseIdentifierUUID`/`ordinalName`/`lessonName`; `author` | Was stubbed on a false premise — see `../reference/sourcing-verdict.md`. 3,301 lessons, ranked teaches-before-builds-toward. The curriculum aligns **only to Multi-State CCSS nodes** (all 561 of them; zero California), so a state standard reaches it through the crosswalk bridge and the result carries `alignedVia`. Without that bridge every lookup of a California standard returned `[]`. |
| `find_materials_for_lesson` | **Implemented** | `lessonIdentifier`; `materialSource[]` | 12,599 activities and assessments, in lesson sequence. |
| `list_standards_for_mathematical_practice` | **Implemented** | none | MP1-MP8, one entry each, taken from the slice's own jurisdiction rather than the Multi-State copy. |

**Correction vs the pitched "three-tool core":** I originally proposed statement + SMP-list
+ progression. The extracted contract shows the SMP-list tool is never invoked, while
misconceptions + components are in the mandatory math batch. v1 therefore fully implements
**statement + progression** and best-efforts **misconceptions + components**. That reordering
of priorities was right; what followed from it was not.

**Correction to this document, 2026-08-11.** Three of the seven were shipped as registered
stubs and all three are now implemented. Two of the three reasons recorded here were wrong,
and wrong in the same way — each justified a stub by something other than the data:

- `find_curriculum_lessons` / `find_materials_for_lesson` were stubbed because the curriculum
  layer was "not in the public export". It was: 16,021 nodes of it. The join failed on an
  identifier-space mismatch that returns an empty list and raises nothing, which is
  indistinguishable from absence. See `../reference/sourcing-verdict.md`.
- `list_standards_for_mathematical_practice` was stubbed because *the skills never call it*.
  That is a fact about the consumer, not about the data, and the data — MP1 to MP8 with full
  statements — was in the shipped export from the first build. A registered tool returning
  `[]` is indistinguishable from a subject that has no practice standards.

The general lesson, recorded because it recurred three times: **an empty return is not
evidence of an empty source.** Where a tool cannot answer, the reason belongs in the tool's
docstring as a measurement, with the query that produced it.

### Join keys
- `caseIdentifierUUID` — the spine. Returned by `find_standard_statement`, consumed by all
  progression/misconception/component calls. We adopt Learning Commons' node `identifier`
  as this UUID (their graph ids are already stable), maximizing parity with the real connector.
- `lessonIdentifier` — curriculum lessons → materials.

### Downstream fields the skills hard-require
- `shared.standard_code` ← `find_standard_statement.code`
- `shared.standard_text` ← `find_standard_statement` verbatim statement text
  These render the target-standard callout and each differentiation tier's eyebrow. If
  these are wrong or missing, the authored JSON breaks. **These two are the acceptance core.**

### Footer to flip (math, planning)
Suppress/replace: *"Generated without the Learning Commons Knowledge Graph. Standards and
misconceptions reflect general best practice."* → a positive stamp, e.g. *"Grounded in
public California Common Core mathematics standards."* (Exact stamp string is a v1 decision;
default proposed here.)

---

## 4. Data model (CASE / 1EdTech-shaped)

Four entities, one store. `case_uuid` adopts the Learning Commons node `identifier` (stable
graph ids), so it satisfies the skills' `caseIdentifierUUID` contract directly — no minting.

- **Standard**: `case_uuid` (PK), `code`, `statement_text`, `academic_subject`,
  `jurisdiction`, `grade`, `parent_uuid` (nullable → builds `subStandards`), `source`,
  `source_license`.
- **Progression** (edge): `from_uuid`, `to_uuid`, `direction` (`backward`/`forward`),
  `source`. Backward = prerequisite, forward = next.
- **Misconception**: `case_uuid` (FK), `student_behavior`, `teacher_move`, `source`.
- **LearningComponent**: `case_uuid` (FK), `ordinal`, `description`, `source`.

The exact LC-field → model-field mapping is pinned in `docs/reference/lc-export-schema.md`
(produced from the real export). Store implementation: a single embedded store (SQLite via a
thin repository layer) — the MCP depends only on the repository interface, not the storage
engine, so it can be swapped. Every record carries `source` + `source_license` for
attribution compliance.

---

## 5. Data sourcing (v1, California math) — ADOPT

Decided by the build-vs-adopt sourcing gate (`docs/reference/sourcing-verdict.md`):
**adopt the data, build the server.**

- **Primary:** Learning Commons' public knowledge-graph JSONL export (`nodes.jsonl` +
  `relationships.jsonl`, v1.11.0, CC BY 4.0 / CC0, public no-auth CDN). It already unifies
  standards + learning components + progressions as a graph — the exact data backing the
  connector's contract. We filter it to the California-math subset and map it into the store.
- **Supplementary / cross-check:** `commonstandardsproject/api` (Apache-2.0 / CC BY 3.0 US)
  for a second standards-statement source + GUIDs; `allenai/achieve-the-core` (ODC-BY) for a
  CCSS-Math coherence/prerequisite cross-check.
- **Believed absent from the public export, wrongly (now built):** curriculum lessons + instructional materials
  (`find_curriculum_lessons`, `find_materials_for_lesson`). Misconceptions presence in the
  export is being verified; if absent, the misconceptions tool returns empty and the skills
  fall back to training knowledge.

**Attribution (shipped):** every record carries its source + license; the product carries the
Learning Commons / 1EdTech / Achievement Network / Student Achievement Partners attribution
string. **Never** the gated API/connector.

**Open legal item (commercial ship only):** confirm CCSS / NGA-CCSSO primary-source + 1EdTech
republication terms — an open question at the time; does not block local build/validation.

---

## 6. MCP server

- Python MCP server (stdio) exposing the seven tools with schemas matching §3 exactly.
- Depends on a `StandardsRepository` interface; no business logic in tool handlers beyond
  shaping the contract responses.
- Ships a registration snippet for the fork's `plugin/.mcp.json` so the acceptance test can
  wire it in.
- Tool responses are pure functions of the store → fully unit-testable without a model.

---

## 7. Error handling / edge cases

- `find_standard_statement` code miss → return empty `standards[]` (skill falls back to
  keyword search, then to its own cap-at-3 logic). Never raise.
- Keyword search → OR-match across provided keywords; return best matches.
- Prefix semantics on code exactly as documented (parent returns parent + descendants).
- `jurisdiction="California"` → CA-CCSS-M; unknown jurisdiction → CCSS default.
- Progression/misconception/component with unknown UUID → empty, never raise.
- All tools total-function over bad input: empty/typed-empty results, never a traceback
  (the skills forbid surfacing errors to teachers).

---

## 8. Testing & acceptance

- **Deterministic contract tests** (pytest): for a set of known CA-math standards
  (e.g. `6.RP.A.2`, `4.NF.B.3.d`, a `2.OA` parent for prefix), assert each tool returns the
  documented shape and correct data — codes, verbatim text, UUID stability, prefix
  expansion, backward/forward progression, misconception `{student_behavior, teacher_move}`.
- **Store integrity tests**: every `Progression` endpoint resolves to a real `Standard`;
  every `Misconception`/`Component` FK resolves; UUIDs stable across rebuilds.
- **MCP protocol test**: server starts, lists all seven tools, round-trips a
  `find_standard_statement` call.
- **End-to-end acceptance (manual, documented):** register the MCP in the fork's
  `plugin/.mcp.json`, run the planning skill on a CA-math request in an interactive Claude
  session, confirm it grounds and the footer flips. This step needs a live model session,
  so it is staged with exact instructions, not run unattended.

---

## 9. Tooling & layout

Conventions: Python 3.12, `ruff`,
`mypy`, `pytest`, `pyproject.toml`. Proposed package layout:

```
k12-lesson-toolkit/
  pyproject.toml
  src/k12_toolkit/
    model.py            # entities (§4)
    repository.py       # StandardsRepository interface + store impl
    ingest/             # LC-export ingestion (CA-math filter + field mapping)
    mcp/server.py       # 7-tool MCP server (§3, §6)
    wiki/               # deferred read view
  data/
    raw/                # full downloaded exports (gitignored)
    ca-math/            # filtered CA-math subset (committed)
  tests/
  docs/
```

---

## 10. v1 scope boundaries (non-goals)

- Subjects other than math; states other than California. (Store is multi-jurisdiction by
  design; only CA-math data is loaded in v1.)
- Curriculum/HQIM tools (`find_curriculum_lessons`, `find_materials_for_lesson`) — built.
  The reason given at the time for stubbing them, that the data was not in the public
  export, was false: the export carries 16,021 CC BY 4.0 curriculum nodes, and the join is
  one hop.
- The human wiki beyond a thin read view.
- Any change to the upstream skills' code. (We wire in via `.mcp.json` only; the connector-
  absent seam already exists.)
- The teacher interface (Claude Cowork) — separate, later track.
- Any push to a remote — local commits only until the owner ships it.
