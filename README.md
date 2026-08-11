# k12-lesson-toolkit-for-claude-code

Standards-grounded K-12 lesson tooling for Claude Code: an MCP standards server built from
openly-licensed public data, two reference wikis, and a renderer that ships a Teacher Edition
and a Student Edition a teacher can actually hand out.

> *"The skills are written to make effective use of the Learning Commons Knowledge Graph
> Claude connector that is included for all teachers using Claude for Teachers. This connector
> provides Claude with access to academic standards across all 50 states and progressions
> beneath them; **adapt the skills if your environment does not have access to these tools.**"*
>
> — [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)

This is that adaptation.

**Not affiliated with, endorsed by, or supported by Anthropic.** Built on their Apache-2.0
licensed `k12-teacher-skills`, which remains theirs. Anthropic's copyright and NOTICE are
preserved wherever their code is vendored here.

---

## The problem

Anthropic's two K-12 teaching skills ground their output in a Learning Commons connector that
ships only inside Claude for Teachers. Outside that account the connector is absent.

**The skills handle that honestly**, and it is worth being precise about this rather than
overselling the gap. They check whether the connector's tools are available, they state that
they are fully functional without it, they forbid inventing citations, and when the connector
is missing they stamp the lesson plan with a visible footer:

> *"Generated without the Learning Commons Knowledge Graph. Standards and misconceptions
> reflect general best practice."*

That is good engineering. It is also a real cost. A teacher outside Claude for Teachers gets a
lesson plan explicitly marked as *not* grounded in the standard it names — the graceful
degradation, every time, forever. The disclaimer is honest precisely because the grounding is
genuinely absent.

This project supplies that grounding from data anyone can ship, so the skills take their
connected path instead of their fallback path. Same skills, same contract, no gated account.

## What this adds, and what each addition is for

**A standards server the skills already know how to use.** It registers the same seven tool
names the skills look for:

```
find_standard_statement                     find_curriculum_lessons
find_standards_progression_from_standard    find_materials_for_lesson
find_misconceptions_for_standard            list_standards_for_mathematical_practice
find_learning_components_from_standard
```

The skills branch on whether those names are present, so nothing here forks, patches or shims
them. *Use it to:* install Anthropic's `k12-teacher-skills` exactly as published, register this
server, and get lesson plans grounded in the actual standard text instead of the
not-grounded footer.

**The standards themselves, in the repository.** 2,303 California mathematics standards as a
filtered derivative of the Learning Commons public export, CC BY 4.0, each record keeping its
own `license` and `attributionStatement`. No account, no API key, no gated connector.
*Use it to:* clone and have grounding work offline, immediately.

**Published curriculum aligned to those standards.** 3,301 Illustrative Mathematics lessons and
12,599 activities and assessments, CC BY 4.0. *Use it to:* ask "what has someone already
written for this standard?" and get real lesson names back, then pull the activities inside one.

**Teacher Edition and Student Edition documents.** The renderer emits both as editable `.docx`,
answer keys in one and not the other, with figures carrying screen-reader alt text — upstream's
block vocabulary has no image type at all, which is workable for prose subjects and useless for
geometry. *Use it to:* hand a student the Student Edition without hand-editing anything out.

**Two reference wikis, 208 pages.** `docs/sourcing/` answers *may I use this source?* per host,
with the verbatim licence sentence, URL, HTTP status and date behind every verdict — because
licences expire, and two this field relies on were withdrawn inside six months during 2026
while OER indexes went on publishing the old answer. It also keeps **citing, quoting and
adapting** apart, which is where most open-education licence trouble starts: ShareAlike and
NoDerivatives do not touch citation, and quoting does not trigger ShareAlike. `docs/udl/`
answers *does this design remove a barrier, or does it change what I am measuring?*
*Use them to:* settle a sourcing question in a minute, and as standalone reading — they are
the part most likely to be useful even if you never run the server.

