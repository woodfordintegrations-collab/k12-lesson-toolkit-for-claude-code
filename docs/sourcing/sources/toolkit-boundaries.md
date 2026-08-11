---
source_url: 
fetched: 2026-08-07
http_status: n/a (local git repository, read-only)
role: primary
covers: evidence-store-ingest-boundary, evidence-k12-lesson-toolkit-acceptance-record, evidence-kg-coverage-and-gaps, source-learning-commons-kg, concept-attribution-per-record, trap-empty-facet-reads-as-success, practice-assemble-an-attribution-block
---

# k12-lesson-toolkit: what the store holds, what it does not, the ingest boundary, and the acceptance record

## 0 · Provenance

Repository: ``.
Git HEAD at staging: `1ad5649dd4158c5a96a11561f678a2d877747000`, `Wed Jul 22 22:14:08 2026 -0700`.
Local system clock at staging: `2026-08-07 21:17:58 PDT`. See the sibling extract
`k12-lesson-toolkit-store-and-mcp.md` §0 for the full file inventory, mtimes and the date note.

Everything numbered below is either (a) measured in-session against `data/k12-lesson-toolkit.db`
opened read-only, or `data/ca-math/*.jsonl` parsed line by line, or (b) quoted from a repo
document and labelled as that document's claim. The two are never mixed in one sentence.

---

## 1 · What the store contains, measured

`data/k12-lesson-toolkit.db`, 2,342,912 bytes, mtime `2026-07-22 07:41:36`. Row counts by
`SELECT COUNT(*)`:

| Table | Rows |
|---|---|
| `standards` | 2303 |
| `progressions` | 1454 |
| `misconceptions` | 0 |
| `learning_components` | 4203 |

Further measurements on `standards`:

- distinct non-empty `code` values: **794**
- rows with an empty `code`: **283**
- by jurisdiction: `California` **1467**, `Multi-State` **836**
- distinct `source_license` values: exactly one, `https://creativecommons.org/licenses/by/4.0/`, on all **2303** rows

`progressions` by `source` and `direction`:

| source | direction | rows |
|---|---|---|
| `Learning Commons KG v1.11.0` | backward | 361 |
| `Learning Commons KG v1.11.0` | forward | 305 |
| `Learning Commons KG v1.11.0 (via CA->CCSS crosswalk)` | backward | 434 |
| `Learning Commons KG v1.11.0 (via CA->CCSS crosswalk)` | forward | 354 |

`learning_components`, all **4203** rows carry `source = 'Learning Commons KG v1.11.0'`.
The shape of that number matters and is easy to misreport:

- **4,203** is the number of component **attachments** (rows), one per component-to-placement pair.
- **1,853** distinct component `description` strings.
- **1,115** distinct `case_uuid` values carry at least one component.
- **183** placements carry more than five components.
- **41** components is the maximum on any single placement.

### 1.1 The store's own schema is thinner than the export it came from

`PRAGMA table_info` on each table, measured columns:

| Table | Columns |
|---|---|
| `standards` | `case_uuid`, `code`, `statement_text`, `academic_subject`, `jurisdiction`, `grade`, `parent_uuid`, `source`, `source_license` |
| `progressions` | `from_uuid`, `to_uuid`, `direction`, `source` |
| `misconceptions` | `case_uuid`, `student_behavior`, `teacher_move`, `source` |
| `learning_components` | `case_uuid`, `ordinal`, `description`, `source` |

**Only `standards` has a `source_license` column.** Progressions, misconceptions and learning
components carry a free-text `source` string and no licence field at all. No table anywhere
carries `attributionStatement`.

This is a boundary a rights-facing page must state, because `NOTICE` makes a claim that is
true of one artifact and not the other. `NOTICE` lines 21 to 23, verbatim:

> The data under data/ca-math/ is a filtered derivative of the Learning Commons public
> export, retaining each record's `license` and `attributionStatement` fields. We do not
> use the gated Learning Commons API/MCP connector; only the openly-licensed export.

Measured: that sentence is accurate about `data/ca-math/*.jsonl`, which are the original
records unchanged in shape. It is not accurate about `data/k12-lesson-toolkit.db`, which is the
artifact the MCP actually reads. The per-record `attributionStatement` does not survive
ingest, and the per-record `license` survives only for standards. The design spec asserts the
stronger claim, §4 line 116, verbatim: "Every record carries `source` + `source_license` for
attribution compliance." Measured, three of four tables have no `source_license` column.

---

## 2 · What the store does not contain

### 2.1 Misconceptions: zero, by absence in the upstream export

