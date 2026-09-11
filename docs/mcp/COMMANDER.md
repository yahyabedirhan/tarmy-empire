# The commander MCP — field manual

The `commander` MCP (server name `commander`, tools `mcp__commander__*`) is the only way we touch the game. Full official description: `docs/game/commander.md`. The game's own playbook for it (kept current by `tarmy commander`): `.agents/skills/terminal-army/SKILL.md`. This file is the short version plus what we learned the hard way.

## Tools by what they can lose

| Tier | Tools | Undo |
|---|---|---|
| read | `empire_overview` `planet_detail` `production_report` `build_queue` `research_levels` `research_tree` `codex` `units` `quests` `fleets` `reports` `report_detail` `galaxy`* `standing` `leaderboard` `server_stats` `combat_rules` `simulate_combat` `defence_summary` `dark_matter` `messages` `read_message` `conversation(s)` `alliance_chat` `alliances` `alliance_detail` `alliance_standing` `allied_defenses` `acs_groups` `moon_status` `next_event` `changelog` `preview_abandon_planet` | nothing changes |
| spend | `upgrade_building` `queue_research` `build_ships` `build_defense` `cancel_build` `rush_build` `boost_production` `rename_planet` | `cancel_build` refunds a queued level in full, a batch's unbuilt share |
| commit | `dispatch_fleet` `recall_fleet` `launch_missiles` `phalanx_scan` `jump_gate` `send_message` `send_alliance_message` `delete_message` `join_alliance` `leave_alliance` `create_alliance` `create_acs` `invite_acs` `join_acs` `mark_notices_read` `abandon_planet` | none by waiting; `recall_fleet` brings a fleet home |

\* `galaxy` for a system other than your own costs 10 deuterium per jump.

## Call shapes that matter

- `codex(key, level?, planet_id?)` — price, time, prerequisites and effect of the *next* level for *this* planet. Always before `upgrade_building` / `queue_research` / `build_ships`.
- `upgrade_building(building, count?, planet_id?)` — queue holds 5, each level charged when queued. Read `queued` and `stopped_after`.
- `queue_research(tech, planet_id?)` — the parameter is **`tech`** (not `key`, `research_key`, `target_level`). Research is account-wide; the lab used is the highest one you own.
- `build_ships(key, count, planet_id?)` — ships *and* defence. Solar satellites and crawlers are buildings: `upgrade_building`.
- `dispatch_fleet(mission, target_galaxy, target_system, target_position, ships, cargo?, speed_percent?, origin_planet_id?, target_moon?, hold_hours?)` — missions: `attack transport deploy colonize espionage recycle defend`. Say arrival time before sending; `galaxy` gives the reference flight time for one small cargo.
- `next_event(timeout_seconds ≤ 300)` — returns immediately if events are queued, else blocks. Events seen: `queue.completed`, `fleet.dispatched`, `fleet.incoming` (hostile launch, brief payload → read `fleets`), `fleet.returned`, `fleet.combat`, `planet.attacked`, `alliance.message.received`, `state.changed` (any POST by any session on this account — the Commander playing in the TUI — their decision, not a conflict). One stream per account: an event consumed by one agent is gone for the others, so soldiers treat `next_event` as a sleep and re-read state. Resource growth emits nothing: compute the ETA from `production_report` and check then.
- `empire_overview` — `production` and `build_queue` inside it are for the **first planet only**; pass `planet_id` to `production_report` / `build_queue` / `planet_detail` for others.
- `quests` — reading it pays finished rungs. Read it after any completion.

## Hard rules of the server (refusals you will meet)

- Planet count ≤ `1 + ceil(astrophysics / 2)`; colonisable positions depend on astrophysics level (`codex("astrophysics")` → `effect`). A colony ship arriving at a slot you are not allowed lands nothing and is wasted.
- Attack refused when attacker score ≥ 5× defender effective score (ladder score + held resources/1000). Six attacks per planet per 24 h.
- Fleet slots = computer technology + 1.
- Build queue: 5 items. Lab upgrade and research block each other on the same planet.

## Troubleshooting

| Symptom | Cause | Do |
|---|---|---|
| `queue_research` "unexpected additional properties" | wrong parameter name | use `tech` |
| colony ship arrived, no planet | astrophysics allowance full or position not allowed | check `codex("astrophysics")` before every colonize |
| `upgrade_building` returns `stopped_after` < count | resources ran out mid-batch | read `queued`; do not re-send the same count |
| attack refused with two scores | 5× protection rule | pick another target; log the refusal in the campaign file |
| `queue_research` http 409 "already researching" | one research at a time, empire-wide | `research_tree` → `in_progress` for what and when |
| `build_ships` http 409 "5 builds running" | buildings, ships and defence share one 5-slot queue per planet | wait for `queue.completed` or `cancel_build` |
| `next_event` returns `[]` | nothing happened within the timeout | not a completion; compute the ETA and wait again |
| tool absent from the list | tier not handed over (`tarmy commander --allow …`) | tell the Commander; do not keep calling it |
| numbers in a stale espionage report | scan is old | re-scan before an attack |
| production lower than the mines suggest | production factor < 1 | `production_report`, then solar plant / fusion first |

Anything not in this table: `docs/game/commander.md`, then `.agents/skills/terminal-army/SKILL.md`, then escalate with the exact call and the exact error.
