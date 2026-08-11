---
source_url: k12-teacher-skills/plugin/skills/ (fork checkout) and ~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/skills/ (installed copy)
fetched: 2026-08-08
http_status: n/a
role: primary
covers: k12-document-set, k12-shared-registry, k12-lesson-plan-sections, k12-student-materials, k12-observation-template, k12-density-rules, k12-package-consistency, k12-assessment-gap, practice-format-a-lesson-package
---

# The k12-teacher-skills artifact contract

Read at 2026-08-07 21:15 PDT, which is 2026-08-08 04:15 UTC. Local files, so no HTTP
status exists. Every quotation below is byte-exact from the file and line named beside it.
Everything not inside quotation marks is paraphrase.

---

## 0 · Provenance, version, and the two copies

`plugin/.claude-plugin/plugin.json`, whole file, verbatim:

```json
{
  "name": "k12-teacher-skills",
  "version": "0.6.0",
  "description": "Skills and MCPs for K-12 Education, including standards-aligned lesson planning and lesson differentiation across math, ELA, science, and social studies.",
  "author": {
    "name": "Anthropic"
  }
}
```

`plugin/.claude-plugin/marketplace.json` names the same version `"0.6.0"`, `"category": "education"`,
`"displayName": "K-12 Education"`, `"source": "./"`, owner `"Anthropic"`, and a marketplace
`metadata.description` of `"Plugin marketplace for K-12 Education and Claude for Teachers."`

**Measured, this project's own measurement, not a vendor claim.** The installed plugin at
`~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/`
and the fork checkout at `k12-teacher-skills/plugin/` are
byte-identical. Command run and its result:

```
diff -r -q --exclude=__pycache__ \
  ~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/ \
  k12-teacher-skills/plugin/
EXIT:0     (no output, no differing files)
```

The only excluded difference is `__pycache__/*.pyc`, which is build residue. Either path is
therefore a valid citation for the same bytes.

Fork git state, measured: single commit `7c03c83 Initial commit`, clean working tree,
`origin https://github.com/woodfordintegrations-collab/k12-teacher-skills.git`,
`upstream https://github.com/anthropics/k12-teacher-skills.git`.

### Licence sentences, preserved with their neighbours

`plugin/skills/k12-lesson-planning/SKILL.md` frontmatter, line 5, verbatim:

```
license: Complete terms in LICENSE
```

Immediately below the frontmatter, `SKILL.md` lines 8 to 12, verbatim (the HTML comment):

```
<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->
```

The same three-line SPDX block heads `k12-lesson-differentiation/SKILL.md` (lines 7 to 11)
and every one of the ten `references/*.md` files in the two skills.

`LICENSE` is the stock Apache License 2.0 text. Its own line 2 and 3 read `Apache License` /
`Version 2.0, January 2004`. Its appendix is the UNFILLED template: the file's last-but-13
line is verbatim `   Copyright [yyyy] [name of copyright owner]`, with the bracketed
placeholders still in place. Measured: `LICENSE` at the repo root, at
`plugin/skills/k12-lesson-planning/LICENSE`, and at
`plugin/skills/k12-lesson-differentiation/LICENSE` are all three identical.

Repo root `NOTICE`, whole file, verbatim:

```
Agent Skills for K-12 Teachers
Copyright 2026 Anthropic, PBC
Copyright 2026 Learning Commons
Portions of this product were co-developed by Anthropic, PBC
and Learning Commons under a collaboration agreement.
```

`plugin/skills/k12-lesson-planning/references/NOTICE`, whole file, verbatim. Measured
identical to `k12-lesson-differentiation/references/NOTICE`. **This is a separate rights
holder from the Apache grant above, and it is the standards text, not the code:**

```
© 2010 National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved.

The Common Core State Standards included in these reference files are used under the public license available at: https://www.thecorestandards.org/public-license/
```

Note the shape: an Apache-2.0 grant over the skill files, with an all-rights-reserved
NGA/CCSSO copyright and a pointer to a separate public licence sitting inside the same
`references/` directory. The NOTICE does not paste the public licence's terms; it only
gives the URL, which is not fetched in this extract.

---

## 1 · The document set

### 1.1 The material source

`k12-lesson-planning/SKILL.md` line 183 to 193, verbatim:

> The artifacts are rendered by bundled scripts from **one material-source `lesson.json`**. The JSON
> holds a `shared` block (content registered once) and a `documents[]` array (each document
> authored as free-form `sections`). A section's `heading` renders as a large title directly
> above its blocks; a block's `label` renders as a bold lead-in on the block itself. A label
> that repeats its section's heading prints the same words twice in a row — labels carry what
> the heading doesn't (the task's name belongs in one of them, not both). You
> compose every page — the lesson plan, the student
> materials, the observation template, and any others the lesson needs (e.g. a source packet)
> — directly in `documents[]`. Anything that appears on more than one page is registered once
> in `shared` under a key you choose and pulled into each document with
> `{"type": "from_shared", "key": …}`, so the pages cannot drift apart.

`SKILL.md` line 310, verbatim: "Write ONE `lesson.json` with two top-level keys: `shared` and `documents`."

### 1.2 The three required document ids, verbatim from SKILL.md lines 331 to 343

Preamble, line 331 to 332:

> **`documents[]` is where you compose each page.** Each entry is a full page:
> `{id, audience: teacher|student, eyebrow, title, meta?, theme?, sections[{heading, blocks[]}]}`.
> Include at minimum:

The three bullets, lines 336 to 343, verbatim:

> - `id: "lesson_plan"` (`audience: "teacher"`) — the subject file's section structure.
> - `id: "observation_template"` (`audience: "teacher"`) — how-to-use, look-fors,
>   misconceptions, a `fill_table` for student notes, and the exit-ticket sort.
> - `id: "student_materials"` (`audience: "student"`) — **only when students hold a printed
>   page.** A K-2 phonics or oral lesson may have none; a source-heavy lesson may have this AND
>   a separate `id: "source_packet"`. The subject file's *Student page layout* gives the
>   default skeleton; adapt it to the lesson. If the teacher asked for leveled/tiered student
>   materials, label them Group A / B / C (A = below, B = at, C = above grade level) — level
>   wording stays in the teacher-facing documents.

So `student_materials` is CONDITIONAL, and `source_packet` is a named legitimate fourth id.

### 1.3 The full published schema fence, SKILL.md lines 352 to 376, verbatim

> **Schema** — sufficient on its own; do not read any other file for the schema:
>
> ```
> shared:
>   grade, subject, duration, standard_code, standard_text          (required identity)
>   curriculum?, prerequisite_standard?, smps[]?
>   <any key you choose>: string
>                       | block | block[]
>                       | {teacher: …, student: … or null, stimulus?: block[]}
>   (only `standard` is special — it assembles standard_code+standard_text)
> documents[]: {id, audience: teacher|student, eyebrow, title, meta?, theme?,
>               sections[]: {heading, color?, blocks[]}}
> block types:
>   {type: from_shared, key}
>   {type: paragraph, text} | {type: labeled, label, text}
>   {type: callout, kind: special|student-task|teacher-note|student-note, label, text}
>   {type: h2|h3, text} | {type: list, label?, ordered?, items[]}
>   {type: phase_header, name, minutes} | {type: cards, items[{title, text}]}
>   {type: table|data_table, headers[]?, rows[[]]}
>   {type: fill_table, headers[], blank_rows: int, row_height_pt?}
>   {type: number_line, min, max, ticks?, marks[]?}
>   {type: source_card, title, author?, date?, origin?, excerpt}
>   {type: answer_box, height_pt?, ruled?} | {type: page_break}
>   {type: group, blocks[]} | {type: columns, left[], right[]}
> ```

### 1.4 The worked example ships a four-document set

`k12-lesson-planning/references/example_lesson.json`, parsed. Top-level keys are exactly
`shared` and `documents`. `documents[]` has FOUR entries, in this order:

| index | `id` | `audience` | `eyebrow` |
|---|---|---|---|
| 0 | `lesson_plan` | `teacher` | `Grade 6 · Mathematics · Ratios and Rates` |
| 1 | `student_materials` | `student` | `Grade 6 Mathematics · Student Materials` |
| 2 | `hint_cards` | `student` | `Grade 6 Mathematics · Hint Cards` |
| 3 | `observation_template` | `teacher` | `Grade 6 Mathematics · Observation Template` |

`hint_cards` is a fourth page not named anywhere in SKILL.md's minimum set, and its
`audience` is `student`. `lesson_plan.meta` is the string `Grade 6 · 50 minutes · 6.RP.A.2`.
`student_materials.meta` is the string
`Name: ____________________    Date: ____________    Partner: ____________________`.
`hint_cards` and `observation_template` carry no `meta` key at all.

