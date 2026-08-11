---
source_url: k12-teacher-skills/plugin/skills/k12-lesson-planning/references/learning-commons-kg.md and .../scripts/ (byte-identical to the installed 0.6.0 plugin)
fetched: 2026-08-08
http_status: n/a
role: primary
covers: k12-render-invocation, k12-shared-registry, practice-ground-a-lesson-end-to-end, practice-resolve-a-standard-code, k12-document-set
---

# Standards grounding, empty facets, and the render invocation

Read at 2026-08-07 21:15 PDT, which is 2026-08-08 04:15 UTC. Local files, no HTTP status.
Every quotation is byte-exact from the file and line named beside it. Line numbers are from
the fork checkout, byte-identical to the installed plugin at
`~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/` (verified by
`diff -r -q --exclude=__pycache__`, exit 0).

---

## 1 · When the grounding step runs at all

`k12-lesson-planning/SKILL.md` Step 0.3, lines 75 to 78, verbatim:

> 3. **Connector.** Check whether the Learning Commons Knowledge Graph tools (e.g.
>    `find_standard_statement`) are available in this conversation. This decides which path
>    Step 2 takes. The skill is fully functional without the connector.

`k12-lesson-planning/SKILL.md` Step 2, lines 94 to 105, verbatim, whole section:

> ## Step 2 — Ground in standards
>
> **If the LC Knowledge Graph is connected:** follow the subject's section in
> `references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
> critical failure. Extract only what each call specifies, then proceed directly to Step 3 — do
> not summarize findings in chat.
>
> **If not connected:** draft from best knowledge and add this footer to the lesson plan:
> *"Generated without the Learning Commons Knowledge Graph. Standards and misconceptions reflect
> general best practice."* Do not invent KG citations or attribute content to curriculum
> materials you have not seen.

The differentiation skill's Step 2, `k12-lesson-differentiation/SKILL.md` lines 131 to 140,
verbatim, whole section, with a stricter clause about how the lesson arrived:

> ## Step 2 — Ground in standards
>
> **If the LC Knowledge Graph is connected:** follow the subject's section in
> `references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
> critical failure. This applies no matter how the source lesson was obtained — uploaded, pasted,
> or fetched from a URL. Retrieving the lesson never satisfies this step.
>
> **If not connected:** proceed from best knowledge and add this footer to the teacher plan:
> *"Generated without the Learning Commons KG. Standard text, prerequisite grounding, and
> misconceptions reflect general best practice."* Do not invent KG citations.

Note that the two disclaimer footers are DIFFERENT strings, and both are meant to be printed
verbatim. Planning uses "the Learning Commons Knowledge Graph"; differentiation uses "the
Learning Commons KG". A third variant exists for science, given in §2.4 below.

`references/learning-commons-kg.md` lines 9 to 12, verbatim, the file's own scope statement:

> Used by `k12-lesson-planning` Step 2 **only when the LC Knowledge Graph tools are available**.
> If they are not, skip this file entirely (SKILL.md Step 2 has the fallback).
> Each section below is the call sequence for one subject. Calling the KG when connected is
> mandatory; not calling it is a critical failure.

---

## 2 · The call sequences

### 2.1 Resolving the standard, all subjects, and THE 3-ATTEMPT CAP

`k12-lesson-planning/references/learning-commons-kg.md` lines 14 to 31, verbatim, whole
section:

> ## Resolving the standard (all subjects)
>
> Resolve the standard with `find_standard_statement`, passing `academicSubject` and `jurisdiction` (the U.S. state) when they're known:
>
> - **A code is provided** (named in the source lesson or by the teacher): search by code — `find_standard_statement(code=<code>, academicSubject="<subject>")`. A code search matches both the code itself and everything beneath it (prefix match): a leaf like `3.NF.A.1` returns just that standard, while a parent like `2.OA` returns `2.OA` plus all `2.OA.*`. **If it returns nothing**, the code's format probably doesn't match the graph's — fall back to keyword search (below); its results come back with real `code` values that reveal the correct format, which you can use to retry the code search.
> - **No code provided**: start with keyword search — `find_standard_statement(keywords=["<word or phrase>", "<word or phrase>", …], academicSubject="<subject>")`. `keywords` is a **list** of topic words/phrases; a standard matches if ANY of them appears in its description. Pick the best-matching standard from the returned `standards` array — its `code` can seed a follow-up code search for related standards (e.g. its parent prefix to pull the whole family).
>
> When a returned standard has children, they come back in its `subStandards` array — use whichever is most relevant to the user's request, the standard itself or one of its sub-standards.
>
> **Cap at 3 search attempts total.** Results from the wrong grade band or course count as
> a miss — a high-school US History request answered with elementary codes means the search
> terms missed, so spend the remaining attempts with different keywords (the course name,
> the era, the standard family) rather than falling back early. If no usable standard after
> 3 calls to `find_standard_statement`, stop searching — proceed with the best-matching
> standard from training knowledge for the grade and topic, and add the partial-coverage
> footer to the lesson plan. Never call `find_curriculum_lessons` to locate a standard.
>
> From the chosen standard, extract: the verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls). When the statement has lettered sub-parts, the verbatim quote is the sub-part(s) this lesson targets, with the parent named by code.

