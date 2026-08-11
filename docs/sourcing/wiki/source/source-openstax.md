---
title: "openstax.org (OpenStax textbooks, and the edition licence inversion)"
type: source
verdict: quote_sharealike
fetched: 2026-08-08
sources:
  - https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=algebra-and-trigonometry&fields=license_name,license_version
  - https://openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry
  - https://openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry
  - https://openstax.org/details/books/algebra-and-trigonometry-2e
  - sources/host-openstax.md
  - sources/verdict-wide-sweep.md
updated: 2026-08-08
---

# openstax.org (OpenStax textbooks, and the edition licence inversion)

## Summary

"OpenStax is CC BY 4.0" is the folk claim this page exists to kill. It is true of the edition people
learned it from and false of the edition they will actually reach, and the aggregator most likely to
be consulted publishes the wrong answer for exactly this book.

On this host **the licence is a property of the book slug, and nothing else tells you which one you
have.** At the 2026-08-08 fetch, ten mathematics slugs were queried against OpenStax's own content
API. Two returned `Creative Commons Attribution License` version `4.0`. Eight returned
`Creative Commons Attribution-NonCommercial-ShareAlike License` version `4.0`. The newer edition is
the more restricted one, which is the opposite of what anyone expects.

**The frontmatter verdict on this page is `quote_sharealike`, and it is a deliberately restrictive
host-level default rather than a finding about any single book.** Eight of the ten slugs measured
carry NonCommercial and ShareAlike. Two do not. A reader holding an `openstax.org/books/...` URL
cannot tell which case they are in without running the check in "What you may do with it" below.
Defaulting to the restricted answer costs one API call to correct; defaulting to the permissive
answer ships a licence violation. Per book, on the evidence staged here:

| Book slug | `license_name` returned | Per-book verdict |
|---|---|---|
| `algebra-and-trigonometry` | `Creative Commons Attribution License` `4.0` | `quote_and_adapt` |
| `precalculus` | `Creative Commons Attribution License` `4.0` | `quote_and_adapt` |
| `algebra-and-trigonometry-2e`, `precalculus-2e`, `college-algebra-2e`, `elementary-algebra-2e`, `intermediate-algebra-2e`, `prealgebra-2e`, `contemporary-mathematics`, `calculus-volume-1` | `Creative Commons Attribution-NonCommercial-ShareAlike License` `4.0` | `quote_sharealike`, and under the project's governing ruling that means quote-only for this repository |

**Do not compress that table into a rule about editions.** `calculus-volume-1` has no `-2e` suffix,
was first published one day after `algebra-and-trigonometry`, and returned the NonCommercial
ShareAlike string. "1e is CC BY, 2e is CC BY-NC-SA" is a rule this host's own data breaks. The only
defensible statement is per slug, with the two returned fields and a fetch date.

## When to reach for it

Reach for `algebra-and-trigonometry` §7.2 and `precalculus` §5.4 when you need a right-triangle
trigonometry treatment the repository may rewrite and ship. Both are first editions, both returned
CC BY 4.0 at this fetch, both are server-rendered plain HTML with no login, and they are two
independent routes to the same material. This project's wide sweep records five licence-compatible
sources for a CC BY 4.0 repository, three of them cleanly, and these two are two of the three; the
third is the IM curriculum at [[source-im-kendall-hunt]].

Reach for this page **before** touching any other OpenStax title, including any title that looks
like an obvious upgrade of one of those two. The upgrade is the restricted one.

Reach for the API check described below whenever an OpenStax URL enters the build, every time, and
record the date. It is one request and it is the only unambiguous answer this host gives.

Do **not** reach for the book's landing page to read a licence. `openstax.org/details/books/...`
delivers a JavaScript shell whose entire rendered text is two lines, and contains zero occurrences
of `Creative Commons`. See [[trap-license-lives-off-the-obvious-page]].

Do not reach for the Open Textbook Library, or any other aggregator, as a licence source for an
OpenStax book. See gotcha 6.

Do not reach for a second-edition title to paraphrase from. Under the project's governing ruling the repository
ships CC BY 4.0 and takes no paraphrase from any ShareAlike source, ever. See
[[trap-sharealike-contaminates-by-paraphrase]].

## What its own page says

Every byte below came from `curl` responses written to disk and read back from disk on 2026-08-08,
staged in `sources/host-openstax.md`. That matters unusually much here, because the finding is a
contradiction between two strings on the same page and a summarizing layer would resolve it
silently. See [[trap-summary-layer-is-not-evidence]].

### The content API, which is the authoritative check

Endpoint form:

```
https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=<SLUG>&fields=license_name,license_version
```

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

`slug=algebra-and-trigonometry-2e`, complete response body, byte-exact, and this is the whole
inversion in one object:

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

