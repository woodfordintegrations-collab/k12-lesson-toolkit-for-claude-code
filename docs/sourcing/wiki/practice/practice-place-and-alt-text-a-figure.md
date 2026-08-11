---
title: Place and alt-text a figure
type: practice
sources:
  - sources/k12-plugin-contract.md
  - sources/k12-grounding-and-render.md
  - sources/k12-block-types.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
  - k12-teacher-skills/plugin/skills/k12-lesson-planning/references/math.md
  - Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md
updated: 2026-08-08
---

# Place and alt-text a figure

## Summary

A geometry unit is mostly diagrams and the renderer draws none of them. `SKILL.md` line 381,
verbatim:

> The renderer cannot draw images — anything the
> teacher displays (a video, photo, projected image, chart) lives in the lesson plan: name it
> in Materials and in the phase script that uses it. A student page carries only what is
> printed on it.

That single sentence is the whole placement rule, and the mistake this page exists to prevent
follows directly from it: **authoring a lesson as though a figure can be dropped into
`lesson.json`.** There is no image block. A figure referenced by a block the renderer does not
know prints nothing at all, with no error and no non-zero exit, so the failure looks like a
finished document with a gap where the diagram should be.

The second mistake is the accessibility half. A figure that reaches the page can still be
invisible to a screen reader, and the artifacts that prevent that are split across two files by
project ruling: `<title>` and `<desc>` live inside the SVG, and the long description lives in
`figures/alt-text.md`.

The third half of this procedure, palette validation, **cannot be written against tooling that
exists.** That section below is marked unverified with what would close it, rather than
described as though it runs.

## When to reach for it

Reach for it before any figure is authored, because the palette is locked first. Design §4
lists phase 6a as "Figures: palette lock, then authoring, then validation", and marks the
palette lock as one of the build's serial steps: no figure exists before it.

Reach for it whenever a lesson or an item depends on something visual. That includes the case
where the visual is not a file at all: the renderer draws three organiser blocks natively, and
choosing one of those is often the correct answer instead of an SVG.

Do not reach for it to decide whether an external figure may be reproduced. A figure carries
its own rights, independently of the text around it, and every IM figure in the units this
project sampled is uncleared. That question belongs to [[concept-third-party-carve-out]] and
[[practice-cite-without-redistributing]].

## How it works

**1. Decide first whether it is a drawn block or a file.** The renderer natively emits
`number_line`, `table`, `fill_table` and `cards`, among twenty block types. `references/math.md`
requires at least one of the organisers, verbatim: "Include at least one visual scaffold
registered in `shared` (a `data_table`, `number_line`, or `fill_table` organizer) and pulled
into the lesson plan with the teacher-facing rationale beside it." A drawn block needs no file,
no placement rule and no alt text file, because it renders as real content. Prefer it wherever
it expresses the idea.

**2. If it must be an image, it is not in the document set.** It becomes a supplementary
artifact under `SKILL.md` §5e, verbatim: "An artifact whose value depends on its form — exact
card dimensions for cutting, poster-scale type — belongs outside it, as its own file in
whatever format produces the best version (e.g. a print-ready PDF). Your judgment picks the
format; source any shared content from `shared` so pages can't drift, and name the file in
Materials like any other page."

**3. Name it twice.** Once in the lesson plan's Materials list, once in the phase script that
uses it. The contract's package-consistency rule closes the loop in both directions: every
listed item is used by a named phase, and every item any section sends students to appears in
Materials. Naming it in only one of the two is a defect no script catches. See
[[k12-package-consistency]].

**4. Decide teacher-only versus student-page deliberately.** `references/math.md`, verbatim:
"a blank `fill_table` students complete or a `number_line` they mark belongs on the worksheet;
a worked reference table that shows the operation or answer structure is teacher-only,
printing it gives away the thinking." The same ruling governs a diagram: a figure that carries
the answer belongs on the teacher page.

**5. Put the short description inside the file and the long description beside it.** Design §6
fixes the split: `figures/alt-text.md` holds long descriptions, with "`<title>`/`<desc>` live in
the SVG". The tree it lives in, verbatim from that section:

```
├── figures/
│   ├── _tokens.md                   # locked palette hexes, stroke weights, viewBox convention
│   ├── fig-01..fig-25.svg
│   ├── alt-text.md                  # long descriptions; <title>/<desc> live in the SVG
│   └── figures-index.html           # so a browser or auditor can load them
```

