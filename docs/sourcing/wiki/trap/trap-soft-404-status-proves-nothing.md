---
title: A soft 404 makes HTTP status prove nothing
type: trap
sources:
  - sources/host-accessim-360.md
  - sources/host-achieve-the-core.md
  - sources/host-open-middle.md
  - sources/host-learnwithsap.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# A soft 404 makes HTTP status prove nothing

## Summary

**What the broken case looks like:** `https://host/terms` returns HTTP 200, and the fetch log
records that the terms page was retrieved. There is no terms page. The server answered 200 with
something else entirely, and the something else is byte-identical to what it serves for a path
nobody has ever typed.

Two shapes of this were measured in this corpus, on two hosts, by two different agents:

| Host | Bogus-path probe | What came back | Real pages for comparison |
|---|---|---|---|
| `accessim.org` | `/zzz-definitely-not-a-real-page-9876` | HTTP 200, 1,486,023 bytes, Sentry transaction `GET /[curriculum_slug]` | `/privacy-policy`, 120,462 bytes, genuinely distinct |
| `achievethecore.org` | any unknown path | HTTP 200, the identical 140,749-byte homepage shell | `/terms-of-use`, 93,954 bytes; `/privacy-policy`, 80,465 bytes |

On `accessim.org` a byte-diff of `/terms` against the bogus slug is recorded as identical except
for the echoed slug in nav hrefs and the per-request Sentry trace id. All of
`/terms /terms-of-use /terms-of-service /copyright /license /licensing /permissions /about /faq
/attribution /attributions /legal` returned approximately 1,485,7xx bytes of the same shell. The
recorded conclusion, verbatim:

> **accessim.org has no site-wide terms-of-use, copyright, or license page.**

On `achievethecore.org` the same shape produced a worse outcome, because someone had already
acted on it. The evidence file records the soft-404 as the reason an earlier fetch "found no
licensing statement": it was reading the homepage, not the terms.

**The consequence for this wiki:** a 200 is not evidence that a page exists, and therefore a 200
on a policy path is not evidence about the licence. Under honesty floor F1 a licence claim needs
a pasted sentence from the bytes. On a soft-404 host the bytes are a decoy that reads as a clean
fetch.

## When to reach for it

Reach for this page before recording any negative licence finding from a URL probe. "No terms
page exists" and "the terms page said nothing about licensing" are both conclusions a soft 404
manufactures for free, and both are wrong on at least one host in this corpus.

Reach for it before recording a positive one, too. If `/permissions` returns 200 and your
extractor found no licence string, you may be extracting from a homepage.

Reach for it whenever the host is a single-page application or a modern framework with a
catch-all route. Both measured cases here are that: `achievethecore.org` is recorded as an SPA,
`accessim.org` as Next.js App Router on Vercel with a dynamic catch-all.

Do not reach for this page when the host returns 200 with a body that is not the site's content
at all, such as a stack trace or a bot challenge. That is a different failure with a different
next move. See [[trap-down-is-not-one-state]].

## How it works

A soft 404 is a routing decision. A catch-all route matches the unknown path, the framework
renders a valid page, and the HTTP layer reports what it always reports for a page it rendered.
Nothing is broken and nothing lies: the status code is describing the response, not the
existence of the resource you asked for.

Three properties follow, and each of them defeats a common check:

1. **Status is uninformative.** Every probe returns 200, so a status-only fetch log records
   twelve successful retrievals of pages that do not exist.
2. **Content-type is uninformative.** The shell is real HTML, so a check for `text/html` passes.
3. **Non-empty body is uninformative.** The `accessim.org` shell is over 1.48 MB. A size floor
   set to catch empty responses passes it easily.

What does discriminate is **comparison against a known-nonexistent path on the same host**.
That is the only probe whose expected answer you know in advance.

### The inverse shape, which breaks the same check from the other side

`openmiddle.com` returns HTTP **404** on `/terms/`, `/terms-of-use/`, `/terms-of-service/`,
`/copyright/`, `/permissions/`, `/license/`, `/licensing/`, `/faq/`, `/privacy/` and
`/privacy-policy/`, and serves an approximately 92KB soft-404 template with it. The status is
honest; the body is large. Any check keyed on body size rather than status reaches the same
wrong answer from the opposite direction.

