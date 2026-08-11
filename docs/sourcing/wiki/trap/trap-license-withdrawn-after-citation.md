---
title: "A licence withdrawn after your citation was recorded"
type: trap
sources:
  - sources/host-achieve-the-core.md
  - sources/host-open-middle.md
  - sources/host-learnwithsap.md
  - sources/host-learning-commons-kg.md
  - sources/host-im-kendall-hunt.md
  - sources/verdict-twelve-host-table.md
  - https://achievethecore.org/ccpd
  - https://www.openmiddle.com/
  - https://illustrativemathematics.org/terms-of-use/
  - https://learningcommons.org/terms-of-use/
updated: 2026-08-08
---

# A licence withdrawn after your citation was recorded

## Summary

**A licence verdict is a timestamped observation, not a durable property of a source.** That is the
whole doctrine, and everything below is the mechanism that makes forgetting it invisible.

A grant is a mutable fact: it can be edited, delinked or deleted at any time, with no version
number, no changelog and no notification to anyone who relied on it. A citation is an immutable
record: once written, it renders exactly the same whether it was checked this morning or three
years ago. Nothing in a finished artifact re-checks one against the other, and a stale licence label
looks identical to a fresh one on the page.

Two grants in this corpus vanished inside six months. Each window is bounded by a last-seen and a
first-not-seen observation, not by a stated date:

| Source | Last observed carrying the grant | First observed without it |
|---|---|---|
| Open Middle, CC BY-NC-SA 4.0 | 2026-02-16, Wayback capture | 2026-03-03, Wayback capture |
| Achieve the Core, blanket public-domain dedication | 2026-04-25, Wayback capture | 2026-08-08, live fetch |

This project's own record states the consequence, verbatim: "Folk knowledge about open-education
licensing has been measured wrong three times in this project, not twice."

**Scope of this page.** It holds the mechanism and the re-verification trigger, and nothing else.
The dated register of what changed and when is [[license-withdrawn-grants]]. The per-host facts,
with their footers and snapshot tables, are [[source-open-middle]] and
[[source-achieve-the-core-sap]]. The fetch-and-record procedure is
[[practice-build-a-source-table]]. Those three are not duplicated here.

## When to reach for it

Reach for it whenever a licence claim is being made from anything other than a fetch performed in
the current session: a memory, a prior citation, a third-party OER list, a README, a NOTICE file, a
project cheatsheet, or a wiki page including this one.

Reach for it before publication. Every claim about a source's licence has a half-life, and the
question at the gate is not "was this true" but "when was this last checked, and has anything on
the list moved since".

Reach for it when a source's terms carry a revision clause, which two in this corpus do explicitly.
That is a scheduled risk rather than a surprise, and it should be handled on a schedule.

Do **not** reach for this page to establish what a specific host says today. That is the source
page for that host, refetched.

## How it works

**Step one: the grant moves.** Achieve the Core's `/ccpd` Permissions page served the blanket
dedication continuously at Wayback snapshots dated 2016-03-03, 2017-07-22, 2020-04-30, 2022-01-03,
2024-03-23, 2026-01-11 and 2026-04-25. The latest capture carrying the text is `20260425161111`.
Its final paragraph, verbatim from that capture:

> "All of the content on achievethecore.org is covered by the Creative Commons Public Domain
> Dedication License unless it is marked with the ©, which indicates that it includes content that
> has been licensed to Student Achievement Partners, Inc., from third parties and must be used
> solely as noted when hovering over the © next to the applicable content."

Live on 2026-08-08 that path returns 140,749 bytes byte-identical to the homepage shell, and
"Public Domain Dedication" occurs zero times. What is live instead is a weaker per-item claim,
verbatim from the current Terms of Use:

> "Some material on Our Site is protected by copyright and some material has been dedicated to
> the public domain. For material protected by copyright, SAP owns or has the right to include
> the material on Our Site. Material may be used as indicated on Our Site for the particular
> material."

**Step two: the removal is deliberate and leaves no error.** The footer link to that page is present
in the live markup but commented out, recorded as appearing twice, verbatim:

```
<!-- <li><a href="/ccpd">Permissions</a></li> -->
```

A deleted page would 404. A commented-out link paired with a soft-404 route produces HTTP 200 on
the old URL and no broken link anywhere. Nothing in the site reports a change.

**Step three: the detection layer fails too, in both directions.** This is why the trap is silent
rather than merely easy to miss.

- On Achieve the Core, any unknown path returns the identical homepage shell with HTTP 200. A link
  checker pointed at the old permissions URL reports the citation healthy. See
  [[trap-soft-404-status-proves-nothing]].
- On Open Middle, a default user agent gets HTTP 406 while a browser agent gets HTTP 200 at
  100,227 bytes. A link checker reports a live host broken. See [[trap-down-is-not-one-state]].
