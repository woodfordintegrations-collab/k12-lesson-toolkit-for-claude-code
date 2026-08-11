---
source_url: https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/outcomes ; https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage-5/facb3aa952 ; https://www.nsw.gov.au/education-and-training/nesa/copyright
fetched: 2026-08-08
http_status: 200 / 200 / 200 for the three above; 404 for the URL recorded in INVENTORY.md (see section 1)
role: primary
covers: source-nesa-nsw
---

## 0 · Fetch log

Every request was made with `curl` and written to disk, then parsed from disk. No summarizing
layer was used, per the CONFIG evidence floor. Fetch clock:
`2026-08-08 04:28:52 UTC` / `2026-08-07 21:28:52 PDT`.

| URL | HTTP | Final URL | Bytes |
|---|---|---|---|
| `.../mathematics-k-10-2022/content/stage5/fa63d5e5b6` | **404** | `https://curriculum.nsw.edu.au/404?path=learning-area/mathematics/mathematics-k-10-2022/content/stage5` | 1155830 |
| `.../mathematics-k-10-2022/content/stage5` | **404** | `https://curriculum.nsw.edu.au/404?path=/learning-areas/mathematics/mathematics-k-10-2022/content/stage5/fad5496b8e` | 1155830 |
| `.../mathematics-k-10-2022/outcomes` | 200 | same | 2010655 |
| `.../mathematics-k-10-2022` | 200 | `.../mathematics-k-10-2022/overview` | 1531022 |
| `.../mathematics-k-10-2022/content/stage-5/facb3aa952` | 200 | same | 7597010 |
| `https://www.nsw.gov.au/education-and-training/nesa/copyright` | 200 | same | 154236 |

---

## 1 · The URL in INVENTORY.md is dead, and how it fails matters

INVENTORY.md row `source-nesa-nsw` cites:

```
https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage5/fa63d5e5b6
```

At this fetch it returns **HTTP 404**. Naming the failure mode precisely, because the retired
vocabulary requires it: this is **not** a bot block (no 403, no 406), **not** a TLS failure,
and **not** genuinely gone. It is a **soft-404 with a redirect**: the server issues a redirect
to `/404?path=...` and then serves a 1155830-byte fully-styled site page under a genuine 404
status line. A checker that looks only at "did bytes come back" or "does the page render" would
mark the URL healthy. Only the status line reveals it.

Two details in the redirect are diagnostic:

1. The redirect target rewrites `learning-areas` to `learning-area`, dropping the plural. The
   live path is `learning-areas`.
2. The redirect target drops the trailing hash `fa63d5e5b6`, and on the second probe the server
   substituted a different hash of its own, `fad5496b8e`. The live Stage 5 content hash is
   **`facb3aa952`**, and the live path segment is **`stage-5`** with a hyphen, not `stage5`.

Live path, measured from the internal link list on the outcomes page:

```
https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/content/stage-5/facb3aa952
```

The whole family of stage paths on this site takes the same hyphenated form and its own hash:
`content/early-stage-1/fa000b1c71`, `content/stage-1/fa26b2cd40`, `content/stage-2/fa3867d7b8`,
`content/stage-3/fa87632ef7`, `content/stage-4/fa783c951a`, `content/stage-5/facb3aa952`, plus
`content/k/fad5496b8e`, `content/life-skills/fad5496b8e` and `content/year-1` through
`content/year-10`, all of which carry `fad5496b8e`. **These hashes are part of the URL and are
not stable across the site's own redirects**, which is a durable warning for any citation into
this host.

---

## 2 · MA5-TRG-P-02: the outcome text, verbatim

The site does not serve outcome text as HTML prose. It embeds a JSON payload in the page and
renders from it client-side. The extraction below decodes that payload with a real JSON string
decoder, so the apostrophes and en dashes are the source's own characters and not an artefact.

Source object, byte-exact from
`https://curriculum.nsw.edu.au/learning-areas/mathematics/mathematics-k-10-2022/outcomes`:

```json
"code":{"name":"📜 Code","type":"text","value":"MA5-TRG-P-02"},
"title":{"name":"📜 Title","type":"text","value":""},
"description":{...,"name":"📜 Description","type":"rich_text",
  "value":"<p>establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations <em>(Path: Adv)</em></p>"}
```

and its system record:

