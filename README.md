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

This Draft candidate requires compiler/capability36 and uses compact declarations
such as `class/v16 trainee`, named
sections such as `[action.channel]`, and generic `module/v21` manifests. Adding a
definition needs no source-list edit. Training owns its player, guard, encounter and
range map together; context and mobile-scout keep separate owners. `workspace.json`
preserves the four catalog plays and adds `training-dummy-quick`, an explicit 100-health
respawn fixture using the existing trainee kit. The production dummy remains at 60,000
health; both named roles use a three-second death respawn delay. Basic Classes and
their two final plays are still being implemented in application PR527.
Abilities are ordinary `.phability` definitions, including private possess/return.
Classes bind them with concise actions; encounters own grants, state and schedules.
All six admitted definition kinds can be public exports: class, encounter, map,
ability, NPC and behavior. Exporting a definition does not grant play eligibility,
activate it or authorize execution.
The [application Authoring Manual](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/authoring/README.md)
is the maintained language reference.

Use the current application workshop reader compatible with compiler/capability36,
semantic contract36 and identity algorithm3. Encounter source is `encounter/v16`.
Transport compatibility is owned by the application. Public main, `tools/validator.json`
and the trusted workflow remain on compiler34. That published validator is expected
to reject this Draft grammar until a separately authorized public cutover.
The selected content PR records review and candidate status for the coordinated
validator, trusted-workflow and content transition.
The externally selected workflow remains the required validation gate; candidate YAML
and local validation cannot replace it. Completed activation receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Application deployment and workshop freeze remain separate. See the
[maintainer availability guidance](docs/maintainers.md) for the local-workshop and
anonymous shared-NAT limits.

The supported closure is at most 256 canonical source records and 384 KiB, including
all private definitions, module manifests and the selected descriptor. The current
largest plays use 32 records, leaving 224 record slots subject to the same byte bounds.
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
