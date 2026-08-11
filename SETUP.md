# Setup instructions, written for an AI agent

**If you are a person:** you do not need to read this. Open this repository in Claude Code (or
any coding agent) and say *"read SETUP.md and set this up, then verify it and tell me what
works."* Come back when it reports. The rest of this file is addressed to the agent.

**If you are an agent:** work through this in order. Every step has an acceptance check with a
real expected value, measured on 2026-08-11. Do not report success on a step whose check you
have not run. If a check disagrees with what is written here, say so plainly — a number that
has drifted is information, not a formality to wave through.

---

## 0. What you are setting up, and why it is shaped this way

Anthropic's `k12-teacher-skills` ground their lesson output in a Learning Commons connector
available only inside Claude for Teachers. Without it the skills still work, but they stamp
every lesson plan with a footer saying the standards are not grounded.

This repository supplies the missing tools rather than modifying the skills. It runs an MCP
server registering the same seven tool names, backed by an openly-licensed standards export
that ships in the repo. The skills detect those tool names and take their connected path.

**So the end state you are working toward is:** the seven tools answer real queries, and
Anthropic's skills, installed unmodified, stop emitting the ungrounded-output footer.

## 1. Python version

`requires-python = ">=3.12"`.

Prefer **3.12 or 3.13** if you have a choice. On 3.14 several wheels for the optional document
renderer are not yet prebuilt, and `pip install` will try to compile them from source — this
was measured taking over ten minutes before being abandoned. The MCP server itself has one
dependency and installs fine anywhere.

## 2. Install

Two install modes. Pick by what the human actually wants.

```bash
pip install -e .                 # the MCP standards server. This is the common case.
pip install -e ".[docgen]"       # ...plus the Teacher/Student .docx renderer
```

**Do not "helpfully" upgrade `mcp`.** The pin is `mcp>=1.28,<2` and it is deliberate: `mcp`
2.0 removed `mcp.server.fastmcp`, which this server imports. If you see
`ModuleNotFoundError: No module named 'mcp.server.fastmcp'`, something installed 2.x over the
pin. Reinstall with the constraint.

## 3. Build the store

```bash
python -m k12_toolkit.ingest --source data/ca-math --db data/standards.db
```

**Acceptance check.** It prints a stats block. These values, verbatim:

| key | expected |
|---|---|
| `standards` | 2303 |
| `learning_components` | 4203 |
| `progressions_backward` / `progressions_forward` | 795 / 659 |
| `curriculum_lessons` | 3301 |
| `curriculum_alignments` | 36529 |
| `curriculum_materials` | 12599 |
| `component_edges_orphaned` | 0 |

`standards_without_code: 283` is expected and fine — those are framework grouping nodes that
carry no statement code. `relatesto_skipped: 284` is also expected; those edges are
non-sequential and have no home in the progression model.

If `curriculum_*` are all `0`, the curriculum files are missing from `data/ca-math/`. That is a
real failure, not a degraded mode.

## 4. Run the tests

```bash
pytest -q
```

**Acceptance check**, and it differs by install mode. Both were measured on 2026-08-11:

| install | expected |
|---|---|
| `pip install -e ".[docgen]"` | `115 passed, 1 skipped` |
| `pip install -e .` | `105 passed, 2 skipped` |

The ten-test difference is the figure rasterizer. Those tests inspect pixels, so without Pillow
they would assert nothing at all — they skip rather than pass vacuously. Report which mode you
ran. A *failure* in either mode is a real problem; a lower pass count in server-only mode is
not.

## 5. Register the server with Claude Code

Use absolute paths for both the executable and the database.

```bash
claude mcp add k12-standards \
  -e K12_TOOLKIT_DB="$(pwd)/data/standards.db" \
  -- "$(python -c 'import sys,os; print(os.path.join(sys.prefix,"bin","k12-standards-mcp"))')"
```

Then confirm the tools are actually registered, in a new session:

