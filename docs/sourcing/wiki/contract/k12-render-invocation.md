---
title: "Renderer invocation and its failure modes"
type: contract
sources:
  - sources/k12-grounding-and-render.md
  - sources/k12-plugin-contract.md
  - sources/k12-block-types.md
updated: 2026-08-08
---

# Renderer invocation and its failure modes

## Summary

There is one render command:

```bash
bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
```

It writes one `.docx` and one `.html` per `documents[]` entry, named by that entry's `id`, plus
a copy of the source JSON. That is the happy path. The rest of this page is the six
distinguishable ways it hands back something that looks finished and is not, because **a
populated output directory is not proof of delivery** and this project's design spec files that
as trap 13: do not trust agent return signals for census, enumerate the output tree.

The six, each a different fact:

1. `python-docx` is pip-installed **at render time**, pinned to `1.1.2`, with `|| true`
   swallowing every failure. There is no vendored wheel anywhere in the plugin.
2. When the import still fails, the script renders **HTML only**, writes a diagnostic to
   **stderr**, and **exits 1**. The output directory fills with real files.
3. `set -euo pipefail` means a renderer traceback kills the run mid-loop, leaving the documents
   already written on disk and looking correct.
4. The `id` is silently rewritten into a filename, and two ids that sanitize alike overwrite
   each other.
5. The HTML twin is written **before** the docx for every document, so the presence of `X.html`
   proves nothing about `X.docx`.
6. The `$OUTPUT_DIR` mirror keys off an **environment variable**, not the positional argument.
   Unset it and the mirror never runs.

The vendor's own instruction is the correct one and it is not optional: list `$OUTPUT_DIR` and
confirm both extensions exist for every document.

## When to reach for it

Reach for it immediately after writing a `lesson.json` and before telling anyone the package
exists. The check this page describes is the last thing between a valid JSON file and a claim of
delivery.

Reach for it when a render "worked" and a document is missing, when a filename does not match
the `id` you wrote, or when a package rendered on one machine and not another.

Reach for it when planning any batch or unattended build. Six of the six failure modes above
are invisible to a caller that reads stdout only or counts files without checking extensions.

Do not reach for it for whether the documents are internally consistent, which is
[[k12-package-consistency]], or for what the block vocabulary is, which is [[k12-block-types]].

## How it works

### The vendor instruction, verbatim, `SKILL.md` lines 406 to 423

> ### 5b. Render every Word document — one command, same turn
>
> ```bash
> bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
> ```
>
> This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
> `$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
> `source_packet.docx`), plus `.html` and `lesson.json` working files. Render straight into
> `$OUTPUT_DIR` and leave everything the script writes in place — later revision turns
> re-render from the working files even though the teacher only sees the Word documents. Then list `$OUTPUT_DIR`
> and confirm every document has both its `.docx` and `.html`; if either is missing or tiny,
> rerun the script. Present the Word documents to the teacher together — attach the lesson plan
> last so it lands on top (chat surfaces stack newest-first). If there is no `student_materials`
> document, say so plainly ("This lesson is oral, so there's no student handout — students will
> work with …"). If the script errors, fix `lesson.json` (it is almost always malformed JSON)
> and rerun. If file generation fails entirely, say so clearly — do not silently fall back to a
> chat-only delivery.

Both skills give this instruction. It is the vendor telling the author to prove delivery by
enumeration rather than by return signal, and the sections below are why.

### The dependency install, `render_all.sh` lines 20 to 24, verbatim

```bash
# python-docx powers the .docx output; the .html twins render without it. If the install
# can't complete (offline container), render html now so the twins always exist.
if ! python3 -c "import docx" 2>/dev/null; then
  python3 -m pip install -q "python-docx==1.1.2" || true
fi
```

The pin is exactly `python-docx==1.1.2`. `|| true` makes a network outage, a proxy block, a
resolver error and a read-only `site-packages` all the same non-event. Measured: the only files
under either skill's `scripts/` directory are the five renderer files, `theme.css`, and
`__pycache__` residue. No wheel ships with the plugin.

### The failure branch, lines 25 to 33, verbatim

```bash
if python3 -c "import docx" 2>/dev/null; then
  python3 "$here/render_documents.py" "$json" --format both --outdir "$outdir"
else
  # Render the html twins so a readable preview still exists, then fail loudly: the
  # teacher's .docx deliverables could not be produced.
  python3 "$here/render_documents.py" "$json" --format html --outdir "$outdir"
  echo "error: python-docx could not be installed — no .docx deliverables were produced" >&2
  exit 1
fi
```

The signature of this failure is specific: `$OUTPUT_DIR` fills with `.html` files, `lesson.json`
is **not** copied because the `cp` at line 36 is unreachable after `exit 1`, the diagnostic goes
to stderr, and the exit code is 1. The message string, byte exact, is
`error: python-docx could not be installed — no .docx deliverables were produced`.

### Fail-fast, and what it leaves behind

Line 13 is `set -euo pipefail`, and the header comment at line 10 is
`# Fail-fast: any renderer error stops the run.` A malformed `lesson.json` raises in
`json.loads` and kills the script. `render_documents.main()` writes inside
`for i, doc in enumerate(docs)`, one document at a time, with no transaction and no cleanup, so
a crash on document 3 of 4 leaves documents 1 and 2 on disk looking correct.

