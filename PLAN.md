# Plan — next 24 h from 2026-09-20T19:16Z, in lanes

Rolling plan, rewritten at every hand-off (`empire-cycle` step 7). Times UTC. Sources: decisions 013 (roles), 014 (roadmap, accepted), 015 (walls) — **standing priority (Commander 20:55Z 09-18): planet 6 + crystal mining first, defence second**. Metal is the empire gate now; crystal is slack.

## Mining (crystal levels ranked empire-wide by payback — 013 clarification)
| when | where | action | gate |
|---|---|---|---|
| when metal allows | :10 | metal_mine 21 (200k M / 50k C) — energy fixed by solar_plant 19 this cycle | metal (short ~4k, +25k/h) |
| when metal allows | :9 | metal_mine 20 (133k M / 33k C) — energy fixed by solar_plant 19 this cycle | metal (short ~3k, +23k/h) |
| when metal allows | :1 | crystal_mine 22 (928k M / 464k C, 135 h) — next crystal rung by payback | metal (:1 has only metal_mine 6) |
| after | capital | crystal_mine 20 (363k M / 181k C) | metal |
| every cycle | all | pools ≥ 80 % cap; energy spare ≥ 0 before any mine | — |

## Research (014 H2 — always busy)
| when | action | gate |
|---|---|---|
| running | plasma 7 (256k C) → lands **2026-09-21T03:43:49Z** | — |
| after | weapons 10 → impulse 5–6; or astro 10 → 11 if the Commander says so (crystal ≥ 80k/h — trigger fired) | crystal |

## Advanced tech (014 H1/H2)
| when | where | action | gate |
|---|---|---|---|
| when 1M M | capital | nanite 1 (1M / 500k / 100k; rung the_nanites) — :10/:9 metal every cycle (~48k/h) | ~15 h |
| when metal/crystal allow | :14 | deuterium_synthesizer 17 (148k M / 49k C) — planet is poor, needs a shuttle | metal + crystal |

## Defence (015 — second priority)
| when | where | action | gate |
|---|---|---|---|
| on attack `fleet.incoming` | any | fly cargo + stocks out, lock crystal in a probe batch, alert | — |
| **watch ~19:34–19:49Z** | capital / :14 | BTC recon-to-strike pattern (~90 min after Furukhai's 18:04Z probe) — no fleet inbound yet | — |
| after the raid | :9 | wall rebuilt to 107 RL / 15 LL / 3 HL / 4 ion / 6 gauss / SSD — no refill beyond LSD until BTC's intent is known | — |
| when metal is slack | :14 / :1 | +25 RL per 50k M (walls 85 / 50 now) | metal |
| later | capital | silo 1–2 + 10 ABM when metal is slack (missile_silo needs shipyard 9, landing 20:20:05Z) | metal |

## Logistics (013 rule 4)
| when | action |
|---|---|
| every cycle | deut on :10/:9/:14 → capital 700k tank (raid lesson); crystal on :10/:9/:1 → capital research |
| every cycle | :10/:9 metal → capital (nanite 1) |
| 20:00Z / 08:00Z | `leaderboard` snapshot → `intel/leaderboard/<ts>.json`; growth in the status report |

## Alliance / intel
| when | action |
|---|---|
| cycle 76 (done) | status report + alliance skim — flagged BTC recon-to-strike pattern from necati/NeC |
| open | **BTC raided us (albaycasey)** — Commander decides whether BJACK is told; Furukhai probed us again 18:04Z, scan on 5:314:8 confirms `avoid` (huge stock) |
| cycle 80 | next status report |

Idle on purpose: terraformer; moon (Commander-only); raids (parked, no clean farm target); IPM; trades. Astro 10/11 waits on the Commander's go (trigger fired).
