---
when: 2026-09-20T19:57:14Z launch → 20:18:02Z (:1)
attacker: Furukhai (BTC, rank 7) from 5:314:8 (Bakim, planet 5002)
fleets: 98920 → :1 — 40 ships (cruiser, large_cargo), split hidden (no fresh scan on his side; ours was lost 19:14Z)
status: closed — lost, wall wiped, ~half the crystal saved
---
## Before
- Furukhai probed us 18:04Z (capital + :14, both destroyed); our return probe on 5:314:8 was lost (19:14Z, counter 95%) — read only M 3.4M/C 1.12M/D 1.25M, no fleet/defence intel.
- Alliance chat (necati/NeC, 18:13–19:14Z) flagged a ~90 min recon-to-strike pattern for BTC; his 18:04Z probe on us put our risk window at ~19:34–19:49Z. That window passed clean, then two more probes landed on us (:1 19:56:13Z, capital 19:56:41Z) immediately followed by this attack launch 19:57:14Z — the real recon was the second probe wave, not the first.
- :1 at 19:57Z: 15.9k M / 344.5k C / 3.3k D; wall 50 RL only (no lasers/gauss/dome — weakest wall in the empire); 3 large cargos at home (just returned from the 19:25Z crystal run).

## What we did (19:57:14–19:58:07Z)
- rocket_launcher ×7 queued (293773, 14k M) → 20:11:24Z, wall to 57 RL before the attack lands.
- 3 LC dispatched to the capital (98923) with 60k C + 3k D, arrives 20:11:25Z (well clear of the 20:18:02Z attack). Cargo capacity (75k) could not clear the full 344.5k C stockpile — ~284.5k C plus ~2k M left exposed.
- `simulate_combat` (guessed 35 CR / 5 LC, W9/S7/A10 — his tech unknown, used our own as a floor) vs 57 RL: attacker wins round 1, we lose the entire wall, he loses nothing. Confirms the wall was never going to hold; evacuation was the only lever.

## Expected
- :1 wall (57 RL) wiped. Loot ≈ half of whatever crystal/metal remains after evacuation (~284k C / ~2k M) minus whatever his large_cargo capacity can't lift.

## After (`reports kind=combat` 60415)
- :1 20:18:06Z: 30 CR + 10 LC (W10/S8/A11) vs 57 RL + 7 sats → attacker in 2 rounds, no losses; we lost the wall (57 RL, rebuilt 44) + 7 satellites; loot 146.1k C / 1.3k M / 141 D. Left ~138k C on the ground uncollected (his cargo or the drop math didn't clear it all) — first thing to secure next cycle.
- Same launch (98921) also hit the capital 20:18:33Z, 31s later — see `2026-09-20T19-58Z_furukhai-attack-capital.md`. One recon window, two simultaneous strikes.

## Lessons
- The ~90 min recon-to-strike read from alliance chat (necati/NeC) was wrong for us: the second probe wave (19:56Z) was the real trigger, launching 1 minute later — not the first (18:04Z). Watch every probe as a possible trigger, not just the first of a session.
- :1's wall (50 RL, no lasers/gauss/dome) was undersized for its stock (344k C) relative to every other colony. 015 doctrine (walls are a floor, not a fleet answer) held — evacuation, not more RL, is what saved the 60k C.
- His tech (W10/S8/A11) is a level above our own (W9/S7/A10) — one tier ahead across the board.
