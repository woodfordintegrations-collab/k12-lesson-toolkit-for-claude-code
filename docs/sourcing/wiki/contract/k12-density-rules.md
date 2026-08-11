---
title: "Density and quotation limits"
type: contract
sources:
  - sources/k12-plugin-contract.md
  - sources/verdict-twelve-host-table.md
  - sources/k12-block-types.md
updated: 2026-08-08
---

# Density and quotation limits

## Summary

`k12-lesson-planning` publishes an eight-bullet block of hard limits on how much text goes in a
block: paragraph length, bullet length, where parallel variants go, how many callouts a phase
may carry, one instruction in one place, sentence-case headings, a half-page ceiling on
continuous prose.

Seven of the eight are legibility rules. The eighth is not. **Quote the standard verbatim
exactly once** is the rule this project's whole licensing layer hangs on, because the mandated
NGA/CCSSO notice and the Learning Commons per-record attribution attach to that one quotation
and to nothing else. Multiply the quotation across five documents and you have multiplied an
attribution obligation, not just added words.

Two further facts a package author has to hold:

- The sibling skill `k12-lesson-differentiation` ships a **different** density block. Four rules
  differ, and the two skills share one renderer, so nothing at render time tells you which set
  you are under.
- Nothing enforces any of it. No length check, sentence counter or callout census exists
  anywhere in either skill's `scripts/`. Every rule here is author-enforced.

## When to reach for it

Reach for it before writing a `lesson.json`, and again before rendering, as the pass that asks
whether any block has grown past its cap.

Reach for it whenever a standard statement is about to be pasted into a document. That is the
moment the licensing obligation attaches, and the last section of this page is what you owe.

Reach for it when moving between the two skills, because their blocks are similar enough to read
as identical and are not.

Do not reach for it for which block type to use, which is [[k12-block-types]], or for
cross-document agreement, which is [[k12-package-consistency]]. Density is how much goes in one
block; "everything matches" is whether two blocks agree.

## How it works

### The planning skill's block, verbatim, `SKILL.md` lines 212 to 236

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

### The differentiation skill's block, verbatim, its `SKILL.md` lines 240 to 255

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

### The differences, measured by comparing the two blocks

| Rule | Planning | Differentiation |
|---|---|---|
| 3-sentence paragraph cap | yes | yes |
| Bullets as 15-word fragments | yes | yes |
| Parallel variants in ONE table, 25 words per cell | yes, "variants" | yes, "tiers" |
| Quote the standard verbatim exactly once | yes | yes |
| Half-page restructure ceiling | yes | yes |
| Headings use sentence case | yes | absent |
| "Write like a colleague's note" | yes | absent |
| At most one or two callouts in a phase | yes | absent |
| Each instruction in exactly one place | yes | absent |
| An aside longer than one sentence becomes a callout | absent | yes |

The last two rows are the pair that actually conflicts in practice. The planning skill caps
callouts per phase and sends teacher asides to `labeled` or `instructions` blocks; the
differentiation skill promotes any aside longer than one sentence into a callout.

## In practice

### The checkable form

| Cap | Value as published | Applies to |
|---|---|---|
| Paragraph or labeled block | at most 3 sentences | every document |
| Bullet item | one idea, about 15 words or fewer | every document |
| Table cell in a parallel-variant table | about 25 words or fewer | every document |
| Callouts in one phase | at most one or two | planning skill only |
| Continuous prose in one section | about half a page | every document |
| Verbatim standard quotations in the whole package | exactly 1 | every document |
| Gist length for every later mention of a standard | ten words or fewer | every document |

"About" and "at most" are the vendor's own hedges. `≤ ~15 words` and `≤ ~25 words` are byte
exact from the source; do not harden them into a counted rule and then report a package as
failing it.

### Only the sibling skill publishes a page or word budget

`k12-lesson-differentiation/references/math.md` line 207, verbatim:
"### Document content — teacher plan (`id: teacher_plan`) — max 3 pages", with a stated budget
at lines 209 to 213 of "**Length budget: ~1,200 words rendered (the 3-page cap in practice).**"
The planning skill publishes no page or word budget for any document. Its only length control is
the half-page-per-section ceiling above.

### The heading-case rule does not survive the trip to the sibling skill

Planning: "Headings use sentence case". The differentiation skill's own `teacher_plan` section
headings, byte-exact in file order from its `references/math.md` lines 221 to 279, are
`Learning Objective`, `Differentiation Overview`, `Tier Design`, `Formative Check`,
`Anchor Activity`, `Flexible Grouping`, `Why this works (1)`, `Why this works (2)`,
`Next Steps`. That is Title Case, from the vendor, against the other skill's stated rule.
Copying a heading list across is a defect.

### Structure beats prose is partly enforced by a repair pass, not by you

Three render-time rewrites turn prose these rules discourage into the structure they prefer: a
markdown pipe-table run inside a text block becomes a real `table`, a prose block with
bullet-marked lines is split into prose plus a `list`, and mid-prose `(a)` or `(2)` enumerations
get a newline inserted. They are a legibility safety net, not a licence to write walls of text.
Documented in full on [[k12-block-types]].

### Quote the standard verbatim exactly once, and what attaches to that one quotation

This is the last rule in the block and the one with consequences outside the document.

**The mechanism.** `lesson_common.expand_from_shared` treats `standard` as the only special
key. Verbatim from the staged code:

```python
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
        return [{"type": "callout", "kind": "special",
                 "label": f"{shared.get('standard_code', '')} — Target standard".strip(" —"),
                 "text": shared.get("standard_text", "")}]
```

One key, one callout, one place the statement text can enter a document. Every subject file
repeats the rule in its own section 1, and this project's design spec files it as trap 15.

