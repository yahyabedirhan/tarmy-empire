# Handoff — 2026-09-11T19:13Z

## Do this first
Run `/empire-cycle`. Then read `strategy/decisions/009-growth-engine-expansion-first.md` (the engine and the forecast) and `010-alliance-trading.md` (waiting on the Commander). The astro-5 clock is the plan: fill every queue with the best-returning mine in the empire (colonies first), sweep crystal to the capital when 75k exists, queue astro 5, send the colony ship to 5:316:3 when it lands.

## Where we are
- Capital (5080): fusion 5 + satellite 6 landed 18:18Z → factor back to 1 (was 0.94 unnoticed). Laser 6 landed 18:24Z; combustion 7 (zero crystal) researching → 19:51:04Z. ~0 metal / ~6k crystal / ~31k deut after paying it. Fleet unchanged: 62 LF, 5 LC, 4 SC, 2 recyclers, 10 probes, 1 colony ship. Wall 16 RL + 2 LL.
- 5:316:10 (5288): fusion 4 + satellite landed 18:17Z (headroom ~145). Waiting for 39.4k metal → metal_mine 17 (~20:50Z). ~8k crystal held.
- 5:316:9 (5587): solar 14, deut 1–4 and crystal 11 all landed by 18:48Z (crystal now 3.1k/h, deut 393/h). Headroom 4 → solar 15 (21.9k/8.8k, +190) at ~20:40Z, then deut 5 and crystal 12.
- Empire production 35.3k / 13.2k / 2.8k per hour. Score 2 141, rank 416. No hostile fleets. Astro 5: 37.5k/75k/37.5k; empire crystal ~26k.
- Strategy rewritten this session under the Commander's delegated authority (commit `strategy: expansion-first engine…`): decisions 008/009/010, five new doctrine rules, L10–L14, research order, both skills. The full BJACK chat (419–663) is digested in `ops/diplomacy/2026-09-11_BJACK-chat.md`.

## Next actions
1. 19:51Z combustion 7 lands → `queue_research`: computer 6 (0/12.8k/19.2k) only if it does not push astro 5 past its ETA; otherwise weapons 5 (12.8k/3.2k) or armour 7 (64k metal).
2. ~20:40Z 5:316:9: solar 15 (21.9k/8.8k), then deut synth 5, crystal 12.
3. ~20:50Z 5:316:10 metal ≥ 39.4k → metal_mine 17.
4. Astro clock (ETA ≈ 00:30–01:00Z on 09-12 at 13.2k crystal/h after solar 15 and metal 17 are paid): every cycle write ETA(astro 5) = max((75k − empire crystal) ÷ 13.2k/h, (37.5k − capital deut) ÷ …). When empire crystal ≥ 75k: sweep 5:316:10 and :9 crystal to the capital with the 5 LC (13 min flights), then `queue_research(astrophysics)`. Colony ship to 5:316:3 only after it *lands* (L3), per `empire-colonize`.
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
