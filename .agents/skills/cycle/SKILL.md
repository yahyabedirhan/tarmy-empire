---
name: cycle
description: One heartbeat of the empire loop. Reads the empire, runs every planet through its state, acts, records, hands off.
disable-model-invocation: true
---

One cycle. Run it every 30 minutes (`/loop 30m /cycle`) and immediately after any `fleet.incoming` or `planet.attacked` event. `strategy/DOCTRINE.md` is the rulebook; this file is the order of operations.

1. **Read.** `empire_overview`, then `fleets`, then `production_report` and `build_queue` for every planet beyond the first. `quests` (it pays finished rungs). `alliance_chat` and `messages` for anything new → `ops/diplomacy/` if it concerns us.
2. **Threats.** Any hostile fleet inbound → that planet is `THREATENED / incoming`: follow the DOCTRINE row now, before anything else, and alert the Commander.
3. **Per planet**, in `empire/planets/`: decide the state with the DOCTRINE table (first matching row), then act:
   - `STALLED` → fix the trigger (energy / storage / fields).
   - `BOOTSTRAP` → `colonize` skill, bootstrap section.
   - `STAGING` → build what the mission file lists.
   - `GROWING` → `farm` skill.
   If state or sub-state changed, append a row to the planet's *State history* and update the frontmatter (`state`, `substate`, `since`, `wake`).
4. **Missions.** For every open file in `ops/missions/` with `status: running`, check whether its wake fired (a soldier reported, an event arrived, a timestamp passed). Close it with a result or let it run. Spawn new soldiers (`soldier` skill) only for a concrete wake.
5. **Opportunities.** If a fleet slot is free and no mission needs it: due scans (`spy` skill, decision 005); a `farm` target with a fresh scan and a clean simulation (`raid` skill, Lieutenant only).
6. **Record.** Commit `empire/`, `ops/`, `intel/` changes (`AGENTS.md` → Git). Every 4th cycle or on any notable change, `status` skill.
7. **Hand off.** `handover` skill: `HANDOFF.md` reflects this cycle. Commit it.

Done when every planet file's `wake` names something that has not happened yet, every open mission has a `wake`, and `HANDOFF.md` is committed.