### The id becomes a filename, `render_documents.py` lines 78 to 84, verbatim

```python
    for i, doc in enumerate(docs):
        # Sanitize the document id before it becomes a filename: the id comes from generated
        # JSON, so strip path separators and anything outside [A-Za-z0-9_-].
        doc_id_raw = str(doc.get("id") or f"document_{i + 1}")
        doc_id = re.sub(r"[^A-Za-z0-9_\-]", "_", Path(doc_id_raw).name) or f"document_{i + 1}"
        if args.only and doc_id_raw not in args.only and doc_id not in args.only:
            continue
```

An `id` of `student materials` becomes `student_materials.docx`. An `id` of `answer key (A)`
becomes `answer_key__A_.docx`. A missing or falsy `id` becomes `document_1`, `document_2` and so
on by position. Two ids that sanitize to the same string overwrite each other's output with no
warning, so the file count can be lower than the `documents[]` count.

### The HTML twin always ships, lines 86 to 97, verbatim

```python
        # The HTML twin always ships — docx is the teacher deliverable, html is its
        # always-available preview. Rendering docx alone leaves the twin missing, so
        # "docx" implies both.
        from render_lesson_html import render as render_html
        path = outdir / f"{doc_id}.html"
        path.write_text(render_html(full), encoding="utf-8")
        written.append(str(path))
        if args.format in ("docx", "both"):
            from render_lesson_docx import render as render_docx
            path = outdir / f"{doc_id}.docx"
            render_docx(full, str(path))
            written.append(str(path))
```

HTML is written first, for every document, before any docx is attempted. That is exactly why
§5b says to confirm both extensions.

### The mirror is conditional on an environment variable, lines 38 to 44, verbatim

```bash
# Delivery guarantee: when $OUTPUT_DIR is set and the render went elsewhere
# (a staging dir like /tmp/out), mirror EVERYTHING into $OUTPUT_DIR too.
# Revision turns re-render from the lesson.json that lands there;
# hand-copying a subset there is the failure this removes.
if [ -n "${OUTPUT_DIR:-}" ] && [ "$(cd "$outdir" && pwd)" != "$(mkdir -p "$OUTPUT_DIR" && cd "$OUTPUT_DIR" && pwd)" ]; then
  cp -R "$outdir"/. "$OUTPUT_DIR"/
fi
```

`outdir` is the second **positional** argument. The mirror compares it against the
**environment** variable `OUTPUT_DIR`. The two are the same directory only because the
documented invocation passes `"$OUTPUT_DIR"` as the second argument.

## In practice

### The delivery check, in order

1. Run the command. Capture **both** streams and the exit code. Do not read stdout alone.
2. If the exit code is 1, read stderr. Three distinguishable messages exist, byte exact:

   ```
   error: python-docx could not be installed — no .docx deliverables were produced
   error: no `documents` array in input
   nothing rendered — check --only ids against the documents' `id` fields
   ```

   The first is the dependency failure. The second means the input had no `documents` array. The
   third is returned when `--only` matched no id.
3. Enumerate the output directory. For every entry in `documents[]`, compute the sanitized id
   and confirm both `{id}.docx` and `{id}.html` exist and are not tiny.
4. Confirm the file count equals the `documents[]` count. A shortfall means two ids collided.
5. Confirm `lesson.json` landed in the output directory. Its absence alongside `.html` files is
   the python-docx failure signature.
6. Only then say the package exists.

### The success path is one stdout line

Verbatim from `render_documents.py`: `print("wrote " + ", ".join(written))`. That line is the
entire positive signal, and it enumerates paths, so it is worth capturing. It still does not
prove the files are non-trivial, which is why step 3 checks size.

### Rendering formats

`--format both` is what the happy path passes. `--format docx` implies both anyway, per the
comment quoted above. `--format html` is what the failure branch passes. There is no mode that
produces docx without html.

### The differentiation skill's copy is the same script

Measured by `diff`: its `render_all.sh` differs in exactly five hunks, all comment or filename
related. The pip line, the html-only branch, the `exit 1` and the `$OUTPUT_DIR` mirror are
identical. It takes `differentiation.json` and persists it under that name. Everything on this
page applies to it.

### Measured on this workstation, 2026-08-07 PDT

This project's own measurement of this machine, not a claim about any other environment:

```
$ python3 -c "import docx; print('docx importable, version:', getattr(docx,'__version__','n/a'))"
docx importable, version: 1.2.0
$ which python3
/usr/local/bin/python3
$ python3 -V
Python 3.14.6
```

Two consequences. The pip branch would not fire here, because the `if ! python3 -c "import
docx"` guard short-circuits. And the version present is **1.2.0**, not the `1.1.2` the script
pins, because the pin applies only when the module is absent. An environment that already
carries a different python-docx runs on that one, unpinned and unchecked.

## Gotchas & constraints