**The cap exists in exactly one place in the plugin.** Measured, with the command and its
full output:

```
$ grep -rn "Cap at 3\|3 search attempts\|3 calls to" \
    k12-teacher-skills/plugin/skills/
k12-lesson-planning/references/learning-commons-kg.md:23:**Cap at 3 search attempts total.** Results from the wrong grade band or course count as
k12-lesson-planning/references/learning-commons-kg.md:27:3 calls to `find_standard_statement`, stop searching — proceed with the best-matching
```

Two hits, both in the PLANNING skill's KG reference. **The differentiation skill's
`references/learning-commons-kg.md` has no cap at all.** Its "Resolving the standard (all
subjects)" section (lines 14 to 23 of that file) is otherwise word-for-word identical to the
planning one through the `subStandards` paragraph, and then simply stops. Its closing line,
line 23, verbatim, is:

> From the chosen standard, extract: the verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls).

It has no "Cap at 3 search attempts total" paragraph, no wrong-grade-band-counts-as-a-miss
rule, no "Never call `find_curriculum_lessons` to locate a standard" prohibition, and no
lettered-sub-parts sentence. Two skills, one shared renderer, and only one of them bounds the
search.

The "partial-coverage footer" the cap paragraph refers to is named but never given as a
string anywhere in `learning-commons-kg.md`. The only footer strings the plugin supplies
verbatim are the three not-connected disclaimers quoted in §1 and §2.4.

### 2.2 Mathematics, the fullest sequence

`k12-lesson-planning/references/learning-commons-kg.md` lines 35 to 39, verbatim:

> Call BEFORE drafting. Not calling when connected is a critical failure. Make all calls, extract only what is specified below, then proceed directly to Step 3 — KG findings surface in chat only through the draft's one-line standard read-back, never as a results summary.
>
> The only cross-call data dependencies are the standard's `caseIdentifierUUID` (used by steps 2–5) and the `lessonIdentifier` that `find_curriculum_lessons` returns (used by `find_materials_for_lesson`). So: resolve the standard, then issue the step 2–4 calls and `find_curriculum_lessons` — each with its full parameters as specified below — as one parallel batch, then fetch materials.
>
> **Available tools:** `find_standard_statement`, `find_standards_progression_from_standard`, `find_misconceptions_for_standard`, `find_learning_components_from_standard`, `list_standards_for_mathematical_practice`, `find_curriculum_lessons`, `find_materials_for_lesson`.

The six numbered steps, lines 41 to 51, verbatim:

> 1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Mathematics"`. Use the verbatim statement text exactly as written in the lesson plan's standard callout.
>
> 2. **Prerequisite**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract: the single primary prerequisite standard, verbatim. Use in the LEARNING GOAL section. Non-negotiable — not naming the prior standard is a critical failure.
>
> 3. **Learning components**: Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill descriptions (unknown positions, problem types). Use directly as SWBAT bullets and as look-for row labels in the observation template. Discard the rest.
>
> 4. **Misconceptions**: Call `find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` → extract: the 3 most relevant misconceptions. For each keep only the student behavior and the teacher move, rewritten in your own words. If no results, draft 3 from training knowledge.
>
> 5. **Lesson materials**: Call `find_curriculum_lessons(caseIdentifierUUID=<uuid from step 1>, author="Illustrative Mathematics")` → select the single most relevant lesson (grade-level match first). Call `find_materials_for_lesson(lessonIdentifier, materialSource=["lesson", "activity"])` for the lesson overview and activity materials in one call → extract: (a) activity names and sequence, (b) problem types and unknown positions addressed, (c) any explicit discourse moves. Discard full activity narratives and student-facing text — these must not be reproduced verbatim.
>
> 6. **SMPs**: Choose 2–3 from training knowledge. No KG call needed.

The exact numbers to preserve: "up to 5 sub-skill descriptions" in step 3, "the 3 most
relevant misconceptions" in step 4, "draft 3 from training knowledge" as its no-result
fallback, "2–3" SMPs in step 6.

