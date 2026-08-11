---
title: "Taxonomy: the seven entity types and the boundaries between them"
type: topic
sources:
  - CLAUDE.md
  - INVENTORY.md
  - meta/lint_config.py
  - meta/lint.py
  - meta/lint-report.md
  - meta/synthesis-brief.md
  - templates/page-template.md
  - the private workspace/machinery/skills/build-a-wiki/assets/page-template.md
  - wiki/source/source-im-kendall-hunt.md
  - wiki/license/license-sharealike.md
  - wiki/concept/concept-cite-quote-adapt.md
  - wiki/contract/k12-document-set.md
  - wiki/practice/practice-ground-a-lesson-end-to-end.md
  - wiki/trap/trap-code-form-silent-zero.md
  - wiki/evidence/evidence-store-ingest-boundary.md
updated: 2026-08-08
---

# Taxonomy: the seven entity types and the boundaries between them

CONFIG declares seven `entity_types`. Most rows assign themselves. The build's real cost sat in
four boundaries where two families both looked correct, and each of those four moved rows during
Gate 1 adjudication. This page is the assignment rule, the four boundary tests, and the map from
type to page profile.

## The seven types

| type | folder | pages | profile | the question one page answers | what puts a row here |
|---|---|---|---|---|---|
| `source` | `wiki/source/` | 16 | C | May I use what **this one host** serves, and what does its own page literally say? | a rights verdict scoped to a single host |
| `license` | `wiki/license/` | 8 | A | What does **this regime** do, wherever it appears? | host-independent terms: a licence or a rider |
| `concept` | `wiki/concept/` | 6 | A | What idea must a reader hold to reason correctly here? | load-bearing, and its absence produces visible confusion |
| `contract` | `wiki/contract/` | 10 | A | What **shape** must the artifact have? | a schema, a layout, an invariant, a vocabulary |
| `practice` | `wiki/practice/` | 8 | A | What do I do, in order? | a procedure a person executes |
| `trap` | `wiki/trap/` | 13 | A | What fails **without saying so**? | the silence test, below |
| `evidence` | `wiki/evidence/` | 5 | B | Is this claim supported, and by what measurement? | this project measured it, and the measurement is the point |

66 content pages. The seven family counts above were each re-counted on disk for this page rather
than copied from `INVENTORY.md`. `meta/lint-report.md`, generated 2026-08-07 over the content set
alone, records `pages_scanned: 66`, `status: PASS`, 0 errors, 0 warnings.

Structural pages sit alongside the content set and are not content: `wiki/index.md`,
`wiki/when-to-use.md`, and the family index pages under `wiki/groups/`. `meta/lint_config.py` names
`groups` and `topics` in `STRUCTURAL_DIRS`, which exempts them from the section and frontmatter
checks; `is_content()` in `lint.py` treats any page whose top-level folder is not a `CONTENT_TYPES`
key the same way. This page sits at the wiki **root** under `topics/`, outside the linter's walk
entirely, since `lint.py` walks only `OUTPUT_FOLDER`.

One naming exception, ruled and kept at Gate 1: **the `contract` family does not use its family
prefix.** All ten contract slugs are `k12-*`, not `contract-*`, because they name the vendor
contract rather than this wiki's taxonomy. Every other family self-prefixes. This is collision-safe
today and is the one place where a future row could collide without warning, since a `practice-*`
page about k12 output would be tempted by a `k12-*` slug.

## The three page profiles

The rule for a writer is exact titles, exact order, `## ` level. Note precisely what is machine
checked and what is not: `lint.py` reads the configured list for the page's type and asserts that
every title in it is **present** as an `## ` heading. It does not check their order, and it does not
reject an extra heading. Order and restraint are the written rule, enforced by review rather than by
the linter, so a page can pass lint with its sections shuffled.

**Profile A** (`license`, `concept`, `contract`, `practice`, `trap`), 45 pages:

```
## Summary
## When to reach for it
## How it works
## In practice
## Gotchas & constraints
## Related
## Composes with
## References
```

**Profile B** (`evidence`), 5 pages. It appraises a claim, so the middle pair differs:

```
## Summary
## When to reach for it
## The claim
## What the evidence shows
## Gotchas & constraints
## Related
## Composes with
## References
```

**Profile C** (`source`), 16 pages. It is a rights verdict about one host, and the reader arrives
with two questions, neither of which is "how does it work":

```
## Summary
## When to reach for it
## What its own page says
## What you may do with it
## Gotchas & constraints
## Related
## Composes with
## References
```

Measured across the built set: 45 pages carry `## How it works`, 5 carry `## The claim`, 16 carry
`## What its own page says`. That is 66, with no page carrying two middle pairs.

