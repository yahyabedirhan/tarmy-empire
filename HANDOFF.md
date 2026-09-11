# Handoff — 2026-09-11T12:40Z

## Do this first
Run `/empire-cycle`. First: **AGENTS.md needs the autonomy-language edit** — the Commander asked (this session) for explicit language making the Lieutenant act autonomously, running the loop until interrupted, once a session starts; that edit was deferred to a fresh agent and never made. Use the `writing-for-agents` skill, then get the Commander's approval before committing (`AGENTS.md` → Git rules) since it changes standing behaviour.

## Where we are
- 3 planets, all GROWING: capital 5:316:12 (research shielding 4 → 12:49:13Z; ships light_fighter 60→13:50:31Z, large_cargo 3→14:19:19Z, recycler 2→14:44:55Z; buildings crystal_mine 13→15:09:14Z, robotics_factory 4→15:11:43Z), 5:316:10 (crystal_mine 13 → 12:46:54Z), 5:316:9 (solar 9, metal_mine 10, crystal_mine 7 → 12:47:14Z).
- No hostiles, no fleets in the air, no running missions.
- Goal: decision 002 (cluster expansion, next slot 5:316:3, blocked on astrophysics 5) + first raid income; rulebook `strategy/DOCTRINE.md`.

## Next actions
1. AGENTS.md autonomy edit (see *Do this first*) — the actual trigger: this cycle found both the capital's research queue (idle ~23 min after ion 3 landed) and 5:316:9's build queue (idle ~20 min) sitting empty with nobody watching between cycles. Concrete case for why the loop needs to run itself.
2. 12:46–12:47Z: both colonies' queues empty — `production_report` + `empire-farm` for each.
3. ~13:50:31Z: light_fighter 60 exist at the capital — fresh-scan 5:316:8 and 5:316:5, then `empire-raid` Saeed2 (`ops/attacks/2026-09-11_G5-S316-P8_Saeed2.md`), then caioc.
4. Astrophysics push: build cargo capacity and transport crystal 5:316:10 → capital (capital has ~23k, need ~118k total for astro 4+5) — see `strategy/STANDING_QUESTIONS.md` → *When are we going to expand to a new planet?* for the full numbers.
5. Resume the neighbourhood watch (systems 314–322) once espionage probes exist — build at 5:316:10's shipyard once free.
Later: 5:316:10 has zero defence sitting on ~280k in resources — queue rocket launchers there (`strategy/STANDING_QUESTIONS.md` → defence answer).

## Questions for the Commander
- none

## Uncommitted strategy changes awaiting approval
- none (AGENTS.md autonomy edit not yet made — see *Do this first*, not "uncommitted" since it doesn't exist yet)

## What changed this session
- Added [`strategy/STANDING_QUESTIONS.md`](strategy/STANDING_QUESTIONS.md): live answers to the Commander's recurring questions (current focus, next expansion, next attack, defence readiness), to be revised every cycle. Commit `827d6c2`.
- Confirmed the research queue runs independent of the build/ship queue (queued ion 3 while the ship queue was mid-build) — see [G5-S316-P12.md](empire/planets/G5-S316-P12.md), commit `434f07c`.
- Found and fixed two idle queues on a pre-handoff check rather than leaving them for the next cycle: capital research (idle ~23 min) and 5:316:9 build queue (idle ~20 min) — commits `7284c66`, `7e2243b`. This is the concrete case behind the Commander's autonomy request below.
- Commander asked to make the Lieutenant act autonomously (run the loop until interrupted) once a session starts, with the rule made explicit in AGENTS.md via `writing-for-agents` — deferred to the next session, see *Do this first*.
