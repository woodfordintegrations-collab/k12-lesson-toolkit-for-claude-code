---
source_url: https://creativecommons.org/licenses/by-nc/4.0/
fetched: 2026-08-08
http_status: 200
role: primary
covers: license-noncommercial, concept-cite-quote-adapt, source-accessim-360, practice-assemble-an-attribution-block
---

# CC BY-NC 4.0 deed, staged verbatim

This deed was recorded in `INVENTORY.md` (line 401) as `verified_current: pending (2026-08-07)`
with the note `recorded as an href target, never fetched by any agent`. This extract closes
that gap. It was fetched on 2026-08-08 and returned HTTP 200.

## 0 · Fetch record

| Document | URL | HTTP | Redirects | Bytes |
|---|---|---|---|---|
| Deed | `https://creativecommons.org/licenses/by-nc/4.0/` | 200 | 0 | 35485 |
| Legal code | `https://creativecommons.org/licenses/by-nc/4.0/legalcode.en` | 200 | 0 | 50209 |

Method: `curl -sS -L`, default user agent, 2026-08-08. No bot block, no redirect, no soft-404.
Raw bytes parsed locally, no summarizing layer.

Page `<title>`: `Deed - Attribution-NonCommercial 4.0 International - Creative Commons`
Declared `<link rel="canonical">`: `https://creativecommons.org/licenses/by-nc/4.0/deed.en`
On-page "Canonical URL" article text: `https://creativecommons.org/licenses/by-nc/4.0/`
Legal code version line: `Version 4.0 • See the errata page for any corrections and the date of change`

**Quotation convention.** Quotations reproduce the rendered text with HTML source line-wrap
whitespace collapsed to single spaces. Characters, including the deed's own em dashes, are
otherwise unaltered.

## 1 · The deed's own summary of what is permitted

Heading: **You are free to:**

> **Share** — copy and redistribute the material in any medium or format

> **Adapt** — remix, transform, and build upon the material

> The licensor cannot revoke these freedoms as long as you follow the license terms.

**The load-bearing fact is what is absent.** The CC BY 4.0 deed ends both freedoms with `for any
purpose, even commercially`. This deed does not. The NC restriction is expressed by deleting that
clause from the freedoms and adding a separate condition below, not by negating it in place. A
page comparing the two deeds must compare the full sentences, because the difference is a
deletion.

## 2 · The deed's own summary of what is required

Heading: **Under the following terms:**

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **NonCommercial** — You may not use the material for commercial purposes.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Heading: **Notices:**

> You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

## 3 · ShareAlike and NoDerivatives

**Neither condition is present on this deed.** Measured: the "Under the following terms" list
has exactly three items, `Attribution`, `NonCommercial` and `No additional restrictions`.

This is the fact most often collapsed. CC BY-NC 4.0 has **no copyleft**. You may paraphrase and
republish, and your derivative does **not** have to ship under CC BY-NC 4.0. What travels
downstream is the NC constraint on the underlying material, not a licence obligation on your
own contribution. The only downstream-licence rule is legal code Section 3(a)(4), verbatim:

> If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

Compare `[[license-sharealike]]`, where the adapter's licence is dictated rather than merely
constrained.

## 4 · The three answers a page will need

**Commercial use: prohibited.** The deed condition, verbatim:

> **NonCommercial** — You may not use the material for commercial purposes.

The deed's own footnote defining the term, verbatim:

> **commercial purposes** — A commercial use is one primarily intended for commercial advantage or monetary compensation.

The legal code definition is longer and adds a file-sharing carve-out the deed omits entirely.
Verbatim:

> **NonCommercial** means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.

Note `not primarily intended for or directed towards`. The test is the intent of the use, not the
tax status of the user. A non-profit can make a commercial use and a company can make a
non-commercial one.

NC is also written into the grant itself rather than bolted on. Legal code Section 2(a)(1),
verbatim:

> reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
>
> produce, reproduce, and Share Adapted Material for NonCommercial purposes only.

And a royalty reservation that survives, legal code Section 2(b)(3), verbatim:

> To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.

**Indication of changes: required whenever you Share, not only when you adapt.** Same 4.0 rule as
CC BY 4.0. The deed's footnote, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

**Attribution must contain**, per the deed's footnote, verbatim:

> **appropriate credit** — If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

The legal code Section 3 of CC BY-NC 4.0 is byte-identical to Section 3 of CC BY 4.0, including
the closing Section 3(a)(4) sentence. This was measured, not eyeballed: both sections extracted
from the fetched bytes and compared after whitespace normalisation are 1554 characters and
compare equal. The full text is staged in `cc-by-4-0.md` section 4 and is not duplicated here.
The attribution machinery does not change between BY and BY-NC in 4.0. Every retain-item is
conditioned on `if it is supplied by the Licensor`.

## 5 · Where the deed differs from the legal code

**The deed says it is not the licence.** Verbatim, under the heading `Notice`:

> This deed highlights only some of the key features and terms of the actual license. It is not a license and has no legal value. You should carefully review all of the terms and conditions of the actual license before using the licensed material.

> Creative Commons is not a law firm and does not provide legal services. Distributing, displaying, or linking to this deed or the license that it summarizes does not create a lawyer-client or any other relationship.

Differences measured in this fetch:

1. **The deed's NC definition drops the file-sharing carve-out.** The deed's footnote is one
   sentence. The legal code definition is two, and the second sentence declares certain
   non-monetary exchanges NonCommercial. A page relying on the deed alone would not know this.
2. **The deed does not say NC is inside the grant.** On the deed, NonCommercial reads as a
   condition sitting beside Attribution. In the legal code it qualifies the grant clause itself,
   `for NonCommercial purposes only`, in both limbs.
3. **The deed omits the royalty reservation** in Section 2(b)(3), which expressly preserves the
   licensor's right to collect royalties for non-NonCommercial uses.
4. **The deed omits the format-change carve-out.** Legal code Section 2(a)(4), verbatim:
   `For purposes of this Public License, simply making modifications authorized by this Section
   2(a)(4) never produces Adapted Material.`
5. **The deed omits Sui Generis Database Rights.** Legal code Section 4(a) narrows them to
   NonCommercial too, verbatim: `for the avoidance of doubt, Section 2(a)(1) grants You the right
   to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the
   database for NonCommercial purposes only`.

## 6 · Rider next door to the grant

The deed page's own site footer, verbatim, with its carve-out in the same sentence and a separate
third-party attribution immediately after:

> Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license. Icons by Font Awesome.

Note the trap: this deed page describes BY-NC, but the page itself is published under **CC BY
4.0**, not BY-NC. Do not read the footer as evidence about the instrument the page documents.

The legal code page adds, verbatim:

> The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication.

followed immediately by the trademark reservation covering the `"Creative Commons"` name and logo.

## 7 · What this extract does not establish

- The deed is now fetched, which closes the `pending` flag on `INVENTORY.md` line 401 for the
  deed itself. It says nothing about whether accessim.org still serves the footer that links here.
  That is a separate fetch against a separate host.
- No localised deed variant (`deed.en_US` and similar) was fetched.
- The errata page linked from the legal code version line was not fetched.
