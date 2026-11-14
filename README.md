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

This Garr S01 / Lucifron S02 candidate requires the unpublished compiler/capability44 application
reader. The public gate and `tools/validator.json` remain compiler41 and may reject
the new syntax; no public activation is selected. [Play Garr locally](docs/garr.md) or
[play the Lucifron utility candidate](docs/lucifron.md).

Each `module` manifest declares
`edition = workshop_1` exactly once. Definitions use declarations such as `class trainee`,
named sections such as `[action.channel]`, and short policy names. Qualified current
spellings assert the edition's contract and cannot override it. Adding a
definition needs no source-list edit. The three source modules are:
`basic_classes` owns Melee/Ranged, their four paid offensive abilities, free recovery and shared Curse;
`training_encounters` owns the dummy and both opponent practices, private NPC kits and
variants, grant utilities and shared Slow. NPC Curse imports `basics/effect.curse`.
`classicwow_moltencore` adds Garr and Firesworn with a private ordinary NPC kit at
`modules/classicwow/moltencore`, without a dependency on Training Encounters.
The three retained public entries are `training-dummy` (Training Dummy),
`grant-practice-melee` (Melee Opponent Practice) and `grant-practice-ranged` (Ranged
Opponent Practice). Each retains both Basics in one immutable Session. A participant's
personal choice does not change that Session's identity. The new candidate entry
`classicwow-moltencore-garr` and `classicwow-moltencore-lucifron` also admit both Basics in one Session.
Lucifron selects both Basics, one shared enemy kit and one solo-proxy kit; retained Garr
definitions validate without occupying another active kit.
The production dummy retains 60,000 health and a three-second respawn. Older Training,
Context/Mobile Scout, Visitor/Frost and quick-dummy source now belongs to maintained
application development fixtures, outside this production repository.
All seven admitted definition kinds can be public exports: class, encounter, map,
ability, effect, NPC and behavior. Exporting a definition does not grant play eligibility,
activate it or authorize execution.
The [application Authoring Manual](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/authoring/README.md)
is the maintained language reference.

Use the changed application reader for this candidate: compiler/capability44, semantic
contract44 and identity algorithm4. Transport compatibility is owned by the application.
`tools/validator.json` continues to identify the public compiler41 distribution.
Its presence does not establish publication or activation; the external workflow remains
the required gate. Local checks do not replace that gate.
The selected content PR records review and candidate status for the coordinated
validator, trusted-workflow and content transition.
The externally selected workflow remains the required validation gate; candidate YAML
and local validation cannot replace it. Completed activation receipts belong in the
[application workshop runbook](https://github.com/Tethys-Games/parse-hero/blob/alpha/a3-a4-authoring-workshop/docs/runbooks/authoring-workshop.md).
Application deployment and workshop freeze remain separate. See the
[maintainer availability guidance](docs/maintainers.md) for the local-workshop and
anonymous shared-NAT limits.

Both grant practices start the player and enemy at 1,000 health. Right-click each
pedestal to learn its utility on keys 5 and 6. Basic offense remains on keys 1 and 2;
key 3 now recovers 40 resource with a six-second cooldown, including from depletion.
Melee Attack/Cleave cost 8/16; Ranged Attack/Curse cost 12/12. Key 4 stays empty.
Basic Curse retains its eight-second, four-pulse Magic DoT. The imported NPC Curse
still uses that exact shared effect; private training attacks and utility grants stay free.
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