```bash
claude mcp list
```

**Acceptance check:** `k12-standards` appears and connects. If it is listed but fails to
connect, run the command from the `-- ...` part directly in a terminal and read the error; a
stdio MCP server that cannot start prints to stderr and is otherwise silent.

## 6. Verify it answers, and verify it the right way

This is the step that matters, and the one most likely to produce a confident wrong answer.
Run this:

```bash
python - <<'PY'
from k12_toolkit.repository import SqliteStandardsRepository
from k12_toolkit.mcp.server import (
    find_standard_statement_impl, find_curriculum_lessons_impl,
    list_standards_for_mathematical_practice_impl)

repo = SqliteStandardsRepository("data/standards.db")
found = find_standard_statement_impl(repo, code="HSG-SRT.C.6", jurisdiction="California")
std = found["standards"][0]
print("statement:", std["statement_text"][:70])

lessons = find_curriculum_lessons_impl(repo, caseIdentifierUUID=std["caseIdentifierUUID"])
print("lessons  :", [entry["lessonName"] for entry in lessons["lessons"]][:3])
print("via      :", "bridge" if "alignedVia" in lessons["lessons"][0] else "direct")

practices = list_standards_for_mathematical_practice_impl(repo)
print("practices:", len(practices["standardsForMathematicalPractice"]))
PY
```

**Acceptance check:** the statement text begins *"Understand that by similarity, side ratios in
right triangles..."*, the lesson list is non-empty and includes **"Angles and Steepness"**, the
alignment reads **bridge**, and the practice count is **8**.

### Three ways this step lies to you

Read these before you interpret an empty result. All three have already happened in this
repository, and each cost real time.

**A standards code has to be in the exact form the store holds.** `HSG-SRT.C.6` returns rows.
`G-SRT.6` and `HSG-SRT.6` return **zero rows and no error**. If a lookup comes back empty, try
the code's other forms before concluding the standard has no content.

**Curriculum attaches to Multi-State CCSS nodes, not to a state's own standards.** All 561
standards the curriculum aligns to are Multi-State; zero are California's. A California lookup
reaches lessons only through the crosswalk bridge, and the result says so via `alignedVia`. If
you query a raw uuid you picked yourself and get `[]`, you may have picked the state node while
the data hangs off its CCSS twin — which is exactly the mistake the `via: bridge` line above is
there to make visible.

**An empty return is not evidence of an empty source.** Three tools in this repo shipped as
stubs on that reasoning and all three turned out to have their data present the whole time. If
a tool returns nothing, find out whether the source is empty or your key is wrong, and say
which one you established.

## 7. Optional: the document renderer

Only if the human wants `.docx` output. Requires `[docgen]`.

```bash
python -m k12_toolkit.docgen.rasterize     # prints which rasterizer backend is available
```

**Acceptance check:** it names a backend (`cairosvg`, `rsvg-convert`, `resvg`, `inkscape` or
`qlmanage`). If it says none is available, it prints install options; the HTML output path
needs no rasterizer at all, so this blocks `.docx` figures only.

Note `cairosvg` installs cleanly without its native cairo library and fails only when asked to
draw. That is why the backend chain probes by rendering rather than by importing, and why "it
is installed" is not an answer to "does it work".

## 8. What to report back

Tell the human, in this order:

1. Which install mode you used, and the Python version.
2. The ingest counts, and whether they matched.
3. The test result, and which mode.
4. Whether `claude mcp list` shows the server connected.
5. The verification output from step 6 — the actual lesson names it returned.
6. Anything that disagreed with this file.

Then tell them the two things they cannot see from a green run:

- The shipped data is **California mathematics only**. Other states and subjects are a
  documented build step (`README.md` → *Building a different state or subject*), not a
  download.
- **Misconceptions are empty for every slice.** The upstream export contains none, so
  `find_misconceptions_for_standard` returns `[]` always and the skills fall back to their own
  knowledge for that one field. This is not a broken install.
