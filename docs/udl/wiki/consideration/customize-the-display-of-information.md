---
title: "1.1 Support Opportunities to Customize the Display of Information"
type: consideration
sources:
  - https://udlguidelines.cast.org/representation/perception/customize-display/
  - https://udlguidelines.cast.org/representation/perception/
  - sources/nodes-guideline-1-perception.md
  - sources/cast-guidelines-3-0-structure.md
updated: 2026-08-07
---

# 1.1 Support Opportunities to Customize the Display of Information

## Summary

Consideration 1.1 sits under [[perception]] in [[multiple-means-of-representation]]. It
asks you to let learners adjust *how* information is displayed (font, size, contrast,
volume, timing) rather than fixing those parameters once for everyone. CAST's own
framing draws a line this page treats as load-bearing: digital materials make this kind
of customization possible, but "digital does not mean the content is accessible."

## When to reach for it

Reach for 1.1 when information already reaches the learner through a workable
modality, but its display parameters are locked (too small, too fast, too low-contrast,
too loud, too quiet) for some learners to use comfortably.

| The actual problem | Where to go instead |
|---|---|
| There is no alternative modality at all: only a visual or only an auditory version exists | [[multiple-ways-to-perceive-information]] (1.2) |
| The material itself fails a legal accessibility test (screen reader can't parse it, no keyboard path) regardless of what settings you expose | [[mistaking-udl-for-accessibility-compliance]] |
| The content excludes or flattens identities rather than being hard to see or hear | [[diversity-of-perspectives-and-identities]] (1.3) |
| The barrier is vocabulary or sentence complexity, not display settings | [[clarify-vocabulary-and-language-structures]] (2.1) |
| The barrier is how a learner responds or navigates, not how content is displayed | [[response-navigation-and-movement]] (4.1) |

The diagnostic question is narrower than it looks: "can this learner perceive the
content at all" routes to 1.2; "can this learner tune the presentation of content they
can already perceive" routes here.

## How it works

CAST's own text states the mechanism and its limit in the same breath:

> While print materials have fixed displays, digital materials enable flexible
> customization. This adaptability helps diverse learners by adjusting perceptual
> clarity and accommodating individual preferences. However, an important caveat
> applies: digital does not mean the content is accessible, as many digital materials
> are equally inaccessible if accessibility features weren't integrated during
> development.

That caveat is the substance of this consideration, not a footnote to it. A slider that
resizes text in a browser view is a UDL move; whether the underlying document is
readable by a screen reader at all is a separate, testable question governed by
technical accessibility standards and the disability-rights law built on them, not by
this framework. UDL has no success criteria of its own: see
[[mistaking-udl-for-accessibility-compliance]] for why "we built in customization" is
not the same claim as "this is legally accessible."

CAST also names who does the tuning: "Educators and learners should work together to
attain the best match of features to learning needs." The right settings are found
through use, not assigned in advance from a profile.

## In practice

CAST's design options for this consideration, verbatim, are customization of:

- Font, text size, character and line spacing, character width, background color, and
  text colors
- Size of images, graphs, tables, and visual content
- Contrast between background and images
- Color used for information or emphasis
- Volume or rate of speech or sound
- Speed or timing of video, animation, sound, simulations
- Layout of visual or other elements

**A worked pass.** A digital worksheet is distributed as a scanned, flattened PDF:
an image of text, not text. Offering a font-size control in the PDF viewer does
nothing: there is no underlying text to resize, and a screen reader gets nothing at
all. Applying 1.1 here is not a single move. The UDL move is deciding up front that
display parameters (size, spacing, contrast, layout) should be adjustable; the
technical prerequisite for that move to mean anything is that the document is built as
structured, tagged text rather than a raster image. Skipping the second step makes the
first one cosmetic.

## Gotchas & constraints

- **Digital does not mean accessible.** This is CAST's own caveat, not an outside
  addition, and it is the main way this consideration gets misapplied: treating the
  presence of a settings panel as evidence of access. Customizability that a screen
  reader cannot reach is not access.
- **The legal floor and the design framework are different obligations.** Technical
  accessibility standards are enforceable and testable; this consideration is a design
  instinct that happens to overlap with them heavily, especially in Guideline 1. Passing
  one does not certify the other. See [[mistaking-udl-for-accessibility-compliance]].
- **Source gap.** The staged extract for this consideration does not name specific
  legal citations or WCAG success criteria, only the general accessibility caveat
  quoted above. Do not read specific compliance claims into this page beyond that.
- **Co-design, not a fixed profile.** CAST frames the right settings as found jointly
  by educator and learner, not derived from a diagnosis or a preference category
  assigned once.

## Related

[[perception]]
[[mistaking-udl-for-accessibility-compliance]]
[[access-to-assistive-technologies]]
[[multiple-ways-to-perceive-information]]
[[multiple-means-of-representation]]
[[learner-variability]]

## Composes with

_Reserved for a later composition phase._

## References

1. [Consideration 1.1: Support opportunities to customize the display of information, CAST UDL Guidelines 3.0](https://udlguidelines.cast.org/representation/perception/customize-display/)
2. [Guideline 1: Perception, CAST UDL Guidelines 3.0](https://udlguidelines.cast.org/representation/perception/)
3. `sources/nodes-guideline-1-perception.md`, staged extract, fetched 2026-08-07
4. `sources/cast-guidelines-3-0-structure.md`, staged framework map, fetched 2026-08-07
