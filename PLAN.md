# Plan — next 24 h from 2026-09-19T17:58Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. Sources: decisions 013 (roles), 014 (roadmap, accepted), 015 (walls) — **standing priority (Commander 20:55Z 09-18): planet 6 + crystal mining first, defence second**. Metal is the empire gate now; crystal is slack.

## Mining (crystal levels ranked empire-wide by payback — 013 clarification)
| when | where | action | gate |
|---|---|---|---|
| 20:16:10Z | capital | crystal_mine 19 lands (273945) | — |
| 21:59:52Z | :10 | crystal_mine 20 lands (273923) → 1 more satellite (+124 of +150 queued) | — |
| 22:48:23Z | :9 | crystal_mine 20 lands (274092) | — |
| ~11:00Z 09-20 | :3 | crystal_mine 21 (580k M / 290k C, 120 h) — own 18.5k M/h + :10/:9 surplus | 580k M |
| later | :1 | crystal_mine 22 (928k M / 464k C, 135 h) | metal |
| every cycle | all | `tools/ov.py`: pools ≥ 80 % cap (:14 deut 280k/375k — keep shipping to the capital); energy spare ≥ 0 before any mine | — |

## Research (014 H2 — always busy)
| when | action | gate |
|---|---|---|
| 21:57:04Z | computer 10 lands (274118) → plasma 6 (128k C, 4.3 h) | 128k C at the capital: 50k from :1 (90968, 18:09Z) + 70k from :3 at 19:55Z |
| ~02:15Z 09-20 | plasma 6 lands → hyperspace drive 1 (rung `hyperspace_engines` chain) | crystal from :1/:3 |
| after | HD 2–4 → plasma 7 → weapons 10 → impulse 5 | crystal |

## Advanced tech (014 H1/H2)
| when | where | action | gate |
|---|---|---|---|
| 21:27:09Z | capital | robotics 9 lands (274495) → robotics 10 (205k M / 61k C / 102k D) | 205k M (ship from :3 185k, :10/:9 after 22:00Z) |
| after | capital | nanite 1 (1M / 500k / 100k) — 2 fields | metal (≈ 20 h of :10 + :9 surplus) |
| when 8k C | :14 | deuterium_tank 4 (8k/8k) | crystal |

## Defence (015 — second priority)
| when | where | action | gate |
|---|---|---|---|
| 18:47:03Z | :1 | RL ×25 lands (274128) → wall 50 RL; +25 per 50k M shipped in | metal |
| 19:52:23Z | :14 | RL ×25 lands (274457) → wall 65 RL | — |
| after 22:00Z | :10 / :9 | 1 gauss/h each from own crystal until 10; LSD (50k/50k) after | crystal on site |
| later | capital | LSD + silo 1–2 + 10 ABM when metal is slack | metal |

## Logistics (013 rule 4)
| when | action |
|---|---|
| 18:05Z / 18:09Z | 75k D (90956) and 50k C (90968) land at the capital |
| 19:55Z | :3 → capital 70k C (2 LC + 4 SC) for plasma 6 |
| every cycle | :14 deut → capital (robotics 10, nanite); :1/:3 crystal → capital (research); :10/:9 metal → capital (robotics 10) and :3 (crystal 21) |
| 20:00Z / 08:00Z | `leaderboard` snapshot → `intel/leaderboard/<ts>.json`; `growth.py` in the status report |

## Alliance / intel
| when | action |
|---|---|
| cycle 68 (19:55Z) | status report; alliance skim done 17:30Z (trade tables only) |

Idle on purpose: astro 11 (crystal ≥ 80k/h first); terraformer; moon (Commander-only); raids (parked); IPM; trades.
