---
title: "CC BY (4.0 and 3.0 Unported)"
type: license
sources:
  - https://creativecommons.org/licenses/by/4.0/
  - https://creativecommons.org/licenses/by/4.0/legalcode.en
  - https://creativecommons.org/licenses/by/3.0/
  - https://creativecommons.org/licenses/by/3.0/legalcode.en
  - sources/cc-by-4-0.md
  - sources/cc-by-3-0.md
  - sources/host-im-kendall-hunt.md
  - sources/host-math-vision-project.md
  - sources/host-math-mistakes.md
  - sources/host-learning-commons-kg.md
  - sources/host-openstax.md
  - sources/host-eric.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# CC BY (4.0 and 3.0 Unported)

## Summary

CC BY is the plain-attribution regime: the only grant family in this corpus that clears citation,
quotation and paraphrase-and-republish with no copyleft and no commercial bar. It is also the
licence this repo itself ships under, which makes it the only page here with an outbound
direction as well as an inbound one.

**"CC BY" names two different instruments here and their duties are not the same.** 4.0
International and 3.0 Unported are separate documents at separate URLs. A notice reading only
"Creative Commons Attribution" is under-specified, and upgrading a 3.0 label to 4.0 changes what a
credit line must contain. Both were fetched for this wiki on 2026-08-08 and staged verbatim.

Three facts, each measured on fetched bytes rather than remembered:

1. **Neither ShareAlike nor NoDerivatives is present on either deed.** The "Under the following
   terms" list has exactly two items on both.
2. **The deed is not the licence, and it says so on 4.0 but not on 3.0.** The string
   `highlights only some` appears 1 time on each of the three 4.0 deed pages fetched and 0 times
   on the 3.0 deeds. The disclaimer is true of every deed; it just cannot be quoted from a 3.0 one.
3. **The grant attaches to a host and often to a record, not to a brand.** Here one publisher runs
   CC BY on one host and CC BY-NC on another, one contradicts itself between a page and the file
   that page serves, and one publisher's edition marker does not track its licence at all.

## When to reach for it

Reach for this page when a host notice names Attribution and nothing else, and you need to know
what the credit line must contain before anything ships. Reach for it when choosing between two
candidate sources and one is ShareAlike: under this project's ruling R9, recorded verbatim in
`INVENTORY.md` as "The repo ships CC BY 4.0 and writes from standard text only. No paraphrase from
any ShareAlike source, ever", the plain-BY sources are the only ones an adapted through-line can
rest on.

Reach for it before writing any version number into an attribution string.

Do **not** reach for this page to settle what a specific host serves today. That is a dated fetch
against that host with the sentence pasted. This page is evidence about the instruments only.

## How it works

### The two freedoms, and the clause that carries commercial use

Both deeds state the freedoms in byte-identical wording. CC BY 4.0, verbatim:

> **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.

> **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

The trailing `for any purpose, even commercially` sits on both limbs of both BY deeds. It is the
clause the NC deeds **delete** rather than negate, which is why comparing deeds means comparing
whole sentences: a search for a "not" will not find the difference. See [[license-noncommercial]].

### The two conditions, and what is absent

> **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

> **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

That is the whole list. `ShareAlike` and `NoDerivatives` appear zero times in it. The nearest thing
CC BY 4.0 has to a downstream rule is a floor rather than copyleft, legal code Section 3(a)(4):

> If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

Your adaptation may carry any licence you like so long as it does not block recipients from
exercising CC BY on the underlying material. That is the structural difference from
[[license-sharealike]], where the adapter's licence is dictated rather than constrained.

### 4.0 versus 3.0, the three differences that reach a credit line

**Indication of changes.** Under 4.0 it is owed whenever you Share, including unmodified. The
deed's footnote, verbatim:

> **indicate if changes were made** — In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

Two duties sit there: indicate your own modification, and **retain** any indication of previous
ones. Under 3.0 the duty exists only on an adaptation and sits inside the grant as a condition of
the adaptation right, worded `clearly label, demarcate or otherwise identify`. Failing it under
3.0 means the adaptation was never licensed, not merely that the credit was thin.

**Title.** Required by CC BY 3.0 Section 4(b)(ii), `the title of the Work if supplied`. Measured:
`title of the Work` appears 1 time in the CC BY 3.0 legal code and 0 times in CC BY 4.0.

**Adaptation credit.** CC BY 3.0 Section 4(b)(iv) requires `a credit identifying the use of the
Work in the Adaptation`. The 3.0 deed does not mention this at all, in the main text or any
footnote, and it has no 4.0 counterpart.

### What 4.0 attribution must actually contain

