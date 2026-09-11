---
name: empire-soldier
description: Spawn a sub-agent on one narrow mission with a written brief, and record the mission in ops/missions/. Use when a concrete wake (an event, a timestamp, a threshold) needs watching and acting on without the Lieutenant's attention.
---

A soldier is a sub-agent (Agent tool, `subagent_type: general-purpose`, `model: haiku` for watch-and-act, `sonnet` when the mission needs judgement) with exactly one mission. It reports to the Lieutenant, never to the Commander.

1. Write `ops/missions/<YYYY-MM-DDTHH-MM>_<slug>.md` from the template with `status: running`. The brief is the whole prompt: a soldier gets no other context.
2. Spawn with the brief as the prompt, `run_in_background: true`. Put the agent id in the file.
3. On the report: paste the soldier's *Report* section into the file, set `status: done | failed`, commit `ops: mission <slug>`.

Brief rules: one goal, one wake, the exact tool calls with exact parameters, the stop conditions, and the reporting format. `next_event` is one shared stream: an event another agent consumed is gone. A soldier uses `next_event(timeout_seconds=120)` only as a sleep and then *checks state with a read tool* (`build_queue`, `research_tree`, `fleets`, `empire_overview`) — it never relies on seeing the event itself; a soldier never retries a failed spend/commit call more than once; a soldier never sends messages, never attacks, never abandons.

## Template — `ops/missions/<ts>_<slug>.md`

```markdown
---
slug: colonize-5-316-9
status: running | done | failed
model: haiku
agent: <id>
opened: <ts>
closed: <ts>
wake: <event / timestamp / threshold>
---
## Brief
You are a soldier of yabepa's empire in terminal.army, acting through the `commander` MCP. Read `AGENTS.md` → Working the MCP and `docs/mcp/COMMANDER.md` first. Your one mission:

GOAL: <one sentence>
WAKE: <what to wait for and how: e.g. loop next_event(timeout_seconds=300) until an event with type queue.completed and item astrophysics appears, or until <ts>>
THEN: <the exact calls, in order, with parameters>
STOP IF: <conditions → report and end>
REPORT: write the section below and end.

## Report
result: 
calls made: 
observed: 
errors: 
```
