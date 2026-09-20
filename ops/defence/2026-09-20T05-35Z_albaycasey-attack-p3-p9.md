---
when: 2026-09-20T05:35:25Z launch → 06:01:13Z (:3) and 06:07:05Z (:9)
attacker: albaycasey (BTC, rank 23, 33 253) from 5:305:5 (Homeworld, planet 4928)
fleets: 94743 → :3 — 31 ships (cruiser, large_cargo); 94745 → :9 — 228 ships (battlecruiser, battleship, cruiser, heavy_fighter, light_fighter, large_cargo, small_cargo); counts hidden (espionage 6)
status: incoming
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
## After (fill in from `reports kind=combat`)
- result:
- loot taken:
- debris:
- rebuilt:
## Lessons
- Deuterium has no crystal-free sink on a metal-world: a 229k D pool behind a wall a 228-ship fleet can break is loot. Ship deut to the capital's 700k tank the moment a real threat probes (Furukhai/albaycasey day), not after the attack launches. → strategy/LESSONS.md via empire-lesson after the battle.
- The queue is a vault: a paid ship batch (charged at queue time, refundable on cancel) hides crystal from loot in 30 s.
