---
title: "oh-ost.portal.cambiumast.com (Ohio's State Tests released items)"
type: source
verdict: cite_only
fetched: 2026-08-08
sources:
  - https://oh-ost.portal.cambiumast.com/
  - https://oh-ost.portal.cambiumast.com/content/contentresources/en/OST_Sp22_IRSG_Geo_093022.pdf
  - https://oh-ost.portal.cambiumast.com/content/contentresources/en/Sp19_Geo_ItemRelease_ScoringGuide.pdf
  - https://oh-ost.portal.cambiumast.com/content/contentresources/en/Geometry.pdf
  - sources/host-ohio-released-items.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# oh-ost.portal.cambiumast.com (Ohio's State Tests released items)

## Summary

Ohio's Geometry item releases publish, for every multiple-choice item, a rationale naming the
specific reasoning error that leads a student to each wrong option, and for constructed-response
items an exemplar plus annotated zero-point student work. This project located nothing else like it
anywhere in either sweep. Verdict: `cite_only`. **No reuse grant for the items exists in the
delivered bytes.**

The mistake this page exists to prevent is precise, and it is the mistake a keyword search makes.
A `grep -i` for `permission` over the 169-page Spring 2022 document returns exactly one granting
sentence:

> Permission to reproduce is given when authorship is fully cited khess@nciea.org

It is the last line of a block, so it reads as though it closes the document. It does not. It
belongs to Marge Petit and Karin K. Hess, its subject is the Depth-of-Knowledge descriptor matrix
reproduced from the Center for Assessment, and the line immediately above it names them as the
copyright holders. **Ohio's items begin on the next page under no permission sentence at all.** A
carve-out was mistaken for a grant. See [[trap-font-notice-is-not-a-content-license]] for the same
mechanism on a different string.

Three further facts belong in the same breath as the verdict:

- **The host is not Ohio.** These are Ohio's State Tests materials served from
  `oh-ost.portal.cambiumast.com`, a Cambium Assessment portal, not an `ohio.gov` or
  `education.ohio.gov` domain. The portal footer reserves rights and names no holder at all.
- **Nothing in any of the three documents claims copyright for Ohio, the Ohio Department of
  Education, or Cambium.** `pdfinfo` metadata carries no rights field either. That is a measured
  absence, not a grant. Silence resolves to all rights reserved, not to open; see
  [[license-unmarked-silence]].
- **What makes this source valuable is not licensable in the first place.** A distractor-to-error
  mapping is a fact about how students reason. This project's own wide-sweep adjudication puts it
  the same way: item taxonomies, distractor-to-misconception mappings and rubric grammars are facts
  about assessment and about students, not copyrightable expression.

## When to reach for it

Reach for the two item-release documents when you need a misconception set that somebody else has
already validated against real student responses at scale. Spring 2022 Question 34 is the C.7 item
at Depth of Knowledge Level 1 with four per-option rationales. Spring 2019 Question 20 is the same
standard as a Level 2 constructed response, fusing the complementary relationship with special
right triangles and the triangle sum theorem, and carrying an exemplar chain plus annotated
zero-point responses.

Reach for the annotated zero-point work when you need to know what an error looks like on paper
rather than what it is called. Spring 2022 carries 28 blocks headed `Sample Response: 0 points`,
Spring 2019 carries 24, and `Geometry.pdf` carries 43. Each is followed by `Notes on Scoring`
naming the specific error.

Reach for the release structure when you are specifying your own item bank. Each released item
carries `Points Possible`, `Content Cluster`, `Content Standard`, and, in the two item-release
documents only, `Depth of Knowledge` with the specific lettered descriptors it was tagged with
rather than merely a level.

Do **not** reach for this host for item stems, answer options, figures, exemplar responses or
rationale prose to put in a deliverable. There is no grant.

Do not reach for `Geometry.pdf` expecting a blueprint or DOK tags. It has neither; see gotcha 4.

Do not reach for it as a standards reference. Ohio writes the code in its own bare form and the
Content Standard text is worded identically to the CCSS wording, which means quoting it is quoting
the upstream rights-holder's text, not Ohio's. See [[source-corestandards-nga-ccsso]].

## What its own page says

