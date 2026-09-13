# Plan — next 24 h from 2026-09-13T19:45Z

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC; each line is a wake with the action that fires on it. Done lines are dropped, not kept.

| when | where | action | gate |
|---|---|---|---|
| 19:48:48Z | 5:316:14 | fleet 65851 colonize lands: founded → BOOTSTRAP (`empire-colonize`), feed from 5:316:10; bounced → ship home, wait for astro 7 | cap formula 1 + ceil(astro ÷ 2) |
| ~20:12Z | 5:316:3 | crystal 17 (88.5k M / 44.3k C, +1.5k C/h); energy headroom 214 covers +124 | M ≥ 88.5k, C ≥ 44.3k |
| ~23:30Z | 5:316:9 | 4 satellites (8k C / 2k D) then crystal 17 (88.5k/44.3k) | C ≥ 52.3k |
| ~00:00Z 09-14 | 5:316:10 | 4 satellites then crystal 17 (88.5k/44.3k) | C ≥ 52.3k |
| 03:00–10:00Z | capital, 5:316:9 | metal-only sinks: deut 13 / deut 11 only if `codex` payback beats astro-7 delay; else rocket launchers (decision 006 floor) | no crystal spent after ~06:00Z |
| ~10:00–12:00Z | colonies → capital | sweep crystal + deuterium (3 LC at 5:316:9/10, 1 LC + 4 SC at 5:316:3) | deut within ~2 h of 115k |
| ~12:30Z | capital | queue astrophysics 7 (115k/230k/115k); `codex` for the exact landing time | 115k D empire-wide |
| ~18:00Z | capital → 5:316:14 | colony ship colonize (if it bounced on 09-13); planet 5 founded ~18:30Z, then feed + first mines | astro 7 landed |
| every 4th cycle | — | status report (`empire-status`); read alliance chat when credits allow | — |

Idle on purpose: research slot (crystal is astro 7's); capital build queue (crystal-priced, worse return than colonies — decision 008).
