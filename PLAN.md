# Plan — next 24 h from 2026-09-16T19:05Z

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC; each line is a wake with the action that fires on it. Done lines are dropped, not kept.

| when | where | action | gate |
|---|---|---|---|
| 19:17Z | capital | colony ship lands (232793) — park it | — |
| 19:21Z | :10 | metal_storage 6 lands (cap 2.35M) | — |
| ~21:00Z, then every ≤ 2 h | :10 / :9 / :3 | crystal ≥ ~85k → `codex` crystal_mine + satellites → queue (payback ~50 h < 58 h clock) | crystal on hand |
| every cycle | all | `capcheck.py` stock/cap, flag ≥ 80 % (L16) | — |
| from 09-17 ~12:00Z | :14 → capital | 1 LC × 25k D hop so the capital holds ≥ 50k D for the planet-6 bootstrap | :14 deut ≥ 25k |
| before 09-17 18:28Z | Commander | pick planet 6 slot → write `ops/colonies/G5-S316-P<slot>.md` | Commander answer |
| 09-17 18:28:15Z | capital | astro 9 lands → `codex astrophysics` = 6 planets → `dispatch_fleet colonize` (colony ship, speed 100 %) → bootstrap cargo from :10/:3 (metal) + :14 (deut) per `empire-colonize` | slot file exists |
| after colonize | research | slot idle → next research per `empire/research.md` (fillers: laser 9, weapons 7, armour 9; astro 11 only on a Commander yes) | — |
| cycle 38 | — | status report; alliance skim (four things only) | — |

Idle on purpose: raids (parked until planet 6, Commander 09-15 08:40Z); alliance chat; astro 11 (no Commander yes); RL walls on colonies (idle-metal question open).
