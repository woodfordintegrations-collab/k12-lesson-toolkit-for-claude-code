---
source_url: https://www.jmap.org/ (plus https://www.jmap.org/htmlstandard/G.SRT.{B.4,B.5,C.6,C.7,C.8}.htm, https://jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.pdf, https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions2.pdf, https://www.nysed.gov/terms-of-use, https://www.nysedregents.org/)
fetched: 2026-08-08
http_status: see the per-URL table in section 0; all 200 except one 404 noted there
role: primary
covers: source-jmap
---

## 0 · Fetch log

Every byte below came from `curl` written to disk and read from disk. No summarizing layer
was used anywhere in this extract, per the CONFIG evidence floor. Fetch clock: the machine
reported `2026-08-08 04:28:52 UTC` / `2026-08-07 21:28:52 PDT` at the end of the run, so
`fetched: 2026-08-08` is the UTC date.

| URL | HTTP | Content-Type | Bytes |
|---|---|---|---|
| `https://www.jmap.org/` | 200 | text/html | 29257 |
| `https://www.jmap.org/htmlstandard/G.SRT.B.4.htm` | 200 | text/html | 29688 |
| `https://www.jmap.org/htmlstandard/G.SRT.B.5.htm` | 200 | text/html | 39460 |
| `https://www.jmap.org/htmlstandard/G.SRT.C.6.htm` | 200 | text/html | 22869 |
| `https://www.jmap.org/htmlstandard/G.SRT.C.7.htm` | 200 | text/html | 22793 |
| `https://www.jmap.org/htmlstandard/G.SRT.C.8.htm` | 200 | text/html | 39140 |
| `https://jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.pdf` | 200 | application/pdf | 143957 |
| `https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions2.pdf` | 200 | application/pdf | 86192 |
| `https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.tst` (HEAD) | 200 | text/x-c | n/a |
| `https://www.jmap.org/Worksheets/G.SRT.C.7.Cofunctions1.doc` (HEAD) | 200 | application/msword | n/a |
| `https://www.jmap.org/JMAP_WORKSHEETS.htm` | 200 | text/html | 24203 |
| `https://www.jmap.org/htmlsupport/ABOUT_JMAP.htm` | **404** | text/html | 355 |
| `https://www.nysedregents.org/` | 200 | text/html | 10334 |
| `https://www.nysedregents.org/geometrycc/` | 200 | text/html | 22598 |
| `https://www.nysedregents.org/geometrycc/117/geomcc12017-exam.pdf` | 200 | application/pdf | 211515 |
| `https://www.nysedregents.org/geometrycc/117/geomcc12017-rg.pdf` | 200 | application/pdf | 71584 |
| `https://www.nysed.gov/terms-of-use` | 200 | text/html | 54267 |
| `https://www.nysed.gov/copyright` | **404** | text/html | 48125 |
| `https://www.nysed.gov/terms-use` | **404** | text/html | 48125 |

Failure-mode note: the two `nysed.gov` 404s are soft-404s in the sense that they return a
48125-byte styled page rather than a bare error body, but the status line is a genuine 404,
not a 200. The JMAP `ABOUT_JMAP.htm` 404 is a hard Apache 404 with a 355-byte body reading
`404 Not Found / Not Found / The requested URL was not found on this server.` Neither is a
bot block: nothing in this cluster returned 403 or 406.

Encoding note: JMAP serves `charset=windows-1252`. All quotations below were taken after
`iconv -f WINDOWS-1252 -t UTF-8`, which is why the copyright symbol resolves; read as UTF-8
the same byte is U+FFFD.

---

## 1 · JMAP's own copyright statement, verbatim

The statement is in the footer table of every JMAP page checked (home page and all five
`htmlstandard/` pages). Byte-exact after windows-1252 decoding, with the source HTML
entity noted:

> Copyright © 2004-now&nbsp; JMAP, Inc. - All rights reserved