The deed's two words compress seven legal-code items. Section 3(a)(1) requires you to **retain**,
`if it is supplied by the Licensor`: creator and attribution-party identification, a copyright
notice, a notice referring to the Public License, a notice referring to the warranty disclaimer,
and a URI or hyperlink to the material; and to indicate modification and retain indications of
previous modification; and to indicate the licence and include its text or a link.

The conditional matters: **do not state that a copyright notice is required where the source
supplies none.** The satisfaction rule is deliberately loose, verbatim:

> You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.

That sentence is what licenses a single shipped attribution file rather than a credit block on
every page. See [[practice-assemble-an-attribution-block]].

## In practice

Each row is a dated host measurement, not a property of a publisher.

| Host or artifact | Version measured | Recorded evidence |
|---|---|---|
| `im.kendallhunt.com`, IM K-12 Math 1st edition | CC BY 4.0 | Footer "© 2019 Illustrative Mathematics®. Licensed under the Creative Commons Attribution 4.0 license." on 7 of 8 sampled curriculum pages; the grant text is off-host in IM Terms §7.1. 2026-08-07 |
| `im.kendallhunt.com/MS/`, IM 6-8 Math | CC BY 4.0 | Same licence, different copyright holder: Open Up Resources 2017-2019 for the base curriculum. 2026-08-07 |
| `mathematicsvisionproject.org/geometry.html` | CC BY 4.0 | Page notice plus `href` to `by/4.0/`; `g1_mod4_se_82017f.pdf`, 70pp, carries CC BY 4.0 on the cover and in 68 page footers. 2026-08-08 |
| `mathmistakes.org` | CC BY **3.0 Unported** | Sidebar `rel=license` widget, recoverable only from Wayback; the live host serves a PHP fatal error. 2026-08-07 |
| Learning Commons KG v1.11.0 export | CC BY 4.0 | `247786` of `247786` nodes carry `"license":"https://creativecommons.org/licenses/by/4.0/"`, 0 nodes missing the field. 2026-08-08 |
| OpenStax slugs `algebra-and-trigonometry`, `precalculus` | CC BY 4.0 | CMS API returned `license_name: Creative Commons Attribution License`, `license_version: 4.0`. 2026-08-08 |
| Arhin and Hokor 2021, `mathsciteacher.com` | CC BY 4.0 | The in-PDF notice names the licence with no version; 4.0 is pinned only on the journal's open-access policy page. 2026-08-08 |

**The attribution string is a property of the record.** On `im.kendallhunt.com` a `/HS/` page
credits Illustrative Mathematics 2019 and a `/MS/` page must credit Open Up Resources 2017-2019.
Both paste-ready blocks live on [[source-im-kendall-hunt]]; the rule lives on
[[concept-attribution-per-record]].

**Two hosts here supply no attribution string at all.** `mathmistakes.org` offers a bare CC BY
widget, and the Learning Commons export supplies a different `attributionStatement` per record.
Where none is published, construct a reasonable one from title, author, source URL and licence,
and say in the deliverable that you constructed it.

## Gotchas & constraints

**1. Do not silently upgrade a 3.0 label to 4.0.** `mathmistakes.org` is 3.0 Unported, recorded on
six root captures from `20140517212051` to `20260220051333`. Relabelling it 4.0 misstates the
duties in both directions: it drops the title and adaptation-credit requirements and invents a
retain-previous-modifications duty 3.0 does not impose. The 3.0 deed's banner recommending 4.0 is
advice to licensors choosing a licence, not a withdrawal. Material licensed under 3.0 stays there.

**2. `Unported` is not `US`.** Different documents at different URLs, and neither ported variant
is staged in this wiki. Do not answer a 3.0 US question from the Unported extract;
[[source-engageny-nysed]] is where that ambiguity actually bites.

**3. The 3.0 deed serves 4.0 wording.** Its main Attribution clause states the changes indication
unconditionally, which is the 4.0 rule, and only its footnote corrects this. Reading the deed
alone gives you the wrong duty on a 3.0 source and no notice of the title and adaptation-credit
duties, which is the direction that matters.

**4. The licence does not track the edition marker.** Ten OpenStax maths slugs were queried on
2026-08-08: two returned `Creative Commons Attribution License` `4.0` and eight returned the
NC-SA string. `calculus-volume-1` carries no `-2e` suffix, has `id` 74 and first published
`2016-03-10`, one day after `algebra-and-trigonometry`, yet returned NC-SA. **The staged evidence
does not support a rule of the form "first editions are CC BY."** The only defensible statement is
per-slug: name the slug, quote the two returned fields, give the fetch date. See
[[source-openstax]].

**5. A host can contradict itself between a page and the file it serves.** MVP's
`/secondary-mathematics-ii.html` claims CC BY-NC-SA over files whose covers and page footers say
CC BY 4.0, and which notice governs was recorded as not resolvable from published text. The route
around it is operational: use the Geometry Module 4 path, where page and file agree. See
[[source-math-vision-project]].

