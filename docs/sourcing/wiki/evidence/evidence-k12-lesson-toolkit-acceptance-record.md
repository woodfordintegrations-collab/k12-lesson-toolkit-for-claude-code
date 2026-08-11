---
title: "The k12-lesson-toolkit acceptance record: what was proven, when, and where the proof lives"
type: evidence
sources:
  - sources/k12-lesson-toolkit-boundaries.md
  - sources/k12-lesson-toolkit-store-and-mcp.md
  - docs/acceptance/ca-math-grounding.md
  - README.md
  - docs/handoff/2026-07-22-overnight-build.md
updated: 2026-08-08
---

# The k12-lesson-toolkit acceptance record: what was proven, when, and where the proof lives

## Summary

Has the standards store ever been proven to ground a real k12 skill end to end? The repository
says no. The git history says something happened. An outside memory record says yes, with run
detail. All three are about 2026-07-22 and none of them is a lie.

The error this page exists to prevent is settling the question from whichever artifact you opened
first, and it runs in both directions.

- **Reading the unticked checkbox as proof the grounding path was never exercised.** It was, at
  least twice, on the same day, by live model sessions that found two real defects and fixed both.
- **Reading "v1 ACCEPTANCE PASSED (2026-07-22)" as proof the four pass conditions were met.**
  Nothing in the repository records that, the procedure's own request for an outcome annotation was
  never answered, and this project's staging agent **did not open** the file that asserts the pass.

The staged extract states the shape of the disagreement better than a summary can:

> The unticked checkbox and the "acceptance passed" memory are not necessarily in conflict about
> the facts; they may be in conflict about what counts as the acceptance.

This wiki records that. It does not repair it. Editing the k12-lesson-toolkit repository is a separate
task with its own commit, and this wiki documents systems rather than fixing them.

## When to reach for it

Reach for it before writing any sentence of the form *the store is proven* or *the store has never
been validated*. Both are available from the record and neither is supported by it.

Reach for it before scheduling a re-run, because the procedure is specific about what it tests and
about what it costs: it needs an interactive session and cannot run unattended.

Reach for it when a `.si` memory record and a repository artifact disagree about a shipped fact.
This is the worked instance, and the resolution posture generalises.

Do **not** reach for it as evidence about the MCP contract or the store's contents. Those are
[[evidence-store-ingest-boundary]] and [[evidence-kg-coverage-and-gaps]].

## The claim

**C1. The procedure carries no outcome.** `docs/acceptance/ca-math-grounding.md` is staged as an
exact four-condition procedure and carries no outcome annotation anywhere in its 83 lines. Its own
closing line asks for one and no such record was written into the spec it names. Falsifier: an
outcome annotation in that file or in the spec section it points to.

**C2. The repository's status documents say unrun, and they are one moment in time.** The README
checklist item for the acceptance run is unticked, and the handoff names it as the first
outstanding action. Both were written at the same commit on 2026-07-22 at 07:57, mtimes 90 seconds
apart, and neither has been touched since. Falsifier: a later mtime or a later commit touching
either.

**C3. Live grounding runs happened after those documents were frozen.** Two commits landed the same
day, at 19:38 and 22:14, whose messages describe live model sessions exercising the grounding path.
Falsifier: a reading of those commit bodies that does not describe a live run.

**C4. Those runs are not the acceptance.** They report defects found and fixed, not a pass
recorded, and they name standards outside the acceptance procedure's own example. Falsifier: a
commit or artifact asserting all four pass conditions were met.

**C5. The in-repo corroboration of the memory's run detail is a different claim.** The handoff
records `6.RP.A.2` resolving with its backward and forward neighbours "through the tool impls".
Pass condition 1 is about the skill's own probe taking the grounded path, which is not the same
thing, and the same document draws that distinction two lines apart. Falsifier: showing the tool
impls and the skill path are one route.

**What these claims do not say.** They do not say the acceptance failed. They do not say the memory
record is wrong; its content is reported here only as `INVENTORY.md` describes it and is **not
evidence in this wiki**, because no agent in this build opened it. And they say nothing about the
store's correctness, only about what has been demonstrated and written down.

## What the evidence shows

### The procedure, and its four pass conditions verbatim

`docs/acceptance/ca-math-grounding.md`, Step 4, lines 52 to 60:

> Pass = all of:
> 1. **Probe** — the skill's Step 0.3 sees the KG tools as available (it takes the grounded
>    path, not the fallback).
> 2. **Standard grounded** — the lesson's target-standard callout shows the **verbatim
>    6.RP.A.2 text and code** from our store (not a paraphrase).
> 3. **Real prerequisite** — it names **6.RP.A.1** (or the true prior standard) from the
>    progression tool — proof the CA→CCSS crosswalk bridge reached the skill.
> 4. **Footer flipped** — the teacher plan does **not** carry *"Generated without the Learning
>    Commons Knowledge Graph…"*. (Optionally shows the positive provenance stamp.)

Its closing line, line 83, verbatim: "Record the outcome and any field-name reconciliation
back into the spec §3 footer/section." No such record exists; spec §3 lines 94 to 95 still read
"(Exact stamp string is a v1 decision; default proposed here.)"

### Reading A: the repository's own status, frozen at 07:57

`README.md` lines 39 to 43:

> - [x] Fork + study the upstream engine
> - [x] Spec the standards resource
> - [x] Build the California-math vertical (store + 7-tool MCP + ingestion; 50 tests green)
> - [ ] Validate against the skills (live acceptance run — `docs/acceptance/ca-math-grounding.md`)
> - [ ] Ship

`docs/handoff/2026-07-22-overnight-build.md`, line 78 to 79, under "Honest gaps / v1 boundaries":

> - **Not yet proven end-to-end that the skills ground** — that is the acceptance run, the one
>   thing left that matters most.

The timing is what makes these one reading rather than two. Both were written at commit
`95fbde3c`, 2026-07-22 07:57:58, whose subject is "docs: morning handoff + README status (v1 built;
acceptance + push pending)". `README.md` mtime `2026-07-22 07:57:29`, the handoff's
`2026-07-22 07:56:59`. Neither file has been touched since. **They describe the repository as it
stood at 07:57 on 2026-07-22, and nothing more.**

### Reading B: the git history after 07:57

`b8fd521c`, 2026-07-22 19:38:37, message body, verbatim excerpt:

> The tools returned placements in an unstable, non-richness
> order, so grounding landed on an empty node while a rich sibling held the data. The
> live grounding test (haiku + sonnet) confirmed this on 3 of 4 HS standards.

`1ad5649d`, 2026-07-22 22:14:08, the current HEAD, verbatim excerpt:

> Follow-up grounding re-test found academicSubject matching was case-sensitive:
> find_standard_statement(code="8.EE.A.2", academicSubject="mathematics") returned []
> while "Mathematics" resolved.

and, verbatim: "Verified against the deployed console script: lowercase and mismatched
subject now resolve."

These are in-repo artifacts and they establish that at least two live model sessions exercised the
grounding path that day, after the status documents were frozen. They do **not** establish the four
pass conditions, because they name `8.EE.A.2` and "3 of 4 HS standards" rather than the
acceptance's own `6.RP.A.2` example, and because they report failures found rather than a pass
recorded.

### Reading C: an outside record, not opened here

`INVENTORY.md` cites a `.si` episodic memory file as carrying a paragraph headed "v1 ACCEPTANCE
PASSED (2026-07-22)", with the detail that California `6.RP.A.2` returned prerequisite `6.RP.A.1`
plus three Achievement Network learning components. **That file was outside this project's staging
scope and was not opened.** It is reported here exactly as `INVENTORY.md` describes it, and it is
not evidence at this wiki's floor.

One in-repo corroboration of that specific detail exists and can be quoted.
`docs/handoff/2026-07-22-overnight-build.md` lines 72 to 73, under "What is real right now
(verified this session)":

> - `6.RP.A.2` (California) resolves verbatim; backward `6.RP.A.1`, forward `7.RP.A.1` — the
>   CA→CCSS crosswalk bridge works end to end through the tool impls.

Read carefully, that sentence says the **tool impls** were exercised. Pass condition 1 requires the
skill's own Step 0.3 probe to take the grounded path. The same document asserts both things:
`6.RP.A.2` works "through the tool impls" at line 72, and at line 78 it is "Not yet
proven end-to-end that the skills ground."

### The stale number that dates the freeze independently

The README says "50 tests green". The suite run at staging returned `68 passed in 1.14s`. The two
later commits record the counts in their own messages: `b8fd521` says "pytest (65) green",
`1ad5649` says "pytest (68) green". 50 was true at `95fbde3` and is stale by two commits, which is
independent confirmation that the status documents describe a moment rather than the present.

## Gotchas & constraints

**1. Two documents saying "unrun" are one witness.** The README and the handoff were written into
the same commit within 90 seconds of each other. Counting them as two independent sources
overstates Reading A.

**2. A live grounding test is not the acceptance, and the commits do not claim it is.** They
claim a path was exercised and a defect was found. Both defects were fixed and committed the same
day, which is a stronger signal about the system than a green checkbox would be, and a weaker one
about the procedure.