`shared` in that file has exactly these 18 keys, in file order: `grade`, `subject`,
`duration`, `standard_code`, `standard_text`, `anchor_task`, `showdown_prices`, `p1`, `p2`,
`p3`, `p4`, `p5`, `vocabulary`, `misconceptions`, `look_fors`, `exit_ticket`, `exit_sort`,
`hint_cards`.

Note that `hint_cards` is both a `shared` registry key and a `documents[]` id in the same
file. The two namespaces do not collide, because ids become filenames and keys are looked up
in `shared`.

### 1.5 One document, one filename

`SKILL.md` line 406 to 416, verbatim (the render command and what it writes):

> ```bash
> bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
> ```
>
> This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
> `$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
> `source_packet.docx`), plus `.html` and `lesson.json` working files.

The mechanism is in `scripts/render_documents.py`. See `k12-grounding-and-render.md` in this
sources/ directory for the id sanitization and the failure modes.

---

## 2 · The `shared` registry and audience faceting

### 2.1 What SKILL.md publishes, lines 312 to 329, verbatim

> **`shared` is a content registry.** It always carries the lesson identity — `grade`,
> `subject`, `duration`, `standard_code`, `standard_text` (and `curriculum`,
> `prerequisite_standard`, `smps[]` when applicable). Beyond that, register any content that
> appears on more than one page under a key you choose: a problem as `p1`, a source as
> `stamp_act_petition`, a data set as `prices_table`. A key's
> value can be a string, a single block, a list of blocks, or a faceted object
> `{teacher: …, student: …, stimulus: [blocks]}`. On a **student** page, only the `student`
> facet (after any `stimulus` blocks) renders — a `student` of `null` means nothing prints
> there, which is how oral or teacher-led tasks stay off the worksheet. On a **teacher** page,
> both facets render: the teacher facet as plain script, then the student facet as one
> "Students see" line, so the teacher reads their own script and the exact prompt
> students will work from. A teacher facet written as a list of strings renders one move per
> line — the glanceable form for any script with more than two moves — and since the student
> text prints right beside it, the script points to it ("read the story in the box aloud")
> rather than quoting it again. Apart from `standard` (which assembles `standard_code` +
> `standard_text` into the target-standard callout), key names carry no special rendering — a
> vocabulary list, a misconceptions table, an exit-ticket sort are blocks you compose yourself
> (see `references/example_lesson.json` for the patterns).

`SKILL.md` lines 345 to 350, verbatim:

> Inside any document, pull registered content with `{"type": "from_shared", "key": "…"}` —
> the same key on two pages renders the same content (faceted by audience). Adding
> `"label": "1"` to a `from_shared` block renders the pulled text as a numbered item on one
> line. Within a single document, pull each key once (a reference table, an exit-ticket
> protocol, a word list appears in one section only). Content that appears on only one page
> can be written inline.

### 2.2 The eight identity keys, from the code

`scripts/lesson_common.py` lines 236 to 238, verbatim:

```python
# Keys in `shared` that are document/identity metadata, never expanded as content blocks.
_IDENTITY_KEYS = {"grade", "subject", "duration", "curriculum", "standard_code",
                  "standard_text", "prerequisite_standard", "smps"}
```

Eight keys. `expand_from_shared` lines 334 to 335, verbatim, is what makes them different:

```python
    if key in _IDENTITY_KEYS:
        return [{"type": "paragraph", "text": str(val)}]
```

An identity key pulled with `from_shared` renders as a bare paragraph of its `str()`, never
as blocks.

### 2.3 `standard` is the only special key

`lesson_common.py` lines 324 to 329, verbatim:

```python
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
        return [{"type": "callout", "kind": "special",
                 "label": f"{shared.get('standard_code', '')} — Target standard".strip(" —"),
                 "text": shared.get("standard_text", "")}]
```

The label string built here is the standard code, then a space, then an em dash, then
` Target standard`, with a leading or trailing ` —` stripped when the code is absent.

### 2.4 THE DOCUMENTED-VERSUS-CODE CONTRADICTION on facet order

SKILL.md line 318 to 320 says the student page renders "only the `student`
facet (after any `stimulus` blocks)". The code does the opposite ordering.

`lesson_common.py` `_faceted()`, lines 277 to 292, verbatim:

```python
def _faceted(val: dict, audience: str) -> list[dict]:
    """Expand a {teacher?, student?, stimulus?} value.

    Student pages: student facet, then stimulus — the worksheet reads task-then-surface —
    and nothing else: teacher script never reaches the worksheet, and a null/absent
    student facet renders nothing (so oral/teacher-led tasks leave no trace).

    Teacher pages: stimulus + teacher facet as plain script, then the
    student facet as ONE quoted "Students see" line — the teacher reads their own script and
    the exact prompt students will work from, the way a printed teacher edition shows both.
    Neither facet is a callout: callouts are reserved for the few moments a teacher must not
    miss, and a page where every task is boxed highlights nothing."""
    out: list[dict] = list(_as_blocks(val.get("stimulus")))
    if audience != "teacher":
        out[:0] = _as_blocks(val.get("student"))
        return out
```

`out[:0] = ...` is a PREPEND. On a student page the rendered order is therefore student facet
first, then stimulus. The function's own docstring agrees with the code ("student facet, then
stimulus"). SKILL.md line 318 to 319 says the opposite ("only the `student` facet (after any
`stimulus` blocks)"). Both are quoted here exactly. The code governs what prints.

### 2.5 Teacher-page facet rendering, lines 293 to 309, verbatim

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
    return out
```

The literal label string is `Students see`, and the teacher facet becomes an `instructions`
block, a type SKILL.md's schema fence never publishes.

### 2.6 The `label` fold, lines 343 to 365, verbatim

```python
    # `{type: from_shared, key: p1, label: "1"}` — fold the label into the first text-bearing
    # block (scanning past leading diagram blocks, which have nothing to fold into) so a
    # numbered prompt renders on one line, not an orphan number above a paragraph.
    # A label must never render alone. Dispatch on that block's FIELDS, not its
    # type name — type names change (callout -> instructions broke the old version of
    # this); the text/label/items field shapes are the schema's stable contract.
    label = (blk or {}).get("label")
    if label and out:
        i = next((j for j, b in enumerate(out)
                  if b.get("label") or b.get("text") or b.get("items")), 0)
        first = out[i]
        if first.get("label"):
            out[i] = {**first, "label": f"{label}. {first['label']}"}
        elif first.get("text"):
            out[i] = {"type": "labeled", "label": str(label), "text": first["text"]}
        elif first.get("items"):
            items = list(first["items"])
            out[i] = {"type": "labeled", "label": str(label), "text": str(items[0])}
            if items[1:]:
                out.insert(i + 1, {**first, "items": items[1:]})
        else:
            out.insert(i, {"type": "labeled", "label": str(label), "text": ""})
    return out
```

### 2.7 Empty and absent values

`expand_from_shared` lines 331 to 333, verbatim:

```python
    val = shared.get(key)
    if val is None or val == "" or val == []:
        return []
```

A missing key, a `None`, an empty string and an empty list all return an empty block list.
There is no warning, no error, and no placeholder. `_as_blocks` lines 250 to 251, verbatim,
does the same for a facet: `if v is None or v == "": return []`.

---

## 3 · `lesson_plan` section structure, per subject

The lesson plan's sections are NOT in SKILL.md. They are in the subject reference file,
and loading it is mandatory. `SKILL.md` lines 61 to 67, verbatim:

> **Loading the matching reference file is mandatory.** Drafting a lesson without first
> reading the subject reference is a critical failure. The reference file carries the
> complete subject-specific instructions: clarify priorities, curriculum branching,
> grade-band structures, section structure, non-negotiables, and the lesson.json mapping.
> Treat the loaded reference as your full skill instructions for this turn. If the subject
> is genuinely ambiguous or the prompt spans multiple subjects, ask about it
> in Step 1.

The Step 0 routing map, `SKILL.md` lines 56 to 59, verbatim:

> - math → `references/math.md`
> - ELA → `references/ela.md`
> - science → `references/science.md`
> - social studies → `references/social_studies.md`

### 3.1 MATH: five sections, `references/math.md` lines 80 to 89, verbatim

