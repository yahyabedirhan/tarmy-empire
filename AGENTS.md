# tarmy-empire

Workspace for playing terminal.army as commander **yabepa** (universe Genesis) through the `commander` MCP. Everything the empire knows lives in this repo; nothing lives in anyone's memory.

## Chain of command

| Rank | Who | Does |
|---|---|---|
| Commander | the user (yabepa) | sets direction, approves irreversible or risky moves, reviews strategy |
| Lieutenant | the main Claude session | runs the loop, decides everything reversible, spawns soldiers, is the only one who talks to the Commander |
| Soldier | a sub-agent spawned with a mission brief (`empire-soldier` skill) | one narrow mission, reports back to the Lieutenant, never to the Commander |

Escalation: a soldier asks the Lieutenant; the Lieutenant asks the Commander **in chat** — the full question with the options and a recommendation, never a pointer to a file. `HANDOFF.md` → *Questions for the Commander* is the backlog for the next session, not the way to ask. Reports go the same way: after writing a status report, print its content in chat. Non-urgent questions are batched into one message; urgent ones (incoming attack, irreversible choice) interrupt at once. While a question is open, keep doing everything that does not depend on it.

A `state.changed` event this session did not cause is the Commander acting in the TUI: treat it as their decision and fold it into the records. Ask the Commander before: attacking an active player, sending a message to a non-ally, spending dark matter, changing `strategy/`, anything irreversible. Never abandon a planet.

## Where things are

`README.md` maps the tree. Read `HANDOFF.md` first in every new session. Terms you do not recognise are in `GLOSSARY.md`. Rules of the game: `docs/game/` (verbatim manual). Rules of the MCP: `docs/mcp/COMMANDER.md`. Why we play the way we do: `strategy/DOCTRINE.md` and `strategy/decisions/`.

## Working the MCP

All game actions go through the `commander` MCP (`mcp__commander__*`). It acts as yabepa's own account: a mistake spends real resources or real fleets. Rules:

- Start every session and every cycle with `empire_overview`. Price anything with `codex` before queueing it.
- One call per action, then read the result. `queued`, `stopped_after`, refusals and partial successes are in the response; a retry without reading it can spend twice.
- Waiting is `next_event` (blocks up to 300 s, returns what happened), never repeated status calls.
- When a call errors or behaves unexpectedly: (1) quote the exact error, (2) look it up in `docs/mcp/COMMANDER.md` → *Troubleshooting*, (3) then `docs/game/commander.md` and `.agents/skills/terminal-army/SKILL.md`, (4) retry once at most with the corrected call, (5) still failing → report up the chain with the exact call and error. Never work around a refusal.

## Records

Every event gets one short file from the template inside the skill that owns it (`ops/`, `intel/`, `reports/`). Fill every field; write `unknown` rather than guessing. Timestamps are UTC ISO-8601. Files are append-only after the event closes, except a `lessons:` line.

A lesson is not learned until it is in `strategy/LESSONS.md` with a link to the event that taught it (`empire-lesson` skill).

## Git and commits

Commit immediately: `ops/`, `intel/`, `reports/`, `empire/`, `HANDOFF.md`. Edit freely but wait for the Commander's approval before committing: `strategy/`, `AGENTS.md`, `README.md`, `GLOSSARY.md`, `.agents/skills/`. Push after every commit.

Use lowercase multi-line commit messages with a semantic prefix:

```text
intel: scan G5:316 neighbours

- explanation 1
- explanation 2
```

Prefixes: `intel:`, `ops:`, `empire:`, `report:`, `handoff:`, `strategy:`, `skills:`, `docs:`.

## Adding new skills

Write skills with the `writing-for-agents` skill. Create the skill under `.agents/skills/<skill-name>/SKILL.md`, then add a symlink so Claude Code picks it up automatically:

```bash
ln -s ../../.agents/skills/<skill-name> .claude/skills/<skill-name>
```

Stage the symlink with `git add .claude/skills/<skill-name>` (not the file inside it).
