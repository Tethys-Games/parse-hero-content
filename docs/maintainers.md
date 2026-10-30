# Maintainer preparation and atomic integration

The contributor command and read-only Windows PR job share the pinned production
updater/validator. Preparation success and strict committed-tree validity are distinct.
Neither a PR-controlled green check nor a downloaded PR artifact authorizes publication.

## Protected web/fork preparation

After reviewing a source PR, obtain its full head SHA and current upstream main SHA.
Dispatch `prepare-content.yml` on upstream **main** with those exact inputs and the PR
number. The proposed `content-preparation` environment must restrict dispatch to trusted
maintainers/reviewers. The action uses its protected literal kit pin, captures/verifies
the approved origin and both refs, reads exact Git objects in a fresh bare repository,
and runs no candidate scripts, hooks, filters or actions. It downloads no PR artifact.

The shared operation validates staged changes, then the maintainer path independently
checks a full Git successor and isolated release payload. Its single parent is the
captured main, and modes and all reviewed metadata are retained. The action rechecks
PR/main before and after its non-force review-branch push. Stale inputs fail explicitly;
any branch created during a late race is marked stale and cannot integrate. It does
not advance main or grant approval. If a fork lacks captured main ancestry, update
that source branch first so unrelated main changes cannot be silently lost.

Open/review the generated `codex/content-pr-*` branch and its exact commit. Link the
source PR and credit its author. Fork writes are unnecessary. No automatic merge,
retarget, force push or source-first repair job is part of preparation.

## Final exact-candidate gate

The maintained publication path must select its validator outside the candidate and
independently run `ph-content check --base <expected-main> --tree <candidate>` plus the
existing exact-candidate publication preparation. Require strict success for the
actual candidate, complete history uniqueness, safe conversion policy, and the exact
ordinary single parent. Compare actual main to that expected parent again at the
separately authorized non-force advancement. Publish the complete authored tree and
matching index in one commit. A normal two-parent merge does not satisfy this policy.
Never promote a generated proposal solely because its preparation passed.

## Proposed protection; not yet enforced by these files

Require CODEOWNERS approval for workflows, `ph-content.py`, `ph-content.cmd`,
`tools/validator.json`, this procedure, `.gitattributes`, `LICENSE`, `NOTICE.md`, `docs/tool-licenses/`
and `.github/CODEOWNERS` itself.
The publisher and application-owned kit producer require trusted application review.
Protect main from direct contributor writes, force pushes and deletions. Require the
independent exact-candidate gate from a trusted workflow/actor; a same-named PR job is
not sufficient. Restrict the preparation environment and workflow changes to maintainers.
The preparation token may create review branches, but it must not bypass main rules.

## Selected validator distribution and terms

Publish the measured Windows kit as a versioned GitHub Release in
`Tethys-Games/parse-hero-content`, at the exact URL in `tools/validator.json`.
The first-party binaries use Parse Hero Content Validator License 1.0; public helper
scripts/workflows and the authored definitions use MIT. See [the license scopes](../NOTICE.md).
Contributors retain copyright and submit under those same MIT terms. Preserve copyright
and permission notices in copied or generated content distributions; application
implementation, non-corpus assets and branding remain outside the content grant.

The first Windows kit is publicly available as an immutable release. For future
versions, confirm GitHub release immutability before publishing. Prepare a draft with the archive, `validator-kit.json`,
archive SHA-256, producer identity and license texts; verify all assets before
publishing. Record the exact existing content commit used as the release tag target
separately from the private application producer named in the kit. Creating a tool
release must not advance content main or imply compatible application/content rollout.
The public release tag is not the private application commit. A changed archive
requires a new version and updated archive/manifest pins; never replace pinned bytes
or use a moving `latest` URL. Candidate metadata cannot establish publication: require
the public release to report immutable status and verify anonymous download hashes.
Release immutability does not establish the separate contributor protections above.

Before adopting a new kit pin, verify its archive/manifest hashes from public access.
Before enabling public contributors: perform a real public-fork run; apply and inspect the protections above; and
select the compatible descriptor2/source2 application/content rollout. These external
actions are pending. Preserved schema1 history is provenance, not a runnable rollback
for descriptor2 readers. Compatible R1/correction/restoration evidence stays with its
recorded producer. Preparation does not freeze the authoring workshop.
