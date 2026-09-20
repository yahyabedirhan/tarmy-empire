---
when: 2026-09-20T19:57:45Z launch → 20:18:33Z (capital, 5:316:12)
attacker: Furukhai (BTC, rank 7) from 5:314:8 (Bakim, planet 5002)
fleets: 98921 → capital — 100 ships (70 cruiser / 30 large_cargo, W10/S8/A11)
status: closed — lost, wall + all 43 satellites wiped, fleet saved in full
---
## Before
- Launched 31s after the :1 strike (98920) — same recon window, two simultaneous targets, both from 5:314:8.
- Capital at 19:58Z: ~250k M / ~180k C / ~275k D; wall 200 RL / 10 LL / 2 gauss / SSD / LSD; fleet 62 LF / 1 LC / 2 recyclers / 1 colony ship / 9 probes; 43 solar satellites (energy-critical, factor exactly 1 before the raid).

## What we did (19:58:14–19:59:33Z)
- `simulate_combat` (guessed 90 CR / 10 LC, W9/S7/A10 — floor estimate) vs full wall + fleet: total wipe in 3 rounds, we lose everything including the colony ship, he loses ~3 CR/1 LC. Confirmed the wall could not hold regardless of size.
- Deployed the entire mobile fleet (62 LF, 1 LC, 2 recyclers, 1 colony ship, 8 probes — 9th probe was already gone) to 5:316:10 (strongest wall in the empire) loaded with 35k M / 25k C / 15k D. Departed 19:59:33Z, arrives 20:24:43Z — clear of the attack window either way since it left the planet.
- Could not evacuate more: no ships remained at the capital after the deploy, and the shipyard was mid-upgrade (shipyard 9, lands 20:20:05Z) so no new cargo could be built in time.

## After (`reports kind=combat` 60417)
- 20:18:36Z: 70 CR + 30 LC (W10/S8/A11) vs 200 RL + 10 LL + 2 gauss + 2 domes + 43 satellites → attacker in 4 rounds; he lost 4 CR + 1 LC; we lost the entire wall (rebuilt 140 RL / 9 LL / 1 SSD — LSD and gauss did NOT rebuild) + all 43 solar satellites (0 rebuilt, they don't auto-rebuild); loot 126.8k C / 30.6k M / 120.3k D; debris 25.8k M / 36k C.
- **Energy crisis**: 43 satellites gone and not rebuilt automatically — capital production factor will have crashed. First action next cycle: rebuild energy (satellites or fusion) before anything else, per the STALLED/energy doctrine row.
- Fleet-saved: 62 LF, 1 LC, 2 recyclers, 1 colony ship, 8 probes all alive at 5:316:10 (arrives 20:24:43Z). The colony ship — the one asset that can't be rebuilt in a day — survived.

## Lessons
- Solar satellites are the soft belly and don't rebuild like defence does (confirms the 2026-09-20 draft lesson in `strategy/LESSONS.md`, still awaiting Commander approval) — 43 lost here on top of :9's 87 earlier today. A raid that reaches the satellites is an energy attack, not just a resource one.
- The large/small shield domes did not appear in `defender_defenses_rebuilt` — domes do not partially rebuild at 70% like rocket launchers/lasers do; they are all-or-nothing losses.
- Fleet-save worked: evacuating the mobile fleet 19 minutes before impact saved 100% of the ships (including the irreplaceable colony ship) at the cost of only the resources that could fit in their cargo holds.
- His tech W10/S8/A11 vs ours W9/S7/A10 — one full tier ahead on weapons, shielding and armour. He wins any straight fight regardless of our wall size, which matches 015's standing read (empty planets + evacuation over more turrets).
