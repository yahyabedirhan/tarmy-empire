# 015 — Defence plan: a wall per planet class that makes a 60-cruiser raid lose money

- **status:** accepted — walls are bought with the crystal left after planet 6 and the crystal mines (Commander 20:55Z: "top priority is to boost the new colony and maximize our crystal mining, then defence is the second priority"); metal-only parts first, RL capped as written
- **date:** 2026-09-17
- **decided by:** Lieutenant (pending approval); drafted by research round 2 (`reports/research/2026-09-17T19-35Z_round-2.md`); Commander direction 2026-09-17T19:40Z: "defence is more important than attack growth… otherwise we'd be farming for others"

## Context (2026-09-17T19:35Z)
- Who can hit us: the 5× rule refuses an attacker whose invested score is ≥ 5 × ours (14 178 → ≥ 70.9k). Ranks 1–6 (82k–112k) cannot; **ranks 7–~2 000 can**. Our band (ranks 30–80) holds 13.5k–17k score; a 60-cruiser fleet is 1.74M resources = 1 740 score, a plausible 10 % of such a player's spend. 25 battleships = 1.5M.
- Loot is at most half of each pool within the raider's cargo (manual → Combat → Loot). Half-pools today: :10 **424k**, :9 **315k**, :3 181k, :14 114k, capital 75k, :1 24k.
- Walls today (`empire_overview`, queued batches included): capital 139 RL / 10 LL / 2 gauss / 1 small dome + 62 LF, 9 probes, 2 recyclers, 38 satellites; :10 147 RL; :9 94 RL; :3 53 RL; :14 40 RL; :1 nothing (no shipyard — turrets need "Shipyard level 1" on that planet, `codex`).
- Our techs: weapons 8, shielding 7, armour 9 (+10 % per level on every turret and ship, manual → Combat). Raider assumed 8/8/8.
- Unit values (`combat_rules`, `codex`): RL 80 attack / 20 shield / 2 000 hull for 2 000 M; LL 100/25/2 000 for 1.5k/0.5k; HL 250/100/8 000 for 6k/2k; ion 150/500/8 000 for 5k/3k; gauss 1 100/200/35 000 for 20k/15k/2k; plasma turret 3 000/300/100 000 for 50k/50k/30k (needs plasma 7); small dome 2 000 shield / 20 000 hull for 10k/10k; large dome 10 000 shield / 100 000 hull for 50k/50k. Seven in ten destroyed turrets rebuild; ships never do; defences leave no debris.
- Rapid fire against turrets (`combat_rules`): cruiser 10 × RL; bomber 20 × RL and LL, 10 × HL and ion, 5 × gauss and plasma; destroyer 10 × LL; deathstar everything. **Battleships, battlecruisers and light fighters have no rapid fire against any turret.** So a wall of only rocket launchers is exactly what a cruiser fleet farms; heavy lasers, ion cannons and gauss are what cruisers cannot chain through.
- Shields regenerate every round and a shot at or below 1 % of the shield bounces; a large dome (10 000 × 1.7 = 17 000 shield) shrugs off a cruiser's 720-damage shot 23 times in one round — it soaks its share of the raider's fire for nothing.

## Simulations (`simulate_combat`, 5 runs, seed 14, raider 8/8/8 with cargo, us 8/7/9)

| wall | vs | result | raider loses | we lose (before 70 % rebuild) | raider's loot |
|---|---|---|---|---|---|
| capital today (139 RL, 10 LL, 2 gauss, SSD + 62 LF, 38 sats) | 60 cruisers + 20 LC | **raider 5/5** | 112k | 780k (fleet, satellites, every turret) | ≤ 75k + 145k debris |
| capital target (200 RL, 50 LL, 20 HL, 10 ion, 10 gauss, SSD, LSD + fleet) | 60 cruisers + 20 LC | defender 5/5 | **1.98M** (all) | 896k (55 LF, 33 sats, 176 RL, 48 LL, 15 HL — turrets rebuild 70 %) | 0 |
| capital target | 25 battleships + 20 LC | defender 5/5 | **1.74M** (all) | 177k | 0 |
| :10 today (147 RL, 56 sats) | 60 cruisers + 20 LC | **raider 5/5** | 2.4k | 434k | ≤ 424k — a free farm |
| :10 lean (150 RL, 40 LL, 10 HL, 5 ion, 4 gauss, SSD, LSD) | 60 cruisers | raider 5/5 | 391k | 908k | ≤ 424k — still pays |
| :10 floor (150 RL, 50 LL, 20 HL, 10 ion, 10 gauss, SSD, LSD) | 60 cruisers | **draw 5/5** | 1.49M | 914k | 0 (a draw loots nothing) |
| :10 target (200 RL, 50 LL, 20 HL, 10 ion, 15 gauss, SSD, LSD) | 60 cruisers | defender 5/5 | **1.98M** | 674k | 0 |
| :10 target | 60 cruisers at **10/10/10** techs | defender 5/5 | **1.98M** | 813k | 0 |
| crystal/deut target (100 RL, 30 LL, 10 HL, 5 ion, 6 gauss, SSD) | 30 cruisers + 10 LC | defender 5/5 | 990k | 356k | 0 |

Reading: the number that flips a fight is gauss + heavy lasers + ion (units cruisers cannot rapid-fire through) behind a large dome; rocket launchers alone are loot. The fleet parked at the capital dies in every fight it is in, win or lose: 62 LF are 248k that only a moon or a deploy-away saves.

## Decision — the wall per planet class

