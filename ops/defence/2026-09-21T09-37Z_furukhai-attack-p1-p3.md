---
when: 2026-09-21T09:37:16Z (:1) and 09:37:36Z (:3) — landed while no session was open (last hand-off 06:45Z)
attacker: Furukhai (BTC, 5:314:8, Bakim)
fleets: 101996 → :1, 101999 → :3 — 30 cruiser + 10 large_cargo each (W10/S8/A11)
status: closed — lost, both walls wiped, :3 satellites wiped, ~345k C looted
---
## Before
- Furukhai probed :10 at 06:58Z and 09:14Z (both destroyed). No session was open; nothing was evacuated.
- :1 held ~267k C + ~7k M with 50 RL and the 3 LC that had come from :14 (deploy). :3 held ~243k M / ~262k C / ~40k D with 82 RL + 23 LL + 27 satellites.

## What happened (`reports` 61751, 61753)
| planet | his fleet | our wall | rounds | his loss | our loss | loot |
|---|---|---|---|---|---|---|
| :1 | 30 CR + 10 LC | 50 RL + 3 LC | 2 | none | 50 RL (34 rebuilt), 3 LC | 224.6k C / 6.9k M / 71 D |
| :3 | 30 CR + 10 LC | 82 RL + 23 LL + 27 sats | 3 | 1 LC | 82 RL (55 rebuilt), 23 LL (14 rebuilt), 27 sats | 121.1k C / 112.0k M / 20.0k D |

- :3 dropped to production_factor ~0.54 (1470 / 2740 E) — this is the "bleeding energy" the Commander reported at 11:30Z.
- Third-party recon followed: engin (5:298:7/8) probed :10 + capital 10:44Z and :1 + :9 10:57Z — all destroyed.

## What we did (11:30–11:35Z)
- :3: 27 solar_satellite queued in rounds of 5 (soldier mission `ops/missions/2026-09-21T11-33_satellite-rebuild-p3.md`), 2k C / 500 D each — :3 had exactly enough deuterium (20k) for 27.
- Logistics restart: 10 large_cargo queued at the capital (302506, 60k M / 60k C, lands 12:29Z); :14's 3 LC deployed to :1 (102565, lands 11:45Z) carrying 40k M / 20k D so :1 can rebuild its floor and the LCs can lift crystal to the capital.
- Research: impulse 5 queued (302505 → 13:39Z), 64k C sunk at the capital.
- :10: metal 21 + 4 sats + LL 7 / gauss 1 / HL 1 (015 floor). :9: metal 20 + 4 sats + LL 5 / gauss 2. Capital: LL 1.

## Lessons
- Same attacker, same fleet (30 CR + 10 LC), same two crystal worlds, ~13 h after his sweep — he farms whatever crystal sits on :1 and :3. With no cargo fleet since 09-20 the crystal could not leave; the exposed pile *is* the trigger. Cargo capacity is a defence, not a convenience (feeds pending L-lesson "the queue is a vault").
- An unattended empire (06:45–11:30Z) cannot evacuate: the loop only lives while the chat is open (`AGENTS.md`). Anything left on a crystal world overnight should be assumed lost.
