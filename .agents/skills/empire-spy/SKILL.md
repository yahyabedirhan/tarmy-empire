---
name: empire-spy
description: Scan foreign planets with espionage probes and record what was seen in intel/ (one file per target planet, one per player). Use for neighbourhood watch rounds, before any raid, or when asked to look at a coordinate.
---

1. **Choose targets.** Neighbourhood watch (decision 005): every occupied slot in 5:310–322 whose target file is older than 12 h. Pre-raid: the named target. `galaxy` shows occupants (10 deut per foreign system).
2. **Send.** `dispatch_fleet(mission="espionage", ships={"espionage_probe": 3})` per target; keep one fleet slot free. Note fleet ids.
3. **Wait** on `next_event` for `fleet.returned`, then `reports(kind="espionage", since_hours=1)`.
4. **Record** per target in `intel/targets/<G-S-P>_<owner>.md` (create from the template; otherwise replace the *Latest scan* block and append one *Scan history* row). Update or create `intel/players/<owner>.md`.
5. **Verdict.** `empty` (nothing to take); `farm` (resources ≥ 30k, defence beatable at zero loss per `simulate_combat`, owner inactive: no change across ≥ 2 scans ≥ 12 h apart); `watch` (loot but defended or active); `avoid` (stronger than us or a BJACK member).
6. Commit `intel: …`.

Done when every scanned target has a fresh *Latest scan* block, a history row and a verdict.

## Template — `intel/targets/<G-S-P>_<owner>.md`

```markdown
---
coord: 5:316:7
owner: nash1999
alliance: 
player: intel/players/nash1999.md
first_seen: <ts>
last_scan: <ts>
verdict: farm | watch | avoid | empty
---
## Latest scan <ts>
resources: M <n> · C <n> · D <n>
fleet: <ship counts or "none seen" or "hidden (esp tech too low)">
defence: <counts>
buildings: <mines/solar/storage levels if shown>
research: <if shown>
activity: <online/last change vs previous scan>
## Scan history
| when | M / C / D | fleet | defence | verdict | note |
|---|---|---|---|---|---|
```

## Template — `intel/players/<name>.md`

```markdown
---
name: nash1999
alliance: 
planets: [5:316:7]
rank: 
activity: active | idle | inactive
last_updated: <ts>
---
## Pattern
<what changes between scans, when they seem online, what they build>
## History with us
<raids on them, raids by them, messages — link ops/ files>
```
