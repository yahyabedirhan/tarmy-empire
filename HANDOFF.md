# Handoff — 2026-09-11T18:25Z

## Do this first
Run `/empire-cycle`. Then read `strategy/decisions/009-growth-engine-expansion-first.md` (the engine and the forecast) and `010-alliance-trading.md` (waiting on the Commander). The astro-5 clock is the plan: fill every queue with the best-returning mine in the empire (colonies first), sweep crystal to the capital when 75k exists, queue astro 5, send the colony ship to 5:316:3 when it lands.

## Where we are
- Capital (5080): fusion 5 + satellite 6 landed 18:18Z → factor back to 1 (was 0.94 unnoticed). Laser 6 lands 18:24:18Z — research slot must be refilled at once (computer 6 if astro clock allows, else armour 7 / combustion 7 as metal-only fillers). ~20k metal / ~3k crystal / ~68k deut after the fixes. Fleet unchanged: 62 LF, 5 LC, 4 SC, 2 recyclers, 10 probes, 1 colony ship. Wall 16 RL + 2 LL.
- 5:316:10 (5288): fusion 4 + satellite landed 18:17Z (headroom ~145). Waiting for 39.4k metal → metal_mine 17 (~20:30Z). ~4k crystal left.
- 5:316:9 (5587): solar 14 lands 18:29:46Z, deut synth 1–4 by 18:30:42Z. Next: crystal_mine 11 (5.3k M / 2.6k C) at ~18:45Z when metal allows — best mine in the empire (5 h crystal payback) — then crystal 12, 13.
- Empire production 35.3k / 13.2k / 2.8k per hour. Score 2 141, rank 416. No hostile fleets. Astro 5: 37.5k/75k/37.5k; empire crystal ~26k.
- Strategy rewritten this session under the Commander's delegated authority (commit `strategy: expansion-first engine…`): decisions 008/009/010, five new doctrine rules, L10–L14, research order, both skills. The full BJACK chat (419–663) is digested in `ops/diplomacy/2026-09-11_BJACK-chat.md`.

## Next actions
1. 18:24Z laser 6 lands → `queue_research`: computer 6 (0/12.8k/19.2k) **only if** capital crystal ≥ 12.8k without delaying astro 5 past its ETA; otherwise armour 7 (64k metal — not yet affordable) or combustion 7 (25.6k metal / 38.4k deut) as the zero-crystal filler.
2. 18:30Z 5:316:9 queue empties → crystal_mine 11 as soon as metal ≥ 5.3k (≈18:45Z); keep queuing crystal 12/13 while payback < astro ETA.
3. ~20:30Z 5:316:10 metal ≥ 39.4k → metal_mine 17.
4. Astro clock: every cycle write ETA(astro 5) = max((75k − empire crystal) ÷ 13.2k/h, (37.5k − capital deut) ÷ …). When empire crystal ≥ 75k: sweep 5:316:10 and :9 crystal to the capital with the 5 LC (13 min flights), then `queue_research(astrophysics)`. Colony ship to 5:316:3 only after it *lands* (L3), per `empire-colonize`.
5. Capital wall: as the astro hoard grows past 150k on the capital, add rocket launchers (2k metal each) so wall value ≥ hoard ÷ 4.
6. No trades, no alliance chat messages (Commander 18:30Z). Deuterium for planet 5 comes from synthesizers on 5:316:9 and the capital only.
7. Neighbourhood watch resumes with **one probe per target** (L14) once crystal is slack — 19 targets listed in `ops/missions/2026-09-11T16-48_neighbourhood-watch-resume.md`.

## Questions for the Commander
- Decision 010 (trades): **rejected** 18:30Z. Closed.
- Confirm or amend decisions 008 and 009 (edited and committed under the authority granted 18:05Z).

## Uncommitted strategy changes awaiting approval
None — everything is committed under the delegated authority; the Commander's reply may reverse any of it.

## What changed this session
- Read the entire BJACK chat (200 messages) and every strategy/doc file; rewrote the growth strategy around the measured rules (lowest mine first, priced energy, astro clock, one-probe spy law, trade the metal surplus).
- Fixed the capital's energy factor (0.94 → 1), refilled the research slot, queued fusion/satellite at 5:316:10 for metal 17, solar 14 + deut 1–4 at 5:316:9.
- Formalized planet roles (008), forecast to planets 4/5/6 (009), proposed alliance trades (010).
