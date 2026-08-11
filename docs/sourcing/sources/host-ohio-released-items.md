---
source_url: https://oh-ost.portal.cambiumast.com/content/contentresources/en/OST_Sp22_IRSG_Geo_093022.pdf ; https://oh-ost.portal.cambiumast.com/content/contentresources/en/Sp19_Geo_ItemRelease_ScoringGuide.pdf ; https://oh-ost.portal.cambiumast.com/content/contentresources/en/Geometry.pdf ; https://oh-ost.portal.cambiumast.com/
fetched: 2026-08-08
http_status: 200 / 200 / 200 for the three PDFs; 200 for the portal root; 403 for /resources/practice-test-materials
role: primary
covers: source-ohio-released-items
---

## 0 · Fetch log

All three PDFs were downloaded with `curl` to disk and read from disk with
`pdftotext -layout -enc UTF-8` and `pdfinfo`. No summarizing layer was used, per the CONFIG
evidence floor. Fetch clock: `2026-08-08 04:28:52 UTC` / `2026-08-07 21:28:52 PDT`.

| URL | HTTP | Content-Type | Bytes | Pages |
|---|---|---|---|---|
| `.../en/OST_Sp22_IRSG_Geo_093022.pdf` | 200 | application/pdf | 4770499 | 169 |
| `.../en/Sp19_Geo_ItemRelease_ScoringGuide.pdf` | 200 | application/pdf | 3831260 | 163 |
| `.../en/Geometry.pdf` | 200 | application/pdf | 6417404 | 208 |
| `https://oh-ost.portal.cambiumast.com/` | 200 | text/html | 26357 | n/a |
| `https://oh-ost.portal.cambiumast.com/resources/practice-test-materials` | **403** | text/html | 20243 | n/a |

Page counts come from `pdfinfo`, not from the documents' own numbering, and they match the
`169pp` / `163pp` / `208pp` recorded in INVENTORY.md.

Failure-mode note: the 403 is a bot block that still returns a body. It served 20243 bytes of
rendered chrome including the site footer, so a naive "did I get HTML back" check passes while
the request was refused. The three PDF fetches were not blocked. This is a 403, not a soft-404
and not a TLS failure.

**Host note, load-bearing.** These documents are Ohio's State Tests materials, but the host is
`oh-ost.portal.cambiumast.com`, a Cambium Assessment portal, not an `ohio.gov` or
`education.ohio.gov` domain. Any rights statement quoted here belongs to whichever party the
document names, and the host is a third one. F5 applies: name the host.

---

## 1 · The permission question, which is the point of this row

### 1a · What the Cambium portal footer says

Verbatim from the raw HTML of `https://oh-ost.portal.cambiumast.com/`, entities as delivered:

```html
<div><span class="line">Copyright &copy; 2026. All rights reserved.</span> <span class="line border-left"><a rel="noopener noreferrer" href="https://privacypolicy.cambiumassessment.com/" target="_blank">Terms of Use &amp; Privacy Policy</a></span> <span class="line border-left"><a rel="noopener noreferrer" href="/contact.html">Contact Us</a></span></div>
```

Rendered: `Copyright © 2026. All rights reserved.` **The footer names no rights-holder.** It
gives a year and a reservation with no party attached, and links a combined Terms of Use and
Privacy Policy on a different hostname, `privacypolicy.cambiumassessment.com`, which was not
fetched for this extract.

### 1b · The only permission sentence in either item-release document

`grep -n -i -E "copyright|©|reserved|permission|reproduc|NCIEA|Petit|Hess|used with"` over the
full extracted text of all three documents returned this, and nothing else:

**`OST_Sp22_IRSG_Geo_093022.txt`**: three hits, at lines 405, 483, 484.
**`Sp19_Geo_ItemRelease_ScoringGuide.txt`**: three hits, at lines 448, 531, 532.
**`Geometry.txt`**: **zero hits.**

The Spring 2022 hits, verbatim and in position. Line 405 is the attribution line under the
DOK table's title on page vii (2022):

> Table 1: Math Descriptors – Applying Depth of Knowledge Levels for
> Mathematics (Webb, 2002) & NAEP 2002 Mathematics Levels of Complexity
> (M. Petit, Center for Assessment 2003, K. Hess, Center for Assessment, updated 2006)

Lines 483 and 484 are the two closing lines of that same table, on page ix (2022), immediately
after the note about DOK Level 4:

