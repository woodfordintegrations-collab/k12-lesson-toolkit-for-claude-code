---
source_url: https://creativecommons.org/licenses/by/3.0/
fetched: 2026-08-08
http_status: 200
role: primary
covers: license-cc-by, concept-cite-quote-adapt, practice-assemble-an-attribution-block, source-math-mistakes
---

# CC BY 3.0 Unported deed, staged verbatim

The permissive end of the 3.0 generation. Staged separately from `cc-by-4-0.md` because the two
are different instruments with different attribution duties, and because `INVENTORY.md` warns at
line 360 against silently upgrading a 3.0 label to 4.0.

## 0 · Fetch record

| Document | URL | HTTP | Redirects | Bytes |
|---|---|---|---|---|
| Deed | `https://creativecommons.org/licenses/by/3.0/` | 200 | 0 | 32052 |
| Legal code | `https://creativecommons.org/licenses/by/3.0/legalcode.en` | 200 | 0 | 51333 |

Method: `curl -sS -L`, default user agent, 2026-08-08. No bot block, no redirect, no soft-404.
Raw bytes parsed locally, no summarizing layer.

Page `<title>`: `Deed - Attribution 3.0 Unported - Creative Commons`
Declared `<link rel="canonical">`: `https://creativecommons.org/licenses/by/3.0/deed.en`
On-page "Canonical URL" article text: `https://creativecommons.org/licenses/by/3.0/`
Legal code version line: `Version 3.0 • See the errata page for any corrections and the date of change`

**Relation to the previously recorded fetch.** `INVENTORY.md` line 388 records
`http://creativecommons.org/licenses/by/3.0/deed.en_US` as fetched HTTP 200, redirecting to
`https://creativecommons.org/licenses/by/3.0/deed.en`. This extract fetched a **different path**,
the bare `https://creativecommons.org/licenses/by/3.0/`, which returned 200 with **0 redirects**.
Two different paths, both live, consistent version. The `deed.en_US` variant itself was not
re-fetched here and its body is not staged in this file.

**Quotation convention.** Quotations reproduce the rendered text with HTML source line-wrap
whitespace collapsed to single spaces. Characters, including the deed's own em dashes, are
otherwise unaltered.

## 1 · The older-version notice, verbatim

Under the heading `Notice`, at the top of the page:

> This is an older version of this license. Compared to previous versions, the 4.0 versions of all CC licenses are more user-friendly and more internationally robust. If you are licensing your own work, we strongly recommend the use of the 4.0 license instead: Deed - Attribution 4.0 International

Advice to licensors about future choices. Not a withdrawal, not an expiry. Material licensed
under 3.0 stays under 3.0.

## 2 · The deed's own summary of what is permitted

Heading: **You are free to:**

> **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.

> **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

> The licensor cannot revoke these freedoms as long as you follow the license terms.

Byte-identical in wording to the CC BY 4.0 freedoms, including the trailing `for any purpose,
even commercially` on both limbs.

## 3 · The deed's own summary of what is required

Heading: **Under the following terms:**

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Heading: **Notices:**

> You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

## 4 · ShareAlike and NoDerivatives

**Neither condition is present.** Measured: the "Under the following terms" list has exactly two
items, `Attribution` and `No additional restrictions`. There is no copyleft and no restriction on
distributing adaptations.

The 3.0 counterpart of the 4.0 downstream floor is in the grant itself rather than a separate
clause, and it is a labelling duty rather than a licensing one. See section 5.

## 5 · The three answers a page will need

**Commercial use: permitted, and the deed says so twice**, once on each freedom, with the clause
`for any purpose, even commercially`. The legal code grant contains no commercial restriction and
the string `NonCommercial` does not appear as a condition.

**Indication of changes: required only when you create an Adaptation, and it sits inside the
grant.** This is where 3.0 genuinely differs from 4.0, and where the deed's main text is
misleading because it serves the 4.0 template wording.

The deed's Attribution clause says `indicate if changes were made`, flatly. The deed's own
footnote qualifies it, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

The legal code confirms the footnote and gives the operative wording. Section 3(b), verbatim,
inside the License Grant:

> to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";

Three consequences a page can rely on. The duty is `clearly label, demarcate or otherwise
identify`, not merely "indicate". It is a **condition of the adaptation right**, so failing it
means the adaptation was never licensed, not merely that attribution was incomplete. And there is
no 4.0-style duty to retain an indication of previous modifications; measured, the phrase
`previous modifications` appears 0 times in the CC BY 3.0 legal code.

