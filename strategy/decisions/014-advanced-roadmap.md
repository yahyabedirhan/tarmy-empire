# 014 — Advanced roadmap: plasma and robotics compound, nanite serves the capital, moons and terraformer wait

- **status:** accepted — crystal mining and planet 6 first, defence second (Commander 20:55Z); research lane as written (plasma path is a crystal multiplier)
- **date:** 2026-09-17
- **decided by:** Lieutenant (pending approval); drafted by research round 2 (`reports/research/2026-09-17T19-35Z_round-2.md`)

## Context (2026-09-17T19:35Z, `empire_overview`, `research_tree`, `codex`)
- Rank 48 of 4 602, score 14 178 (`leaderboard`). Score is resources *spent* ÷ 1 000 (manual → Ranking), so 1.40M idle metal is 1 400 rank points not yet on the board.
- Production per hour: metal 77.6k, crystal 48.7k, deuterium 19.0k gross (three fusion-5 reactors burn 1 209 → 17.8k net). Stocks: 1.40M M, 166k C, 695k D. Crystal is the gate for everything on this list; one crystal-hour = 46–49k C.
- Research: energy 6, laser 9 (10 lands 22:06Z), ion 5, hyperspace 2, plasma 0, computer 6, astro 9, espionage 5, combustion 7, impulse 3, hyperspace drive 0, weapons 8, shielding 7, armour 9, graviton 0. Lab 8 on the capital only. Research seconds = (M+C) ÷ (1 000 × 5 × (1+lab)) × 3 600 (manual → Build & research time; matches every `codex` figure).
- Facilities: capital robotics 8 / shipyard 8 / lab 8, 110/139 fields. Colonies: robotics 7 / 6 / 5 / 4 / 2; :1 has no shipyard. Free fields empire-wide: 503 (capital 29, :10 51, :9 73, :3 108, :14 110, :1 132).
- Prerequisites (`codex`, per planet for buildings): nanite ← robotics 10 + computer 10; terraformer ← nanite 1 + energy 12; plasma ← energy 8 + laser 10; jump gate ← lunar base 1 + hyperspace 7; phalanx ← lunar base 1; IPM ← silo 4; ABM ← silo 2; cruiser ← impulse 4; battleship ← hyperspace drive 4 (← hyperspace 3); bomber ← impulse 6 + plasma 5; battlecruiser ← hyperspace drive 5 + laser 12 + hyperspace 5; destroyer ← shipyard 9 + hyperspace drive 6 + hyperspace 5; deathstar ← shipyard 12 + hyperspace 6 + hyperspace drive 7 + graviton 1 (← lab 12 + 300 000 spare energy).
- Decision 013 (organs) is in force; 002 amendment: no 7th planet before crystal ≥ 80k/h. Raiding parked (001/009).

## What each advanced item is, priced from our levels (`codex`, capital, lab 8 / robotics 8)