- The archive probe used to bound the change can itself lie. The agent bounding the Achieve the Core
  window recorded that its first pass returned gzip bytes, that a grep over them found zero matches,
  and that it nearly filed "CC0 already gone by April 2026" as a finding. See
  [[trap-compressed-body-grepped-as-text]].

None of those three signals tracks the grant. Two of them actively point the wrong way.

**Step four: the citation does not notice.** The label in the bibliography, the licence line in an
attribution block and the verdict in a source table all continue to render their original value.
This project's adjudication of the Open Middle case, recorded as its own reasoning rather than as
the host's words: any memory, prior citation or third-party OER list predating March 2026 says
CC BY-NC-SA 4.0, and is now wrong for material accessed today.

## In practice

**Every licence claim carries a fetch date, or it is not a claim.** A licence claim with no fetch
date is a memory. That rule is CONFIG policy for this wiki rather than a preference, and this page
is the worked reason for it.

**The four mutability surfaces measured in this corpus**, each with the evidence that makes it a
scheduled risk rather than a hypothetical:

| Surface | What makes it mutable | Recorded state |
|---|---|---|
| Achieve the Core | Blanket dedication delinked and its page turned into a soft-404 shell | Withdrawn between 2026-04-25 and 2026-08-08 |
| Open Middle | CC clause deleted from the footer, then a rights-holder change | CC removed between 2026-02-16 and 2026-03-03; holder changed between 2026-03-03 and 2026-05-12 |
| Illustrative Mathematics | Central Terms of Use headed "Effective as of May 21, 2026", with §4 reserving revision at IM's sole discretion | In force at the 2026-08-07 fetch, eleven weeks old |
| Learning Commons | Data Provider revocation reserved in the Terms of Use | Terms state "Last updated: July 1, 2026" |

The Learning Commons clause, verbatim, because its shape differs from the other three:

> "You acknowledge and agree that a Data Provider may, at its sole discretion, revoke access to any
> Content previously made available through the Services."

and, later in the same section, after the report's own elision marker:

> "Revocation of access applies on a prospective basis. Except as otherwise required by applicable
> law or expressly set forth in a separate agreement between a Data Provider and a Build Partner,
> revocation does not automatically require deletion of Adapted Content already created or deployed
> prior to such revocation."

That is a withdrawal regime that says what happens to work already shipped. The other three say
nothing about it, which is precisely the gap the counsel question in gotcha 4 sits in.

**The re-verification trigger, which this page owns.** This project's own verdict document records
it, and it is a trigger rather than a schedule: three grants in this corpus changed inside the six
months before the fetch, and IM's terms are eleven weeks old and revisable at sole discretion.
Therefore **re-pull the licence surface for the affected hosts before this repository is published,
and record the new fetch date in the attribution block.** In the twelve-host table those are rows 1,
4, 10 and 11: `im.kendallhunt.com`, `accessim.org`, `openmiddle.com` and `achievethecore.org`.

The trigger says when and which. The procedure for actually doing it, raw bytes over a summarizing
layer, HTTP status and fetch date on every claim, soft-404 detection by byte-diff, belongs to
[[practice-build-a-source-table]], and the place the new date lands belongs to
[[practice-assemble-an-attribution-block]].

## Gotchas & constraints

**1. The windows are bounded, not dated. Do not narrow them.** The Achieve the Core withdrawal sits
between 2026-04-25 and 2026-08-08. The Open Middle removal sits between 2026-02-16 and 2026-03-03,
and Wayback captured nothing between those two dates. Both are recorded as unnarrowed gaps that a
more granular archive query or a question to the operator could close. Stating a single date for
either would be a fabricated number.

**2. The licence and the rights-holder can move separately, and on Open Middle they did.** The CC
clause went first. The holder changed from Open Middle Partnership to Glenrock Consulting, LLC
between 2026-03-03 and 2026-05-12, which is a later and independent event. A page that collapses
them into one change gets both the date and the causation wrong.

**3. Both observed movements went from more open to less open, and two data points are not a law.**
Open Middle's all-rights-reserved is strictly more restrictive than the CC BY-NC-SA 4.0 it replaced,
and Achieve the Core's per-item claim is weaker than the blanket dedication. This corpus contains no
observed movement in the other direction. It also contains no census: grants may have opened
elsewhere without anyone looking.

**4. Whether a withdrawn dedication reaches back is a legal question, and no fetch will settle it.**
A public-domain dedication is generally understood to be irrevocable, which would favour "material
published under it stays dedicated", but that turns on whether the dedication was validly made, to
which items, and when each item was published. This project's own record calls it "the single most
consequential open question in the corpus" and routes it to counsel. The same shape recurs for Open
Middle: whether the CC removal affects copies obtained before 2026-02-16 is unresolved. Neither is
asserted anywhere in this wiki.