Rendered, `&nbsp;` is a non-breaking space, so a reader sees two spaces between `2004-now`
and `JMAP, Inc.`. `od -c` on the decoded bytes confirms the sequence
`C o p y r i g h t   ©   2 0 0 4 - n o w & n b s p ;   J M A P ,   I n c .   -   A l l   r i g h t s` followed by a line break and `reserved`.
The separator before "All rights reserved" is a HYPHEN-MINUS, not an em dash.

The sentence immediately after it in the same table cell, which is the only other
rights-adjacent text on the page:

> JMAP, Inc. is a 501(c)(3) New York Not-for-Profit Corporation

And immediately before it:

> Questions should be directed to JMAP's Editor, Steve Sibol or Cofounder, Steve Watson

**There is no licence page, no terms page, and no permissions page.** `grep -i` for
`copyright|©|&copy;|reserved|permission|terms|licen` over the raw bytes of
`htmlstandard/G.SRT.C.7.htm` returned zero hits before the windows-1252 decode and, after
decoding, only the footer line above. `htmlsupport/ABOUT_JMAP.htm` is a 404. So the whole of
JMAP's rights position, as delivered, is that one all-rights-reserved compilation notice.

---

## 2 · The per-standard worksheet index: structure

Each `htmlstandard/<CODE>.htm` page is a single table. Its shape is constant across all five
standards checked:

```
row 1 (colspan 4) :  STANDARD <CODE>
                     <course abbreviation>
                     <the standard's text>
rows 2..n         :  [row-group label]  |  worksheet name        |  count column  |  format links
                        REGENTS            "Regents-<Topic> <n>"    "3/26"           TST PDF DOC
                        WORKSHEETS         <series codes line>
                                           [optional qualifier]
                        PRACTICE           "Practice-<Topic>"       "7"              WS PDF
                        WORKSHEETS
                        & JOURNALS         "Journal-<Topic>"        "3"              WS PDF
                        LINK               "Wikipedia-Cofunctions"   -               LINK
```

The middle two columns are positionally paired: the series-code line (`GEO/GEO`, `GE/A`,
`B/SIII`, `GEO/GEO/IA/A/SIII`) has one slash-separated token per one slash-separated integer
in the count column. On G.SRT.C.7, `GEO`/`GEO` pairs with `3`/`26`, and `B`/`SIII` pairs with
`1`/`15`. The first token of each pair is emitted inside `<b>` on the CCSS rows.

**What the series abbreviations decode to is NOT stated anywhere in the delivered bytes.**
The left navigation offers the only adjacent evidence, a "JMAP RESOURCE ARCHIVES" block
listing `Current Standards`, `CCSS (2015-2026)`, `IA/GE/A2 (2007-17)`, `Math A/B (1998-2010)`.
A page-writer must either treat the mapping as unresolved or ground it in the REF suffixes in
section 4, which are independent evidence.

### 2a · G.SRT.C.7, the full table, verbatim

Standard text as printed on the page:

> Explain and use the relationship between the sine and cosine of complementary angles

| Group | Worksheet | Series | Counts | Formats |
|---|---|---|---|---|
| REGENTS WORKSHEETS | Regents-Cofunctions 1 | **GEO**/GEO | **3**/26 | TST PDF DOC |
| REGENTS WORKSHEETS | Regents-Cofunctions 2 | B/SIII | 1/15 | TST PDF DOC |
| LINK | Wikipedia-Cofunctions | | | LINK (to `https://en.wikipedia.org/wiki/Cofunction`) |

C.7 is the only one of the five standards with **no** PRACTICE WORKSHEETS group.

### 2b · The other four standards

Standard texts as printed (G.SRT.B.4 and B.5 carry bulleted sub-clauses which are reproduced
in full in the raw capture; the head sentence is given here):