> ### Section structure — both paths
>
> 1. **At a glance** — standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist); a one-line lesson arc naming the phases with minutes ("Launch 8 → Explore 15 → Discuss 12 → Synthesize 5 → Exit 5") so the period's shape is visible before any detail; materials — name each item plainly (e.g. "Number cards 0-20"); SMPs named
> 2. **Learning goal** — Big Idea (enduring understanding, 1 sentence); SWBAT; Prerequisite (prior standard by code + one plain sentence on what students can already do and how today builds on it)
> 3. **Vocabulary & anticipated challenges** — 3–5 key terms with brief definitions; 2–3 misconceptions each as: *What students do* / *Why it happens* / *Teacher move*
> 4. **Lesson sequence** — phases per curriculum branch above; **Discuss gets at least 10 minutes** (in a short warm-up-style request, shrink the other phases, not Discuss); in Explore: 3+ look-fors each naming the student response, why it matters, and what to do with it — and if the anchor task admits more than one correct response or equation, one look-for must say so explicitly so the teacher accepts all of them; in Discuss: at least one named student-to-student talk move (Think-Pair-Share, Turn-and-Talk, partner compare, agree/disagree) + specific discourse prompts (not generic)
> 5. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when
>    adapting, with brief reasoning, including the lesson's central representation (the visual
>    or model students work with) and its one-sentence why. Rationale lives here, after the
>    teaching path — a teacher prepping reads the arc first, the reasoning second.

The realised headings in `example_lesson.json` documents[0] are, in order, and byte-exact:
`At a glance`, `Learning goal`, `Vocabulary & anticipated challenges`, `Lesson sequence`,
`Design notes`. That is five, matching the reference. The section heading uses an ampersand,
not the word "and".

The phase names for both math paths, `math.md` line 43 and line 49, verbatim:
"Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** exactly." (IM-confirmed) and
"Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** (problem-based)." (not IM-confirmed).

Problem-set coverage, `math.md` lines 57 to 64, verbatim:

> Before writing the practice problems (`shared.p1`..`pN`), ENUMERATE the standard's structural cases — the full span
> from the baseline case (the one every student must clear) to the structurally hardest case
> (the one students most often get wrong: start-unknown for K–2 story problems; a product
> smaller than both factors for decimal multiplication; the missing-leg case for the
> Pythagorean theorem; a midpoint or just-below-boundary number for rounding; a
> linear-but-not-proportional relationship for proportionality; and so on for other
> standards). Then write the set so EVERY enumerated case is a numbered, required problem (or
> the exit ticket), with its case named in that problem's `teacher` facet.

The four coverage rules follow at lines 66 to 78. Their first bullet, verbatim: "A structural
case that appears only in prose — the SWBAT, an anticipated challenge, a teacher move, or the
Discuss notes — does NOT count as covered. If the plan's prose names a case, a numbered
problem must present it to students."

Exit-ticket bar, `math.md` line 95, verbatim:

> - It IS the **structurally hardest enumerated case** (from the problem-set enumeration above; K–2: start-unknown or change-unknown), never a mid-difficulty stand-in. Pick it with the **misconception test**: a student who holds the lesson's primary anticipated misconception must get the exit ticket WRONG. If that student would get it right, you picked an affirming instance — swap it for the discriminating one (a lesson distinguishing X from not-X exits on the not-X case; a lesson fixing a placement habit exits where that habit produces a wrong answer). Name the case in `shared.exit_ticket.teacher`.

`math.md` line 99, verbatim: "- 3 sort buckets — *Got it* / *Almost there* / *Needs re-teaching* — **each with explicit criteria** describing what a response in that bucket contains (e.g. "Got it: correct equation with the unknown where it lives in the story", not the bare label); all three criteria appear in the lesson plan, never truncated to labels."

### 3.2 ELA: five sections, `references/ela.md` lines 170 to 178, verbatim

> ### Section structure — all grade bands
>
> 1. **At a glance** — standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist); a one-line lesson arc naming the phases with minutes so the period's shape is visible before any detail; anchor text (title + genre + Lexile if known, or [suggested] flag); materials list — name each item plainly (e.g. "Picture cards, 18")
> 2. **Learning goal** — Big Idea (enduring understanding, 1 sentence tied to the text and unit); SWBAT bullets drawn from KG learning components (learning-commons-kg.md, ELA call 2), naming specific sub-skills; Prerequisite (prior standard by code + gist + 1 sentence on prior knowledge assumed)
> 3. **Vocabulary & anticipated challenges** — 2–3 Tier 2 target words with definitions and text context; 3 misconceptions specific to this text and task, drawn from the KG or training knowledge, each formatted: *What students do* / *Why it happens* / *Teacher move*
> 4. **Lesson sequence** — phases per grade band above; in every phase where students work (reading, word work, writing, sorting): 3+ look-fors each naming the specific student behavior, why it matters for the standard, and what to do; in every discussion phase: specific text-dependent prompts (not generic)
> 5. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when adapting, each with a brief reason grounded in the research (Science of Reading for K–2 phonics; text complexity for 3–12), including the lesson's central representation or routine and its one-sentence why.
>
> → **Section structure complete. Proceed to the draft (when the teacher chose one) or Step 5.**

The ELA section names are byte-identical to math's five.

### 3.3 SCIENCE: SEVEN sections, `references/science.md` lines 138 to 151, verbatim

> ### Section structure — all grade bands
>
> 1. **At a glance** — standard verbatim in a `special` callout; a one-line lesson arc naming the phases with minutes so the period's shape is visible before any detail; anchoring phenomenon (title / brief description, or [suggested] flag); materials list — name each item plainly (e.g. "Data-recording cards")
> 2. **Three-dimensional learning targets** — state each dimension explicitly and separately, with framework names spelled out: Science and Engineering Practice ("Students will [practice verb] to [purpose]"); Disciplinary Core Idea ("Students will understand that [specific content idea]"); Crosscutting Concept ("Students will apply [named concept] to [specific use]"). Do not merge dimensions into a single vague objective.
> 3. **Unit storyline context** — 2–3 sentences. When the teacher has said where this lesson sits in a unit, place it: what students figured out last time, how today advances the explanation. When they haven't, write the lesson to stand alone and connect it by concept, not by position — name the ideas it builds on and the ones it pairs with ("builds on what students know about living things; pairs naturally with cells whenever you teach them"). Schools sequence topics their own way; a placement guess from the standards' canonical order is only right for schools that follow it.
> 4. **Vocabulary** — a reference list of the terms this lesson introduces, with
>    student-friendly definitions. A term is here because a phase teaches it (anchored to
>    something concrete — the diagram, an analogy, what students just observed); a term on a
>    student page that no phase teaches is a gap in the lesson, not in this list.
> 5. **Anticipated student ideas & misconceptions** — up to 3 entries from the KG OSE-materials call or training knowledge, each formatted: *What students think* / *Why it persists* / *Teacher move*
> 6. **Lesson sequence** — phases per grade band above; in every investigation phase: 3+ look-fors each naming the specific student behavior, why it matters for the 3D standard, and what to do; in every discussion phase: specific science-based prompts (not generic)
> 7. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when adapting, each with a brief reason grounded in three-dimensional learning, including the lesson's central representation (model, diagram, or data display) and its one-sentence why.
>
> → **Section structure complete. Proceed to the draft (when the teacher chose one) or Step 5.**

Science splits what math and ELA fold together: Vocabulary is its own section 4, and
misconceptions are section 5 under the name `Anticipated student ideas & misconceptions`.
There is no `Learning goal` section; section 2 is `Three-dimensional learning targets`.

Science's phase names differ per grade band, `science.md` lines 69, 86, 104, 122, verbatim:

- K to 2: `Phases: Launch Phenomenon → Investigation → Sensemaking Discussion → Model/Representation → Exit Ticket`
- 3 to 5: `Phases: Launch Phenomenon → Investigation → Sensemaking Discussion → Claim-Evidence-Reasoning Writing → Model Update → Exit Ticket`
- 6 to 8: `Phases: Launch Phenomenon → Investigation → Argumentation Discussion → Claim-Evidence-Reasoning Explanation → Model Revision → Formative Check`
- 9 to 12: `Phases: Launch Phenomenon → Investigation → Scientific Argumentation → Explanation/Modeling → Science-Society Connection → Formative Check`

### 3.4 SOCIAL STUDIES: SEVEN sections, `references/social_studies.md` lines 74 to 113, verbatim

