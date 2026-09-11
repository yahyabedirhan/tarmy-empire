# 002 — Expansion: six planets, galaxy 5, home system outward

- **status:** accepted
- **date:** 2026-09-11
- **decided by:** Commander (challenged: "why stay in galaxy 5, why close, what about cross-galaxy?")

## Context (from `docs/game/mechanics.md`)
- Planets allowed = `1 + ceil(astrophysics/2)`. Astro cost grows 1.75×/level: level 3 → 12k/25k/12k (planet 3); 5 → 38k/75k/38k (4); 7 → 115k/230k/115k (5); 9 → 352k/704k/352k (6); 11 → 1.08M/2.15M/1.08M (7); 13 → 3.3M/6.6M/3.3M (8).
- Colonisable positions widen with astro: 1–3 → positions 4–12; 4–5 → 3–13; 6–7 → 2–14; 8+ → 1–15.
- Position bonuses: metal +17/23/35/23/17 % on 6–10; crystal +40/30/20 % on 1–3; deuterium ∝ (1.36 − 0.004·T_avg), colder (higher position) is better; solar satellites prefer warm.
- Distance: same system `1000 + 5·Δpos`; same galaxy `2700 + 95·Δsystem`; other galaxy `20000·Δgalaxy`. Flight time ∝ √distance. So (small cargo, this tech, 4× fleet): same system ≈ minutes; next system ≈ 3× that; adjacent galaxy ≈ 4.5×; but every transport is a *round trip in a fleet slot*, and we have 4 slots.
- Fields are unknown until settled. Home system 5:316 today: free 1,2,3,4,6,9,11,13,14,15; neighbours caioc (5), nash1999 (7), Saeed2 (8).
- Research is account-wide and uses the highest lab; only the capital needs a lab.

## Options
1. **Cluster: galaxy 5, system 316 first, then 315/317** — every planet minutes from the capital.
   Pro: one transport fleet feeds every bootstrap in one cycle; a threatened planet can fleet-save to a neighbour in minutes; defence fleets and recyclers cover the whole cluster from one place; scans of one system cover all our targets and all our worlds. Con: one hostile neighbour sees everything we have; a strong raider in 5:31x hits all of us at once; we inherit the metal/crystal/deut spread of one system (positions decide it, and 1–3 need astro 6–8).
2. **Spread across galaxy 5** (e.g. 5:100, 5:316, 5:450) — each planet in a quiet neighbourhood with its own raiding ground.
   Pro: more inactive targets in range overall; not all eggs in one system. Con: transports are hours each way and occupy fleet slots that are our scarcest asset (4); bootstrapping a colony 200 systems away takes days of cargo runs; we cannot defend or fleet-save across it.
3. **Cross-galaxy** — planets in galaxies 4/6.
   Pro: a foothold in another raiding ground; hidden from our galaxy's predators. Con: 20 000 distance units minimum ⇒ ~1.5 h each way even now; a bootstrap is impossible to feed; the colony must be self-sufficient from birth (weeks of near-zero production); there is no defence or recovery possible; nothing about production changes by galaxy, so the only upside is target access — and we lack the fleet to use it.
4. **Deep, not wide** — stay at 2 planets, max their mines.
   Pro: no astro spend. Con: a planet is another build queue, another energy budget and another 5 queue slots in a 5× universe; at 12k/25k/12k astro 3 costs less than one mine level on the capital. Wide wins early.

## Decision
Option 1. Horizon **six planets** (astro 9 ≈ 1.4M total, affordable when income is ~5× today's). Order of slots, each chosen for a written reason:
1. **5:316:9 or 6** (+17 % metal, allowed now at astro 3) — the third planet; metal is the volume resource for ships and mines.
2. **5:316:3** at astro 5 (+20 % crystal) — crystal is our historical limiter (L5).
3. **5:316:13/14** at astro 7 (cold → deuterium; also a warm solar-satellite world is *not* this one) — fuel and research pricing.
4. **6th**: best remaining metal slot (8 if ever free, else 315/317 slot 6–10).
Cross-galaxy: refused until we own a moon with a jump gate (hyperspace 7), which is the only mechanic that makes distance free.

## Consequences
DOCTRINE → Colonize rule; `colonize` skill target list; planet roles: 12 capital, 10 metal-world, next metal-world, then crystal-world, then deut-world.

## Revisit when
- A hostile active raider settles in 5:314–318 or hits us twice (cluster risk realised).
- Astro 9 is affordable (decide 7th+ or stop).
- We build a jump gate (cross-galaxy becomes free).
- Any chosen slot turns out to have < 120 fields (too small for a mine-world).
