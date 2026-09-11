---
slug: capital-ships
status: running
model: haiku
agent: 
opened: 2026-09-11T08:30Z
closed: 
wake: capital (planet 5080) build queue drops below 5 items, expected 08:46Z and 08:49Z
---
## Brief
You are a soldier of yabepa's empire in terminal.army, acting through the `commander` MCP (tools `mcp__commander__*`; load them with ToolSearch `select:` first). Read `AGENTS.md` → Working the MCP and `docs/mcp/COMMANDER.md` first. Your one mission:

GOAL: queue three ship batches at the capital (planet_id 5080) as queue slots free up: first `light_fighter` × 60, then `large_cargo` × 3, then `recycler` × 2.
WAKE: loop — call `next_event(timeout_seconds=120)` purely as a sleep (ignore its contents), then `build_queue(planet_id=5080)`. Whenever the list has fewer than 5 items, queue the next batch that is not yet queued with `build_ships(key=..., count=..., planet_id=5080)`. Expected: two slots free around 08:46–08:49Z, a third around 09:26Z. Give up at 2026-09-11T10:00Z (server UTC).
STOP IF: a `build_ships` call errors twice in a row (report the exact error); or the queue never frees before the deadline. Never cancel anything. Never send messages, never attack, never abandon anything.
REPORT: fill the section below and end — list each batch with the queue id and `finished_at` the server returned.

## Report
result: 
calls made: 
observed: 
errors: 
