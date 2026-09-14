# The commander MCP — field manual

The `commander` MCP (server name `commander`, tools `mcp__commander__*`) is the only way we touch the game. Full official description: `docs/game/commander.md`. The game's own playbook for it (kept current by `tarmy commander`): `.agents/skills/terminal-army/SKILL.md`. This file is the short version plus what we learned the hard way.

## Tools by what they can lose

| Tier | Tools | Undo |
|---|---|---|
| read | `empire_overview` `planet_detail` `production_report` `build_queue` `research_levels` `research_tree` `codex` `units` `quests` `fleets` `reports` `report_detail` `galaxy`* `standing` `leaderboard` `server_stats` `combat_rules` `simulate_combat` `defence_summary` `dark_matter` `messages` `read_message` `conversation(s)` `alliance_chat` `alliances` `alliance_detail` `alliance_standing` `allied_defenses` `acs_groups` `moon_status` `next_event` `changelog` `preview_abandon_planet` | nothing changes |
| spend | `upgrade_building` `queue_research` `build_ships` `build_defense` `cancel_build` `rush_build` `boost_production` `rename_planet` (free since v0.15.4, once a day per world) | `cancel_build` refunds a queued level in full, a batch's unbuilt share |
| commit | `dispatch_fleet` `recall_fleet` `launch_missiles` `phalanx_scan` `jump_gate` `send_message` `send_alliance_message` `delete_message` `join_alliance` `leave_alliance` `create_alliance` `create_acs` `invite_acs` `join_acs` `mark_notices_read` `abandon_planet` | none by waiting; `recall_fleet` brings a fleet home |

\* `galaxy` for a system other than your own costs 10 deuterium per jump.

## Call shapes that matter

- `codex(key | keys[], level?, planet_id?)` — price, time, prerequisites and effect of the *next* level for *this* planet. Pass `keys` to price a whole build order in one call (v0.15.0). Always before `upgrade_building` / `queue_research` / `build_ships`.
- `upgrade_building(building, count?, planet_id?)` — the *construction* line holds 5 building levels, each charged when queued. Read `queued` and `stopped_after`. Every row also reports `energy_after`, `production_factor_after` and `costs_production` when the level would slow the planet's mines (v0.15.0).
- `queue_research(tech, planet_id?)` — the parameter is **`tech`** (not `key`, `research_key`, `target_level`). Research is account-wide; the lab used is the highest one you own.
- `build_ships(key, count, planet_id?)` — ships *and* defence, into the planet's own *shipyard* line (5 batches, runs beside the construction line — v0.15.3). Solar satellites and crawlers are buildings: `upgrade_building`. Lock: no batch can be ordered while the shipyard or nanite factory is upgrading, and neither can be upgraded while a batch is queued.
- `dispatch_fleet(mission, target_galaxy, target_system, target_position, ships, cargo?, speed_percent?, origin_planet_id?, target_moon?, hold_hours?)` — missions: `attack transport deploy colonize espionage recycle defend`. Say arrival time before sending; `galaxy` gives the reference flight time for one small cargo. An attack on an alliance member is refused by name unless `confirm_ally` is set (Commander v1.5.3, changelog v0.15.5 — the running MCP process may be older: `dark_matter`/`rename_planet` descriptions tell which).
- `next_event(timeout_seconds ≤ 3600, kinds?)` — returns immediately if events are queued, else blocks (default 30 s, up to an hour since v0.15.0; keep it under the client's own request timeout). `kinds=["queue.completed"]` sleeps through everything else, but anything that arrived is still returned. Events seen: `queue.completed`, `fleet.dispatched`, `fleet.incoming` (hostile launch, brief payload → read `fleets`), `fleet.returned`, `fleet.combat`, `planet.attacked`, `alliance.message.received`, `state.changed` (any POST by any session on this account — the Commander playing in the TUI — their decision, not a conflict). One stream per account: an event consumed by one agent is gone for the others, so soldiers treat `next_event` as a sleep and re-read state. Resource growth emits nothing: compute the ETA from `production_report` and check then.
- `empire_overview` — the top-level `production` and `build_queue` are the first planet's, but `planet_detail[]` carries **every** planet with its own `production` and `build_queue` (v0.15.0), so one call covers the empire. `production.deuterium_per_hour` is *net of the fusion reactor's burn*. `universe` gives the speeds (Genesis: economy 5, fleet 4, research 5).
- `quests` — reading it pays finished rungs (so does `empire_overview`). Read it after any completion.
- `leaderboard(limit ≤ 500, offset)` — paged; `standing` is one call for our own band.

## Hard rules of the server (refusals you will meet)

- Planet count ≤ `1 + ceil(astrophysics / 2)`; colonisable positions depend on astrophysics level (`codex("astrophysics")` → `effect`). A colony ship arriving at a slot you are not allowed lands nothing and is wasted.
- Attack refused when attacker score ≥ 5× defender **invested** score (resources spent on buildings/ships/research; held resources do NOT count — `docs/game/mechanics.md` → Protection). The refusal names both scores, so a refused launch is free intel. Six attacks per planet per 24 h.
- Fleet slots = computer technology + 1.
- Two build lines per planet since v0.15.3: **construction** (5 building levels) and **shipyard** (5 ship/defence batches), running side by side. A cancel closes the gap in its own line only. Locks: shipyard and nanite factory cannot be upgraded while a batch is queued, and no batch while either is upgrading. Research: **one at a time account-wide, no queue** (`queue_research` while one runs → http 409); the lab used is the highest in the empire (manual → Build & research time). A research lab cannot be upgraded while a research *started from it* runs, and that planet cannot start research while its lab upgrades.

## Troubleshooting

| Symptom | Cause | Do |
|---|---|---|
| `queue_research` "unexpected additional properties" | wrong parameter name | use `tech` |
| colony ship arrived, no planet | astrophysics allowance full or position not allowed | check `codex("astrophysics")` before every colonize |
| `upgrade_building` returns `stopped_after` < count | resources ran out mid-batch | read `queued`; do not re-send the same count |
| attack refused with two scores | 5× protection rule | pick another target; log the refusal in the campaign file |
| `queue_research` http 409 "already researching" | one research at a time, empire-wide | `research_tree` → `in_progress` for what and when |
| `build_ships` http 409 "5 builds running" | the *shipyard* line already holds 5 batches (buildings no longer count, v0.15.3) | wait for `queue.completed` or `cancel_build` |
| `build_ships` refused while shipyard/nanite upgrading, or `upgrade_building(shipyard)` refused while a batch is queued | shipyard lock (v0.15.3) | finish or cancel the other side first |
| colony ship sent for planet N+1 but astro level only raised the position range | planets allowed = `1 + ceil(astro/2)`: odd levels add a planet, even levels only widen positions (astro 8 → still 5 planets, astro 9 → 6) | `codex("astrophysics", level)` → `effect.planets_allowed` before planning |
| `next_event` returns `[]` | nothing happened within the timeout | not a completion; compute the ETA and wait again |
| tool absent from the list | tier not handed over (`tarmy commander --allow …`) | tell the Commander; do not keep calling it |
| numbers in a stale espionage report | scan is old | re-scan before an attack |
| production lower than the mines suggest | production factor < 1 | `production_report`, then solar plant / fusion first |

Anything not in this table: `docs/game/commander.md`, then `.agents/skills/terminal-army/SKILL.md`, then escalate with the exact call and the exact error.