| item | chain from today | M / C / D | research-slot h | construction h | what it multiplies for us | verdict |
|---|---|---|---|---|---|---|
| **plasma 1–4** | energy 7, 8 → plasma 1–4 | 30k / 214k / 92k | 5.4 | — | +1 % M, +0.66 % C, +0.33 % D per level on every mine we own: plasma 4 = +3.1k M, +1.29k C, +250 D per hour, for ever. Crystal payback of the whole entry (214k C) = 166 h; of plasma 1–4 alone (60k C) = 47 h | **compounding %** — cheapest production we can buy after mine level 20 |
| plasma 5–7 | plasma 5, 6, 7 (rung `plasma_theory` at 7) | 224k / 448k / 112k | 14.9 | — | +2.3k M, +0.96k C, +0.19k D per hour; plasma 5 unlocks bombers, 7 unlocks plasma turrets | compounding %, weaker each level (cost ×2, gain flat) |
| plasma 8 | — | 256k / 512k / 128k | 17.1 | — | +776 M, +321 C, +63 D per hour; crystal payback 1 600 h | vanity until crystal ≥ 100k/h |
| **robotics on colonies** | :3 robotics 5→8: 89.6k / 26.9k / 44.8k; :1 2→8: 126k / 38k / 63k; :14 4→8: 115k / 34k / 57k | metal-heavy | — | 0.2–1 h each | build time ÷ (1+robotics): :3's 7.25 h crystal-20 build becomes 4.8 h at robotics 8, 4.0 h at 10; a 100-RL batch on :1 takes 16 h at robotics 2, 5.3 h at 8 | **compounding %** on every future build and wall; paid in idle metal |
| **nanite 1** (capital) | robotics 9, 10 + computer 7, 8, 9, 10 → nanite 1 (rungs `hands_of_many`, `deep_computing`, `the_nanites` pay 27k / 24k / 17k) | 1 307k / 976k / 830k | 8.5 (computer) | 3.5 (robotics) + 3.8 (nanite) | halves every build time **on the capital only** (`2^nanite` in the formula, per planet): lab 12 from 10.9 h to 5.5 h, shipyard 12 likewise, a large cargo from 384 s to 192 s, a 100-turret batch in half the time. Does nothing for the colonies' 7-hour mines | **insurance / ladder** — worth it as the gate to terraformer and for +1 600 score, not as a growth lever |
| nanite 2 | — | 2M / 1M / 200k | — | 7.6 | capital builds ÷ 4 | vanity |
| **terraformer 1** | nanite chain + energy 7–12 (rungs `abundant_power`, `more_ground`, `the_terraformer`) → terraformer 1 | 1 307k / 4 252k / 2 543k | 80 (energy 7–12 = 71.7 at lab 8) | 7.5 | +5 fields, occupies 1 → **net +4 fields** per level (`codex` level 12 = 60 added), draws no energy (no `energy_use` in `codex`, unlike a mine); per planet, needs that planet's own nanite. We have 503 free fields; the capital keeps 13 after the whole facility ladder | **vanity** this month; insurance when a planet drops below 10 free fields |
| **lunar base / moon** | a battle *at our planet* leaving ≥ 100 000 ship debris: 1 % per 100k, cap 20 % at 2M (`combat_rules.moon_chance`); the moon goes to the defender | 20% shot = 1 667 LF destroyed (6.67M) − 2M debris recycled = 4.67M net, expected 5 shots ≈ **23M** | — | — | a moon mines nothing, 1 field + 3 per lunar base level (base occupies 1); can hold robotics, shipyard, storages, phalanx, jump gate and any defence; **cannot be scanned or phalanxed** — the only safe parking for a fleet | **vanity** for an economy empire; becomes insurance the day we own a fleet worth saving (> 5M) |
| sensor phalanx | lunar base 1 (20k/40k/20k) → phalanx 1 (20k/40k/20k) | 80k / 160k / 80k for level 2 | — | 0.3 | range level² − 1 systems: L1 = own system only, L2 = 3, L3 = 8, L4 = 15, L5 = 24; 5 000 D a scan; reads fleets at a planet with arrival/return times | insurance / offence tool; useless while raiding is parked |
| jump gate | lunar base 1 + hyperspace 3–7 (496k C, 248k D, 11 h) → gate 2M / 4M / 2M on **two** moons | ≥ 8M + two moons | 11 | 15.2 per gate | moves ships between two of our moons instantly, no fuel, no cargo; 60 min cooldown both ends. Our six planets are 13 min apart already | **vanity** — cross-galaxy only (002) |
| missile silo 1–2 + 10 ABM | silo 1, 2 (60k/60k/3k) + ABM ×10 (80k M / 20k D); rung `the_shield_against_them` 9k/9k/6k | 140k / 60k / 23k | — | 1.0 | each ABM destroys exactly one incoming IPM before it lands; capacity 10 ABM per silo level | **insurance**, cheap, metal-priced |
| silo 3–4 + 5 IPM | silo 3, 4 (240k/240k/12k) + IPM ×5 (62.5k/12.5k/50k); rungs `the_silo`, `a_salvo` | 302k / 252k / 62k | — | 2.4 | IPM: 12 000 damage to emplacements only, ignores shields, nothing it kills rebuilds; range 5 × impulse − 1 systems (impulse 3 = 14, 4 = 19); one IPM (25k) kills 6 rocket launchers (12k) or ⅓ of a gauss (12k) | **vanity** while raiding is parked (it is an attack tool); 2 rungs pay 48k of its 616k |
| gauss / large dome / plasma turret | gauss and large dome are unlocked; plasma turret needs plasma 7 | gauss 20k/15k/2k, LSD 50k/50k, PT 50k/50k/30k | — | 1 120 s / 3 200 s / 3 200 s per unit | see decision 015 — a wall of 200 RL / 50 LL / 20 HL / 10 ion / 10–15 gauss / SSD / LSD turns 60 cruisers from a free win into a 1.5–2.0M loss for the raider (`simulate_combat`) | **insurance** — the one thing that stops us being farmed |
| cruiser | impulse 4 (rung `stronger_impulse`) | 16k / 32k / 4.8k | 1.1 | 864 s each | 400 attack, RF 10 vs rocket launchers, 6 vs light fighters; 20k/7k/2k each | the cheapest real warship; only if raiding reopens |
| battleship | hyperspace 3 + hyperspace drive 1–4 (rungs `hyperspace_theory`, `hyperspace_engines`, `the_battleship`) | 150k / 316k / 98k | 10.4 | 1 920 s each | 1 000 attack, 60k hull, 45k/15k/0 each — best attack per resource of anything we can reach; no RF vs defences | offence only |
| bomber | impulse 5, 6 + plasma 5 | 96k / 192k / 29k on top of plasma 1–5 | 6.4 | 2 400 s each | RF 20 vs RL/LL, 10 vs HL/ion, 5 vs gauss/plasma — the wall-breaker | offence only |
| battlecruiser | hyperspace 4, 5 + hyperspace drive 5 + laser 11, 12 | 774k / 1 411k / 344k on top of HD 1–4 | 43 | 2 240 s each | RF 7 vs battleships, 4 vs cruisers | vanity this month |
| destroyer | shipyard 9 + hyperspace 5 + hyperspace drive 6 | 422k / 691k / 218k on top of HD 1–5 | 21 | 3 520 s each | 2 000 attack, 110k hull | vanity this month |
| graviton / deathstar | lab 9–12 (768k / 1 536k / 768k, 20.5 h construction) + 300 000 spare energy on one planet (4 688 satellites on :1 = 9.4M C) + shipyard 12 + hyperspace 6 + HD 7 | > 25M | 90+ | — | the last rung | **vanity** |

