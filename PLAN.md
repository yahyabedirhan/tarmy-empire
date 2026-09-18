# Plan — next 24 h from 2026-09-18T17:05Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. One lane per row group (Commander 2026-09-17T19:45Z); each line is a wake → action → gate. Done lines are dropped. Sources: decisions 013 (roles), 014 (roadmap, proposed), 015 (walls, proposed) — **standing priority (Commander 20:55Z): planet 6 + crystal mining first, defence second** — crystal-priced wall parts only from what is left after :1's levels and the research lane.

## Mining (on-role only, 013)
| when | where | action | gate |
|---|---|---|---|
| ~19:30Z | :1 | crystal 21 (580.3k M / 290.1k C, 7.7 h) after 4 more satellites — metal shuttles hourly from :3/:10/:9/capital | metal |
| after 21 | :1 | crystal 22 priced then (≈ 930k M / 465k C); compare with :3 crystal 21 (290k C) and plasma 6 (128k C) | payback |
| 23:46:51Z | :3 | crystal_mine 20 lands → robotics 6–8 first (idle metal), crystal 21 (290k C) when the defence lane leaves crystal | crystal |
| every cycle | :10, :9 | **no crystal or metal mines** (crystal frozen 19/18; metal over-stocked → stock rule) | — |
| every cycle | :14 | synths only if deuterium gates a plan (it does not) | — |
| every cycle | all | `capcheck.py` ≥ 80 %; energy spare ≥ 0 before any mine | — |

## Research (014 order — always busy)
| when | action | gate |
|---|---|---|
| 19:12:25Z | plasma 5 lands → weapons 9 (204.8k M / 51.2k C, 5.7 h) | 51k C at the capital |
| ~01:00Z 09-19 | computer 8 (51.2k C / 76.8k D) → 9 → 10 (nanite gate, 11 fleet slots) | crystal slack |
| when crystal allows | lab 9 (51k/102k/51k) — start research from :10's lab while it builds (P4 confirmed) | crystal |

## Advanced tech (014 H1)
| when | where | action | gate |
|---|---|---|---|
| 20:58:33Z | :10 | robotics 8 lands; :9 robotics 7 20:46:36Z → 8 next cycle | metal on site |
| 20:15Z | :3 | 25k D lands → robotics 6, 7, 8 (90k M / 27k C / 45k D total; more deut from :14) | deuterium |
| when metal is shipped back | :14 | robotics 5–8 (96k M / 29k C / 48k D) | 100k M from :10 |
| later (H1) | capital | robotics 9 → 10 (fields 2) after the wall batches | metal, deut |

## Defence (015 — metal-worlds first)
| when | where | action | gate |
|---|---|---|---|
| 20:18:37Z | :10 | shipyard 6 lands → SSD (10k/10k), HL ×20 (120k/40k), LL ×50 (75k/25k), RL to 150 (+93, 186k M); gauss ×10 (200k/150k) + LSD (50k/50k) as crystal allows | crystal split answer |
| 20:23:47Z | :9 | shipyard 6 lands → RL to 150 (+100, 200k M), SSD, HL ×20, LL ×50; gauss/LSD later | same |
| 20:49:40Z | capital | RL ×45 lands (184) → RL +16, LL ×40 (60k/20k), HL ×20, ion ×10, gauss ×8 (160k/120k), LSD; silo 1–2 + 10 ABM (rung) | crystal from :3/:1 |
| 21:13:46Z / 22:40:55Z | :3 / :14 | RL batches land (52 / 40) → crystal/deut-world wall (100 RL, 30 LL, 10 HL, 5 ion, 6 gauss, SSD) after shipyard 6 on each | metal on site |
| after robotics 8 | :1 | shipyard 1 (queued) → RL ×100 batch when it holds > 80k | robotics 8 |

## Logistics (013 rule 4)
| when | action |
|---|---|
| now | 3 new LC at the capital (fleet home: 3 LC); :10 1 LC; :9 2 LC + 2 SC; :3 1 LC + 4 SC; :14 1 LC |
| every cycle | :10/:9 metal → capital (armour 10, walls) and :1; :3/:1 crystal → capital (research); :14 deut → :3/:1 robotics; log every flight in the planet file |
| 08:00Z / 20:00Z | `leaderboard` snapshot → `intel/leaderboard/<ts>.json`; `growth.py` in the status report |

## Alliance / intel
| when | action |
|---|---|
| cycle 52 | status report + alliance skim (four things only; nothing sent). Necati/NeC posted 4 messages 19:15–20:00Z — skim then |

Idle on purpose: astro 11 (crystal ≥ 80k/h first); terraformer (4.25M C, 503 free fields); moon (Commander-only); raids (parked); IPM; trades.