- **G.SRT.B.4**: `Prove and apply similarity theorems about triangles.` followed by
  `• Include multi-step proofs and algebraic problems built upon these concepts.` and
  `• Examples of theorems include but are not limited to:` with three sub-bullets (side
  parallel to one side divides proportionally; altitude to the hypotenuse is the geometric
  mean; the centroid divides each median in the ratio 2:1).
- **G.SRT.B.5**: `Use congruence and similarity criteria for triangles to:` / `a. Solve
  problems algebraically and geometrically.` / `b. Prove relationships in geometric figures.`
  plus two bullets, one of which reads `• This standard is a fluency recommendation.`
- **G.SRT.C.6**: `Understand that by similarity, side ratios in right triangles are
  properties of the angles in the triangle, leading to definitions of sine, cosine and
  tangent ratios for acute angles.`
- **G.SRT.C.8**: `Use sine, cosine, tangent, the Pythagorean Theorem and properties of
  special right triangles to solve right triangles in applied problems.` plus
  `Special right triangles refer to the 30-60-90 and 45-45-90 triangles.`

Worksheet rows, verbatim, name / series / counts:

**G.SRT.B.4** (7 Regents rows, 3 Practice rows)

| Worksheet | Series | Counts | Formats |
|---|---|---|---|
| Regents-Side Splitter Theorem 1 | GEO | 4 | TST PDF DOC |
| Regents-Side Splitter Theorem 2 | GEO | 27 | TST PDF DOC |
| Regents-Side Splitter Theorem 3 | GE/A | 12/1 | TST PDF DOC |
| Regents-Similarity 1 | GEO/GEO | 4/26 | TST PDF DOC |
| Regents-Similarity 2 | GE/B | 17/4 | TST PDF DOC |
| Regents-Medians, Altitudes and Bisectors | GEO/GEO/GE/B | 1/5/3/1 | TST PDF DOC |
| Regents-Centroid, Orthocenter, Incenter and Circumcenter | GEO/GEO/GE | 1/5/24 | TST PDF DOC |
| Practice-Side Splitter Theorem | | 7 | WS PDF |
| Practice-Similarity | | 4 | WS PDF |
| Practice-Centroid, Orthocenter, Incenter and Circumcenter | | 3 | WS PDF |

**G.SRT.B.5** (8 Regents rows, 16 Practice rows, 2 Journal rows). B.5 adds a qualifier
sub-line inside the worksheet-name cell that the other standards mostly lack:

| Worksheet | Qualifier | Series | Counts |
|---|---|---|---|
| Regents-Similarity 1 | basic | GEO/GEO | 4/26 |
| Regents-Similarity 2 | basic | GE/A | 8/6 |
| Regents-Similarity 3 | perimeter and area | GEO/GEO/GE/A | 2/3/8/7 |
| Regents-Triangle Congruency | | GEO/GE | 5/11 |
| Regents-Triangle Proofs 1 | statements | GEO/GEO/GE/B | 1/9/9/8 |
| Regents-Triangle Proofs 2 | proof | GEO/GE/B | 5/6/1 |
| Regents-Quadrilateral Proofs | | GEO/GEO/GE/B | 3/14/7/5 |
| Regents-Circle Proofs | | GEO/GE/B/SIII | 3/3/4/3 |

Practice rows for B.5, name and count: Practice-Similarity 1 (basic) 11; Practice-Similarity 2
(basic) 7; Practice-Similarity 3 (collinear side) 7; Practice-Similarity 4 (parallel sides) 8;
Practice-Similarity 5 (basic) 6; Practice-Similarity 6 (perimeter) 6;
Practice-Triangle Congruency 5; Practice-Triangle Proofs 1 (statements) 6;
Practice-Triangle Proofs 2 (statements) 6; Practice-Triangle Proofs 3 (statements) 12;
Practice-Triangle Proofs 4 (statements) 6; Practice-Triangle Proofs 5 (HL) 5;
Practice-Triangle Proofs 6 (proofs) 8; Practice-Triangle Proofs 7 (proofs, CPCTC) 12;
Practice-Quadrilateral Proofs 3; Practice-Circle Proofs 3; Journal-Similarity 3;
Journal-Triangle Proofs 4.

