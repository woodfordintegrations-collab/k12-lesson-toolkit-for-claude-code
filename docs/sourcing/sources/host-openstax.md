---
source_url: https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=<SLUG>&fields=license_name,license_version (ten slugs, listed in section 1) ; https://openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry ; https://openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry ; https://openstax.org/details/books/algebra-and-trigonometry-2e
fetched: 2026-08-08
http_status: 200 on all thirteen requests
role: primary
covers: source-openstax
---

## 0 · Fetch log

Every request below was made with `curl` and its response body written to disk, then read from
disk. No summarizing layer was used, per the CONFIG evidence floor, which matters unusually
much here because the finding is a contradiction between two strings on the same page. Fetch
clock: `2026-08-08 04:28:52 UTC` / `2026-08-07 21:28:52 PDT`.

| Request | HTTP | Bytes |
|---|---|---|
| CMS API, ten book slugs (section 1) | 200 × 10 | 630 to 705 each |
| `openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry` | 200 | 451140 |
| `openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry` | 200 | 434277 |
| `openstax.org/details/books/algebra-and-trigonometry-2e` | 200 | 12410 |

No 403, no 404, no redirect, no TLS problem anywhere in this cluster.

---

## 1 · The CMS API: the authoritative check, and its raw output

Endpoint form:

```
https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=<SLUG>&fields=license_name,license_version
```

It returns JSON. The two fields that matter are `license_name` and `license_version`, both
inside `items[0]`. Ten slugs were queried. Every one returned `"total_count": 1`.

### 1a · The two slugs INVENTORY.md names

`slug=algebra-and-trigonometry`, complete response body, byte-exact:

```json
{
    "meta": {
        "total_count": 1
    },
    "items": [
        {
            "id": 38,
            "meta": {
                "slug": "algebra-and-trigonometry",
                "type": "books.Book",
                "detail_url": "https://openstax.org/apps/cms/api/v2/pages/38/",
                "html_url": "https://openstax.org/details/books/algebra-and-trigonometry",
                "first_published_at": "2016-03-09T09:53:01.890636-06:00",
                "locale": "en"
            },
            "title": "Algebra and Trigonometry",
            "license_name": "Creative Commons Attribution License",
            "license_version": "4.0"
        }
    ]
}
```

`slug=precalculus`, complete response body, byte-exact:

```json
{
    "meta": {
        "total_count": 1
    },
    "items": [
        {
            "id": 37,
            "meta": {
                "slug": "precalculus",
                "type": "books.Book",
                "detail_url": "https://openstax.org/apps/cms/api/v2/pages/37/",
                "html_url": "https://openstax.org/details/books/precalculus",
                "first_published_at": "2016-03-09T09:50:20.975884-06:00",
                "locale": "en"
            },
            "title": "Precalculus",
            "license_name": "Creative Commons Attribution License",
            "license_version": "4.0"
        }
    ]
}
```

One second-edition body in full, so the exact returned string is on the record:

```json
{
    "meta": {
        "total_count": 1
    },
    "items": [
        {
            "id": 553,
            "meta": {
                "slug": "algebra-and-trigonometry-2e",
                "type": "books.Book",
                "detail_url": "https://openstax.org/apps/cms/api/v2/pages/553/",
                "html_url": "https://openstax.org/details/books/algebra-and-trigonometry-2e",
                "first_published_at": "2021-12-02T15:49:18.084000-06:00",
                "locale": "en"
            },
            "title": "Algebra and Trigonometry 2e",
            "license_name": "Creative Commons Attribution-NonCommercial-ShareAlike License",
            "license_version": "4.0"
        }
    ]
}
```

### 1b · All ten results

`license_name` and `license_version` are transcribed exactly as returned. `id` and
`first_published_at` come from the same responses and are given because they are the only
edition evidence the endpoint carries.

| slug | `title` | `id` | `first_published_at` | `license_name` | `license_version` |
|---|---|---|---|---|---|
| `algebra-and-trigonometry` | Algebra and Trigonometry | 38 | 2016-03-09T09:53:01.890636-06:00 | `Creative Commons Attribution License` | `4.0` |
| `precalculus` | Precalculus | 37 | 2016-03-09T09:50:20.975884-06:00 | `Creative Commons Attribution License` | `4.0` |
| `algebra-and-trigonometry-2e` | Algebra and Trigonometry 2e | 553 | 2021-12-02T15:49:18.084000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `precalculus-2e` | Precalculus 2e | 551 | 2021-12-02T15:40:23.883000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `college-algebra-2e` | College Algebra 2e | 550 | 2021-12-02T15:27:45.192000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `elementary-algebra-2e` | Elementary Algebra 2e | 414 | 2020-03-23T10:48:54.491000-05:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `intermediate-algebra-2e` | Intermediate Algebra 2e | 418 | 2020-04-15T09:08:40.749000-05:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `prealgebra-2e` | Prealgebra 2e | 392 | 2020-03-02T15:22:33.670000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `contemporary-mathematics` | Contemporary Mathematics | 689 | 2023-03-08T14:08:14.732000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |
| `calculus-volume-1` | Calculus Volume 1 | 74 | 2016-03-10T14:37:26.063000-06:00 | `Creative Commons Attribution-NonCommercial-ShareAlike License` | `4.0` |