`slug=precalculus` returned `id` 37, `first_published_at` `2016-03-09T09:50:20.975884-06:00`, and
the same `Creative Commons Attribution License` `4.0` pair. Every one of the ten slugs queried
returned `"total_count": 1`.

The row that breaks the edition rule, from the same ten-slug sweep: `calculus-volume-1`, `id` 74,
`first_published_at` `2016-03-10T14:37:26.063000-06:00`, `license_name`
`Creative Commons Attribution-NonCommercial-ShareAlike License`, `license_version` `4.0`.

### What the landing page delivers, which is nothing

`https://openstax.org/details/books/algebra-and-trigonometry-2e`, HTTP 200, 12410 bytes. The
delivered bytes contain **zero** occurrences of `Creative Commons` and **zero** of `CC BY`. Stripped
of script and style, the entire rendered text is:

> OpenStax
> You must enable JavaScript in order to use this site.

Any licence a human sees there is produced by JavaScript after load. It is not a bot block: the
status is 200 and the body is served in full. See [[trap-access-is-not-a-rights-fact]] for why a
clean 200 settles nothing either way.

### One page, two licence statements, and they disagree

The two first-edition section pages are server-rendered and each carries **two** licence statements.
From `openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry`, the
Citation/Attribution panel, rendered text in order, tags stripped:

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

and the panel's closing lines:

> © Dec 8, 2021 OpenStax. Textbook content produced by OpenStax is licensed under a Creative Commons Attribution License .
>
> The OpenStax name, OpenStax logo, OpenStax book covers, OpenStax CNX name, and OpenStax CNX logo are not subject to the Creative Commons license and may not be reproduced without the prior and express written consent of Rice University.

The same page embeds a machine-readable object, byte-exact from the HTML, and it is the only place
in the whole cluster where a deed URL is given:

```json
"license":{"url":"http://creativecommons.org/licenses/by/4.0/","name":"Creative Commons Attribution License"}
```

On the **same page**, in the footer, verbatim:

> © 1999-2026, Rice University. Except where otherwise noted, textbooks on this site are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY NC-SA) license.

The footer's link target is `creativecommons.org/licenses/by-nc-sa/4.0/`. So one document delivers
two deed URLs. The two statements are formally reconcilable through `Except where otherwise noted`,
the footer being the site default and the panel being the per-book note that overrides it. But a
reader who greps the page for `Creative Commons` and stops at the first hit gets a different answer
from one who stops at the last. **This is a page that returns CC BY and CC BY-NC-SA to the same
query, which is why the API is the check.**

`openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry` carries the identical
structure, the identical embedded `license` object, the identical trademark carve-out and the same
footer.

## What you may do with it

### The check, which is the operative content of this page

1. Take the slug out of the URL. In `openstax.org/books/<SLUG>/pages/...` it is the segment after
   `/books/`.
2. Request
   `https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=<SLUG>&fields=license_name,license_version`.
3. Read `items[0].license_name` and `items[0].license_version`. Record both strings verbatim, with
   the date.
4. Map: `Creative Commons Attribution License` plus `4.0` is CC BY 4.0. `Creative Commons
   Attribution-NonCommercial-ShareAlike License` plus `4.0` is CC BY-NC-SA 4.0. **The API does not
   do this mapping for you**, and it returns no deed URL and no SPDX identifier.
5. Apply the operations table below to what came back, not to what the page said.

### Operations, for a slug the API returned CC BY 4.0 for

| Operation | Permitted | Condition |
|---|---|---|
| Cite: name the book and section, link it, state what it covers | yes | none, and no licence is needed to do this |
| Quote: reproduce its exact expression in quotation marks | yes | the attribution block below, plus riders 1 and 2 |
| Paraphrase and republish: rewrite its material and ship it | yes | the attribution block below, no copyleft attaches, plus riders 1 and 2 |

### Operations, for a slug the API returned CC BY-NC-SA 4.0 for

| Operation | Permitted | Condition |
|---|---|---|
| Cite | yes | none |
| Quote | yes | attribution; a quotation set in your own prose with attribution is a use, not an adaptation, so ShareAlike does not reach out of it |
| Paraphrase and republish | **no, for this repository** | the licence itself would allow it under NonCommercial plus ShareAlike, but the project's governing ruling forbids taking any paraphrase from any ShareAlike source into a CC BY 4.0 repository |

See [[license-cc-by]], [[license-sharealike]] and [[license-noncommercial]] for the regimes, and
[[concept-cite-quote-adapt]] for why the three rows are three different questions.

### The attribution string, which is prescribed and differs by medium

Not free-form. The required text is `Access for free at ` followed by the book's own **introduction**
URL, which is neither the section URL you took the material from nor the book's landing page. Print
requires it on every physical page; digital requires it on every digital page view.