The terminology sweep, lines 53, verbatim:

> **Curriculum-terminology check (if not IM-confirmed):** Before proceeding, scan your working notes and verify they contain zero mentions of "Illustrative Mathematics," "IM," any MLR name (MLR 1–8), "Compare and Connect," "Stronger and Clearer Each Time," or any IM lesson/activity title. Remove any that remain — a teacher who has not confirmed IM must not receive IM-specific terminology in the lesson or in chat (the same rule as SKILL.md's Copyright guardrail).

### 2.3 ELA, two calls

Lines 65 to 71, verbatim:

> **Available tools:** `find_standard_statement`, `find_learning_components_from_standard`
>
> 1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="English Language Arts"` (codes look like RL.4.3, RI.6.6, RF.1.2b, W.8.1, L.5.4). Use the verbatim statement text exactly as written in Section 1.
>
> 2. **Learning components**: Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill descriptions if available. Use directly as SWBAT bullets in Section 2. Discard the rest.
>
> 3. **Text complexity check**: If an anchor text is identified (from teacher or KG), note whether its Lexile falls in the correct CCSS grade-band range. Flag if outside band.

Step 3 is not a KG call. The `academicSubject` string for ELA is the literal
`"English Language Arts"`, not `"ELA"`.

### 2.4 Science: two tools are documented as RETURNING NOTHING

Lines 83 to 89, verbatim:

> **Available tools:** `find_standard_statement`, `find_curriculum_lessons`, `find_materials_for_lesson`.
>
> Note: `find_learning_components_from_standard` and `find_standards_progression_from_standard` do **not** return data for science standards — do not call them.
>
> 1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Science"` (the code is an NGSS Performance Expectation, e.g. `MS-LS2-3`, `3-LS1-1`, `HS-PS1-1`). Use the verbatim statement text exactly as written in Section 1.
>
> 2. **OpenSciEd unit and lesson**: Call `find_curriculum_lessons(caseIdentifierUUID=<uuid from step 1>, author="OpenSciEd")` → select the single most relevant lesson (grade-level match first, then closest topic match). Call `find_materials_for_lesson(lessonIdentifier, materialSource=["activity"])` → extract: (a) unit anchoring phenomenon; (b) unit driving question; (c) this lesson's investigative phenomenon or question; (d) this lesson's position in the unit storyline; (e) which SEP(s) and CCC(s) are foregrounded; (f) any specific routines or activity structures used. **Do NOT reproduce OSE student-facing text, investigation prompts, or discussion questions verbatim — these must be rewritten as original content.**

This is a documented empty-result contract, not a failure mode: two of the seven Learning
Commons tools are stated to return nothing for science standards, so the skill forbids
calling them rather than handling the empty result.

Science's disclaimer footer is a THIRD string. Line 91, verbatim:

> **If KG not connected:** draft from best knowledge; add footer: *"Generated without the Learning Commons Knowledge Graph. Standards and OpenSciEd alignment reflect general best practice."*

Math and ELA both use the "Standards and misconceptions" wording (lines 55 and 73).

### 2.5 Social studies: one call, and the jurisdiction is mandatory

Lines 100 to 104, verbatim, the whole section body:

> Use the KG to find the authoritative standard statement for this topic and grade band. This grounds the lesson in the actual standard rather than a paraphrase.
>
> 1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Social Studies"` and `jurisdiction="<state>"` (required — Social Studies standards live only under the state, never `Multi-State`). Use the verbatim statement text in the lesson plan header under `**Standard:**`, and let it anchor the compelling question and formative task.
>
> **If no standard is found:** align the lesson to the most relevant state specific standard from training knowledge, and note briefly: *"Standard lookup not available for [state/code]."* Do not halt generation.

The literal fallback note carries an unfilled placeholder, `[state/code]`, in the source.

Each of the four sections ends with the same line, verbatim:
`→ **KG phase complete. Proceed immediately to Step 3.**` (lines 57, 75, 93, 106).

### 2.6 The differentiation skill's math sequence, for contrast

`k12-lesson-differentiation/references/learning-commons-kg.md` lines 28 to 34, verbatim:

> **Call all three before drafting. Not calling when connected is a critical failure.**
>
> Note any standard code the source lesson names — the resolution step searches by it when present.
>
> After the standard resolves, the progression calls (both directions), misconceptions, and learning components all depend only on its `caseIdentifierUUID` — issue those four as one parallel batch, each with its full parameters as specified below. Step 5 runs on its own terms (its own lookup modes and teacher confirmation), untouched by the batch.
>
> **Available tools:** `find_standard_statement`, `find_standards_progression_from_standard`, `find_misconceptions_for_standard`, `find_learning_components_from_standard`, `find_curriculum_lessons`, `find_materials_for_lesson`.

Its step 2 requires BOTH progression directions, line 43, verbatim:

> 2. **Prerequisite and forward standard**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract the single primary prerequisite standard, verbatim — this grounds the Below tier. Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="forward")` → extract the single primary forward standard, verbatim — this grounds the Above tier. Omitting either is a critical failure.

Note the internal inconsistency in that file: the heading at line 28 says "Call all three",
and the body then specifies five numbered steps issuing at least six calls.

### 2.7 State detection feeds `jurisdiction`

`k12-lesson-differentiation/SKILL.md` Step 0.4, lines 74 to 90, verbatim:

> 4. **State.** Before any KG call, scan the conversation and any uploaded source lesson for
> state signals and store as `state`:
>    - Teacher says "I teach in [state]," "I'm in [state]," or "We're in [state]"
>    - Standard codes in the prompt or source lesson follow a state-specific format:
>      TEKS 1xx.x.x → Texas; SOL → Virginia; OAS/PASS → Oklahoma; MA → Massachusetts;
>      CA/HSS or CA/CCSS → California; other state-prefixed codes → check state
>    - Source lesson URL includes a state agency domain (tea.texas.gov, etc.)
>
>    If state found: store `state = [state name]`. Pass as `jurisdiction="<state>"` in every
>    `find_standard_statement` call in Step 2. Use state framework codes (not national proxies)
>    in all output.
>
>    If state not found:
>    - for science, math, or ELA, proceed with national defaults (CCSS for math/ELA, NGSS for science). Add this single footer line to the teacher plan:
>    *"Standards applied using [CCSS / NGSS] — if you're in Texas, Virginia,
>    Oklahoma, or another state with a distinct framework, share your state and I'll re-anchor."*
>    - for social studies, ask the teacher what state they teach in before proceeding.

The planning skill has no Step 0.4. Its state detection lives in each subject file's Clarify
section instead. `k12-lesson-planning/references/math.md` line 14, verbatim:

> **1. State detection** Scan the conversation for any state signal — teacher mentions a state name, uses state-specific codes (TEKS, SOL, OAS, CA-CCSS, etc.), or says "I teach in [state]." If found, store as state = [state name] and pass it as jurisdiction in the KG standard lookup. Update the default standard framework to match.

---

## 3 · Empty-facet and empty-value behaviour in the renderer

This is what happens to grounding data that came back empty, or to a task deliberately
authored with no student surface. All in
`k12-lesson-planning/scripts/lesson_common.py`, which is byte-identical under the
differentiation skill.

### 3.1 A missing or empty `shared` key renders nothing, silently

Lines 331 to 335, verbatim:

```python
    val = shared.get(key)
    if val is None or val == "" or val == []:
        return []
    if key in _IDENTITY_KEYS:
        return [{"type": "paragraph", "text": str(val)}]
