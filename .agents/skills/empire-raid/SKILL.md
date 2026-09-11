---
name: empire-raid
description: Plan, simulate, fly and record a raid campaign against one target — the attack rule of the doctrine, end to end, with one file per campaign in ops/attacks/. Lieutenant only.
---

A campaign is every sortie against one target under one plan. One file per campaign, from the template below, written **before** the first launch.

1. **Eligibility.** Target file in `intel/targets/` with `verdict: farm` and `last_scan` < 2 h, and < 30 min when probes can reach it in minutes (else `empire-spy` first). Owner not in BJACK, not flagged active; if active, stop and take it to the Commander (decision 004, `strategy/ALLIANCE.md`).
2. **Plan.** Cargo needed = min(half of each pool, our capacity). Fleet = enough cargo hold + the escort `simulate_combat` says wins **every run** with expected losses ≤ 5 % of expected loot. Round-trip time from `galaxy`. Check DOCTRINE thresholds: loot ≥ 30 000 and ≥ 15 000 per round-trip hour; one fleet slot stays free. Write the file with `status: planned` and the expected numbers.
3. **Fly.** `dispatch_fleet(mission="attack", …)`. Row per sortie: launch, arrival, fleet id. `status: flying`.
4. **Result.** On `fleet.combat` / `fleet.returned`: `reports(kind="combat", since_hours=1)` → loot, losses, debris, whether defences rebuilt. Fill the sortie row. Update the target's *Scan history* with what the report showed.
5. **Repeat** up to 6 sorties/24 h while the yield stays above threshold and the last report shows no new defence or fleet. Any loss, any refusal, any surprise → stop, `status: closed`, and a `empire-lesson`.
6. Close with `expected vs actual` and `lessons:`; commit `ops: raid <target>`.

Done when the file is `closed` with every sortie row filled.

## Template — `ops/attacks/<YYYY-MM-DD>_<G-S-P>_<owner>.md`

```markdown
---
target: 5:316:8
owner: Saeed2
intel: intel/targets/G5-S316-P8_Saeed2.md
status: planned | flying | closed
opened: <ts>
closed: <ts>
expected: loot <n> · losses 0 · round_trip <h> · yield <n>/h
actual: loot <n> · losses <n> · sorties <n> · yield <n>/h
---
## Plan
<why this target, fleet composition, simulation summary>
## Sorties
| # | launched | fleet | ships | arrived | loot M/C/D | losses | note |
|---|---|---|---|---|---|---|---|
## Debrief
assumptions that held / broke:
lessons: 
```
