# Website contribution and atomic integration

The contributor command and Windows automation use one pinned production updater
and validator. Preparation success is a proposal; strict committed-tree validity is
the merge requirement. A candidate-controlled green job or downloaded PR artifact
cannot authorize integration.

## Normal website flow

1. A contributor opens a PR with descriptive source edits.
2. **Prepare content for review**, from protected upstream main, captures current
   main and the source head once. It obtains the pinned public kit and prepares exact
   Git objects in isolation without candidate scripts, hooks, filters or artifacts.
3. Already complete PRs need no replacement. If generated changes are needed, the
   same job independently validates the full successor and opens a maintainer-owned
   `codex/content-pr-*` PR. Its body identifies and credits the source PR.
4. If GitHub requests **Approve workflows to run** on the bot-created PR, a maintainer
   clicks it. The trusted required workflow must then pass on that committed tree.
5. Ixl-irl reviews the complete diff and uses the website merge queue. The queue
   validates the exact result against current main and squash-merges one PR at a time.

No checkout, manual kit installation, hash entry or routine protection bypass is
needed. Preparation never approves, merges or advances main. It creates no persistent
credential. Its short-lived GITHUB_TOKEN can create review branches/PRs but cannot
bypass main rules. Automation does not approve its own PRs.

Failed preparation retains file/entry diagnostics and `proposal.diff`. A changed
source head/main rejects the run; restart **Prepare content for review** on main with
only the PR number to explicitly capture new inputs. A newer main is merged as data,
preserving unrelated changes; conflicts require source correction. Repeating identical
inputs produces the same proposed files and review commit. Existing differing branches
are preserved. Old prepared PRs identify their captured source; close superseded ones
after reviewing their replacement, rather than treating them as the latest source.

Automatic preparation refuses changes to `.github/`, `tools/`, `ph-content.py` or
`ph-content.cmd` when it would create an upstream replacement branch. Those changes
stay in the original PR for explicit maintainer review. This prevents promoting
fork-controlled automation into a repository context with write-token access.

## Trusted final gate and ancestry

An **organization required-workflow rule** selects
`.github/workflows/content.yml` at an externally reviewed immutable commit SHA.
Its literal public kit URL and archive/manifest hashes are outside candidate control.
A same-named Actions status is insufficient. The rule has no bypass actors and does
not exempt branch creation. The workflow handles both `pull_request` and `merge_group`.

The gate captures approved main, the PR head and (for queue runs) the queue head,
fetches those exact objects, and fences them again after validation. A queue tree
must equal the Git merge of captured main and that single PR. Repository files and
modes, all published identity history, conversion policy and isolated selected payloads
are independently checked with the production reader. No updater or repair runs in
the final gate; a successful prepared proposal cannot make an inconsistent tree pass.

For this website route, identity is the **validated complete Git tree plus exact
expected base**, not GitHub's final squash commit metadata. The gate derives a local
single-parent validation witness of that tree to reuse the existing exact publisher.
The witness is never pushed. The queue publishes a single-parent squash commit with
that complete tree. Its temporary two-parent merge-group object is not published
ancestry. Queue admission binds these checks to current main; movement requires a new
group/check. Source and generated index land together, never in a source-first repair.

The legacy local exact-commit publisher still requires its exact ordinary parent
and non-force advancement. Neither path indexes the enclosing commit or descriptor
hash. Application PR #527 must remain unmerged; it is not a content merge prerequisite.
Compatible application rollout and workshop freeze remain separate decisions.

## Enforcement setup and safe transition

These files describe the required configuration; they do not apply settings themselves.
Before replacing the old `main-owner-publication` update restriction:

- Publish/verify the new immutable Windows kit. Put the reviewed workflow in a public
  immutable Git commit and record that exact SHA outside the candidate.
- At organization level, target only repository ID **1428699425**
  (`Tethys-Games/parse-hero-content`) and `refs/heads/main`. Require that workflow,
  pinned by `sha` (not a moving branch), with no bypass actors.
- At repository level, require merge queue: **Squash**, build concurrency **1**,
  minimum and maximum merge group size **1**, all entries green, check timeout
  **15 minutes**. The queue rule must also have no bypass actors.
- Retain PR review, CODEOWNERS, stale-review dismissal, last-push approval, resolved
  conversations, linear history, no force pushes/deletions and admin enforcement.
  The `content` status can remain a useful visible check, but cannot replace the
  externally pinned required workflow.
- Enable GitHub Actions and allow its token to create pull requests. Keep the default
  token read-only, fork tokens read-only, and fork secrets disabled. The protected
  preparation job alone requests contents/PR write. If organization policy filters
  `pull_request_target`, explicitly permit this protected workflow for this repository.
- Verify the replacement rules are active and the exact candidate passes. Only then
  retire the old owner-only update restriction/PR bypass that forced website users to
  bypass protection. Do not add an owner or bot bypass to the replacement gate/queue.

The first migration PR may need one new event/rerun after required-workflow activation.
Keep it blocked until the pinned gate has actually run. Do not merge a candidate whose
checks only passed under its own editable workflow. Once enabled, review website
behavior on a real fork and a generated PR; preserve exact run/head/tree identities.
The merge queue itself is exercised only by a separately authorized content merge.

Protect workflows, all tools/pins, entry point, this procedure, `.gitattributes`,
`LICENSE`, `NOTICE.md`, `docs/tool-licenses/` and CODEOWNERS itself. Public helper
changes originate in the maintained application tooling; kit production and publisher
changes require trusted application review. When updating a gate/kit, validate and
publish its new immutable source first, then deliberately change the external workflow
pin. A candidate cannot select its own authority.

## Validator distribution and terms

The versioned GitHub Release and exact archive/manifest hashes are recorded in
`tools/validator.json`. First-party binaries use Parse Hero Content Validator License
1.0; helpers, workflows and authored content use MIT. Contributors retain copyright
and contribute under MIT without a separate agreement. Preserve notices. Application
implementation, other assets and branding remain outside the content grant.

For a new kit, confirm release immutability, upload and verify draft assets, then
publish and verify anonymous downloads. Never replace pinned bytes or use a moving
`latest` URL. Record the public release tag target separately from the private
application producer. Tool publication does not advance content main or deploy the
application. Historical schema1 commits remain provenance, not runnable rollback for
descriptor2 readers. Compatible correction/restoration evidence remains at its producer.