The full grant, Section 3, verbatim:

> Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the duration of the applicable copyright) license to exercise the rights in the Work as stated below:
>
> to Reproduce the Work, to incorporate the Work into one or more Collections, and to Reproduce the Work as incorporated in the Collections;
>
> to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";
>
> to Distribute and Publicly Perform the Work including as incorporated in Collections; and,
>
> to Distribute and Publicly Perform Adaptations.

Note `perpetual (for the duration of the applicable copyright)` where 4.0 says `irrevocable`.

**Attribution must contain**, per the legal code, which is the authority here. Section 4(b),
verbatim:

> If You Distribute, or Publicly Perform the Work or any Adaptations or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work; and, (iv) consistent with Section 3(b), in the case of an Adaptation, a credit identifying the use of the Work in the Adaptation (e.g., "French translation of the Work by Original Author," or "Screenplay based on original Work by Original Author").

So the required credit is: all copyright notices kept intact, plus (i) the author or designated
Attribution Parties, (ii) **the title of the Work if supplied**, (iii) the URI, and (iv) **for an
adaptation, a credit identifying the use**, with the two worked examples quoted above.

Items (ii) and (iv) have no counterpart in 4.0. Measured: `title of the Work` appears 1 time in
this legal code and 0 times in the CC BY 4.0, CC BY-NC 4.0 and CC BY-NC-SA 4.0 legal codes.

The deed's footnote acknowledges (ii) generically, verbatim:

> **appropriate credit** — If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

`and may have other slight differences` is the deed declining to enumerate. Item (iv) is one of
them.

Section 4(a) additionally requires the licence to travel, verbatim:

> You may Distribute or Publicly Perform the Work only under the terms of this License. You must include a copy of, or the Uniform Resource Identifier (URI) for, this License with every copy of the Work You Distribute or Publicly Perform.

Same clause, the Collection carve-out and the takedown-of-credit duty, verbatim:

> This Section 4(a) applies to the Work as incorporated in a Collection, but this does not require the Collection apart from the Work itself to be made subject to the terms of this License. If You create a Collection, upon notice from any Licensor You must, to the extent practicable, remove from the Collection any credit as required by Section 4(b), as requested. If You create an Adaptation, upon notice from any Licensor You must, to the extent practicable, remove from the Adaptation any credit as required by Section 4(b), as requested.

## 6 · Where the deed differs from the legal code

Four differences, measured on the fetched bytes:

1. **Indication of changes.** The deed's main Attribution clause states it unconditionally, in
   4.0 wording. In 3.0 it is a condition on the adaptation right only, worded `clearly label,
   demarcate or otherwise identify`. Only the deed's footnote flags this.
2. **Title.** Required by legal code Section 4(b)(ii), absent from the deed's main clause,
   present only as a generic aside in the `appropriate credit` footnote.
3. **Adaptation credit.** Legal code Section 4(b)(iv) requires `a credit identifying the use of
   the Work in the Adaptation` with worked examples. The deed does not mention this at all, in
   the main text or in any footnote.
4. **The 3.0 deeds omit the "this deed is not a license" notice.** Measured: `highlights only
   some` appears **0 times** on this page and **1 time** on each of the three 4.0 deed pages. The
   `Notice` slot here holds the older-version banner instead. **Say the deed is a summary and not
   the licence anyway**, because it is true of every deed; it simply cannot be quoted from this
   page.

The surviving disclaimer on this page is narrower, verbatim:

> Creative Commons is the nonprofit behind the open licenses and other legal tools that allow creators to share their work. Our legal tools are free to use.

## 7 · Rider next door to the grant

Deed page site footer, verbatim, with its carve-out in the same sentence and a third-party
attribution immediately after:

> Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license. Icons by Font Awesome.

The page documents CC BY 3.0 but is itself published under CC BY **4.0**. The version numbers on
this page are a live confusion hazard, which is exactly the `INVENTORY.md` line 360 warning.

Legal code page, verbatim:

> The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication.

followed immediately by the trademark reservation over the `"Creative Commons"` name and logo.

## 8 · What this extract does not establish

- `Unported` means not ported to a national jurisdiction. `3.0 Unported` is not `3.0 US`. Those
  are different documents at different URLs and neither ported variant is staged here.
- The `deed.en_US` variant recorded at `INVENTORY.md` line 388 was not re-fetched in this pass.
- The errata page linked from the version line was not fetched.
- Whether mathmistakes.org, or any host, still carries a CC BY 3.0 notice is a separate fetch
  against that host. This deed is evidence about the instrument only.
