---
source_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
fetched: 2026-08-08
http_status: 200
role: primary
covers: license-sharealike, license-noncommercial, trap-sharealike-contaminates-by-paraphrase, concept-cite-quote-adapt, source-im-task-bank, source-achieve-the-core-sap
---

# CC BY-NC-SA 4.0 deed, staged verbatim

The strictest instrument in this corpus that still permits paraphrase-and-republish. Its exact
ShareAlike scope is the fact most pages will turn on, so section 3 quotes it in full from both
the deed and the legal code.

## 0 · Fetch record

| Document | URL | HTTP | Redirects | Bytes |
|---|---|---|---|---|
| Deed | `https://creativecommons.org/licenses/by-nc-sa/4.0/` | 200 | 0 | 37346 |
| Legal code | `https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en` | 200 | 0 | 53058 |

Method: `curl -sS -L`, default user agent, 2026-08-08. No bot block, no redirect, no soft-404.
Raw bytes parsed locally, no summarizing layer.

Page `<title>`: `Deed - Attribution-NonCommercial-ShareAlike 4.0 International - Creative Commons`
Declared `<link rel="canonical">`: `https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en`
On-page "Canonical URL" article text: `https://creativecommons.org/licenses/by-nc-sa/4.0/`
Legal code version line: `Version 4.0 • See the errata page for any corrections and the date of change`