> ### Section structure — teaching order
>
> 1. **At a glance** — grade band; time; standard verbatim in a `special` callout (the ONE
>    verbatim quote — everywhere else standards go by code + short gist); a one-line lesson arc
>    naming the phases with their minutes (e.g. "Hook 5 -> source work 20 -> discussion 15 ->
>    exit 10") so the shape of the lesson is visible before any detail; the lesson's C3 inquiry
>    focus in plain words (e.g. "C3: evaluating sources and using evidence"); materials —
>    name each item plainly.
> 2. **Compelling & supporting questions** — the unit-level question, and the narrower question
>    this single lesson investigates (one of the 3–5 that would make up the full unit).
> 3. **Lesson goals & background for the teacher** — 1–2 SWBATs; assumed prior knowledge,
>    specific; 2–3 anticipated challenges for this topic and source set (*what students do* /
>    *why it happens* / *teacher move*); Key
>    vocabulary (4–6 terms, defined at grade level, each introduced at the moment the
>    lesson needs it). The background content itself lives inside the lesson sequence, in the
>    phase that delivers it.
> 4. **Source set (2 sources)** — sources are real, high-quality, and specifically cited
>    (title, author, date, archive). If you have web search, confirm before using. A
>    public-domain text source (pre-1929, government documents) gets an excerpt reproduced, sized to the analysis the questions ask of it
>    as a `source_card`; an image, photograph, political cartoon, or copyrighted text isn't
>    reproduced — name it (title, citation, where to find it) in Materials and the phase that
>    uses it. Register each reproduced source in `shared` under its own key. For each source:
>    the card itself (its citation carries where the text lives — full URL when you verified it
>    resolves this session; otherwise the archive and collection by name, nothing more — the
>    same rule covers call numbers and catalog IDs, which appear only verified) plus
>    ONE sentence of why this source, as a labeled line. Procurement details, search tips, and
>    alternate locations don't help a teacher mid-prep — leave them out. Close the section with
>    one sentence on the pairing — the tension or contrast the two sources create.
> 5. **Lesson sequence** — phases in teaching order, minutes summing exactly to the period:
>    background knowledge (this phase carries its content inline — the short labeled chunks
>    the teacher actually says, a half page at most, never an essay) → source work with
>    **2–3 guided analysis questions** (scaffolded:
>    observe → source or contextualize → corroborate and connect to the supporting question) →
>    discussion → exit ticket.
> 6. **Exit ticket** — students answer the supporting question with evidence from the sources.
>    Sized to the minutes remaining in the period: a claim plus one or two pieces of cited
>    evidence, per the grade band below — never a take-home essay. 2–3 success-criteria bullets.
> 7. **Design notes** — 2–3 elements to keep intact when adapting, each with a one-sentence
>    reason grounded in the standard, including the lesson's central organizer or source-work
>    structure and its one-sentence why.

Social studies is the only subject where the exit ticket is a top-level lesson_plan SECTION
(6) rather than the last phase inside Lesson sequence. The other three all say the exit
ticket is the last phase in Lesson Sequence, pulled with `from_shared:exit_ticket` under its
phase header (`math.md` line 93, `ela.md` line 182, `science.md` line 155).

`social_studies.md` line 19, verbatim, on the C3 framework:

> **C3 Framework note.** The C3 Framework is an *inquiry design* framework, not a standards document. Use C3 for instructional design (the inquiry arc, sourcing, argumentation, civic action), but the lesson's content scope and the verbatim standard must come from the **state** standard — never substitute a C3 dimension or indicator for the standard, and never fall back to C3 when a state standard is unavailable.

`social_studies.md` line 29, verbatim: "- **State** (required): Social studies standards are state-specific. If the teacher does not name a state and it is not inferrable, ask."

---

## 4 · `observation_template`

The document is required (SKILL.md line 338 to 339, quoted in §1.2 above). Its layout comes
from `references/math.md` lines 150 to 159, verbatim:

> **Observation template layout** (the `id: "observation_template"` document):
>
> ```
> sections:
>   "How to use this"        one-paragraph instructions
>   "Look-fors"              from_shared:look_fors
>                            fill_table headers=[Student, Strategy seen, Next step] blank_rows=8
>   "Anticipated challenges" from_shared:misconceptions
>   "Exit-ticket sort"       from_shared:exit_ticket
> ```

Four sections. The heading strings, byte-exact: `How to use this`, `Look-fors`,
`Anticipated challenges`, `Exit-ticket sort`.

`references/ela.md` line 226, verbatim: "**Observation template layout** matches the math layout in `references/math.md`."

`references/social_studies.md` lines 196 to 197, verbatim: "**Observation template layout**: as in `references/math.md`, with `fill_table` headers
`[Student, Evidence of thinking, Instructional move]`."

`references/science.md` lines 177 to 178, verbatim: "- In the observation template, prefix each look-for with its dimension so the teacher sees
which one they're watching for." Science gives no `fill_table` header override.

### 4.1 The realised observation_template in example_lesson.json

`documents[3]`, parsed and reproduced exactly:

```json
{
 "id": "observation_template",
 "audience": "teacher",
 "eyebrow": "Grade 6 Mathematics · Observation Template",
 "title": "Grocery Store Showdown Observation",
 "sections": [
  {"heading": "How to use this",
   "blocks": [{"type": "paragraph", "text": "Circulate during Explore. Tally what you see in the Look-fors grid; star one ratio-table scaler and one divider to share in Discuss. After class, sort exit tickets into the three piles below."}]},
  {"heading": "Look-fors",
   "blocks": [{"type": "from_shared", "key": "look_fors"},
              {"type": "fill_table", "headers": ["Student", "Strategy seen", "Next step"], "blank_rows": 8, "row_height_pt": 26}]},
  {"heading": "Anticipated challenges",
   "blocks": [{"type": "from_shared", "key": "misconceptions"}]},
  {"heading": "Exit-ticket sort",
   "blocks": [{"type": "from_shared", "key": "exit_ticket"},
              {"type": "from_shared", "key": "exit_sort"}]}
 ]
}
```

Note that the example pulls TWO shared keys in `Exit-ticket sort`, `exit_ticket` and
`exit_sort`, while the math reference layout names only `from_shared:exit_ticket`. The sort
buckets are a separate registered key.

`shared.exit_sort` in that file, verbatim:

```json
{
 "type": "cards",
 "items": [
  {"title": "Got it",
   "text": "Both unit prices correct ($1.25 and $1.40 per bag), picks Store A, and explains using per-1 language."},
  {"title": "Almost there",
   "text": "Divides to find a price per bag (right method) but makes an arithmetic slip or finds only one unit price; conclusion follows their numbers."},
  {"title": "Needs re-teaching",
   "text": "Agrees with Maya by comparing totals ($4.20 < $5.00) or compares bag counts, without finding any price per bag."}
 ]
}
```

`shared.exit_ticket` in that file, verbatim, showing the faceted shape:

```json
{
 "teacher": "Collect on a half-sheet. The trap mirrors Rice: agreeing with Maya means comparing totals, not unit prices.",
 "student": {
  "type": "callout",
  "kind": "student-task",
  "label": "Exit ticket",
  "text": "Store A sells a 4-bag pack of popcorn for $5.00. Store B sells a 3-bag pack for $4.20. Maya says Store B is the better deal because $4.20 is less money. Find the price per bag at each store. Who is right, and why? Use the word 'per' in your answer."
 }
}
```

### 4.2 `fill_table` accepts an undocumented `rows` int

SKILL.md's schema fence publishes only `{type: fill_table, headers[], blank_rows: int, row_height_pt?}`.
`scripts/render_lesson_docx.py` `_emit_fill_table`, lines 409 to 434, verbatim:

```python
def _emit_fill_table(doc, blk, theme):
    headers = coerce_headers(blk.get("headers"))
    try:
        cols = max(1, len(headers) or int(blk.get("cols") or 2))
    except (TypeError, ValueError):
        cols = 2
    cols = min(cols, 12)
    rows_val = blk.get("rows")
    if isinstance(rows_val, list):
        # Mixed rows: a non-empty list renders its cells (a worked example);
        # an empty list [] renders a blank write-in row.
        rows = []
        for r in coerce_rows(rows_val[:50]):
            cells = r[:cols]
            rows.append(cells + [""] * (cols - len(cells)))
    else:
        try:
            n = int(blk.get("blank_rows") or rows_val or 3)
        except (TypeError, ValueError):
            n = 3
        rows = [[""] * cols for _ in range(min(max(1, n), 50))]
    fwd = {"headers": headers, "rows": rows}
    for k in ("row_height_pt", "empty_row_height_pt"):
        if blk.get(k):
            fwd[k] = blk[k]
    _emit_table(doc, fwd, theme)
```

So: `cols` (undocumented) is honoured, capped at 12; `rows` as a LIST renders mixed
filled/blank rows and is truncated at 50; `rows` as a non-list falls through to
`int(blk.get("blank_rows") or rows_val or 3)`, meaning `rows: 8` and `blank_rows: 8` are
equivalent and the default with neither is 3; row count is clamped to `min(max(1, n), 50)`;
and `empty_row_height_pt` (undocumented for `fill_table`) is forwarded alongside
`row_height_pt`. SKILL.md's block table documents `fill_table`'s `rows` behaviour at line
400 but the schema fence at line 371 does not list it.

---

## 5 · `student_materials`

Existence condition, SKILL.md line 340 to 343, quoted verbatim in §1.2 above: the document
exists "**only when students hold a printed page.**"

`references/ela.md` lines 206 to 211, verbatim, is the explicit no-document case:

> **Which documents to emit.** A K-2 phonemic-awareness or oral-language lesson (RF.*.2,
> RF.*.3 phonics warm-ups, listening-comprehension) often has **no `student_materials`
> document** — students hold response cards or nothing. Say so in the lesson plan's Materials
> line and in your message to the teacher. For 3–12 reading/writing lessons, emit
> `student_materials`; if the anchor text is reproduced, also emit a `source_packet` document
> containing just `from_shared:passage`.

`references/social_studies.md` lines 174 to 178, verbatim, is the opposite:

> **Documents to emit.** Social-studies inquiry lessons always have written analysis
> questions, so **always include `id: "student_materials"`** alongside `lesson_plan` and
> `observation_template`. When sources are registered, also include `id: "source_packet"`
> (one `from_shared` per source, plus a one-line "Read these with the worksheet" note). The
> student worksheet opens with "*See your Source Packet for Source A and Source B.*"

### 5.1 The four student-page skeletons, verbatim

MATH, `references/math.md` lines 128 to 148:

> **Student page layout** (the `id: "student_materials"` document) — start from this skeleton
> and adapt:
>
> ```
> sections:
>   "<warm-up heading, kid-facing>"  group[ from_shared:anchor_task, answer_box ]
>   "<practice heading>"     optional callout(student-note) — a brief reminder, only when one helps
>                            from_shared:<visual-scaffold key>   ← only when it is something
>                              students work with (blank fill_table, number_line, the data
>                              set the problems analyze) — a worked reference table is
>                              teacher-only
>                            for each problem k:
>                              group[ {type: from_shared, key: pk, label: "k"},
>                                     answer_box (bare -- it sizes to the grade band;
>                                     ruled: true when the answer is composed sentences) ]
>                            on the ONE problem whose hard part is the writing move, its
>                              group also carries the sentence support -- plain text before
>                              the answer_box (see Sentence supports in SKILL.md)
>                            page_break
>   "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
> ```

ELA, `references/ela.md` lines 213 to 224:

> **Student page layout** (when emitted) — start from this and adapt:
>
> ```
> sections:
>   "Before you read"        from_shared:anchor_task ; answer_box if a written prediction
>   "Text"                   from_shared:passage   (omit when the text isn't reproduced)
>   "Read and respond"       for each question k:
>                              group[ {type: from_shared, key: qk, label: "k"},
>                                     answer_box ]
>                            page_break
>   "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
> ```

SOCIAL STUDIES, `references/social_studies.md` lines 180 to 191:

> **Student page layout** (the `id: "student_materials"` document):
>
> ```
> sections:
>   "Supporting question"    callout(student-task) from_shared:supporting_question
>   "Sources"                from_shared:source_a ; from_shared:source_b
>   "Analyze the sources"    for each question k:
>                              group[ {type: from_shared, key: qk, label: "k"},
>                                     answer_box ]
>                            page_break
>   "Make your claim"        group[ from_shared:exit_ticket, answer_box ~180pt ]
> ```

SCIENCE ships NO skeleton. `references/science.md` lines 180 to 181 is the whole of it,
verbatim: "- Student-page section headings in plain inquiry language ("What do you notice?",
"Investigation") — you compose them directly in the document's sections."

