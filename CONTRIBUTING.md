# Contributing content

Edit the descriptive files under `modules/`. `release-workspace.json` lists entries;
`workspace.json` names its modules, plays and exact dependency bindings. Shared modules
have one physical owner. Keep local symbols and meaningful ordering. Paths, comments
and whitespace do not change a revision; gameplay and exact dependency changes do.
Do not enter generated IDs, hashes or a revision argument, or commit `release.json`.

Start a definition with its kind/version and local name, for example `ability/v4 channel`.
Use schema-defined named sections, such as `[resource/bounded_int focus]` and `[action channel]`.
A `module/v20` manifest declares exports and dependency slots. Recognized files below
its directory belong to that module unless a child module starts a new boundary.
Private unused definitions are still checked and retained; do not hide invalid work by
omitting an export. Duplicate names in the same scope reject. Class-local names, typed
artifact references, action bindings and stable actor keys keep their separate meanings.

Public exports may expose class, encounter, map, ability, NPC and behavior definitions.
Use `alias/export_name` only in a typed consumer that admits that kind. Exports must
be owned locally; dependencies cannot be re-exported. A public NPC or behavior library
needs no default play. Class `eligibility` and encounter grants are separate permissions.

Write programs in `.phability` files and bind a class action with `definition`.
Its single resource and actor-action cooldown infer their unique binding. Optional
matching assertions normalize identically; contradictory assertions reject. Tracking's
explicit actor-or-encounter permission and encounter access choices remain meaningful.
Possess and return live in private files while the encounter keeps finite grants and
state. The former encounter `[ability]` spelling is retired. Moving a program into a
new file intentionally changes module identity; validation/import do not make that edit.

A play selects explicit exported roots, for example `training/class.trainee`,
`training/encounter.training` and `training/map.range`. Two distinct eligible classes
from one module may participate; repeated aliases resolving to the same root reject.
See the [Authoring Manual](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/authoring/README.md)
for the grammar, fixed encounter policy omissions and executable examples.

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

The same check validates every declared module and play, and preflights each catalog
selection for public M4 acquisition. A module may
be relocated to a bounded directory such as `player/`; update its workspace path and
keep its authored contents unchanged to preserve revisions and canonical bytes.
Public modules need a containing directory. Keep large notes/unowned trees outside
selected module subtrees and avoid excessive ancestor depth. Selected metadata and
cold HTTP/reserved-I/O limits include the browser's possible CORS preflights; the
diagnostic names the affected path and bound. Unrelated unselected subtrees are not
recursively acquired. Local M5 retains its ordinary folder capture behavior.

The pin is trusted distribution metadata, not a contributor-selected executable.
Offline users may pass `--kit-archive <path>`; all exact archive/manifest checks remain.
If the selected kit has not been published, use its exact reviewed local archive or
the application workshop check below. [PR7](https://github.com/Tethys-Games/parse-hero-content/pull/7)
records publication and activation status. No local kit installation or Godot
installation is needed for this validator.

In the application checkout, workshop authors can instead run `python tools/workshop.py check`.
It incrementally builds the same shared validator and checks the configured content checkout;
`--no-build` reuses a current build. Editing supported content needs no validator release.
Parser, semantic or supported-capacity changes require a compatible reader and coordinated
public promotion. Keep the published historical kits for exact pins and rollback.

A complete selected closure may contain at most 256 canonical source records and 384 KiB.
Private definitions, module manifests and the generated descriptor all count. This is a
combined count/byte limit, not permission for 256 maximum-sized files or new asset kinds.
Current outpost/context-shared plays use 32 records and leave 224 record slots; active gameplay
limits are unchanged. Public planning also checks 320 HTTP slots, 8 MiB charged I/O and
a complete 896 KiB archive, including mandatory inventory.

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
when the workspace explicitly binds `baseline_role = player`. Root enumeration and named
plays resolve that exact retained owner automatically, without a second native alias selection.
Cancellation, failure or stale inputs preserve the previous chooser state. The Dependencies control supplies local
modules or imports/exports portable exact bindings. A cache locates selected bytes;
it never chooses a dependency version or interprets a missing name as latest.
The Roots control selects a named play or exported typed roots. Its named-play route
captures only that play's complete closure; explicit root choices retain the selected
module pins. A contribution preserves the exact match encounter, map and required classes.

Matching modules and exact dependency revisions produce identical canonical artifact
bytes in M4 and M5. Complete session equality additionally requires the same roots,
roles, additional classes and preparation options. Ordinary receiving needs no author
permission or origin access. Verified cached bytes can be reused in both directions.

## Availability

This source revision requires compiler/capability32 and the compatible validator
identified by `tools/validator.json`. [PR7](https://github.com/Tethys-Games/parse-hero-content/pull/7)
records the coordinated transition's review and activation status. An externally
selected older validator can reject newer content until its reviewed pin changes;
keep that result visible and do not disable or bypass the gate. Local candidate
validation is a separate result. Application integration, deployment and workshop
freeze remain separate. The [maintainer guide](docs/maintainers.md) defines compatible
preparation and rollback; the application workshop runbook records completed activation.

Public M4 reads GitHub anonymously. The selected validator reports each play's cold
metadata/raw/CORS request plan and mandatory archive reservation. REST is limited to
60 requests/hour/IP, shared by users behind a NAT. Cached immutable objects reduce
repeat traffic but do not guarantee cold-start availability. Wait for a reported rate
limit to reset or use an explicitly selected compatible known-good/bundled payload.
An assigned authority must acquire its exact pin or fail; it cannot use fallback.