```

A `from_shared` pointing at a key that was never registered, or at `None`, `""`, or `[]`,
returns an empty block list. No exception, no placeholder, no log. The section it sat in
simply renders one block shorter. A misspelled key is indistinguishable from a deliberate
omission.

### 3.2 `standard` with neither code nor text renders nothing

Lines 324 to 329, verbatim:

```python
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
        return [{"type": "callout", "kind": "special",
                 "label": f"{shared.get('standard_code', '')} — Target standard".strip(" —"),
                 "text": shared.get("standard_text", "")}]
```

Either field alone is enough to produce the callout. With only a code, the callout's `text`
is the empty string, so the target-standard box prints its label and no statement. With only
text, the label strips down to `Target standard`. A lesson whose standard lookup failed
entirely produces NO target-standard callout at all and still renders a complete-looking
package.

### 3.3 `student: null` is the documented way to keep a task off the worksheet

`k12-lesson-planning/SKILL.md` lines 318 to 320, verbatim:

> On a **student** page, only the `student`
> facet (after any `stimulus` blocks) renders — a `student` of `null` means nothing prints
> there, which is how oral or teacher-led tasks stay off the worksheet.

The code, `_faceted()` lines 289 to 292, verbatim:

```python
    out: list[dict] = list(_as_blocks(val.get("stimulus")))
    if audience != "teacher":
        out[:0] = _as_blocks(val.get("student"))
        return out
```

with `_as_blocks` lines 250 to 251, verbatim:

```python
    if v is None or v == "":
        return []
