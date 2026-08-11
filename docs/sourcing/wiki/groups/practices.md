---
title: "practice: the eight procedures"
type: group
updated: 2026-08-08
---

# practice

Eight procedures. Each one is a sequence of steps with its checks written **inside** the steps
rather than bolted on afterwards, because on this build almost every failure is silent: the call
returns, the render exits 0, the file looks finished.

You want this family when you know what you are allowed to do and need to do it: resolve a code,
ground a lesson, turn a host into a defensible verdict, format a package, ship a credit line. A
`concept` page tells you a credit line is per record; [[practice-assemble-an-attribution-block]] is
where you find out which block a given record needs.

The family runs on two tracks that meet once. The **grounding and formatting** track runs per
lesson and is where an ungrounded claim gets into a document. The **rights** track runs per host
and is where a wrong verdict gets into a bibliography. They meet at the end, in the attribution
block, which is the only procedure here whose failure is visible in the shipped artifact rather
than in a working note.

Two of these pages carry an honestly marked hole rather than a procedure.
[[practice-place-and-alt-text-a-figure]] cannot describe its palette-validation step against
tooling that exists, and says so instead of describing it as though it runs.

## Pick a procedure

**Ordering: by how many times the procedure runs in one build of this unit, most-run first.** The
last two run exactly once each, and running them early guarantees a re-run.

| Page | What error it prevents |
|---|---|
| [[practice-resolve-a-standard-code]] | Reading a zero-row result as "the store has no data for this standard". `G-SRT.6` and `HSG-SRT.6` both return 0 rows where `HSG-SRT.C.6` returns 4, and nothing in the response says so. |
| [[practice-ground-a-lesson-end-to-end]] | Finishing a complete-looking package whose grounded sections were quietly filled from the model's prior. Four of the seven tools return empty on every call. |
| [[practice-format-a-lesson-package]] | Writing a separate file per document, or repeating content across them, which disables the one mechanism keeping the pages identical after an edit. |
| [[practice-build-a-source-table]] | Recording a licence finding nobody can re-run. The bar is not "did you find the licence", it is whether someone who was not there lands on the same verdict. |
| [[practice-cite-without-redistributing]] | Dropping a `cite_only` source as unusable. Citation is unconstrained by every source in this corpus, and it carries most of what a build needs. |
| [[practice-place-and-alt-text-a-figure]] | Authoring a lesson as though a figure can be dropped into `lesson.json`. There is no image block, and a block the renderer does not know prints nothing at all. |
| [[practice-format-an-assessment-artifact]] | Five agents inventing five shapes for one instrument set, and printing an instrument-level tool or timing statement that silently invalidates specific items on a mixed paper. |
| [[practice-assemble-an-attribution-block]] | One hard-coded credit line over a package that drew on several hosts and several record classes. It is wrong in four independent ways at once. |

## Where this family ends

- What you are permitted to do before any of this runs: [[sources]] and [[licenses]].
- Why the procedure is shaped this way, stated once rather than per page: [[concepts]].
- The shape the formatting procedures are writing to: [[contracts]].
- The silent failure each check is defending against, worked in full: [[traps]].
