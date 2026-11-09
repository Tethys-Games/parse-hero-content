# Trusted contribution and compatible cutover

The original authored PR and exact merge-queue candidate validate read-only through
one externally pinned managed semantic preparer. This guide defines compatibility,
distribution and rollback. The selected content PR records the transition's review.
Completed publication,
external-pin, protected-integration and public-acquisition receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Neither these generated docs nor candidate YAML establish what is currently active.

## Local edition candidate and public compiler38 compatibility

The local edition candidate requires capability39, semantic contract39, package23,
module identity algorithm4 and one immutable `edition = workshop_1` per authored module.
Class18 and ability8 retire the separate combat-default assertion. Workspace5 named plays,
catalog2, mandatory capture/archive4 and encounter17 retain their contracts. Effect1
provides reusable typed periodic, rich mark and modifier definitions. NPC5,
behavior5 and map5 retain their meanings. Transport compatibility remains application-owned; a compiler revision does not select a wire revision. The application Authoring
Manual owns the exact language; this guide owns coordinated distribution.

The five-module corpus combines training's player and encounter owners, keeps context
and `mobile_scout` separate, and adds `basic_classes` and `training_dummy` owners. The six
catalog plays are training, context, context-shared, outpost, training-dummy-melee and
training-dummy-ranged. All nine workspace plays are validated, including the three
local quick fixtures; they do not add public catalog entries. `tools/validator.json`
retains the public compiler38 validator, while the organization rule independently
selects its authoritative workflow. This local candidate needs the application's compiler39
reader; the public helper/gate cannot qualify its newer grammar. An older externally selected validator can reject
newer content until the coordinated pin change. Keep that result visible; candidate
YAML and a local passing validator cannot replace the gate.

Prepare immutable candidate validator bytes, archive/manifest SHA-256 pins, exact content
and application heads, the trusted-workflow YAML and its future immutable commit pin.
Review these together. Execute the compatible cutover through immutable publication,
the independently authorized workflow-pin update, original-source and queue verification
and normal protected content integration. Eligible review remains required. Application
integration/deployment and workshop freeze remain separate. Existing releases remain
immutable. The cutover PR identifies the exact reviewed payloads and their actual disposition;
these preparation instructions do not establish that an external change occurred.

The retained compiler38 corpus had these complete closure counts and cold browser plans. The source
record count includes every private definition, module manifest and the generated
selection descriptor; runtime compiler auxiliaries are separate. The browser request
count includes possible metadata CORS preflights. These are measured corpus facts,
not extra admission limits. Preserve them as compiler38 producer evidence; the local edition
candidate's current shared check supplies its own plan and byte results.

| Catalog selection | Canonical source records | Cold browser requests | Original source bytes | Mandatory archive bytes |
| --- | ---: | ---: | ---: | ---: |
| training | 12 | 23 | 7,638 | 140,323 |
| context | 27 | 40 | 18,223 | 151,912 |
| context-shared / outpost (each) | 32 | 49 | 20,702 | 154,846 |
| training-dummy-melee / training-dummy-ranged (each) | 17 | 30 | 8,259 | 141,317 |

The largest closure retains 28 definitions, three module manifests and one descriptor;
the Basic Classes closures retain 14 definitions, two manifests and one descriptor.
Private possession, return and quick-fixture definitions remain present even when
inactive. Canonical bytes remain bounded to 384 KiB and
exchange to 512 KiB; 256 maximum-sized files are not promised. Public acquisition admits
320 HTTP slots and a complete archive of at most 896 KiB, with 256 body records plus
the catalog and a 128 KiB header reservation. Mandatory inventory cannot be dropped.
The original 45-second operation, 12-second request, two-body concurrency and 8 MiB I/O
bounds remain. Byte, acquisition, inventory and exchange bounds apply independently. The seven
current definition kinds are class, ability, effect, NPC, behavior, encounter and map;
future asset kinds require their own contracts.

## Public compiler38 transition's immediate compiler34 reverse set

The completed compiler38 transition preserves the complete November7 compiler34 set as its
immediate rollback. Its active compiler38 pins and full receipts remain in the application
workshop runbook. That complete active compiler38 set is the prospective edition transition's
immediate reverse set. The table below retains compiler38's historical predecessor;
no edition-compatible publication, workflow activation or integration is selected here.

