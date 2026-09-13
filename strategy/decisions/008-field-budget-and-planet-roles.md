# 008 — Field budget: the capital builds facilities, the colonies dig

- **status:** confirmed by the Commander 2026-09-13T09:45Z (accepted under delegated authority 2026-09-11T18:05Z)
- **date:** 2026-09-11
- **decided by:** Lieutenant under delegated authority; Commander to confirm or amend

## Context
- On this server every building level costs **one field, cumulative**, for every structure; ships, defence, research and solar satellites cost none. Confirmed against all three planets' `fields_used` (capital 90/139, 5:316:10 73/150, 5:316:9 45/169 at 2026-09-11T18:07Z).
- The terraformer (+5 fields/level, `codex`) needs nanite factory 1 (1M/500k/100k) which needs robotics 10 + computer 10. Many sessions away.
- The quest ladder still asks the capital for robotics 5→10, shipyard 6→12, lab 7→12, silo 0→4, nanite 0→1 = **21 fields**. That leaves ~28 for anything else on the capital.
- Research is account-wide and uses the highest lab: only one planet needs a lab. Ships are built where the shipyard is: only one planet needs a deep shipyard.
- BJACK measurement (`ops/diplomacy/2026-09-11_BJACK-chat.md`): a mine one level ahead of the empire's lowest is ~32 % worse per resource; the #1 player's capital is her *worst* mine investment and she says so.
- Fields per planet are random 125–248 (12 measured planets, no relation to slot). Ours are small-to-medium.

## Options
1. **Roles by field budget** — capital = facilities + fleet home, mines only when cheaper than any colony's; 5:316:9 (169 fields) = deep mine world; 5:316:10 (150) = metal world; planet 4 at 5:316:3 = crystal world. Pro: no field ever blocks a ladder rung; every mine level goes where it yields most. Con: the capital's own income plateaus.
2. **Ad hoc per cycle** — keep deciding field use by whatever is affordable. Pro: nothing to maintain. Con: the last two sessions already spent capital fields on mines that the colonies would have used better.
3. **Capital as mine world, move the lab** — no: the lab is 7 already and research time depends on it; moving it is pure waste.

## Decision
Option 1. Field allocation on the capital, in order: energy (satellites, no fields) → ladder facilities → mines only if `codex` shows a better return per 1 000 resources (mine + forced energy) than the best colony mine. On colonies: mines first, robotics to ~6, storage as pools demand, no shipyard beyond what a rung asks (5:316:10 has 2 and keeps it), no lab.

Roles (planet files updated):
| planet | fields | role | favours |
|---|---|---|---|
| 5:316:12 capital | 139 | `capital` | lab, shipyard, robotics, silo, nanite; fleet home; satellites for energy |
| 5:316:9 | 169 | `metal-world` (deepest mines) | metal, then crystal; deuterium (coldest world we own, T_avg 4) |
| 5:316:10 | 150 | `metal-world` | metal, crystal within 2 levels |
| 5:316:3 (planet 4, astro 5) | unknown | `crystal-world` | crystal first (+20 % slot bonus) |
| planet 5 (astro 7) | — | `deut-world` at 5:316:13/14 (cold) or 2nd crystal world at 5:316:1/2 if astro 6 opens them — decide at astro 6 from `galaxy` |

## Consequences
- DOCTRINE → *Lowest mine first* rule and *Fields* line.
- `empire-farm` step 3 rewritten: compare return across planets, not within one.
- Capital mines stop at whatever level the comparison says; today that is metal 16 / crystal 14 / deut 11 unless a colony's next level is dearer.

## Revisit when
- Planet 4 lands with < 120 fields (then it is a crystal outpost, not a mine world, and planet 5's slot is chosen for fields too).
- Nanite factory is affordable (terraformer path opens; the capital can dig again).
- A colony's mines reach the capital's levels (the comparison flips by itself; nothing to decide).
