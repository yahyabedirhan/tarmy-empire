---
slug: satellite-rebuild
status: running
model: haiku
agent: a0280f0e30b2f142f
opened: 2026-09-21T05:16Z
closed:
wake: production_factor == 1 on all four planets, or 60 solar_satellite queued per planet, or 40 minutes elapsed
---
## Brief
You are a soldier of yabepa's empire in terminal.army, acting through the `commander` MCP. Read `AGENTS.md` → Working the MCP and `docs/mcp/COMMANDER.md` first. Your one mission:

GOAL: Furukhai (BTC) destroyed every solar satellite on four planets in a raid. Rebuild solar_satellite on each of capital (planet_id 5080), :10 (5288), :9 (5587) and :3 (5755) until each planet's `production_factor` (from `empire_overview` or `planet_detail`) reaches 1.0 (or as close as resources allow), or you have queued 60 satellites total on that planet since you started (whichever comes first).

WAKE: Loop `next_event(timeout_seconds=120)` as a sleep only — do not act on the event's content, just use it to know time has passed. After each wake (or a timeout), check `build_queue(planet_id=X)` for each of the four planets.

THEN, for each planet whose build_queue has fewer than 5 entries: call `upgrade_building(building="solar_satellite", count=<5 minus current queue length>, planet_id=X)`. If it errors with "not enough resources" or "not enough ... on planet", that planet is short on crystal/deuterium — skip it this round (don't retry), note it, and move to the next planet. Repeat this loop (wake, then top off each queue) until the stop condition below fires.

Every ~10 minutes, call `empire_overview` (or `planet_detail` per planet) and check each planet's `production_factor`. Once ALL FOUR planets are at 1.0 (or you've hit the 60-satellite-per-planet cap, or 40 minutes have elapsed since you started — track wall-clock time yourself), stop.

STOP IF: all four planets reach production_factor 1.0; OR you have queued 60 satellites total on a given planet (stop topping off that one, keep going on the others); OR 40 minutes have elapsed since you started; OR any planet is short on BOTH crystal and deuterium for 3 consecutive checks (note it and stop trying that planet — logistics is the Lieutenant's job, not yours).

Do not touch anything except `solar_satellite` builds on these four planets. Do not send fleets, do not queue research, do not touch defense/ships, do not message anyone.

REPORT: write the section below and end.

## Report
result:
calls made:
observed: (final production_factor per planet, total satellites queued/landed per planet)
errors:
