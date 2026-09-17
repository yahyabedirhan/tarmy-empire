# 013 — Planets are organs, not clones: produce on-role, ship the rest

- **status:** accepted (Commander direction in chat 2026-09-17T19:16–19:28Z: "think our planets as a whole group of utilization instead of individuals that all repeat the same thing"; "make sure that our resources are not idle for no reason"; "boosting a new planet is a nice priority")
- **date:** 2026-09-17
- **decided by:** Commander (direction), Lieutenant (wording)

## Context
- Six planets, all in 5:316: a transport between any two is ~13 min and 5–11 deuterium. Distance is not a cost inside the cluster (decision 002).
- 2026-09-17T18:40Z stocks: metal 1.7M idle across the empire, crystal ~200k, deuterium 676k. Crystal gates every build; metal has no sink but rocket launchers and armour research.
- The four colonies converged on the same shape (metal 19–20 / crystal 18–20) although their roles differ (008): the *Lowest mine first* rule ranks by return-per-1000 across the empire and lets the role only break ties, so same-system planets with near-identical returns all bought the same levels — including metal we cannot spend.
- Planet 6 (5:316:1, +40 % crystal) was bootstrapped 2026-09-17T18:59Z with the generic ramp (metal to 8 first). The Commander stopped it at metal 6: on-site metal is worth ~17k M/day against 1.7M idle, and the crystal + energy it costs buys crystal levels instead.
- 5:316:14 sat idle for 14 h with 104k M / 204k D because the astro clock (009) froze crystal spend — and there is no astro clock any more (002 amendment: no 7th planet).
- Slot attributes: :1 +40 % crystal, hottest (209..249 → 64 E per satellite); :3 +20 % crystal, hot (110..150); :10 and :9 +17 % metal; :9 coldest of the metal pair; :14 deuterium ×1.73 (cold); capital: lab 8, shipyard 8, fleet home, 29 free fields.

## Options
1. **Return-per-1000 across the empire, role as tie-breaker** (status quo, 008/009). Pro: mathematically greedy per level. Con: ignores whether the resource can be spent; produces clones; leaves surplus idle.
2. **Produce on-role only; ship everything else** — each planet buys mine levels only for its product; off-role mines freeze; a stock rule stops production of anything we already cannot spend; a standing transport table moves resources; new colonies are the priority sink. Pro: every crystal goes where the bonus is largest; idle metal becomes walls, research and the crystal worlds' building bills; colonies bootstrap in an hour instead of half a day. Con: fleet slots and cargo hulls become the constraint (4 LC + 6 SC today, 7 slots); a planet cut off (attack, slot shortage) stalls.
3. **Self-sufficient planets** — every planet grows all three mines to feed itself. Con: this is option 1 with extra steps; rejected.

## Decision
Option 2.

| planet | strongest attribute | produces | frozen at (2026-09-17) | receives |
|---|---|---|---|---|
| 5:316:1 | +40 % crystal, hottest | crystal | metal 6, no synths | M from :10/:9, D from the capital/:14 |
| 5:316:3 | +20 % crystal, hot | crystal | metal 19, synth as is | M from :10/:9, D from :14 |
| 5:316:10 | +17 % metal, 150 fields | metal → walls, research metal, crystal-world bills | crystal 19 | — (ships out) |
| 5:316:9 | +17 % metal, coldest of the pair | metal (+ deuterium if it ever gates) | crystal 18 | — (ships out) |
| 5:316:14 | deuterium ×1.73, cold | deuterium (synths when deuterium gates a plan; otherwise its tank is the reserve) | metal, crystal as is | — (ships out) |
| capital | lab 8, shipyard 8, fleet home | research, ships, cargo hulls | all mines | C from :3/:1, M from :10/:9, D from :14 |

Rules:
1. **Produce on-role.** A mine level is bought only for the planet's product, ranked by return-per-1000 among on-role candidates (the slot bonus is already in `codex`). Off-role mines stay at their level.
2. **Stock rule.** A resource whose empire stock exceeds ~24 h of planned spend gets no new mine anywhere; its producers switch to sinks (rocket launchers to the 006 floor, metal-only research, storage levels if a pool nears cap).
3. **Bootstrap by role.** A new crystal-world exits `BOOTSTRAP` at crystal ≥ 5, factor 1, storage ≥ 2, metal capped at 6, no synthesizers, everything shipped in. Feeding it is the empire's first call on surplus for its first 24 h.
4. **Logistics is a product.** The capital builds and home-ports cargo hulls; every planet keeps enough hulls for its outbound flow (:10/:9 metal, :3/:1 crystal, :14 deuterium). Computer 7 (8th fleet slot) moves ahead of the fillers in the research ladder.
5. **Energy by climate.** Satellites on the hot pair (:1 64 E, :3 48 E each) once the plant is dearer per energy than a satellite; plants on the cold ones.
6. **Nothing idles.** A planet with an empty queue and stock above its next on-role level either ships out or builds a sink the same cycle; "waiting for crystal" is not a reason while metal or deuterium sits there.

## Consequences
- DOCTRINE: *Lowest mine first* → *On-role mine first* + stock rule; `BOOTSTRAP` row exit by role; new *Logistics* rule; *Never an empty queue* extended with "or ship out".
- `empire-colonize` bootstrap section: crystal-world ramp rewritten; `empire-farm` step 3 restricted to on-role candidates.
- `empire/research.md`: computer 7 after armour 10.
- Superseded in part: 008's "colonies dig all three" and 009's crystal-first-on-colonies rule (the gate it served is gone).

## Revisit when
- A planet is cut off from the cluster for > 2 h (attack, slot shortage) — then it needs a self-sufficiency floor.
- A resource other than crystal becomes the empire gate for > 24 h (the roles' products change).
- A 7th planet is reopened (astro 11) — the astro clock returns for that resource only.
