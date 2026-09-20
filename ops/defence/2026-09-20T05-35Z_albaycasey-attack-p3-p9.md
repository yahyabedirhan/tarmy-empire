---
when: 2026-09-20T05:35:25Z launch → 06:01:13Z (:3) and 06:07:05Z (:9)
attacker: albaycasey (BTC, rank 23, 33 253) from 5:305:5 (Homeworld, planet 4928)
fleets: 94743 → :3 — 31 ships (cruiser, large_cargo); 94745 → :9 — 228 ships (battlecruiser, battleship, cruiser, heavy_fighter, light_fighter, large_cargo, small_cargo); counts hidden (espionage 6)
status: closed — both battles lost, loot small, energy rebuilt
---
## Before
- Probe sweeps: 23:03Z (5 planets, all caught), 05:08Z (:3, :9, both caught). ops/threats/2026-09-19T22-42Z_furukhai-probe-sweep.md.
- :9 at 05:36Z: ~4k M / 197k C / 229k D; wall 150 RL / 20 LL / 5 HL / 5 ion / 6 gauss / SSD; 2 LC + 2 SC.
- :3 at 05:36Z: ~106k M / 102k C / 7k D; wall 52 RL; 2 LC + 4 SC; crystal 21 building (paid).
## What we did (05:36–05:38Z)
- 94749: :9 2 LC + 2 SC deploy → :10 with 60k D. 94750: :3 2 LC + 4 SC deploy → :10 with 70k C.
- :9: gauss ×2 (282219, 40k/30k/4k, paid) ; **espionage_probe ×190 (282234, 190k C, paid up front, builds after 06:24Z) — cancel after the battle for the refund**.
- :3: RL ×45 (282220, 90k M, paid; ~5 finish before 06:01Z).
- :1: 75k C → capital (94759).
- simulate_combat (guess 5 BC / 15 BS / 40 CR / 60 HF / 100 LF / 8 cargo) vs :9 wall: attacker 5/5, his loss ~178k, ours 662k before the 70 % rebuild.
## Expected
- :9 wall falls; loot ≈ half of 4k M / 7k C / 229k D ≈ 115k D. :3: 52 RL fall; loot ≈ 8k M / 16k C.
## After (`reports kind=combat` 58213, 58237)
- :3 06:01:16Z: 25 CR + 6 LC (W6/S6/A10) vs 57 RL + 23 sats → attacker; he lost 1 LC; we lost 57 RL (41 rebuilt) + 23 satellites; loot 11.8k M / 19.5k C / 3.5k D; debris 1.8k M / 15.6k C.
- :9 06:07:06Z: 33 BC / 14 BS / 69 CR / 36 HF / 35 LF / 28 LC / 13 SC (W6/S6/A10) vs full wall + 64 sats → attacker in 3 rounds; he lost 2 CR / 5 HF / 10 LF / 2 LC / 6 SC; we lost the wall (rebuilt 107 RL / 15 LL / 3 HL / 4 ion / 5 gauss / SSD) + 64 satellites; loot 7.8k M / 7.1k C / 115.8k D; debris 37.2k M / 58.8k C — our 2 recyclers took 20k/20k (94960).
- 06:07–07:00Z: probe batch cancelled (190k C refunded); satellites rebuilt 5 at a time (:9 → 64, :3 → 27); :3's crystal 21 cancelled (full refund) so the sats could go first, requeued 06:48Z → 14:36:31Z (cost: 4.8 h of build progress, worth ≈ 12k C; the 3 h at factor ~0.5 would have cost ≈ 45k).
- Net: ≈ 165k loot + ≈ 200k of satellites + wall rebuild 30 % (≈ 120k) against his ≈ 200k of ships. He knows our walls now.
## Lessons
- Deuterium has no crystal-free sink on a metal-world: a 229k D pool behind a wall a 228-ship fleet can break is loot. Ship deut to the capital's 700k tank the moment a real threat probes (Furukhai/albaycasey day), not after the attack launches. → strategy/LESSONS.md via empire-lesson after the battle.
- The queue is a vault: a paid ship batch (charged at queue time, refundable on cancel) hides crystal from loot in 30 s.