> *Note: Ohio’s State Tests only assess and measure DOK Levels 1 – 3 in grades K – 12. Level 4 is
> included in this table for informational purposes only.
>
>
> Updated 2006 © Marge Petit & Karin K. Hess, National Center for Assessment, Dover, NH
> Permission to reproduce is given when authorship is fully cited khess@nciea.org

Spring 2019 carries the identical pair at lines 531 and 532, byte-identical apart from leading
whitespace:

> Updated 2006 © Marge Petit & Karin K. Hess, National Center for Assessment, Dover, NH
> Permission to reproduce is given when authorship is fully cited khess@nciea.org

### 1c · The mis-read this row exists to name

`Permission to reproduce is given when authorship is fully cited` is the only sentence in
either 169-page or 163-page document that grants anything. It is preceded on the immediately
preceding line by `Updated 2006 © Marge Petit & Karin K. Hess, National Center for Assessment,
Dover, NH`, and it sits at the foot of Table 1, which is the Webb/NAEP Depth-of-Knowledge
descriptor matrix reproduced from the Center for Assessment. The email in the sentence,
`khess@nciea.org`, is a National Center for the Improvement of Educational Assessment address.

**The grantor is Petit and Hess, the granted work is the DOK matrix, and the grant does not
reach Ohio's items.** The items begin on the next page, headed
`Geometry / Spring 2022 Item Release / Question 6 / Question and Scoring Guidelines`, under no
permission sentence at all. A keyword grep for `permission` over these documents returns the
carve-out and reads it as the document's licence. That is the error.

### 1d · No Ohio rights statement exists in the delivered bytes

Nothing in any of the three documents claims copyright for Ohio, the Ohio Department of
Education, the Ohio Department of Education and Workforce, or Cambium. `pdfinfo` metadata
carries no rights field either, and no `Title` or `Subject` on two of the three:

| Document | Author | Creator | CreationDate |
|---|---|---|---|
| OST_Sp22_IRSG_Geo_093022 | Russell, Nicole (Wiesenhahn) | Microsoft® Word for Office 365 | Thu Sep 29 06:53:45 2022 PDT |
| Sp19_Geo_ItemRelease_ScoringGuide | Russell, Nicole (Wiesenhahn) | Acrobat PDFMaker 19 for Word | Wed Jul  3 14:01:00 2019 PDT |
| Geometry | Russell, Nicole (Wiesenhahn) | Microsoft® Word for Microsoft 365 | Mon Jul 17 05:58:33 2023 PDT |

**A measured absence, not a grant.** No reuse permission for the items was located. That is
what this extract supports, and no more.

---

## 2 · The per-item release structure: what fields each item's release contains

Measured by counting field labels across the full extracted text of each document.

| Field label | Sp22 (169pp) | Sp19 (163pp) | Geometry.pdf (208pp) |
|---|---|---|---|
| `Points Possible:` | 21 | 20 | 26 |
| `Content Cluster:` | 21 | 20 | 26 |
| `Content Standard:` | 21 | 20 | 26 |
| `Depth of Knowledge:` | 21 | 20 | **0** |
| `Rationale for Option` | 24 | 32 | 20 |
| `Exemplar Response` | 14 | 12 | 19 |
| `Other Correct Responses` | 14 | 12 | **0** |
| `Sample Response:` | 56 | 59 | not counted |
| `Sample Response: 0 points` | 28 | 24 | 43 |

Read the shape, not just the numbers. `Points Possible` / `Content Cluster` /
`Content Standard` occur once per released item, so the item counts are 21, 20 and 26.
`Depth of Knowledge` occurs exactly as often in the two item-release documents, meaning every
released item is DOK-tagged in both, and **never** in the practice-test guide.
`Rationale for Option` and `Exemplar Response` are alternatives, not companions: multiple-choice
and selected-response items get four `Rationale for Option` blocks, constructed-response items
get `Exemplar Response` plus `Other Correct Responses`.

### 2a · The two document layouts

**Item-release documents** (Sp22, Sp19) run:

```
Content Summary and Answer Key      (a table, repeated across several pages)
Depth of Knowledge (DOK)            (prose definitions of Levels 1-3, then Table 1)
Question <n>: Question and Scoring Guidelines
Question <n>: Sample Response(s)
```

