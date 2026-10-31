# Trusted contribution and compatible cutover

The original authored PR and exact merge-queue candidate validate read-only through
one pinned managed semantic preparer. The existing public corpus, validator release
and protected workflow are live. This candidate replaces their generated-identity
and prepared-replacement-PR requirement; it does not publish or enable itself.

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

Keep the required workflow pinned independently of candidate YAML. Preserve current
PR review, CODEOWNERS, stale-review dismissal, last-push approval, resolved discussions,
linear history, no force pushes/deletions and admin enforcement. Preserve the one-PR
squash queue, concurrency one, group size one and existing 15-minute check timeout.
Repository ID is 1428699425, target `Tethys-Games/parse-hero-content`, `refs/heads/main`.
No bot/owner bypass or elevated fork token is needed. Retire the privileged
`prepare-content.yml` workflow and its write-token helper; do not create replacement PRs.
Leave trial PRs #2 and #3 intact and unmerged under this assignment.

## Concrete rollout sequence

Prepare and review these exact candidates first: application/compiler29/protocol33,
authored catalog1/workspace4/source3 content migration, self-contained Windows
validator package with producer/file hashes and notices, and trusted workflow with
that package's immutable release URL/hash/length. The candidate application source
record contains their exact producers and local evidence. No moving `latest` pin.

Under separate publication/settings authority:

1. Publish and anonymously verify the immutable validator archive at its recorded
   release tag. Confirm exact archive and manifest hashes; never replace existing bytes.
2. Advance the externally enforced required-workflow SHA to the reviewed read-only
   workflow, preserving all protections. Exercise real fork/original-PR and exact
   merge-group routing. A local simulated event does not prove public enforcement.
3. Advance compatible authored content and application artifacts in a coordinated
   cutover. Old compiler28/protocol32 products reject this content/protocol. An assigned
   authority must prepare the selected exact pin or fail; a client may visibly choose
   a complete compatible known-good/M3 fallback. Do not relabel historical bytes.
4. Verify the actual published heads, installed workflow pin and deployed products
   independently. Application PR #527 and content candidates remain unmerged until
   integration is selected; deployment and workshop freeze remain separate decisions.

M4 uses trusted HTTPS Git-object metadata: exact commit to selected trees to expected
Git SHA-1 blob ID and length, then raw-byte verification. Semantic revisions and
canonical hashes remain SHA-256. A post-download SHA-256 is not a predeclared raw
commitment. Selected-module subtree requests, coalescing and bounded retained caches
reduce repeat traffic. Anonymous REST remains limited to 60 requests/hour/IP. Cold
outpost is budgeted at 10 REST plus 26 raw requests before later freshness checks;
shared-NAT cold-start availability and this trust boundary require an explicit rollout
decision. A single-client success cannot establish supported shared-NAT availability.
Do not add client credentials, a proxy/index service or an unchecked fallback.

Rollback means restoring a reviewed compatible application/content/validator/workflow
set through ordinary forward commits and explicit external pin updates. Existing exact
pins and compatible known-good cache entries remain valid for their original contract.
Do not rewrite history, reuse a new revision label for old bytes, downgrade receiving
checks, or silently assign an old release to a compiler29 authority.

## Distribution and terms

Protect workflows, tools/pins, entry points, this guide, `.gitattributes`, licenses,
notices and CODEOWNERS itself. Helper changes originate in reviewed application tooling.
The engine-free validator packages the shared semantic core and its pinned runtime;
first-party binaries retain Parse Hero Content Validator License 1.0. Helpers,
workflows, authored definitions, generated content and documentation retain MIT.
Preserve all runtime and Clipper2 notices. Application implementation, other assets
and branding remain outside the corpus grant. Identity derivation changes no license.
