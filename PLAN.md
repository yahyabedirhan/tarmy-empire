# Plan — next 24 h from 2026-09-19T08:12Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. One lane per row group (Commander 2026-09-17T19:45Z); each line is a wake → action → gate. Done lines are dropped. Sources: decisions 013 (roles), 014 (roadmap, proposed), 015 (walls, proposed) — **standing priority (Commander 20:55Z): planet 6 + crystal mining first, defence second** — crystal-priced wall parts only from what is left after :1's levels and the research lane.

## Mining (crystal levels ranked empire-wide by payback — 013 clarification)
| when | where | action | gate |
|---|---|---|---|
| ~08:30Z | capital | 6 satellites + crystal_mine 19 (226.7k M / 113.3k C, 80 h payback, 1 field) | 227k M (ship 60k from :9/:10) |
| when metal ≥ 363k | :10 | crystal_mine 20 (362.7k M / 181.3k C, 95 h) — :10 holds ~188k C; keep its metal home | metal |
| when metal ≥ 363k | :9 | crystal_mine 20 (same) — holds ~156k C | metal |
| later | :3 | crystal_mine 21 (580k M / 290k C, 120 h) | metal |
| later | :1 | crystal_mine 22 (928k M / 464k C, 135 h); meanwhile :1 exports ~22k C/h (its 5 LC are at :3 — bring 2 back) | — |
| every cycle | all | `tools/ov.py` on `empire_overview`: pools ≥ 80 % cap; energy spare ≥ 0 before any mine | — |

## Research (014 order — always busy)
| when | action | gate |
|---|---|---|
| 08:39:31Z | espionage 6 lands → computer 10 (204.8k C / 307.2k D; nanite gate) | 307k D at the capital (ship 60k from :9, 25k from :14) |
| after | robotics 9 → 10 at the capital (102k/31k/51k, 205k/61k/102k; 2 fields) → nanite 1 (1M/500k/100k) | metal, deut |
| when crystal allows | lab 9 (51k/102k/51k) — start research from :10's lab 1 while it builds | crystal |

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