The Content Summary and Answer Key table header in Sp22, verbatim column labels in order:

> Question No.* | Item Type | Content Cluster | Content Standard | Depth of Knowledge | Answer Key | Points

**The practice-test guide** (`Geometry.pdf`) runs:

```
Ohio's State Tests
     PRACTICE TEST ANSWER KEY &
            SCORING GUIDELINES
                     GEOMETRY
Content Summary and Answer Key
Question <n>: Question and Scoring Guidelines
Question <n>: Sample Response(s)
```

with a **six-column** header, dropping Depth of Knowledge:

> Question No.* | Item Type | Content Cluster | Content Standard | Answer Key | Points

A footnote under each page of that table reads:

> (★) indicates that modeling should be incorporated into the standard.

**`Geometry.pdf` contains no blueprint.** `grep -ci "blueprint"` returns **0** for
`Geometry.txt`. The word appears exactly **once** in each of the two item-release documents,
and there it is a reference to a blueprint that lives elsewhere, inside the DOK prose:

> Each grade’s blueprint contains information about the number of points of opportunity
> students will encounter at each DOK level.

### 2b · One item release, end to end (Sp22 Question 6, an Equation Item)

Reproduced complete so a page-writer never needs the PDF. Page numbers as printed.

```
         Question 6

Question and Scoring Guidelines

             1 (2022)
Question 6 37232

                   2 (2022)
       Points Possible: 1

       Content Cluster: Understand the relationships between lengths,
       areas, and volumes.

       Content Standard: Understand how and when changes to the
       measures of a figure (lengths or angles) result in similar and
       non-similar figures. (G.GMD.5)

       Depth of Knowledge: Level 2
       c. Use models to represent mathematical concepts
       i. Retrieve information from a table, graph, or figure and use it to
       solve a problem requiring multiple steps
       l. Select a procedure according to criteria and perform it

Scoring Guidelines
Exemplar Response

   •   The length of 𝑊𝑍 is 7.5 inches and the measure of angle Y is 45 degrees.

Other Correct Responses

   •   any equivalent values

For full credit (1 point), the student’s response satisfies the bullet below.

   •   The student enters 7.5 inches as the side length and 45 degrees as the
       angle length.

                                        3 (2022)
        Geometry
Spring 2022 Item Release

      Question 6

   Sample Responses

          4 (2022)
Sample Response: 1 point
```

Two structural facts visible here and nowhere else: the bare integer after the question number
(`Question 6 37232`) is an internal item identifier printed on the item's own page, and the
`Depth of Knowledge:` field is followed by the specific lettered descriptors from Table 1 that
the item was tagged with, not merely by a level.

---

## 3 · The per-distractor rationale, verbatim

This is the feature that makes the row worth a page. Sp22 Question 34, the G.SRT.7 item.

```
         Question 34

Question and Scoring Guidelines

             116 (2022)
Question 34 33726

    Points Possible: 1

    Content Cluster: Define trigonometric ratios, and solve problems
    involving right triangles.

    Content Standard: Explain and use the relationship between the sine
    and cosine of complementary angles. (G.SRT.7)

    Depth of Knowledge: Level 1
    a. Recall, observe, or recognize a fact, definition, term, or property
    c. Apply a formula
    n. Represent math relationships in words, pictures, or symbols

                                   117 (2022)
Scoring Guidelines
 Rationale for Option A: This is incorrect. The student may remember that the
 relationship involves a trigonometric ratio of another angle but confuses
 cosine with sine and the angle complementary to the angle Q with the right
 angle.

 Rationale for Option B: This is incorrect. The student may remember that the
 relationship should involve a trigonometric ratio of another angle but confuses
 the angle complementary to the angle Q with the right angle.

 Rationale for Option C: This is incorrect. The student may remember that the
 relationship involves a trigonometric ratio of the complementary angle but
 confuses cosine with sine of complementary angle R.

                                                                               𝑃𝑅
 Rationale for Option D: Key – The student realizes that because sin Q =             and
                                                                               𝑄𝑅
           𝑃𝑅
 cos R =        , sin Q = cos R. So, the sine of the acute angle Q is equal to the
           𝑄𝑅
 cosine of its complement, angle R.

                                        118 (2022)
Sample Response: 1 point

                           119 (2022)
```

Four notes a writer will need.

