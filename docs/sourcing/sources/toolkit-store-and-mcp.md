---
source_url: 
fetched: 2026-08-07
http_status: n/a (local git repository, read-only)
role: primary
covers: concept-standard-placement-vs-code, trap-code-form-silent-zero, trap-learning-components-truncated-at-five, trap-stale-stdio-mcp-server, trap-empty-facet-reads-as-success, practice-resolve-a-standard-code, practice-ground-a-lesson-end-to-end, evidence-c7-store-gap-not-corpus-gap
---

# k12-lesson-toolkit: the seven-tool contract, code forms, dedupe_richest, the component cap

## 0 · Provenance and what was actually exercised

Repository: ``.
Git HEAD at staging: `1ad5649dd4158c5a96a11561f678a2d877747000`, dated `Wed Jul 22 22:14:08 2026 -0700`.
Working tree clean except one untracked directory, `wiki/` (`git status --porcelain` returns exactly `?? wiki/`).

Date discipline: the local system clock at staging read `2026-08-07 21:17:58 PDT`. The
wiki's Stage 0.5 convention date is 2026-08-08 and `INVENTORY.md` marks these same repo
files `verified_current: yes (2026-08-08)`. The header above carries the date this agent
actually read the bytes. These are local files under version control, so the one-day
difference does not affect currency. Flagged, not resolved.

File sizes and mtimes as measured by `stat`:

| File | Bytes | mtime |
|---|---|---|
| `README.md` | 1959 | 2026-07-22 07:57:29 |
| `NOTICE` | 1467 | 2026-07-22 07:29:51 |
| `docs/reference/sourcing-verdict.md` | 4907 | 2026-07-22 07:08:27 |
| `docs/reference/k12-engine-map.md` | 8639 | 2026-07-22 07:10:21 |
| `docs/reference/lc-export-schema.md` | 18709 | 2026-07-22 07:24:51 |
| `docs/acceptance/ca-math-grounding.md` | 3877 | 2026-07-22 07:47:33 |
| `docs/handoff/2026-07-22-overnight-build.md` | 5714 | 2026-07-22 07:56:59 |
| `src/k12-lesson-toolkit/mcp/server.py` | 14017 | 2026-07-22 22:12:35 |
| `src/k12-lesson-toolkit/repository.py` | 18166 | 2026-07-22 22:12:15 |
| `src/k12-lesson-toolkit/ingest/builder.py` | 13655 | 2026-07-22 07:41:10 |
| `data/k12-lesson-toolkit.db` | 2342912 | 2026-07-22 07:41:36 |
| `.venv/bin/k12-lesson-toolkit-mcp` | 217 | 2026-07-22 07:23:57 |

Test suite run by this agent at staging: `.venv/bin/pytest -q` returned `68 passed in 1.14s`.
Note the divergence from the repo prose, which is stale. `README.md` line 41 says
"50 tests green"; `docs/handoff/2026-07-22-overnight-build.md` lines 5 to 6 carry "green:
ruff + mypy strict + 50 pytest" across the line break, and line 91 carries "50 passing"
in a code comment. Both were true at commit
`95fbde3`. Two later commits added tests, and their messages record the counts verbatim:
`b8fd521` says "ruff + mypy(strict) + pytest (65) green" and `1ad5649` says
"ruff + mypy(strict) + pytest (68) green". 68 is what runs today.

All numeric measurements below were produced in-session against `data/k12-lesson-toolkit.db`
opened read-only (`file:...?mode=ro`) and against `data/ca-math/*.jsonl`. Where a number
comes from a repo document rather than a measurement, it is labelled as such.

---

## 1 · The seven-tool contract

The contract exists because of a detection mechanism, not a handshake. `server.py` module
docstring, lines 1 to 6, verbatim:

