# Doctrine

The standing rules. Every rule names the decision or lesson it comes from; a rule with no source is a guess and says so. Change this file only with the Commander's approval (`AGENTS.md` → Git). Numbers that a tool will tell you (prices, times, energy) are never written here: ask `codex` / `production_report`.

Posture: **economy first, opportunistic raider, adequate defence** (decision 001). The empire grows by adding planets and deepening mines; raids are a supplement taken when a target is inactive and the simulation is clean; defence is sized to make raiding us unprofitable, not to win wars.

## Planet state machine

Every planet file (`empire/planets/`) carries exactly one state, one sub-state, and one **wake** (what it is waiting for). The `empire-cycle` skill runs each planet through this table top to bottom; the first row that matches is the state.

| State | Sub-states | Enter when | Do | Leave when |
|---|---|---|---|---|
| `THREATENED` | `incoming` `recovering` | `fleets` shows a hostile fleet aimed at it, or it was hit in the last 24 h | `incoming`: read the attacker; `simulate_combat`; if we lose, fleet-save (deploy ships + resources to another planet timed to return after arrival) and rush nothing; alert the Commander. `recovering`: rebuild defences per 006, read the combat report, write the lesson | no hostile fleet and 24 h since the hit |
| `STALLED` | `energy` `storage` `fields` | production factor < 1; a pool ≥ 90 % of cap; fields ≤ 2 free | `energy`: solar plant, else fusion (compare with `codex`), before any mine. `storage`: spend (transport to a needing planet, queue builds) or storage level. `fields`: stop mines, plan terraformer | the trigger is gone |
| `BOOTSTRAP` | `landing` `powering` `stocking` | planet age < 24 h or metal mine < 8 | follow the bootstrap order in the `empire-colonize` skill; transports from the capital every cycle | metal mine ≥ 8, solar covers it, storage ≥ 2 |
| `STAGING` | `fortify` `fleet` | a named mission in `ops/missions/` or `ops/attacks/` needs this planet to build ships/defence | build exactly what the mission file lists, nothing else, until it is done | the mission file says `status: ready` |
| `GROWING` | `building` `waiting` | everything else | the `empire-farm` skill: keep ≥ 2 items in the build queue in doctrine order; research per `empire/research.md`; `waiting` when nothing affordable — write the wake as a resource threshold + ETA | never (default state) |

Roles (long-lived, set in the planet file, decision 002): `capital` (highest lab, shipyard, fleet home), `metal-world`, `crystal-world`, `deut-world`, `forward-base`. The role picks which mine the `empire-farm` skill favours when several are affordable.

## Standing rules

**Energy first.** No mine, synthesizer or crawler is queued on a planet whose production factor is < 1 or would drop below 1 after the build (`codex` shows energy draw). Source: lesson L1, the 2026-09-06 energy collapse.

**Never a full pool.** A pool above 80 % of cap triggers spending or a storage level this cycle. Lost production is the only loss that cannot be recovered. Source: L2 (colony metal sat at cap for days).

**Never an empty queue.** Every planet keeps ≥ 2 items queued, ≤ 5. Reserve cheap metal-only builds (storage, robotics) as fillers when crystal is short. Source: archive lessons, 2026-09-07 crystal cascade.

**Research order = quest ladder, with three overrides** (`empire/research.md`): astrophysics whenever it unlocks a planet we can afford to bootstrap; computer whenever fleet slots are the binding constraint on transports/scans; the rest in ladder order.

**Colonize** when all hold: astrophysics allows another planet; a colony ship exists; the slot is chosen per decision 002 and written into `ops/colonies/` *before* launch; the capital can spare the bootstrap cargo. Send the ship only after the research that allows the slot has *completed* (L3).

**Raid** (decision 004) when all hold: target verdict `farm` in `intel/`; scan < 6 h old; `simulate_combat` wins every run and expected losses ≤ 5 % of expected loot (decision 004); expected loot ≥ 30 000 resources and ≥ 15 000 per hour of round trip; a fleet slot stays free for emergencies. Active players: never without the Commander, and only after diplomacy (`strategy/ALLIANCE.md`).

**Defend** (decision 006): defence value on a planet ≥ the resources normally sitting there ÷ 4, plus a small shield dome as soon as it is unlocked. Keep stockpiles low by spending; that is cheaper than any turret.

**Spy** (decision 005): neighbourhood watch — systems 310–322 re-scanned every 12 h; anything with a `farm` verdict re-scanned before every sortie. Wider sweeps only on request.

**Dark matter** (decision 003): hoard. Spend only with the Commander's explicit approval.

**Wait well.** Waiting is `next_event` (≤ 300 s per call) plus a computed ETA for resource thresholds. A planet in `waiting` always has its wake written down.

## Cycle cadence

One `empire-cycle` every 30 minutes while a session is open, or immediately on any `fleet.incoming` / `planet.attacked`. Watcher soldiers are spawned for one concrete wake each (a research finishing, a fleet returning) and end when it fires.

## Revisiting doctrine

A rule changes through the `empire-lesson` skill: the event → the lesson → the proposed edit → Commander approval. Decision records list their `revisit-when` triggers; the `empire-status` skill reports any that have fired.
