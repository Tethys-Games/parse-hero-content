# Trusted contribution and compatible cutover

The original authored PR and exact merge-queue candidate validate read-only through
one externally pinned managed semantic preparer. This guide defines compatibility,
distribution and rollback. [PR7](https://github.com/Tethys-Games/parse-hero-content/pull/7)
records the compiler32 transition's review and activation status. Completed publication,
external-pin, protected-integration and public-acquisition receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Neither these generated docs nor candidate YAML establish what is currently active.

## Compiler32 compatibility

The selected implementation requires capability32, semantic contract31, package20, module identity algorithm2,
workspace5 named plays, catalog2 and mandatory capture/archive3. Class14, ability4
and encounter14 version the shared program and normalized binding contract. NPC4,
behavior4, map4 and protocol33 retain their meanings. The application Authoring
Manual owns the exact language; this guide owns coordinated distribution.

The corpus combines training's former player and encounter owners, keeps context
and mobile-scout separate, and preserves all four play roles. `tools/validator.json`
identifies this revision's compatible validator, while the organization rule independently
selects the authoritative workflow. An older externally selected validator can reject
newer content until the coordinated pin change. Keep that result visible; candidate
YAML and a local passing validator cannot replace the gate.

Prepare immutable candidate validator bytes, archive/manifest SHA-256 pins, exact content
and application heads, the trusted-workflow YAML and its future immutable commit pin.
Review these together. Execute the compatible cutover through immutable publication,
the independently authorized workflow-pin update, original-PR/fork/queue verification
and normal protected content integration. Eligible review remains required. Application
integration/deployment and workshop freeze remain separate. Existing releases remain
immutable. PR7 identifies the exact reviewed payloads and their actual disposition;
these preparation instructions do not establish that an external change occurred.

The complete outpost and context-shared closures now retain exactly 32 canonical source
records: 28 definitions, three module manifests and the generated selection descriptor.
The supported 256-record ceiling leaves 224 records of count headroom. Training
retains 12 records and context retains 27. Private possession and return definitions
remain in that proof even when inactive. Canonical bytes remain bounded to 384 KiB and
exchange to 512 KiB; 256 maximum-sized files are not promised. Public acquisition admits
320 HTTP slots and a complete archive of at most 896 KiB, with 256 body records plus
the catalog and a 128 KiB header reservation. Mandatory inventory cannot be dropped.
The original 45-second operation, 12-second request, two-body concurrency and 8 MiB I/O
bounds remain. Byte, acquisition, inventory and exchange bounds apply independently. The six
current definition kinds are admitted; future asset kinds require their own contracts.

## Retained compiler29 baseline and rollback

The October31 cutover integrated authored content at
`36d51d27880df2dbc9482f28ca40e5f43ac10988` (tree
`6082355e37c5d4cf7770a7f0aaba4bd3534e94c5`) through
[PR4](https://github.com/Tethys-Games/parse-hero-content/pull/4) and its exact
[merge-group receipt](https://github.com/Tethys-Games/parse-hero-content/actions/runs/41250662521).
Its immutable validator is `content-validator-78db40ac5176`. That historical workflow
selection used rule26232258, SHA `f9f54422829b2e4ef9f53d94356a513923ce32c8`
and `refs/heads/codex/automatic-module-revisions`. Preserve those identities in the
rollback payload; this revision's `tools/validator.json` selects the compiler32 kit.

The retained rollback content commit is `1237af57596d9f3f295045aef201d01c359ac96f`
(tree `f5d6e5d50e1199b70accf2996048f35d5038e0d8`). The prepared rollback retains its
original entry points, compiler29 archive/manifest pins and trusted-workflow selection
byte-for-byte. The original-source and real fork positive/negative/restoration proofs
remain at [PR5](https://github.com/Tethys-Games/parse-hero-content/pull/5), closed unmerged;
PR4 and application PR527 retain the historical public-origin native/browser and
independent authority/receiving products and normal-release receipts.

If rollback is selected, restore that compatible set through reviewed forward commits
and explicit external pin updates. Keep capability32 local products on a compatible
known-good selection until compatible assignments resume; never silently pair an old
content pin with an incompatible authority.

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
workflow replacement. Keep the final content SHA in that task-local payload and PR7, rather
than embedding the commit's own hash or an activation assertion in its generated docs.
Record completed activation in the application runbook after the event. This avoids changing
the content tree merely to update its own publication status.
The promotion `pins` command verifies the committed candidate and prepares an exact expected
workflow-pin replacement plus compatible rollback. Applying that replacement and protected
integration remain explicit cutover actions; candidate code never chooses its authoritative validator.
Retain historical kits and rollback pins. Do not copy application implementation or compiled ZIPs
into this repository. Capability32 changes the runtime compiler auxiliary; semantic31 module R/H
and canonical bytes remain stable for unchanged source/dependencies.

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
an incompatible reader rejects the content. PR7 and the application workshop runbook identify
review and completed activation respectively. Application integration/deployment remains
separately selected. Documentation changes use an ordinary protected PR and the existing
one-PR squash queue. Eligible owner/CODEOWNERS review is required; bot checks do not replace it.

For a future incompatible cutover, first prepare the exact compatible content, application,
validator and enforcement set. Hold new assignments while publishing and anonymously
verifying immutable validator bytes, advancing the external workflow pin under its authority,
and exercising original-source/fork/queue routing. Integrate/deploy only the selected
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