`source` pages alone require two extra frontmatter keys, `verdict` and `fetched`. `verdict` takes
one of `quote_and_adapt`, `quote_noncommercial`, `quote_sharealike`, `cite_only`, `do_not_use`. The
built distribution is 8 `cite_only`, 4 `quote_and_adapt`, 3 `quote_sharealike`, 1
`quote_noncommercial`. A licence claim with no fetch date is a memory, not a fact, which is why
`fetched` is structural rather than optional.

### The canonical template is stale. The linter config is the contract.

Both copies of the shipped page template, `templates/page-template.md` in this wiki and the
machinery original at `machinery/skills/build-a-wiki/assets/page-template.md`, carry this at line
23:

```
## Configuration / key details
```

**No page in this wiki uses that heading.** A grep across all 66 returns zero occurrences. All 45
Profile A pages use `## In practice` instead.

`meta/lint_config.py` says so in its own comment, and this is the authoritative statement:

```
# NOTE: "In practice", NOT "Configuration / key details". The shipped
# assets/page-template.md in machinery still says the latter and is stale against
# every wiki that actually exists; all 83 UDL pages use "In practice". Writing to
# the template instead of to this list makes the linter reject every page.
```

This wiki's `CLAUDE.md` gives the same instruction: "Write to that file, not to
`machinery/skills/build-a-wiki/assets/page-template.md`", "which still says
`## Configuration / key details` and is stale against every wiki that exists".

So the operative rule for any page-writer, and for anyone repairing a page later: **`SECTIONS`,
`EVIDENCE_SECTIONS` and `SOURCE_SECTIONS` in `meta/lint_config.py` are the contract. The template
is documentation, and it is wrong.** The failure is not subtle in effect but is easy to walk into:
a writer who follows the template produces a page the linter rejects on a missing section it will
name explicitly.

Note also that `lint_config.py` is the only wiki-specific file in `meta/`. `lint.py` beside it is a
shared engine, byte-identical across wikis and hash-locked by `lint.lock.json`. Editing the engine
is a deliberate, noisy act. Editing the config is the normal one.

## Boundary 1: `concept` versus `trap`, decided by the silence test

**The test.** If the broken behaviour and the correct behaviour produce the same-looking output, it
is a `trap`. If the idea is merely load-bearing, it is a `concept`.

The test is about the *observer*, not about the severity. A failure that raises, returns an error
string, or renders visibly differently is not a trap by this taxonomy however damaging it is,
because the reader will find it. A trap page exists precisely because nothing in the output will
ever tell the reader they are wrong.

**What it cost.** The `concept` family was drafted at 10 rows and adjudicated to 6. Four went, and
this test is why:

| cut row | absorbed by | the finding |
|---|---|---|
| `concept-standard-code-form` | `trap-code-form-silent-zero` | SILENT. "a near-miss code returns zero rows with no error" |
| `concept-verbatim-license-floor` | `trap-summary-layer-is-not-evidence`, `practice-build-a-source-table` | SILENT. The WebFetch summary returned the correct licence, "so nothing flagged it" |
| `concept-license-verdicts-expire` | `trap-license-withdrawn-after-citation`, `license-withdrawn-grants` | SILENT. "a stale citation renders identically to a fresh one" |
| `concept-silence-is-not-a-grant` | `license-unmarked-silence`, `trap-access-is-not-a-rights-fact` | Not the silence test by name. "Both halves were already owned, each better sourced. It was the thin middle." |

Three of the four carry `SILENT` verbatim in the adjudication record. The fourth fell to the
adjacent boundary: both of its halves were silences already owned by better-sourced pages, one in
`license` and one in `trap`. The arithmetic is the same either way. Ten drafted concepts, six
survivors, and the trap family took the difference.

**The residue, and why `concept` is the smallest Profile A family.** Once every silent failure has
been claimed by `trap`, what is left in `concept` is the ideas whose absence produces *visible*
confusion. `concept-cite-quote-adapt` is the model case: a reader who has collapsed cite, quote and
paraphrase-and-republish into one question does not fail silently, they argue visibly about whether
a source is "open". The concept page settles a distinction. It does not warn about an invisible
failure.

**Two forms of this boundary that stayed split.** `license-sharealike` and
`trap-sharealike-contaminates-by-paraphrase` were examined and kept apart: the licence page is a
version and host inventory of what the SA text says, the trap is the mechanism by which a file
becomes contaminated with nothing announcing it. Different jobs.

## Boundary 2: `license` versus `source`, regime against host

**The test.** A `license` page is about a **regime** and is host-independent. A `source` page is a
**rights verdict about one host**.