1. **The correct option is marked inline**, by the token `Key –` after the option letter. It is
   not a separate answer key field. The dash in `Key –` is an EN DASH in the source bytes and is
   preserved here under F3.
2. **The three wrong rationales each name a specific reasoning error**, not a category: A is
   "confuses cosine with sine AND confuses the complementary angle with the right angle", B is
   the second of those alone, C is the first of those alone. The taxonomy is compositional.
3. `𝑃𝑅` and `𝑄𝑅` are mathematical-italic Unicode letters in the source, and the fractions are
   laid out vertically, which is why `pdftotext -layout` puts numerator and denominator on
   separate lines around the prose.
4. **Ohio writes the standard as `(G.SRT.7)`**, not `HSG-SRT.C.7` and not `G-SRT.7`. All three
   documents use Ohio's own bare form. `grep -c "G.SRT.7"` returns 2 in each of the three
   documents, and `G.SRT.6` and `G.SRT.8` likewise return 2 each in `Geometry.txt`. Ohio's
   Content Standard text for G.SRT.7 is worded identically to the CCSS wording.

---

## 4 · Sp19 Question 20: the same standard as a constructed response

```
         Question 20

Question and Scoring Guidelines

             70 (2019)
Question 20

29760

        Points Possible: 1

        Content Cluster: Define trigonometric ratios and solve problems
        involving right triangles.

        Content Standard: Explain and use the relationship between the sine
        and cosine of complementary angles. (G.SRT.7)

        Depth of Knowledge: Level 2
        d. Solve a routine problem requiring multiple steps/decision points,
        or the application of multiple concepts

                                       71 (2019)
Scoring Guidelines
Exemplar Response

•   30 degrees

Other Correct Responses

•   any equivalent value

For the item, a full-credit response includes

•   a correct angle measure (1 point).

                                      72 (2019)
        Geometry
Spring 2019 Item Release

      Question 20

   Sample Responses

          73 (2019)
Sample Response: 1 point

       Notes on Scoring

       This response earns full credit (1 point) because it correctly
       identifies the measure of the complementary angle.

       There is more than one way to approach this question.

       One of them is to use a relationship between sine and cosine
       of complementary angles stating that if angles A and B are
       complementary, then cos A = sin B. In this situation, since cos
       A = 0.5, then sin B = 0.5 as well.

       By using Triangle Sum Theorem, m ∠A + m ∠B + m ∠C = 180
       and m ∠A + m ∠B = 90 by a definition of complementary
       angles. Therefore, m ∠C = 90, and triangle ABC is a right
       triangle.

       Based on ratios of special right triangles (30º-60º-90º), if sine
       of an angle B equals to 0.5, then the measure of angle B is
       30 degrees.
                                    74 (2019)
```

Note two differences from Sp22 that are structural, not cosmetic. The Sp19 Content Cluster
reads `Define trigonometric ratios and solve problems` with no comma after `ratios`; Sp22 reads
`Define trigonometric ratios, and solve problems` with one. And Sp19's full-credit sentence is
`For the item, a full-credit response includes` where Sp22's is
`For full credit (1 point), the student’s response satisfies the bullet below.` The template
changed between administrations. Note also the awkward `equals to 0.5` and `30º-60º-90º` using
the MASCULINE ORDINAL INDICATOR rather than the degree sign; both are as printed.

`Notes on Scoring` is a field that appears only under a `Sample Response:` block, never under
`Scoring Guidelines`. It is where the annotated student work lives.

---

## 5 · The annotated 0-point responses

Sp22 carries 28 blocks headed `Sample Response: 0 points`; Sp19 carries 24; `Geometry.pdf`
carries 43. Each is followed by `Notes on Scoring` naming the specific error. The one
INVENTORY.md singles out, at line 2442 of the Sp22 extraction, page 112 (2022):

```
Sample Response: 0 points

                            112 (2022)
Notes on Scoring

This response earns no credit (0 points) because it shows an incorrect
length of side NO and an incorrect measure of ∠O.

The student may realize that triangles JKL and JNO are similar but
incorrectly applies the scale factor to the angle measures instead of
the side lengths, and concludes that NO = KL = 10 in., and the
                         3
measure of angle L = 22· = 13.2°.
                         5

                              113 (2022)
```

The fraction `3/5` is laid out vertically in the source, which is why `pdftotext -layout` puts
`3` above and `5` below the prose line. The stated wrong answer is `13.2°`.

