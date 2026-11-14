# Garr S01

Select `classicwow-moltencore-garr` from `workspace.json`. Both Basic Melee and
Basic Ranged belong to the same Session and each participant chooses independently.
The module exports `encounter.garr` and `map.garr`; its elemental kit, strike,
behavior and NPC templates are private.

Preparation has no combat timer. Choose classes, then right-click the Pull object
near the player spawns. The committed Pull freezes the eligible human party:
one human selects Garr and three Firesworn, two select four Firesworn, and larger
parties select `min(8, N + 2)` Firesworn. Enemies activate together after their
complete selected roster is installed. The two-minute deadline starts then.

Defeat Garr and every selected Firesworn in any order. Individual deaths leave
survivors able to finish; all counted lives defeated fails the attempt, including
on the final enemy's death cut. Party Retry clears progress and acquired utilities
and returns everyone to fresh Preparation after old work settles. Class changes
after Pull reject; a new human cannot join the frozen fight. Leave uses normal
session teardown. Numbers are provisional balance for this scoped milestone.

This branch is a local candidate. The public compiler41 validator and required
workflow remain unchanged and cannot validate the new Pull vocabulary. Build the
changed application reader and use its maintained workshop `author check`,
`inspect`, `emit` and `verify` commands. Install that emitted selection through
ordinary local authoring; use candidate mode for a locally served browser build.
Ordinary public Lobby Play still acquires public main's three practices.

S01 does not implement Banish, Clear Shackles, pressure, tethers, death fuses or
general reactions. S08/S09 evolve this same encounter and play into full Garr.
