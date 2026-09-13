# 009 — Growth engine: planets before fleet, crystal before metal, the astro ladder as the clock

- **status:** confirmed by the Commander 2026-09-13T09:45Z (accepted under delegated authority 2026-09-11T18:05Z); deuterium trade declined by the Commander 2026-09-13T07:52Z — synthesizers only
- **date:** 2026-09-11
- **decided by:** Lieutenant under delegated authority; Commander to confirm or amend

## Context (2026-09-11T18:10Z)
- Production: metal 35.3k/h, crystal 13.2k/h, deuterium 2.8k/h (3 planets) ≈ 1.23M/day. Score 2 141, rank 416/4 245. Universe: 5× economy, 4× fleet, 5× research.
- Astrophysics ladder (`docs/game/mechanics.md`, ×1.75/level): 5 → 37.5k/75k/37.5k (planet 4); 6+7 → 180k/361k/180k (planet 5); 8+9 → 553k/1.1M/553k (planet 6).
- At today's rates: astro 5 crystal = 5.7 h of empire crystal; astro 6+7 crystal = 27 h but **deuterium = 64 h** — deuterium, not crystal, is the planet-5 bottleneck (same finding as NeC, `ops/diplomacy/2026-09-11_BJACK-chat.md`).
- A level-11 crystal mine on 5:316:9 costs 5.3k/2.6k and pays back its crystal in 5 h; crystal 15 on the capital costs 34.6k/17.3k and pays back in 18 h; a new colony's mines 1–10 pay back in hours. Mines compound only while they are cheap; new planets are where cheap mines live.
- BJACK's fastest grower doubled his income in one evening by (a) upgrading the lowest mine in the empire first, (b) pricing energy with the mine, (c) never leaving a queue or the research slot empty; the #1 player refused to build a fleet because 922k in a colony returns +24k/h forever vs one-off loot.
- Raiding is parked (L9). Our 5× floor is 428 invested; every farm below it is closed, and it rises with every build.

## Options
1. **Expansion first** — every cycle: fill every queue with the best return in the *empire* (lowest mines, colonies first), sweep crystal/deuterium to the capital for each astro level the moment the sum is there, colony ship ready before the research lands, bootstrap the new planet from the capital. Fleet = cargo + probes only until planet 5. Pro: highest compounding; matches what the top players measured. Con: stockpiles of 75k–360k crystal sit on the capital before each astro level (raid bait; decision 006 covers it).
2. **Balanced** — alternate astro levels with capital mines and a small cruiser line. Pro: some loot, some score from ships. Con: cruisers close our own targets (L8), lose 100 % when they die, and every 60k in a cruiser is a colony mine not built.
3. **Deep first** — mines to 20+ on three planets before astro 5. Con: 32 % worse per resource than the same money in a 4th planet (measured).

## Decision
Option 1, with these knobs:
- **The astro ladder is the clock.** Each cycle computes ETA(astro N) = max over resources of (needed − on hand) ÷ empire production, and everything crystal-priced that is not a mine with payback < ETA(astro N) waits. Mines whose payback is shorter than the ETA are *always* built — they arrive before the research would anyway.
- **Crystal before metal** on every colony until crystal production ≥ ½ metal production empire-wide (today 0.37). Deuterium synthesizers on the cold worlds (5:316:9, capital) until deuterium ≥ astro pace (planet 5 needs ~4k/h to keep up with crystal).
- ~~Trade the structural surplus (decision 010)~~ — rejected by the Commander 18:30Z. Surplus metal goes to rocket launchers (wall, pure metal), metal-only research (armour/combustion) and metal storage; deuterium comes only from our own synthesizers on the cold worlds.
- **Fleet**: cargo for sweeps and bootstraps, probes for watch, nothing else until planet 5 or a Commander order. Defence per 006, rocket launchers as the metal sink when crystal is the only thing missing.
- **Horizon** stays six planets (002). Reassess at astro 9.

## Forecast (rough, compounding assumed from measured mine curves; revise each status report)
| milestone | earliest | expected | empire production then | score then |
|---|---|---|---|---|
| astro 5 queued | +6 h (pure hoard) | +8–10 h (mines with payback < ETA still built) | ~40k/15k/3.5k | ~2.6k |
| planet 4 founded (5:316:3) | +3 h after astro 5 lands (2.8 h research) | ~2026-09-12 early UTC | — | — |
| planet 4 self-sustaining (mines ~10) | +8 h of bootstrap cargo | 2026-09-12 midday | ~55k/25k/5k | ~4k |
| astro 7 lands → planet 5 | 180k deut is the gate: ~36 h at 5k/h, or ~12 h with a 100k deut trade | 2026-09-13 | ~75k/35k/8k | ~7k |
| astro 9 lands → planet 6 | 553k deut / 1.1M crystal: ~2 days at 5-planet rates | 2026-09-15/16 | ~130k/60k/15k | ~15–20k (top ~150) |
Reference points from the chat: 3 planets → 21.9k metal/h (DenizYoldas), 4 planets → 45.8k/18.1k/4k (NeC), 5 planets → 194k/77k/18.5k (aranella, deep mines, days of lead).

## Consequences
- DOCTRINE → *Lowest mine first*, *Astro clock*, *Crystal before metal*, *Research slot never idle*; posture line unchanged.
- `empire/research.md` reordered: astro 5 → computer 6 (ladder, rung, fleet slot for two sweeps at once) → espionage 5 (halves probe losses; rung-free so only when crystal is slack) → astro 6, 7. Weapons/armour/combustion only as metal-only fillers when the slot would otherwise idle.
- `empire-farm` skill rewritten to the cross-planet comparison.

## Revisit when
- Planet 5 is founded (fleet question reopens: cruiser line vs astro 8/9).
- We are raided for more than one hour of production in a week (stockpile discipline failed → fleet-save routine).
- Crystal production reaches ½ of metal (the crystal-before-metal knob turns off by itself).
