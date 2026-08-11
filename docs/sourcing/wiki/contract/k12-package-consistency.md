---
title: "Package consistency invariants"
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-block-types.md
  - sources/k12-grounding-and-render.md
updated: 2026-08-08
---

# Package consistency invariants

## Summary

`k12-lesson-planning` publishes two blocks of cross-document requirements, "Everything matches"
and "Document integrity". Between them they demand that materials and phases agree in both
directions, that a task worded twice is worded identically, that phase minutes sum exactly to
the stated period, that exit-ticket sort buckets partition the answers, and that every
computation in the package was actually worked.

**No script in either skill checks any of it.** Measured: `render_lesson_docx.emit_block`
dispatches on block type and falls back to plain prose. There is no arithmetic on `minutes`, no
cross-document scan, and no coverage test anywhere in the render path. These invariants are
author-enforced only, and the renderer's failure behaviour is to print something rather than to
stop.

Two structural facts make that worse rather than neutral:

1. The strongest statement of the bidirectional alignment check, O6, is in the **sibling** skill
   `k12-lesson-differentiation`, not in the planning skill. A planning author who reads only
   their own `SKILL.md` gets the weaker prose form.
2. Three renderer behaviours silently absorb exactly the errors these invariants describe: an
   unregistered `shared` key renders nothing, an unknown block type prints its text as prose or
   vanishes, and two document ids that sanitize to the same filename overwrite each other.

## When to reach for it

Reach for it as the pre-render pass, after the `lesson.json` is written and before
`render_all.sh` runs. That is where the vendor puts the differentiation skill's check: "run ALL
checks before calling the render script. Do not render until every item passes."

Reach for it after any revision. §5d calls stale prose "the most common consistency failure".

Reach for it when a package spans more than the three-document minimum. Every extra document is
another surface these invariants must hold across, and none of them is checked.

Do not reach for it for how much text goes in one block, which is [[k12-density-rules]], or for
whether the render produced files, which is [[k12-render-invocation]]. This page is about
whether the parts agree with each other.

## How it works

### "Everything matches", verbatim, `SKILL.md` lines 237 to 263

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

### "Document integrity", the arithmetic and verification half, `SKILL.md` lines 284 to 306

The block opens, verbatim: "**Document integrity.** Every document is finished prose a teacher
hands out or works from:". Its four load-bearing bullets, verbatim:

> - Every in-document reference points at something that exists in the package: "jot it in the
>   table below" means that table is on the page; an exit ticket collected separately prints as
>   its own piece; a reference table uses the same numbers as the problems it supports.
> - Materials and the lesson match both ways: each listed item is used somewhere in the
>   lesson, every item any section sends students to — phases and extensions alike — appears
>   in Materials, and anything students read is printed in the package or named by its exact
>   title. Offers and pointers to the chat conversation stay out
>   of documents entirely.
> - Phase minutes include the transitions they cause (handing out, regrouping, collecting), at
>   a pace real students of this grade manage, and the phases sum to exactly the stated
>   period — transition time lives inside the phases, never as invisible buffer.
> - Verify every computation by working it — answer keys, worked examples, and any quantitative
>   chain the lesson builds on (an energy pyramid's levels, a ratio table's entries, a coin
>   total) produce the numbers the materials state.

The minutes rule appears a second time in the block table. `SKILL.md` line 395, verbatim in
part: "the lesson-sequence phases use `phase_header`, which renders as h2 with minutes; the
`minutes` across all phase headers should sum to `shared.duration`."

### O6, the bidirectional check, stated only in the differentiation skill

`k12-lesson-differentiation/SKILL.md` lines 257 to 276, verbatim in part:

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

That block also states its own scope limit, verbatim: "Shared content is guaranteed by
`from_shared` blocks; the check targets document-specific blocks and plan prose."

