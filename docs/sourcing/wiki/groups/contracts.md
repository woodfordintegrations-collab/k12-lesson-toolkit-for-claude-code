---
title: "contract: the k12 artifact shape"
type: group
updated: 2026-08-08
---

# contract

Ten pages documenting what the `k12-teacher-skills` plugin actually publishes and what its code
actually does: how many documents a package has, where content lives so two pages cannot drift,
what a block may be, what each document's sections are, how much text fits in one, and what the
render command really hands back.

You want this family the moment a grounded lesson has to become files. It answers "what shape does
the artifact take", which is the third of the three questions this wiki exists to answer, and it is
the only family with nothing to do with rights.

**One property runs through every page and is the reason the family is this long: nothing enforces
any of it.** No id whitelist, no length check, no phase-minute arithmetic, no cross-document scan,
no coverage test anywhere in the render path. An unrecognised block type prints nothing. An
unregistered `shared` key returns an empty list with no warning. An unknown callout `kind` is
silently rewritten. A package that violates every invariant here renders cleanly and looks
finished. Every rule in this family is author-enforced, which makes reading it the enforcement.

**The vendor documentation is incomplete in ways it does not announce.** The lesson plan's sections
are not in `SKILL.md`. Two published block names are undocumented aliases and five canonical types
are published nowhere. The observation template's layout block names three shared pulls when the
worked example ships four. Where a page here contradicts the vendor prose, it is because the code
was read and the code governs what prints.

One page, [[k12-assessment-gap]], is half measurement and half this project's own design decision,
and it says which half is which. Nothing in that second half should ever be repeated as something
the plugin requires.

## Pick a page

**Ordering: the sequence of authoring one package**, from the first structural decision to the
check that the render actually delivered. Frequency does not separate these rows usefully, because
every package touches every one of them; what decides which page you want is where you are in the
file.

| Page | What error it prevents |
|---|---|
| [[k12-document-set]] | Reading the three-id minimum as an enum and hard-coding three documents per lesson, which prints a worksheet for an oral lesson and leaves nowhere to put an answer key. |
| [[k12-shared-registry]] | Copying content between documents instead of registering it once, which disables the only thing keeping two pages in step after a revision. A misspelled key renders empty with no warning. |
| [[k12-block-types]] | Assuming an unrecognised block type fails. A misspelled `data_tbale` prints nothing at all, with no error and no non-zero exit. |
| [[k12-lesson-plan-sections]] | Taking the five math sections from `SKILL.md`, which does not carry them, or carrying them into a science lesson, which ships seven with different names. |
| [[k12-student-materials]] | Always shipping a worksheet, and asserting the published `~115pt` writing-box height when `answer_profile()` returns `116.0`. |
| [[k12-observation-template]] | Following the layout block literally. It names three `from_shared` pulls; the exit-sort criteria live in a fourth key and never reach the teacher who is sorting the papers. |
| [[k12-density-rules]] | Multiplying the verbatim standard quotation across documents. Seven of the eight rules are legibility; the eighth multiplies an attribution obligation, not just words. |
| [[k12-package-consistency]] | Trusting a clean render as a consistency check. No script in either skill checks any of these invariants, and three renderer behaviours silently absorb exactly the errors they describe. |
| [[k12-render-invocation]] | Reading a populated output directory as delivery. Six distinguishable failures leave real files on disk, including one that writes HTML only and exits 1. |
| [[k12-assessment-gap]] | Citing quiz counts, exam structure, the ten-day arc or the `answer_key` id as part of the k12 contract. The plugin says nothing about any of them; this project decided, and that is a different authority. |

## Where this family ends

- The authoring procedure that consumes these shapes: [[practice-format-a-lesson-package]], and for instruments [[practice-format-an-assessment-artifact]].
- Getting the content to put in them: [[practice-ground-a-lesson-end-to-end]].
- Whether a figure may be placed at all, given that the renderer draws none: [[practice-place-and-alt-text-a-figure]].
- Whether the material may be reproduced in the first place: [[sources]], [[licenses]], [[concepts]].