**Why the split is structural rather than tidy.** One organisation can publish three grants on
three hosts. Illustrative Mathematics does exactly that: `im.kendallhunt.com` serves the first
edition under CC BY 4.0, `tasks.illustrativemathematics.org` serves the 2016 task bank under
CC BY-NC-SA 4.0, and `accessim.org` serves v.360 under CC BY-NC 4.0. Three source pages, one
publisher. Honesty floor F5 in `meta/synthesis-brief.md` states the consequence in its operative
form: `"IM is CC BY 4.0" is a floor violation. "im.kendallhunt.com serves the first edition under
CC BY 4.0" is correct.`

The inverse holds too, and one host in this corpus proves it. `map.mathshell.org` publishes four
regimes and says so on its own homepage: "Precise terms vary between materials". Classroom
Challenges, Summative Tasks and PD Modules each carry different terms, and TRU Math carries no
statement at all. That is one `source` page covering four regimes, not four source pages.

So the two families cut the same material along perpendicular axes, and neither axis can carry the
other's content:

- Collapse `license` into `source` and every regime gets restated once per host, with the
  restatements free to drift.
- Collapse `source` into `license` and the three-hosts-one-brand error becomes structurally
  unsayable, which is how "IM is CC BY 4.0" survived in the first place.

**Visible in the built pages.** Counting only host extracts named in frontmatter, the eight
`license` pages draw on 2 to 6 hosts each. Of the sixteen `source` pages, eleven draw on exactly
one host extract, and the five that reach 2 or 3 are precisely the ones that must distinguish
themselves from a sibling host: the three IM hosts and the two SAP domains.

**The reader's version of the test.** If you can answer the question without naming a host, it is a
`license` page. If the answer changes when you change the URL, it is a `source` page.

**One case where the boundary itself is the finding.** `source-achieve-the-core-sap` folds two
domains onto one page, ruled at Gate 1, because the load-bearing fact is neither host's: the
surviving dedication is worded to cover `learnwithsap.org` alone, and whether it reaches the maths
library on the other domain is unresolved. Split across two pages, a reader lands on one half and
re-derives the wrong answer, which is how the blanket CC0 belief survived after the grant was
withdrawn.

## Boundary 3: `contract` versus `practice`, shape against procedure

**The test.** A `contract` describes a **shape** an artifact must have. A `practice` describes a
**procedure** someone executes.

**What it cost.** One drafted contract row moved families. `k12-standards-grounding-sequence` was
cut from `contract` and absorbed by `practice-ground-a-lesson-end-to-end` and
`practice-resolve-a-standard-code`. The adjudication record states the test in one line: "Every
other contract row describes the SHAPE of a document or schema. This one described a call ORDER,
which is a procedure by nature."

A call order is the giveaway. If reordering the steps breaks the thing, it is a procedure, and
procedures belong to `practice`.

**The two operational forms of the test:**

1. Can it be checked against a finished file, with nobody present and no record of how the file was
   made? Then it is a shape, and it is a `contract`. `k12-document-set` is checkable this way: one
   `lesson.json`, exactly two top-level keys, `id` becomes the filename, `audience` decides which
   facets render.
2. Does it have an order, and does the order matter? Then it is a procedure, and it is a
   `practice`. `practice-ground-a-lesson-end-to-end` is the model case: probe the connector, resolve
   the standard, batch the dependent calls, freeze the bundle with provenance. Run those out of
   order and the pass produces a complete-looking package with nothing behind it.

**The pair that stayed split, and why.** `k12-render-invocation` and
`practice-format-a-lesson-package` were examined and both kept: "The contract row is the invocation
surface and its failure modes; the practice row is the authoring procedure that ends in it." A
surface has a shape. Reaching it has an order. Two pages.

## Boundary 4: `evidence` versus everything

**The test.** An `evidence` page appraises a **claim** and uses Profile B. It exists where this
project measured something and the measurement is the point.

The profile is the tell. `## The claim` forces the claim to be stated precisely enough to be wrong,
and `## What the evidence shows` forces the appraisal to be separate from the claim rather than
folded into it. A page that cannot fill both halves is not an evidence page, whatever it is about.

**Against `trap`.** Both families report measurements, so this is the boundary most likely to blur.
The distinction is what the page is *for*. A trap owns the mechanism by which the broken case looks
like the working one. An evidence page owns the census. The adjudication record kept
`evidence-store-ingest-boundary` and `trap-empty-facet-reads-as-success` apart on exactly that
line: "The trap owns `_never_raise` (success and failure are byte-identical); the evidence page
owns the census (which node types cross, the 16,021 figure, the stale repo doc)."

**Against `source`.** A source page reports what a host's own page says. An evidence page reports
what this project found when it looked. `source-learning-commons-kg` states the two-layer grant.
`evidence-kg-coverage-and-gaps` states what the export actually contains and where it is empty.

