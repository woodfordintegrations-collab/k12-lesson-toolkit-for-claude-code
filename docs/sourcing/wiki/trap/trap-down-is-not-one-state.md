---
title: '"Down" is not one state'
type: trap
sources:
  - sources/host-open-middle.md
  - sources/host-engageny-nysed.md
  - sources/host-math-vision-project.md
  - sources/host-math-mistakes.md
  - sources/host-learning-commons-kg.md
  - sources/host-learnwithsap.md
  - sources/host-accessim-360.md
  - sources/host-eric.md
  - sources/verdict-twelve-host-table.md
updated: 2026-08-08
---

# "Down" is not one state

## Summary

**What the broken case looks like:** a source-table row reading `unreachable`, or a fetch log
line reading `HTTP 000`, and a verdict of `cite_only` or `do_not_use` written on the strength of
it. The row looks exactly like the row for a host that is genuinely gone. It renders identically
in the table, it passes every lint, and the licence text it wrote off is sitting on the live
server, one flag away.

This corpus contains the worked instance. The prior finding handed to the EngageNY verifier was,
verbatim, "HTTP 000, does not resolve". The report records that as **partially confirmed, with
the reason overturning the conclusion**: the 000 is real, and the site is not dead. The apex is
NXDOMAIN, `www` has an expired certificate, and over plain HTTP the host answers immediately and
301s into NYSED, where the licence statement is live.

Every failure signature measured in this corpus is listed below. Each one produces "it did not
work" at the level of description most fetch logs record, and each one has a different correct
next move.

| Signature as measured | Host it was measured on | What it actually is | Next move |
|---|---|---|---|
| HTTP 406 to a default UA, HTTP 200 to a browser UA | `openmiddle.com`, 100,227 bytes with browser UA | server or WAF user-agent filter | retry with a browser UA; note the block contradicts the host's own `robots.txt`, which allows `*` |
| HTTP 403 to WebFetch's default agent, HTTP 200 to browser-UA curl | `learnwithsap.org`, 305,636 bytes | Cloudflare-fronted UA block on one client | swap the client, not the conclusion |
| HTTP 403 with body "Enable JavaScript and cookies to continue", to curl with a browser UA and to WebFetch alike | `thecorestandards.org`, root and `/public-license/` | JS or cookie challenge on a live site | archive snapshot now, real browser session to close it properly |
| `curl: (6) Could not resolve host`, http_code 000 | `engageny.org` apex | NXDOMAIN on the apex only | try `www`; check DNS before concluding anything |
| `curl: (60) SSL certificate problem: certificate has expired`, http_code 000 | `www.engageny.org` | expired TLS certificate on a live redirector | `curl -k` or plain http, then follow the 301 chain |
| `SSLV3_ALERT_HANDSHAKE_FAILURE` on three independent TLS stacks, TCP 443 connects first | `mathematicsvisionproject.org` | host-specific edge TLS misconfiguration | plain `http://`; never cite the `https://` URL |
| HTTP 200 whose entire body is a PHP fatal error, byte-identical on every path probed | `mathmistakes.org`, 1,830 bytes | live server, dead application | Wayback; every citation points at a snapshot |
| `curl: (28) Connection timed out`, then `curl: (35) Recv failure`, http_code 000, while sibling paths fetch fine | `accessim.org`, two paths | intermittent server-side failure | retry; if it persists, record the path as never retrieved |
| HTTP 404 on a file whose parent record is live | `files.eric.ed.gov`, `EJ1454267` and `EJ1370844` | no such file; the ID-to-PDF pattern is not guaranteed | do not read it as a block or a dead host |
| HTTP 200 for every path including a deliberately bogus one | `accessim.org`, `achievethecore.org` | soft 404, a separate failure family | see [[trap-soft-404-status-proves-nothing]] |

The rule this page enforces is the retired-vocabulary rule: never write "the source is
unavailable". Write which one it is.

This page runs longer than a trap page in this wiki usually does, and the table above is why.
The failure being documented is precisely that these signatures are indistinguishable at the
level of description a fetch log records, so a page carrying only some of them reproduces the
confusion it exists to prevent. A reader who already knows which signature they are looking at
does not need this page at all.