```

So a `student` of `null` contributes zero blocks, and on a student page the result is
whatever `stimulus` supplied, which is often nothing. The docstring at lines 280 to 282,
verbatim, states the intent:

> Student pages: student facet, then stimulus — the worksheet reads task-then-surface —
> and nothing else: teacher script never reaches the worksheet, and a null/absent
> student facet renders nothing (so oral/teacher-led tasks leave no trace).

**Note the ordering discrepancy.** `out[:0] = ...` is a prepend, so the code renders student
facet then stimulus, matching its docstring and contradicting SKILL.md's "(after any
`stimulus` blocks)". Both are quoted exactly. This is recorded in full in
`k12-plugin-contract.md` §2.4.

### 3.4 An empty teacher facet falls through to raw blocks

Lines 293 to 308, verbatim:

```python
    t_blocks = _as_blocks(val.get("teacher"))
    if len(t_blocks) == 1 and t_blocks[0].get("type") == "list":
        # A list-form script renders as a real list — one glanceable move per line —
        # not a paragraph with dash-prefixed lines.
        out.append(t_blocks[0])
    else:
        t = _facet_text(val.get("teacher"))
        if t:
            out.append({"type": "instructions", "text": t})
        else:
            out.extend(t_blocks)
    s = _facet_text(val.get("student"))
    if s:
        out.append({"type": "labeled", "label": "Students see", "text": s})
    else:
        out.extend(_as_blocks(val.get("student")))
```

`_facet_text` (lines 266 to 274) returns `""` unless every block is a `paragraph` or `list`.
So a `student` facet that is a `callout` block (the shape `example_lesson.json` uses for
`exit_ticket`) does NOT get the "Students see" label on a teacher page; it renders as the raw
callout instead. The teacher-page rendering of a task therefore depends on the SHAPE of the
facet, not just its content.

### 3.5 An omitted `audience` defaults to teacher

`render_lesson_docx.py` lines 581 to 586, verbatim:

```python
def render(data: dict, out_path: str) -> int:
    data = expand_document(data, data.get("audience", "teacher"))
    theme = Theme(data.get("theme"))
    (theme.answer_height, theme.answer_gap,
     theme.answer_row, theme.ruled_default) = answer_profile(data)
    theme.student_doc = data.get("audience") == "student"