```
Access for free at https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites
Source: https://openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry
Licensed CC BY 4.0 (per openstax.org CMS API, license_name "Creative Commons Attribution License",
license_version "4.0", checked 2026-08-08). Changes were made to the original material.
```

```
Access for free at https://openstax.org/books/precalculus/pages/1-introduction-to-functions
Source: https://openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry
Licensed CC BY 4.0 (per openstax.org CMS API, license_name "Creative Commons Attribution License",
license_version "4.0", checked 2026-08-08). Changes were made to the original material.
```

See [[concept-attribution-per-record]] for why the string is a property of the book rather than of
the host, and [[practice-assemble-an-attribution-block]] for where these land in the deliverable.

### Three riders sit immediately around the grant, and none of them is a Creative Commons term

**Rider 1, the AI and LLM restriction, and it is directly on point for this project.** It is the
FIRST line of the Citation/Attribution panel, above the licence sentence, on both first-edition
pages:

> This book may not be used in the training of large language models or otherwise be ingested into large language models or generative AI offerings without OpenStax's permission.

CC BY 4.0 contains no such term. This is a condition asserted by the licensor on the same panel as
the grant, and it must never be dropped when the CC BY sentence is quoted. Any pipeline that routes
this host's text through a model needs a decision on it recorded in the build docs. Whether it binds
as a matter of law is not a question this wiki answers, and the wiki's job is to make sure nobody
reaches the CC BY sentence without reading this one.

**Rider 2, the trademark carve-out.** The OpenStax name, logo, book covers, CNX name and CNX logo
are outside the licence and need prior express written consent from Rice University. Naming OpenStax
in a citation is ordinary nominative use and is unaffected. See [[concept-third-party-carve-out]].

**Rider 3, the medium-specific attribution**, set out above.

## Gotchas & constraints

**1. The frontmatter verdict is a host-level default, not a book-level finding.** `quote_sharealike`
is the restrictive answer for a reader who has an OpenStax URL and has not yet run the check. Two
named slugs are `quote_and_adapt` per book. Anything that consumes the verdict field mechanically
must be told this, or it will refuse a genuinely CC BY 4.0 source. Stating it here rather than
burying it is the price of a single-valued field on a host with plural grants.

**2. "1e is CC BY, 2e is CC BY-NC-SA" is not a rule, and the data breaks it.**
`calculus-volume-1` carries no edition suffix, first published one day after
`algebra-and-trigonometry`, and returned NonCommercial ShareAlike. `contemporary-mathematics`
likewise has no edition suffix and returned the same. Slug shape and publication order both fail as
predictors. Query the slug.

**3. The obvious page has no licence in it at all.** A fetch of the book's landing page returns 200,
12410 bytes, a JavaScript shell, and no licence string. An agent that concludes "no licence found,
therefore unlicensed" has repeated this project's recorded error on a different host. See
[[trap-license-lives-off-the-obvious-page]].

**4. The section page answers the same question twice, differently.** Grep-first and grep-last
return CC BY and CC BY-NC-SA respectively. If a licence finding on this host ever came from a
keyword search rather than from the API, it is not evidence, whichever answer it produced.

**5. The API returns a display string, not an identifier.** `license_name` is human-readable prose
that OpenStax could reword without the licence changing, or could leave unchanged while the licence
changes. There is no deed URL, no SPDX id, and no field distinguishing first from second edition
beyond the slug text. The fetch date is the whole of the guarantee.

**6. The Open Textbook Library claim in this project's records is unverified at this wiki's floor.**
This project's wide-sweep adjudication states that the Open Textbook Library lists Algebra and
Trigonometry 2e as CC BY and that its metadata is stale and wrong on exactly this book. That
adjudication fetched nothing and says so in its own opening paragraph, so it is a report of a
report. **No `open.umn.edu` URL was fetched by any agent in this project.** What would close it:
fetch the Open Textbook Library record for Algebra and Trigonometry 2e, paste its licence line, and
record URL, HTTP status and date. Until then, the durable and fully-grounded half of the claim is
the API result: `algebra-and-trigonometry-2e` returned `Creative Commons
Attribution-NonCommercial-ShareAlike License` `4.0`. Any aggregator saying otherwise is contradicted
by the publisher's own endpoint, and that is enough to act on without asserting what the aggregator
currently says.

**7. Three different dates for one book, in three places on this host.** The copyright line reads
`© Dec 8, 2021 OpenStax`, the citation panel's `Publication date` field reads `Feb 13, 2015` for
Algebra and Trigonometry and `Oct 23, 2014` for Precalculus, and the API's `first_published_at` is
`2016-03-09`. Cite whichever the citation context calls for, name which field it came from, and do
not reconcile them.