The realised student_materials in `example_lesson.json` (documents[1]) has three section
headings, byte-exact: `Warm up together`, `Showdown: find the price for 1`,
`Show what you know`. Its block types per section are `[group]`,
`[callout, from_shared, group, group, group, group, group]`, and `[group]`.

### 5.2 The `group` wrapper and the automatic pairing

SKILL.md line 404, verbatim (the block table row):

> | `group` | Keeps a task's prompt, stimulus, supports, and answer box together so a page break never separates them. |

The pairing also happens automatically. `lesson_common.py` lines 386 to 404, verbatim:

```python
_PROMPT_TYPES = ("paragraph", "labeled", "callout", "list", "h3")


def _pair_writing_space(blocks: list[dict]) -> list[dict]:
    """Glue a prompt block to the workspace/answer_box that follows it so a page break can
    never separate a question from its writing space (renderers keep groups together).
    Types are compared post-alias (btype) so canonical and legacy names both pair."""
    out: list[dict] = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if (btype(b) in _PROMPT_TYPES and i + 1 < len(blocks)
                and btype(blocks[i + 1]) == "workspace"):
            out.append({"type": "group", "blocks": [b, blocks[i + 1]]})
            i += 2
            continue
        out.append(b)
        i += 1
    return out
```

Five prompt types pair. `h2`, `phase_header`, `table`, `cards` and `source_card` do not.
Because the comparison is `btype()` (post-alias), an `answer_box` pairs exactly as a
`workspace` does.

### 5.3 Grade-band writing-space sizing

SKILL.md line 403, verbatim (the block table row for `answer_box`):

> | `answer_box` | Writing space after a task. With no `height_pt` it sizes itself to the grade band (K-2 ~200pt, 3-5 ~150pt, 6-8 ~130pt, 9-12 ~115pt). K-5 boxes draw ruled handwriting lines except in math, which defaults to open space; `ruled: true` draws lines at any grade — the surface for answers of composed sentences — and `ruled: false` gives open space for drawing or model-sketching. A task answered in a `fill_table` or on a `number_line` already has its surface. |

The code, `lesson_common.py` `answer_profile()` lines 570 to 591, verbatim:

```python
def answer_profile(data: dict) -> tuple:
    """Grade-banded writing-space defaults:
    (height pt, ruled line gap pt, table-row pt, ruled by default).

    Math work space is open by default; a block's explicit `ruled: true`
    still gets the band's gap, so a grade-1 sentence answer gets K-2 pitch."""
    n = grade_number(data)
    if n is None:
        return 120.0, 22.0, 96.0, False
    shared = data.get("shared")
    shared = shared if isinstance(shared, dict) else {}
    # smps (Standards for Mathematical Practice) is the most reliable math signal — it is
    # math-only and the math reference mandates it, whereas shared.subject is often omitted.
    is_math = bool(shared.get("smps")) or "math" in " ".join(str(x or "") for x in (
        shared.get("subject"), data.get("eyebrow"), data.get("title"))).lower()
    if n <= 2:
        return 200.0, 40.0, 160.0, not is_math
    if n <= 5:
        return 150.0, 28.0, 126.0, not is_math
    if n <= 8:
        return 130.0, 24.0, 108.0, False
    return 116.0, 22.0, 96.0, False
```

**Exact numbers.** The 9-to-12 band returns `116.0`, not the "~115pt" SKILL.md publishes.
The unknown-grade fallback (`n is None`) is `120.0`, a value SKILL.md never mentions. The
`ruled` flag is `not is_math` for K-2 and 3-5 only; grades 6 to 8, 9 to 12 and the
unknown-grade fallback all return `False` unconditionally, so the "K-5 boxes draw ruled
handwriting lines" sentence is exact and the math carve-out applies only below grade 6.

`is_math` is detected from `shared.smps` being truthy, or the literal substring `math`
appearing in the lowercased join of `shared.subject`, `data.eyebrow` and `data.title`.

Explicit sizes, `lesson_common.py` lines 610 to 624, verbatim:

```python
WORKSPACE_SIZES = {"small": 70.0, "med": 130.0, "large": 220.0}
FILL_IN_CHARS = {"short": 12, "med": 28, "long": 60}  # underscore counts for non-CSS formats


def workspace_height(blk: dict, theme: Theme) -> float:
    """Resolve a workspace block's height in points (format-agnostic)."""
    h = blk.get("height_pt")
    if h is None:
        h = WORKSPACE_SIZES.get(str(blk.get("size", "")).lower())
    if h is None:
        h = theme.answer_height
    try:
        return float(h)
    except (TypeError, ValueError):
        return float(theme.answer_height)
```

Resolution order: explicit `height_pt`, then the named `size`, then the grade-band default.
`size` is not published in the planning SKILL.md's `answer_box` schema line, which lists only
`height_pt?` and `ruled?`. The differentiation SKILL.md does publish it, as
`{type: workspace, size: small|med|large, height_pt?}`.

