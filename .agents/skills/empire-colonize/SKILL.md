---
name: empire-colonize
description: Found and bootstrap a new planet — check the astrophysics allowance, choose the slot per decision 002, send the colony ship after the licence exists, then feed and build the colony until it leaves BOOTSTRAP. Use when a colony ship can be sent or a planet is in BOOTSTRAP.
---

Two parts. **Found** runs once; **Bootstrap** runs every cycle while the planet is in `BOOTSTRAP`.

## Found

1. `codex("astrophysics")` → `effect.planets_allowed` and `colonisable_positions`. Owned planets must be **fewer** than allowed, and research must be *completed*, not in progress (L3). If not, stop: the wake is `queue.completed` for astrophysics.
2. Pick the slot from `strategy/decisions/002-expansion-scope.md` → Decision list, skipping any position no longer empty in `galaxy`. Write `ops/colonies/<COORD>.md` from the template below with `status: planned` **before** launching.
3. `dispatch_fleet(mission="colonize", ships={"colony_ship":1, "small_cargo":n}, cargo={...})`. Cargo for the first hour: ≥ 3 000 metal, 1 000 crystal, 500 deuterium (fits in the colony ship's hold + escorts). Record fleet id, ETA → `status: flying`.
4. On `fleet.returned`/planet appearing in `empire_overview`: create `empire/planets/<COORD>.md` (copy an existing one; state `BOOTSTRAP / powering`, tags from its position bonus, temperature and fields; *Why this planet* from the decision), set the colony file `status: founded`. If no planet appeared: `status: failed`, reason, and a `empire-lesson`.

## Bootstrap (each cycle)

Order, each level only when `codex` says it is affordable *on the colony*: solar plant 1–2 → metal mine 1–4 → crystal mine 1–2 → metal storage 1 → solar to keep factor 1 → metal mine to 8, crystal to 5, deut 1–3 → robotics 2 → storage 2. Transport from the capital every cycle whatever the next two levels need (`dispatch_fleet mission=transport`), logged as a row in the colony file. Leave `BOOTSTRAP` when metal mine ≥ 8, factor = 1, storage ≥ 2 → planet state `GROWING`, colony file `status: closed`.

## Template — `ops/colonies/<COORD>.md`

```markdown
---
target: 5:316:9
status: planned | flying | founded | failed | closed
decision: strategy/decisions/002-expansion-scope.md
reason: <one line — bonus, distance, role>
launched: <ts> | fleet: <id> | eta: <ts>
founded: <ts> | planet_id: <id> | fields: <n> | temp: <a..b>
---
## Transports
| when | M / C / D | fleet | arrived |
|---|---|---|---|
## Notes
lessons: 
```
