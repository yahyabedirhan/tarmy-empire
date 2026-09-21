---
when: 2026-09-21T16:12:16Z launch → 16:33:04Z landing (capital 5:316:12)
attacker: Furukhai (BTC, 5:314:8, Bakim)
fleets: 103709 — 85 ships (cruiser + large_cargo, split hidden); W10/S8/A11 last seen
status: closed — wall wiped, loot held to 31k (29k D)
---
## Before
- Probe wave 16:08–16:11Z on all six planets (capital first, 16:08:56Z); attack launched 16:12:16Z — 3 min 20 s after the capital probe landed. Second full-empire probe of the day (12:13Z produced no strike).
- Capital at 16:08Z (est.): ~260k C, ~50k M, ~150k D; 215 RL, 10 LL, 1 SSD; 55 probes; no cargo (13 LC spread over :1/:10).

## What we did
- 16:08:57Z gauss ×2 (305192, → 16:42Z) and espionage_probe ×250 (305195) queued *behind* it — 250k C vaulted, nothing starts before 16:42Z so the cancel refunds in full.
- 16:10:52Z 5 LC :10 → :14 (103702, 16:24Z) to lift :14's deuterium, since :14 was probed too.
- 16:12:27Z 55 probes deployed to :1 (103711, landed 16:12:36Z).
- 16:12:34Z 8 LC :1 → capital (103713, lands 16:25:52Z) to lift ~150k D + the metal before 16:33Z.
- :9 gauss ×1 + probes ×40, :3 RL ×5 + probes ×40 queued as small vaults; :10 vault refused (crystal short after shielding 8 was paid from there).

## Expected
Wall falls in 2–3 rounds (015: 215 RL vs ~75 CR — same as 09-20). Loot ≤ half of what stays on the ground: target < 30k after the LC lift.

## After (`reports` 62465, 16:33:06Z)
- 70 CR + 15 LC vs 215 RL + 10 LL + 1 gauss + SSD + 48 sats → attacker in 3 rounds. He lost 1 cruiser + 2 large cargo (debris 9.6k M / 34.5k C — we have no recycler). We lost 215 RL (159 rebuilt), 10 LL (5 rebuilt), gauss 1, SSD (rebuilt), all 48 satellites.
- **Loot: 910 M / 769 C / 29 057 D.** The lift (103772, 40k M / 99k C / 60k D → :10) and the 250k C vault held; the probe batch was cancelled 16:33Z with a full refund. Same fleet took 126.8k C / 120.3k D / 30.6k M here on 09-20.
- Cost to us: 48 satellites (96k C / 24k D) + 56 RL + 5 LL + 1 gauss to the floor. Re-queued satellites 16:33Z, 5 at a time.

## Lessons
- Loot denial works: probe → lift + vault within 15 min held loot to 31k against an 85-ship fleet. He paid 54k in ships for it. Keep doing exactly this on every probe.
- Satellites are the real recurring loss on the capital (third time: 43, 48 today); each sweep costs ~100k C. Hardened energy on the capital (fusion — also the only deuterium sink we have — and solar plant 18) should replace part of the satellite bank.
- Full-empire probe waves: 12:13Z → nothing, 16:08Z → strike in 3.5 min. Treat every capital probe as a launch.