**6. A CC BY sentence in a research PDF often carries no version and no link.** Arhin and Hokor
2021 names the licence with neither, and the 4.0 pin exists only on the journal's policy page. Of
7 ERIC-hosted PDFs opened, the tally was 1 CC BY, 2 explicitly restrictive, 4 completely silent.
ERIC grants nothing; see [[source-eric]] and [[license-unmarked-silence]].

**7. The creativecommons.org footer is not evidence about the instrument.** Every deed page
fetched carries "Except where otherwise noted, content on this site is licensed under a Creative
Commons Attribution 4.0 International license." The page documenting CC BY 3.0 is itself CC BY 4.0.

**8. The outbound direction, and what shipping CC BY 4.0 costs.** `No additional restrictions`
bars adding an NC or ND rider on top of CC BY material we redistribute. ShareAlike material cannot
be paraphrased into a CC BY 4.0 file, because BY-NC-SA 4.0 Section 3(b) requires the Adapter's
License to be a CC licence with the same `License Elements` and CC BY 4.0's elements are
Attribution alone; see [[trap-sharealike-contaminates-by-paraphrase]]. NoDerivatives material
cannot be paraphrased in at all, because the grant never reaches adaptation; see
[[license-noderivatives]].

**9. Every CC BY grant here has a carve-out beside it.** On both IM hosts and on OpenStax the
grant sentence is followed at once by a trademark carve-out and then a third-party image or asset
carve-out. Those are part of the notice. See [[concept-third-party-carve-out]].

**10. A grant with no fetch date is a memory.** Two grants in this corpus were withdrawn inside
six months. See [[license-withdrawn-grants]] and [[trap-license-withdrawn-after-citation]].

## Related

- [[license-noncommercial]] rides on this baseline by deleting the commercial clause.
- [[license-sharealike]] dictates the adapter's licence rather than constraining it.
- [[license-noderivatives]] removes the `Adapt` freedom entirely.
- [[license-public-domain-dedication]] is the only regime here looser than plain BY.
- [[license-unmarked-silence]] is what a source with no notice resolves to, which is not this.
- [[concept-cite-quote-adapt]] is the three-operation split every verdict here applies.
- [[concept-attribution-per-record]] is why the credit line belongs to the record.
- [[source-im-kendall-hunt]] is the spine host, and holds both paste-ready attribution blocks.
- [[source-learning-commons-kg]] is the CC BY 4.0 data layer under every standard statement.
- [[source-math-mistakes]] is the 3.0 Unported instance behind gotcha 1.
- [[trap-license-lives-off-the-obvious-page]] is why a clean fetch of a CC BY host's landing page
  can return "unlicensed".

## Composes with

- [[practice-assemble-an-attribution-block]] consumes the three components and the satisfaction
  rule above into the repo's shipped attribution file.
- [[practice-build-a-source-table]] is the procedure that dates every row in the table above.

## References

Instruments fetched by this project 2026-08-08, `curl -sS -L`, default user agent, raw bytes
parsed locally, no summarizing layer:

- `https://creativecommons.org/licenses/by/4.0/` HTTP 200, 32178 bytes, 0 redirects, and
  `.../by/4.0/legalcode.en` HTTP 200, 48970 bytes. Sections 2(a), 3(a)(1), 3(a)(4).
- `https://creativecommons.org/licenses/by/3.0/` HTTP 200, 32052 bytes, 0 redirects, and
  `.../by/3.0/legalcode.en` HTTP 200, 51333 bytes. Sections 3(b), 4(a), 4(b).

Staged extracts in this wiki, all staged 2026-08-08: `sources/cc-by-4-0.md` and
`sources/cc-by-3-0.md` (primary, both instruments verbatim with the absence measurements);
`sources/host-im-kendall-hunt.md` (primary, both band footers and IM Terms §7.1);
`sources/host-math-vision-project.md` (primary, the clean Geometry route and the page-versus-file
conflict); `sources/host-math-mistakes.md` (primary, the 3.0 widget and its snapshot table);
`sources/host-learning-commons-kg.md` (primary, the whole-export census);
`sources/host-openstax.md` (primary, the CMS API responses byte-exact); `sources/host-eric.md`
(primary, the 7-PDF tally and the version pin); `sources/verdict-twelve-host-table.md`
(reference, §2 verdict key, §3 corrections 1, 5, 6 and 9, and the §4 attribution blocks).

This project's own record, cited as this project's ruling and not as any outside party's
statement: `INVENTORY.md` quotes design spec §2 ruling R9 verbatim, and the project's governing ruling
records the project ruling the same on 2026-08-08.