**The obligation.** Two notices attach to that quotation, and this project's adjudication says
to ship both. The NGA/CCSSO notice is mandated verbatim by the Common Core public licence, and
the staged verdict record gives it as:

```
Common Core State Standards
© Copyright 2010. National Governors Association Center for Best Practices and
Council of Chief State School Officers. All rights reserved.
http://www.corestandards.org/
```

That record notes the mandating sentence, "Any publication or public display shall include the
following notice...", was verified via a Wayback snapshot dated 2025-12-21 because the live page
is Cloudflare 403 bot-blocked as of 2026-08-08.

The second notice is the Learning Commons per-record statement, and **there is no single
string**. The staged record carries four forms, selected by which record was actually cited:
Multi-State CCSS, California, Achievement Network learning components, and lesson metadata. Use
the one attached to the record you quoted. See [[concept-attribution-per-record]] and
[[source-corestandards-nga-ccsso]].

**Why once matters.** One quotation is one attribution site. Paste the statement into the lesson
plan, the worksheet and the observation template and the notice obligation follows it to all
three, leaving three places to keep in sync and three to get wrong. Registering it once in
`shared` and pulling it once is what makes the obligation tractable. The licence position on the
surrounding curriculum prose is a separate question; see [[license-cc-by]] and
[[concept-cite-quote-adapt]].

## Gotchas & constraints

**1. No script checks any of this.** Measured: no length check, sentence counter, callout census
or word budget exists anywhere in either skill's `scripts/`. A package violating every rule on
this page renders cleanly and exits 0.

**2. The two skills' blocks differ and nothing announces it.** Four rules present in one are
absent from the other, and the callout rules point opposite ways. An author who learned density
on one skill and applies it on the other is wrong in a direction that looks like care.

**3. "Exactly once" is about the package, not the document.** One verbatim quote across the
whole set, not one per document. Pulling `from_shared: standard` into two documents of the same
package breaks it. `SKILL.md` separately says to pull each key once within a document, which is
a weaker and different rule.

**4. A code-only `shared` produces a labelled box with no statement.** With `standard_code`
present and `standard_text` absent the callout still renders, `text` empty. A lesson whose
standard lookup failed entirely produces no target-standard callout at all and still renders a
complete-looking package. See [[trap-empty-facet-reads-as-success]].

**5. The ten-word gist is a paraphrase and carries its own risk.** It is an editorial act, not
covered by the notice attached to the verbatim quotation, and a gist that misstates the standard
is a content defect this project owns. Write gists from the statement you quoted, not from
memory.

**6. Sentence case is a rule about your headings, not about quoted text.** Restyling the case of
a standard statement, a bucket label or any other quoted string to satisfy a heading rule is
falsification. The rule reaches document headings only.

**7. Unverified from here: the NGA/CCSSO live page.** This project's record states it was
Cloudflare 403 bot-blocked as of 2026-08-08 and the mandating sentence was read from a Wayback
snapshot dated 2025-12-21. What would close it: a successful fetch of the live public licence
page with the notice pasted from raw bytes. The admissibility rule that makes the archive
provenance something to state rather than to omit is [[trap-summary-layer-is-not-evidence]].

## Related

- [[k12-block-types]] holds the vocabulary these caps apply to and the repair passes that
  restructure prose after you write it.
- [[k12-shared-registry]] holds the `standard` special key that makes one quotation reachable
  from many documents.
- [[k12-package-consistency]] is the sibling rule set: whether two blocks agree.
- [[k12-lesson-plan-sections]] is where the single verbatim quotation sits, in `At a glance`.
- [[license-cc-by]] holds the attribution regime the standards data is served under.
- [[source-corestandards-nga-ccsso]] is the rights holder of the standards text and the source of
  the mandated notice.
- [[concept-attribution-per-record]] is why there is no single Learning Commons string.
- [[concept-cite-quote-adapt]] separates quoting a standard from adapting prose around it.
- [[trap-empty-facet-reads-as-success]] covers the code-only and lookup-failed cases in gotcha 4.
- [[trap-summary-layer-is-not-evidence]] holds the admissibility rule (raw bytes, a URL, a
  status) that gotcha 7 reports against.

## Composes with

- [[practice-format-a-lesson-package]] runs these caps as an authoring pass, and is where the
  once-per-package quotation is placed.
- [[practice-assemble-an-attribution-block]] consumes the two notices this page's last section
  names, and is where the per-record string is selected.

## References

Staged extracts in this wiki, all staged 2026-08-08. The plugin extracts were read from local
files at 2026-08-07 21:15 PDT, so no HTTP status exists for them.

- `sources/k12-plugin-contract.md`, primary. §6 both density blocks verbatim and the measured
  differences; §6.1 the 3-page and ~1,200-word budgets; §2.3 the `standard` special key code;
  §3.1 the `math.md` line 82 fragment; §9.1 the `teacher_plan` Title Case heading list.
- `sources/verdict-twelve-host-table.md`, reference. §4.1 the mandated NGA/CCSSO notice, the
  Wayback verification date, the live 403, and all four Learning Commons per-record forms.
- `sources/k12-block-types.md`, primary. §7 the render-time repair passes.

This project's own working file, cited as this project's measurement and not as any outside
party's statement: `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §7 Tier 3 trap
15, which elevates the quote-once rule from a density bullet to a build trap.

Underlying vendor files, cited as the staged extracts cite them, under
`k12-teacher-skills/plugin/skills/`: `k12-lesson-planning/SKILL.md`, `references/math.md`,
`scripts/lesson_common.py`, `k12-lesson-differentiation/SKILL.md`, and its `references/math.md`.
Plugin version 0.6.0.