The planning skill has no equivalent numbered check. Its nearest statement is the prose bullet
"A task worded in two places ... uses identical wording in both", which is one direction only.
This project's design spec files the two-direction form as trap 16 and the minutes rule as trap
18, and those are this project's framing rather than the planning skill's.

### Revisions, `SKILL.md` lines 444 to 461, verbatim in part

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

The third rule is the one that protects the second: forking a `shared` key into per-document
variants is how a package acquires two versions of one task that then drift.

## In practice

### The checkable list, and who checks it

| Invariant | Enforced by | What a violation looks like |
|---|---|---|
| Every Materials item used by a named phase | author | An item on the list that no phase touches |
| Every item a phase sends students to appears in Materials | author | A phase naming cards the list omits |
| A counted set matches its enumeration | author | "Picture cards, 18" over a list of 16 |
| A task worded twice is worded identically | `from_shared` when registered; author otherwise | Plan says "price per bag", worksheet says "unit price" |
| Every plan task has a printed student block | author | A task that exists only as plan prose |
| Every printed task is named in the plan | author | A worksheet problem the plan never mentions |
| Phase minutes sum exactly to `shared.duration` | author | 8 + 15 + 12 + 5 + 5 against a stated 50 |
| Sort buckets partition the answers | author | A response that fits two buckets or none |
| An answer space mirrors its ask | author | Three rows under a prompt asking for four |
| Every computation verified by working it | author | A ratio table whose entries were not checked |
| In-document references point at something present | author | "the table below" with no table |

The only row with any structural guarantee is the wording one, and only for content that
actually went through `shared`. Everything else is a reading pass.

### Register once, then sweep

The mechanism that removes the largest class of drift is [[k12-shared-registry]]: anything
appearing on more than one page is registered once and pulled with
`{"type": "from_shared", "key": …}`, so the copies cannot diverge. The residue after that is
prose, and prose is exactly what §5d's consistency sweep targets. Treat the sweep as mandatory
after any change to context, names or numbers, not as a courtesy.

### Run the minutes arithmetic by hand, every time

`shared.duration` is one of the eight identity keys, so a `from_shared: duration` pull renders
as a bare paragraph of its `str()`. It is never compared against anything. Sum the
`phase_header` minutes yourself and read the total against `duration`. Transitions live inside
the phases, so a package that sums to less than the period is not "leaving room", it is wrong
by the vendor's own rule.

### Escalate the exit-ticket bar through the package

`references/math.md` line 95 sets the exit ticket at the structurally hardest enumerated case,
picked with the misconception test: a student holding the lesson's primary anticipated
misconception must get it wrong. This project's design spec files that bar as trap 17 and
extends it: no quiz or exam item may read easier than the exit ticket. That extension is this
project's ruling, not the plugin's, and it is recorded on [[k12-assessment-gap]].

## Gotchas & constraints

**1. The toolchain is not a safety net, and it is shaped to hide these errors.** Three
behaviours, all measured from the staged code:

- A `from_shared` pull at a key that is missing, `None`, `""` or `[]` returns an empty block
  list. No exception, no placeholder, no log. The section renders one block shorter.
- An unrecognised block type is not an error. `emit_block` misses the lookup, then prints
  `blk["text"]` as a bare paragraph, or `blk["items"]` as bullets, or nothing. A `data_tbale`
  typo carrying only `rows` prints nothing, so the table vanishes with no error and no log line.
- Two `documents[]` ids that sanitize to the same filename overwrite each other unconditionally,
  so the file count can be lower than the `documents[]` count.

**2. O6 lives in the other skill.** The planning skill's own text gives one direction. Anyone
running a planning-skill package against a two-direction check is applying the differentiation
skill's rule, and should say so rather than attribute it to `k12-lesson-planning`.

**3. Blocks that print are not always the blocks you wrote.** Four repair passes run on every
document after `from_shared` expansion: enumeration-break insertion, pipe-table conversion,
inline-bullet splitting, and prompt-plus-workspace grouping. A fifth, conditional pass appends a
sentence the author never wrote, verbatim `*The symbol ■ stands for the unknown number.*`, when
that character appears undefined. A consistency check against the JSON is not a check against
the printed page. See [[k12-block-types]].