| Boundary | Compatible predecessor |
| --- | --- |
| Content main / tree | `d55efac86ac5da7b48d2faa02a0c03d79fe2f9af` / `a8a42301567e9f082b0ad643d0d0501cffc896da` |
| Validator producer / tag | `656aa24126d577d9beaf2a796d7b3f51dc517ac2` / `content-validator-656aa24126d5` |
| ZIP bytes / SHA256 | 37,990,618 / `99f43f23322dd5f0ecae27c2e659bbded90a44fc78249b2112b6963a51ad3d43` |
| Separate manifest SHA256 | `be88047d74a5a2e3785b2a72a199a372da809ca58026b36f3f28ac86e94f43dd` |
| Producer inventory SHA256 | `f02bef6d5067a05bb2e49a88dd353abdae7cadcd59e9b8284f1f859b75e2b1f0` |
| Workflow SHA / ref | `c513cfb193600daf966809aa46dcb9d50a830212` / `refs/heads/codex/explicit-actor-targets` |

The workflow belongs to repository1428699425 at `.github/workflows/content.yml`
under organization ruleset26232258. Its pre-squash workflow commit differs from
the integrated content ancestor; rollback content uses `d55efac8`, not `c513cfb`.
Restore the complete compatible set through normal protected forward commits and
an explicitly selected external workflow update. Older compiler33, compiler32 and compiler29
sets remain historical in the application workshop record. Existing original-source
and real-fork proofs retain their actual producers; repeat a trust-boundary proof
only when that boundary changes. An old content pin cannot serve an incompatible authority.

## Local authoring and validator promotion

Ordinary source edits reuse the compatible validator; public helper downloads are cached
by their exact archive hash. In the application checkout, `python tools/workshop.py check`
incrementally builds the shared source validator and checks the configured content repository
read-only. `--no-build` reuses that build. No ZIP or release is needed for this edit/check loop.

Promote a new kit when parser/compiler semantics, schemas or supported capacity change.
The maintained application `tools/content_validator_promote.py` composes selected tests,
exact-producer packaging, immutable publication and anonymous verification. Its package receipt
feeds `content_contributor_files.py`, which generates validator pins, contributor guides
and the workflow together. A documentation-only template change reuses the exact compatible
package receipt; it does not relabel or republish the validator's producer. Regenerate and
review the contributor files, then finalize the content commit before preparing the external
workflow replacement. Keep the final content SHA in that task-local payload and the cutover PR, rather
than embedding the commit's own hash or an activation assertion in its generated docs.
Record completed activation in the application runbook after the event. This avoids changing
the content tree merely to update its own publication status.
The promotion `pins` command verifies the committed candidate and prepares an exact expected
workflow-pin replacement plus compatible rollback. Applying that replacement and protected
integration remain explicit cutover actions; candidate code never chooses its authoritative validator.
Retain historical kits and rollback pins. Do not copy application implementation or compiled ZIPs
into this repository. Publication metadata is exported from the managed owners and checked
against the maintained package contract; generated compatibility guidance uses that same metadata.
This does not change the authored identity or transport contract.

## Trusted gate

An organization required-workflow rule selects `.github/workflows/content.yml` at an
externally reviewed immutable SHA. The workflow contains literal validator URL,
archive length/SHA-256 and manifest SHA-256 outside candidate control. It runs for
`pull_request` and `merge_group` with read-only contents/PR permissions and no candidate
checkout. Exact Git objects are data. Candidate scripts, hooks, filters, workflows,
validator overrides and downloaded candidate artifacts never execute with credentials.

The gate captures main and the source head, validates the original source head, and
fences both after validation. A queue run also checks that the exact queue tree equals
the Git merge of captured main and its single PR, then validates that queue tree.
A stale head or conflict rejects. No complete release-history scan, generated-index
equality, namespace allocation, source pin rewrite or prepared branch is involved.
A local Git merge witness is data for comparing queue trees and is never pushed.