Nothing on this list multiplies production by ten. What compounds is: plasma (flat gain per level, cheap at 1–5), robotics where the builds are, walls that stop loot, and — when the Commander reopens it — the 7th planet (astro 11: 1 078k / 2 155k / 1 078k, 71.8 h at lab 8, 49.7 h at lab 12).

## Options
1. **Ladder as written** (quest order): energy 8 → computer 10 → nanite → hyperspace → battleships → … Pro: every step pays a rung. Con: computer 8–10 (384k C, 576k D) and nanite (1M / 500k / 100k) come before plasma and before the walls; the capital gets faster while the colonies stay slow and the metal-worlds stay farms.
2. **Compounding first, ladder second** — plasma 1–5 and the colonies' robotics now (they pay every hour), walls now (decision 015, metal we cannot otherwise spend), then the nanite chain in week 1 (rungs + terraformer gate), hyperspace/battleship line in week 2–3, terraformer and moons only on a trigger. Pro: production and safety rise first; the ladder is delayed by ~3 days, not skipped. Con: nanite/terraformer arrive later than the ladder would give them.
3. **Military first** — hyperspace drive to battleships, then bombers, reopen raiding. Con: the Commander parked raiding; every battleship is 60k that a wall or plasma level would compound.

## Decision
Option 2. Three horizons, five lanes.

### Horizon 1 — next 48 h (crystal budget ≈ 553k C ≈ 12 crystal-hours of 96)
Research slot, in order (≈ 21 h of 48; the rest is armour 10 as a metal sink):
1. laser 10 — running, lands 22:06Z (rung `focused_light`).
2. energy 7 (51.2k C / 25.6k D, 1.1 h) — plasma gate, no rung.
3. energy 8 (102.4k C / 51.2k D, 2.3 h) — plasma unlocked; rung `abundant_power` +9k/9k/6k.
4. plasma 1, 2, 3, 4 (30k / 60k / 15k, 2.0 h) — +3.1k M, +1.3k C, +250 D per hour for 60k C: crystal payback 47 h.
5. hyperspace 3 (16k C / 8k D, 0.4 h) — rung `hyperspace_theory` +9k/9k/6k pays it back; opens hyperspace drive.
6. computer 7 (25.6k C / 38.4k D, 0.6 h) — 8th fleet slot for the 013 supply network (decision 013 rule 4).
7. plasma 5 (32k / 64k / 16k, 2.1 h) — +776 M, +321 C, +63 D per hour; bomber gate.
8. armour 10 (512k M, 11.4 h) — zero crystal; +10 % hull on every turret in decision 015; +512 score.
Construction (capital): robotics 9 → 10 (307k / 92k / 154k, 3.5 h; rung `hands_of_many`), missile silo 1 → 2 (60k / 60k / 3k), large shield dome (50k / 50k; rung `the_greater_dome`). Colonies: robotics to 8 on :3, :1, :14 (metal-heavy), shipyard 1 on :1, walls per 015 in the shipyard line beside the mines.
Mining lane unchanged: on-role crystal levels with the remaining ~37 crystal-hours.

### Horizon 2 — days 3–7 (crystal ≈ 1.74M C ≈ 38 crystal-hours of 168)
Research slot (≈ 40 h): computer 8, 9, 10 (358k C / 537k D, 8.0 h; rung `deep_computing`) → plasma 6 (128k C, 4.3 h) → hyperspace drive 1–4 (300k C / 90k D, 10 h; rungs `hyperspace_engines` and, with one battleship built, `the_battleship`) → plasma 7 (256k C, 8.5 h; rung `plasma_theory`; plasma turret unlocked) → weapons 9 (204.8k M / 51.2k C, 5.7 h; +10 % on every turret) → impulse 4 (32k C, 1.1 h; rung `stronger_impulse`).
Construction: nanite 1 (1M / 500k / 100k, 3.8 h; rung `the_nanites`) the hour computer 10 lands; lab 9 (102k C) started from a **colony lab 1** (200/400/200 on :10) so the research slot never idles during the capital's lab upgrade (manual → Queues: a lab is locked only "while a research started from it is running"); shipyard 9 (102k / 51k / 26k; rung `a_vast_yard`); walls to the 015 floor on all six planets.