The corresponding correct reasoning, from the 1-point `Notes on Scoring` for the same item
family, verbatim:

> completed sentence providing evidence of understanding that in
> similar figures scaling of one side results in scaling of all other sides
> with the same constant scale factor, but this scaling does not affect
> angle measures. Therefore, corresponding angles of similar figures
> are congruent.
>
> In the two similar figures, sides QR = 2 and WX = 5 are corresponding.
> The scale factor is WX/QR = 5/2 = 2.5 and WZ/QT = 2.5. Therefore,
> WZ = 2.5 · QT or WZ = 2.5· 3 = 7.5.
>
> Since the measure of corresponding angles of similar figures are
> equal and 𝑚∠S = 45°, then 𝑚∠Y = 45° too.

The ratio expressions in the last passage are stacked fractions in the PDF; they have been set
inline here with a slash and are therefore **paraphrased layout, not byte-exact**, unlike every
other quotation in this file. The numbers are unchanged.

---

## 6 · The Depth of Knowledge apparatus, and its boundary

The DOK prose, verbatim from page vii (2022) of Sp22, which is Ohio's own text and not
Petit/Hess:

> DOK refers to the complexity of thinking required to complete a task in a given item.
> Items with a DOK 1 designation focus on the recall of information, such as definitions
> and terms, and simple procedures. Items with a DOK 2 designation require students to
> make decisions, solve routine problems, perform calculations, or recognize patterns.
> Items with a DOK 3 designation feature higher-order cognitive tasks. These DOK 3 tasks
> include but are not limited to: critiquing a statement and forming a conclusion;
> explaining, justifying, or proving a statement; or approaching abstract, complex, open-
> ended, and non-routine problems. Each grade’s blueprint contains information about
> the number of points of opportunity students will encounter at each DOK level.

Then Table 1 begins, and **Table 1 is where the ownership changes hands.** Its four columns are
headed `Level 1 / Recall`, `Level 2 / Skills/Concepts`, `Level 3 / Strategic Thinking`,
`Level 4* / Extended Thinking`. Level 1 runs items a. through o., Level 2 a. through n.,
Level 3 a. through p., Level 4 a. through h. The Level 1 entries this unit's items are tagged
with, verbatim:

> a. Recall, observe, or recognize a fact, definition, term, or property
> c. Apply a formula
> n. Represent math relationships in words, pictures, or symbols

Level 2 entry `d.`, which tags Sp19 Q20, quoted from the item's own tag block where it is set
as running text rather than from Table 1 where it is column-wrapped:

> d. Solve a routine problem requiring multiple steps/decision points, or the application of multiple concepts

Inside Table 1 itself the same descriptor is broken across four narrow column lines as
`d. Solve a routine` / `problem requiring` / `multiple steps/` / `decision points, or`, so any
quotation taken from the table rather than from an item tag will not be byte-identical.

And the Ohio-authored footnote that closes the table, immediately before the Petit/Hess line:

> *Note: Ohio’s State Tests only assess and measure DOK Levels 1 – 3 in grades K – 12. Level 4 is
> included in this table for informational purposes only.

So the page has three parties stacked on consecutive lines: Ohio's DOK prose, Ohio's Level 4
footnote, and then the Petit/Hess copyright plus grant. The grant is the last line of the
block, which is exactly why it reads as though it closes the document.

---

## 7 · Released item coverage, for a writer sizing the corpus

The `Content Summary and Answer Key` tables list, per item, its Item Type. Types observed in
`Geometry.pdf`'s first table page, verbatim: `Multiple Choice Item`, `Equation Item`,
`Graphic Response Item`, `Gap Match Item`. Sp22 adds `Inline Choice Item`. A sample row from
`Geometry.pdf` reproducing the table's own text:

> 1 | Multiple Choice Item | Understand and apply theorems about circles. | Prove that all circles are similar using transformational arguments. (G.C.1) | C | 1 point

and from Sp22, the row that shows the extra DOK column and a starred standard:

> 8 | Equation Item | Define trigonometric ratios, and solve problems involving right triangles. | Solve problems involving right triangles.★ / a. Use trigonometric ratios and the Pythagorean Theorem to solve right triangles in applied problems if one of the two acute angles and a side length is given. | Level 2 | --- | 1 point

`---` in the Answer Key column is the document's own marker for a non-multiple-choice item,
used where a letter key would otherwise sit.