Everything below was extracted with `pdftotext -layout -enc UTF-8` and `pdfinfo` from files
downloaded to disk on 2026-08-08 and read back from disk, and is staged in
`sources/host-ohio-released-items.md`. No summarizing layer was involved; see
[[trap-summary-layer-is-not-evidence]].

### The portal footer, which names no rights-holder

Verbatim from the raw HTML of `https://oh-ost.portal.cambiumast.com/`, entities as delivered:

```html
<div><span class="line">Copyright &copy; 2026. All rights reserved.</span> <span class="line border-left"><a rel="noopener noreferrer" href="https://privacypolicy.cambiumassessment.com/" target="_blank">Terms of Use &amp; Privacy Policy</a></span> ...
```

Rendered, that is `Copyright © 2026. All rights reserved.` A year and a reservation with no party
attached. The combined Terms of Use and Privacy Policy it links sits on a different hostname,
`privacypolicy.cambiumassessment.com`, and **was not fetched**. See gotcha 2.

### The complete search result, which is the evidence for the absence

A `grep -n -i -E "copyright|©|reserved|permission|reproduc|NCIEA|Petit|Hess|used with"` over the
full extracted text of all three documents returned:

| Document | Hits |
|---|---|
| `OST_Sp22_IRSG_Geo_093022.txt` | three, at lines 405, 483, 484 |
| `Sp19_Geo_ItemRelease_ScoringGuide.txt` | three, at lines 448, 531, 532 |
| `Geometry.txt` | **zero** |

That is the whole of the rights-adjacent text in 169, 163 and 208 pages respectively.

### The three parties stacked on consecutive lines

Line 405 of Spring 2022 is the attribution line under Table 1's title on page vii, verbatim:

> Table 1: Math Descriptors – Applying Depth of Knowledge Levels for
> Mathematics (Webb, 2002) & NAEP 2002 Mathematics Levels of Complexity
> (M. Petit, Center for Assessment 2003, K. Hess, Center for Assessment, updated 2006)

Lines 483 and 484 close that same table on page ix, immediately after Ohio's own footnote about
Level 4. All three lines, in position and verbatim:

> *Note: Ohio’s State Tests only assess and measure DOK Levels 1 – 3 in grades K – 12. Level 4 is
> included in this table for informational purposes only.
>
> Updated 2006 © Marge Petit & Karin K. Hess, National Center for Assessment, Dover, NH
> Permission to reproduce is given when authorship is fully cited khess@nciea.org

Spring 2019 carries the identical pair at lines 531 and 532, byte-identical apart from leading
whitespace.

So the page carries Ohio's DOK prose, then Ohio's Level 4 footnote, then a third party's copyright
line, then that third party's grant. The grant is the last line of the block, which is exactly why
it reads as though it closes the document. The email in it, `khess@nciea.org`, is a National Center
for the Improvement of Educational Assessment address.

### Ohio's own DOK prose, for contrast, so the boundary is visible

Page vii of Spring 2022, verbatim, and this is Ohio's text rather than Petit and Hess's:

> DOK refers to the complexity of thinking required to complete a task in a given item.
> Items with a DOK 1 designation focus on the recall of information, such as definitions
> and terms, and simple procedures. Items with a DOK 2 designation require students to
> make decisions, solve routine problems, perform calculations, or recognize patterns.
> Items with a DOK 3 designation feature higher-order cognitive tasks. These DOK 3 tasks
> include but are not limited to: critiquing a statement and forming a conclusion;
> explaining, justifying, or proving a statement; or approaching abstract, complex, open-
> ended, and non-routine problems. Each grade’s blueprint contains information about
> the number of points of opportunity students will encounter at each DOK level.

Table 1 begins after that, and **Table 1 is where the ownership changes hands.**

### The feature that makes the row worth a page

Spring 2022 Question 34, the C.7 item, page 117 as printed. Verbatim:

> Rationale for Option A: This is incorrect. The student may remember that the
> relationship involves a trigonometric ratio of another angle but confuses
> cosine with sine and the angle complementary to the angle Q with the right
> angle.
>
> Rationale for Option B: This is incorrect. The student may remember that the
> relationship should involve a trigonometric ratio of another angle but confuses
> the angle complementary to the angle Q with the right angle.
>
> Rationale for Option C: This is incorrect. The student may remember that the
> relationship involves a trigonometric ratio of the complementary angle but
> confuses cosine with sine of complementary angle R.

