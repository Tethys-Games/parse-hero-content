# Contributing content

Edit the descriptive files under `modules/`. Entries are declared in the root
`release-workspace.json` and their root-level workspace JSON files. Shared modules
have one physical owner. Keep comments and meaningful ordering; the production
updater changes only required IDs, references, dependency pins and generated metadata.

## Contribution rights

The authored definitions, module/workspace manifests, generated representations and
accompanying documentation use the [MIT license](LICENSE). You retain copyright in
your work. By submitting a contribution for inclusion, you license it under those
same MIT terms and confirm that you have the right to do so. No copyright assignment
or separate contributor agreement is required.

MIT permits reuse and modification in other projects, including commercial projects.
Keep copyright and permission notices with copies or substantial portions; for
generated distributions, include the license and relevant notices alongside the
content or product. Preserve any existing third-party notices and identify any
third-party material and its license in your PR. The application implementation,
non-corpus game assets and branding remain separately scoped in [NOTICE.md](NOTICE.md).

## Local editing on Windows

Install Python 3.11 or later and Git for Windows. Clone this repository, edit your
source, then run these commands from its root:

```powershell
.\ph-content.cmd prepare
.\ph-content.cmd check
git diff
```

`prepare` obtains and verifies the pinned public validator, captures approved upstream
history once, chooses an unpublished revision when needed, stages and strictly validates
the complete result, and only then applies changes. You do not install a kit manually,
capture history yourself, choose a revision label, or repair hashes. A repeat run with
unchanged input makes no unnecessary changes. Check remains read-only. Both commands
print the retained output location; preparation includes `proposal.diff`, entry hashes
and diagnostics. Failures preserve the original edit and staged/recovery files.
If another writer changes the checkout or main, review the reported difference and
prepare again; do not overwrite that writer or reuse a stale proposal.

Commit the authored files and matching generated `release.json` together. Review the
ordinary diff, then propose a PR. There is one authored tree and no distribution copy.
Physical directory moves preserve canonical meaning; logical paths and gameplay edits
can require revised immutable identities. The updater makes that decision with the
production compiler and complete approved history.

## Editing in the GitHub web editor or a fork

Edit source and open a PR. Windows PR CI runs the same preparation operation on your
exact Git head without running your branch's scripts. Its report distinguishes:

- **Source prepared:** the proposal and every advertised entry validate. Review the
  generated changes in `proposal.diff` and the accompanying proposal files.
- **Committed tree valid:** your actual commit already contains the correct authored
  bytes and generated index. A successful proposal cannot make a stale commit pass
  this check or grant final integration approval.

For web-only edits, ask a maintainer to run **Maintainer content preparation** with
the PR number, exact head and expected main. It independently rebuilds the proposal
with protected tooling and creates an upstream review branch; fork write access is
not required. The maintainer can open that branch as the successor PR and link your
original PR. Review it before integration. A changed PR head/main rejects preparation
or requires a fresh rebuild. The complete prepared tree must land atomically using
the exact-candidate ordinary-successor procedure in [maintainers](docs/maintainers.md).

An invalid edit reports the affected file/span and associated entry where the
production reader can identify them. Correct that source and rerun; do not edit raw
hashes or bypass the validator. Catalog bounds, immutable IDs, safe paths and limits
also apply to new entries; no application allowlist grants membership.

## Current availability

The first Windows validator is publicly available as an immutable release, with free
validator use, MIT helper terms and MIT authored content; see [NOTICE.md](NOTICE.md).
The convenience command downloads and verifies the exact URL and hashes in the pin.
An actual public-fork run, protected contributor settings and compatible
content/application rollout remain pending. Local reviewers can also select the same
archive with `--kit-archive <path>`; all digest checks remain.
See [validator provenance](tools/validator.json) and [maintainers](docs/maintainers.md).