So neither status alone nor size alone is the test. The pair, compared against a control, is.

## In practice

### The probe that replaces the status code

1. **Fetch a deliberately bogus path on the host.** Make it obviously bogus, and record its
   status, its byte count and its body. `accessim.org/zzz-definitely-not-a-real-page-9876` is the
   worked example in this corpus.
2. **Fetch every policy path you care about and diff against that control.** Identical, modulo
   an echoed slug and a per-request trace id, means the page does not exist.
3. **Confirm a real page too.** On `achievethecore.org` the real `/terms-of-use` is 93,954 bytes
   against a 140,749-byte shell, and `/privacy-policy` is 80,465 bytes. Having one confirmed real
   page tells you the discriminator works on this host.
4. **Corroborate a negative independently before writing it down.** For `openmiddle.com` the
   verifying agent confirmed the absence of any policy document three ways: `page-sitemap.xml`
   returned the complete page list with no terms, privacy, copyright or licence page; the site's
   own search for `copyright`, `license` and `permission` returned zero content results; and
   Wayback CDX returned zero captures ever for `openmiddle.com/terms*`, `/copyright*`,
   `/license*` and `/privacy*`, with control queries against the root and `/similar-triangles/`
   proving the CDX endpoint was working.
5. **Write the conclusion at the level the evidence supports.** "This host has no site-wide
   terms page" is supportable. "This host is unlicensed" is not, because the licence may be on
   the deep content pages or off-host entirely. See
   [[trap-license-lives-off-the-obvious-page]].

### What the probe found on the two hosts, in the form a source table needs

- `accessim.org`: no site-wide terms, copyright or licence page. The only real distinct policy
  page is `/privacy-policy`, confirmed to contain no copyright, IP, licence, permitted-use or
  redistribution text. The licence is on the curriculum pages, and only there: the homepage and
  the privacy policy carry no licence notice at all, because the footer is rendered inside the
  curriculum route tree.
- `achievethecore.org`: `/page/terms-of-use` is a shell, `/terms-of-use` is real,
  `/ccpd` is a shell where a real Permissions page used to be. The footer HTML contains,
  commented out and appearing twice, the string `<!-- <li><a href="/ccpd">Permissions</a></li> -->`.
  A second agent, fetching a day earlier, independently found `/permissions`, `/license` and
  `/copyright` all returning HTTP 200 and `cmp`-identical to the fetched root. A removed page and
  a never-existing page produce the same soft 404, and only the archive and the commented markup
  separate them. See [[license-withdrawn-grants]].

## Gotchas & constraints

**1. A soft 404 hides a withdrawal as effectively as it hides an absence.** `achievethecore.org/ccpd`
carried a blanket public-domain dedication continuously across snapshots at 2016-03-03,
2017-07-22, 2020-04-30, 2022-01-03, 2024-03-23, 2026-01-11 and 2026-04-25. The latest snapshot
carrying the text is `20260425161111`. Live on 2026-08-08 the same path is the 140,749-byte
shell and "Public Domain Dedication" occurs 0 times. A probe that trusted the 200 would record
"page present" for a page that had been removed inside the previous few months.

**2. The byte-count fingerprint is not stable, and two of this project's own extracts disagree
about it.** `host-achieve-the-core.md` records the homepage shell at 140,749 bytes, fetched
2026-08-08. `host-learnwithsap.md`, a different agent fetching a day earlier, records it at
137,828 bytes. Both figures are reproduced as written in the staged corpus and neither is
reconciled. Do not average them, do not pick one, and do not carry a byte count from one session
into the next as a test. Re-derive the control in the session you are working in.

**3. Do not run the bogus-path probe at scale.** These are requests to a live host. This
project's adjudication records that IM's Terms §9 bars automated tools that place excessive load
on servers or circumvent technical access controls, and its own sampling on that host was
roughly twenty requests, hand-paced. One control path plus the policy paths you actually need is
enough.