### Horizon 3 — weeks 2–4 (crystal ≈ 7.3M C ≈ 159 crystal-hours of 720, plus astro 11 = 47)
Lab 10–12 (1.43M C; 19 h construction, halved by nanite) → hyperspace 4, 5 (96k C) → hyperspace drive 5, 6 (960k C; destroyers) → laser 11, 12 (307k C; battlecruisers) → shipyard 10–12 (768k C) → silo 3–4 + IPM rung (252k C) → energy 9–12 (3.07M C / 1.54M D, 68 h at lab 8 / 47 h at lab 12) → terraformer 1 *only if a planet is below 10 free fields*. Astro 11 (2.16M C) when crystal ≥ 80k/h (002 amendment). Plasma 8 when crystal ≥ 100k/h. Moon: Commander-only (needs an ally's fleet to die at our planet).

### The five lanes over three horizons

```text
lane      │ H1: next 48 h              │ H2: days 3–7                │ H3: weeks 2–4
──────────┼────────────────────────────┼─────────────────────────────┼─────────────────────────────
mining    │ on-role crystal levels     │ same; plasma 6–7 on top     │ crystal ≥ 80k/h → astro 11
          │ plasma 1–5: +3.9k M +1.6k C│ plasma 7: +5.4k M +2.2k C   │ → 7th planet (crystal world)
──────────┼────────────────────────────┼─────────────────────────────┼─────────────────────────────
research  │ laser10→energy7→8→plasma1–4│ computer8–10→plasma6→HD1–4  │ hyp.4–5→HD5–6→laser11–12
          │ →hyperspace3→computer7     │ →plasma7→weapons9→impulse4  │ →energy9–12 (68 h)→plasma 8
          │ →plasma5→armour10 (metal)  │ lab 9 via colony lab 1      │ lab 10–12 (−31 % research h)
──────────┼────────────────────────────┼─────────────────────────────┼─────────────────────────────
advanced  │ robotics 9→10 (capital)    │ nanite 1 (capital, 3.8 h)   │ shipyard 9–12, silo 3–4, IPM
tech      │ robotics →8 on :3 :1 :14   │ shipyard 9                  │ terraformer 1 only on trigger
          │                            │                             │ moon: Commander-only
──────────┼────────────────────────────┼─────────────────────────────┼─────────────────────────────
defence   │ silo 1–2 + 10 ABM (capital)│ walls to 015 floor, all six │ plasma turrets vs bombers
(015)     │ LSD capital; gauss/HL first│ weapons 9; shielding 8      │ walls grow with the pools
          │ metal-worlds first (600k)  │                             │
──────────┼────────────────────────────┼─────────────────────────────┼─────────────────────────────
logistics │ computer 7 → 8 slots       │ computer 8–10 → 11 slots    │ —
          │ 4 LC + 2 SC; build 6 LC    │ 1 battleship (rung), 10 LC  │
──────────┴────────────────────────────┴─────────────────────────────┴─────────────────────────────
crystal   │ 553k C = 12 crystal-hours  │ 1.74M C = 38 crystal-hours  │ 7.3M C = 159 crystal-hours
research h│ 21 h + 11 h armour         │ ~40 h                       │ ~190 h
```

## Consequences
- `empire/research.md` is rewritten to the order above (diff in the round-2 report).
- DOCTRINE *Research slot never idle* gains: "a colony lab 1 exists so the slot runs while the capital's lab upgrades".
- DOCTRINE *Fields*: the terraformer is not planned; "fields ≤ 2 free" in `STALLED` stays the only trigger.
- Decision 013 stock rule: idle metal goes to robotics on colonies, walls (015), armour 10, weapons 9 — in that order.
- Decision 015 (defence) is the companion; its walls are the first sink for the 1.4M idle metal.

## Revisit when
- Crystal ≥ 80k/h (astro 11, 002) or ≥ 100k/h (plasma 8).
- Any planet has < 10 free fields (terraformer chain becomes insurance, 4.25M C).
- The Commander reopens raiding (impulse 4 → cruisers first, then bombers via plasma 5 + impulse 6; a moon becomes worth a 23M expected spend only when the fleet is worth more than that).
- Our fleet exceeds 5M in value (moon as fleet-save parking).
- A lab-lock test fails (research cannot be started from a colony lab 1 while the capital's lab upgrades) — then lab levels wait for research gaps.