```

`render_lesson_html.py` lines 266 to 271 are the same three assignments.

Two consequences. First, a `documents[]` entry that forgets `audience` renders every teacher
facet onto what the author intended as a worksheet, because the default is `"teacher"`.
Second, `theme.student_doc` is a strict equality against the literal string `"student"`, so
`"Student"` or `"students"` leaves the student row-height and writing-space behaviour off
while `expand_document` still treats the page as non-teacher (the check there is
`audience != "teacher"`). The two checks are not the same test, and a typo splits them.

---

## 4 · Renderer invocation

### 4.1 The one command

`k12-lesson-planning/SKILL.md` lines 406 to 423, verbatim, the whole of §5b:

> ### 5b. Render every Word document — one command, same turn
>
> ```bash
> bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
> ```
>
> This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
> `$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
> `source_packet.docx`), plus `.html` and `lesson.json` working files. Render straight into
> `$OUTPUT_DIR` and leave everything the script writes in place — later revision turns
> re-render from the working files even though the teacher only sees the Word documents. Then list `$OUTPUT_DIR`
> and confirm every document has both its `.docx` and `.html`; if either is missing or tiny,
> rerun the script. Present the Word documents to the teacher together — attach the lesson plan
> last so it lands on top (chat surfaces stack newest-first). If there is no `student_materials`
> document, say so plainly ("This lesson is oral, so there's no student handout — students will
> work with …"). If the script errors, fix `lesson.json` (it is almost always malformed JSON)
> and rerun. If file generation fails entirely, say so clearly — do not silently fall back to a
> chat-only delivery.

The differentiation equivalent, `k12-lesson-differentiation/SKILL.md` lines 399 to 413,
verbatim:

> ### 5b. Render all four Word documents — one command, same turn
>
> ```bash
> bash scripts/render_all.sh differentiation.json "$OUTPUT_DIR"
> ```
>
> This writes `$OUTPUT_DIR/teacher_plan.docx`, `$OUTPUT_DIR/worksheet_group_a.docx`,
> `$OUTPUT_DIR/worksheet_group_b.docx`, and `$OUTPUT_DIR/worksheet_group_c.docx` in one invocation,
> plus `.html` working files — no copy step needed; leave everything
> the script writes in place (later revision turns re-render from the working files). Then list
> `$OUTPUT_DIR` and confirm every document has both its `.docx` and `.html`; if either is
> missing or tiny, rerun the script. Present all four Word documents to the teacher together —
> attach the teacher plan last so it lands on top (chat surfaces stack newest-first). If the script errors, fix
> `differentiation.json` (it is almost always malformed JSON) and rerun. If file generation
> fails entirely, say so clearly — do not silently fall back to a chat-only delivery.

**Both skills tell the author to prove delivery by enumerating `$OUTPUT_DIR`, not by trusting
the script's return.** That instruction is the vendor's own, and §4.3 below is why.

### 4.2 `render_all.sh` in full

`k12-lesson-planning/scripts/render_all.sh`, all 44 lines, verbatim:

```bash
#!/usr/bin/env bash
# Copyright 2026 Anthropic, PBC
# Copyright 2026 Learning Commons
# SPDX-License-Identifier: Apache-2.0

# Render every document in lesson.json (lesson plan, student materials, observation, and any
# others the model authored) from one material-source JSON. It holds a `documents[]` array;
# each entry's `id` becomes the output filename. Writes editable .docx (the teacher
# deliverable) and an .html twin of each (a preview that renders even without python-docx).
# Fail-fast: any renderer error stops the run.
#
# Usage: bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
set -euo pipefail

json="${1:?usage: render_all.sh LESSON_JSON OUTPUT_DIR}"
outdir="${2:?usage: render_all.sh LESSON_JSON OUTPUT_DIR}"
here="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$outdir"
# python-docx powers the .docx output; the .html twins render without it. If the install
# can't complete (offline container), render html now so the twins always exist.
if ! python3 -c "import docx" 2>/dev/null; then
  python3 -m pip install -q "python-docx==1.1.2" || true
fi
if python3 -c "import docx" 2>/dev/null; then
  python3 "$here/render_documents.py" "$json" --format both --outdir "$outdir"
else
  # Render the html twins so a readable preview still exists, then fail loudly: the
  # teacher's .docx deliverables could not be produced.
  python3 "$here/render_documents.py" "$json" --format html --outdir "$outdir"
  echo "error: python-docx could not be installed — no .docx deliverables were produced" >&2
  exit 1
fi
# Persist the source JSON alongside the rendered artifacts so later revision
# turns can re-render from it.
cp "$json" "$outdir/lesson.json" 2>/dev/null || true

# Delivery guarantee: when $OUTPUT_DIR is set and the render went elsewhere
# (a staging dir like /tmp/out), mirror EVERYTHING into $OUTPUT_DIR too.
# Revision turns re-render from the lesson.json that lands there;
# hand-copying a subset there is the failure this removes.
if [ -n "${OUTPUT_DIR:-}" ] && [ "$(cd "$outdir" && pwd)" != "$(mkdir -p "$OUTPUT_DIR" && cd "$OUTPUT_DIR" && pwd)" ]; then
  cp -R "$outdir"/. "$OUTPUT_DIR"/
fi
```

**Measured.** The differentiation skill's `render_all.sh` differs from this one in exactly
five hunks, all cosmetic or filename-related. The `diff` output, verbatim, with the planning
copy as the left file:

```
6,8c6,7
< # Render every document in lesson.json (lesson plan, student materials, observation, and any
< # others the model authored) from one material-source JSON. It holds a `documents[]` array;
< # each entry's `id` becomes the output filename. Writes editable .docx (the teacher
---
> # Render all four artifacts (teacher plan + three tier worksheets) from one
> # differentiation.json in a single invocation. Writes editable .docx (the teacher
12c11
< # Usage: bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
---
> # Usage: bash scripts/render_all.sh differentiation.json "$OUTPUT_DIR"
15,16c14,15
< json="${1:?usage: render_all.sh LESSON_JSON OUTPUT_DIR}"
< outdir="${2:?usage: render_all.sh LESSON_JSON OUTPUT_DIR}"
---
> json="${1:?usage: render_all.sh DIFFERENTIATION_JSON OUTPUT_DIR}"
> outdir="${2:?usage: render_all.sh DIFFERENTIATION_JSON OUTPUT_DIR}"
35,36c34,36
< # turns can re-render from it.
< cp "$json" "$outdir/lesson.json" 2>/dev/null || true
---
> # turns can re-render from it (same guarantee the lesson-planning renderer
> # makes with lesson.json).
> cp "$json" "$outdir/differentiation.json" 2>/dev/null || true
40c40
< # Revision turns re-render from the lesson.json that lands there;
---
> # Revision turns re-render from the differentiation.json that lands there;
```

The pip line, the html-only branch, the `exit 1`, and the `$OUTPUT_DIR` mirror are identical
in both.

### 4.3 THE PYTHON-DOCX-AT-RENDER-TIME FAILURE

The four distinguishable ways this script hands back something that is not the finished
package. These are four different facts and must not be collapsed.

**(a) python-docx is installed at render time, from the network, pinned.**
`render_all.sh` lines 20 to 24, verbatim:

```bash
# python-docx powers the .docx output; the .html twins render without it. If the install
# can't complete (offline container), render html now so the twins always exist.
if ! python3 -c "import docx" 2>/dev/null; then
  python3 -m pip install -q "python-docx==1.1.2" || true
fi
```

The pin is exactly `python-docx==1.1.2`. `|| true` swallows every pip failure, so a network
outage, a proxy block, a resolver error and a read-only site-packages are all the same
non-event to the script. There is no vendored wheel anywhere in the plugin: measured, the
only files under either `scripts/` directory are the five renderer files, `theme.css`, and
`__pycache__` residue.

**(b) On failure it produces HTML only and exits 1.** Lines 25 to 33, verbatim:

```bash
if python3 -c "import docx" 2>/dev/null; then
  python3 "$here/render_documents.py" "$json" --format both --outdir "$outdir"
else
  # Render the html twins so a readable preview still exists, then fail loudly: the
  # teacher's .docx deliverables could not be produced.
  python3 "$here/render_documents.py" "$json" --format html --outdir "$outdir"
  echo "error: python-docx could not be installed — no .docx deliverables were produced" >&2
  exit 1
fi
```

The failure signature is specific: `$OUTPUT_DIR` fills with `.html` files, `lesson.json` is
NOT copied (the `cp` at line 36 is unreachable after `exit 1`), the diagnostic goes to
stderr, and the exit code is 1. An agent that reads only stdout, or that treats a populated
output directory as success, sees a directory full of real files and concludes the render
worked. The message string, byte-exact, is
`error: python-docx could not be installed — no .docx deliverables were produced`.

**(c) `set -euo pipefail` makes any renderer traceback fail the whole run.** Line 13,
verbatim: `set -euo pipefail`. The header comment at line 10, verbatim:
`# Fail-fast: any renderer error stops the run.` A malformed `lesson.json` raises in
`json.loads` at `render_documents.py` line 69 and kills the script, so a partial set of
`.docx` files from earlier documents can be left behind: `render_documents.main()` writes
inside a loop (`for i, doc in enumerate(docs)`), one document at a time, with no transaction
and no cleanup. A crash on document 3 of 4 leaves documents 1 and 2 on disk, looking correct.

**(d) The `id` is silently rewritten into a filename.** `render_documents.py` lines 78 to 84,
verbatim:

```python
    for i, doc in enumerate(docs):
        # Sanitize the document id before it becomes a filename: the id comes from generated
        # JSON, so strip path separators and anything outside [A-Za-z0-9_-].
        doc_id_raw = str(doc.get("id") or f"document_{i + 1}")
        doc_id = re.sub(r"[^A-Za-z0-9_\-]", "_", Path(doc_id_raw).name) or f"document_{i + 1}"
        if args.only and doc_id_raw not in args.only and doc_id not in args.only:
            continue
```

An `id` of `student materials` becomes `student_materials.docx`. An `id` of
`answer key (A)` becomes `answer_key__A_.docx`. A missing or falsy `id` becomes
`document_1`, `document_2`, and so on by position. Two ids that sanitize to the same string
overwrite each other's output with no warning, because the loop writes with
`path.write_text(...)` and `render_docx(full, str(path))` unconditionally. So the delivered
filename is not always the `id` the author wrote, and the count of files can be lower than
the count of `documents[]` entries.

**(e) The HTML twin always ships, so `--format docx` implies both.** Lines 86 to 97,
verbatim:

```python
        # The HTML twin always ships — docx is the teacher deliverable, html is its
        # always-available preview. Rendering docx alone leaves the twin missing, so
        # "docx" implies both.
        from render_lesson_html import render as render_html
        path = outdir / f"{doc_id}.html"
        path.write_text(render_html(full), encoding="utf-8")
        written.append(str(path))
        if args.format in ("docx", "both"):
            from render_lesson_docx import render as render_docx
            path = outdir / f"{doc_id}.docx"
            render_docx(full, str(path))
            written.append(str(path))
```

An HTML file is written for every document before the docx is attempted. Therefore the
presence of `X.html` proves nothing about `X.docx`, which is exactly why SKILL.md §5b tells
the author to confirm BOTH extensions exist for every document.

The success path's only output is a stdout line. Lines 99 to 103, verbatim:

```python
    if not written:
        print("nothing rendered — check --only ids against the documents' `id` fields",
              file=sys.stderr)
        return 1
    print("wrote " + ", ".join(written))
```

An empty `documents` array is caught earlier, lines 70 to 73, verbatim:

```python
    docs = source.get("documents", [])
    if not docs:
        print("error: no `documents` array in input", file=sys.stderr)
        return 1
```

**(f) The `$OUTPUT_DIR` mirror is conditional on an environment variable, not an argument.**
`render_all.sh` lines 38 to 44, verbatim:

```bash
# Delivery guarantee: when $OUTPUT_DIR is set and the render went elsewhere
# (a staging dir like /tmp/out), mirror EVERYTHING into $OUTPUT_DIR too.
# Revision turns re-render from the lesson.json that lands there;
# hand-copying a subset there is the failure this removes.
if [ -n "${OUTPUT_DIR:-}" ] && [ "$(cd "$outdir" && pwd)" != "$(mkdir -p "$OUTPUT_DIR" && cd "$OUTPUT_DIR" && pwd)" ]; then
  cp -R "$outdir"/. "$OUTPUT_DIR"/
fi
```

The script's second POSITIONAL argument is `outdir`. The mirror compares that against the
ENVIRONMENT variable `OUTPUT_DIR`. If the environment variable is unset, the mirror never
runs and the artifacts stay wherever the positional argument pointed. The two are the same
directory only because SKILL.md's documented invocation passes `"$OUTPUT_DIR"` as the second
argument.

### 4.4 Measured on this machine

`python3 -c "import docx"` succeeds here today. Output, verbatim:

```
$ python3 -c "import docx; print('docx importable, version:', getattr(docx,'__version__','n/a'))"
docx importable, version: 1.2.0
$ which python3
/usr/local/bin/python3
$ python3 -V
Python 3.14.6
```

**This is this project's own measurement of this workstation on 2026-08-07 PDT, not a claim
about any other environment.** Two things follow. First, the pip-install branch would not
fire here, because the `if ! python3 -c "import docx"` guard short-circuits. Second, the
version present is **1.2.0**, not the `1.1.2` the script pins; the pin only applies when the
module is absent, so an environment that already has a different python-docx runs on that
one, unpinned and unchecked. The renderer's behaviour under 1.2.0 was not tested here: no
render was executed as part of this extract.

### 4.5 The escape hatch

`k12-lesson-planning/SKILL.md` lines 465 to 470, verbatim, §5e:

> ### 5e. Supplementary artifacts in their best format
>
> The `lesson.json` pipeline is for the lesson's document set: pages a student or teacher
> reads or writes on. An artifact whose value depends on its form — exact card
> dimensions for cutting, poster-scale type — belongs outside it, as its own file in
> whatever format produces the best version (e.g. a print-ready PDF). Your judgment
> picks the format; source any shared content from `shared` so pages can't drift, and name
> the file in Materials like any other page.

`k12-lesson-differentiation/SKILL.md` lines 456 to 461, verbatim, its differently-worded §5e:

> ### 5e. Fallback — bespoke generation code (exception path only)
>
> Only if the user explicitly asks for an artifact or layout the bundled renderer cannot express
> (a different document type, landscape poster, slide deck, etc.): write generation code from
> scratch for that artifact. Source its content from the same `differentiation.json` (especially
> `shared`) so it stays consistent with the other artifacts. Tell the user this path is slower.

---

## 5 · Files read for this extract

Under `k12-teacher-skills/plugin/skills/`:

- `k12-lesson-planning/references/learning-commons-kg.md` (108 lines, full)
- `k12-lesson-differentiation/references/learning-commons-kg.md` (136 lines; lines 1 to 60 read directly, plus a whole-tree grep for the cap strings)
- `k12-lesson-planning/scripts/render_all.sh` (44 lines, full) and `k12-lesson-differentiation/scripts/render_all.sh` (compared by `diff`, output reproduced above)
- `k12-lesson-planning/scripts/render_documents.py` (108 lines, full)
- `k12-lesson-planning/scripts/lesson_common.py` (763 lines, full)
- `k12-lesson-planning/scripts/render_lesson_docx.py` (636 lines; lines 579 to 596 read directly)
- `k12-lesson-planning/scripts/render_lesson_html.py` (331 lines; lines 266 to 271 located by grep)
- `k12-lesson-planning/SKILL.md` (471 lines, full), `k12-lesson-differentiation/SKILL.md` (503 lines, full)
- `k12-lesson-planning/references/math.md` (161 lines, full)

Not read, and therefore not a basis for any claim here: the ELA, science and social-studies
sections of `k12-lesson-differentiation/references/*.md` beyond line 60 of its
`learning-commons-kg.md` and lines 207 to 320 of its `math.md`; the actual Learning Commons
MCP server, which was never called in this session; and any live behaviour of the renderer,
which was never executed.