**G.SRT.C.6** (1 Regents row, 1 Practice row), the thinnest of the five.

| Worksheet | Series | Counts | Formats |
|---|---|---|---|
| Regents-Trigonometric Ratios 1 | GEO/GEO/IA/A/SIII | 1/6/14/2/2 | TST PDF DOC |
| Practice-Trigonometric Ratios | | 10 | WS PDF |

**G.SRT.C.8** (12 Regents rows, 8 Practice rows, 1 Journal row), the thickest.

| Worksheet | Qualifier | Series | Counts |
|---|---|---|---|
| Regents-Pythagorean Theorem 1 | graphics | IA/GE/A/B | 7/3/5/1 |
| Regents-Pythagorean Theorem 2 | without graphics | IA/A | 6/7 |
| Regents-Pythagorean Theorem 3 | triples | IA/GE/A | 2/3/2 |
| Regents-Special Right Triangles | | GEO/GEO/IA/A/B/SIII | 3/2/1/1/5/1 |
| Regents-Using Trigonometry to Find a Side 1 | | GEO | 8 |
| Regents-Using Trigonometry to Find a Side 2 | MC | GEO | 18 |
| Regents-Using Trigonometry to Find a Side 3 | open ended | GEO | 27 |
| Regents-Using Trigonometry to Find a Side 4 | | IA/A2 | 13/2 |
| Regents-Using Trigonometry to Find a Side 5 | | A | 17 |
| Regents-Using Trigonometry to Find a Side 6 | | B/SIII | 7/7 |
| Regents-Using Trigonometry to Find an Angle 1 | | GEO/GEO | 3/22 |
| Regents-Using Trigonometry to Find an Angle 2 | | IA/A2/A/SIII | 14/3/6/1 |

Practice/Journal rows for C.8: Practice-Pythagorean Theorem 1 15;
Practice-Pythagorean Theorem 2 (triples) 10; Journal-Pythagorean Theorem (converse) 1;
Practice-30-60-90 Triangles 10; Practice-Using Trigonometry to Find a Side 1 10;
Practice-Using Trigonometry to Find a Side 2 15; Practice-Using Trigonometry to Find a Side 3 10;
Practice-Using Trigonometry to Find a Side 4 6; Practice-Using Trigonometry to Find an Angle 14.

**Do not add these numbers together and publish the sum as a fact about the standard.** Two
worksheets on B.4 and B.5 share the same name (`Regents-Similarity 1`, series `GEO/GEO`,
counts `4/26`), so items are indexed under more than one standard and a naive total
double-counts.

---

## 3 · File formats offered per worksheet

Two distinct format sets, measured from the `href` attributes:

- **Regents worksheets**: three links per row, `TST` / `PDF` / `DOC`, resolving to
  `../Worksheets/<NAME>.tst`, `.pdf`, `.doc`.
- **Practice worksheets and Journals**: two links per row, `WS` / `PDF`, resolving to
  `../Worksheets/<NAME>PR.ws` and `.pdf` (the `PR` suffix is part of the practice-file
  basename, for example `G.SRT.C.6.TrigonometricRatiosPR.ws`).

All three Regents extensions HEAD 200 on `G.SRT.C.7.Cofunctions1`:
`.tst` returns `Content-Type: text/x-c`, `.doc` returns `application/msword`,
`.pdf` returns `application/pdf`. The `text/x-c` on `.tst` is the server's MIME guess, not a
statement about the file's real format.

The site-wide format legend on `JMAP_WORKSHEETS.htm` lists a fourth token this unit does not
reach: the FORMAT column there reads `TST PDF DOC TNS` for AI/GEO/AII and `PDF TNS` for CALC.
The left navigation carries an `EXAMVIEW` link pointing at
`https://examview-assessment-suite.software.informer.com/amp/6.1/`.
**JMAP never defines TST, DOC, WS or TNS in the delivered bytes.** Any expansion of those
abbreviations is inference, not evidence.

