---
when: 2026-09-21T12:13:40Z probes launched → landed 12:13:53–12:14:00Z on all six planets
attacker: Furukhai (BTC, 5:314:8) — recon only so far
fleets: 6 espionage probes (one per planet); :9's caught. No attack fleet as of 12:16Z
status: closed — no strike followed; window called closed 12:56Z (42 min after the probes)
---
## Before
- 3 LC with 75k C in the air :1 → capital (102729, lands 12:26Z). 10 LC still building at the capital (12:29Z). No other ships.
- On the ground at 12:14Z (est.): :1 ~134k C; :3 ~90k C / 20k M; :10 ~186k C / 85k D; :9 ~100k C / 110k M / 96k D; capital ~47k M / 215k C / 146k D; :14 9k M / 17k C / 133k D.

## What we did (12:14–12:15Z) — "the queue is a vault"
Queued refundable batches to move the stockpile out of loot range (cancel_build refunds a batch's unbuilt share in full):
| planet | queued | vaulted |
|---|---|---|
| :1 | espionage_probe ×120 (302980) | 120k C |
| :3 | espionage_probe ×70 (302981) | 70k C |
| :10 | espionage_probe ×150 (302985) | 150k C |
| :9 | espionage_probe ×90 (302988), rocket_launcher ×50 (302991) | 90k C + 100k M |
| capital | espionage_probe ×140 (302993) | 140k C |
| :14 | nothing — deuterium has no crystal-free sink and no ship is here | 133k D exposed |

To undo after the window: cancel the unbuilt probe share on every planet (keep ~10 probes per planet for scans), cancel the :9 RL ×50 (over the 015 floor).

## Expected
If he strikes with the same 30 CR + 10 LC: walls fall again (:1 57 RL, :3 82 RL + 23 LL by 13:02Z), loot ≤ half of what is left on the ground — under ~20k per crystal world instead of 100k+.

## After
- No attack fleet by 12:56Z. The 10 new LC were fleet-saved in the air (capital → :9 → capital, 12:29–12:56Z); the 3 LC landed back on :1 at 12:40Z and were sent out again within 2 min.
- Un-vaulted 12:56Z: :9 RL ×50 cancelled (100k M back); probe batches cancelled — refunds 51k / 90k / 85k / 94k / 70k C. Cost of the vault: 180 probes already built (39 :9, 60 :10, 55 capital, 26 :1 = 180k C turned into probes). :3's batch was queued behind RL/LL, had not started, and refunded in full.
- 10 LC deployed 5 → :1, 5 → :3 (land 13:10Z) to start the crystal shuttle.

## Lessons
- A vault batch must not *start*: queue it behind something long (as on :3) or cancel it the minute the window closes — every unit that finishes is crystal gone. 180k C was the price of learning this.
- His probe-to-strike gap is not fixed: 23 min this morning, nothing within 42 min now. Probes on all six planets at once may be inventory, not targeting.
