# Parse Hero content

This repository owns the editable M4 catalog and modules. Contributors maintain
descriptive paths, local definition names, explicit exports and exact dependency bindings.
The application derives immutable revisions and canonical artifacts; generated
manifests and release indexes are not contributor files.

Edit source and open one PR. Trusted CI validates that original candidate read-only.
On Windows, `ph-content.cmd check` is the optional local convenience command using
the same pinned managed preparer. Native M5 accepts these same authored modules and
their dependency closure, or the same exact portable/baseline bindings. See
[Contributing](CONTRIBUTING.md) and [Maintainers](docs/maintainers.md).

The public check includes selected-tree metadata and cold browser acquisition planning.
It validates the complete original candidate inventory without querying a moving main.
Safe path moves preserve identity; excessive selected metadata or ancestor depth fails
with a source diagnostic before public acceptance. Rate-limit availability is separate.

This content revision requires compiler/capability39. Each `module` manifest declares
`edition = workshop_1` exactly once. Definitions use declarations such as `class trainee`,
named sections such as `[action.channel]`, and short policy names. Qualified current
spellings assert the edition's contract and cannot override it. Adding a
definition needs no source-list edit. Training owns its player, guard, encounter and
range map together; context and mobile-scout keep separate owners. Basic Classes owns
the Melee/Ranged classes and reusable Curse; Training Dummy owns its health-only targets,
encounters and maps. `workspace.json` names all nine plays across these five modules.
`release-workspace.json` exposes six: training, context, context-shared, outpost,
training-dummy-melee and training-dummy-ranged. The three quick workspace fixtures remain
local selections; the public dummy has 60,000 health and a three-second respawn.
Abilities are ordinary `.phability` definitions, including private possess/return.
Classes bind them with concise actions; encounters own grants, state and schedules.
All seven admitted definition kinds can be public exports: class, encounter, map,
ability, effect, NPC and behavior. Exporting a definition does not grant play eligibility,
activate it or authorize execution.
The [application Authoring Manual](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/authoring/README.md)
is the maintained language reference.

Use an application and validator compatible with compiler/capability39, semantic
contract39 and identity algorithm4. Transport compatibility is owned by the application.
`tools/validator.json` identifies this revision's exact
validator distribution; its presence does not establish publication or activation.
The selected content PR records review and candidate status for the coordinated
validator, trusted-workflow and content transition.
The externally selected workflow remains the required validation gate; candidate YAML
and local validation cannot replace it. Completed activation receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Application deployment and workshop freeze remain separate. See the
[maintainer availability guidance](docs/maintainers.md) for the local-workshop and
anonymous shared-NAT limits.

The supported closure is at most 256 canonical source records and 384 KiB, including
all private definitions, module manifests and the selected descriptor. Inspect each
play's complete closure to measure its remaining capacity under the same byte bounds.
Ordinary content edits reuse a compatible validator. Application workshop authors can
use `python tools/workshop.py check` to build the shared reader incrementally and check
their configured content checkout without publishing a kit. Existing published kits remain
available for public contributors and exact rollback.

Authored definitions, generated representations, documentation and helpers retain
[MIT](LICENSE) terms. Contributors retain copyright; commercial reuse outside
Parse Hero is permitted. Validator binaries retain their scoped free-use terms in
[NOTICE.md](NOTICE.md). Application implementation and branding remain separate.

Use `dependencies = [training]` to declare the exact module alias. An external name such as
`training/class.trainee` always includes the exported kind. A class declares Boolean
`player_selectable`. Encounter and map can both export `practice`. Edit
`modules/context/encounters/practice.phenc` and explicitly restage the `context` play.
