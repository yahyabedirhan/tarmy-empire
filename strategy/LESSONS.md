# Lessons

Numbered, never deleted; a superseded lesson gets a `superseded-by:` line. Each links to the event that taught it. New entries through the `empire-lesson` skill.

## L1 — Energy before ore (2026-09-06)
Queued MM6→7 and CM3→4 before the solar surplus existed; factor fell 0.97→0.83 and every mine on the planet slowed for hours. Source: `archive/STRATEGY.md`. Rule: DOCTRINE → Energy first.

## L2 — A full pool is a leak (2026-09-09 → 11)
The colony sat at its metal cap while the capital held 447k idle metal and an empty queue; days of production were discarded. Source: `archive/COLONY_GROWTH_STRATEGY.md`, `reports/status/2026-09-11T08-00.md`. Rule: DOCTRINE → Never a full pool, Never an empty queue.

## L3 — A colony ship without the licence is a lost ship (2026-09-09)
Two colony ships were sent to 5:316:2 and 5:317:12 with astrophysics 2 (allowance: 2 planets). Both arrived, neither founded a planet, one earlier attempt at 5:317:8 failed the same way. Source: `archive/COLONY_GROWTH_STRATEGY.md`. Rule: DOCTRINE → Colonize (research must be *completed* before launch); `docs/mcp/COMMANDER.md` troubleshooting.

## L4 — One scan, then simulate, then fly (2026-09-08)
2 light fighters were sent at 5:316:7 (nash1999: 3 rocket launchers + 16 light fighters, 432k resources) on the strength of a resource total; both were lost for nothing. Source: `archive/ATTACK.md`. Rule: DOCTRINE → Raid (zero expected losses in `simulate_combat`). The same day a raid on 5:316:8 (Saeed2) "won" 50 resources: an undefended target is not a target unless it holds loot.

## L5 — Crystal is the empire's limiter (2026-09-07)
Seven researches in 46 minutes took crystal from 214k to 8k and cascaded every crystal-priced build into failure. Source: `archive/OPERATIONS_LOG.md`. Rule: `empire/research.md` prices a research chain in full before starting it; crystal-world is the second colony role (decision 002).

## L6 — Session snapshots are not doctrine (2026-09-11)
Five sessions wrote their live status into the strategy files; by session six nobody could tell rule from snapshot. Rule: `AGENTS.md` → Records (one file per event, doctrine separate from state).

## L7 - A soldier dies with the connection (2026-09-11)
Both haiku soldiers were killed by the harness watchdog (600 s without progress) during an hour-long MCP hang, mid-mission. The colonize soldier had already dispatched; the ships soldier had queued 2 of 3 batches. Source: `ops/missions/2026-09-11T08-30_*.md`. Rule: after any soldier failure the Lieutenant re-reads state before redoing anything (a dead soldier may have acted); briefs must be idempotent (check before each spend). No doctrine change.

## L8 — Protection is invested score, and our own growth closes targets (2026-09-11)
Assumed the 5× rule counted held resources (our MCP doc said so) and planned raids on 5:316:8 / :5 / :7 for ~250k loot. All three launches were refused: attacker 1582→1685 vs invested 41 / 114 / 187 — the rule counts only resources *spent* (`docs/game/mechanics.md` → Protection). Between planning (score 712) and launch, 60 light fighters and four researches tripled our score and lifted the floor above every neighbour. Source: `ops/attacks/2026-09-11_G5-S316-P8_Saeed2.md`, `ops/attacks/2026-09-11_G5-S316-P7_nash1999.md`. Rule: DOCTRINE → Raid gains "target invested score ≥ our score ÷ 5, checked at planning *and* at launch; a refused launch is free intel — try it before any other check". Raid with the fleet you have before you grow the fleet or the score.

## L9 — Above the floor, light fighters do not raid (2026-09-11)
The only targets above our 5× floor (Kara6 5:310:8, yuxuanz4 5:311:7, hina_ito 5:312:10) sit behind 30–82 rocket launchers, 20–40 light lasers, heavy lasers, ion cannons and a small shield dome. 62 LF + cargo vs Kara6's wall: draw 10/10, 36 LF lost (~186k) for nothing. Source: `ops/attacks/2026-09-11_G5-S316-P7_nash1999.md` (debrief sim). Rule (Commander, 2026-09-11T15:15Z): **raiding is parked**; growth first (astro 5, mines), defence second where a planet is exposed. No new warships until the Commander reopens raiding; `empire/research.md` row 5 (impulse 4 / cruisers) drops below rows 8–9. Revisit when astro 5 is done or a target ≥ our score ÷ 5 appears with a wall the current fleet beats.

