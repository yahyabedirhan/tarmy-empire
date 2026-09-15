# Doctrine

The standing rules. Every rule names the decision or lesson it comes from; a rule with no source is a guess and says so. Change this file only with the Commander's approval (`AGENTS.md` → Git). Numbers that a tool will tell you (prices, times, energy) are never written here: ask `codex` / `production_report`.

Posture: **economy first, adequate defence, raiding parked** (decision 001; raiding parked by the Commander 2026-09-11T15:15Z, L9 — reopen only by the Commander). The empire grows by adding planets and deepening mines; raids are a supplement taken when a target is inactive and the simulation is clean; defence is sized to make raiding us unprofitable, not to win wars.

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

**Lowest mine first.** A mine level goes to whichever planet returns the most per 1 000 resources, priced as (mine cost + the share of energy it forces us to buy) ÷ hourly gain — `codex` on every candidate planet, not one. In practice the colonies' low mines come before the capital's; a mine one level ahead of the empire's lowest is ~32 % worse. Source: decisions 008, 009; BJACK measurements in `ops/diplomacy/2026-09-11_BJACK-chat.md`.

**Energy is priced, not assumed.** Before any energy purchase compare `codex` for solar plant and satellite *on that planet* (crystal per energy; read `energy_after` in `planet_detail` before every mine): plant at low plant levels, satellites once the plant is ~17+ and only behind a wall (they are unarmed). **Fusion is frozen at level 5**: a fusion level burns its extra deuterium every hour for ever (fusion 6: +129 D/h for +84 energy, which three satellites give once) — research round 1 P3, Commander 2026-09-15T12:30Z. A plant is not a purchase, it is what makes the next two mine purchases possible. Source: L1, decision 009.

**The astro clock.** Each cycle computes, for the next *planet-granting* astro level (odd levels; even levels only widen positions — astro 8+9 are one purchase), `ETA_r = (need_r − on hand_r) ÷ empire rate_r` for each resource; the largest is the clock and its resource is the **gate** (2026-09-14: deuterium; 2026-09-15 after the synth push: crystal). A build that spends the gate resource waits unless it raises the gate resource's rate with `cost_gate ÷ gain_per_hour < ETA`; a build priced only in non-gate resources goes. Crystal before metal on colonies until crystal ≥ ½ metal; deuterium synthesizers on cold worlds (capital, 5:316:9, 5:316:14) while deuterium gates. When research time becomes the long leg (`codex build_seconds` > the gate ETA), a lab level is bought. No trades, ever, until the Commander reopens them (decisions 010, 011). Source: decision 009; research round 1 P2/P4 (Commander 2026-09-15T12:30Z).

**Research slot never idle.** Research is one empire-wide slot; an idle hour is lost score. Price a ladder research net of its rung (rungs pay ~40–45k); a research that pays no rung and opens nothing is a loss. When the gate resource is the only thing missing, run a research priced in neither crystal nor deuterium (armour, weapons, laser) rather than idle; combustion and computer cost deuterium and wait while deuterium gates (round 1 P4). Source: decision 009, L5.

**Fields.** One field per building level, cumulative; ships, defence, satellites are free. The capital's remaining fields belong to the facility ladder; colonies carry the deep mines; planet 4 is the crystal world. Source: decision 008.

**Never an empty queue.** Every planet keeps ≥ 2 items queued, ≤ 5. Reserve cheap metal-only builds (storage, robotics) as fillers when crystal is short. Source: archive lessons, 2026-09-07 crystal cascade.

**Research order = quest ladder, with three overrides** (`empire/research.md`): astrophysics whenever it unlocks a planet we can afford to bootstrap; computer whenever fleet slots are the binding constraint on transports/scans; the rest in ladder order.

**Colonize** when all hold: astrophysics allows another planet; a colony ship exists; the slot is chosen per decision 002 and written into `ops/colonies/` *before* launch; the capital can spare the bootstrap cargo. Send the ship only after the research that allows the slot has *completed* (L3).

**Raid** (decision 004, 009): parked until planet 5 or a Commander order. A farm is valued by its *production* (from the scan's mine levels: `rate(L) = ours(L0) × L/L0 × 1.1^(L−L0)`), not its vault — loot is capped at half of each pool per hit, so a vault pays once and production pays daily. The target class is the "sleeping builder": invested score ≥ ours ÷ 5 and rising, mines 18+, wall < 20 turrets, no fleet. A wall that reads 120 RL / 60 LL / 20 HL / 10 ion / 4 gauss / 2 domes is the standard advanced wall: cruisers lose to it (rapid fire only hits RL and LF), only bombers break it, and a large dome alone can force a six-round draw with zero loot. When reopened, the old conditions still hold: target invested score ≥ our score ÷ 5 (server 5× protection, L8 — a refused launch is free intel, try it first); target verdict `farm` in `intel/`; scan < 2 h old at launch (< 30 min preferred — probes are seconds away in-system); `simulate_combat` wins every run and expected losses ≤ 5 % of expected loot (decision 004); expected loot ≥ 30 000 resources and ≥ 15 000 per hour of round trip; a fleet slot stays free for emergencies. Active players: never without the Commander, and only after diplomacy (`strategy/ALLIANCE.md`).

**Defend** (decision 006): rocket launchers are pure metal (2 000) — the sink for idle metal when crystal gates everything else; light lasers against cruisers (no rapid fire on them); defence self-repairs 70 % after a fight while a lost fleet is gone. Stockpiles are the real exposure: an astro hoard on the capital is raid bait, so the capital's wall grows with the hoard (value ≥ hoard ÷ 4). Original rule: defence value on a planet ≥ the resources normally sitting there ÷ 4, plus a small shield dome as soon as it is unlocked. Keep stockpiles low by spending; that is cheaper than any turret.

**Spy** (decision 005, counter law from BJACK 2026-09-11): **one probe per target** — one probe already returns info 5/5 against anyone at or below our espionage level; each extra probe adds only risk. Expected loss before sending: `counter = (defences + domes + parked ships) × probes × 2^(their espionage − ours) / 100` (floor 0.005). A target reading counter ≥ 0.5 is the standard 216-unit wall; do not probe it twice. Raising our espionage one level halves every future probe's risk. neighbourhood watch — systems 310–322 re-scanned every 12 h; anything with a `farm` verdict re-scanned before every sortie. Wider sweeps only on request.

**Dark matter** (decision 003): hoard. Spend only with the Commander's explicit approval.

**Wait well.** Waiting is `next_event` (≤ 300 s per call) plus a computed ETA for resource thresholds. A planet in `waiting` always has its wake written down.

## Cycle cadence

Wake-driven, never a clock. The `empire-cycle` skill loops for as long as the session is open: after each cycle it sleeps on `next_event` until the earliest recorded wake (a queue completing, a fleet arriving, a resource ETA), capped at 2 h so no planet goes unlooked-at longer than that, and cycles at once on any `fleet.incoming` / `planet.attacked`. Watcher soldiers are spawned for one concrete wake each (a research finishing, a fleet returning) and end when it fires.

## Revisiting doctrine

A rule changes through the `empire-lesson` skill: the event → the lesson → the proposed edit → Commander approval. Decision records list their `revisit-when` triggers; the `empire-status` skill reports any that have fired.