## When to reach for it

Reach for this page the moment any fetch fails and you are about to record the outcome. The
recording is the decision. Once "unreachable" is in the source table, nobody re-probes it, and
the row is what the verdict gets written from.

Reach for it when you inherit a reachability finding from someone else. Two of the findings in
this corpus were inherited and wrong: "HTTP 000, does not resolve" for EngageNY, and an
"unreachable" classification for MVP whose TLS half was right and whose conclusion was not.

Reach for it before writing a licence claim as unverified. A live host behind a bot block still
holds the authoritative text. Recording it as unverifiable when a browser session would close it
is a false gap, and this corpus has one flagged: `thecorestandards.org` is recorded as a
closeable gap that was not escalated.

Do not reach for this page to decide what a host permits. Reachability and rights are different
axes, and a 200 says nothing about either existence or permission. See
[[trap-access-is-not-a-rights-fact]].

## How it works

### An HTTP 000 is your client's outcome, not the server's statement

`000` is what a client reports when it never got a status line. It covers DNS failure, TLS
failure, connection timeout and read failure, which are four different facts about four
different layers. The EngageNY probe table separates them, and separating them is what
overturned the conclusion:

| Probe | Result |
|---|---|
| `dig +short engageny.org A` | empty; apex does NOT resolve (NXDOMAIN) |
| `dig +short www.engageny.org A` | CNAME to `sedldbal.nysed.gov.` then 149.10.125.41, .40 |
| `curl https://engageny.org/` | `curl: (6) Could not resolve host`, http_code=000 |
| `curl https://www.engageny.org/` | `curl: (60) SSL certificate problem: certificate has expired`, http_code=000 |
| `curl -k https://www.engageny.org/` | **301** to `http://www.nysed.gov/curriculum-instruction/engageny` |
| `curl http://www.engageny.org/` | **301** to the same target |
| `curl -L http://www.engageny.org/` | **200**, 3 redirects, final `https://www.nysed.gov/standards-instruction/standards-resources-and-supports#engageny` |

The report's verdict, in its own emphasis: **not dead, not bot-blocked. It is a live redirector
with a broken cert.** Nameservers include `srv21.nysed.gov`, so NYSED still controls the domain.

### The control set is what separates your network from their host

MVP fails the TLS handshake on BoringSSL, LibreSSL 3.3.6 and OpenSSL 3.6.3 identically, and TCP
port 443 connects before the server alerts on the Client Hello. On its own that is ambiguous
between a broken host and a broken egress. The verifying agent ran a control set from the same
machine, the same egress and the same minute: `example.com` 200, `khanacademy.org` 200,
`openupresources.org` 301, `weebly.com` 200. The last one matters, because MVP's own headers
record `X-Host: blu49.sf2p.intern.weebly.net`. With the control set the conclusion is forced: not
egress filtering, not a bot block, not a dead site, but a host-specific edge TLS
misconfiguration.

Run a control set every time. It costs four requests and it is the difference between a finding
and a guess.

### A live server can serve a dead application, and it looks like nothing else

`mathmistakes.org` answers in 0.88 seconds with HTTP 200, no 403, no 406, and a clean TLS
handshake. The entire 1,830-byte body is a PHP fatal error, staged verbatim in part:

```
Fatal error: Uncaught ArgumentCountError: Too few arguments to function
WP_Widget::__construct(), 0 passed in /home/mathmist/public_html/wp-includes/
class-wp-widget-factory.php on line 62 and at least 2 expected in
/home/mathmist/public_html/wp-includes/class-wp-widget.php:163
```

The diagnosed cause is legible in the trace: an abandoned `advanced-tag-list` plugin registers a
widget whose constructor signature broke under PHP 8, and it throws on `widgets_init`, which
fires on every WordPress request before routing. Hence a total outage with no exceptions. RSS
and the REST API are down too, so there is no machine-readable escape hatch. The verifying agent
recorded that its brief's three categories had no slot for this and called it a fourth thing.

The consequence for the wiki is precise: **every licence claim about this host is Wayback
evidence, and zero licence text is obtainable from the live host.** A citation must point at a
snapshot, or a bare link lands the reader on a stack trace.

## In practice

### Recording the row

A reachability field with two values, live and dead, cannot hold any of this. The staged corpus
uses a third value, `partial`, for EngageNY and for MVP, and spells the reason out in prose
beside it. Copy that shape. Each row needs the client used, the exact error string or status, and
the working alternative if one was found.

Correct: "`www.engageny.org` https fails, `curl (60) certificate has expired`, http_code 000;
plain http 301s to nysed.gov and resolves 200 after 3 redirects. Live redirector, expired cert.
Fetched 2026-08-08."

Incorrect: "engageny.org: unreachable."

### The escalation ladder, in order of cost

1. Retry with a browser user agent. Closes the `openmiddle.com` 406 and the `learnwithsap.org`
   403 outright.
2. Try plain `http://`. Closes MVP entirely and closes the EngageNY certificate failure.
3. Try the other hostname. `www` versus apex is a real distinction and it was decisive twice
   here: EngageNY's apex is NXDOMAIN while `www` lives, and `corestandards.org/public-license/`
   genuinely 404s while `thecorestandards.org/public-license/` is 403 on a live site.
4. Go to Wayback. Mandatory for `mathmistakes.org`, and the only readable copy of the CCSS
   public license at the time of this corpus.
5. Escalate to a real browser session. The remaining closeable gap, unrun, is
   `thecorestandards.org`.

### Two archive failures that are not host failures

The archive has its own states, and they get attributed to the host if you are not careful.

- The Wayback CDX API returned 503 on four attempts and then 504 to the `mathmistakes.org`
  agent, which recorded it as an Internet Archive infrastructure problem on their end, noting
  that the availability API and individual snapshot replay both worked fine throughout. The
  consequence was a real limit on that finding: the agent could not enumerate the full capture
  history or pin the exact outage onset date.
- The CDX API timed out twice at 60 seconds for the EngageNY agent, which used the `available`
  endpoint instead and recorded that its sample is 5 hand-picked pages rather than an exhaustive
  crawl.

## Gotchas & constraints

**1. An archived page can be an archived block.** Probing `/web/2025/` and `/web/2026xxxx/` for
`mathmistakes.org` returned a 46,860-byte page that is not a capture. It is HTTP 403 with
`<title>Visitor anti-robot validation</title>`, replayed from snapshot `20260104191043`: an
anti-bot challenge the host served to the Internet Archive crawler and which got archived as
content. The report's own line is that reporting it as "the site was blocked in 2025" would have
been wrong in two ways at once. Some 2026 snapshots of that host are WAF pages; `20260220051333`
is clean, at 257,612 bytes with zero occurrences of "Fatal error".

**2. Archive evidence carries its own date, and the page must say so.** The CCSS public license
text in this corpus comes from a snapshot dated 2025-12-21, and the licence's own text reserves
the right to release under different terms or to stop distributing at any time. A Wayback-sourced
licence claim is a claim about that snapshot date, not about today.

**3. Do not carry a path count you did not verify.** The `mathmistakes.org` extract records that
its underlying report's prose says 13 probed paths while its own reproduced table lists 14 rows,
and it explicitly declines to pick a winner. Where a count is needed, this wiki writes "every
path probed".

**4. A bot block can contradict the host's own published crawl policy, and that is worth
recording.** `openmiddle.com` serves a `robots.txt` that allows `*` with `Crawl-delay: 2` and
disallows only Baiduspider, Sosospider and one `wp-content` path, while the server 406s
non-browser agents. The verifying agent also recorded, and verified with `xxd`, that the served
`robots.txt` literally begins `ser-agent: *` with the leading `U` absent from the raw bytes, so
its first directive group is malformed. Neither fact changes the licence. Both change what an
automated link checker will report.

**5. Failing over to a working client does not license bypassing an access control.** These
moves are user-agent and protocol choices against openly served pages. Nothing here supports
defeating a login, a paywall or a technical access control, and at least one host in this corpus
bars automated tools that circumvent them.

**6. Two hosts in this corpus were re-classified by the probe and their licence findings
changed with them.** MVP went from unreachable to fully readable over plain http, where its
Geometry course page carries a clean CC BY 4.0 grant. EngageNY went from "does not resolve" to a
live successor page at NYSED carrying the CC BY-NC-SA statement. The cost of the collapsed
category, in this corpus, was two usable sources.

