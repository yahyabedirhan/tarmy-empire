# Handoff — 2026-09-11T17:40Z

## Do this first
Run `/empire-cycle`. Capital armour 6 (research) lands 18:06:19Z — queue the next research then (crystal is thin at the capital, ~6.8k; pick metal-only techs like armour/weapons until it recovers). All three build queues are otherwise empty and were left that way deliberately — see *Where we are*.

## Where we are
- Capital (5080): ~25k metal / ~6.8k crystal / ~69k deuterium. 12 espionage probes on hand, fleet otherwise unchanged (62 LF, 5 LC, 4 SC, 2 recyclers, 1 colony ship). Building/ship queues intentionally empty: nothing affordable doesn't eat into the crystal reserve held for astro 5.
- 5:316:10: ~3.4k metal / ~4.9k crystal / ~36k deuterium. Idle — accumulating toward the ≥30k crystal astro-5 shuttle threshold.
- 5:316:9: ~10.7k metal / ~7.9k crystal / 6k deuterium, factor 1 but only 10 energy headroom. Solar 14 not yet affordable (needs 14.6k metal); crystal_mine 11 would drop factor below 1 (needs +54 energy) so deliberately not queued. Idle.
- Posture unchanged (Commander 15:15Z): raiding parked, growth first, defence where exposed. Goal: astro 5 → planet 4 at 5:316:3 (decision 002) once crystal ≥ 75k at the capital.
- Neighbourhood-watch-resume mission closed partial (`ops/missions/2026-09-11T16-48_neighbourhood-watch-resume.md`): only 2/21 remaining targets scanned — probe supply (1k crystal each) competes with the astro-5 crystal hold, so the sweep isn't worth resuming until crystal is more abundant. 19 targets still unscanned (see file for the list).

## Next actions
1. On armour 6 landing (18:06:19Z), queue the next capital research — favour metal-only or crystal-light options while crystal rebuilds (`research_tree` for current costs).
2. Once capital crystal climbs back past ~15-20k, resume queueing buildings there (robotics/shipyard/lab ladder per `empire-farm`).
3. 5:316:10: once crystal ≥ 30k, shuttle it to the capital with the capital's LC/SC fleet (5 LC + 4 SC currently idle at home) for the astro-5 push.
4. 5:316:9: once metal ≥ ~15k, queue solar 14 first (adds energy headroom), then crystal 11.
5. Neighbourhood watch: resume the remaining 19 targets (list in the closed mission file) once crystal is no longer being hoarded, or if the Commander wants scans prioritised over astro 5 sooner — otherwise leave parked.
Later: `.plans/remote-24-7-lieutenant.md` — the Commander researches a 24/7 remote runner.

## Questions for the Commander
- none open.

## Uncommitted strategy changes awaiting approval
- none.

## What changed this session
- Prior evening queue (shipyard 6, metal 15/16, fusion 4, RL ×30 across two colonies) landed in full; six more quest rungs paid.
- Research un-stalled: armour 5 → hyperspace 1 → armour 6 queued in sequence, all crystal-light, preserving crystal for astro 5.
- Neighbourhood-watch-resume soldier ran ~48 min, scanned 2/21 remaining targets (`intel/targets/5-314-5_Furukhai.md`, `5-314-6_Aaliyah_O.md`), then closed partial — probe cost (1k crystal each) conflicts with the astro-5 crystal hold; deferred rather than resumed.
- All three planets deliberately left with empty build queues at points this cycle where every affordable item would have spent crystal earmarked for astro 5, or (5:316:9) dropped the energy factor below 1.
