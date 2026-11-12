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

This grant-practice candidate requires compiler/capability40. Each `module` manifest declares
`edition = workshop_1` exactly once. Definitions use declarations such as `class trainee`,
named sections such as `[action.channel]`, and short policy names. Qualified current
spellings assert the edition's contract and cannot override it. Adding a
definition needs no source-list edit. Exactly two production modules remain:
`basic_classes` owns Melee/Ranged, their four reusable player abilities and shared Curse;
`training_encounters` owns the dummy and both opponent practices, private NPC kits and
variants, grant utilities and shared Slow. NPC Curse imports `basics/effect.curse`.
The three workspace plays and public entries are `training-dummy` (Training Dummy),
`grant-practice-melee` (Melee Opponent Practice) and `grant-practice-ranged` (Ranged
Opponent Practice). Each retains both Basics in one immutable Session. A participant's
personal choice does not change that Session's identity.
The production dummy retains 60,000 health and a three-second respawn. Older Training,
Context/Mobile Scout, Visitor/Frost and quick-dummy source now belongs to maintained
application development fixtures, outside this production repository.
All seven admitted definition kinds can be public exports: class, encounter, map,
ability, effect, NPC and behavior. Exporting a definition does not grant play eligibility,
activate it or authorize execution.
The [application Authoring Manual](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/authoring/README.md)
is the maintained language reference.

Use an application and local validator compatible with compiler/capability40, semantic
contract40 and identity algorithm4. Transport compatibility is owned by the application.
The public validator in `tools/validator.json` and the enforced workflow still select
compiler39. This candidate is intended for Draft review and strict unpublished local
staging; it requires a separately authorized compatible publication and cutover before
public-main acquisition. Local checks do not replace that gate.
The selected content PR records review and candidate status for the coordinated
validator, trusted-workflow and content transition.
The externally selected workflow remains the required validation gate; candidate YAML
and local validation cannot replace it. Completed activation receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Application deployment and workshop freeze remain separate. See the
[maintainer availability guidance](docs/maintainers.md) for the local-workshop and
anonymous shared-NAT limits.

Both grant practices start the player and enemy at 1,000 health. Right-click each
pedestal to learn its utility on keys 5 and 6; the visitor's base actions remain on 1â€“4.
Melee grants Slow (50% for five seconds; 12-second cooldown) and held Defend
(one second, rooted and immune; 30-second cooldown). Ranged grants Interrupt
(2,500 mm; six-second cooldown) and friendly/self Dispel (12,000 mm; eight-second cooldown).
Slow's range is 12,000 mm. All four utilities cost zero resource. Dispel requires an
explicit friendly or self selection and consumes nothing when no eligible effect exists.
The ranged enemy's projectile casts for three seconds and cools down for four;
Curse cools down for twelve. It retains a three-metre retreat goal only while both
actions cool down. Invalid or stalled goals exhaust five candidates and hold.
The selected opponent and two Basics occupy three installed kits; the sibling opponent
remains fully validated source but is inactive. The independent application fixture
imports `practice/effect.slow` for its alternate delivery; no effect copy is required.

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

Use `dependencies = [basics]` to declare the exact module alias. An external name such as
`basics/effect.curse` includes its exported kind. A class declares Boolean
`player_selectable`. Edit `modules/training_encounters/encounters/melee_practice.phenc`
and explicitly restage the `grant-practice-melee` play.