Three notes a reader needs. The correct option is marked inline by the token `Key –` after the
option letter, not in a separate answer-key field, and the dash in `Key –` is an en dash in the
source bytes, preserved here under honesty floor F3. The three wrong rationales are compositional
rather than categorical: A is two errors at once, B is one of them, C is the other. And the item's
tag block reads `Depth of Knowledge: Level 1` followed by the specific lettered descriptors, in
this case `a. Recall, observe, or recognize a fact, definition, term, or property`, `c. Apply a
formula`, and `n. Represent math relationships in words, pictures, or symbols`.

The zero-point annotation that INVENTORY.md singles out, page 112 of Spring 2022, verbatim:

> This response earns no credit (0 points) because it shows an incorrect
> length of side NO and an incorrect measure of ∠O.
>
> The student may realize that triangles JKL and JNO are similar but
> incorrectly applies the scale factor to the angle measures instead of
> the side lengths

### The measured absence of any Ohio rights claim

Nothing in the three documents claims copyright for Ohio, the Ohio Department of Education, the
Ohio Department of Education and Workforce, or Cambium. `pdfinfo` metadata carries no rights field:

| Document | Author | Creator | CreationDate |
|---|---|---|---|
| OST_Sp22_IRSG_Geo_093022 | Russell, Nicole (Wiesenhahn) | Microsoft® Word for Office 365 | Thu Sep 29 06:53:45 2022 PDT |
| Sp19_Geo_ItemRelease_ScoringGuide | Russell, Nicole (Wiesenhahn) | Acrobat PDFMaker 19 for Word | Wed Jul  3 14:01:00 2019 PDT |
| Geometry | Russell, Nicole (Wiesenhahn) | Microsoft® Word for Microsoft 365 | Mon Jul 17 05:58:33 2023 PDT |

No reuse permission for the items was located. That is what the evidence supports, and no more.

## What you may do with it

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name the document, link it, state which item covers which standard, describe in your own words what a rationale says | yes | none, and no licence is needed to do this |
| Quote: reproduce item stems, options, rationale prose, exemplar responses or scoring notes | no | no grant was located, and unmarked is not unowned |
| Paraphrase and republish: rewrite an Ohio item or rationale and ship it | no | same, and a close rewrite of a specific item's structure is an adaptation however different the wording |

### The one grant that does exist here, and whose it is

Table 1, the Depth-of-Knowledge descriptor matrix, carries a real grant from a real named grantor:
`Permission to reproduce is given when authorship is fully cited`. Three constraints travel with it
and none of them is optional.

1. **The grantor is Marge Petit and Karin K. Hess, not Ohio and not Cambium.** Citing Ohio for
   Table 1 is an incorrect attribution even though Ohio is the document you took it from.
2. **The permission is to reproduce.** It does not say adapt, modify or build upon. Reproduce the
   matrix or do not use it.
3. **"Fully cited" has a text to be cited from**, sitting one line above the grant:
   `Updated 2006 © Marge Petit & Karin K. Hess, National Center for Assessment, Dover, NH`, with
   the table's own title line naming Webb 2002 and NAEP 2002 upstream of that.

This is a carve-out inside a document that otherwise grants nothing, which is the inverse of the
usual shape and the reason the mis-read is so easy. See [[concept-third-party-carve-out]].

### The layer that needs no licence at all

- **The misconception taxonomy itself.** That a student pairs the angle with the right angle
  instead of the other acute angle, that a student swaps the function but keeps the angle, that a
  student applies a scale factor to angle measures: these are facts about student reasoning. Stated
  in your own words, from your own analysis, they carry no rights encumbrance.
- **Structural facts about the release**: that it is DOK-tagged, that item types include
  `Multiple Choice Item`, `Equation Item`, `Graphic Response Item`, `Gap Match Item` and, in Spring
  2022, `Inline Choice Item`, that multiple-choice items get four rationale blocks while
  constructed-response items get `Exemplar Response` plus `Other Correct Responses`.
- **Which released item covers which standard**, and the fact that a state assesses the standard at
  all. That is the evidentiary work this row does in [[evidence-c7-store-gap-not-corpus-gap]].