**8. Only mathematics titles were checked.** All ten slugs queried are maths. Nothing here supports
any statement about OpenStax science, humanities or business titles, and the licence pattern found
here is not a basis for guessing at them.

**9. One fetch, one date, and stability unmeasured.** The API was queried once. Two grants in this
corpus were withdrawn inside six months. Re-run the check before publication and record the new
date. See [[license-withdrawn-grants]] and [[trap-license-withdrawn-after-citation]].

**10. The section content itself was deliberately not staged.** The staged extract records the
rights surface and explicitly does not reproduce the mathematical body of either section. If the
build needs the cofunction derivation itself, re-fetch and stage that passage so the quotation
carries its own provenance rather than inheriting this page's.

## Related

- [[license-cc-by]] is the plain-attribution regime the two first-edition titles grant under, and the
  outbound licence this repository ships, which is what makes the second editions unusable for
  paraphrase.
- [[license-sharealike]] and [[license-noncommercial]] are the two riders the other eight slugs
  carry, and the reason their material cannot be mixed into a file with the first editions'.
- [[trap-sharealike-contaminates-by-paraphrase]] is the working test for when a rewrite of
  second-edition material has crossed from use into adaptation.
- [[trap-license-lives-off-the-obvious-page]] is the recorded failure this host reproduces in a new
  form: the licence is absent from the landing page because the page is a client-rendered shell.
- [[trap-summary-layer-is-not-evidence]] is why the contradiction in section 3 above survives on this
  page instead of being silently resolved.
- [[trap-access-is-not-a-rights-fact]] covers the HTTP 200 on a page that grants nothing.
- [[concept-cite-quote-adapt]] is the three-operation split both verdict tables apply.
- [[concept-attribution-per-record]] is why the attribution string is a property of the book and its
  output medium rather than of `openstax.org`.
- [[concept-third-party-carve-out]] holds the trademark class that rider 2 belongs to.
- [[source-im-kendall-hunt]] is the other plain-attribution prose source for this content, and the
  page whose structure this one follows: one organisation, several hosts or editions, several grants.
- [[license-withdrawn-grants]] is why the fetch date in this page's frontmatter is load-bearing.
- [[evidence-c7-store-gap-not-corpus-gap]] is where the first-edition sections count as located,
  usable coverage.

## Composes with

- [[practice-build-a-source-table]] is the fetch-and-record procedure this page's check belongs
  inside, and the API query is the strongest single instance of raw-bytes-over-rendered-page in the
  corpus.
- [[practice-assemble-an-attribution-block]] consumes the two paste-ready blocks above, including
  the introduction-URL form and the changes-made indication.

## References

Fetched by this project on 2026-08-08, `curl` to disk and read from disk. HTTP 200 on all thirteen
requests, no 403, no 404, no redirect, no TLS problem anywhere in the cluster:

- `https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&slug=<SLUG>&fields=license_name,license_version`,
  ten slugs, 630 to 705 bytes each. `algebra-and-trigonometry`, `precalculus`,
  `algebra-and-trigonometry-2e`, `precalculus-2e`, `college-algebra-2e`, `elementary-algebra-2e`,
  `intermediate-algebra-2e`, `prealgebra-2e`, `contemporary-mathematics`, `calculus-volume-1`.
- `https://openstax.org/books/algebra-and-trigonometry/pages/7-2-right-triangle-trigonometry`
  HTTP 200, 451140 bytes. The Citation/Attribution panel, the embedded `license` object, the footer.
- `https://openstax.org/books/precalculus/pages/5-4-right-triangle-trigonometry` HTTP 200, 434277
  bytes. Identical rights structure, different citation fields.
- `https://openstax.org/details/books/algebra-and-trigonometry-2e` HTTP 200, 12410 bytes. The
  JavaScript shell with zero licence strings.

Staged extracts in this wiki, staged 2026-08-08:

- `sources/host-openstax.md`, primary. The fetch log, three complete API bodies, the ten-row table,
  §1c on what those rows do and do not support, the landing-page measurement, the two contradictory
  page statements with both deed URLs, the three riders, and §6 on what is not established.
- `sources/verdict-wide-sweep.md`, reference. This project's own adjudication of eight sweep
  reports, which fetched nothing and says so: §6.4 retiring the unqualified "OpenStax is CC BY 4.0"
  claim, the reuse-terms table, and the Open Textbook Library assertion recorded in gotcha 6 as
  unverified at this wiki's floor.

This project's own rulings, cited as this project's decisions and not as OpenStax's:

- the project's governing ruling: the repository ships CC BY 4.0 and takes no paraphrase from any
  ShareAlike source, ever. That ruling, not the licence, is what makes the eight NonCommercial
  ShareAlike slugs quote-only here.
