---
source_url: https://creativecommons.org/licenses/by-nc-sa/3.0/
fetched: 2026-08-08
http_status: 200
role: primary
covers: license-sharealike, license-noncommercial, trap-sharealike-contaminates-by-paraphrase, source-engageny-nysed, source-math-vision-project
---

# CC BY-NC-SA 3.0 Unported deed, staged verbatim

`INVENTORY.md` line 415 records NYSED's live successor statement as naming no version while its
anchor `href` is `licenses/by-nc-sa/3.0/`, and line 319 records an MVP page claiming
`4.0 Unported`, which is not a real licence name, against an `href` of `by-nc-sa/3.0`. This is
the deed those hrefs resolve to.

**It carries the single largest deed-versus-legal-code divergence in this cluster**: the deed
offers a compatible-licence route that the 3.0 legal code does not contain. Section 4 has the
measurement.

## 0 · Fetch record

| Document | URL | HTTP | Redirects | Bytes |
|---|---|---|---|---|
| Deed | `https://creativecommons.org/licenses/by-nc-sa/3.0/` | 200 | 0 | 37273 |
| Legal code | `https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode.en` | 200 | 0 | 56255 |

Method: `curl -sS -L`, default user agent, 2026-08-08. No bot block, no redirect, no soft-404.
Raw bytes parsed locally, no summarizing layer.

Page `<title>`: `Deed - Attribution-NonCommercial-ShareAlike 3.0 Unported - Creative Commons`
Declared `<link rel="canonical">`: `https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en`
On-page "Canonical URL" article text: `https://creativecommons.org/licenses/by-nc-sa/3.0/`
Legal code version line: `Version 3.0 • See the errata page for any corrections and the date of change`

**Quotation convention.** Quotations reproduce the rendered text with HTML source line-wrap
whitespace collapsed to single spaces. Characters are otherwise unaltered, including the deed's
own em dashes and three defects in the served legal code flagged inline below (`con-nection`,
`a Adaptation`, and a wrong cross-reference). Do not correct them when quoting.

## 1 · The older-version notice, verbatim

Under the heading `Notice`, at the top of the page:

> This is an older version of this license. Compared to previous versions, the 4.0 versions of all CC licenses are more user-friendly and more internationally robust. If you are licensing your own work, we strongly recommend the use of the 4.0 license instead: Deed - Attribution-NonCommercial-ShareAlike 4.0 International

Advice to licensors about future choices. Not a withdrawal and not an expiry. Material licensed
under 3.0 stays under 3.0.

## 2 · The deed's own summary of what is permitted

Heading: **You are free to:**

> **Share** — copy and redistribute the material in any medium or format

> **Adapt** — remix, transform, and build upon the material

> The licensor cannot revoke these freedoms as long as you follow the license terms.

The `for any purpose, even commercially` clause that ends both CC BY freedoms is **absent**, not
negated.

## 3 · The deed's own summary of what is required

Heading: **Under the following terms:**

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **NonCommercial** — You may not use the material for commercial purposes.

> **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Heading: **Notices:**

> You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

## 4 · ShareAlike, exact scope

### 4a · The deed's ShareAlike sentence and footnote, verbatim

> **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

> **same license** — You may also use a license listed as compatible at https://creativecommons.org/compatiblelicenses

**Both are byte-identical to the CC BY-NC-SA 4.0 deed.** Verified by extracting the
`ref-same-license` footnote from both fetched pages and comparing: the strings match exactly. CC
now serves one deed template across versions.

### 4b · The legal code offers no compatibility route

**This is the divergence.** Measured on the fetched bytes: the strings `Creative Commons
Compatible License` and `compatiblelicenses` appear **0 times** in the CC BY-NC-SA 3.0 legal
code, while `compatiblelicenses` appears **2 times** in the 3.0 deed page. The deed offers a
route the licence it summarizes does not contain.

The legal code's actual ShareAlike clause, `<li id="s4b">`, complete and verbatim:

> You may Distribute or Publicly Perform an Adaptation only under: (i) the terms of this License; (ii) a later version of this License with the same License Elements as this License; (iii) a Creative Commons jurisdiction license (either this or a later license version) that contains the same License Elements as this License (e.g., Attribution-NonCommercial-ShareAlike 3.0 Unported) ("Applicable License"). You must include a copy of, or the URI, for Applicable License with every copy of each Adaptation You Distribute or Publicly Perform. You may not offer or impose any terms on the Adaptation that restrict the terms of the Applicable License or the ability of the recipient of the Adaptation to exercise the rights granted to that recipient under the terms of the Applicable License. You must keep intact all notices that refer to the Applicable License and to the disclaimer of warranties with every copy of the Work as included in the Adaptation You Distribute or Publicly Perform. When You Distribute or Publicly Perform the Adaptation, You may not impose any effective technological measures on the Adaptation that restrict the ability of a recipient of the Adaptation from You to exercise the rights granted to that recipient under the terms of the Applicable License. This Section 4(d), applies to the Adaptation as incorporated in a Collection, but this does not require the Collection apart from the Adaptation itself to be made subject to the terms of the Applicable License.

Three permitted Applicable Licenses, exhaustively: this licence, a later version with the same
License Elements, or a CC jurisdiction licence with the same License Elements. No compatibility
list. A page must not tell a reader they may relicense a BY-NC-SA 3.0 adaptation under something
merely listed as compatible.

**Defect in the served page, preserved above.** This clause is `id="s4b"`, so it is Section 4(b),
but its own closing self-reference reads `This Section 4(d), applies to the Adaptation` and the
anchor links to `#s4d`, which is the attribution clause. The stray comma after the reference is
also in the bytes. The quotation above reproduces this exactly. Attribution is genuinely 4(d) in
BY-NC-SA 3.0, because ShareAlike takes 4(b) and NonCommercial takes 4(c); the cross-reference
inside 4(b) is simply wrong.

**Trigger.** `You may Distribute or Publicly Perform an Adaptation only under`. As in 4.0, the
duty attaches on distribution or public performance, not on creation. But note the 3.0 wording
constrains the licence of **the Adaptation**, where 4.0 constrains the Adapter's License applied
to **Your contributions**. That is a real difference in what the obligation covers and a page
comparing the two versions should not flatten it.

### 4c · NoDerivatives

**Not present.** Measured: the "Under the following terms" list has exactly four items,
`Attribution`, `NonCommercial`, `ShareAlike` and `No additional restrictions`. Adaptation is
permitted, subject to 4(b).

## 5 · The three answers a page will need

**Commercial use: prohibited.** Deed condition and footnote, verbatim:

> **NonCommercial** — You may not use the material for commercial purposes.

> **commercial purposes** — A commercial use is one primarily intended for commercial advantage or monetary compensation.

Legal code Section 4(c), verbatim. **The typo `con-nection` is in the served bytes**, reproduced
exactly:

> You may not exercise any of the rights granted to You in Section 3 above in any manner that is primarily intended for or directed toward commercial advantage or private monetary compensation. The exchange of the Work for other copyrighted works by means of digital file-sharing or otherwise shall not be considered to be intended for or directed toward commercial advantage or private monetary compensation, provided there is no payment of any monetary compensation in con-nection with the exchange of copyrighted works.

Note `private monetary compensation` in 3.0 where 4.0 says `monetary compensation`.

**Indication of changes: required only when you create an Adaptation, and it sits inside the
grant.** The deed's Attribution clause says `indicate if changes were made`, which is 4.0
template wording served on a 3.0 page. The deed's own footnote qualifies it, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

The legal code confirms it. Section 3(b), verbatim, inside the License Grant:

> to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";

Byte-identical to the CC BY 3.0 grant clause staged in `cc-by-3-0.md`. The duty is `clearly
label, demarcate or otherwise identify`, and it is a **condition of the adaptation right**, so
failing it means the adaptation was never licensed at all.

**Attribution must contain**, per legal code Section 4(d), verbatim. **The article error
`a Adaptation` is in the served bytes**, reproduced exactly:

> If You Distribute, or Publicly Perform the Work or any Adaptations or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work; and, (iv) consistent with Section 3(b), in the case of an Adaptation, a credit identifying the use of the Work in the Adaptation (e.g., "French translation of the Work by Original Author," or "Screenplay based on original Work by Original Author"). The credit required by this Section 4(d) may be implemented in any reasonable manner; provided, however, that in the case of a Adaptation or Collection, at a minimum such credit will appear, if a credit for all contributing authors of the Adaptation or Collection appears, then as part of these credits and in a manner at least as prominent as the credits for the other contributing authors. For the avoidance of doubt, You may only use the credit required by this Section for the purpose of attribution in the manner set out above and, by exercising Your rights under this License, You may not implicitly or explicitly assert or imply any connection with, sponsorship or endorsement by the Original Author, Licensor and/or Attribution Parties, as appropriate, of You or Your use of the Work, without the separate, express prior written permission of the Original Author, Licensor and/or Attribution Parties.

Required credit: all copyright notices kept intact, plus (i) the author or designated Attribution
Parties, (ii) **the title of the Work if supplied**, (iii) the URI, and (iv) **for an adaptation,
a credit identifying the use**, with the two worked examples quoted above.

Items (ii) and (iv) have no counterpart in 4.0. Measured: `title of the Work` appears 0 times in
the CC BY 4.0, CC BY-NC 4.0 and CC BY-NC-SA 4.0 legal codes.

Section 4(a) additionally requires the licence to travel, verbatim:

> You may Distribute or Publicly Perform the Work only under the terms of this License. You must include a copy of, or the Uniform Resource Identifier (URI) for, this License with every copy of the Work You Distribute or Publicly Perform.

Note the compounding: 4(a) makes the underlying licence travel with the Work, and 4(b) separately
makes the Applicable License travel with the Adaptation.

## 6 · Where the deed differs from the legal code

Five differences, all measured on the fetched bytes:

1. **The compatibility route.** Deed footnote: `You may also use a license listed as compatible
   at https://creativecommons.org/compatiblelicenses`. Legal code: 0 occurrences of any
   compatible-licence language. The deed's footnote is 4.0 machinery served on a 3.0 page.
2. **What ShareAlike attaches to.** Deed: `your contributions`. Legal code 4(b): the licence of
   the Adaptation as a whole.
3. **Indication of changes.** Deed main clause states it unconditionally; in 3.0 it conditions
   the adaptation right only. Only the deed's footnote flags this.
4. **Title and adaptation-credit.** Legal code 4(d)(ii) and 4(d)(iv) have no counterpart in the
   deed's main text. The `appropriate credit` footnote covers the title generically, verbatim:

   > **appropriate credit** — If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

   `and may have other slight differences` is the deed declining to enumerate. 4(d)(iv) is one.
5. **The 3.0 deeds omit the "this deed is not a license" notice.** Measured: `highlights only
   some` appears **0 times** on this page and **1 time** on each of the three 4.0 deed pages. The
   `Notice` slot here holds the older-version banner instead. **Say the deed is a summary and not
   the licence anyway**, because it is true of every deed; it just cannot be quoted from this page.

The surviving disclaimer on this page is narrower, verbatim:

> Creative Commons is the nonprofit behind the open licenses and other legal tools that allow creators to share their work. Our legal tools are free to use.

## 7 · Rider next door to the grant

Deed page site footer, verbatim, with its carve-out in the same sentence and a third-party
attribution immediately after:

> Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International license. Icons by Font Awesome.

The page documenting BY-NC-SA 3.0 is itself published under CC BY 4.0. Do not read the footer as
evidence about the instrument the page documents.

Legal code page, verbatim:

> The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication.

followed immediately by the trademark reservation over the `"Creative Commons"` name and logo.

## 8 · What this extract does not establish

- `3.0 Unported` is not `3.0 US`. `INVENTORY.md` line 415 records NYSED per-resource badges
  pinning **3.0 US** while the prose anchor points at **3.0 Unported**. The ported US legal code
  is a different document at a different URL and is **not** staged here. Do not answer a 3.0 US
  question from this file.
- `https://creativecommons.org/compatiblelicenses` was not fetched, so this extract cannot name
  which licences appear on that list. Under this licence the list has no legal effect anyway,
  per section 4b.
- The errata page linked from the version line was not fetched.
- Whether NYSED, MVP or any host still serves material under this licence is a separate fetch
  against that host.
