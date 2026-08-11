---
title: Third-party carve-outs inside a licensed work
type: concept
sources:
  - sources/host-im-kendall-hunt.md
  - sources/host-accessim-360.md
  - sources/host-mars-map.md
  - sources/host-im-task-bank.md
  - sources/host-math-vision-project.md
  - sources/host-engageny-nysed.md
  - sources/cc-by-4-0.md
  - sources/cc0-1-0.md
  - sources/verdict-twelve-host-table.md
  - https://illustrativemathematics.org/terms-of-use/
  - https://im.kendallhunt.com/HS/teachers/2/3/index.html
updated: 2026-08-08
---

# Third-party carve-outs inside a licensed work

## Summary

A licence covers the licensor's own expression. It does not automatically cover everything rendered
on the page beside it. Two classes of thing routinely sit inside a cleanly licensed work while
standing outside its grant:

1. **Embedded third-party content**, most often images, but in this corpus also the standards text
   that every host reproduces and none of them owns.
2. **Names and marks**, meaning the licensor's own trademarks, logos and certification badges, which
   are carved out of the grant by the same footer that makes it.

Both classes are usually announced in the notice itself. On the two Illustrative Mathematics
curriculum hosts the grant sentence is followed **immediately** by the trademark carve-out and then
by the third-party image carve-out. The three sentences are one footer, and the carve-outs are part
of the notice rather than decoration around it. A reader who quotes only the first sentence has
quoted a third of the licensing statement.

The error this prevents is specific and expensive: taking a verified `quote_and_adapt` verdict on a
lesson page and reusing that page's figures under it. On `im.kendallhunt.com` the grant is verified
and every figure in the target units is uncleared, and those two facts coexist.

## When to reach for it

Reach for it before reproducing any image, diagram or photograph from a licensed source, and before
putting any source's name or logo on something you produced. Reach for it whenever a work reproduces
material a third party plainly authored: standards text, a named pedagogical routine, an assessment
framework, a photograph with a credit line. And reach for it before placing a figure in a package,
because that is where the clearance question becomes concrete and cheap to answer. See
[[practice-place-and-alt-text-a-figure]].

Do **not** reach for it for the neighbouring case where something merely looks like a licence notice
but is not part of the work at all, such as a font vendor's copyright string in a PDF's embedded
metadata. That is [[trap-font-notice-is-not-a-content-license]].

## How it works

### The licences say the carve-out exists

CC BY 4.0's own deed says so twice in its Notices block, verbatim:

> You do not have to comply with the license for elements of the material in the public domain or
> where your use is permitted by an applicable exception or limitation.

> No warranties are given. The license may not give you all of the permissions necessary for your
> intended use. For example, other rights such as publicity, privacy, or moral rights may limit how
> you use the material.

CC0 1.0 is blunter still, legal code Section 4(c), verbatim:

> Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work
> or any use thereof, including without limitation any person's Copyright and Related Rights in the
> Work.

And Creative Commons applies the second class to itself. Its legal code pages state that the licence
texts are dedicated to the public domain under CC0, then immediately reserve the mark, verbatim:
"Creative Commons does not authorize the use of the trademark "Creative Commons" or any other
trademark or logo of Creative Commons without its prior written consent". The text is free and the
name is not. Two facts, not one.

### Class 1: embedded third-party content

The verbatim curriculum footer on `im.kendallhunt.com`, HTTP 200, fetched 2026-08-07:

> This book includes public domain images or openly licensed images that are copyrighted by their
> respective owners. Openly licensed images remain under the terms of their respective licenses. See
> the image attribution section for more information.

Note what that sentence does and does not do. It tells you the images are not under the page grant.
It does not tell you what they are under. The answer lives in an index, and on this host the index
could not be found.

The class is broader than images. `map.mathshell.org` carves out text in its global footer, HTTP
200, fetched 2026-08-08, verbatim:

> State, district and CCSSI standards appear courtesy of their respective
> authors. All other material Copyright © 2007-2015 Mathematics
> Assessment Resource Service, University of Nottingham.

The standards text inside a MARS lesson is not MARS's to license. The same is true of every host in
this corpus that reproduces a standard statement, which is all of them, and it is why standards text
carries its own upstream notice. See [[source-corestandards-nga-ccsso]].

### Class 2: names and marks

The sentence sitting between the grant and the image carve-out on `im.kendallhunt.com`, verbatim:

> The Illustrative Mathematics name and logo are not subject to the Creative Commons
> license and may not be used without the prior and express written consent of Illustrative
> Mathematics.

Reinforced off-host by Terms of Use Section 7.3, HTTP 200, fetched 2026-08-07, verbatim:

> Use of the Illustrative Mathematics name, brand, associated trademarks, or curriculum content
> beyond the scope of the applicable Creative Commons license requires express written permission
> from IM. Unauthorized commercial use or brand co-option is a violation of these Terms and may
> infringe IM's intellectual property rights. The Illustrative Mathematics® company name and
> associated trademarks ("IM®" and "IM Illustrative Mathematics Certified®") are not subject to use
> with Creative Commons licenses.

The distinction that keeps this workable: **naming a source in a citation is nominative use and is
unaffected. Branding your own material with the mark is not.** Writing "based on a lesson from
Illustrative Mathematics" is a citation. Putting the IM logo or the "IM Certified" badge on a
package you assembled is a use of the mark.

### The test, and where it is available

`accessim.org` publishes an actual per-image test in its Course Guide Attributions section, HTTP
200, fetched 2026-08-07, verbatim:

> Images that are not the original work of Illustrative Mathematics are in the public
> domain or released under a Creative Commons Attribution (CC-BY) license, and include an
> appropriate citation. Images that are the original work of Illustrative Mathematics do
> not include such a citation.

That is a usable rule on that host: an inline citation marks a third-party image. `map.mathshell.org`
and `mathematicsvisionproject.org` do the same thing by convention rather than by rule, crediting
photographers inline.

`im.kendallhunt.com` publishes no such test. The footer points at an image attribution section that
could not be located: **all 8 guessed paths returned 404**, and no `href` containing "attribution"
exists in any sampled page. The verifying agent's recorded consequence, verbatim:

> the per-image license status for any specific IM figure is UNVERIFIED from here.

Where the test is absent, the honest position is that every figure on that host is uncleared, and
the remedy is to use the host's text without the host's images.

## In practice

**MVP, where the carve-out is legible per figure.** Geometry Module 4 and its Secondary Math II
twin interleave Flickr-sourced photographs, each credited inline. The verifying agent recorded these
credits verbatim from one module: `CC BY the kirbster "Pythagorean Theorem"`, `CC BY Stuart Heath
"tree shadow"`, `CC BY Jorge Jaramillo "depth . . ."`, `CC BY Jacque Davis "origami birds"`,
`CC BY Official U.S. Navy Page`, `CC BY Lidyanne Aquino`, `CC BY Andi Saleh`, `CC BY Hammad Kahn`,
`CC BY Barkbud`, `CC BY pbemjestes`, plus a bare Flickr URL. Reusing one of those photographs means
attributing the photographer, not MVP. The safest posture the report records is not to reproduce
them.

**accessim.org, where the carve-out is looser than the grant.** The site licence is CC BY-NC 4.0.
The non-IM images are recorded as public domain or CC BY, which is **less** restrictive than the
page they sit on. A carve-out is not a synonym for a restriction. It means the embedded item has its
own terms, and those terms may run either way.

**accessim.org, where a permission does not travel.** The same Attributions section, verbatim:

> *Notice and Wonder* and *I Notice/I Wonder* are trademarks of the National Council of
> Teachers of Mathematics, reflecting approaches developed by the Math Forum
> (https://imk12.org/MathForum), and used here with permission.

That permission runs to Illustrative Mathematics. It does not run downstream to a reuser of the
lesson. A named routine used with permission inside a CC-licensed work is a class 2 carve-out even
though it is words rather than a logo.

**EngageNY, where the carve-out is broad and its edge is ambiguous.** The archived Terms of Use
carve out, verbatim:

> Permission to copy, use, and distribute materials as described above shall not extend
> to the following:  All images on EngageNY / Information housed on EngageNY.org that is
> credited to other sources / Information on websites to which this site links

The verifying agent is precise about placement: that clause sits under the non-CC "Other EngageNY
materials" heading rather than literally under the CC curricular-documents clause, so whether it
reaches images **inside** the CC-licensed module PDFs is genuinely ambiguous. No module PDF was
opened. The recorded instruction is to treat module diagrams as not cleared.

**The IM task bank, where there is no credit line at all.** Task 1591 embeds photographs served from
a plain-http S3 bucket with no credit line anywhere on the page, and a keyword sweep of six task
pages for `courtesy`, `used with permission`, `photo by`, `wikimedia` and `flickr` returned zero
hits. Silence about an embedded image is the hardest case, because there is nothing to read either
way. The page licence implicitly covers it and the upstream source is unstated.

## Gotchas & constraints

**1. Verifying the grant does not clear the figures, and the two findings must be filed separately.**
`im.kendallhunt.com` is `quote_and_adapt`, verified from a pasted footer, and every figure on it is
uncleared. A source table that records only the verdict has lost the second fact.

**2. Absence of a credit line is not evidence of ownership on a host that has no rule.** The
accessim.org test works because accessim.org publishes it. Applying "no citation means it is theirs"
to a host that never said so is inventing a test.

**3. Nominative use survives; branding does not.** Citing Illustrative Mathematics, Open Middle,
Achieve the Core or Learning Commons by name is normal. Every one of those four reserves its marks
in writing, and Open Middle's is a registered trademark. Do not name a product after a source and do
not imply endorsement.

**4. A carve-out can be looser than the grant it sits inside.** Read it rather than assuming it
narrows.

**5. The clearance question is per figure, not per page.** One lesson page can carry an IM-authored
diagram and a Flickr photograph under a stranger's CC BY. The page grant is one fact; each figure is
another.

**6. This project opened no image and inspected no image metadata.** Every finding here is read off
prose: footers, attribution sections and credit lines. Where a page says a figure is uncleared, that
means unverified from the text, not proven encumbered. Privacy is a further axis that copyright
clearance does not settle, and it is held at [[concept-chain-of-title]].

## Related

- [[concept-cite-quote-adapt]] is the operation split this page qualifies: a page may be
  `quote_and_adapt` for its prose and `cite_only` for its figures.
- [[concept-chain-of-title]] is the adjacent failure where the host never held rights to the
  expression itself, rather than to something embedded in it.
- [[license-cc-by]] holds the grant that the IM and MVP carve-outs sit inside.
- [[license-noncommercial]] holds the accessim.org grant, which its own image carve-out is looser
  than.
- [[trap-font-notice-is-not-a-content-license]] is the third class that used to live here: a
  notice-shaped string that belongs to neither the work nor a third-party contribution.
- [[source-im-kendall-hunt]] carries the unfound image attribution index and the 8 probed paths;
  [[source-accessim-360]] the per-image test and the NCTM permission that does not travel;
  [[source-mars-map]] the standards-text carve-out in the global footer;
  [[source-math-vision-project]] the inline photographer credits; and [[source-engageny-nysed]] the
  broad image carve-out and its placement ambiguity.
- [[source-corestandards-nga-ccsso]] is the upstream owner of the text every host carves out.

## Composes with

- [[practice-place-and-alt-text-a-figure]] is the procedure a figure passes through on its way into
  a package, and a figure that fails the clearance question above never reaches it.
- [[practice-assemble-an-attribution-block]] is where a cleared third-party figure acquires its own
  credit line, separate from the page's.

## References

Host evidence, fetched by this project on the dates stated:
`https://im.kendallhunt.com/HS/teachers/2/3/index.html` HTTP 200, 2026-08-07, the HS footer carrying
the grant, the trademark carve-out and the third-party image carve-out as three consecutive
sentences; `https://illustrativemathematics.org/terms-of-use/` HTTP 200, 2026-08-07, header
"Effective as of May 21, 2026", Section 7.3;
`https://accessim.org/9-12-aga/geometry/course-guide/attributions?a=teacher` HTTP 200, 2026-08-07,
the per-image rule, the CCSS trademark notice and the NCTM permission; `https://map.mathshell.org/`
HTTP 200, 2026-08-08, the global footer carving out state, district and CCSSI standards.

Staged extracts in this wiki, all primary, staged 2026-08-08.
`sources/host-im-kendall-hunt.md`: sections 3 and 10, the footer and the enumerated riders; section
9, the image attribution index that could not be located, with the 8 probed paths and the verbatim
recorded consequence. `sources/host-accessim-360.md`: section 3, the four-paragraph footer as
served; section 5, Course Guide Attributions in full; section 6, riders 3 through 6.
`sources/host-mars-map.md`: section 3b, the global footer; section 5, rider 5.
`sources/host-math-vision-project.md`: section 6, rider 1, the inline Flickr credits as recorded.
`sources/host-im-task-bank.md`: section 5, rider 4, the uncredited task 1591 photographs and the
zero-hit keyword sweep. `sources/host-engageny-nysed.md`: section 3b, the carve-out verbatim;
section 6, rider 5, the placement ambiguity and the treat-as-not-cleared instruction.
`sources/cc-by-4-0.md` and `sources/cc0-1-0.md`: the Notices block, CC0 Section 4(c), and the
Creative Commons trademark reservation.

This project's own adjudication, cited as this project's measurement and not as any outside party's
statement: `sources/verdict-twelve-host-table.md`, reference, row 1 riders, row 2 on the MVP
photographs, row 4 on the accessim.org image and NCTM riders, row 5 on the EngageNY image carve-out,
row 7 on the MARS standards carve-out, and section 6, which files IM's image attribution index as a
gap closeable only by asking IM or registering for a teacher account.