**Against `concept`.** A concept asserts an idea. An evidence page appraises a claim and can come
back negative. `evidence-c7-store-gap-not-corpus-gap` is the worked case: the gap is real in the
store and was an artefact in the corpus, and the row was rewritten post-Gate-1 when the second half
inverted. A concept row cannot survive that kind of reversal. An evidence row is built for it.

**The attribution requirement that follows.** Honesty floor F4 requires that where a claim comes
from this project's own measurement rather than an outside source, the page says so in those words.
Evidence pages are where that language is mandatory rather than merely available, because on an
evidence page the measurement is the entire content.

## Assignment procedure

Several rows pass more than one test, so the order is load-bearing rather than cosmetic. Take the
first match.

1. Is it a rights verdict about **one host**? Then `source`.
2. Is it a **regime**, answerable without naming a host? Then `license`.
3. Do the broken case and the correct case **produce the same-looking output**? Then `trap`. This
   step comes before 5, 6 and 7 deliberately: it is the step that cut four concepts, and running it
   late is how a silent failure gets written up as doctrine instead of as a warning.
4. Is the content a **measurement this project made**, with the measurement as the point? Then
   `evidence`, on Profile B.
5. Does it describe a **shape** an artifact must have, checkable against a finished file? Then
   `contract`.
6. Does it describe a **procedure**, where the order matters? Then `practice`.
7. Is it a load-bearing idea that survives all six? Then `concept`. The family is small on purpose.

## What this taxonomy deliberately has no type for

**The standards themselves.** `CLAUDE.md` is explicit: never write a page that restates a
standard's content. That artifact is machine-derived by `wiki-vaults/build_standards_vault.py`,
which imports the store's dedupe directly and so cannot drift from it. A hand-written standard page
here would be a copy that can.

**The evidence floor.** The rule that a licence claim is valid only with a verbatim sentence, its
URL and its HTTP status is CONFIG policy, not a content page. It binds every page rather than being
a topic within one. This is part of why `concept-verbatim-license-floor` was cut: the incident
belongs to `trap-summary-layer-is-not-evidence`, the procedure belongs to
`practice-build-a-source-table`, and the doctrine belongs to `CLAUDE.md`.

**Group pages.** The family index pages under `wiki/groups/` are structural, not an eighth entity
type. They index a family; they do not classify a subject. Nothing in the assignment procedure above
depends on one existing, which is why the taxonomy was fixed before the connective layer was built.

## Related

- [[source-im-kendall-hunt]], the Gate 2 golden page and the Profile C exemplar
- [[license-sharealike]], the regime page whose host inventory shows the `license` axis
- [[concept-cite-quote-adapt]], the surviving concept that settles a visible confusion
- [[k12-document-set]], a shape checkable against a finished file
- [[practice-ground-a-lesson-end-to-end]], a procedure whose order is the content
- [[trap-code-form-silent-zero]], the silence test in its purest form
- [[evidence-store-ingest-boundary]], Profile B and the census it owns
- [[trap-summary-layer-is-not-evidence]], the incident behind the evidence floor

## References

1. `CLAUDE.md`, this wiki root. CONFIG `entity_types`, the evidence floor, the three page profiles,
   and the instruction to write to `meta/lint_config.py` rather than the shipped template.
2. `meta/lint_config.py`. `SECTIONS`, `EVIDENCE_SECTIONS`, `SOURCE_SECTIONS`, `CONTENT_TYPES`,
   `STRUCTURAL_DIRS`, and the NOTE recording that the shipped template is stale.
3. `meta/lint.py`. The shared engine: what counts as a content page, what the section and
   frontmatter checks actually assert, and the hash lock against `meta/lint.lock.json`.
4. `meta/lint-report.md`, generated 2026-08-07. `pages_scanned: 66`, `status: PASS`, 0 errors, 0
   warnings. That run covered the 66 content pages. It predates the connective layer, so it is
   evidence about the content set and not about the wiki's current lint state.
5. `INVENTORY.md`. The per-family census, the five cross-family cuts with the test applied to each,
   the six content merges, and the duplication examined and declined.
6. `meta/synthesis-brief.md`. Honesty floors F1 to F5, the verdict vocabulary, the retired
   vocabulary table, and the three page profiles as given to page-writers.
7. the project's governing ruling. Gate 1 at 62 rows expanded to 66, Gate 2 on the golden page, ruling 2a
   and its amendment, ruling 2b on en dashes inside quotations.
8. `templates/page-template.md` line 23, and
   `the private workspace/machinery/skills/build-a-wiki/assets/page-template.md`
   line 23. Both read `## Configuration / key details`. Zero pages in this wiki use it.