**4. A 200 body that is not the shell is still not necessarily the page.** On `accessim.org` the
Course Guide attributions content lives in the RSC flight payload rather than the initial DOM,
so a summarizing fetcher truncates before reaching it and reports a page with no attribution
text. The bytes were there. The layer reading them was not. See
[[trap-summary-layer-is-not-evidence]].

**5. Decompress before grepping the control.** A raw archive fetch can return gzip bytes, and
grep over them returns zero matches with no error. That near-miss happened in this corpus on the
`achievethecore.org` snapshot and nearly produced a wrong withdrawal date. See
[[trap-compressed-body-grepped-as-text]].

**6. Two intermittent HTTP 000 failures on `accessim.org` are recorded as server-side, not as
blocks and not as soft 404s.** `/9-12-aga/geometry/course-guide/lessons-by-standard?a=teacher`
failed twice, `curl (28) Connection timed out after 40005 ms` then `curl (35) Recv failure:
Operation timed out`, and was never retrieved. A page that never came back is a gap, and this
wiki records it as one rather than folding it into the soft-404 finding.

## Related

- [[source-accessim-360]] is the host whose catch-all produced the worked case, and where the
  licence turned out to be present on the content pages the whole time.
- [[source-achieve-the-core-sap]] is the host where a soft 404 caused an earlier fetch to
  conclude there was no licensing statement, and where a real page was removed behind one.
- [[source-open-middle]] is the inverse shape: honest 404 status, large soft-404 body, absence
  confirmed three independent ways.
- [[trap-down-is-not-one-state]] holds the other reachability signatures a status code fails to
  distinguish, including a 200 whose body is a stack trace.
- [[trap-license-lives-off-the-obvious-page]] is the conclusion this trap tempts you into: no
  terms page found, therefore no licence, when the grant is one level in or on another host.
- [[trap-summary-layer-is-not-evidence]] covers the other way a 200 misleads, where the bytes
  contain the answer and the reading layer does not.
- [[trap-compressed-body-grepped-as-text]] is the extraction failure that turns a present string
  into a measured absence.
- [[license-withdrawn-grants]] is where a page that used to exist, and the dated window in which
  it stopped existing, is recorded.
- [[license-unmarked-silence]] is the doctrine for what a genuine absence of any notice means,
  once the absence has actually been established rather than manufactured by a soft 404.

## Composes with

- [[practice-build-a-source-table]] is the fetch-and-record procedure this probe belongs inside;
  the control path and its byte count are fields that procedure must capture per host, per
  session.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-accessim-360.md`, primary. §1 the reachability table and the two intermittent
  HTTP 000 failures; §2 the bogus-slug measurement, the byte-diff, the twelve identical policy
  paths, the recorded conclusion, and `/privacy-policy` as the only real distinct policy page;
  §4 the per-page licence audit showing the homepage and privacy policy carry no notice; §5 the
  RSC flight-payload extraction note.
- `sources/host-achieve-the-core.md`, primary. §2 the SPA soft-404 measurement, the
  140,749-byte shell, the real `/terms-of-use` and `/privacy-policy` byte counts, the
  commented-out Permissions link, and the recorded byte-size discrepancy against the sibling
  extract; §4b the dated snapshot list and the removal window; §4c the compressed-body method
  warning.
- `sources/host-open-middle.md`, primary. §2 the ten 404 policy paths with the approximately
  92KB soft-404 template, and the three independent confirmations that no policy document exists.
- `sources/host-learnwithsap.md`, primary. §3d, the independent soft-404 measurement on the same
  host: `/permissions`, `/license` and `/copyright` all HTTP 200 and recorded as `cmp`-identical
  to the fetched root, at a homepage-shell size of 137,828 bytes, with the same commented-out
  footer link observed as visible `-->` fragments in the rendered tail.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication: Row 4, where
  the recorded verdict is "Status codes prove nothing on this host", and Row 11, where it is
  "HTTP status is a useless existence signal here"; and Row 1's record of the terms clause bearing
  on automated load.

Every status code, byte count and diff result above was measured by an agent of this project
against the live web on the fetch date its own extract states, and is this project's measurement
rather than any host's statement. The quoted conclusion about `accessim.org` and the quoted
commented-out markup are transcriptions of those agents' records.