`figures-index.html` exists, per its own comment, "so a browser or auditor can load them", which
is the only way any served-URL auditor can reach the set at all.

**6. Validate what can actually be validated, and say which is which.** See the next section.
This is the step where the procedure stops being fully sourced.

## In practice

### The palette-validation step, UNVERIFIED

Design trap 27 requires `validate_palette.py` to be copied into the repo's `scripts/` and
committed, verbatim: "**The dataviz skill lives in `/private/tmp` and materializes on invoke.**
Copy `validate_palette.py` into `scripts/` and commit it, or the gate evaporates."

**Measured by this project on 2026-08-08, and this is this project's own measurement, not any
vendor's statement.** A filesystem search of the whole home directory for `validate_palette*`
returned 0 files. No `dataviz` skill directory exists under `~/.claude`. The deliverable repo
`~/Documents/hs-geometry-similarity-trig` does not exist yet, so neither do
`scripts/greyscale_gate.py` and `scripts/check_construct_register.py`, which the same section of
the design names.

One nearby thing does exist and it is **not** established to be the same tool.
`validate_contrast.py`, the filename design trap 28 uses, is present at
`Documents/flyboy/.si/vendor/ui-ux-pro-max/payload/design/scripts/validate_contrast.py`, 353
lines. Its command-line flags, read from its own `argparse` block, are `--sweep`, `--fixture`
with choices `all`, `uswds`, `tailwind`, `golden`, `none`, `--seeds` and `--quiet`. It has **no
`--pairs` flag**, so it is not the invocation `--pairs all` that trap 26 and this page's row in
`INVENTORY.md` describe. Whether it is the intended gate under a different name, or a different
program entirely, is not decidable from here.

**What this page therefore does not assert:** that any palette gate can be run today, what its
exit code means, or that `--pairs all` is a valid invocation of anything on this machine.

**What would close it:** phase 6a copies the actual script into the repo's `scripts/` and
commits it, then this section is replaced by the committed path, the exact flags read from that
committed copy, and a recorded exit code. It closes with a one-line edit; nothing else on this
page depends on it.

### What validation would still not prove, even once the script exists

Design trap 28, verbatim: "**Nothing validates contrast inside an SVG file.**
`validate_contrast.py` is a palette-token gate. Exit 0 proves the checker is honest and nothing
about the figures." A green palette gate is a statement about a list of hex values, not about
whether two shapes that touch in `fig-07.svg` are distinguishable.

Design trap 31 names the claim not to make, verbatim: `"WCAG 2.2 AA compliant" is an
over-claim. State what was measured.`

### The rendering path, measured

Design trap 29, verbatim: "**Playwright is the only render path on this machine.** No rsvg,
cairosvg, inkscape, or imagemagick. Its profile was measured as already locked by another
session." A figure pipeline that assumes a command-line SVG rasteriser has no rasteriser.

## Gotchas & constraints

**1. There is no image block, and the failure is silent.** An unrecognised block type reaching
`emit_block` is not an error: the emitter lookup misses, then `blk["text"]` prints as a bare
paragraph, `blk["items"]` as bullets, or nothing. The HTML renderer's own comment records why
it prints nothing rather than the JSON, verbatim: "NEVER dump raw JSON into the page — a printed
worksheet with {"type": ...} on it is a blocking print-safety failure". So an invented `image`
block leaves an empty space and a clean exit. See [[k12-block-types]].

**2. Greyscale is anti-correlated with the colour gate.** Design trap 25, verbatim: "**Greyscale
is anti-correlated with the dataviz validator.** Its lightness band is deliberately narrow,
which is what destroys greyscale print. The reference palette's worst pair measured 1.046:1.
Greyscale needs a separate luminance gate." Classroom figures are printed in black and white by
default, so passing the colour gate is the wrong reassurance.