```json
"system":{"codename":"ma_k_10_ms_oc_ma5_trg_p_02","collection":"default",
"id":"de3383e2-fe63-4b91-aea5-2a76fa8edbc2","language":"default",
"lastModified":"2022-11-24T08:20:08.826426Z","name":"MA5-TRG-P-02",
"sitemapLocations":[],"type":"outcome","workflowStep":"published"}
```

With the HTML stripped, the outcome text is:

> establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations (Path: Adv)

`(Path: Adv)` is italicised in the source (`<em>`), and `title` is an empty string, so the code
is the outcome's only name.

**This text does not name the complementary-angle relationship.** `grep` for `complementary` and
for `Complementary` over the whole 2010655-byte outcomes page returns **0** occurrences of each.
INVENTORY.md's source line describes MA5-TRG-P-02 as "naming the complementary relationship
explicitly." Against the bytes fetched here, that is not what the outcome says. What is true is
in section 3.

### 2a · The other three Stage 5 Trigonometry outcomes, for contrast

Same extraction method, same page.

| Code | Outcome text |
|---|---|
| MA5-TRG-C-01 | applies trigonometric ratios to solve right-angled triangle problems |
| MA5-TRG-C-02 | applies trigonometry to solve problems, including bearings and angles of elevation and depression |
| MA5-TRG-P-01 | applies Pythagoras’ theorem and trigonometry to solve 3-dimensional problems and applies the sine, cosine and area rules to solve 2-dimensional problems, including bearings (Path: Stn, Adv) |
| MA5-TRG-P-02 | establishes and applies the properties of trigonometric functions and finds solutions to trigonometric equations (Path: Adv) |

The apostrophe in `Pythagoras’` is U+2019, as in the source.

### 2b · MA5-TRG-P-02's own taxonomy fields

From the same object, verbatim values:

- `syllabus`: `Mathematics K–10 (2022)`, codename `mathematics_k_10_2022`. The dash in the
  syllabus name is an EN DASH in the source.
- `syllabus_type__items`: `Mainstream`
- `stages__stages`: `Stage 5`
- `stages__stage_years`: `9`, `10`
- `isoverarching`: `No`
- `relatedlifeskillsoutcomes`: empty
- `lastModified`: `2022-11-24T08:20:08.826426Z`

**The `P` in the code and the `(Path: Adv)` suffix mark this as a Path outcome, not core Stage 5
content.** The two core Stage 5 Trigonometry outcomes are MA5-TRG-C-01 and MA5-TRG-C-02, and
neither mentions complementary angles. Any claim about what NSW requires of all Stage 5 students
has to reckon with that distinction, and this extract does not resolve it because the syllabus's
own definition of a Path outcome was not fetched.

---

## 3 · Where NESA does name the complementary relationship

Measured on the live Stage 5 content page (`content/stage-5/facb3aa952`, HTTP 200, 7597010
bytes). `complementary` occurs 26 times there; `MA5-TRG-P-02` occurs 4 times.

### 3a · The focus area to outcome mapping, measured not assumed

Each focus-area object in the payload links its outcome by codename. Extracted by locating each
`"name":"MS S5 Trigonometry <X>","sitemapLocations":[],"type":"focusarea"` record and reading
the outcome codenames inside that object:

| Focus area | `type` | Linked outcome codename |
|---|---|---|
| MS S5 Trigonometry A | focusarea | `ma5_trg_c_01` |
| MS S5 Trigonometry B | focusarea | `ma5_trg_c_02` |
| MS S5 Trigonometry C (Path) | focusarea | `ma5_trg_p_01` |
| MS S5 Trigonometry D (Path) | focusarea | `ma5_trg_p_02` |

So **Trigonometry D (Path) is the focus area of MA5-TRG-P-02**, established from the payload's
own link, not inferred from the letter ordering.

### 3b · The content group under it

Two content groups sit under Trigonometry D. Verbatim `title` values and their codenames:

- `ma_k_10_cg_trd_sol`: **`Solve trigonometric equations using exact values and the relationships between supplementary and complementary angles`**
- `ma_k_10_cg_trd_utu`: `Use the unit circle to define trigonometric functions and represent them graphically`

Full system record of the first:

```json
"system":{"codename":"ma_k_10_cg_trd_sol","collection":"default",
"id":"8b768e63-4f14-484b-8f28-b0e5eb5b8aaf","language":"default",
"lastModified":"2023-10-25T05:07:15.4855934Z",
"name":"MS S5 Solve trigonometric equations using exact values and the relationships between supplementary and complementary angles",
"sitemapLocations":[],"type":"contentgroup","workflowStep":"published"}
```

Its `code` field reads `MA_K_10_CG_TRD_SOL`, its `stages__stage_years` are `9` and `10`, and its
`content_items` field lists four children:

```json
"content_items":{"name":"📄 Content Items","type":"modular_content",
"value":["ma_k_10_cp_trd_sol_stg5_01","ma_k_10_cp_trd_sol_stg5_02",
"ma_k_10_cp_trd_sol_stg5_03","ma_k_10_cp_trd_sol_stg5_04"],"linkedItems":[]}
```

**Those four content-point objects are NOT in the delivered bytes.** `linkedItems` is empty and
no object with any of those four codenames exists in the payload. The site lazy-loads them. So
the text of the four individual NSW content points under this group is a genuine gap in this
extract, and a page must not paraphrase content it has not fetched.

### 3c · What IS in the delivered bytes: the Trigonometry D key ideas

The `teachingadvice` object `n5__trigonometry_d__path_` carries a `content` rich_text field
whose Key ideas list is present in full. Decoded from the payload's escapes, verbatim:

> Key ideas
> Students:
>
>   prove that the tangent ratio can be expressed as a ratio of the sine and cosine ratios
>   compare the features of sine, cosine and tangent curves from their graphs for angles of any magnitude, including negative angles
>   apply the relationships for obtuse angles
>   apply the sine rule and area rule to find angles involving the ambiguous case
>   relate the gradient of a line to its angle of inclination on the Cartesian plane
>   apply the exact sine, cosine and tangent ratios for angles of 30°, 45° and 60°
>   apply the relationships between the sine and cosine ratios of complementary angles in right-angled triangles
>   find the possible acute and/or obtuse angle(s) given a trigonometric ratio
>
> Key terms
>
>   acute angle
>   angle of inclination
>   Cartesian plane
>   complementary angles
>   cosine rule
>   obtuse
>   Pythagoras’ theorem
>   sine rule
>   tangent ratio
>   trigonometric ratio
>   unit circle

The seventh bullet is the closest NESA statement located to the G.SRT.C.7 idea:

> apply the relationships between the sine and cosine ratios of complementary angles in right-angled triangles

Attribute it correctly. It is a **Key ideas bullet inside NESA's teaching advice** for
Trigonometry D (Path), which is the focus area of MA5-TRG-P-02. It is not the outcome text, and
it is not one of the four syllabus content points, which were not delivered.

For the C.6-adjacent comparison, the Trigonometry A content group present in the same payload is
titled:

> Demonstrate and explain the constancy of trigonometric ratios for a given angle in right-angled triangles

### 3d · A false-positive warning for anyone grepping this host

Most of the 26 `complementary` hits on the Stage 5 page are **probability**, not trigonometry:
`Determine probabilities for complementary events` (Stage 4), `complementary events` in three
separate Key terms lists, `Recognising and describing complementary events` in background
knowledge. A keyword search for `complementary` over NESA returns probability content by a wide
margin. Two further hits are Stage 4 geometry (`complementary angles` in an angle-relationships
Key terms list, and `Bearings connects to geometrical properties for angles at a point,
complementary and supplementary angles.`).

---

## 4 · NESA's copyright terms, verbatim

The syllabus site does not carry the terms inline. Its footer holds a `copyright` weblink object
whose `link_url` is, byte-exact from the payload:

```json
"link_url":{"name":"🔗 Link Url","type":"text","value":"https://www.nsw.gov.au/education-and-training/nesa/copyright"}
```

and the syllabus page footer itself renders only `NESA © 2026 Privacy` plus a bare
`Copyright © 2026` in the site chrome, with no named holder and no terms.

The linked page, `https://www.nsw.gov.au/education-and-training/nesa/copyright`, HTTP 200,
154236 bytes, titled `NESA Copyright | NSW Government`, attributed at its head to
`© NSW Education Standards Authority`. Its full body, verbatim, headings included:

> **Copyright disclaimer**
>
> The documents on the NSW Education Standards Authority (NESA) website and the NSW Curriculum website contain material prepared by NESA for and on behalf of the Crown in right of the State of New South Wales. The material is protected by Crown copyright.
>
> These websites hold the only official and up-to-date versions of the documents available on the internet. Any other copies of these documents, or parts of these documents, that may be found elsewhere on the internet might not be current and are not authorised. You cannot rely on copies from any other source.
>
> All rights are reserved. No part of the material may be:
>
> - reproduced in Australia or in any other country by any process, electronic or otherwise, in any material form
> - transmitted to any other person or stored electronically in any form without the written permission of NESA except as permitted by the Copyright Act 1968 (Cth).
>
> When you access the material, you agree:
>
> - to use the material for research or study, criticism or review, reporting news and parody or satire
> - to use the material for information purposes only
> - not to modify the material or any part of the material without the written permission of NESA
> - to reproduce a single copy for personal bona fide study use only and not to reproduce any major extract or the entire material without the permission of NESA
> - to include this copyright notice in any copy made
> - to acknowledge that NESA is the source of the material.
>
> The documents may include third-party copyright material such as photos, diagrams, quotations, cartoons and artworks. This material is protected by Australian and international copyright laws and may not be reproduced or transmitted in any format without the copyright owner’s permission. Unauthorised reproduction, transmission or commercial use of such copyright material may result in prosecution.
>
> NESA has made all reasonable attempts to locate the owners of third-party copyright material. NESA invites anyone from whom permission has not been sought to contact the Copyright Officer.
>
> **Special arrangements applying to the NSW Curriculum Reform**
>
> As part of the NSW Curriculum Reform process, NESA grants a limited non-exclusive licence to:
>
> - teachers employed in NSW government schools and registered non-government schools
> - parents of children registered for home schooling
>
> to use, modify and adapt the NSW syllabuses for **non-commercial educational use only**. The adaptation must not have the effect of bringing NESA into disrepute.
>
> **Note:** The above arrangements do not apply to private/home tutoring companies, professional learning service providers, publishers, and other organisations.
>
> For more information on the above or for **commercial use or any other purpose**, please contact the Copyright Officer for permission.
>
> Email: copyright@nesa.nsw.edu.au

The bold in `non-commercial educational use only`, `Note:` and `commercial use or any other
purpose` is the source's own emphasis, preserved because it marks the operative restrictions.
The `lastModified` on the copyright weblink object is `2025-06-12T05:04:49.8941888Z`.

### 4a · The three riders, kept next to the grant

1. **The baseline is all rights reserved under Crown copyright**, with a statutory carve-out for
   whatever the `Copyright Act 1968 (Cth)` independently permits. Nothing here is a Creative
   Commons instrument.
2. **The Curriculum Reform licence is closed by class of person, not by use.** It reaches
   teachers employed in NSW government and registered non-government schools, and home-schooling
   parents. The `Note:` then explicitly excludes `private/home tutoring companies, professional
   learning service providers, publishers, and other organisations`. A curriculum-resource
   project is not in the granted class.
3. **Third-party material inside NESA documents is excluded entirely**, and NESA states it has
   not located every owner.

The list of things a user agrees to on access is worth reading as a whole rather than
cherry-picked: `criticism or review` and `reporting news` sit alongside
`to reproduce a single copy for personal bona fide study use only`. Nothing in the passage
grants redistribution.

---

## 5 · What is NOT established here

- **The comparative finding is not in this file.** INVENTORY.md's second and third source lines
  point at two local files under `Projects/HS Geometry/sources/` for the claim that C.7 is absent
  by specification from AQA GCSE, ACARA v9, Ontario, Singapore E-Math and the post-2023 NCERT.
  Those are a different cluster's staging job. Nothing about AQA, ACARA, Ontario, Singapore or
  NCERT was fetched here, and nothing in this file supports a claim about them.
- **The four NSW content points under `ma_k_10_cg_trd_sol` were not delivered** and their text is
  unknown to this extract. See section 3b.
- **Whether MA5-TRG-P-02 is core or elective for a given NSW student is unresolved.** The code
  says `Path` and `(Path: Adv)`; the syllabus's definition of a Path outcome was not fetched.
- **NESA's own assessment materials were not fetched.** Nothing here says whether or how the
  complementary relationship is examined in NSW.