**3. The two claims differ at pass condition 1.** Tool impls exercised directly is not the skill's
Step 0.3 probe taking the grounded path. A re-run has to go through the skill.

**4. Never verify through an in-process import.** All 68 tests exercise `build_server(...)` and the
`*_impl` functions by direct import and never the spawned binary. The install is a bare `src` path
append, and the stdio server binds its modules once at import. So a green suite proves nothing
about the process the build is actually calling. See [[trap-stale-stdio-mcp-server]].

**5. Control the database path before believing any re-run.** `create_schema()` runs
unconditionally at startup, so a server pointed at a missing or empty file starts successfully and
every tool then returns its typed-empty payload. A silent empty result can mean "wrong
`OVEREDUCATED_DB`". The acceptance's own registration block pins the path, and it should be checked
rather than assumed. See [[trap-empty-facet-reads-as-success]].

**6. The re-run cannot be automated.** The handoff states it needs an interactive session and
cannot run unattended. Whatever this costs, it is not a background job.

**7. Do not repair the repository from this wiki.** The recommendation carried at Gate 1 is
explicit: record both readings, name the outside record as the source of the pass claim with its
run detail, state plainly that the repository's own artifacts do not carry that evidence, and do
**not** edit `README.md` or annotate the acceptance document. Whether that repair is scheduled is
The owner's call, and it belongs in the k12-lesson-toolkit repository's own commit.

**8. The outside record remains unverified from here, and that is the honest state.** What would
close it: open the `.si` episodic file, read the paragraph, and record whether it names all four
pass conditions or only the prerequisite and component detail. Until that is done, this wiki has
one reading it has not inspected and says so.

## Related

- [[trap-stale-stdio-mcp-server]] is why a green test suite is not evidence about the running
  server, and is the rule any re-run has to obey.
- [[trap-empty-facet-reads-as-success]] is why a re-run that returns nothing needs its database
  path confirmed before the result is interpreted.
- [[evidence-store-ingest-boundary]] is what the store actually holds, which is the substrate the
  acceptance would be testing.
- [[evidence-kg-coverage-and-gaps]] is the upstream census, and the reason some tools would return
  empty even on a fully working run.
- [[practice-ground-a-lesson-end-to-end]] is the procedure whose grounded path pass condition 1
  refers to.
- [[practice-resolve-a-standard-code]] holds the code-resolution step the two fixed defects both
  landed in.
- [[trap-code-form-silent-zero]] is the adjacent failure mode: the case-sensitivity fix made the
  filter values case-insensitive and left the code comparison byte-exact.

## Composes with

- [[practice-ground-a-lesson-end-to-end]] is where the four pass conditions would actually be
  exercised, and re-running this acceptance is that practice performed against a named standard
  with the outcome written down.

## References

Local artifacts read read-only by this project at staging on 2026-08-07, repository HEAD
`1ad5649dd4158c5a96a11561f678a2d877747000` dated 2026-07-22 22:14:08:

- `docs/acceptance/ca-math-grounding.md`, 3877
  bytes, mtime 2026-07-22 07:47:33. The four pass conditions, the registration block, and the
  closing request for an outcome record.
- `README.md`, 1959 bytes, mtime 2026-07-22
  07:57:29. The status checklist and the stale "50 tests green".
- `docs/handoff/2026-07-22-overnight-build.md`,
  5714 bytes, mtime 2026-07-22 07:56:59. Lines 5 to 7, 11 to 14, 72 to 73 and 78 to 79.
- Git history: commits `95fbde3c`, `b8fd521c` and `1ad5649d`, quoted from their message bodies.
- `.venv/bin/pytest -q` run at staging, returning `68 passed in 1.14s`.

Staged extracts in this wiki, both staged 2026-08-08:

- `sources/k12-lesson-toolkit-boundaries.md`, primary. §5 the acceptance contradiction in full: Reading A
  with the timing evidence, Reading B with both commit bodies, Reading C recorded as unopened, the
  tool-impls distinction, and the closing statement of the precise open question.
- `sources/k12-lesson-toolkit-store-and-mcp.md`, primary. §0 the file inventory, mtimes and the 68-test
  measurement; §5 the case-sensitivity commit in full with its diffs; §6 the stale stdio server,
  the editable install, and what the in-repo tests do and do not prove.

Not opened by this project, and named here as an unverified reading:
`a private project store (not public)/memory/episodic/project/project_k12-lesson-toolkit.md`, the
"v1 ACCEPTANCE PASSED (2026-07-22)" paragraph, reported only as `INVENTORY.md` describes it.