---

## 4 · The REF code: format and decoding

Every item in the answer section of a worksheet PDF carries a `REF:` tag. Extracted with
`pdftotext -layout`, in document order.

### 4a · G.SRT.C.7.Cofunctions1.pdf, 29 REF codes

Count measured: `grep -c "REF:"` returns **29**, and the standard page's count column for this
worksheet reads `3/26`.

```
 1 061512geo    2 081919geo    3 012304geo    4 062312geo    5 082403geo
 6 062206geo    7 011609geo    8 082210geo    9 012606geo   10 011922geo
11 082311geo   12 061703geo   13 081606geo   14 081504geo   15 012401geo
16 061909geo   17 061808geo   18 081721geo   19 081824geo   20 062420geo
21 062619geo   22 012021geo   23 062529geo   24 012531geo   25 061628geo
26 fall1407geo 27 spr1407geo  28 011827geo   29 011727geo
```

### 4b · G.SRT.C.7.Cofunctions2.pdf, 16 REF codes

Count measured: `grep -c "REF:"` returns **16**, and the standard page reads `1/15`.

```
 1 010320b     2 069621siii   3 068025siii   4 068717siii   5 088622siii
 6 019729siii  7 089633siii   8 069825siii   9 089131siii  10 019428siii
11 089704siii 12 010404siii  13 088415siii  14 069912siii  15 060310siii
16 018712siii
```

### 4c · What the format decodes to

The regular form is **MMYYNNxxx**: a two-digit month, a two-digit year, a two-digit question
number within that exam, and a trailing alphabetic exam-series suffix. Grounding, from the
codes above set against the worksheet body:

- `061512geo`: the first item of Cofunctions 1, which is a June sitting, question 12.
- `012304geo`: a January sitting, question 04.
- `082403geo`: an August sitting, question 03.
- The suffix varies with the series column of section 2: Cofunctions 1 is `GEO/GEO` and every
  regular code there ends `geo`; Cofunctions 2 is `B/SIII` and its codes end `b` (one item,
  `010320b`) and `siii` (fifteen items).

**Two of the 29 codes in Cofunctions 1 do not fit MMYYNNxxx**, and this is a fact about the
format, not noise: `fall1407geo` and `spr1407geo`. Both replace the two-digit month with a
season word (`fall`, `spr`), keeping `14` as the year and `07` as the question number.

**The century is not in the code.** `069621siii` and `019729siii` sit in the same worksheet as
`010320b`. A two-digit year alone cannot separate 1996 from 2096, so the century is recoverable
only from the exam-series suffix, which is a property of when that series existed. Any decoding
that reads `96` as 2096 or `03` as 1903 is unfounded on the delivered bytes.

Do not restate a derived count such as "17 distinct sittings" without recomputing it from the
list above. This extract publishes the codes, not a derived tally.

---

## 5 · The defective released item in Cofunctions 2

Question 1 of `G.SRT.C.7.Cofunctions2.pdf`, REF `010320b`.

**Encoding note, load-bearing.** This PDF embeds `EAPBNI+SymbolMT` and `EAPBOJ+FSCSymbol` as
CID TrueType with Identity-H, so `pdftotext` emits Symbol-font glyphs into the Unicode Private
Use Area rather than as their standard characters. The mapping observed in this file, and the
only PUA codepoints present in it, is Symbol code + 0xF000:

| Extracted | Symbol slot | Renders as | Occurrences in file |
|---|---|---|---|
| U+F02B | 0x2B | `+` | 38 |
| U+F02D | 0x2D | `-` | 10 |
| U+F03D | 0x3D | `=` | 62 |
| U+F0B0 | 0xB0 | `°` | 22 |
| U+F0D0 | 0xD0 | `∠` | 2 |

