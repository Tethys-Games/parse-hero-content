# Contributing content

Edit the descriptive files under `modules/`. `release-workspace.json` lists entries;
each workspace names its modules, roots and exact dependency bindings. Shared modules
have one physical owner. Keep local symbols and meaningful ordering. Paths, comments
and whitespace do not change a revision; gameplay and exact dependency changes do.
Do not enter generated IDs, hashes or a revision argument, or commit `release.json`.

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

Install Python 3.11 or later and Git for Windows, clone the repository, and edit source.
Run this optional check from the repository root:

```powershell
.\ph-content.cmd check
git diff
```

The helper downloads and verifies the exact pinned validator, captures your original
files, and validates them read-only. It does not allocate names from release history,
rewrite source, or prepare a replacement PR. Commit your source edits and open one PR.
Failures identify the captured file and source span where the reader can locate them;
correct that source and rerun. Retained output is printed. Concurrent edits are
preserved and reported; check the new capture rather than overwriting another writer.

The same check preflights every catalog entry for public M4 acquisition. A module may
be relocated to a bounded directory such as `player/`; update its workspace path and
keep its authored contents unchanged to preserve revisions and canonical bytes.
Public modules need a containing directory. Keep large notes/unowned trees outside
selected module subtrees and avoid excessive ancestor depth. Selected metadata and
cold HTTP/reserved-I/O limits include the browser's possible CORS preflights; the
diagnostic names the affected path and bound. Unrelated unselected subtrees are not
recursively acquired. Local M5 retains its ordinary folder capture behavior.

The pin is trusted distribution metadata, not a contributor-selected executable.
Offline users may pass `--kit-archive <path>`; all exact archive/manifest checks remain.
No local kit installation or Godot installation is needed for this validator.

## GitHub web editor or fork

Edit source and open a PR. The externally pinned **Trusted content integration**
workflow validates your exact original head without executing its scripts or workflows.
A comment-only edit and a gameplay edit both use this same route. No generated commit
or maintainer-authored replacement is required. Stale main/head captures fail visibly;
resolve conflicts or update your source PR and run the newly selected candidate.

After human review, the separately authorized merge queue validates its exact combined
candidate against captured current main. A candidate-controlled green status cannot
replace this trusted gate. This procedure does not itself authorize merging a PR.

## Native M5 and exact dependencies

Select the authored workspace or module inside the native application. Copy its local
dependency closure too, or supply exactly matching portable library bindings. For a
class contribution, select **Contribute** and use the captured match player baseline
when the workspace explicitly binds that role. The Dependencies control supplies local
modules or imports/exports portable exact bindings. A cache locates selected bytes;
it never chooses a dependency version or interprets a missing name as latest.

Matching modules and exact dependency revisions produce identical canonical artifact
bytes in M4 and M5. Complete session equality additionally requires the same roots,
roles, additional classes and preparation options. Ordinary receiving needs no author
permission or origin access. Verified cached bytes can be reused in both directions.

## Migration availability

The earlier public validator/workflow remains available. This automatic-revision
candidate requires a compatible application, validator, content tree and trusted
workflow pin before public cutover; [maintainers](docs/maintainers.md) owns that sequence.
The currently published legacy validator cannot validate this migrated grammar.