| class | planets | wall (units) | to buy from today | cost M / C / D | shipyard-line hours (robotics as today) |
|---|---|---|---|---|---|
| **capital** (fleet home, ~250k stock) | 5:316:12 | 200 RL / 50 LL / 20 HL / 10 ion / 10 gauss / 1 SSD / **1 LSD** / silo 2 + 10 ABM | +61 RL, +40 LL, +20 HL, +10 ion, +8 gauss, LSD; silo 1–2, 10 ABM | 562k / 260k / 16k (+ silo/ABM 140k / 60k / 23k) | 7.3 h (+ 1.0) |
| **metal-world** (600k+ stock) | :10, :9 | 200 RL / 50 LL / 20 HL / 10 ion / **15 gauss** / SSD / LSD (floor: 150 RL, 10 gauss = the draw wall) | :10 +53 RL; :9 +106 RL; each +50 LL, +20 HL, +10 ion, +15 gauss, SSD, LSD | :10 711k / 380k / 30k; :9 817k / 380k / 30k | :10 8.7 h (robotics 7); :9 10 h (robotics 6) |
| **crystal-world** | :3, :1 | 100 RL / 30 LL / 10 HL / 5 ion / 6 gauss / SSD | :3 +47 RL; :1 shipyard 1 then +100 RL; each +30 LL, +10 HL, +5 ion, +6 gauss, SSD | :3 354k / 150k / 12k; :1 460k / 150k / 12k | :3 5.7 h (robotics 5); :1 32 h at robotics 2 → **robotics 8 first** (10.7 h) |
| **deut-world** | :14 | same as crystal-world | +60 RL, +30 LL, +10 HL, +5 ion, +6 gauss, SSD | 380k / 150k / 12k | 7.8 h (robotics 4) |

Totals: turrets and domes **3.28M metal, 1.47M crystal, 112k deuterium**; with the capital's silo 1–2 and 10 ABM **3.42M / 1.53M / 135k** — 1.40M idle metal plus ~26 h of metal production; 33 crystal-hours (at 46k C/h) spread over decision 014's H1–H2; +5 000 score (rank ~48 → ~27 on today's board). Turrets go in the *shipyard line*, beside the mines (manual → Queues), so no crystal level waits for them.

Order of purchase (the metal sink of decision 013's stock rule):
1. Metal-worlds first — they hold the loot and today lose it for free: :10 to the floor wall (511k / 305k / 20k), then :9.
2. Capital to target + silo 2 + 10 ABM (rung `the_shield_against_them` 9k/9k/6k) + LSD (rung `the_greater_dome` 9k/9k/6k).
3. :3, :14 to the crystal/deut wall; :1 after shipyard 1 and robotics 8.
4. Metal-worlds from floor to target (+50 RL, +5 gauss each).
Within a planet: gauss and HL before more RL (they are what the sim needs), LL as the cheap filler, ion last.

Research that multiplies the wall (all planets at once): **armour 10** (512k M, 11.4 h — pure metal, +10 % hull on 3.3M of turrets ≈ 330k of value) → **weapons 9** (204.8k M / 51.2k C, 5.7 h; +10 % attack) → shielding 8 (25.6k M / 76.8k C, 2.3 h) when crystal is slack. Each later level is ×2 the price for the same +10 %: stop at armour 10 / weapons 9 / shielding 8 until the walls double.

Missiles: an IPM (12.5k / 2.5k / 10k) does 12 000 to emplacements only, ignores both domes, and what it kills does not rebuild; range 5 × impulse − 1 systems (a raider at impulse 4 reaches 5:297–5:335). One IPM kills 6 RL (12k) or a third of a gauss — a raider spends 75k to remove 37k of gauss, so IPMs are aimed at domes, gauss and plasma turrets, not at RL. Answer: silo 2 + 10 ABM (60k/60k/3k + 80k M/20k D) on the capital now, on :10/:9 in H2; each ABM destroys exactly one incoming missile.

Plasma turrets (plasma 7, 50k/50k/30k each, 3 000 attack): 4 of them equal 11 gauss in attack for 520k vs 407k — gauss stay the better buy per resource; plasma turrets only once plasma 7 is researched for its production bonus anyway (H2) and a wall needs single big hulls against bombers (RF 5 vs both).

Fleet: the 62 LF stay at the capital only because it will have the strongest wall; on `fleet.incoming` they deploy to the planet farthest from the attacker (13 min, 5–11 D) — the existing THREATENED rule. A moon is the permanent answer and is priced in decision 014 (≈ 23M expected; not now).

## Consequences
- DOCTRINE *Defend*: the "value ≥ stock ÷ 4" rule is replaced by the class walls above; "rocket launchers are the sink for idle metal" becomes "gauss/HL/LL/RL in the class mix are the sink".
- Decision 006 amended: the floor is a wall that makes `simulate_combat` (60 cruisers, 8/8/8) lose money on every planet, re-run monthly and whenever a pool doubles.
- Decision 013: metal-worlds spend their own metal on their own walls before shipping any out.
- `empire-farm`: the shipyard line always holds the next wall batch of the planet's class until the class wall is complete.

## Revisit when
- We are hit and the report shows the raider profited (loot + debris > losses).
- Our score passes 30k (the raider pool changes: ranks 7–20 gain interest, 25 battleships become 50).
- Plasma 7 lands (re-price plasma turret vs gauss with `simulate_combat` vs 20 bombers).
- A planet's half-pool exceeds 1M for a day (then the wall doubles or the stock ships out).