**5. A withdrawal removes a fallback, not just a label.** Any plan that quietly assumed "worst case,
we can still adapt it under the CC terms" loses that floor the day the clause is deleted. The
verdict moves from `quote_sharealike` to `cite_only`, and material already drafted against the old
assumption has to be re-derived rather than re-attributed.

**6. The base rate is unknown because nobody looked at the stable hosts.** No Wayback cross-check
was run against `im.kendallhunt.com`, `tasks.illustrativemathematics.org`, `accessim.org`,
`map.mathshell.org` or the Learning Commons repository: the archive step was conditioned on a host
being dead or blocked. For those hosts, when the current footer was introduced is simply unknown.
The two withdrawals this project found are the two it was positioned to find.

**7. An artifact's own date is not the grant's date.** A footer reading "Typeset May 4, 2016" says
when the page was generated, not when its licence was last confirmed in force. Read the date on your
own fetch, never the date printed on the source.

## Related

- [[license-withdrawn-grants]] is the dated register this page's mechanism operates on, plus the
  standing fact that IM's terms are revisable at sole discretion.
- [[source-open-middle]] holds the full snapshot table, the live all-rights-reserved footer and the
  rights-holder transfer; [[source-achieve-the-core-sap]] holds the archived dedication, the
  commented-out footer link and the current per-item terms.
- [[license-public-domain-dedication]] is the instrument that was withdrawn, and why "CC0" is an
  inference nobody can read off the page that granted it. [[license-all-rights-reserved]] is what
  Open Middle resolves to now.
- [[source-im-kendall-hunt]] is the host whose governing terms carry the explicit revision clause,
  and [[source-learning-commons-kg]] is the export whose terms reserve prospective revocation.
- [[trap-soft-404-status-proves-nothing]] is why the delinked permissions page still answers 200,
  and [[trap-down-is-not-one-state]] is why a live host reads as broken to a link checker. Neither
  signal can be trusted as a change detector.
- [[trap-compressed-body-grepped-as-text]] is the near-miss that almost mis-dated one of these two
  windows.
- [[concept-cite-quote-adapt]] is the verdict this page's mechanism silently invalidates.

## Composes with

- [[practice-build-a-source-table]] is the procedure this page triggers. This page says when and
  which; that page says how, and produces the fetch date the claim then carries.
- [[practice-assemble-an-attribution-block]] is where the refreshed fetch date lands in the shipped
  artifact, which is the only place a reader can see how old the verdict is.

## References

Primary evidence, fetched by this project and staged verbatim in this wiki:

- `https://achievethecore.org/ccpd` HTTP 200, 140,749 bytes, 2026-08-08, byte-identical to the
  homepage shell; and the archived text at
  `https://web.archive.org/web/20260425161111id_/https://achievethecore.org/ccpd`, HTTP 200,
  retrieved with `--compressed`.
- `https://achievethecore.org/terms-of-use` HTTP 200, 93,954 bytes, 2026-08-08.
- `https://www.openmiddle.com/` HTTP 200 with a browser user agent, 100,227 bytes, 2026-08-08, plus
  the Wayback `id_` captures bounding the removal window.
- `https://illustrativemathematics.org/terms-of-use/` HTTP 200, 2026-08-07, header "Effective as of
  May 21, 2026", §4 reserving revision at IM's sole discretion.
- `https://learningcommons.org/terms-of-use/` HTTP 200, 2026-08-08, "Last updated: July 1, 2026".

Staged extracts, all staged 2026-08-08:

- `sources/host-achieve-the-core.md`, primary. §2 the SPA soft-404 measurement and the
  commented-out footer link, §3 the live terms verbatim, §4a the archived dedication, §4b the
  snapshot series and the measured removal window, §4c the compressed-body method warning.
- `sources/host-open-middle.md`, primary. §1 the user-agent measurement, §3 the live footer, §5 the
  snapshot table and the two separate events, §8 the unresolved retroactivity question.
- `sources/host-learnwithsap.md`, primary. §3a the surviving dedication on the sibling domain, §3d
  the soft-404 permissions path on Achieve the Core.
- `sources/host-learning-commons-kg.md`, primary. §8 the revocation clause.
- `sources/host-im-kendall-hunt.md`, primary. The Terms of Use effective date and the revision
  clause that makes this host's verdict dated rather than settled.

This project's own adjudication, cited as this project's reasoning and not as any outside party's
statement: `sources/verdict-twelve-host-table.md` §3 corrections 3 and 8, row 10 on the
stale-citation consequence, §6 the two bounded windows and the irrevocability question listed as not
closeable by fetching, and the re-verification trigger naming rows 1, 4, 10 and 11.
