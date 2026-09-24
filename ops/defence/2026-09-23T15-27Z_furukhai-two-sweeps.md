---
when: 2026-09-23T15:27:16–15:30:21Z (three planets) and 2026-09-23T21:59:06–22:01:11Z (all six)
attacker: Furukhai (BTC, 5:314:8), W10 / S8 / A11
fleets: 116134–116163 (15:27 sweep); 117823–117837 (21:59 sweep)
status: closed — both landed with no session open; found 2026-09-24T09:27Z
---
## What was lost
| when | planet | his fleet | our wall before (after 70 % rebuild) | loot (M / C / D) | he lost |
|---|---|---|---|---|---|
| 09-23 15:27 | :1 | 30 CR + 10 LC | 29 RL | 17.3k / 179.9k / 0.6k | — |
| 09-23 15:28 | :3 | 30 CR + 10 LC | 33 RL + 7 LL | 69.3k / 98.7k / 0.7k | — |
| 09-23 15:30 | capital | 22 CR + 10 LC | 61 RL + 7 LL | 38.3k / 78.8k / 29.2k | — |
| 09-23 21:59 | :1 | 10 CR + 10 LC | 21 RL | 14.7k / 164.5k / 0.3k | — |
| 09-23 21:59 | :3 | 10 CR + 10 LC | 20 RL + 6 LL | 79.6k / 96.1k / 0.5k | — |
| 09-23 21:59 | :9 | 25 CR + 15 LC | 34 RL + 8 HL | 156.4k / 64.4k / 39.2k | 1 LC |
| 09-23 22:00 | :10 | 50 BS + 50 CR + 10 DS + 20 LC | 110 RL + 15 LL + 9 HL + 11 gauss + 2 ion + SSD | 208.5k / 102.2k / 55.5k | 8 CR (debris 48k M / 16.8k C) |
| 09-23 22:00 | capital | 20 CR + 10 LC | 44 RL + 4 LL | 50.4k / 66.8k / 24.2k | — |
| 09-23 22:01 | :14 | 25 CR + 12 LC | 54 RL | 42.6k / 11.4k / 143.0k | — |

**Totals: 15:27 sweep 125k / 357k / 31k (513k); 21:59 sweep 552k / 505k / 263k (1.32M). 09-23 as a whole, with the 09:05 sweep (`2026-09-22T17-45Z_albaycasey-and-furukhai-sweeps.md`): ~3.5M looted in 13 h.** His cost: 8 cruisers + 1 LC (~250k), and he owns recyclers.

## Pattern
- Three sweeps on 09-23 at 09:05, 15:27, 21:59 — every ~6.4 h, cruiser slices of 10–30 on every planet, the battleship stack only on :10 (the one wall that hurts).
- He chooses by pool size: :1 (crystal pile) and :3 were hit in every sweep.
- Nothing since 22:01Z (11.5 h at 09:27Z) — likely asleep; the next sweep can come at any time.

## Why it landed
- No session open from 09-23T10:00Z to 09-24T09:27Z; every planet's build queue was empty and ~3M sat on the ground again.
- Walls were the 70 % free rebuild of RL-heavy walls — the shape cruisers farm (`2026-09-22T08-27Z_wall-sizing-sims.md`).

## Response (09-24T09:29Z)
- Sims, seed 24: a ~560k mixed wall (40 RL / 40 LL / 20 HL / 6 gauss / SSD) draws his 30-cruiser slice 5/5 (he loses ~920k, loots nothing) but loses to 40 cruisers; a 1.4M wall on :10 still loses to his 50 BS + 50 CR + 10 DS stack (he loses ~530k). No affordable wall beats his main fleet (166 BS + 100 BC + 43 DS, aranella 09-21) — walls only force him to bring it.
- Spent everything spendable at once (loot is half a pool — an empty pool is the defence): 54 large cargo across five planets (lift + fleet-save), mixed walls on :10, :9, :3, capital; shipyard 4 on :14. Proposal to the Commander: decision 016 "empty vault".

lessons: the pool, not the wall, is what he farms — three sweeps in 13 h hit every planet in proportion to its stock; see `strategy/decisions/016-empty-vault.md` (draft).