**Quotation convention.** Quotations reproduce the rendered text with HTML source line-wrap
whitespace collapsed to single spaces. Characters, including the deed's own em dashes and the
legal code's apostrophes in `Adapter's License`, are otherwise unaltered. The legal code is
inconsistent about that apostrophe, counted on the fetched bytes: 2 curly (U+2019) against 3
straight (U+0027). Curly in Section 2(a)(5)(B) and Section 3(b)(1); straight in the Section 1
definition heading, Section 3(b)(2) and Section 3(b)(3). Both forms are reproduced as found, so
a grep for either spelling alone will miss occurrences.

## 1 · The deed's own summary of what is permitted

Heading: **You are free to:**

> **Share** — copy and redistribute the material in any medium or format

> **Adapt** — remix, transform, and build upon the material

> The licensor cannot revoke these freedoms as long as you follow the license terms.

As with CC BY-NC 4.0, the `for any purpose, even commercially` clause that ends both CC BY 4.0
freedoms is **absent**, not negated.

## 2 · The deed's own summary of what is required

Heading: **Under the following terms:**

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **NonCommercial** — You may not use the material for commercial purposes.

> **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Heading: **Notices:**

> You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

## 3 · ShareAlike, exact scope

### 3a · The deed's ShareAlike sentence, verbatim

> **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

`same license` is a hyperlink to a footnote. That footnote, verbatim:

> **same license** — You may also use a license listed as compatible at https://creativecommons.org/compatiblelicenses

Two things a page must not lose. First, the obligation attaches to **your contributions**, not to
the whole work you place them in. Second, the trigger phrase is `If you remix, transform, or
build upon`, and the duty is on `distribute`.

### 3b · The legal code's ShareAlike section, verbatim

Section 3(b), complete:

> **ShareAlike.**
>
> In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the following conditions also apply.
>
> The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.
>
> You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.
>
> You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.

**The trigger is Sharing, not producing.** The deed's phrasing (`if you remix, transform, or
build upon the material, you must distribute your contributions under the same license`) can be
read as attaching on creation. The legal code is explicit: `if You Share Adapted Material You
produce`. Producing an adaptation that is never shared triggers nothing. This is the single most
load-bearing difference between the deed and the licence for a repository that drafts internally
before deciding what to publish.

**`same license` is wider than same version.** The legal code permits `a Creative Commons license
with the same License Elements, this version or later, or a BY-NC-SA Compatible License`. The
deed's word `same` is looser than the licence, in the licensee's favour.

Supporting definitions from Section 1, verbatim:

> **Adapted Material** means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.

> **Adapter's License** means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.

> **BY-NC-SA Compatible License** means a license listed at creativecommons.org/compatiblelicenses, approved by Creative Commons as essentially the equivalent of this Public License.

> **License Elements** means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.

> **Share** means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.

`Share` is defined by **provision to the public**. Internal circulation that does not provide
material to the public is not Sharing, which is what makes the Section 3(b) trigger narrower than
the deed's wording suggests.

The `Adapted Material` definition contains the boundary that matters for paraphrase:
`modified in a manner requiring permission under the Copyright and Similar Rights held by the
Licensor`. Where no permission would be required, no Adapted Material exists and ShareAlike does
not attach. That is the seam `[[concept-cite-quote-adapt]]` and
`[[trap-sharealike-contaminates-by-paraphrase]]` sit on.

The reciprocal downstream offer, Section 2(a)(5)(B), verbatim:

> **Additional offer from the Licensor – Adapted Material.** Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.

And the database rule that makes an aggregation an adaptation, Section 4(b), verbatim:

> if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section 3(b); and

## 3c · NoDerivatives

**Not present on this deed.** Measured: the "Under the following terms" list has exactly four
items, `Attribution`, `NonCommercial`, `ShareAlike` and `No additional restrictions`. Adaptation
is permitted. See `cc-by-nc-nd-3-0.md` for the ND instrument in this cluster.

## 4 · The three answers a page will need

**Commercial use: prohibited.** Deed condition, verbatim:

> **NonCommercial** — You may not use the material for commercial purposes.

Deed footnote, verbatim:

> **commercial purposes** — A commercial use is one primarily intended for commercial advantage or monetary compensation.

Legal code definition, verbatim:

> **NonCommercial** means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.

NC sits inside the grant. Legal code Section 2(a)(1), verbatim:

> reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
>
> produce, reproduce, and Share Adapted Material for NonCommercial purposes only.

**Indication of changes: required whenever you Share, not only when you adapt.** Deed footnote,
verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

**Attribution must contain**, per the deed's footnote, verbatim:

> **appropriate credit** — If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

Legal code Section 3(a)(1), verbatim:

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

Section 3(a) here is 2136 characters against 1554 for CC BY 4.0 and CC BY-NC 4.0, measured on the
fetched bytes. The excess is the ShareAlike subsection; Section 3(a) itself is unchanged. Note
that Section 3(b) adds a **second** licence-inclusion duty on top of 3(a)(1)(C): you include the
underlying licence, and separately you include the Adapter's License.

## 5 · Where the deed differs from the legal code

**The deed says it is not the licence.** Verbatim, under the heading `Notice`:

> This deed highlights only some of the key features and terms of the actual license. It is not a license and has no legal value. You should carefully review all of the terms and conditions of the actual license before using the licensed material.

> Creative Commons is not a law firm and does not provide legal services. Distributing, displaying, or linking to this deed or the license that it summarizes does not create a lawyer-client or any other relationship.

Differences measured in this fetch:

1. **Trigger.** Deed: `If you remix, transform, or build upon the material`. Legal code: `if You
   Share Adapted Material You produce`. Production alone does not trigger ShareAlike.
2. **Which licence.** Deed: `the same license as the original`, footnoted to a compatibility list.
   Legal code: `a Creative Commons license with the same License Elements, this version or later,
   or a BY-NC-SA Compatible License`. Later versions are allowed and the deed's main text does
   not say so.
3. **The deed omits the second inclusion duty**, Section 3(b)(2), requiring the text or URI of
   the Adapter's License itself.
4. **The deed omits the no-further-restrictions rule specific to Adapted Material**, Section
   3(b)(3), which is distinct from the general `No additional restrictions` item.
5. **The deed omits the format-change carve-out.** Legal code Section 2(a)(4), verbatim:
   `For purposes of this Public License, simply making modifications authorized by this Section
   2(a)(4) never produces Adapted Material.`
6. **The deed omits Sui Generis Database Rights** and the Section 4(b) rule that a substantial
   database inclusion is itself Adapted Material for ShareAlike purposes.

## 6 · Rider next door to the grant

Deed page site footer, verbatim, with its carve-out in the same sentence and a third-party
attribution immediately after:

> Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license. Icons by Font Awesome.

The page documenting BY-NC-SA is itself published under CC BY 4.0. Do not read the footer as
evidence about the instrument the page documents.

Legal code page, verbatim:

> The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication.

followed immediately by the trademark reservation over the `"Creative Commons"` name and logo.

## 7 · What this extract does not establish

- `https://creativecommons.org/compatiblelicenses` was **not** fetched. This extract therefore
  cannot name which licences are BY-NC-SA compatible, and a page must not guess.
- The errata page linked from the version line was not fetched.
- Whether a given host still serves material under this licence is a separate fetch against that
  host.