### 5.4 Sentence supports, SKILL.md lines 272 to 279, verbatim

> **Sentence supports** are plain text where students write: a starter to begin from
> ("One central idea is…") or a fill-in frame with blanks sized for the student's handwriting.
> A support helps the student start, not answer — it never pre-fills what the task asks for.
> Place each one on the specific task whose writing move is hardest — including the
> explain-why beside a math equation — never one bank copied across problems. K-2 students
> and multilingual learners get a support on every task that asks for composed sentences.
> Tasks that take only a number, a single word, or a drawing need none.

---

## 6 · Density rules

SKILL.md lines 212 to 236, verbatim, the whole block:

> **Density rules — hard requirements for every document.** Every document is clear, brief,
> and easy to skim. Include what a teacher needs to teach it; leave out what merely
> demonstrates rigor. Headings use sentence case. Structure beats prose:
>
> - A `paragraph` or `labeled` block is at most 3 sentences. Longer → split it, bullet it, or
>   table it.
> - Write like a colleague's note: plain, direct sentences built from commas and periods.
> - Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
> - Parallel variants (per-group supports, per-phase differentiation, tiered look-fors) go in
>   ONE `table` block — rows = phases or features, columns = variants, ≤ ~25 words per cell —
>   never back-to-back multi-sentence paragraphs.
> - A callout marks the few moments a teacher must not miss — a warning ("do not resolve the
>   debate yet"), a collect-before-moving-on, the one make-or-break move of a phase. A page
>   where everything is boxed highlights nothing: a phase reads as plain script with at most
>   one or two callouts. Teacher asides (watch-fors, confer prompts) are `labeled` or
>   `instructions` blocks.
> - Each instruction lives in exactly one place. A phase's opening prose and its blocks divide
>   the work between them — the prose sets up, the blocks carry the content; neither repeats
>   the other.
> - Quote the standard verbatim exactly once (the target-standard callout, from `shared`).
>   Everywhere else — prerequisite grounding, forward connections — reference by code plus a
>   gist of ten words or fewer; never re-paste full standard text.
> - A section that runs past about half a page of continuous prose must be restructured
>   (table, bullets, or split into two sections) before rendering.

The verbatim-once rule appears again in each subject file's section 1. `math.md` line 82,
verbatim fragment: "standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist)".

The differentiation skill's density block is shorter and differs. `k12-lesson-differentiation/SKILL.md`
lines 240 to 255, verbatim:

> **Density rules — hard requirements for every document.** Teachers consistently flag dense
> walls of text. Structure beats prose:
>
> - A `paragraph` or `labeled` block is at most 3 sentences. Longer → split it, bullet it, or
>   table it.
> - Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
> - Parallel tier content (Below / At / Above doing the same phase differently) goes in ONE
>   `table` block — rows = phases or features, columns = tiers, ≤ ~25 words per cell — never
>   three back-to-back multi-sentence paragraphs.
> - An aside longer than one sentence (misconception watch-fors, confer prompts, deployment
>   guidance) becomes its own `callout` block, not a sentence buried in a paragraph.
> - Quote the standard verbatim exactly once (the target-standard callout, from `shared`).
>   Everywhere else — prerequisite grounding, forward connections — reference by code plus a
>   gist of ten words or fewer; never re-paste full standard text.
> - A section that runs past about half a page of continuous prose must be restructured
>   (table, bullets, or split into two sections) before rendering.

Differences, measured by comparing the two blocks: the planning skill adds "Headings use
sentence case", the colleague's-note sentence, the callout-count rule, and the
each-instruction-in-one-place rule; the differentiation skill adds the aside-becomes-a-callout
rule and has no callout-count rule.

### 6.1 Additional length caps in the differentiation skill

`k12-lesson-differentiation/references/math.md` line 207, verbatim:
"### Document content — teacher plan (`id: teacher_plan`) — max 3 pages"

Line 209 to 213, verbatim:

> **Length budget: ~1,200 words rendered (the 3-page cap in practice).** Tighten the tier
> sections and overview before touching the closers (Flexible Grouping, Why this works, Next
> Steps) — the most common overrun is a Worksheet tasks line that restates worksheet content
> instead of naming it. **"Why this works (1)" and "Why this works (2)" are required and cannot
> be dropped to meet the length budget — cut tier section prose first.**

---

## 7 · Package consistency invariants

SKILL.md lines 237 to 263, verbatim, the "Everything matches" block:

> **Everything matches — hard requirements for every document.** A teacher trusts the package
> because every part agrees with every other part:
>
> - The materials list and the phases agree exactly: every listed item is used by a named
>   phase, and every counted set matches its enumeration ("Picture cards, 18" lists 18 words).
> - **Classroom-ready:** the lesson runs on what the teacher already holds. Every Materials
>   item is a page this package ships, equipment the classroom has, or a sourced resource
>   with its access path stated — exact title and source, a link when you could confirm one.
>   Anything harder to get than that stays out of the lesson unless the teacher steered
>   toward it. A printable the lesson depends on ships with the package — as lesson pages
>   when the document set expresses it, or as its own file in the format that renders it
>   best (5e).
> - A task worded in two places (plan's "Students see" and the student page) uses identical
>   wording in both.
> - Student tasks match the skill the standard names, in both directions. Decoding, spelling,
>   and writing skills happen on paper — students read and write real words on a student page.
>   Listening and speaking skills get spoken, pointed, sorted, drawn, or circled responses.
>   The lesson's scope statement binds every task that follows it.
> - Scripts and worked examples are final say-aloud text: every step decided before it lands
>   on the page, exactly what the teacher says.
> - Exit-ticket sort buckets partition the answers: each example response fits exactly one
>   bucket, and equivalent forms of one answer (17 + 24 = ? and 24 + 17 = ?) sit in the same
>   bucket together.
> - An answer space mirrors its ask: rows match the count requested, and every box sits under
>   a prompt naming what goes in it.
> - Number pairs inside a sentence are plain text ("2 → 10, 5 → 25"); a table is always its
>   own block.

SKILL.md lines 284 to 306, verbatim, the "Document integrity" block:

> **Document integrity.** Every document is finished prose a teacher hands out or works from:
>
> - Every in-document reference points at something that exists in the package: "jot it in the
>   table below" means that table is on the page; an exit ticket collected separately prints as
>   its own piece; a reference table uses the same numbers as the problems it supports.
> - Materials and the lesson match both ways: each listed item is used somewhere in the
>   lesson, every item any section sends students to — phases and extensions alike — appears
>   in Materials, and anything students read is printed in the package or named by its exact
>   title. Offers and pointers to the chat conversation stay out
>   of documents entirely.
> - Lessons are light on materials: the default kit is what every classroom has (board,
>   projector, paper) plus the pages this lesson ships. A separate printable or manipulative
>   earns its place only when the activity genuinely needs it — and the same thinking work on
>   the worksheet usually serves. When a printable earns it (cards, mats, a template), ship it
>   with the package (5e picks the format); equipment a classroom owns is simply listed.
> - Phase minutes include the transitions they cause (handing out, regrouping, collecting), at
>   a pace real students of this grade manage, and the phases sum to exactly the stated
>   period — transition time lives inside the phases, never as invisible buffer.
> - Teacher notes read as finished sentences. A predicted error names one specific wrong answer
>   a real student would produce.
> - Verify every computation by working it — answer keys, worked examples, and any quantitative
>   chain the lesson builds on (an energy pyramid's levels, a ratio table's entries, a coin
>   total) produce the numbers the materials state.

The phase-minutes arithmetic appears a second time in the block table. SKILL.md line 395,
verbatim: "| `h2` | Sub-sections inside a section — the lesson-sequence phases use `phase_header`, which renders as h2 with minutes; the `minutes` across all phase headers should sum to `shared.duration`. |"

Revision consistency, SKILL.md lines 444 to 461, verbatim:

> ### 5d. Revisions — one edit, every artifact stays in sync
>
> Make **targeted edits to `lesson.json`**, then re-render every document (instant). Rules that
> keep the artifacts consistent:
>
> - If the change touches content registered in `shared` (a problem, a source, the exit ticket,
>   vocabulary, look-fors, the phenomenon/context/numbers), edit it **in `shared`** — every
>   document that pulls that key updates automatically.
> - **Consistency sweep after any context/number/task change:** after editing `shared`, re-read
>   every prose block in every `documents[]` entry and update every sentence that still mentions
>   the old context, names, or numbers. When you are done, no document may reference the
>   replaced content anywhere — stale prose is the most common consistency failure.
> - A change aimed at one document (e.g. "more workspace on the worksheet", "add a column to the
>   observation grid") goes in that document's `sections` — never by forking a `shared` key into
>   two variants.
> - Styling: `theme` fields (`primary`, `title_size`, `body_size`) apply to every artifact.
>   Artifacts use minimal color so they print cleanly in black-and-white; do not set
>   per-section or per-phase colors.

The differentiation skill states its own bidirectional check explicitly. `k12-lesson-differentiation/SKILL.md`
lines 257 to 276, verbatim:

> **Pre-write cross-check — run ALL checks before calling the render script. Do not render until every item passes.**
>
> **O6 — Artifact alignment (both directions):**
> 1. **Plan → tier documents.** List every task the plan says students do — tier problems/tasks,
>    exit ticket, the anchor activity, anything assigned to "early finishers." Each must have a
>    printed student-facing block on at least one tier document (the anchor activity on all
>    three, via `from_shared: anchor_activity`). A task that exists only as a plan description
>    fails.
> 2. **Tier documents → plan.** For each tier document, list every printed task — each
>    problem/task, the extension and each of its printed sub-parts, anything printed on one tier
>    only, the exit ticket, "If you finish early," "Reflect." Each must appear in that tier's
>    **Worksheet tasks** line in the plan, with its scaffold named (e.g., "P1 (tape diagram +
>    sentence support)" not just "P1"). A printed task the plan never names fails — a named
>    scaffold the worksheet does not print fails — and so does a plan line naming a task or
>    organizer no tier document prints.
>
> Shared content is guaranteed by `from_shared` blocks; the check targets document-specific
> blocks and plan prose. Also confirm the exact `shared.standard_code` string appears in each of
> the three tier documents' `eyebrow` (`"[Grade] [Subject] · [standard_code]"`) — the standard
> must be named on every tier, not only in the teacher plan. Fix mismatches before rendering.

**Measured, this project's own measurement.** No script in either skill's `scripts/`
directory performs any of these checks. `render_lesson_docx.emit_block` (lines 568 to 576,
quoted in `k12-block-types.md`) dispatches on block type and falls back to plain prose; there
is no arithmetic on `minutes`, no cross-document scan, and no coverage test anywhere in the
render path. These invariants are author-enforced only.

---

## 8 · The turn protocol

### 8.1 Step sequence, planning skill

Step headings verbatim from `k12-lesson-planning/SKILL.md`, with their line numbers:

- line 44: `## Step 0 — Route (silent, before anything else)`
- line 81: `## Step 1 — Clarify`
- line 94: `## Step 2 — Ground in standards`
- line 108: `## Step 3 — Build the lesson`
- line 116: `## Copyright guardrail`
- line 131: `## Step 4 — The draft offer`
- line 178: `## Step 5 — Output (one turn)`
- line 308: `### 5a. Write the complete `lesson.json` (same turn)`
- line 406: `### 5b. Render every Word document — one command, same turn`
- line 427: `### 5c. The satisfaction ask + iteration options (every output turn)`
- line 444: `### 5d. Revisions — one edit, every artifact stays in sync`
- line 465: `### 5e. Supplementary artifacts in their best format`

Step 0 has three numbered parts: **Subject** (route to the reference file), **Curriculum**,
**Connector**. SKILL.md line 75 to 78, verbatim:

> 3. **Connector.** Check whether the Learning Commons Knowledge Graph tools (e.g.
>    `find_standard_statement`) are available in this conversation. This decides which path
>    Step 2 takes. The skill is fully functional without the connector.

Step 1, SKILL.md lines 83 to 90, verbatim:

> Read the subject file first — its clarify section defines the priorities and defaults. We
> usually ask 0–2 clarifying questions — your judgment on what's relevant; the subject
> file's priorities rank which missing answers matter most. Apply the defaults silently for
> everything you don't ask about.
>
> The **draft offer** (see *Step 4 — The draft offer* below) travels with this message's questions
> as its own separate question — output logistics, not lesson content, so it doesn't count
> toward the 0–2. When nothing needs clarifying, the offer is asked on its own.

### 8.2 The draft offer, SKILL.md lines 138 to 146, verbatim

> - Question: *Should I go ahead and build the full classroom-ready packet (lesson plan + student materials, as
>   editable Word docs), or do you want to see a quick draft first?*
> - Options: **Go ahead and build it** · **Quick draft first** — the lesson at a glance,
>   right here in chat
>
> **The full packet is the default.** Declining, not answering, or anything like "proceed
> with your defaults" runs Steps 2–3 and goes straight to Step 5; the draft happens only on
> a clear yes.
>
> **The draft (on a yes) is built on Steps 2–3, never instead of them.** Run Step 2 in
> full — every KG call, exactly as written — and Step 3 before sketching anything. A draft
> sketched without the Step 2 grounding is a critical failure, the same failure as skipping
> the KG on the full build.

Its six draft contents (lines 152 to 161) and the two follow-up options (lines 167 to 171),
verbatim:

> - one line naming the grade, topic, and the standard the lesson is anchored to (code plus
>   a gist of ten words or fewer);
> - a summary of at most 3 sentences (what students do and why it works for this class);
> - the sequence as one bullet per phase (name, minutes, one line of what happens);
> - the student work at a glance — the actual tasks students will do, enough for the
>   teacher to skim and judge coverage;
> - what the lesson assumes students already know — the prerequisite skills or key
>   vocabulary in play — so the teacher can catch a mismatch with where their class is;
> - the exit ticket
>
> - **Make changes** — adjust any part of the draft
> - **Create the materials** — lesson plan, student materials, and observation template, as
>   editable Word documents

### 8.3 The one-turn output rule and the presentation order

SKILL.md line 178 to 181, verbatim:

> ## Step 5 — Output (one turn)
>
> Runs immediately when the teacher chose the full packet, or in the turn the draft is
> approved.

SKILL.md lines 416 to 423, verbatim (the enumerate-and-present protocol):

> Then list `$OUTPUT_DIR`
> and confirm every document has both its `.docx` and `.html`; if either is missing or tiny,
> rerun the script. Present the Word documents to the teacher together — attach the lesson plan
> last so it lands on top (chat surfaces stack newest-first). If there is no `student_materials`
> document, say so plainly ("This lesson is oral, so there's no student handout — students will
> work with …"). If the script errors, fix `lesson.json` (it is almost always malformed JSON)
> and rerun. If file generation fails entirely, say so clearly — do not silently fall back to a
> chat-only delivery.

### 8.4 The closing message, SKILL.md lines 427 to 442, verbatim

> End the turn with EXACTLY ONE closing message that does three things, in this order:
>
> 1. **If Materials names equipment the classroom has that a paper version can stand in
>    for** — coins, blocks, dice, a hundred chart — lead with a bolded offer to print it:
>    *"**This lesson uses base-ten blocks — want me to make a printable set in case
>    yours are short?**"* Anything whose content this lesson wrote — word cards, a
>    source excerpt, a sorting mat with this lesson's categories — already ships with
>    the package.
> 2. Asks whether the teacher is satisfied with **every artifact produced** or wants changes —
>    e.g. *"Take a look at the lesson plan, student materials, and observation template — anything
>    you'd like me to adjust?"* Do not skip the ask.
> 3. Offers 3–4 high-leverage, **specific** iteration options customized to the subject and
>    topic. Do not write "let me know if you want changes" — that's a non-offer. For example,
>    for a 3–5 ELA reading comprehension lesson: *"Would you like to (1) add more scaffolds for
>    English learners, (2) differentiate by proficiency level, or (3) adapt to be specific to
>    your state standards?"*

### 8.5 The plain-language rule

SKILL.md lines 202 to 210, verbatim:

> **Plain language with the teacher.** The machinery above is invisible to the teacher: never
> mention JSON, HTML, schemas, scripts, rendering, file names (`lesson.json`), or code in any
> teacher-facing message — and never link or name the `.html` files the render command also
> writes. Say *"Here's your lesson plan — the student materials and observation template are on
> their way"*, not *"I've rendered lesson.json"*. The only format word in your prose is
> "Word document". This
> applies to every turn: presenting artifacts, the satisfaction ask, revision summaries, and
> error messages (if generation fails, say the documents couldn't be created — not that a
> script or JSON failed).

### 8.6 The do-not-read-the-scripts rule

SKILL.md lines 195 to 200, verbatim:

> Never write layout code, never re-type lesson content into another format, and never edit a
> generated document directly — every change goes into `lesson.json` and is re-rendered
> (re-rendering is instant). **Do not open, cat, head, or grep the renderer scripts** — their
> behavior is fully specified by the commands and output paths in §5a–5d, and
> `references/example_lesson.json` is the complete schema. Reading script source tells you
> nothing this file doesn't already state.

Line 352, verbatim: "**Schema** — sufficient on its own; do not read any other file for the schema:"

**This claim is measurably false** in three respects documented in this sources/ directory:
the schema fence omits five canonical block types and two names it publishes are aliases
(see `k12-block-types.md`); the SKILL.md facet-order sentence contradicts the code (see §2.4
above); and `fill_table` accepts `rows` and `cols` the fence does not publish (see §4.2).

### 8.7 Copyright guardrail, SKILL.md lines 116 to 127, verbatim

> ## Copyright guardrail
>
> Always write original content. KG curriculum materials inform structure, scope, text
> selection, phenomenon selection, problem context, and lesson-arc design only — never
> reproduce student-facing text, teacher notes, comprehension questions, investigation
> prompts, discussion questions, activity narratives, or problem contexts verbatim from KG
> curriculum materials.
>
> If the loaded reference identifies a source curriculum (e.g., IM for math, OpenSciEd for science) and the teacher is not curriculum-confirmed for it, never name
> that curriculum anywhere in the output or in any chat message — not in headers, footnotes,
> rationale sections, facilitation notes, or your message presenting the artifacts. The KG
> data informs the design without being cited.

The differentiation skill's Step 0.2 states the curriculum-confirmation test. Its SKILL.md
lines 61 to 69, verbatim:

> **Curriculum is confirmed when:** the teacher explicitly names it, OR the uploaded source
> lesson references it (a lesson from an IM unit or an OpenSciEd unit
> counts — the upload is implicit confirmation).
>
> **If curriculum is NOT confirmed** (not detectable from upload or link, no explicit mention):
> never name a specific module, unit number, lesson number, or proprietary routine name anywhere
> in the output OR in any chat message — even if you recognize the routine from training.
> Describe the instructional move in your own generic terms ("a compare-strategies
> discussion", not the routine's trademarked name). This is a hard rule; violating it fails P9,
> and chat messages count.

---

## 9 · What the plugin does NOT produce

`k12-lesson-planning/SKILL.md` frontmatter `description`, line 4, the exclusion sentence
verbatim in its surrounding context:

> Use when a K-12 teacher needs a math, ELA, science, or social studies lesson built from scratch — even if grade, subject, or topic isn't yet stated. Do NOT load for grading, a rubric, assessment feedback, a quiz, or a standards lookup — answer those directly.

The same frontmatter, later in line 4, verbatim:

> A new lesson that asks for differentiated, tiered, or leveled materials is still ONE planning request — this skill produces those materials inside the lesson package; do not also invoke k12-lesson-differentiation. Not for differentiating an existing lesson (use k12-lesson-differentiation) or passage rewrites.

`k12-lesson-differentiation/SKILL.md` frontmatter `description`, line 3, the corresponding
exclusion verbatim:

> This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-planning's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.

**Measured, this project's own measurement.** The plugin ships exactly two skills, listed by
directory: `plugin/skills/k12-lesson-planning/` and `plugin/skills/k12-lesson-differentiation/`.
Neither produces a quiz, an exam, a rubric, an answer key, or a multi-day progression.
Searching the two `SKILL.md` files and all ten `references/*.md` files, no `documents[]` id
other than `lesson_plan`, `student_materials`, `observation_template`, `source_packet`,
`hint_cards` (example only), `teacher_plan`, `worksheet_group_a`, `worksheet_group_b`,
`worksheet_group_c` is named anywhere. `render_documents.py` imposes no id whitelist: any id
string renders.

### 9.1 The differentiation skill's fixed four-document set

`k12-lesson-differentiation/SKILL.md` lines 219 to 225, verbatim:

> Four artifacts — **1 teacher-facing plan + 3 student tier documents (below / at / above)** —
> are all rendered by a bundled script from **one `differentiation.json` (the material source)**. Anything that
> appears in more than one artifact (standard, problem/task set, exit ticket, vocabulary,
> sentence supports, misconceptions) lives ONCE in the JSON's `shared` block and is pulled into
> each document with `{"type": "from_shared", "key": …}` blocks, so the teacher plan and the
> tier documents cannot drift apart — and R6 (same context, same core tasks across tiers) is
> enforced structurally.

Its `documents[]` id field is an ENUM in the schema fence, unlike the planning skill's.
`k12-lesson-differentiation/SKILL.md` lines 321 to 323, verbatim:

```
documents[]: {id: teacher_plan|worksheet_group_a|worksheet_group_b|worksheet_group_c,
              audience: teacher|student, eyebrow, title, meta,
              sections[]: {heading, blocks[]}}
```

Its teacher_plan section headings, from `k12-lesson-differentiation/references/math.md`
lines 221 to 279, byte-exact in file order: `Learning Objective`, `Differentiation Overview`,
`Tier Design`, `Formative Check`, `Anchor Activity`, `Flexible Grouping`, `Why this works (1)`,
`Why this works (2)`, `Next Steps`. Note the Title Case, which conflicts with the planning
skill's "Headings use sentence case" density rule; the two skills do not share heading
conventions.

Its worksheet section headings, same file lines 289 to 316, byte-exact: `Vocabulary`,
`If you finish early`, `Reflect`, plus the per-problem blocks and any tier-only add-on
sections between them.

### 9.2 The MCP servers the plugin declares

`plugin/.mcp.json`, whole file, verbatim:

```json
{
  "mcpServers": {
    "ASSISTments": { "type": "http", "url": "https://mcp.assistments.org/mcp" },
    "Brisk Teaching": { "type": "http", "url": "https://mcp.briskteaching.com/mcp" },
    "Canva": { "type": "http", "url": "https://mcp.canva.com/mcp" },
    "Coteach": { "type": "http", "url": "https://coteach.ai/api/mcp" },
    "Diffit": { "type": "http", "url": "https://api.diffit.me/mcp" },
    "Eedi": { "type": "http", "url": "https://teacher-tools.eedi.ai/mcp" },
    "MagicSchool": { "type": "http", "url": "https://app.magicschool.ai/api/mcp" },
    "Snorkl": { "type": "http", "url": "https://api.snorkl.app/mcp" },
    "TeachFX": { "type": "http", "url": "https://api.teachfx.com/mcp" }
  }
}
```

Nine third-party HTTP MCP servers. None of them is the Learning Commons Knowledge Graph:
that connector is separate and is not declared in this file. **Measured in this session:**
eight of the nine (all but ASSISTments) reported as requiring OAuth authorization before
their tools can be used, and no OAuth flow was run. Their URLs are recorded above as
declared; none was fetched, so no HTTP status exists for any of them.

`plugin.json` `description` claims "Skills and MCPs for K-12 Education", and the two skills'
own instructions never call any of these nine servers. The only tool names either SKILL.md
references are the Learning Commons ones (`find_standard_statement` and the rest), which are
covered in `k12-grounding-and-render.md`.

---

## 10 · Files read for this extract

All under `k12-teacher-skills/` unless noted, all read in
full unless a line range is given:

- `plugin/.claude-plugin/plugin.json`, `plugin/.claude-plugin/marketplace.json`, `plugin/.mcp.json`
- `NOTICE`, `LICENSE` (identifying lines and appendix tail)
- `plugin/skills/k12-lesson-planning/SKILL.md` (471 lines)
- `plugin/skills/k12-lesson-differentiation/SKILL.md` (503 lines)
- `plugin/skills/k12-lesson-planning/references/math.md` (161), `ela.md` (227), `science.md` (182), `social_studies.md` (200), `learning-commons-kg.md` (108), `NOTICE`
- `plugin/skills/k12-lesson-planning/references/example_lesson.json` (667 lines, parsed structurally; the observation_template, exit_sort and exit_ticket values reproduced verbatim)
- `plugin/skills/k12-lesson-planning/scripts/lesson_common.py` (763), `render_documents.py` (108), `render_all.sh` (44), `render_lesson_docx.py` (636, targeted ranges), `render_lesson_html.py` (331, targeted ranges)
- `plugin/skills/k12-lesson-differentiation/references/math.md` (326, outline plus lines 207 to 320), `learning-commons-kg.md` (136, lines 1 to 60), `NOTICE`
- `~/.claude/plugins/cache/k12-teacher-skills/k12-teacher-skills/0.6.0/skills/k12-lesson-planning/SKILL.md` and the whole 0.6.0 tree, compared by `diff -r -q`

Not read in full, and therefore not a basis for any claim here:
`k12-lesson-differentiation/references/ela.md` (380), `science.md` (362), `social_studies.md`
(331), `example_differentiation.json` (518), and the four
`evals/*/rubrics/*.csv` files in the fork.
