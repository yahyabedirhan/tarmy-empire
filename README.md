# tarmy-empire

Command post for yabepa's terminal.army empire. Humans start at `AGENTS.md`; agents start at `HANDOFF.md`.

```
AGENTS.md            chain of command, MCP rules, record and commit rules (CLAUDE.md is a symlink to it)
HANDOFF.md           the live state of the campaign: goal, in-flight missions, open questions. Rewritten every cycle.
GLOSSARY.md          every term used in this repo, one line each
README.md            this map

strategy/            WHY we play the way we do — changes need the Commander's approval before commit
  DOCTRINE.md          the standing rules: when to build, research, colonize, attack, fortify, wait
  ALLIANCE.md          diplomacy posture
  LESSONS.md           numbered lessons, each linked to the event that taught it
  decisions/           one file per high-level decision: context, options considered, choice, reasoning, revisit-when

docs/                reference — read on demand
  game/                verbatim copies of the terminal.army manual (mechanics, commands, commander, index) + SOURCES.md
  mcp/COMMANDER.md     the commander MCP: tools by tier, call shapes, troubleshooting

empire/              WHAT we own
  planets/<COORD>.md   one file per owned planet: role, tags, state machine, why we took it, plan, state history
  research.md          research order and the reason for it

ops/                 WHAT we did — one short file per event, template in the owning skill
  attacks/             one file per raid campaign (a campaign = all sorties against one target under one plan)
  colonies/            one file per colonisation attempt
  missions/            one file per soldier mission (the brief + the report)
  diplomacy/           one file per conversation with another player

intel/               WHAT we know about others
  targets/<COORD>_<owner>.md   one file per foreign planet: latest scan block + scan history
  players/<name>.md            one file per player: activity pattern, alliance, planets, verdict

reports/status/      snapshots written by the `empire-status` skill, never hand-edited

archive/             the pre-2026-09-11 files, kept for history, not for guidance

.agents/skills/      the skills (Claude Code reads them through symlinks in .claude/skills/)
```

Naming: coordinates are written `G5-S316-P12` in file names and `5:316:12` in text. Timestamps are UTC ISO-8601 (`2026-09-11T08:00Z`).

## Skills

| Skill | Invoked by | Does |
|---|---|---|
| `empire-cycle` | Lieutenant, on a loop | one heartbeat: read the empire, run every planet through its state, act, record, hand off |
| `empire-status` | Commander or Lieutenant | write a status snapshot to `reports/status/` and summarise it |
| `empire-farm` | `empire-cycle` | the build/research decision procedure for one planet |
| `empire-colonize` | `empire-cycle` or Lieutenant | pick a slot, send the ship, bootstrap the colony, record it |
| `empire-spy` | `empire-cycle` or Lieutenant | scan targets, update `intel/` |
| `empire-raid` | Lieutenant | plan, simulate, execute and record a raid campaign |
| `empire-soldier` | Lieutenant | write a mission brief and spawn a sub-agent on it |
| `empire-lesson` | Lieutenant | record a lesson and propose the doctrine change it implies |
| `empire-handover` | Lieutenant | rewrite `HANDOFF.md` for the next session |
| `terminal-army` | any | the game's own MCP playbook (vendored; refresh with `tarmy commander`) |
