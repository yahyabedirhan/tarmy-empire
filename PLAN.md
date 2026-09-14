# Plan — next 24 h from 2026-09-14T08:12Z

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC; each line is a wake with the action that fires on it. Done lines are dropped, not kept.

| when | where | action | gate |
|---|---|---|---|
| 08:12–12:00Z | all | nothing queued: stocks accrue for astro 7 (deut 87k at 08:10Z, +6.3k/h) | — |
| ~12:00Z | colonies → capital | sweep to 5:316:12: 5:316:9 2 LC + 2 SC (all C + D), 5:316:10 2 LC (all C + D), 5:316:3 1 LC + 4 SC (crystal only). Capital needs 230k C (has 78k) + 115k D (has 33.5k) | deut empire-wide ≥ ~110k |
| ~12:40Z | capital | queue astrophysics 7 (115k/230k/115k); `codex astrophysics` for the landing time (~5.5 h → ~18:15Z) | sweep landed, D ≥ 115k |
| 12:45Z → | colonies | release crystal-priced builds: 5:316:9 / :10 metal 20 (133k/33k + satellites), 5:316:3 crystal 18 (`codex` first); capital idle (008) | astro 7 queued |
| ~18:15Z | capital → 5:316:14 | colony ship colonize (re-check `galaxy 5 316` first; fallback 5:316:13); founded ~18:40Z → BOOTSTRAP: feed 3k M / 1k C / 500 D from 5:316:10, first mines (`empire-colonize`) | astro 7 landed |
| ~18:45Z → | 5:316:14 | bootstrap builds every wake; planet file `empire/planets/G5-S316-P14.md` | founded |
| every 4th cycle | — | status report (`empire-status`); read alliance chat; file the 5:315:10 probe report in `intel/` | — |

Idle on purpose: research slot until astro 7; capital build queue (crystal-priced, worse return than colonies — decision 008).