**A slice builder for other states and subjects.** The export covers 52 jurisdictions and 4
subjects. *Use it to:* build Texas Science or New York ELA instead of California mathematics.

## Getting it running

**You do not need to run any of this yourself.** Clone the repository, open it in Claude Code
(or any coding agent), and say:

> Read SETUP.md and set this up, then verify it and tell me what works.

[**SETUP.md**](SETUP.md) is written for the agent, not for you. It carries the install steps,
the expected numbers at every stage, how to register the MCP server, and — the part that
matters — the three ways this system returns a confident empty answer that looks like a real
one. It ends by telling the agent exactly what to report back.

If you would rather drive it by hand, SETUP.md is perfectly readable; it is just longer than
you need.

## What is tested, and what is not

| | Status |
|---|---|
| The seven MCP tools against the shipped data | **Tested.** 115 automated tests, run on every change. |
| The shipped data reproducing from its own script | **Tested.** Re-extracting California mathematics reproduces `data/ca-math/` record for record. |
| Teacher and Student `.docx` output | **Tested.** The worked example was built end to end and both editions are in `examples/`. |
| Figures on a non-macOS machine | **Partly.** The example was rebuilt with the macOS rasterizer disabled and matched exactly — but on macOS. Never run on Linux or Windows. |
| Anthropic's skills taking their connected path | **Not tested end to end.** The tool names and response shapes are pinned by `tests/test_contract.py` against the contract extracted from the skills. Nobody has watched the real skills run against this server and confirmed the footer disappears. |
| Any state or subject other than California mathematics | **Not tested as content.** The extractor is tested and builds other slices; no unit has been written from one. |
| Misconceptions | **Empty by measurement.** The upstream export contains none, anywhere. That tool returns `[]` and the skills fall back to their own knowledge. |

## Layout

| Path | What |
|---|---|
| `src/k12_toolkit/mcp/` | the 7-tool MCP standards server |
| `src/k12_toolkit/ingest/` | builds the SQLite store from the shipped export |
| `src/k12_toolkit/docgen/` | Teacher/Student edition renderer, vendored from upstream plus a figure block |
| `data/ca-math/` | the standards export, CC BY 4.0 — see `LICENSE-DATA` |
| [`docs/sourcing/`](docs/sourcing/) | **reference wiki:** what you may cite, quote or adapt, per host, with dates |
| [`docs/udl/`](docs/udl/) | **reference wiki:** Universal Design for Learning as a design discipline |
| `docs/reference/` | the engine map, the export schema, the sourcing verdict, the document standard |
| `docs/design/` | why the MCP server has the shape it has |
| `scripts/` | `extract_standards.py` builds a slice for any state and subject; `extract_curriculum.py` adds the curriculum layer |
| `tests/` | the suite |
| [`SETUP.md`](SETUP.md) | install and verification, written for an agent |

Both wikis start at their own `README.md` and read as standalone references.

## The worked example

**The two finished documents are in [`examples/hs-geometry-similarity-trig/`](examples/hs-geometry-similarity-trig/)** — open those first; they are what a teacher actually receives.