Raw extraction of the question stem, PUA codepoints shown as escapes:

```
1 If sin6A  cos 9A, then mA is equal to
     1) 6 2) 36 3) 45 4) 1
```

Raw extraction of the answer-section entry, PUA codepoints shown as escapes:

```
  1 ANS: 1
    6A  9A  90. As originally written, distractor (3) was A  54, also a correct response.
       15A  90
         A6

    REF: 010320b
```

With the PUA codepoints resolved through the table above, the sentence JMAP wrote is:

> 6A + 9A = 90. As originally written, distractor (3) was A = 54, also a correct response.

Note precisely what the bytes do and do not contain. There is a U+F0D0 (`∠`) in the question
stem before `A`, and there is **no** U+F0D0 in the answer note, so the note reads `A = 54` and
not `m∠A = 54`. The distractor list in the stem is `1) 6 2) 36 3) 45 4) 1` with two of the four
choices rendered as stacked fractions that `pdftotext -layout` splits across lines; the keyed
answer is `ANS: 1`.

By contrast, `G.SRT.C.7.Cofunctions1.pdf` extracts as clean Unicode (`m∠C = 90°` comes through
directly), so the PUA problem is specific to the older document, not to JMAP generally.

---

## 6 · What Cofunctions 1's answer section contains

Structure per item: an item number, `ANS:` followed either by a keyed option digit (for
multiple choice) or by nothing (for constructed response), then worked lines, then `REF:`.
Some entries carry prose reasoning rather than algebra; the five reproduced below are the
ones inspected, and this extract does not publish a count of how many of the 29 do, because
that was not measured. Verbatim, from `pdftotext -layout` output which for this file is clean
Unicode:

> 25 ANS:
>    73 + R = 90 Equal cofunctions are complementary.
>          R = 17

> 27 ANS:
>    The acute angles in a right triangle are always complementary. The sine of any acute angle is equal to the cosine
>    of its complement.

> 28 ANS:
>    cos B increases because ∠A and ∠B are complementary and sinA = cos B.

> 29 ANS:
>    Yes, because 28º and 62º angles are complementary. The sine of an angle equals the cosine of its complement.

Item 26's note, which is the longest prose in the file:

> 26 ANS:
>    4x −.07 = 2x +.01 SinA is the ratio of the opposite side and the hypotenuse while cos B is the ratio of the adjacent
>          2x = 0.8
>           x = 0.4
>     side and the hypotenuse. The side opposite angle A is the same side as the side adjacent to angle B. Therefore,
>     sinA = cos B.

`sinA`, `sinC`, `tanA` and similar run-together forms are as printed; the space between the
function name and its argument is genuinely absent in the source for some items and present
for others (`sin A = sin B` in item 1's choices, `sinA = cos B` in item 2's).

The page header on every page of both worksheets reads:

> Regents Exam Questions G.SRT.C.7: Cofunctions 1                  Name: ________________________
> www.jmap.org

---

## 7 · The underlying items: NYSED's own reproduction terms

The items JMAP indexes are New York State Education Department Regents examination questions.
JMAP's own footer asserts a compilation copyright over its arrangement; it says nothing about
the items. NYSED's terms are a separate instrument on a separate host.

### 7a · Which host carries the terms

`https://www.nysedregents.org/` has **no** copyright, licence, terms or permission text of its
own: `grep -o -i -E ".{80}(copyright|reserved|reproduc|permission|&copy;).{140}"` over the raw
bytes of both `nysedregents.org/` and `nysedregents.org/geometrycc/` returned zero matches.

What it has instead is a footer link. Verbatim from the raw HTML of `nysedregents.org/`:

```html
 <div id="bottom_footer_link">
 <a href="http://www.nysed.gov/contact-NYSED">Contact NYSED</a> | 
 <a href="http://www.nysed.gov/about/index-a-z/">Index A - Z</a> | 
 <a href="http://www.nysed.gov/terms-of-use#Accessibility"> Accessibility</a> | 
 <a href="http://www.nysed.gov/terms-of-use">Terms of Use</a> 
 </div>
```