See [[concept-cite-quote-adapt]] for the operation split and
[[practice-cite-without-redistributing]] for the mechanics.

## Gotchas & constraints

**1. The keyword-grep mis-read, stated as the worked instance.** One sentence in 169 pages grants
anything, it sits at the foot of a table owned by a third party, and it is positionally the last
line of a block. A search for `permission` finds it and nothing else, and a reader who stops there
concludes the document is reproducible with citation. The correct procedure is to read what the
grant is attached to, not merely that a grant exists: walk up from the hit to the nearest heading
and ask whose work sits under it.

**2. The portal's own Terms of Use were never fetched, and this is the open gap.** The footer links
a combined Terms of Use and Privacy Policy on `privacypolicy.cambiumassessment.com`. No agent in
this project opened it. **Recorded as unverified.** What would close it: fetch that page, paste any
sentence bearing on reproduction of content served from the portal, record URL, HTTP status and
date. Until then the verdict rests on the measured absence inside the documents, which is a weaker
foundation than a pasted refusal would be.

**3. The portal's practice-test-materials path is a 403 that returns a body.**
`https://oh-ost.portal.cambiumast.com/resources/practice-test-materials` returned HTTP 403 with
20243 bytes of rendered chrome including the site footer. A check that asks "did I get HTML back"
passes while the request was refused. This is a bot block, not a soft-404 and not a TLS failure.
The three PDF fetches were not blocked. See [[trap-down-is-not-one-state]] and
[[trap-soft-404-status-proves-nothing]].

**4. `Geometry.pdf` has no blueprint and no DOK tags, and INVENTORY.md says otherwise.** The
INVENTORY row describes it as carrying "the geometry blueprint". `grep -ci "blueprint"` over the
extracted text returns **0**. The word appears exactly once in each of the two item-release
documents, and there it points at a blueprint that lives elsewhere, inside the DOK prose quoted
above. Separately, `Depth of Knowledge:` occurs 0 times in `Geometry.pdf` and its Content Summary
table header has six columns rather than seven. Reported here rather than fixed, since INVENTORY.md
is not this page's to edit.

**5. Ohio writes the standard as `(G.SRT.7)`.** Not `HSG-SRT.C.7` and not `G-SRT.7`. All three
documents use Ohio's own bare form, and `grep -c "G.SRT.7"` returns 2 in each of the three
documents. Resolve the code before querying anything with it rather than pasting Ohio's form
through: a non-canonical form fails silently, which reads as an absence of data rather than as a
wrong code. See [[trap-code-form-silent-zero]] and [[practice-resolve-a-standard-code]].