[**hs-geometry-similarity-trig**](https://github.com/woodfordintegrations-collab/hs-geometry-similarity-trig)
is the full source: a complete two-week grade 9-10 geometry unit built with this toolkit, CC BY 4.0, with ten lesson
packages, three quizzes, a final exam, a parallel-form practice exam, 73 accessibility-validated
figures, and a construct-register row for every assessable item written before the item existed.

### What it cost to make

Measured from commit timestamps, not recalled:

| Phase | Wall clock |
|---|---|
| Standards research, licence sweep, reference-wiki build, unit design | 6h 22m |
| Unit build — 10 lessons, 5 instruments, 73 figures | 2h 59m |
| Document rendering — Teacher and Student editions | 1h 05m |
| **First unit, starting from nothing** | **10h 26m** |

Output: 143 files, 285,583 words of markdown, 73 validated SVGs, two rendered editions.

**A second unit is a projection, not a measurement.** Only one has been built, so treat the
number accordingly. It would reuse the wikis, the figure validator, the renderer, the document
standard and the construct-register schema, and reuse none of the topic analysis, unit design
or content. On that basis, roughly **5 hours**. If that turns out wrong, the honest number
will replace it here.

## Building a different state or subject

California mathematics is shipped because a clone has to stay small, not because it is the only
slice that works — the whole export would be roughly 280 MB. It covers **52 jurisdictions and
4 subjects**, and `scripts/extract_standards.py` builds any pair.

It needs the Learning Commons knowledge-graph export (`nodes.jsonl` + `relationships.jsonl`,
~812 MB), which is public and not redistributed here. Ask your agent for it — *"build me the
Texas Science slice"* — and point it at the head of `scripts/extract_standards.py`, which
documents the one non-obvious rule: every slice also carries the **Multi-State** standards for
its subject. That is not optional. A state's own standards hold no progression edges and reach
them only through the crosswalk, so a slice built without Multi-State loads perfectly and
answers every progression query with an empty list.

Re-running the script for California mathematics reproduces the shipped `data/ca-math/`
exactly, and `--verify data/ca-math` checks that — so the script is not asking to be trusted.

## Honest limits, in detail

The table above is the summary. These are the five that will bite you specifically, and the
first four share a shape: **they return an empty list rather than an error.** An empty result
from this system is a boundary, not an answer about the standard you asked for.

- **A standards code must be in the exact form the store holds.** `HSG-SRT.C.6` returns rows.
  `G-SRT.6` and `HSG-SRT.6` return **zero rows and no error** — the failure most likely to read
  as "this standard has no content" when it means "you typed it differently".
- **Zero misconception records, and this one is not fixable here.** Measured rather than
  assumed: across all 247,786 nodes of the export, no property key and no relationship label
  matches misconception, error or mistake. `misconceptions.jsonl` is 0 bytes for every slice,
  not just this one. Every misconception in the worked example was authored and cited by
  hand.
- **No progressions outside CCSS mathematics.** All 757 `buildsTowards` edges in the export
  run between Multi-State mathematics standards. A Science or ELA slice loads and answers
  every other tool, and returns nothing on progressions; the extractor says so at build time
  rather than letting the tool look empty later.
- **Curriculum reaches a state standard by inference, not by statement.** All 561 standards
  the curriculum aligns to are Multi-State CCSS nodes; **zero** are California's. A California
  lookup therefore travels the export's own evidence-based crosswalk to its CCSS twin, and
  every such result carries `alignedVia` naming the standard it came through. **525 of
  California's 1,467 standards reach curriculum this way; the other 942 reach none** — most
  have no crosswalk edge at all. Treat an `alignedVia` result as a strong suggestion rather
  than as the publisher's own alignment.
- **Licence verdicts are dated 2026-08-07 and 2026-08-08.** See the note at the foot of
  `LICENSE-DATA` about why that matters more than it looks.

Three limits listed here previously have been closed and are recorded rather than erased,
because in each case the reason for the limit was wrong in an instructive way:
`find_curriculum_lessons` and `find_materials_for_lesson` were stubs "because the data is not
in the public export" — it was, and the join failed only on an identifier-space mismatch that
returns empty without raising (`docs/reference/sourcing-verdict.md`).
`list_standards_for_mathematical_practice` was a stub justified by its consumer rather than by
its data; MP1 to MP8 were in the shipped export all along. And the `.docx` figure path was
macOS-only; it now runs a backend chain and was verified end to end with QuickLook disabled.

## Licence

Code is **Apache-2.0** (`LICENSE`). Data under `data/ca-math/` is **CC BY 4.0** and carries
a separate set of obligations, including a CCSS rider that is not Creative Commons at all
(`LICENSE-DATA`). Third-party attribution is in `NOTICE`.