So `nysedregents.org`, the host that actually serves the exams, points at
`nysed.gov/terms-of-use` as its governing instrument. That link is the only bridge between the
two hosts, and a page-writer should say so in those words rather than asserting the two
hostnames are one rights domain.

The exam PDFs themselves carry nothing. `pdftotext -layout` over
`geometrycc/117/geomcc12017-exam.pdf` (211515 bytes, the January 2017 Geometry Common Core
exam) and over its rating guide `geomcc12017-rg.pdf` (71584 bytes), then
`grep -i -E "copyright|reserved|reproduc|permission|©"`, returned **zero hits in both**. The
exam's last printed line is `Printed on Recycled Paper`.

### 7b · The NYSED grant, verbatim

From `https://www.nysed.gov/terms-of-use`, HTTP 200, under the heading `Copyright`. This is one
continuous passage; the paragraph breaks are as rendered.

> Except as expressly provided to the contrary on any individual document(s) or material(s) published on the New York State Education Department Website, permission to copy, use, and distribute materials created by and/or credited to the New York State Education Department and contained on the New York State Education Department Website is hereby granted without fee for personal, private and educational purposes, except that reproducing materials for profit or any commercial use is strictly forbidden without express prior written permission of the New York State Education Department. Requests for permission should be sent to legal@nysed.gov. Any reproduction or distribution of such materials must expressly credit the State Education Department in a manner likely to inform any recipient as follows (Fill in information indicated by brackets and omit brackets):

> From the New York State Education Department. [Name of article/document.] Internet. Available from [specific webpage on State Education Department Website]; accessed [date, month, year].

> Permission to copy, use, and distribute materials as described above shall not extend to information housed on this Website that is credited to other sources, or to information on Websites to which this site links.

Three riders live inside that grant and must not be separated from it:

1. **The opening carve-out.** `Except as expressly provided to the contrary on any individual
   document(s) or material(s)` means a per-document statement overrides the site grant. The
   January 2017 exam PDF checked above contains no such statement, so nothing overrides it
   there, but this is a per-document question and cannot be answered once for the archive.
2. **The commercial bar.** `reproducing materials for profit or any commercial use is strictly
   forbidden without express prior written permission`.
3. **The third-party exclusion, and the linked-site exclusion.** The final paragraph withdraws
   the grant from anything `credited to other sources` and from `information on Websites to
   which this site links`. JMAP is a website nysed.gov does not link, and jmap.org is not the
   NYSED website, so this grant does not travel to JMAP's copies by its own terms.

**The attribution format is mandatory and prescribed**, not free-form: the bracketed template
above is the required wording.

### 7c · What this extract does NOT establish

It does not establish a "school-use reproduction only, no electronic distribution" restriction.
The word `electronic` does not appear in the granting passage, `distribute` does appear and is
granted, and the qualifiers actually written are `personal, private and educational purposes`
plus the for-profit bar. If a page needs the narrower claim, it needs a different pasted
sentence from a different NYSED instrument, and this extract does not contain one.

---

## 8 · JMAP self-description, for the corpus record

From the promotion block at the head of every JMAP page:

> JMAP 's first iteration began with 611 Math A Regents questions after the January 2005 Exam.

> Revised for the 2005, CC and current curricula, JMAP now offers 10,212 questions.

> Please consider a $10 donation to acknowledge this milestone and this website's impact on high school mathematics education for over 20 years!

The banner above it reads `10,000+ Regents Questions on JMAP`. The archive navigation labels
its three eras `CCSS (2015-2026)`, `IA/GE/A2 (2007-17)` and `Math A/B (1998-2010)`, and the
exam archive is labelled `1866-now`. These figures are JMAP's own claims about itself, not this
project's measurements, and F4 requires they be attributed that way.