**4. "Identical wording in both" is stricter than it sounds on a teacher page.** The plan's copy
of a student prompt renders as a `labeled` block labelled `Students see`, but only when the
facet's blocks are all `paragraph` or `list`; a `callout`-shaped facet renders raw instead. The
same registered content appears in two different frames, and only the words are guaranteed to
match.

**5. A grounding failure passes every one of these checks.** If the standard lookup returned
nothing, `shared.standard` produces no callout and the package still renders complete. Nothing
here asks whether the standard is present. See [[trap-empty-facet-reads-as-success]].

**6. `audience` is checked two different ways.** `expand_document` branches on
`audience != "teacher"`, while `theme.student_doc` is a strict equality against `"student"`, so
a document can render its student facets while keeping teacher-page row heights. Write the
literal strings.

**7. Unverified from here: none of this was observed at render time.** No render was executed as
part of the staged extracts. The claim that no script performs these checks rests on reading
`scripts/` in full, which the extracts record doing, not on watching a violating package render.
What would close it: render a package with deliberately unbalanced phase minutes and confirm
exit 0.

## Related

- [[k12-document-set]] holds the `documents[]` contract these invariants hold across.
- [[k12-shared-registry]] is the one structural defence: a registered task cannot drift.
- [[k12-block-types]] holds the repair passes and the unknown-type fallback behind gotchas 1
  and 3.
- [[k12-density-rules]] is the sibling rule set: how much goes in a block.
- [[k12-lesson-plan-sections]] holds the phase structure whose minutes must sum, and the
  practice-set coverage rule the plan-to-worksheet direction depends on.
- [[k12-student-materials]] and [[k12-observation-template]] are the documents the plan is
  checked against.
- [[k12-render-invocation]] is the next step, and why a clean render proves nothing about
  delivery.
- [[k12-assessment-gap]] carries this project's extension of the exit-ticket bar to quizzes and
  exams.
- [[trap-empty-facet-reads-as-success]] is the worked failure behind gotcha 5.

## Composes with

- [[practice-format-a-lesson-package]] runs this list as its pre-render gate.
- [[practice-format-an-assessment-artifact]] inherits it, because an assessment authored as
  ordinary `documents[]` entries is subject to every invariant above and to no additional
  checking either.

## References

Staged extracts in this wiki, all staged 2026-08-08 from local files read at 2026-08-07 21:15
PDT. Local files, so no HTTP status exists.

- `sources/k12-plugin-contract.md`, primary. §7 the "Everything matches" block verbatim
  (`SKILL.md` 237 to 263), "Document integrity" verbatim (284 to 306), the line 395
  phase-minutes restatement, §5d (444 to 461), the differentiation O6 block (257 to 276), and
  the measurement that no script in either `scripts/` directory performs any of these checks.
- `sources/k12-block-types.md`, primary. §6 the unknown-type fallback in both renderers; §7 the
  four repair passes and the conditional unknown-symbol append.
- `sources/k12-grounding-and-render.md`, primary. §3.1 the silent empty-key return; §3.4
  `_facet_text` and the callout case; §3.5 the two `audience` tests; §4.3(d) the id sanitization
  and the overwrite on collision.

This project's own working file, cited as this project's measurement and not as any outside
party's statement: `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §7 Tier 3 traps
16, 17 and 18.

Underlying vendor files, cited as the staged extracts cite them, under
`k12-teacher-skills/plugin/skills/`: `k12-lesson-planning/SKILL.md`, `references/math.md`,
`scripts/lesson_common.py`, `scripts/render_lesson_docx.py`, `scripts/render_lesson_html.py`,
and `k12-lesson-differentiation/SKILL.md`. Plugin 0.6.0, measured byte-identical to the
installed copy.
