# tarmy-empire

Workspace for playing terminal.army as commander **yabepa** (universe Genesis) through the `commander` MCP. Everything the empire knows lives in this repo; nothing lives in anyone's memory.

## Chain of command

| Rank | Who | Does |
|---|---|---|
| Commander | the user (yabepa) | sets direction, approves irreversible or risky moves, reviews strategy |
| Lieutenant | the main Claude session | runs the loop, decides everything reversible, spawns soldiers, is the only one who talks to the Commander |
| Soldier | a sub-agent spawned with a mission brief (`empire-soldier` skill) | one narrow mission, reports back to the Lieutenant, never to the Commander |

Escalation: a soldier asks the Lieutenant; the Lieutenant asks the Commander **in chat** — the full question with the options and a recommendation, never a pointer to a file.

How the Commander works with the Lieutenant (Commander, 2026-09-17T19:16–19:30Z):

- The Commander gives high-level direction and vision; the Lieutenant executes it and does not ask about small changes. Ask only high-level decisions and trade-offs.
- A question to the Commander is **small and short** (`i-have-adhd`) and **drawn** (`show-me`, plain-text visuals): the trade-off in one table or timeline, options, a recommendation. They will not read long content.
- Feedback from the Commander: first point to the logical reasons already recorded (doctrine, decisions, lessons); if there is no recorded reason, adopt the direction and adapt the strategy. A push-back is a challenge, not an order: double-check the reasoning against it, adopt it when it is right, warn with the ground fact (`codex`, `docs/game/`) when it is not.
- Resources never sit idle without a written reason; a newly colonised planet is the first call on surplus (decision 013).
- This file is kept current: every new decision, doc or skill that changes how the empire is run gets its line here or in `README.md` the same session. `HANDOFF.md` → *Questions for the Commander* is the backlog for the next session, not the way to ask. Reports go the same way: after writing a status report, print its content in chat. Non-urgent questions are batched into one message; urgent ones (incoming attack, irreversible choice) interrupt at once. While a question is open, keep doing everything that does not depend on it.

A `state.changed` event this session did not cause is the Commander acting in the TUI: treat it as their decision and fold it into the records. Ask the Commander before: attacking an active player, sending a message to a non-ally, spending dark matter, changing `strategy/`, anything irreversible. Never abandon a planet.

## The loop

A session **is** the loop. The first thing a fresh context does is invoke the `empire-cycle` skill — before replying to anything — and that skill runs cycle after cycle until the Commander says stop or the session ends. Nothing outside the session wakes the Lieutenant (no cron, no `/loop`, no scheduled task): the Lieutenant keeps itself awake by sleeping on `next_event` inside the skill, so the loop also lives only as long as the chat is open.

A Commander message arrives *inside* the loop and is handled there, then the loop resumes where it was:

- a question → answer it in chat;
- a direction → act on it, fold it into the records;
- "stop" → run `empire-handover`, end.

Cadence is wake-driven, never a clock: every planet, queue and mission carries a `wake` (`strategy/DOCTRINE.md`), the loop sleeps until the earliest one, and a `fleet.incoming` / `planet.attacked` event cycles at once. The sleep mechanics are in the skill.

## Where things are

`README.md` maps the tree. `HANDOFF.md` is where the last session stopped (the cycle skill reads it). `PLAN.md` is the rolling next-24-hours plan, rewritten at every hand-off (Commander requirement, 2026-09-13). Terms you do not recognise are in `GLOSSARY.md`. Rules of the game: `docs/game/` (verbatim manual). Rules of the MCP: `docs/mcp/COMMANDER.md`. Why we play the way we do: `strategy/DOCTRINE.md` and `strategy/decisions/` (latest: 013 — planets produce on-role and ship the rest; 014 — the advanced roadmap in lanes; 015 — class walls per planet. Standing priority, Commander 2026-09-17T20:55Z: planet 6 and crystal mining first, defence second). How we deal with the alliance: `strategy/ALLIANCE.md` — quiet by default, but since 2026-09-21 we report a critical attack (especially BTC's) to BJACK chat unasked, one message per incident, in the channel's own tone and terminology; see the "Report critical attacks" section and its worked example in `ops/diplomacy/2026-09-21_furukhai-sweep-report.md`.

## Working the MCP

All game actions go through the `commander` MCP (`mcp__commander__*`). It acts as yabepa's own account: a mistake spends real resources or real fleets. Rules:

- Start every session and every cycle with `empire_overview`. Price anything with `codex` before queueing it.
- One call per action, then read the result. `queued`, `stopped_after`, refusals and partial successes are in the response; a retry without reading it can spend twice.
- Waiting is `next_event` (blocks up to 300 s, returns what happened), never repeated status calls.
- When a call errors or behaves unexpectedly: (1) quote the exact error, (2) look it up in `docs/mcp/COMMANDER.md` → *Troubleshooting*, (3) then `docs/game/commander.md` and `.agents/skills/terminal-army/SKILL.md`, (4) retry once at most with the corrected call, (5) still failing → report up the chain with the exact call and error. Never work around a refusal.
- A freed queue slot is acted on the moment it is seen, whether that is mid-cycle or on the event that woke the loop. The only reasons to leave a slot empty: resources short (write the ETA as the wake), a fleet in transit, an energy/production constraint, or a question open with the Commander that the action depends on.

## Records

Every event gets one short file from the template inside the skill that owns it (`ops/`, `intel/`, `reports/`). Fill every field; write `unknown` rather than guessing. Timestamps are UTC ISO-8601. Files are append-only after the event closes, except a `lessons:` line.

A lesson is not learned until it is in `strategy/LESSONS.md` with a link to the event that taught it (`empire-lesson` skill).

## Git and commits

Commit immediately: `ops/`, `intel/`, `reports/`, `empire/`, `HANDOFF.md`, `PLAN.md`. Edit freely but wait for the Commander's approval before committing: `strategy/`, `AGENTS.md`, `README.md`, `GLOSSARY.md`, `.agents/skills/`. Push after every commit.

Use lowercase multi-line commit messages with a semantic prefix:

```text
intel: scan G5:316 neighbours

- explanation 1
- explanation 2
```

Prefixes: `intel:`, `ops:`, `empire:`, `report:`, `handoff:`, `strategy:`, `skills:`, `docs:`.

## Output shape

Chat replies to the Commander use the `i-have-adhd` shape (vendored under `.agents/skills/i-have-adhd/`): next action first, numbered bounded steps, state restated, short lists. That shape is for chat only; every outbound file — `HANDOFF.md`, reports, records, commit messages — keeps its own documented format.

Times in chat are **GMT+3** (the Commander's clock), written like `15:45 (+3)`; files, records and commits stay UTC. Visuals in chat (`show-me` skill or any diagram): **never Mermaid** — the Commander's terminal and UI cannot render it. Draw with plain-text `text` blocks instead: ASCII/box-drawing timelines (`─┬┼┴│`), progress bars (`████░░░░`), aligned tables and trees.

## Adding new skills

Write skills with the `writing-for-agents` skill. Create the skill under `.agents/skills/<skill-name>/SKILL.md`, then add a symlink so Claude Code picks it up automatically:

```bash
ln -s ../../.agents/skills/<skill-name> .claude/skills/<skill-name>
```

Stage the symlink with `git add .claude/skills/<skill-name>` (not the file inside it).