The packaged managed check validates every declared module and named play, then applies
the same public acquisition plan as M4 to each catalog selection's exact original
inventory. M4 captures only the selected play's closure. The plan includes unowned selected-subtree
metadata, nonrecursive ancestors, safe one-level module directories, metadata byte/
entry bounds and cold browser HTTP/reserved-I/O limits. Metadata requests reserve
the browser's possible CORS preflight. Cache warmth and Git-object deduplication
cannot admit an otherwise invalid cold plan. Complete selected-tree inventory and child
module boundaries are mandatory cache evidence; missing private source or truncated
metadata rejects replay. Required evidence is reserved with raw bodies under the archive
bound and cannot be dropped for size. Large unselected subtrees stay outside
recursive traversal; local M5 retains its ordinary folder flexibility. Plan reports
are conservative bounds, not observed transfers or a promise of provider availability.

Keep the required workflow pinned independently of candidate YAML. Preserve current
PR review, CODEOWNERS, stale-review dismissal, last-push approval, resolved discussions,
linear history, no force pushes/deletions and admin enforcement. Preserve the one-PR
squash queue, concurrency one, group size one and existing 15-minute check timeout.
Repository ID is 1428699425, target `Tethys-Games/parse-hero-content`, `refs/heads/main`.
No bot/owner bypass or elevated fork token is needed. The privileged
`prepare-content.yml` workflow and its write-token helper are retired; do not create replacement PRs.
Trials [PR2](https://github.com/Tethys-Games/parse-hero-content/pull/2) and
[PR3](https://github.com/Tethys-Games/parse-hero-content/pull/3) are closed as superseded,
without merging. Their evidence commits `80ac9715477d6a5140e5756df26d7337c424f2ef` and
`27cc7193492395521285c37ae2abae73866d6e77` and branch histories are retained.

## Availability and future cutovers

The supported local workshop uses the source3 trust and availability scope below.
Match application, validator and authored-content compatibility before making an assignment;
an incompatible reader rejects the content. The cutover PR and application workshop runbook identify
review and completed activation respectively. Application integration/deployment remains
separately selected. Documentation changes use an ordinary protected PR and the existing
one-PR squash queue. Eligible owner/CODEOWNERS review is required; bot checks do not replace it.

For a future incompatible cutover, first prepare the exact compatible content, application,
validator and enforcement set. Hold new assignments while publishing and anonymously
verifying immutable validator bytes, advancing the external workflow pin under its authority,
and exercising actual original-source/queue routing. Carry unchanged fork evidence at its
actual producer. Integrate/deploy only the selected
compatible products, then verify actual public acquisition and independent authority
preparation before resuming assignments. Never publish the superseded uncorrected
`content-validator-7f9181cae504` candidate as the R1 fix, overwrite an immutable release,
or treat candidate YAML as activated enforcement.

M4 uses trusted HTTPS Git-object metadata: exact commit to selected trees to expected
Git SHA-1 blob ID and length, then raw-byte verification. Semantic revisions and
canonical hashes remain SHA-256. A post-download SHA-256 is not a predeclared raw
commitment. Selected-module subtree requests, coalescing and bounded retained caches
reduce repeat traffic. Anonymous REST remains limited to 60 requests/hour/IP. The historical
compiler29 public-origin witness observed 10 REST GETs plus 26 raw GETs (20,929 authored
body bytes), and its shipping browser observed 10 CORS preflights. That witness's cold
browser plan reserved 46 HTTP slots; conservative reserved-I/O budgets are separate from real transfer
and cache-I/O counters. Later freshness checks are additional. This finite local success
does not establish supported shared-NAT cold-start availability. Treat provider rate-limit
failures separately from deterministic public-layout rejection; a valid plan cannot
guarantee provider availability. The selected scope is the local workshop.
Do not add client credentials, a proxy/index service or an unchecked fallback.

Rollback means restoring a reviewed compatible application/content/validator/workflow
set through ordinary forward commits and explicit external pin updates. Existing exact
pins and compatible known-good cache entries remain valid for their original contract.
Do not rewrite history, reuse a new revision label for old bytes, downgrade receiving
checks, or silently assign an old release to an incompatible authority.

## Distribution and terms

Protect workflows, tools/pins, entry points, this guide, `.gitattributes`, licenses,
notices and CODEOWNERS itself. Helper changes originate in reviewed application tooling.
The engine-free validator packages the shared semantic core and its pinned runtime;
first-party binaries retain Parse Hero Content Validator License 1.0. Helpers,
workflows, authored definitions, generated content and documentation retain MIT.
Preserve all runtime and Clipper2 notices. Application implementation, other assets
and branding remain outside the corpus grant. Identity derivation changes no license.