> """The 7-tool stdio MCP server reproducing the Learning Commons Knowledge Graph contract.
>
> The forked ``k12-teacher-skills`` plugin detects the connector purely by **tool
> availability** (Step 0.3 probes whether ``find_standard_statement`` is registered), so this
> server registers all seven tool names and implements them to the depth the skills consume.

The seven names, verbatim from `tests/test_server.py` lines 17 to 26:

```python
EXPECTED_TOOLS = {
    "find_standard_statement",
    "find_standards_progression_from_standard",
    "find_misconceptions_for_standard",
    "find_learning_components_from_standard",
    "find_curriculum_lessons",
    "find_materials_for_lesson",
    "list_standards_for_mathematical_practice",
}
```

and the assertion that binds the count, `tests/test_server.py` lines 28 to 32, verbatim:

```python
def test_server_registers_exactly_seven_tools(fx: Fixture) -> None:
    server = build_server(fx.repo)
    tools = asyncio.run(server.list_tools())
    assert {t.name for t in tools} == EXPECTED_TOOLS
    assert len(tools) == 7
```

### 1.1 Per-tool depth, verbatim from the design spec

`docs/superpowers/specs/2026-07-22-standards-resource-design.md` §3, lines 62 to 70, the
table reproduced verbatim (pipe characters and emphasis as in the source):

| Tool | v1 depth | Params | Must return |
|---|---|---|---|
| `find_standard_statement` | **Full** | `code` *or* `keywords[]`; `academicSubject="Mathematics"`; `jurisdiction="California"` | `standards[]`, each `{code, statement_text (verbatim), caseIdentifierUUID, subStandards[]}`. Code search is **prefix match** (leaf → itself; parent `2.OA` → `2.OA` + all `2.OA.*`). Keyword search matches if ANY keyword appears. |
| `find_standards_progression_from_standard` | **Full** | `caseIdentifierUUID`; `direction="backward"\|"forward"` | The single primary prerequisite (`backward`) / forward (`forward`) standard, verbatim (code + text). **Math-only** by design. |
| `find_misconceptions_for_standard` | **Best-effort** | `caseIdentifierUUID`; `subject="Mathematics"` | ≥3 misconceptions, each `{student_behavior, teacher_move}`. Empty is tolerated (skill drafts 3 from training knowledge). |
| `find_learning_components_from_standard` | **Best-effort** | `caseIdentifierUUID` | up to 5 sub-skill description strings. Empty tolerated. |
| `find_curriculum_lessons` | **Registered stub** | `caseIdentifierUUID`/`ordinalName`/`lessonName`; `author` | `[]` in v1 (IM/HQIM not in the public export; skills strip IM terminology when unconfirmed). |
| `find_materials_for_lesson` | **Registered stub** | `lessonIdentifier`; `materialSource[]` | `[]` in v1. |
| `list_standards_for_mathematical_practice` | **Registered stub** | not specified in docs | May return the 8 SMPs or `[]`; the skills never consume it (SMPs come from training knowledge). No grounding impact. |

### 1.2 The response shapes are guesses, and the repo says so

`server.py` lines 17 to 23, verbatim:

> NOTE ON FIELD NAMES: the exact JSON field names of the real Learning Commons connector are
> NOT pinned by the KG docs. The names below (``statement_text``, ``caseIdentifierUUID``,
> ``subStandards``, ``student_behavior``, ``teacher_move``, ``learningComponents`` …) are
> reasonable defaults derived from the extracted contract (spec §3) and the fields the skills
> hard-require (``shared.standard_code`` ← ``code``, ``shared.standard_text`` ← statement text).
> Reconcile against the real export when it lands; change only this section.

The shared standard shape, `server.py` lines 59 to 65, verbatim:

```python
def _brief(std: Standard) -> dict[str, str]:
    """The minimal standard shape shared by several tool responses."""
    return {
        "code": std.code,
        "statement_text": std.statement_text,
        "caseIdentifierUUID": std.case_uuid,
    }
```

The two fields that carry the acceptance, spec §3 lines 85 to 89, verbatim:

> ### Downstream fields the skills hard-require
> - `shared.standard_code` ← `find_standard_statement.code`
> - `shared.standard_text` ← `find_standard_statement` verbatim statement text
>   These render the target-standard callout and each differentiation tier's eyebrow. If
>   these are wrong or missing, the authored JSON breaks. **These two are the acceptance core.**

### 1.3 Every tool is total, and that is a deliberate design constraint

`server.py` lines 9 to 10, verbatim:

> - Every tool is a **total function**: on any miss or bad input it returns an empty/typed-empty
>   result and NEVER raises. The skills forbid surfacing errors to teachers.

The mechanism, `server.py` lines 247 to 264, verbatim:

```python
def _never_raise(empty: dict[str, Any]) -> Callable[[_ToolFn], _ToolFn]:
    """Wrap a tool handler so an underlying exception returns ``empty`` instead of raising.

    The skills forbid surfacing errors to teachers, so every tool must be total.
    """

    def decorator(fn: _ToolFn) -> _ToolFn:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> dict[str, Any]:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                print(f"k12-lesson-toolkit: tool {fn.__name__} failed: {exc}", file=sys.stderr)
                return empty

        return wrapper

    return decorator
```

The decorator is applied to all seven registered tools with the per-tool empty payload, at
`server.py` lines 276, 287, 302, 315, 327, 338 and 347. The payloads are, in registration
order: `{"standards": []}`, `{"standard": None}`, `{"misconceptions": []}`,
`{"learningComponents": []}`, `{"lessons": []}`, `{"materials": []}`,
`{"standardsForMathematicalPractice": []}`.

Consequence a page-writer needs stated plainly: a caller cannot distinguish, from the
response alone, a genuine empty result from a swallowed exception. The exception text goes
to stderr only, and the caller receives the identical typed-empty dict.

The `_never_raise` wrapper appears in code but does not appear in the design spec's error
handling section (§7, lines 157 to 166), which describes the total-function rule without
naming a wrapper. It was introduced by commit `5ad87c9`, whose message calls it "F2: MCP
handlers never raise ... (makes the 'no errors to teachers' rule structural)".

---

## 2 · Code-form conventions

### 2.1 The match is exact-or-dotted-descendant, with no normalisation

`repository.py` lines 269 to 286, the sqlite implementation, verbatim:

```python
    def find_by_code(
        self,
        code: str,
        academic_subject: str | None = None,
        jurisdiction: str | None = None,
    ) -> list[Standard]:
        if not code:
            return []
        sql = "SELECT * FROM standards WHERE (code = ? OR code LIKE ? ESCAPE '\\')"
        params: list[str] = [code, _escape_like(code) + ".%"]
        if academic_subject is not None:
            sql += " AND LOWER(academic_subject) = LOWER(?)"
            params.append(academic_subject)
        if jurisdiction is not None:
            sql += " AND LOWER(jurisdiction) = LOWER(?)"
            params.append(jurisdiction)
        sql += " ORDER BY code"
        return [_row_to_standard(r) for r in self._conn.execute(sql, params)]
```

The documented semantics, `repository.py` lines 12 to 16, verbatim:

> - ``find_by_code`` is a **prefix** match on ``code``: a leaf code returns just itself; a
>   parent code (e.g. ``"2.OA"``) returns the parent AND every descendant whose code starts
>   with it. Optional ``academic_subject`` / ``jurisdiction`` filters narrow the result.

The boundary rule (a leaf code does not over-match a longer sibling) came from commit
`5ad87c9`, message verbatim: "F1: code prefix match is self-or-dotted-descendant (leaf
6.RP.A.1 no longer matches 6.RP.A.12); both engines, with LIKE-metachar escaping."

There is no code-form normalisation anywhere in the path. A caller's string is compared to
the stored string.

### 2.2 Measured probes against the live store

Run in-session against `data/k12-lesson-toolkit.db`, using the same `code = ? OR code LIKE ? || '.%'`
predicate the repository uses:

| Probe string | Rows returned | Distinct codes returned |
|---|---|---|
| `G-SRT.6` | 0 | none |
| `HSG-SRT.6` | 0 | none |
| `HSG-SRT.C.6` | 4 | `HSG-SRT.C.6` |
| `HSG-SRT` | 68 | `HSG-SRT.A`, `HSG-SRT.A.1`, `HSG-SRT.A.1.a`, `HSG-SRT.A.1.b`, `HSG-SRT.A.2`, `HSG-SRT.A.3`, `HSG-SRT.B`, `HSG-SRT.B.4`, `HSG-SRT.B.5`, `HSG-SRT.C`, `HSG-SRT.C.6`, `HSG-SRT.C.7` (first 12 of the set) |

Every SRT-family code present in the store, measured as the full distinct set:

`HSG-SRT.A`, `HSG-SRT.A.1`, `HSG-SRT.A.1.a`, `HSG-SRT.A.1.b`, `HSG-SRT.A.2`, `HSG-SRT.A.3`,
`HSG-SRT.B`, `HSG-SRT.B.4`, `HSG-SRT.B.5`, `HSG-SRT.C`, `HSG-SRT.C.6`, `HSG-SRT.C.7`,
`HSG-SRT.C.8`, `HSG-SRT.D`, `HSG-SRT.D.10`, `HSG-SRT.D.11`, `HSG-SRT.D.9`, `HSG.SRT.C.8.1`.

Note the last entry, `HSG.SRT.C.8.1`, uses a dot where the others use a hyphen. It is a
California-specific addition and it is a different string, so it is unreachable by any
`HSG-SRT` prefix probe.

The two wrong forms return zero rows and no error. There is no warning, no partial match and
no diagnostic. They are indistinguishable at the call site from a code that genuinely has no
data.

### 2.3 Why an alternate code form is never indexed

`ingest/builder.py` line 181, verbatim:

```python
        code = props.get("statementCode") or props.get("alternateStatementCode") or ""
```

`alternateStatementCode` is reached only when `statementCode` is absent or falsy. Measured
against `data/ca-math/standards.jsonl`:

- records carrying `alternateStatementCode`: **509**
- records carrying **both** `statementCode` and `alternateStatementCode`: **509**

Every record in the CA-math subset that has an alternate form also has a canonical form, so
all 509 alternate forms are discarded at ingest and none of them is queryable. Measured
example pairs, `(statementCode, alternateStatementCode)`:

`('1.NBT.A.1', '1.NBT.1')`, `('HSF-LE.A.1', 'HSF-LE.1')`, `('HSG-MG.A.1', 'HSG-MG.1')`,
`('6.NS.B.2', '6.NS.2')`, `('6.SP.A.2', '6.SP.2')`, `('HSG-C.A.2', 'HSG-C.2')`.

The upstream field definition, `docs/reference/lc-export-schema.md` §2.3, verbatim rows:

| `statementCode` (160,536) | **The standard CODE** e.g. `6.RP.A.2`, `HSA-CED.A`, `3.G.3` | Absent on ~28% (unlabeled sub-parts) |
| `alternateStatementCode` (20,033) | Secondary code form e.g. `6.SP.5b` for `6.SP.B.5b` | Optional |

Measured in the store: 283 of 2,303 standards rows have an empty `code`. The handoff records
the same number in prose (line 84, verbatim): "283 CA/CCSS standards have no code (unlabeled
sub-parts) → reachable by UUID/parent/progression, not by code search (correct — they have no
code)."

---

## 3 · dedupe_richest, and why hand-derivation is forbidden

### 3.1 The problem, in the repo's own words

`repository.py` lines 356 to 375, the full comment block, verbatim:

```
# --- richest-representative selection (query-layer dedup) --------------------
#
# A single code usually resolves to SEVERAL same-code nodes: the canonical CCSS node plus
# multiple California framework/course placements. Data is authored against SOME of those
# nodes, not replicated across all — and different facets (a prerequisite, sub-skills,
# subStandards, misconceptions) can live on DIFFERENT placements. Returning the raw set
# surfaces an empty placement first (and unstably, since same-code ties are unordered).
#
# So we collapse to one representative per code for grounding, but resolve each FACET to the
# sibling that actually holds it:
#   * dedupe_richest / _grounding_score — pick the representative + rank keyword hits, on the
#     progression+component score (what a lesson grounds on).
#   * select_by_code — resolve a bare `code` to the sibling best for ONE facet (a directional
#     edge, a component count, a misconception count), so a code lookup never misses data that
#     sits on a different placement than the "overall richest" one.
# subStandards are unioned across all same-code placements by the server (children, too, can
# live on a sibling). See spec §4, §6.
#
# `cache` memoizes a node's grounding score across the several sort passes of one request.
```

### 3.2 The scoring function

`repository.py` lines 377 to 394, verbatim:

```python
FacetScore = Callable[["StandardsRepository", Standard], int]


def _grounding_score(
    repo: StandardsRepository, std: Standard, cache: dict[str, int] | None = None
) -> int:
    """Progression + component data a node carries — the grounding-representative rank."""
    if cache is not None and std.case_uuid in cache:
        return cache[std.case_uuid]
    score = 0
    if repo.progression(std.case_uuid, BACKWARD) is not None:
        score += 1
    if repo.progression(std.case_uuid, FORWARD) is not None:
        score += 1
    score += len(repo.learning_components(std.case_uuid))
    if cache is not None:
        cache[std.case_uuid] = score
    return score
```

### 3.3 dedupe_richest itself

`repository.py` lines 397 to 434, verbatim:

```python
def dedupe_richest(
    repo: StandardsRepository,
    standards: Sequence[Standard],
    *,
    prefer_jurisdiction: str = "California",
    order_by_richness: bool = False,
    cache: dict[str, int] | None = None,
) -> list[Standard]:
    """Collapse same-code duplicates to the single richest node per code.

    By default preserves the first-seen order of distinct codes (callers pass code-sorted
    input, so the result stays code-sorted). With ``order_by_richness`` the survivors are
    re-sorted richest-first (used for keyword hits, where the best grounding target should
    lead). Ties break deterministically: more grounding data wins, then ``prefer_jurisdiction``,
    then the lexicographically smallest ``case_uuid`` — so the choice is stable across calls.
    Single-member groups skip scoring; ``cache`` avoids re-scoring a node across sort passes.
    """
    if cache is None:
        cache = {}
    groups: dict[str, list[Standard]] = {}
    for std in standards:
        groups.setdefault(std.code, []).append(std)
    out: list[Standard] = []
    for members in groups.values():
        if len(members) == 1:  # no tie to break — skip the scoring queries entirely
            out.append(members[0])
            continue
        members.sort(
            key=lambda s: (
                -_grounding_score(repo, s, cache),
                0 if s.jurisdiction == prefer_jurisdiction else 1,
                s.case_uuid,
            )
        )
        out.append(members[0])
    if order_by_richness:
        out.sort(key=lambda s: (-_grounding_score(repo, s, cache), s.code))
    return out
```

The tie-break order is therefore, in exact precedence: highest `_grounding_score`, then
`jurisdiction == "California"` ahead of anything else, then the lexicographically smallest
`case_uuid`.

### 3.4 select_by_code, the per-facet resolver

`repository.py` lines 437 to 474, verbatim:

```python
def select_by_code(
    repo: StandardsRepository,
    code: str,
    facet_score: FacetScore,
    *,
    prefer_jurisdiction: str = "California",
) -> Standard | None:
    """Among exact same-code nodes, return the one that best serves a single facet.

    ``facet_score`` ranks nodes for a specific datum ("has a backward edge", "component count",
    "misconception count"); ties fall back to overall grounding richness, then
    ``prefer_jurisdiction``, then the smallest uuid. This lets a bare-``code`` lookup reach the
    sibling that holds the requested datum even when a DIFFERENT sibling is richer overall.
    """
    if not code:
        return None
    exact = [s for s in repo.find_by_code(code) if s.code == code]
    if not exact:
        return None
    exact.sort(
        key=lambda s: (
            -facet_score(repo, s),
            -_grounding_score(repo, s),
            0 if s.jurisdiction == prefer_jurisdiction else 1,
            s.case_uuid,
        )
    )
    return exact[0]


def richest_by_code(
    repo: StandardsRepository,
    code: str,
    *,
    prefer_jurisdiction: str = "California",
) -> Standard | None:
    """Resolve a single code to its overall-richest node (grounding score, facet-agnostic)."""
    return select_by_code(repo, code, _grounding_score, prefer_jurisdiction=prefer_jurisdiction)
```

`select_by_code` is invoked from the server through `_resolve_uuid`, `server.py` lines 68 to
84, verbatim:

```python
def _resolve_uuid(
    repo: StandardsRepository, uuid: str, code: str | None, facet_score: FacetScore
) -> str:
    """A caller may pass a ``caseIdentifierUUID`` OR a bare ``code``.

    A non-empty uuid wins (the real connector's contract); otherwise a ``code`` resolves to the
    same-code node richest in THIS tool's facet (:func:`select_by_code`), so a caller that never
    threads a uuid still reaches the datum even when it lives on a non-representative placement.
    This removes the two-step resolve-then-call dependency that weaker models fumble.
    """
    if uuid:
        return uuid
    if code:
        rep = select_by_code(repo, code, facet_score)
        if rep is not None:
            return rep.case_uuid
    return ""
```

The three facet scorers passed in are, verbatim from the call sites:

- progression, `server.py` line 166: `lambda r, s: 1 if r.progression(s.case_uuid, direction) is not None else 0`
- misconceptions, `server.py` line 186: `lambda r, s: len(r.misconceptions(s.case_uuid))`
- learning components, `server.py` line 209: `lambda r, s: len(r.learning_components(s.case_uuid))`

### 3.5 subStandards are unioned, not taken from the representative

`server.py` lines 87 to 103, verbatim:

```python
def _sub_standards(
    repo: StandardsRepository,
    std: Standard,
    academic_subject: str | None,
    jurisdiction: str | None,
    cache: dict[str, int],
) -> list[dict[str, str]]:
    """Union the children across ALL same-code placements (a placement's children can differ),
    deduped to one per child code, so subStandards never drops a sub-part held by a sibling.
    """
    same_code = [
        n for n in repo.find_by_code(std.code, academic_subject, jurisdiction) if n.code == std.code
    ]
    children: list[Standard] = []
    for node in same_code:
        children.extend(repo.children_of(node.case_uuid))
    return [_brief(child) for child in dedupe_richest(repo, children, cache=cache)]
```

The reason, from commit `b8fd521`, verbatim: "subStandards now union children across all
same-code placements (a childless placement could win the representative and drop the
subtree; e.g. code 4.0 to [])."

### 3.6 Measured: the multiplicity is the normal case, not an edge case

Against `data/k12-lesson-toolkit.db`:

- distinct non-empty codes in `standards`: **794**
- codes resolving to more than one placement: **693**
- maximum placements for a single code: **7**

Per-placement learning-component counts for the five HSG-SRT unit codes, each ordered by
`case_uuid`, measured:

| Code | Placements | Component count per placement, with jurisdiction |
|---|---|---|
| `HSG-SRT.B.4` | 4 | California 0, California 0, California 7, Multi-State 7 |
| `HSG-SRT.B.5` | 4 | California 6, California 0, Multi-State 6, California 6 |
| `HSG-SRT.C.6` | 4 | Multi-State 3, California 3, California 0, California 3 |
| `HSG-SRT.C.7` | 4 | Multi-State 1, California 0, California 1, California 0 |
| `HSG-SRT.C.8` | 4 | California 8, California 0, Multi-State 8, California 8 |

Every one of these five codes has at least one placement carrying zero components. Picking a
placement by hand, or taking whichever row a raw query returns first, lands on a zero
placement for all five codes with non-trivial probability, and the raw ordering is not stable.

### 3.7 The measured motivation, from the commit that introduced it

Commit `b8fd521c46f7ff73ae3663492b9e242b205e0cc1`, `Wed Jul 22 19:38:37 2026 -0700`, message
body verbatim (the parts bearing on this section):

> A single standard code resolves to several same-code framework placements; data
> (prerequisite, next, sub-skills, subStandards, misconceptions) is authored against
> some placements, not all. The tools returned placements in an unstable, non-richness
> order, so grounding landed on an empty node while a rich sibling held the data. The
> live grounding test (haiku + sonnet) confirmed this on 3 of 4 HS standards.
>
> Query-layer fixes (no store rebuild, fully reversible):
> - D1 find_standard_statement collapses same-code duplicates to the single richest
>   node per code, deterministic (prefer California, then smallest uuid). Store-wide
>   "grounds thin despite data" drops 208 codes (115 HS) to 0.
> - D2 keyword search drops blank-code container nodes, leads with the richest leaf,
>   returns the top MAX_KEYWORD_RESULTS matches.
> - D3 progression / misconceptions / learning-components accept a bare code in place
>   of caseIdentifierUUID, resolved PER FACET (select_by_code) so a code lookup reaches
>   the sibling that actually holds a directional edge, the components, or the
>   misconception. Removes the resolve-then-call uuid dependency that weaker models
>   fumble (haiku placeholder-uuid bug). A real uuid still wins; the upstream skill
>   path is unchanged.

The "208 codes (115 HS) to 0" figure is the commit author's claim in the commit message. This
agent did not independently reproduce it.

The same commit records the review posture, verbatim: "Adversarial review (14 agents) found 6
defects in the first cut; all fixed here. ruff + mypy(strict) + pytest (65) green."

---

## 4 · MAX_LEARNING_COMPONENTS

### 4.1 Declaration

`server.py` lines 47 to 51, verbatim:

```python
# Contract caps (spec §3).
MAX_LEARNING_COMPONENTS = 5
# A keyword/topic search returns the richest matches, not the full corpus — grounding needs the
# best leaf, not hundreds. This also bounds the per-result subStandards union work.
MAX_KEYWORD_RESULTS = 25
```

`MAX_LEARNING_COMPONENTS = 5` is on line 48. `MAX_KEYWORD_RESULTS = 25` is on line 51.

### 4.2 Application

`server.py` lines 198 to 214, the whole handler, verbatim:

```python
def find_learning_components_from_standard_impl(
    repo: StandardsRepository,
    caseIdentifierUUID: str = "",
    code: str | None = None,
) -> dict[str, Any]:
    """Up to 5 sub-skill description strings, ordered by ordinal. Empty tolerated.

    Accepts a ``code`` in place of ``caseIdentifierUUID``; the code resolves to the same-code
    node richest in components.
    """
    uuid = _resolve_uuid(
        repo, caseIdentifierUUID, code, lambda r, s: len(r.learning_components(s.case_uuid))
    )
    if not uuid:
        return {"learningComponents": []}
    components = repo.learning_components(uuid)[:MAX_LEARNING_COMPONENTS]
    return {"learningComponents": [c.description for c in components]}
```

The slice is on line 213. The return is on line 214.

The response is a bare list of description strings. It carries no count, no total, no
`truncated` flag, and no indication that a slice occurred. A caller receiving five strings
cannot tell whether the standard has exactly five components or forty-one.

### 4.3 The untruncated query the store still offers

`repository.py` lines 340 to 353, verbatim:

```python
    def learning_components(self, uuid: str) -> list[LearningComponent]:
        cur = self._conn.execute(
            "SELECT * FROM learning_components WHERE case_uuid = ? ORDER BY ordinal",
            (uuid,),
        )
        return [
            LearningComponent(
                case_uuid=r["case_uuid"],
                ordinal=r["ordinal"],
                description=r["description"],
                source=r["source"],
            )
            for r in cur
        ]
```

The cap lives entirely in the MCP layer. The repository returns everything, ordered by
`ordinal`. Any count of a standard's components must come from the store, never from the tool
response.

### 4.4 Measured: how often the cap actually bites

Against `data/k12-lesson-toolkit.db`, at the `case_uuid` (placement) grain:

- placements carrying at least one learning component: **1,115**
- placements carrying **more than five** learning components: **183**
- maximum components on a single placement: **41**

For the five HSG-SRT unit codes, the richest placement per code carries: `HSG-SRT.B.4` 7,
`HSG-SRT.B.5` 6, `HSG-SRT.C.6` 3, `HSG-SRT.C.7` 1, `HSG-SRT.C.8` 8 (see §3.6 for the full
per-placement breakdown). Three of these five exceed the cap and are silently truncated to
five by the tool. `HSG-SRT.C.6` and `HSG-SRT.C.7` are not truncated.

Two project documents disagree with these measurements. `INVENTORY.md` records that
`CHEATSHEET.md` in the HS Geometry project says B.4 has 14 components and C.8 has 24, while
the HS Geometry design spec §7 trap 23 says B.4 has 7 and C.8 has 8. This agent's measurement
against the store gives B.4 = 7 and C.8 = 8 on the richest placement, agreeing with the design
spec. This agent did not open either HS Geometry document; the disagreement is recorded here
only because the store-side number is now measured and can settle it.

---

## 5 · The case-sensitivity fix

Commit `1ad5649dd4158c5a96a11561f678a2d877747000`, `Wed Jul 22 22:14:08 2026 -0700`,
subject `fix(mcp): case-insensitive academicSubject/jurisdiction + code-only fallback`.
This is the repository HEAD. Message body verbatim:

> Follow-up grounding re-test found academicSubject matching was case-sensitive:
> find_standard_statement(code="8.EE.A.2", academicSubject="mathematics") returned []
> while "Mathematics" resolved. A caller that varies casing (the placeholder-uuid
> flake's successor failure mode) got a total-empty resolve with no retry.
>
> - find_by_code / search_by_keywords match academic_subject + jurisdiction
>   case-insensitively (LOWER() in sqlite, .lower() in memory).
> - find_standard_statement falls back to a code-only resolve when a subject/
>   jurisdiction filter empties an otherwise-valid code, so a filter mismatch never
>   silently returns nothing.
>
> The real installed skill passes "Mathematics" so the shipped path was not exposed,
> but the tool is now robust to casing. Verified against the deployed console script:
> lowercase and mismatched subject now resolve. ruff + mypy(strict) + pytest (68) green.

Files touched, from `git show --stat`: `src/k12-lesson-toolkit/mcp/server.py` (9 lines changed),
`src/k12-lesson-toolkit/repository.py` (16), `tests/test_dedup.py` (30 added). Total 44 insertions,
11 deletions.

The server-side change, diff verbatim:

```diff
     cache: dict[str, int] = {}
     if code:
-        standards = dedupe_richest(
-            repo, repo.find_by_code(code, academicSubject, jurisdiction), cache=cache
-        )
+        found = repo.find_by_code(code, academicSubject, jurisdiction)
+        if not found and (academicSubject or jurisdiction):
+            # A subject/jurisdiction filter emptied an otherwise-valid code (e.g. a casing or
+            # vocabulary mismatch): resolve on the code alone rather than silently return empty.
+            found = repo.find_by_code(code)
+        standards = dedupe_richest(repo, found, cache=cache)
```

The repository-side change, diff verbatim (both engines, both methods):

```diff
             if (s.code == code or s.code.startswith(code + "."))
-            and (academic_subject is None or s.academic_subject == academic_subject)
-            and (jurisdiction is None or s.jurisdiction == jurisdiction)
+            and (academic_subject is None or s.academic_subject.lower() == academic_subject.lower())
+            and (jurisdiction is None or s.jurisdiction.lower() == jurisdiction.lower())
```

```diff
         if academic_subject is not None:
-            sql += " AND academic_subject = ?"
+            sql += " AND LOWER(academic_subject) = LOWER(?)"
             params.append(academic_subject)
         if jurisdiction is not None:
-            sql += " AND jurisdiction = ?"
+            sql += " AND LOWER(jurisdiction) = LOWER(?)"
             params.append(jurisdiction)
```

Two things this fix does NOT do, and they matter:

1. It makes the **filter values** case-insensitive. It does not touch the `code` comparison,
   which remains byte-exact. A miscased or misformed code still returns zero rows.
2. The code-only fallback fires only when the filtered result is empty AND at least one filter
   was supplied. A code that is simply wrong returns empty from both attempts.

---

## 6 · The stale stdio server

### 6.1 What is on disk

`.venv/bin/k12-lesson-toolkit-mcp`, 217 bytes, mtime `2026-07-22 07:23:57`, mode `-rwxr-xr-x`.
Full contents, verbatim:

```python
#!.venv/bin/python
import sys
from k12-lesson-toolkit.mcp.server import main
if __name__ == '__main__':
    sys.argv[0] = sys.argv[0].removesuffix('.exe')
    sys.exit(main())
```

It is declared in `pyproject.toml`, verbatim:

```toml
[project.scripts]
k12-lesson-toolkit-mcp = "k12-lesson-toolkit.mcp.server:main"
```

### 6.2 The install is editable, a bare path append

`.venv/lib/python3.12/site-packages/_editable_impl_k12-lesson-toolkit.pth`, 50 bytes, mtime
`2026-07-22 07:23:57`. Its entire content, confirmed byte by byte with `od -c`, is one line:

```
src
```

There is no import hook and no compiled copy: the console script imports directly from the
working tree at `src/`. The measured consequence is precise and easy to state wrong, so state
it exactly:

- A **new** spawn of `.venv/bin/k12-lesson-toolkit-mcp` picks up whatever is in `src/` at that moment.
- An **already-running** process does not. Python binds the module at import time; nothing in
  this server reloads it.

### 6.3 What the server does at startup

`server.py` lines 355 to 370, verbatim:

```python
def _repo_from_env() -> StandardsRepository:
    """Build the default store from ``OVEREDUCATED_DB`` (a sqlite path)."""
    db_path = os.environ.get("OVEREDUCATED_DB", DEFAULT_DB_PATH)
    repo = SqliteStandardsRepository(db_path)
    repo.create_schema()  # tolerate an as-yet-unpopulated DB; ingestion is a separate task.
    return repo


def main() -> None:
    """Entry point: run the stdio MCP server over the env-configured store."""
    server = build_server(_repo_from_env())
    server.run()  # defaults to stdio transport
```

`DEFAULT_DB_PATH = "k12-lesson-toolkit.db"` is `server.py` line 45.

Two startup facts a verifier needs. First, the sqlite connection is opened once, in
`SqliteStandardsRepository.__init__` (`repository.py` lines 230 to 233), and held for the life
of the process. Second, `create_schema()` runs unconditionally at startup, so a server pointed
at a missing or empty database file starts successfully and every tool then returns its
typed-empty payload. A silent empty result can therefore also mean "wrong `OVEREDUCATED_DB`".

The registration the acceptance procedure specifies, `docs/acceptance/ca-math-grounding.md`
lines 26 to 35, verbatim:

```json
{
  "mcpServers": {
    "learning-commons-knowledge-graph": {
      "command": ".venv/bin/k12-lesson-toolkit-mcp",
      "env": { "OVEREDUCATED_DB": "data/k12-lesson-toolkit.db" }
    }
  }
}
```

### 6.4 The honest limit of what this repo proves

The rule "verify any MCP change against the venv binary, never a `src` import" is recorded in
the HS Geometry project's `CHEATSHEET.md` and its design spec trap 11, per `INVENTORY.md`
rows 924 to 927. This agent's read scope was the k12-lesson-toolkit repo only and did not open
those files.

What the k12-lesson-toolkit repo itself supports, measured and quoted above: the console script
exists at the path the acceptance procedure registers; the install is a bare `src` path
append; the process holds one module import and one sqlite connection for its lifetime; and
the tests exercise `build_server(...)` and the `*_impl` functions by direct import, never the
spawned binary (`tests/test_server.py` line 12: `from k12-lesson-toolkit.mcp.server import build_server`).
So the in-repo test suite, all 68 tests, proves nothing about the running server. That is the
gap the rule exists to close.

One in-repo corroboration exists for the practice: commit `1ad5649` states, verbatim,
"Verified against the deployed console script: lowercase and mismatched subject now resolve."
That is the author asserting the verification was run against the binary, not the tests
demonstrating it.

---

## 7 · Sundry exact facts a page-writer may need

- The keyword search is an OR match. `repository.py` lines 16 to 17, verbatim: "``search_by_keywords`` is an **OR** match: a standard matches if ANY keyword appears (case-insensitively) in its ``statement_text``."
- Keyword hits are capped at 25 (`MAX_KEYWORD_RESULTS`, `server.py` line 51) and blank-code container nodes are dropped before dedupe (`server.py` lines 129 to 136).
- `find_standards_progression_from_standard` validates direction against `_VALID_DIRECTIONS = frozenset({BACKWARD, FORWARD})` (`server.py` line 52) and returns `{"standard": None}` for anything else (`server.py` lines 160 to 161). `BACKWARD = "backward"` and `FORWARD = "forward"` are `model.py` lines 16 and 17, commented `# prerequisite` and `# next standard`.
- `progression()` returns a single target, `ORDER BY to_uuid LIMIT 1` (`repository.py` lines 316 to 320), made deterministic by commit `5ad87c9` ("L1: progression() deterministic (ORDER BY to_uuid)").
- LIKE metacharacters are escaped before use: `_escape_like` replaces `\`, `%` and `_` (`repository.py` lines 203 to 205).
- The `Standard` entity fields, `model.py` lines 28 to 36: `case_uuid`, `code`, `statement_text`, `academic_subject`, `jurisdiction`, `grade`, `parent_uuid`, `source`, `source_license`.
- The `case_uuid` is the Learning Commons **node identifier**, not the CASE id. `lc-export-schema.md` §2.2, verbatim: "Note there are **two UUIDs per standard**: `identifier` (the graph node id, the join spine) and `properties.caseIdentifierUUID` (the external IMS/CASE id). **They never coincide** (0 / 222,865 equal)." The MCP nonetheless returns the node `identifier` in the field it names `caseIdentifierUUID` (`server.py` line 64), a deliberate decision recorded in spec §4 line 101 to 102, verbatim: "``case_uuid`` adopts the Learning Commons node ``identifier`` (stable graph ids), so it satisfies the skills' ``caseIdentifierUUID`` contract directly — no minting."