**1. A directory full of files is the failure mode, not the success signal.** The python-docx
branch produces real, readable `.html` for every document and exits 1. A caller that treats a
populated directory as success sees exactly what success looks like.

**2. Exit 1 and a partial set are two different failures with the same shape.** The dependency
failure leaves html for all documents and no `lesson.json`. A mid-loop traceback leaves both
extensions for the documents already processed and nothing for the rest. Distinguish them by
whether any `.docx` exists at all.

**3. The pin is aspirational.** `python-docx==1.1.2` binds only a machine where the module is
absent. Behaviour under any other version is untested here.

**4. Your filename is not your id.** Anything outside `[A-Za-z0-9_-]` becomes an underscore. Two
ids differing only in a space or a slash collide, and the loop writes unconditionally, so the
second silently wins. Use ids that are already filename-safe.

**5. `$OUTPUT_DIR` unset means no mirror.** If the render targets a staging directory and the
environment variable is not set, the artifacts stay there and later revision turns will not find
them.

**6. The vendor tells you not to read the scripts, and the scripts are where this lives.**
`SKILL.md` lines 195 to 200, verbatim in part: "**Do not open, cat, head, or grep the renderer
scripts**, because their behavior is fully specified by the commands and output paths in §5a–5d, and
`references/example_lesson.json` is the complete schema. Reading script source tells you nothing
this file doesn't already state." Line 352, verbatim: "**Schema** — sufficient on its own; do
not read any other file for the schema:". This project measured that claim false in three
respects: the schema fence omits five canonical block types and publishes two aliases as types,
the facet-order sentence contradicts the code, and `fill_table` accepts fields the fence does
not publish. Every failure mode on this page comes from the scripts. Treat the instruction as
addressed to a lesson-writing turn, not to a build that must prove delivery.

**7. The teacher-facing language rule is not a reporting rule for you.** `SKILL.md` bars
mentioning JSON, scripts, rendering or file names in any teacher-facing message. That governs
what a teacher reads. It does not license reporting a failed render as a success: the same block
says that if generation fails, say the documents could not be created.

**8. Unverified from here: the renderer was never run.** The staged extracts record reading
`render_all.sh` (44 lines), `render_documents.py` (108 lines) and `lesson_common.py` (763 lines)
in full, plus targeted ranges of the two renderers. No render was executed and no output was
inspected. What would close it: run `render_all.sh` against `references/example_lesson.json`,
once with python-docx present and once without, and record both output trees and exit codes.

## Related

- [[k12-document-set]] holds the `documents[]` array whose entries become these filenames.
- [[k12-block-types]] holds the render-time repair passes and the unknown-type fallback that
  prints prose instead of failing.
- [[k12-package-consistency]] is the pre-render gate; this page is the post-render gate.
- [[k12-shared-registry]] is why a malformed `shared` key produces a shorter document rather
  than an error, which enumeration will not catch.
- [[k12-observation-template]] and [[k12-student-materials]] are two documents the enumeration
  must find, and `student_materials` is the one that legitimately may not exist.
- [[k12-assessment-gap]] adds more `documents[]` entries than the vendor names, which makes the
  id-collision and count checks here load-bearing rather than theoretical.
- [[trap-empty-facet-reads-as-success]] is the same failure class one layer up, inside the
  document rather than at the file boundary.

## Composes with

- [[practice-format-a-lesson-package]] ends with the delivery check on this page.
- [[practice-format-an-assessment-artifact]] runs the same check over a larger document set,
  where the id-collision risk is higher because ids are this project's invention rather than the
  vendor's fixed three.

## References

Staged extracts in this wiki, all staged 2026-08-08 from local files read at 2026-08-07 21:15
PDT. Local files, so no HTTP status exists.

- `sources/k12-grounding-and-render.md`, primary. §4.1 the `SKILL.md` §5b instruction verbatim
  and its differentiation counterpart; §4.2 `render_all.sh` in full plus the five-hunk `diff`;
  §4.3 the six failure modes verbatim, from the pip block to the environment-variable mirror;
  §4.4 the python-docx 1.2.0 and Python 3.14.6 measurement on this workstation; §4.5 §5e.
- `sources/k12-plugin-contract.md`, primary. §1.5 one document, one filename; §8.5 the
  plain-language rule; §8.6 the do-not-read-the-scripts rule verbatim and the three measured
  respects in which its schema-sufficiency claim is false.
- `sources/k12-block-types.md`, primary. §6 the unknown-type fallback that prints prose.

This project's own working file, cited as this project's measurement and not as any outside
party's statement: `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`, §7 Tier 2 trap 13
(enumerate the output tree) and Tier 3 trap 20 (python-docx is pip-installed at render time).

Underlying vendor files, cited as the staged extracts cite them, under
`k12-teacher-skills/plugin/skills/`: `k12-lesson-planning/scripts/render_all.sh`,
`render_documents.py`, `render_lesson_docx.py`, `render_lesson_html.py`, `SKILL.md`, and
`k12-lesson-differentiation/scripts/render_all.sh`. Plugin 0.6.0, measured byte-identical to the
installed copy by `diff -r -q --exclude=__pycache__`, exit 0.
