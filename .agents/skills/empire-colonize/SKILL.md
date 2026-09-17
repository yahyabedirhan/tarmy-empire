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

Order by the planet's role, each level only when `codex` says it is affordable *on the colony*. **Storage first when a feed will exceed 50k of any resource** (level-0 caps are 50k; a feed may land over the cap but the planet's own production stops there): metal storage 1–2 and crystal storage 1 before the first large feed, deuterium tank 1–2 before synth 8.
- `crystal-world` (decision 013): solar 1–2 → metal 1–3 → crystal 1–2 → metal 4–6 → metal storage 1 → robotics 1–2 → crystal 3+ with solar to keep factor 1 → crystal storage 1–2 → exit at crystal ≥ 5, factor 1, storage ≥ 2. **Metal stops at 6, no synthesizers**: every later metal and deuterium bill is shipped in (a same-system transport is 13 min and 5 deuterium). Robotics to 5 before the first crystal level that takes > 1 h. 5:316:1 went founding → exit in 40 min this way (`ops/colonies/G5-S316-P1.md`).
- `metal-world`: solar 1–2 → metal 1–4 → crystal 1–2 → metal storage 1 → solar to keep factor 1 → metal to 8, crystal to 5 → robotics 2 → storage 2.
- `deut-world` (cold slot): solar 1–2 → metal 1–2 → robotics 1–2 → deuterium synthesizer and solar plant alternating (read `energy_after` in `planet_detail` before each synth) → tank 1–2 by synth 8 → metal to 6, crystal to 2 → storage 1–2 → keep alternating synth/solar. 5:316:14 reached synth 10 in 2 h 14 min this way (`ops/colonies/G5-S316-P14.md`). Transport from the nearest stocked planet every cycle whatever the next two levels need (crystal from the crystal-world, metal from a metal-world) (`dispatch_fleet mission=transport`), logged as a row in the colony file. Leave `BOOTSTRAP` when the role's target is met (crystal ≥ 5 / metal ≥ 8 / synth ≥ 10), factor = 1, storage or tank ≥ 2 → planet state `GROWING`, colony file `status: closed`.

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
