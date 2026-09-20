# Plan — next 24 h from 2026-09-20T13:45Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. Sources: decisions 013 (roles), 014 (roadmap, accepted), 015 (walls) — **standing priority (Commander 20:55Z 09-18): planet 6 + crystal mining first, defence second**. Metal is the empire gate now; crystal is slack.

## Mining (crystal levels ranked empire-wide by payback — 013 clarification)
| when | where | action | gate |
|---|---|---|---|
| now | :1 | crystal_mine 22 (928k M / 464k C, 135 h) — next crystal rung by payback | metal (:10/:9 surplus after nanite) |
| after | capital | crystal_mine 20 (363k M / 181k C) | metal |
| later | :1 | crystal_mine 22 (928k M / 464k C, 135 h) | metal |
| every cycle | all | `tools/ov.py`: pools ≥ 80 % cap (:14 deut 280k/375k — keep shipping to the capital); energy spare ≥ 0 before any mine | — |

## Research (014 H2 — always busy)
| when | action | gate |
|---|---|---|
| **first call after re-auth** | plasma 7 (256k C, 8.5 h; rung at 7) — slot idle since 12:25Z | MCP authenticated |
| after | weapons 10 → impulse 5–6; or astro 10 → 11 if the Commander says so (crystal ≥ 80k/h now) | crystal |

## Advanced tech (014 H1/H2)
| when | where | action | gate |
|---|---|---|---|
| when 1M M | capital | nanite 1 (1M / 500k / 100k; rung the_nanites) — :10/:9 metal every cycle (~48k/h) | ~20 h |
| after | capital | nanite 1 (1M / 500k / 100k) — 2 fields | metal (≈ 20 h of :10 + :9 surplus) |
| when 8k C | :14 | deuterium_tank 4 (8k/8k) | crystal |

## Defence (015 — second priority)
| when | where | action | gate |
|---|---|---|---|
| on attack `fleet.incoming` | any | fly cargo + stocks out, lock crystal in a probe batch, alert | — |
| after the raid | :9 | wall rebuilt to 107 RL / 15 LL / 3 HL / 4 ion / 6 gauss / SSD — no refill beyond LSD until BTC's intent is known | — |
| when metal is slack | :14 / :1 | +25 RL per 50k M (walls 65 / 50 now) | metal |
| after 22:00Z | :10 / :9 | 1 gauss/h each from own crystal until 10; LSD (50k/50k) after | crystal on site |
| later | capital | LSD + silo 1–2 + 10 ABM when metal is slack | metal |

## Logistics (013 rule 4)
| when | action |
|---|---|
| every cycle | deut on :10/:9/:14 → capital 700k tank (raid lesson); crystal on :10/:9 → capital research |
| every cycle | :14 deut → capital (robotics 10, nanite); :1/:3 crystal → capital (research); :10/:9 metal → capital (robotics 10) and :3 (crystal 21) |
| 20:00Z / 08:00Z | `leaderboard` snapshot → `intel/leaderboard/<ts>.json`; `growth.py` in the status report |

## Alliance / intel
| when | action |
|---|---|
| cycle 72 | status report + alliance skim |
| open | **BTC raided us** — Commander decides whether BJACK is told; Furukhai scanned all six planets 12:51Z |

Idle on purpose: astro 11 (crystal ≥ 80k/h first); terraformer; moon (Commander-only); raids (parked); IPM; trades.