## Related

- [[source-engageny-nysed]] is the worked case: an inherited "HTTP 000, does not resolve" whose
  reason overturned its conclusion.
- [[source-math-vision-project]] is the TLS handshake failure with a clean same-minute control
  set, and the host whose `https://` URL must never be cited.
- [[source-math-mistakes]] is the live server running a dead application, where all licence
  evidence is necessarily from the archive.
- [[source-open-middle]] is the user-agent block that contradicts the host's own `robots.txt`.
- [[source-corestandards-nga-ccsso]] is the JS-challenge 403 on a live site, and the one gap in
  this corpus that a real browser session could still close.
- [[source-achieve-the-core-sap]] covers the SAP family, including the second host in this corpus
  whose default-agent 403 is a client problem rather than a host problem.
- [[source-eric]] is where a 404 on a full-text PDF is recorded as an absent file rather than as a
  block, because its parent record is live.
- [[source-accessim-360]] carries the intermittent server-side timeouts that are neither blocks
  nor soft 404s.
- [[trap-soft-404-status-proves-nothing]] is the opposite failure: a status code that reports
  success for a page that does not exist.
- [[trap-access-is-not-a-rights-fact]] is why none of these signatures, resolved either way,
  tells you what you may do with what you find.
- [[trap-compressed-body-grepped-as-text]] is the extraction failure that most often follows a
  successful archive fetch.
- [[license-withdrawn-grants]] is where a dated, archive-sourced licence claim goes, and why
  every such claim carries its snapshot date.

## Composes with

- [[practice-build-a-source-table]] owns the reachability column this page is a decision table
  for; the escalation ladder above is what that procedure runs before a row may read anything
  other than live.

## References

Staged extracts in this wiki, all staged 2026-08-08:

- `sources/host-engageny-nysed.md`, primary. §1 the seven-probe reachability table, the inherited
  finding it overturns, the root cause, and the `partial` classification; §5 the SharePoint
  archive bouncing an anonymous non-JS client to Microsoft SSO, recorded as ambiguous rather than
  gated; §8 the CDX timeouts and the 5-page sampling limit.
- `sources/host-math-vision-project.md`, primary. §1 the three-stack handshake failure, the
  same-minute control set, the live HTTP headers including the Weebly `X-Host`, and the
  instruction never to cite an `https://` MVP URL.
- `sources/host-math-mistakes.md`, primary. §1 the live-server-dead-application finding, the
  verbatim fatal error, the diagnosed root cause and the path-probe table with its recorded
  prose-versus-table count discrepancy; §2 the archived WAF challenge, the CDX 503 and 504
  failures, and the clean snapshot's byte count.
- `sources/host-open-middle.md`, primary. §1 the 406-versus-200 measurement, the `robots.txt`
  contradiction and the malformed `ser-agent` first line verified via `xxd`.
- `sources/host-learnwithsap.md`, primary. §2 the WebFetch 403 against browser-UA curl 200 at
  305,636 bytes, and the note that the sibling host did not need the workaround.
- `sources/host-learning-commons-kg.md`, primary. §9 the four-probe table for
  `thecorestandards.org`, the JS-challenge body, the distinction from the genuinely 404ing bare
  host, and the 2025-12-21 Wayback snapshot the licence text was recovered from.
- `sources/host-accessim-360.md`, primary. §1 the two intermittent HTTP 000 failures recorded as
  server-side rather than as blocks.
- `sources/host-eric.md`, primary. §4.8 the two 404s on `files.eric.ed.gov`, recorded explicitly
  as neither a block nor a dead site.
- `sources/verdict-twelve-host-table.md`, reference. This project's own adjudication, whose
  Reachable column keeps each of these states distinct rather than collapsing them, and which
  flags the `thecorestandards.org` block as a closeable gap that was not escalated.

Every probe result, error string, byte count and timing above was measured by an agent of this
project against the live web or against the Internet Archive on the fetch date its own extract
states. All of it is this project's own measurement. None of it is a statement by any host.