### 1c · What these ten rows do and do not support

They support: the two 1e titles this unit needs, `algebra-and-trigonometry` and `precalculus`,
returned `Creative Commons Attribution License` version `4.0` at this fetch. Six titles with a
`-2e` slug returned `Creative Commons Attribution-NonCommercial-ShareAlike License` version
`4.0`. `contemporary-mathematics`, which has no edition suffix and first published 2023,
returned the same NC-SA string.

They do NOT support a rule of the form "1e is CC BY and 2e is CC BY-NC-SA."
**`calculus-volume-1` breaks it.** It carries no `-2e` suffix, its `id` is 74 and its
`first_published_at` is `2016-03-10`, one day after `algebra-and-trigonometry`, and it returned
`Creative Commons Attribution-NonCommercial-ShareAlike License` `4.0`. So the licence does not
track the edition marker in the slug. The only defensible statement from this evidence is
per-slug: name the slug, quote the two returned fields, give the fetch date.

Note also what the endpoint does not return. There is no CC deed URL and no SPDX identifier in
these responses, only a human-readable name and a bare version number. `Creative Commons
Attribution License` + `4.0` has to be mapped to CC BY 4.0 by the reader; the API does not do
it. Nor is there any field distinguishing a first from a second edition beyond the slug text
itself.

---

## 2 · What the book's own landing page delivers

`https://openstax.org/details/books/algebra-and-trigonometry-2e`, HTTP 200, 12410 bytes. The
delivered bytes contain **zero** occurrences of `Creative Commons` and **zero** of `CC BY`.
Stripped of script and style, the entire rendered text is two lines:

> OpenStax
> You must enable JavaScript in order to use this site.

This is a client-rendered shell. Any licence shown to a human on that page is produced by
JavaScript after load, which means the licence is not in the document a fetch retrieves. That
is the measured basis for "the licence is not reliably rendered on the book's own landing
page." It is not a bot block: the status is 200 and the body is served in full.

---

## 3 · The contradiction on the section pages

Both 1e section pages this unit uses are server-rendered and carry licence text. Each carries
**two different licence statements**, and they disagree.

### 3a · The per-book statement, in the Citation/Attribution panel

From `openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry`,
rendered text of the panel, in order, tags stripped:

> Citation/Attribution
>
> This book may not be used in the training of large language models or otherwise be ingested into large language models or generative AI offerings without OpenStax's permission.
>
> Want to cite, share, or modify this book? This book uses the Creative Commons Attribution License and you must attribute OpenStax.
>
> Attribution information
>
> If you are redistributing all or part of this book in a print format, then you must include on every physical page the following attribution:
>
> Access for free at https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites
>
> If you are redistributing all or part of this book in a digital format, then you must include on every digital page view the following attribution:
>
> Access for free at https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites
>
> Citation information
>
> Use the information below to generate a citation. We recommend using a citation tool such as this one.
>
> Authors: Jay Abramson
> Publisher/website: OpenStax
> Book title: Algebra and Trigonometry
> Publication date: Feb 13, 2015
> Location: Houston, Texas
> Book URL: https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites
> Section URL: https://openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry
>
> © Dec 8, 2021 OpenStax. Textbook content produced by OpenStax is licensed under a Creative Commons Attribution License .
>
> The OpenStax name, OpenStax logo, OpenStax book covers, OpenStax CNX name, and OpenStax CNX logo are not subject to the Creative Commons license and may not be reproduced without the prior and express written consent of Rice University.

The same page also embeds a machine-readable object, byte-exact from the HTML:

```json
"license":{"url":"http://creativecommons.org/licenses/by/4.0/","name":"Creative Commons Attribution License"}
```

This is the only place in the whole cluster where a CC deed URL is given, and it says `by/4.0`.

`openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry` carries the identical
structure, the identical embedded `license` object, and the identical trademark carve-out. Its
citation block differs only in the book fields:

> Authors: Jay Abramson
> Publisher/website: OpenStax
> Book title: Precalculus
> Publication date: Oct 23, 2014
> Location: Houston, Texas
> Book URL: https://openstax.org/books/precalculus/pages/1-introduction-to-functions
> Section URL: https://openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry
>
> © Dec 8, 2021 OpenStax. Textbook content produced by OpenStax is licensed under a Creative Commons Attribution License .

### 3b · The site-wide statement, in the page footer

On the SAME two pages, in the footer, verbatim:

> © 1999-2026, Rice University. Except where otherwise noted, textbooks on this site are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY NC-SA) license.

Immediately after it, in the same footer block:

> Advanced Placement® and AP® are trademarks registered and/or owned by the College Board, which is not affiliated with, and does not endorse, this site.

The footer's link target is `creativecommons.org/licenses/by-nc-sa/4.0/`. So one page delivers
two deed URLs, `by/4.0` from the book object and `by-nc-sa/4.0` from the footer.

### 3c · Reading the contradiction correctly

The two statements are formally reconcilable through `Except where otherwise noted`: the footer
is the site default and the Citation/Attribution panel is the per-book note that overrides it.
But a reader who grepped the page for `Creative Commons` and stopped at the first or the last
hit gets a different answer depending on which end they started from. This is a page that
returns CC BY and CC BY-NC-SA to the same query.

**That is why the CMS API is the check.** The API returns one string per book with no default
layer above it. Any page teaching this must say: query the API by slug, read `license_name` and
`license_version`, and treat the rendered page as ambiguous by construction.

---

## 4 · The riders next door to the grant

Three sentences sit immediately around the CC BY statement and change what the grant means.
None of them is a Creative Commons term.

**Rider 1, the AI/LLM restriction.** It is the FIRST line of the Citation/Attribution panel, on
both 1e pages, above the licence sentence:

> This book may not be used in the training of large language models or otherwise be ingested into large language models or generative AI offerings without OpenStax's permission.

This is a use restriction that CC BY 4.0 does not contain, asserted by the licensor on the same
panel as the grant. Whatever its legal weight, it is a stated condition of this specific host
and it is directly on point for any project that routes source text through a model. It must
never be dropped when the CC BY sentence is quoted.

**Rider 2, the trademark carve-out**, immediately after the licence sentence:

> The OpenStax name, OpenStax logo, OpenStax book covers, OpenStax CNX name, and OpenStax CNX logo are not subject to the Creative Commons license and may not be reproduced without the prior and express written consent of Rice University.

**Rider 3, the mandatory attribution string**, which is prescribed rather than free-form and
differs by output medium. Print: `you must include on every physical page`. Digital:
`you must include on every digital page view`. The required text in both cases is
`Access for free at ` followed by the book's own introduction URL, not the section URL and not
the book's landing page.

Also record the copyright line's own date, which is not the publication date:
`© Dec 8, 2021 OpenStax` on a book whose `Publication date` field reads `Feb 13, 2015`
(Algebra and Trigonometry) or `Oct 23, 2014` (Precalculus), and whose API `first_published_at`
is `2016-03-09`. Three different dates for the same book, in three places on the same host.

---

## 5 · The section content this unit would draw on

Both 1e section pages were fetched in full and are on disk. Their titles as served:
`7-2-right-triangle-trigonometry` in Algebra and Trigonometry, and
`5-4-right-triangle-trigonometry` in Precalculus. Author of both, per the citation block:
`Jay Abramson`. Publisher: `OpenStax`. Location: `Houston, Texas`.

This extract deliberately does not reproduce the mathematical body of either section. Under the
verdict vocabulary, citing the section and describing what it covers needs no licence, and this
row's page is a rights verdict about a host rather than a content page. If a later row needs the
cofunction derivation itself, it should re-fetch and stage that passage separately so the
quotation carries its own provenance.

---

## 6 · What is NOT established here

- **The Open Textbook Library claim is not in this extract.** INVENTORY.md's reference line says
  OTL lists Algebra and Trigonometry 2e as CC BY and that this is wrong. No `open.umn.edu` URL
  was fetched for this staging pass. A page asserting the aggregator is wrong needs its own
  pasted OTL sentence with its own fetch date, and cannot lean on this file.
- **Nothing here covers non-maths OpenStax titles.** All ten slugs queried are mathematics.
- **The API's stability is unmeasured.** One fetch on one date. `license_name` is a display
  string, not an identifier, and could be reworded by OpenStax without the licence changing, or
  the reverse. The fetch date is the whole of the guarantee.