**3. The default pair mode is wrong for geometry.** Design trap 26, verbatim: "`--pairs
adjacent` is the default and is wrong for geometry figures, where any two elements can touch.
Cap the figure palette at 4-5 colours and revalidate with `--pairs all`." Read alongside the
unverified section above: the invocation is recorded as the design's requirement, not as
something this project has run.

**4. An accessibility auditor cannot audit a loose SVG, and its silence reads as a pass.**
Design trap 33, verbatim: "**accessibility-auditor cannot audit bare SVG.** Its Step 1 is
axe-core against a served URL. Loose files produce an empty report that reads as a pass." This
is the reason `figures-index.html` is in the tree.

**5. The expert that would rule on colour vision deficiency does not cover it.** Design trap 32,
verbatim: "**design-kit-expert has zero CVD and zero greyscale coverage** and will correctly say
so. CVD authority is the script, not the expert. Its roster status is `installed`, not
`verified`." Asking the expert is not a substitute for a gate that does not yet exist.

**6. A figure's rights do not travel with the text around it.** Every IM curriculum footer
carves out embedded third-party images, and this project could not find the attribution index
that would identify them: all 8 guessed paths returned 404, and the recorded consequence is
verbatim, "the per-image license status for any specific IM figure is UNVERIFIED from here." The
working position is to reuse IM's text without IM's images. See [[source-im-kendall-hunt]] and
[[concept-third-party-carve-out]].

**7. `_tokens.md` is a lead-owned file.** Design trap 12 partitions ownership before dispatch,
and names tokens among the shared files that belong to the lead rather than to any figure agent.
Six to nine agents run in phase 6a; one palette.

**8. Alt text is authored, not derived.** Nothing in this toolchain generates a description, and
nothing checks that `alt-text.md` has an entry per figure. The count of entries against the
count of `fig-*.svg` files is a manual check, exactly like every other consistency invariant
here. See [[k12-package-consistency]].

## Related

- [[k12-block-types]] holds the twenty canonical block types, including the three organisers
  that are the alternative to a file, and the unknown-type fallback behind gotcha 1.
- [[k12-student-materials]] holds the student page skeleton and the rule that the page carries
  only what is printed on it.
- [[k12-package-consistency]] is the materials-and-phases invariant step 3 satisfies.
- [[k12-document-set]] is why a figure cannot be a `documents[]` entry.
- [[concept-third-party-carve-out]] is the rights class an embedded figure falls into.
- [[source-im-kendall-hunt]] is where the unlocatable image-attribution index was measured.
- [[practice-cite-without-redistributing]] governs reuse of any figure this project did not draw.

## Composes with

- [[practice-format-a-lesson-package]] is where the Materials line and the phase script that
  name the figure are actually written, and it is the file this procedure's output must appear
  in twice.
- [[practice-format-an-assessment-artifact]] carries the same constraint on every item that
  ships a diagram, which in a geometry instrument is most of them.

## References

Plugin files, version 0.6.0, read directly at the paths below; local files, so no HTTP status
exists. Measured byte-identical between the fork checkout and the installed plugin by
`diff -r -q --exclude=__pycache__`, exit 0:

- `plugin/skills/k12-lesson-planning/SKILL.md` line 381, the cannot-draw-images sentence quoted
  in full above; lines 465 to 470, §5e supplementary artifacts; lines 284 to 306, Document
  integrity.
- `plugin/skills/k12-lesson-planning/references/math.md`, the mandatory visual scaffold
  paragraph and the teacher-only ruling on a worked reference table.

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/k12-block-types.md`, primary. §2 the twenty emitters, §6 the unknown-type fallback
  and the print-safety comment quoted in gotcha 1.
- `sources/k12-plugin-contract.md`, primary. §7 the everything-matches invariants and the
  measurement that no script in either skill's `scripts/` directory checks any of them.
- `sources/k12-grounding-and-render.md`, primary. §4.5 the §5e escape hatch, quoted verbatim.
- `sources/host-im-kendall-hunt.md`, primary. The third-party image carve-out and the eight
  404 paths behind gotcha 6.

This project's own working file and this project's own measurements, cited as such and not as
any outside party's statement:

- `Projects/HS Geometry/specs/2026-08-07-srt-unit-design.md`. §4 phase 6a ordering; §6 the
  `figures/` tree quoted verbatim above; §7 tier 4 traps 25, 26, 27, 28, 29, 31, 32, 33, and
  tier 2 trap 12.
- Filesystem measurement, 2026-08-08: `find` over `~` returned 0 files
  named `validate_palette*`; no `dataviz` directory under `~/.claude`;
  `~/Documents/hs-geometry-similarity-trig` does not exist; `validate_contrast.py` is present
  in the flyboy vendor tree at 353 lines with flags `--sweep`, `--fixture`, `--seeds`,
  `--quiet`, and no `--pairs`.
