# Plan — next 24 h from 2026-09-19T17:58Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. Sources: decisions 013 (roles), 014 (roadmap, accepted), 015 (walls) — **standing priority (Commander 20:55Z 09-18): planet 6 + crystal mining first, defence second**. Metal is the empire gate now; crystal is slack.

## Mining (crystal levels ranked empire-wide by payback — 013 clarification)
| when | where | action | gate |
|---|---|---|---|
| ~03:00Z 09-20 | :3 | crystal_mine 21 (580k M / 290k C, 120 h) — holds ~371k; :10/:9 ship every hour | 580k M |
| later | :1 | crystal_mine 22 (928k M / 464k C, 135 h) | metal |
| every cycle | all | `tools/ov.py`: pools ≥ 80 % cap (:14 deut 280k/375k — keep shipping to the capital); energy spare ≥ 0 before any mine | — |

## Research (014 H2 — always busy)
| when | action | gate |
|---|---|---|
| 02:13:11Z 09-20 | plasma 6 lands (277102) → hyperspace drive 1 (rung `hyperspace_engines` chain) | crystal from :10/:1 |
| after | HD 2–4 → plasma 7 → weapons 10 → impulse 5 | crystal |

## Advanced tech (014 H1/H2)
| when | where | action | gate |
|---|---|---|---|
| after :3's crystal 21 is queued | capital | robotics 10 (205k M / 61k C / 102k D; rung hands_of_many) | 205k M from :10/:9 |
| after | capital | nanite 1 (1M / 500k / 100k) — 2 fields | metal (≈ 20 h of :10 + :9 surplus) |
| when 8k C | :14 | deuterium_tank 4 (8k/8k) | crystal |

## Defence (015 — second priority)
| when | where | action | gate |
|---|---|---|---|
| on attack `fleet.incoming` | capital | deploy 62 LF + colony ship + LC to :10; alert | — |
| when metal is slack | :14 / :1 | +25 RL per 50k M (walls 65 / 50 now) | metal |
| after 22:00Z | :10 / :9 | 1 gauss/h each from own crystal until 10; LSD (50k/50k) after | crystal on site |
| later | capital | LSD + silo 1–2 + 10 ABM when metal is slack | metal |

## Logistics (013 rule 4)
| when | action |
|---|---|
| 23:22Z | 75k D :14 → :10 (92341) lands; :14 keeps ~20k D |
| every cycle | :14 deut → capital (robotics 10, nanite); :1/:3 crystal → capital (research); :10/:9 metal → capital (robotics 10) and :3 (crystal 21) |
| 20:00Z / 08:00Z | `leaderboard` snapshot → `intel/leaderboard/<ts>.json`; `growth.py` in the status report |

## Alliance / intel
| when | action |
|---|---|
| cycle 72 | status report + alliance skim |
| open | BTC probe day — Commander decides whether BJACK is told |

Idle on purpose: astro 11 (crystal ≥ 80k/h first); terraformer; moon (Commander-only); raids (parked); IPM; trades.