**6. The template changed between administrations, so a quotation must name its year.** Spring 2019
reads `Define trigonometric ratios and solve problems` with no comma after `ratios`; Spring 2022
reads `Define trigonometric ratios, and solve problems` with one. Spring 2019's full-credit sentence
is `For the item, a full-credit response includes`; Spring 2022's is `For full credit (1 point), the
student’s response satisfies the bullet below.` Quoting one year's wording under the other year's
citation is a falsified quotation.

**7. A descriptor quoted from Table 1 is not byte-identical to the same descriptor quoted from an
item tag.** Inside Table 1 the Level 2 entry `d.` wraps across four narrow column lines. Quoted from
an item's own tag block it is one running line:
`d. Solve a routine problem requiring multiple steps/decision points, or the application of multiple
concepts`. Take it from the item tag and say so.

**8. One passage in the staged extract is explicitly not byte-exact, and must not be re-quoted as
though it were.** The correct-reasoning passage on the similar-figures item contains ratio
expressions that are stacked fractions in the PDF and were set inline with a slash when staged. The
staged file flags this itself. The numbers are unchanged; the layout is paraphrased. Under honesty
floor F3, re-quoting it in quotation marks as byte-exact would be falsification.

**9. `Q37 is B.5` is unverified.** The INVENTORY row names Spring 2022 Question 37 as the B.5 item.
The staged extract reproduces Question 6, Question 34 and the annotated zero-point work, and does
not reach Question 37. **Not asserted here.** What would close it: open the Spring 2022 PDF at
Question 37 and paste its `Content Standard:` line.

**10. Mathematical-italic Unicode and vertical fractions distort every extraction.** The rationale
for the keyed option contains `𝑃𝑅` and `𝑄𝑅` as mathematical-italic letters, and its fractions are
laid out vertically, which is why `pdftotext -layout` puts numerator and denominator on separate
lines around the prose. Any quotation from these documents needs the raw layout inspected, not
just the extracted string.

## Related

- [[license-unmarked-silence]] is the regime this host actually sits in: a document with no rights
  notice anywhere resolves to all rights reserved, not to open, and this is the corpus's largest
  worked instance of it.
- [[trap-font-notice-is-not-a-content-license]] is the same failure mechanism on different strings,
  where a grep hit inside embedded font metadata reads as a rights determination. Here the hit is
  real text with a real grantor, and it is still not the document's licence.
- [[concept-third-party-carve-out]] is the general shape: material inside a work that belongs to
  someone other than the work's publisher, carrying its own terms.
- [[concept-chain-of-title]] is why an absent rights claim leaves the question of who owns the items
  open rather than settled.
- [[source-jmap]] is the other released-item archive in this corpus. Same verdict, opposite
  evidence: JMAP positively asserts all rights reserved, Ohio says nothing at all.
- [[source-corestandards-nga-ccsso]] holds the upstream grant on the standard text that Ohio's
  `Content Standard:` lines reproduce.
- [[trap-down-is-not-one-state]] and [[trap-soft-404-status-proves-nothing]] name the 403 in
  gotcha 3 correctly instead of recording the host as unavailable.
- [[trap-summary-layer-is-not-evidence]] is why every quotation above came from `pdftotext` output
  on a file read from disk.
- [[evidence-misconception-research-licensing]] holds the research-literature half of the same
  question, where the licences are per-paper rather than per-state.
- [[evidence-c7-store-gap-not-corpus-gap]] is where these three documents do their evidentiary work,
  as part of what retired this project's claim that C.7 is externally scarce.
- [[k12-assessment-gap]] is the machinery-side gap that Ohio's release structure is a model for.

## Composes with

- [[practice-cite-without-redistributing]] is the procedure this host demands end to end: the most
  useful document in the corpus, and not one word of its expression may enter the repository.
- [[practice-format-an-assessment-artifact]] is where the release structure read off this host, the
  per-option rationale and the annotated zero-point sample, becomes an original item bank with its
  own distractor rationales written from scratch.

## References

Fetched by this project on 2026-08-08, `curl` to disk, read from disk with `pdftotext -layout -enc
UTF-8` and `pdfinfo`:

- `.../en/OST_Sp22_IRSG_Geo_093022.pdf` HTTP 200, 4770499 bytes, 169 pages. Spring 2022 Geometry
  Item Release and Scoring Guide. Question 34 is the C.7 item with per-option rationales; 21
  released items; 28 zero-point sample blocks.
- `.../en/Sp19_Geo_ItemRelease_ScoringGuide.pdf` HTTP 200, 3831260 bytes, 163 pages. Spring 2019.
  Question 20 is C.7 as a Level 2 constructed response; 20 released items; 24 zero-point blocks.
- `.../en/Geometry.pdf` HTTP 200, 6417404 bytes, 208 pages. Practice test answer key and scoring
  guidelines; 26 released items; 43 zero-point blocks; zero rights-adjacent hits; no DOK column.
- `https://oh-ost.portal.cambiumast.com/` HTTP 200, 26357 bytes. The footer that names no
  rights-holder.
- `https://oh-ost.portal.cambiumast.com/resources/practice-test-materials` HTTP 403, 20243 bytes.
  A bot block that returns a rendered body.

Page counts come from `pdfinfo` rather than from the documents' own numbering.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/host-ohio-released-items.md`, primary. The fetch log, the complete grep result, the
  Petit/Hess block in position, the per-item field census, Question 6 end to end, Question 34's
  rationales, Spring 2019 Question 20, the annotated zero-point work, and the DOK boundary.
- `sources/verdict-wide-sweep.md`, reference. This project's own adjudication of eight sweep
  reports, which fetched nothing and says so: the reuse-terms table row recording that no grant was
  located for Ohio, and the deduplicated error corpus that draws on these rationales.
