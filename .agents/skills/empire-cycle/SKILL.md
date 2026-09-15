---
name: empire-cycle
description: The empire loop. The first skill a fresh context invokes; it reads HANDOFF.md, runs one cycle (read the empire, run every planet through its state, act, record, hand off), sleeps on next_event until the earliest wake, and repeats until the Commander says stop.
---

The loop. It starts when a session starts and ends when the Commander says stop. `strategy/DOCTRINE.md` is the rulebook; this file is the order of operations. Steps 1–7 are one cycle; step 8 is the sleep between cycles.

0. **Resume** (fresh context only). Read `HANDOFF.md` → *Do this first* and *Next actions*; they are the plan until step 3 rewrites it.
1. **Read.** `empire_overview`, then `fleets`, then `production_report` and `build_queue` for every planet beyond the first. `quests` (it pays finished rungs). `messages` for anything new. `alliance_chat` only every 4th cycle (with the status report), skimmed for the four things in `strategy/ALLIANCE.md` → *watch, not a feed*; trades and strategy talk are ignored, not filed.
2. **Threats.** Any hostile fleet inbound → that planet is `THREATENED / incoming`: follow the DOCTRINE row now, before anything else, and alert the Commander.
3. **Per planet**, in `empire/planets/`: decide the state with the DOCTRINE table (first matching row), then act:
   - `STALLED` → fix the trigger (energy / storage / fields).
   - `BOOTSTRAP` → `empire-colonize` skill, bootstrap section.
   - `STAGING` → build what the mission file lists.
   - `GROWING` → `empire-farm` skill.
   If state or sub-state changed, append a row to the planet's *State history* and update the frontmatter (`state`, `substate`, `since`, `wake`). The `wake` is a timestamp or an event, never "next cycle".
4. **Missions.** For every open file in `ops/missions/` with `status: running`, check whether its wake fired (a soldier reported, an event arrived, a timestamp passed). Close it with a result or let it run. Spawn new soldiers (`empire-soldier` skill) only for a concrete wake.
5. **Opportunities.** If a fleet slot is free and no mission needs it: due scans (`empire-spy` skill, decision 005); a `farm` target with a fresh scan and a clean simulation (`empire-raid` skill, Lieutenant only).
6. **Record.** Commit `empire/`, `ops/`, `intel/` changes (`AGENTS.md` → Git). Every 4th cycle or on any notable change, `empire-status` skill.
7. **Hand off.** `empire-handover` skill: `HANDOFF.md` reflects this cycle. Rewrite `PLAN.md` (the next 24 h as a table of wake → action → gate; drop done lines). Commit both. A cycle is complete when every planet file's `wake` names something that has not happened yet, every open mission has a `wake`, and `HANDOFF.md` is committed.
8. **Sleep**, then go to 1. The next wake is the earliest of: every planet's `wake`, every running mission's `wake`, every queued item's completion time, every resource-threshold ETA — capped at 2 h from now (pools, quests and messages have no event; 2 h is the longest a planet may go unlooked-at). State the wake in chat in one line (`sleeping until 13:50:31Z — light_fighter 60 at 5:316:12`), then call `next_event(timeout_seconds = min(300, seconds until the wake))` in a chain until it returns something or the wake time passes:
   - `fleet.incoming` / `planet.attacked` → step 2 now.
   - `queue.completed` / `fleet.returned` / `fleet.combat` / `state.changed` → step 1 now (a freed slot is filled the moment it is seen).
   - `alliance.message.received` / `[]` → keep sleeping.
   A Commander message during the sleep is handled (`AGENTS.md` → The loop) and the sleep resumes with the same wake; "stop" ends the loop after step 7.
