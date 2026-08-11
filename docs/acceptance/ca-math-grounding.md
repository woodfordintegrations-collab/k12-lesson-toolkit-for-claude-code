# v1 Acceptance — California-math grounding

The v1 done-criterion (spec §8): with this project's MCP registered, the forked
`k12-teacher-skills` planning skill **grounds** a California-math request against our data.
This needs a **live Claude session** and cannot be run unattended, so it is staged here as
an exact procedure.

## Prerequisites

1. Store built (rebuildable, gitignored):
   ```
   cd ~/Documents/k12-lesson-toolkit-for-claude-code
   .venv/bin/python -m k12_toolkit.ingest --source data/ca-math --db data/standards.db
   ```
   (Already built once; rebuild if data/ changes. ~2.2 MB, 2303 standards.)

2. The MCP server runs on demand: `.venv/bin/k12-standards-mcp` (reads `K12_TOOLKIT_DB`).

## Step 1 — Register the MCP for the acceptance session

The real Learning Commons connector is injected by the Teachers runtime, not by the plugin's
`.mcp.json` (that file only wires the 9 third-party servers). So we inject ours at the
session level the same way. Simplest: a project-scoped `.mcp.json` in the directory you run
the acceptance session from:

```json
{
  "mcpServers": {
    "learning-commons-knowledge-graph": {
      "command": "/path/to/k12-lesson-toolkit-for-claude-code/.venv/bin/k12-standards-mcp",
      "env": { "K12_TOOLKIT_DB": "/path/to/k12-lesson-toolkit-for-claude-code/data/standards.db" }
    }
  }
}
```

## Step 2 — Install the forked skill plugin (same session)

From `~/Documents` (per the fork README):
```
claude plugin marketplace add ./k12-teacher-skills/plugin
claude plugin install k12-teacher-skills@k12-teacher-skills
```

## Step 3 — Run the planning skill on a CA-math request

Example: *"Plan a grade 6 California math lesson on understanding ratio concepts and using
ratio language (standard 6.RP.A.2)."*

## Step 4 — Acceptance checks

Pass = all of:
1. **Probe** — the skill's Step 0.3 sees the KG tools as available (it takes the grounded
   path, not the fallback).
2. **Standard grounded** — the lesson's target-standard callout shows the **verbatim
   6.RP.A.2 text and code** from our store (not a paraphrase).
3. **Real prerequisite** — it names **6.RP.A.1** (or the true prior standard) from the
   progression tool — proof the CA→CCSS crosswalk bridge reached the skill.
4. **Footer flipped** — the teacher plan does **not** carry *"Generated without the Learning
   Commons Knowledge Graph…"*. (Optionally shows the positive provenance stamp.)

## Known risks to watch (these are what the acceptance actually tests)

- **Tool namespacing (likely the first thing to hit).** Claude Code usually exposes MCP
  tools as `mcp__<server>__<tool>`. The skill's probe looks for `find_standard_statement`.
  Confirm the skill recognizes our (possibly prefixed) tools as the KG tools and calls them.
  If it does not, that is the primary fix target — adjust the server registration/naming, or
  confirm how the skill's detection matches tool names. This is the top open question.
- **Response field names (review finding U1).** If the skill takes the grounded path but
  fails to extract `standard_code` / verbatim `standard_text` / the prerequisite, compare
  what the skill tried to read against our tool output and reconcile the field names in the
  RESPONSE SHAPING section of `src/k12_toolkit/mcp/server.py`. Our names (`code`,
  `statement_text`, `caseIdentifierUUID`, `subStandards`, …) are reasonable but unverifiable
  without the live connector; this step is where they get pinned.

## On partial pass

- Probe fails → tool-namespacing issue (above).
- Grounds but wrong/missing text → field-name reconciliation (U1).
- Names a CCSS-jurisdiction prerequisite instead of the CA equivalent → acceptable for v1
  (the bridge already maps back to CA where a clean reverse crosswalk exists).

Record the outcome and any field-name reconciliation back into the spec §3 footer/section.
