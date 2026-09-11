# Handoff — 2026-09-11T10:20Z

## Do this first
Run `/empire-cycle`. Shielding 2 landed ~10:13Z → `queue_research(tech="shielding")` then `build_ships(key="recycler", count=2)` at the capital (planet 5080).

## Where we are
- 3 planets: capital 5:316:12 GROWING, 5:316:10 GROWING (queue full to 11:39Z), **5:316:9 BOOTSTRAP** (id 5587, 169 fields, founded 09:22Z).
- Transport 55k M / 8k C / 4k D lands on 5:316:9 at 10:25Z (fleet 55318).
- Capital queue: solar 16 10:21Z, MM14 10:38Z, **60 LF 13:50Z**, 3 LC 14:19Z. One slot free.
- Score 843, rank 946. Saeed2 raid approved (decision 004, 5 % loss rule); flies after a fresh scan once the LF exist.
- Goal: decision 002 (cluster expansion) + first raid income; rulebook `strategy/DOCTRINE.md`.

## Next actions
1. 10:13Z+: shielding 3 + 2 recyclers at the capital (`empire/research.md`, ladder `salvage_crew`).
2. 10:26Z: 5:316:9 builds from the landed cargo — metal 6–8, crystal 2–5, metal storage 1, solar to keep factor 1 (`empire-colonize` bootstrap order; `empire/planets/G5-S316-P9.md`).
3. Next transport to 5:316:9 — capital crystal is ~37k, so build 2 small cargo on 5:316:10 (shipyard 2, 113k C there) and ship crystal 10 → 9 directly.
4. Research after shielding 3: energy 5 → impulse 4 → ion 3 (`empire/research.md`).
5. 13:50Z: `empire-spy` 5:316:8 and 5:316:5 → `empire-raid` Saeed2 (`ops/attacks/2026-09-11_G5-S316-P8_Saeed2.md`), then caioc.
Later: neighbourhood-watch scans of 5:310–322 (decision 005) — none done yet beyond 5:316.

## Questions for the Commander
- none (answered today: 5 % loss rule, TUI actions are the Commander's, push after every commit, repo public).

## Uncommitted strategy changes awaiting approval
- none. Note: L7 (soldier watchdog lesson) went out inside a data commit ("ops: planet 3 founded"); revert if unwanted.

## What changed this session
- Workspace rebuilt: `README.md`, `AGENTS.md`, `strategy/`, `empire/`, `ops/`, `intel/`, 9 `empire-*` skills; public repo pushed.
- Planet 3 founded by a haiku soldier 20 s after astrophysics 3 landed (`ops/missions/2026-09-11T08-30_colonize-5-316-9.md`).
- Both soldiers later died in a ~1 h MCP hang (harness 600 s watchdog) → L7: re-read state after any soldier failure; briefs check before each spend.
- `next_event` is one shared stream per account; soldiers sleep on it and re-read state. Buildings/ships/defence share one 5-slot queue. Recycler needs shielding 2.
- Neighbours scanned: Saeed2 and caioc inactive farms (~240k loot), nash1999 idle but fleeted (`intel/targets/`); BJACK chat digest and slot temperatures in `ops/diplomacy/`, `intel/notes.md`.
