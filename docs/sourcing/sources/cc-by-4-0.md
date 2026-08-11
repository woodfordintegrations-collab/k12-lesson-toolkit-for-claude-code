---
source_url: https://creativecommons.org/licenses/by/4.0/
fetched: 2026-08-08
http_status: 200
role: primary
covers: license-cc-by, concept-cite-quote-adapt, practice-assemble-an-attribution-block, license-sharealike (contrast), license-noncommercial (contrast)
---

# CC BY 4.0 deed, staged verbatim

## 0 · Fetch record

Two documents were fetched. They are different instruments and this extract keeps them apart.

| Document | URL | HTTP | Redirects | Bytes |
|---|---|---|---|---|
| Deed | `https://creativecommons.org/licenses/by/4.0/` | 200 | 0 | 32178 |
| Legal code | `https://creativecommons.org/licenses/by/4.0/legalcode.en` | 200 | 0 | 48970 |

Method: `curl -sS -L`, default user agent, 2026-08-08. No bot block, no redirect, no soft-404.
Raw bytes were parsed locally. No summarizing layer was used at any point, per the wiki's
evidence floor.

Page `<title>`: `Deed - Attribution 4.0 International - Creative Commons`
Declared `<link rel="canonical">`: `https://creativecommons.org/licenses/by/4.0/deed.en`
On-page "Canonical URL" article text: `https://creativecommons.org/licenses/by/4.0/`
Legal code version line: `Version 4.0 • See the errata page for any corrections and the date of change`

**Quotation convention.** The deed's HTML wraps sentences across source lines. Quotations below
reproduce the rendered text with that source line-wrap whitespace collapsed to single spaces,
which is exactly what a reader sees. Characters, including the em dashes the deed itself uses,
are otherwise unaltered.

## 1 · The deed's own summary of what is permitted

Heading: **You are free to:**

> **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.

> **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

> The licensor cannot revoke these freedoms as long as you follow the license terms.

## 2 · The deed's own summary of what is required

Heading: **Under the following terms:**

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Heading: **Notices:**

> You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

## 3 · ShareAlike and NoDerivatives

**Neither condition is present on this deed.** Measured, not assumed: the phrases `ShareAlike`
and `NoDerivatives` appear zero times in the deed's "Under the following terms" list. The list
has exactly two items, `Attribution` and `No additional restrictions`.

The nearest thing CC BY 4.0 has to a downstream-licence rule lives in the legal code, not on the
deed, and it is a floor rather than copyleft. Legal code Section 3(a)(4), verbatim:

> If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

That is the whole of it. Your adaptation may carry any licence you like, including a proprietary
one, so long as it does not block recipients from exercising CC BY 4.0 on the underlying
material. This is the structural difference from `[[license-sharealike]]`.

## 4 · The three answers a page will need

**Commercial use: permitted, and the deed says so twice.** Both freedoms carry the trailing
clause `for any purpose, even commercially`. Note this is wording unique to the BY and BY 3.0
deeds in this cluster: the NC deeds drop that clause entirely rather than adding a negation to it.

**Indication of changes: required whenever you Share, not only when you adapt.** The deed's
Attribution clause says `indicate if changes were made`. The deed's own footnote, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

The legal code puts the same duty inside Section 3(a)(1)(B), which is triggered by `If You Share
the Licensed Material (including in modified form)`. Two distinct duties sit in that footnote:
indicate your own modification, and **retain** any indication of previous modifications.

**Attribution must contain, per the deed's footnote, verbatim:**

> **appropriate credit** — If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

The legal code is more specific than the deed. Section 3(a)(1), verbatim:

> If You Share the Licensed Material (including in modified form), You must:
>
> retain the following if it is supplied by the Licensor with the Licensed Material:
>
> identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
>
> a copyright notice;
>
> a notice that refers to this Public License;
>
> a notice that refers to the disclaimer of warranties;
>
> a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
>
> indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
>
> indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.

And the satisfaction rule, verbatim:

> You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.

Every retain-item is conditioned on `if it is supplied by the Licensor`. A page must not state
that a copyright notice is required where the source supplies none.

## 5 · Where the deed differs from the legal code

**The deed says it is not the licence.** Verbatim, under the heading `Notice`:

> This deed highlights only some of the key features and terms of the actual license. It is not a license and has no legal value. You should carefully review all of the terms and conditions of the actual license before using the licensed material.

> Creative Commons is not a law firm and does not provide legal services. Distributing, displaying, or linking to this deed or the license that it summarizes does not create a lawyer-client or any other relationship.

Differences measured in this fetch:

1. **The deed's four-word `appropriate credit` compresses seven legal-code items.** The
   deed's main clause names three things (credit, link to the licence, indication of changes).
   Section 3(a)(1)(A) alone names five retain-items.
2. **The deed omits the grant's shape.** Legal code Section 2(a)(1), verbatim, grants a
   `worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license` to
   `reproduce and Share the Licensed Material, in whole or in part; and` `produce, reproduce,
   and Share Adapted Material.` `non-sublicensable` appears nowhere on the deed.
3. **The deed omits the format-change carve-out.** Legal code Section 2(a)(4), verbatim:
   `For purposes of this Public License, simply making modifications authorized by this Section
   2(a)(4) never produces Adapted Material.` A format conversion is therefore not an adaptation.
4. **The deed omits Sui Generis Database Rights entirely** (legal code Section 4). The string
   `database` appears nowhere in the deed body.
5. **Title is not required in 4.0.** Measured: `title of the Work` appears 0 times in the CC BY
   4.0 legal code, and 1 time in the CC BY 3.0 legal code. The deed footnote's claim that
   pre-4.0 licences additionally require the title is confirmed by that count.

## 6 · Rider next door to the grant

The deed page's own site footer, verbatim, carrying its own carve-out in the same sentence and
a separate third-party attribution immediately after:

> Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license. Icons by Font Awesome.

This governs creativecommons.org pages, not works licensed under CC BY 4.0. Do not read it as
evidence about any third-party host.

The legal code page carries a further sentence about the licence text itself, verbatim:

> The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication.

followed immediately by a trademark reservation, verbatim:

> Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at creativecommons.org/policies, Creative Commons does not authorize the use of the trademark "Creative Commons" or any other trademark or logo of Creative Commons without its prior written consent

So the licence text may be reproduced freely; the CC name and logo may not. Those are two facts,
not one.

## 7 · What this extract does not establish

- No fetch of the `deed.en_US` or other localised deed variants was made in this pass.
- The legal code has an errata page, linked from the version line. It was not fetched, so this
  extract cannot say whether corrections exist.
- Whether any particular host actually serves material under CC BY 4.0 is a separate question
  answered by that host's own page, never by this deed.