- `data/ca-math/misconceptions.jsonl`: **0 bytes**, mtime `2026-07-22 07:22:13`. Every sibling
  file in that directory is between 851,166 and 6,142,448 bytes.
- `misconceptions` table: **0 rows**.

`ingest/builder.py` module docstring, lines 3 to 5, verbatim:

> Reads the five populated ``data/ca-math/*.jsonl`` files (``misconceptions.jsonl`` is empty
> by design — no misconception data exists in the public export) and maps them into the four
> store tables defined by :class:`~k12-lesson-toolkit.repository.SqliteStandardsRepository`.

The upstream finding, `docs/reference/lc-export-schema.md` §5 lines 233 to 248, verbatim in
full because it is the evidentiary basis and its exhaustiveness is the point:

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
>
> **Consequence:** the MCP's `find_misconceptions_for_standard` tool has no source data in the
> public export and must return empty; the skills fall back to training knowledge for
> misconceptions. `data/ca-math/misconceptions.jsonl` is written empty (0 records) as a defined,
> stable path.

The store therefore has no misconception data for **any** code, not merely none for a
particular family. The relevant handler still reports success. `server.py` lines 174 to 195
implement it and its docstring line 180 reads, verbatim: "Return ``{student_behavior, teacher_move}`` records. Empty is tolerated."

### 2.2 Four of the seven tools return empty on every call in v1

Three are constant stubs. `server.py` lines 217 to 237, verbatim:

```python
def find_curriculum_lessons_impl(
    caseIdentifierUUID: str | None = None,
    ordinalName: str | None = None,
    lessonName: str | None = None,
    author: str | None = None,
) -> dict[str, Any]:
    """Registered stub: curriculum/HQIM is not in the public export (spec §5)."""
    return {"lessons": []}


def find_materials_for_lesson_impl(
    lessonIdentifier: str,
    materialSource: list[str] | None = None,
) -> dict[str, Any]:
    """Registered stub: instructional materials are not in the public export (spec §5)."""
    return {"materials": []}


def list_standards_for_mathematical_practice_impl() -> dict[str, Any]:
    """Registered stub: the skills never consume the SMP list (spec §3)."""
    return {"standardsForMathematicalPractice": []}
```

The fourth, `find_misconceptions_for_standard`, is fully implemented but has no backing rows,
so it returns `{"misconceptions": []}` for every input. Measured: `misconceptions` table has
0 rows.

Net: `find_standard_statement`, `find_standards_progression_from_standard` and
`find_learning_components_from_standard` can return data. The other four cannot, in v1.

### 2.3 Related-standard edges are dropped, counted, never mapped

`ingest/builder.py` module docstring lines 31 to 33, verbatim:

> - **relatesTo** — non-sequential related edges have no home in the model (``Progression`` is only
>   backward/forward, and there is no related-edge table). They are skipped and counted, never
>   mapped onto backward/forward.

Measured at ingest: `relatesto_skipped: 284`. The upstream count agrees:
`lc-export-schema.md` §3.1 lists `relatesTo` at **284** with the note "Related standards
(conceptual link, **no sequence**)".

### 2.4 The human wiki is three uncommitted files

`git status --porcelain` returns exactly `?? wiki/`. The directory holds three untracked
files, dated 2026-07-23:

| File | Bytes |
|---|---|
| `wiki/VOICE.md` | 2498 |
| `wiki/6.RP.md` | 7848 |
| `wiki/6.RP-definitions.md` | 2693 |

`wiki/6.RP.md` opens, verbatim (lines 3 to 11):

> Misconception entries for the 6.RP.A cluster. Voice is governed by [VOICE.md](VOICE.md):
> mistakes are expected, respected, and inspected. Each entry names the student behavior,
> gives the teacher a move in a real human voice, and cites the source that grounds it.
>
> This is the starting set for the cluster, not the finished page. Each standard grows
> toward roughly three entries as we add them.
>
> Each entry carries the California `case_uuid` so the human wiki and the machine store
> (`data/ca-math/misconceptions.jsonl`) stay pinned to the same standard and cannot drift.

The pin it describes has no store side: `data/ca-math/misconceptions.jsonl` is 0 bytes and
the `misconceptions` table has 0 rows. These misconception entries are hand-authored prose,
uncommitted, and not reachable through any MCP tool.

An entry cites its own rights position inline. `wiki/6.RP.md`, the "Grounds" line of the
first entry, verbatim:

> *Grounds:* Illustrative Mathematics grade 6 ratio task (part-to-part vs part-to-whole),
> CC BY-NC-SA 4.0, cite and link only. Standard text and example: CCSS-M / California
> Department of Education, public.

---

## 3 · The ingest boundary

### 3.1 The filter that produced the subset

`docs/reference/lc-export-schema.md` §7 lines 282 to 293, verbatim:

> Produced by filtering the raw export to `academicSubject=="Mathematics"` AND
> `jurisdiction ∈ {California, Multi-State}` and pulling the incident edges/nodes. All files are
> JSONL of the original records (unchanged shape); join on `node.identifier`.
>
> | File | Records | Contents |
> |---|---|---|
> | `standards.jsonl` | 2,303 | StandardsFrameworkItem nodes: **1,467 California** + **836 Multi-State CCSS** math |
> | `hierarchy.jsonl` | 2,303 | `hasChild` edges touching a selected standard (parent/child → `subStandards`) |
> | `progressions.jsonl` | 1,041 | `buildsTowards` (757) + `relatesTo` (284); all `Multi-State` math endpoints |
> | `crosswalk.jsonl` | 591 | `hasStandardAlignment` CA-math → CCSS-math bridge edges (jaccard-scored) |
> | `components.jsonl` | 6,056 | 4,203 `supports` edges (LearningComponent→standard) + 1,853 distinct `LearningComponent` nodes (distinguish by `type`: `"relationship"` vs `"node"`) |
> | `misconceptions.jsonl` | 0 | Empty — no misconception data exists in the export |

Independently measured by this agent, parsing each file line by line: `standards.jsonl` 2303
records, `progressions.jsonl` 1041, `crosswalk.jsonl` 591, `components.jsonl` 6056. The
schema document's counts hold.

On-disk sizes, measured: `components.jsonl` 6,142,448 B, `crosswalk.jsonl` 851,166 B,
`hierarchy.jsonl` 2,806,489 B, `misconceptions.jsonl` 0 B, `progressions.jsonl` 1,164,684 B,
`standards.jsonl` 2,890,552 B. The raw export is retained locally and gitignored:
`data/raw/nodes.jsonl` 292,652,341 B, `data/raw/relationships.jsonl` 520,406,049 B, both
mtime 2026-07-22.

### 3.2 The ingest run, re-executed at staging

This agent ran `.venv/bin/python -m k12-lesson-toolkit.ingest --source data/ca-math --db <scratchpad>/probe.db`
into a scratch path, not into the repo. The repo's `data/k12-lesson-toolkit.db` was not modified;
its mtime is still `2026-07-22 07:41:36`. Output verbatim, minus the scratch path:

```
Built <scratch>/probe.db from data/ca-math
  standards: 2303
  progressions_backward: 795
  progressions_forward: 659
  learning_components: 4203
  standards_without_code: 283
  progressions_direct: 666
  progressions_bridged: 788
  relatesto_skipped: 284
  component_edges_orphaned: 0
  component_edges_missing_standard: 0
  html_texts_stripped: 0
  non_multistate_buildstowards_endpoints: 0
  bridge_self_loops_avoided: 0
  multi_parent_children: 0
```

The ingest is reproducible: these counts match the committed store's measured row counts
exactly, and `standards_without_code: 283` matches the store's 283 empty-code rows.

The `IngestStats` field list is `ingest/builder.py` lines 71 to 85, and every field above is
one of them.

### 3.3 The California bridge, which is where most progression rows come from

`ingest/builder.py` module docstring lines 25 to 30, verbatim:

> - **California bridge** — CA standards carry no ``buildsTowards`` (all 757 endpoints are
>   Multi-State CCSS). A CA standard C reaches the progression graph via the crosswalk
>   ``C --hasStandardAlignment--> E`` (highest ``jaccard`` first): backward-of(C) = prereq-of(E),
>   forward-of(C) = forward-of(E). If the chosen CCSS neighbour has exactly one CA standard that
>   crosswalks to it (a clean reverse crosswalk) we return that CA equivalent; otherwise the CCSS
>   neighbour verbatim. These rows are tagged ``source = SOURCE_BRIDGED``.

The two source stamps, `ingest/builder.py` lines 50 to 51, verbatim:

```python
SOURCE = "Learning Commons KG v1.11.0"
SOURCE_BRIDGED = "Learning Commons KG v1.11.0 (via CA->CCSS crosswalk)"
```

Measured: 788 of the 1,454 progression rows carry the bridged stamp, 666 the direct stamp.
More than half of every prerequisite this store can serve is a derived edge, not an edge
present in the upstream export. A page that says "the store's prerequisites come from
Student Achievement Partners" is imprecise: the CCSS-side edge does, the CA-side attachment
is this repo's own inference through a jaccard-scored crosswalk.

The primary-edge rule, `ingest/builder.py` lines 22 to 24, verbatim:

> - **Primary edge selection** — ``buildsTowards`` carries no priority ranking, so when a node has
>   several prerequisites/next-standards the primary is the one with the lowest node identifier
>   (deterministic and stable across rebuilds). The store returns a single primary anyway.

So "the prerequisite" is one arbitrary-but-stable choice among possibly several, selected by
lexicographic identifier order. It is not a pedagogically ranked answer.

### 3.4 Text handling at ingest

`ingest/builder.py` lines 56 to 58, verbatim:

> # LaTeX ($...$) is part of the standard text and must survive verbatim; real HTML tags must be
> # stripped. A tag starts with a letter (or /letter), which never matches a math inequality like
> # "x < c" or "a > 1" (space / digit after the angle bracket).

Measured on this subset: `html_texts_stripped: 0`. No CA-math or Multi-State-math record in
this export needed HTML stripping, so the stored `statement_text` is byte-identical to the
export's `properties.description` for all 2,303 rows. The upstream schema note says HTML does
occur elsewhere: `lc-export-schema.md` §2.3, verbatim, "May contain HTML (`<div>`) in some
jurisdictions."

---

## 4 · CONTRADICTION 1 · the curriculum-lessons layer

Two repo documents, both in `docs/reference/`, both dated 2026-07-22, disagree about whether
the curriculum layer is in the public export. Both readings are recorded here. Neither is
edited. This wiki does not own that repository.

### Reading A: it is not in the export

`docs/reference/sourcing-verdict.md` lines 49 to 52, verbatim:

> **Build from scratch:**
> - The entire 7-tool MCP server (k12-lesson-toolkit) — no forkable server exists.
> - Curriculum-lessons + materials layer (`find_curriculum_lessons` / `find_materials_for_lesson`)
>   — NOT in the public LC JSONL. Biggest genuine build gap; **stubbed in v1**.

The same reading is repeated in three further places:

- `docs/superpowers/specs/2026-07-22-standards-resource-design.md` §5 lines 132 to 133, verbatim: "**Not in the public export (stubbed in v1):** curriculum lessons + instructional materials (`find_curriculum_lessons`, `find_materials_for_lesson`)."
- `docs/superpowers/specs/2026-07-22-standards-resource-design.md` §10 lines 214 to 215, verbatim: "Curriculum/HQIM tools (`find_curriculum_lessons`, `find_materials_for_lesson`) — stubbed (not in the public export)."
- `docs/handoff/2026-07-22-overnight-build.md` lines 80 to 81, verbatim: "Curriculum tools (`find_curriculum_lessons` / `find_materials_for_lesson`) are stubbed (that data is not in the public export)."
- The code says it too. `server.py` line 223, verbatim: `"""Registered stub: curriculum/HQIM is not in the public export (spec §5)."""`

### Reading B: 16,021 nodes of exactly that layer are in the export

`docs/reference/lc-export-schema.md` §2.1, the full label census, verbatim:

> | `labels` | Count | Role |
> |---|---|---|
> | `StandardsFrameworkItem` | 222,865 | A single standard / cluster / domain statement (Class A corpus) |
> | `LearningComponent` | 8,686 | A deconstructed sub-skill that supports a standard (Class B) |
> | `Activity` | 8,173 | Illustrative Mathematics curriculum activity (Class C) |
> | `Assessment` | 4,516 | IM assessment (Class C) |
> | `Lesson` | 2,550 | IM lesson (Class C) |
> | `LessonGrouping` | 764 | IM unit / section (Class C) |
> | `StandardsFramework` | 214 | A framework header (one per jurisdiction×subject), parent of its items |
> | `Course` | 18 | IM course (Class C) |

and §2.2, verbatim:

> - **Illustrative Mathematics content** (`Activity`/`Assessment`/`Lesson`/etc.) is
>   provider-prefixed **`im:`**, e.g. `im:b8982b98-1078-527f-b7c7-fc974eaabf81` (16,021 nodes).

The same document lists the edges that structure that layer, §3.1, verbatim rows:

> | `hasEducationalAlignment` | 52,807 | Activity/Lesson/Assessment/LessonGrouping/Course→SFI | Curriculum→standard alignment (Class C) |
> | `hasPart` | 15,944 | Lesson→Activity/Assessment, LessonGrouping→Lesson… | Curriculum internal structure (Class C) |
> | `hasReference` | 472 | Lesson↔Lesson/Activity/Assessment | Curriculum "use_after" references (Class C) |
> | `hasDependency` | 209 | LessonGrouping→LessonGrouping | Curriculum unit dependency (Class C) |
> | `mutuallyExclusiveWith` | 192 | Assessment→Assessment | IM assessment alternatives (Class C) |

`k12-engine-map.md` §3 characterises the same layer as public but deferred, verbatim:

> - **Class C — IM / OpenSciEd HQIM curriculum structure** (strict copyright guardrail).
>   Public (CC BY) but highest effort; safe to defer.

and §4, verbatim: "**Class C:** public (CC BY) but defer; skills degrade cleanly without it."

### How the two readings reconcile, stated without resolving the documents

The precise position, which both readings partially express and neither states cleanly: what
is in the public export is the curriculum layer's **metadata** (node records with identifiers,
labels, alignment edges and structure edges). The lesson **content** is not, which is why
`k12-engine-map.md` calls it "public (CC BY) but highest effort" while `sourcing-verdict.md`
calls it absent. The v1 decision to stub both tools is unaffected. Only the stated reason on
`sourcing-verdict.md` lines 50 to 52 is wrong as written.

Note also the arithmetic relationship, which this extract states as a relationship rather
than computing a new number: `16,021` is the count of `im:`-prefixed nodes in §2.2, and the
five IM-labelled classes in §2.1 are `Activity` 8,173, `Assessment` 4,516, `Lesson` 2,550,
`LessonGrouping` 764 and `Course` 18. Both figures come from the same document, measured by
its author from the raw export. This agent did not re-parse the 292 MB `nodes.jsonl` to
re-verify either figure.

**Scope note.** `INVENTORY.md` records that a second artifact,
`Projects/HS Geometry/sources/license-lc-kg.md` §10, flagged the same contradiction
independently and measured a 16,021-record IM 360 scope-and-sequence attribution block. That
file was outside this agent's read scope and was not opened.

---

## 5 · CONTRADICTION 2 · the acceptance record

Two readings of whether the v1 grounding acceptance was ever run. Both are recorded. Neither
document is edited.

### Reading A: unrun. Source: the repo's own status documents

`README.md` lines 39 to 43, the Status checklist, verbatim:

> - [x] Fork + study the upstream engine
> - [x] Spec the standards resource
> - [x] Build the California-math vertical (store + 7-tool MCP + ingestion; 50 tests green)
> - [ ] Validate against the skills (live acceptance run — `docs/acceptance/ca-math-grounding.md`)
> - [ ] Ship

The acceptance box is unticked.

`docs/handoff/2026-07-22-overnight-build.md` line 5 to 7, verbatim:

> The v1 standards-resource replacement is **built, tested, and committed locally** (green:
> ruff + mypy strict + 50 pytest). Nothing pushed. What remains needs **you or a live
> session**: the grounding acceptance run, one legal sign-off, and the push.

line 11 to 14, the first actionable item, verbatim:

> 1. **Run the live grounding acceptance** — `docs/acceptance/ca-math-grounding.md`. This is
>    the real proof the forked skills ground against our data. It needs an interactive Claude
>    session (can't run unattended). Or hand it back to me in an interactive session and I'll
>    drive it. It tests the two open risks below.

line 78 to 79, under "Honest gaps / v1 boundaries", verbatim:

> - **Not yet proven end-to-end that the skills ground** — that is the acceptance run, the one
>   thing left that matters most.

`docs/acceptance/ca-math-grounding.md` is staged as a procedure and carries no outcome
annotation anywhere in its 83 lines. Its four pass conditions, §Step 4 lines 52 to 60,
verbatim:

> Pass = all of:
> 1. **Probe** — the skill's Step 0.3 sees the KG tools as available (it takes the grounded
>    path, not the fallback).
> 2. **Standard grounded** — the lesson's target-standard callout shows the **verbatim
>    6.RP.A.2 text and code** from our store (not a paraphrase).
> 3. **Real prerequisite** — it names **6.RP.A.1** (or the true prior standard) from the
>    progression tool — proof the CA→CCSS crosswalk bridge reached the skill.
> 4. **Footer flipped** — the teacher plan does **not** carry *"Generated without the Learning
>    Commons Knowledge Graph…"*. (Optionally shows the positive provenance stamp.)

Its closing line, line 83, verbatim: "Record the outcome and any field-name reconciliation
back into the spec §3 footer/section." No such record was written into the spec; spec §3 line
94 to 95 still says "(Exact stamp string is a v1 decision; default proposed here.)"

**The decisive timing fact for this reading.** Both documents were written at commit
`95fbde3c2a36397e72b0b8e1cef6e295f7cc5027`, `Wed Jul 22 07:57:58 2026 -0700`, subject
`docs: morning handoff + README status (v1 built; acceptance + push pending)`. `README.md`
mtime is `2026-07-22 07:57:29` and the handoff's is `2026-07-22 07:56:59`. Neither file has
been touched since. They describe the repository as it stood at 07:57 on 2026-07-22.

### Reading B: live grounding ran the same day. Source: the git history after 07:57

Two commits landed after those documents were written, and both describe live grounding runs
as having happened.

`b8fd521c46f7ff73ae3663492b9e242b205e0cc1`, `Wed Jul 22 19:38:37 2026 -0700`, message body,
verbatim excerpt:

> The tools returned placements in an unstable, non-richness
> order, so grounding landed on an empty node while a rich sibling held the data. The
> live grounding test (haiku + sonnet) confirmed this on 3 of 4 HS standards.

and, verbatim: "Removes the resolve-then-call uuid dependency that weaker models fumble
(haiku placeholder-uuid bug)."

`1ad5649dd4158c5a96a11561f678a2d877747000`, `Wed Jul 22 22:14:08 2026 -0700`, message body,
verbatim excerpt:

> Follow-up grounding re-test found academicSubject matching was case-sensitive:
> find_standard_statement(code="8.EE.A.2", academicSubject="mathematics") returned []
> while "Mathematics" resolved.

and, verbatim: "Verified against the deployed console script: lowercase and mismatched
subject now resolve."

These are in-repo artifacts. They establish that at least two live model sessions exercised
the grounding path on 2026-07-22, after the README and handoff were frozen. They do **not**
establish that the four documented pass conditions in §Step 4 were all met, because they
describe standards outside the acceptance's own example (`8.EE.A.2`, "3 of 4 HS standards")
and they report failures found, not a pass recorded. Also note the README's "50 tests green"
is stale against the same two commits, which report 65 and then 68.

### Reading C: an outside record asserts a pass. Not opened by this agent

`INVENTORY.md` cites `a private project store (not public)/memory/episodic/project/project_k12-lesson-toolkit.md`
as carrying a paragraph headed "v1 ACCEPTANCE PASSED (2026-07-22)", with the detail that CA
`6.RP.A.2` returned prerequisite `6.RP.A.1` plus three ANet learning components. That file was
outside this agent's assigned read scope and was **not opened**. Its content is reported here
only as `INVENTORY.md` describes it, and it is not evidence in this extract.

One in-repo corroboration of that specific claim exists and can be quoted:
`docs/handoff/2026-07-22-overnight-build.md` lines 72 to 73, under "What is real right now
(verified this session)", verbatim:

> - `6.RP.A.2` (California) resolves verbatim; backward `6.RP.A.1`, forward `7.RP.A.1` — the
>   CA→CCSS crosswalk bridge works end to end through the tool impls.

Read carefully, that sentence says the **tool impls** were exercised, not the skill. It is a
different claim from the acceptance, whose pass condition 1 requires the skill's own Step 0.3
probe to take the grounded path. The handoff itself draws that distinction two lines apart:
the same document asserts `6.RP.A.2` works "through the tool impls" and, at line 78, that it
is "Not yet proven end-to-end that the skills ground."

### The precise open question, for whoever writes the page

Nothing in the k12-lesson-toolkit repository records the acceptance procedure being run to its four
documented pass conditions, and nothing records an outcome where the procedure asks for one.
What the repository does record is live model sessions exercising the grounding path, finding
two defects, and both defects being fixed and committed the same day. The unticked checkbox
and the "acceptance passed" memory are not necessarily in conflict about the facts; they may
be in conflict about what counts as the acceptance.

---

## 6 · Attribution, measured per layer

This section exists because the wiki's licence discipline turns on per-record grants, and this
corpus has a rider sitting next to the grant.

### 6.1 The `license` field, measured on every record of the CA-math subset

Every record of every file carries the identical `properties.license` value:

| File | Records | Distinct `license` values |
|---|---|---|
| `standards.jsonl` | 2303 | `https://creativecommons.org/licenses/by/4.0/` on all 2303 |
| `progressions.jsonl` | 1041 | `https://creativecommons.org/licenses/by/4.0/` on all 1041 |
| `components.jsonl` | 6056 | `https://creativecommons.org/licenses/by/4.0/` on all 6056 |
| `crosswalk.jsonl` | 591 | `https://creativecommons.org/licenses/by/4.0/` on all 591 |

No record in the CA-math subset carries CC0 in its `license` field.

### 6.2 The `attributionStatement` field, measured, verbatim, in full

Five distinct strings cover the whole subset. Each is reproduced byte-exact between pipes.

`standards.jsonl`, 1467 records (the California ones):

|Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. California Mathematics standards provided by California Department of Education available at https://www.cde.ca.gov/be/st/ss/documents/ccssmathstandardaug2013.pdf.|

`standards.jsonl`, 836 records (the Multi-State ones):

|Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Common Core Mathematics standards provided by Common Good Learning Tools available at https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf.|

`components.jsonl`, all 6056 records:

|Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Learning Commons received learning components under CC BY-4.0 from Achievement Network.|

`progressions.jsonl`, all 1041 records:

|Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license. Learning Commons received learning progressions under CC0 from Student Achievement Partners.|

`crosswalk.jsonl`, all 591 records:

|Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.|

Measured `properties.author` per file: `standards.jsonl` splits `California Department of
Education` 1467 and `Common Good Learning Tools` 836; `progressions.jsonl` is
`Student Achievement Partners` on all 1041; `components.jsonl` splits
`Achievement Network` 3650 and `Achievement Network & Learning Commons` 2406;
`crosswalk.jsonl` is `Learning Commons` on all 591.

### 6.3 The rider that lives next door to the grant

On the progression records the two fields disagree in kind. The `license` field says CC BY 4.0
on all 1,041. The `attributionStatement` on the same 1,041 records says Learning Commons
received them "under CC0 from Student Achievement Partners". That is an upstream-provenance
statement sitting inside a field whose neighbour asserts the outbound grant. Both are quoted
above verbatim and neither is interpreted here.

This measurement bears on an assertion recorded in `INVENTORY.md` for the
`source-learning-commons-kg` row, which states that `NOTICE`'s CC0-for-progressions claim "is
reflected nowhere in the v1.11.0 export". Measured against the CA-math subset of that export,
the CC0 claim is reflected, in `attributionStatement`, on all 1,041 progression records. It is
not reflected in the `license` field, which is CC BY 4.0. Recorded, not resolved; the row is
another agent's and the full-export census was outside this agent's scope.

### 6.4 The repo's own NOTICE, in full, verbatim

Because it is short and every clause is load-bearing, `NOTICE` is reproduced entire:

```
k12-lesson-toolkit — NOTICE

This project adopts openly-licensed academic-standards data. Attribution per source:

Learning Commons Knowledge Graph
  https://github.com/learning-commons-org/knowledge-graph
  Public JSONL export v1.11.0. Data provided by Learning Commons under CC BY 4.0:
    - State academic standards: CC BY 4.0, via 1EdTech.
    - Learning components: CC BY 4.0, via Achievement Network (ANet).
    - Learning progressions: CC0 1.0 (public domain), via Student Achievement Partners (SAP).
  Attribution statement (as published in the data):
    "Knowledge Graph is provided by Learning Commons under the CC BY-4.0 license.
     Learning Commons received state standards and written permission under CC BY-4.0
     from 1EdTech."

California Common Core State Standards - Mathematics
  © California Department of Education. Common Core State Standards
  © 2010 National Governors Association Center for Best Practices (NGA Center) and
  Council of Chief State School Officers (CCSSO). Used under the CCSS public license.

The data under data/ca-math/ is a filtered derivative of the Learning Commons public
export, retaining each record's `license` and `attributionStatement` fields. We do not
use the gated Learning Commons API/MCP connector; only the openly-licensed export.

Supplementary sources (identified, not yet ingested):
  - commonstandardsproject/api — Apache-2.0 (code) / CC BY 3.0 US (data)
  - allenai/achieve-the-core — ODC-BY 1.0
```

Measured against the subset: the single "Attribution statement (as published in the data)"
that `NOTICE` hard-codes, the 1EdTech form, appears on **none** of the records this agent
parsed. The parse covered `standards.jsonl` (2303 records), `progressions.jsonl` (1041),
`components.jsonl` (6056) and `crosswalk.jsonl` (591), and every record's
`attributionStatement` fell into one of the five strings listed in §6.2 above. The 1EdTech string is
quoted in `docs/reference/sourcing-verdict.md` lines 77 to 79 as "Attribution string to ship
(from the data itself)", sourced from the repo's LICENSE.md read, not from these records.

### 6.5 The licence basis the repo verified, verbatim

`docs/reference/sourcing-verdict.md` §"License basis (verified in-session)", lines 67 to 79,
verbatim in full:

> - LC `LICENSE.md`: *"Knowledge Graph code is licensed under MIT"* + *"provided by Learning
>   Commons under the CC BY 4.0 license"* (state standards CC BY 4.0 via 1EdTech; learning
>   components CC BY 4.0 via Achievement Network; learning progressions CC0 via Student
>   Achievement Partners).
> - LC `README.md`: *"Local JSONL … Publicly available"*; REST API + MCP Server *"available
>   only to private beta users."*
> - Export: `cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/{nodes,relationships}.jsonl`
>   — public, no credentials (~292 MB nodes).
> - Attribution string to ship (from the data itself): *"Knowledge Graph is provided by
>   Learning Commons under the CC BY-4.0 license. Learning Commons received state standards and
>   written permission under CC BY-4.0 from 1EdTech."*

The open legal item is unresolved in the repo. `sourcing-verdict.md` lines 81 to 84, verbatim:

> ## Open legal item (before commercial ship, not before local build)
>
> Confirm the CCSS / NGA-CCSSO primary-source terms and 1EdTech republication terms are
> satisfied for a commercial product. Local development + validation are unaffected.

The gated-connector line, which the repo corrected once and which must not be re-collapsed.
`sourcing-verdict.md` §"Correction to an earlier claim", lines 24 to 30, verbatim:

> Earlier I wrote "do not touch the KG's data; rebuild from public sources." That conflated two
> things. The **gated API/connector** should not be scraped (ToS bars reverse-engineering). But
> Learning Commons **separately publishes the whole graph** as an openly-licensed data product
> (CC BY 4.0 / CC0) for reuse including commercial. Adopting that published export is exactly
> what the license grants — so we adopt their open export (near parity with what Claude for
> Teachers users get) instead of hand-aggregating CCSS-M. Better coverage, clean license.

The same correction is stamped into `k12-engine-map.md` as a block quote at lines 125 to 129,
verbatim:

> > **Correction (2026-07-22, verified).** "Do not touch the KG's data" applies to the *gated
> > API/connector* only. Learning Commons *separately publishes the entire graph* as an
> > openly-licensed export (CC BY 4.0 / CC0) intended for reuse, including commercial. We
> > therefore **adopt that published export** (with attribution) rather than rebuild Class A/B
> > from scratch. See `sourcing-verdict.md` for the verified build-vs-adopt decision.

`k12-engine-map.md` §4 still carries the superseded blanket sentence above that correction,
lines 122 to 123, verbatim: "Bottom line: **do not touch the KG's data; rebuild Class A/B from
public sources and wire them into the connector-absent seam the skills already expose.**"
The correction block immediately follows it. Anyone quoting §4 must carry both.

---

## 7 · Two facts about the upstream export a boundary page will want

Both from `docs/reference/lc-export-schema.md`, which states its own method at lines 8 to 9,
verbatim: "Every count and field name below was measured directly from the downloaded files,
not inferred."

§1, the file table, verbatim:

> | File | URL | Size | Records |
> |---|---|---|---|
> | `nodes.jsonl` | `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/nodes.jsonl` | 292,652,341 B (~279 MiB) | 247,786 nodes |
> | `relationships.jsonl` | `https://cdn.learningcommons.org/knowledge-graph/v1.11.0/exports/relationships.jsonl` | 520,406,049 B (~496 MiB) | 456,620 relationships |

and the licence sentence immediately following, lines 21 to 24, verbatim, with its
neighbouring sentences intact because the CC0 carve-out sits next door:

> License on every record: **CC BY 4.0** (`https://creativecommons.org/licenses/by/4.0/`).
> The learning-progression edges (`buildsTowards`, `relatesTo`) are additionally sourced from
> Student Achievement Partners under **CC0**. `provider` on all standards nodes = `Learning Commons`.
> Each record carries a per-source `attributionStatement`.

The local copies match those byte counts exactly: `data/raw/nodes.jsonl` is 292,652,341 B and
`data/raw/relationships.jsonl` is 520,406,049 B, measured by `stat`, both mtime 2026-07-22.

§4.2, the California coverage counts, verbatim:

> - **California math StandardsFrameworkItem = 1,467** (`jurisdiction=="California"` AND
>   `academicSubject=="Mathematics"`); 1,276 have a `statementCode`.
> - **Multi-State CCSS math StandardsFrameworkItem = 836** (`jurisdiction=="Multi-State"` AND
>   `academicSubject=="Mathematics"`); 744 have a `statementCode`. These carry the Standards for
>   Mathematical Practice (codes like `HS.MP2`, `3.MP8`) and the canonical CCSS content codes.

Measured in the store: 1,467 California rows and 836 Multi-State rows, agreeing exactly.
