---
name: empire-research
description: Run one research round as a sub-agent — re-read the game manual and the live rule tools, audit every claim in our docs and strategy against them, fix the docs, and propose better strategies with numbers. Use when the Commander asks for research, a "research round", or when a rule in our docs is suspected stale.
---

A **researcher** is a sub-agent (Agent tool, `subagent_type: general-purpose`, `model: opus`, `run_in_background: true`) with one round of work and a report. It reads the game, never plays it: only read-only MCP calls (`codex`, `combat_rules`, `changelog`, `research_tree`, `research_levels`, `empire_overview`, `server_stats`, `leaderboard`, `quests`); never `galaxy` (costs deuterium), never a spend, dispatch, message or queue call. It reports to the Lieutenant, never to the Commander.

1. **Number the round.** `N` = 1 + the count of files in `reports/research/`. Create `reports/research/<YYYY-MM-DDTHH-MM>Z_round-<N>.md` from the template with `status: running`.
2. **Spawn** with the brief below as the whole prompt (a researcher gets no other context); put the agent id in the file.
3. **On the report:** the researcher has written the file itself. Read it. Then:
   - `docs/`, `GLOSSARY.md` edits it made → check them against its cited sources, commit `docs: research round <N> — <what>`.
   - `strategy/` and skill edits it proposes → it wrote them as diffs in the report, never applied; put every proposal to the Commander in chat (mechanism, evidence, expected gain, recommendation), commit only what the Commander approves.
   - Set `status: done | failed`, commit `report: research round <N>`.
   - Print the report's *Findings* and *Proposals* sections in chat.

A round is complete when every claim the researcher flagged has a quoted source on both sides, every proposal carries a number from `codex` or the manual, and the report file is committed.

## Brief — the sub-agent prompt

```markdown
You are the researcher of yabepa's empire in terminal.army, working in the repo at <repo path>. You read the game's rules and our own documents, and you make our documents right and our strategy better. You do not play: the only MCP tools you may call are read-only (`mcp__commander__codex`, `combat_rules`, `changelog`, `research_tree`, `research_levels`, `empire_overview`, `server_stats`, `leaderboard`, `quests`). Never call `galaxy` (it costs deuterium) and never any call that builds, researches, dispatches, messages or joins.

ROUND <N>. Write everything into `<report path>` (template already there); no other file in `reports/`.

1. SOURCES. Refresh the manual: run `docs/game/fetch.sh` (needs curl + pandoc; if it fails, fetch https://docs.terminal.army/ , /mechanics/ , /commands/ , /commander/ with WebFetch and save nothing — read them). Then call `changelog`, `combat_rules`, `research_tree`, `codex` (for every building and technology we own, at our next level: `empire_overview` lists what we own). These are the truth; our documents are the claims.
2. CLAIMS. Read `strategy/DOCTRINE.md`, every file in `strategy/decisions/`, `strategy/LESSONS.md`, `strategy/STANDING_QUESTIONS.md`, `docs/mcp/COMMANDER.md`, `GLOSSARY.md`, `empire/research.md`, and the skills `.agents/skills/empire-farm/SKILL.md`, `empire-colonize`, `empire-spy`, `empire-raid`, `terminal-army`. For every sentence that states a game rule, a number or a formula: find it in the sources. Three outcomes, each recorded in the report:
   - CONFIRMED: source agrees — one line, the source.
   - WRONG: source disagrees — quote both, and fix it if the file is `docs/`, `GLOSSARY.md` or `empire/research.md` (edit in place, cite the source in the edit); if the file is under `strategy/` or `.agents/skills/`, write the exact replacement as a diff block in the report and touch nothing.
   - UNSOURCED: the sources say nothing — mark it; say what would settle it.
3. GAPS. Every mechanic in the sources that our documents never use and that would change what we build, research, colonise, defend or send — a formula, a threshold, a tool parameter, a changelog entry since 2026-09-11. For each: the mechanic (quoted), what we do today (quoted from our docs), what we would do instead, the expected gain in numbers (`codex` on our own planets — production per hour, cost, payback hours, or time saved), and the risk.
4. PROPOSALS. Rank the gaps and the WRONG strategy claims by expected gain per hour of the empire's production. For each of the top five write: mechanism, evidence (source quotes), the exact `strategy/` or skill diff, the expected gain, the recommendation (adopt / test / reject) and why. Any proposal that spends dark matter, attacks a player, sends a message, or abandons a planet is marked COMMANDER-ONLY.
5. FINISH. Set `status: done` in the report frontmatter, fill `agent:`, `sources_read:`, `claims_checked: <confirmed>/<wrong>/<unsourced>`. Do not commit; do not touch `HANDOFF.md`, `PLAN.md`, `ops/`, `intel/`, `empire/planets/`. End with the report's Findings and Proposals sections as your final message.

Finished means: every rule-stating sentence in the files listed has one of the three verdicts, every proposal has a number, and the report reads without you.
```

## Template — `reports/research/<ts>_round-<N>.md`

```markdown
---
round: <N>
status: running | done | failed
agent: <id>
opened: <ts>
closed: <ts>
sources_read: <manual pages, MCP tools, changelog entries>
claims_checked: <confirmed>/<wrong>/<unsourced>
---
## Findings
### Wrong (fixed in docs/ — or diff proposed for strategy/)
### Unsourced
### Confirmed
## Gaps
## Proposals (ranked)
## Open questions for the Commander
```
