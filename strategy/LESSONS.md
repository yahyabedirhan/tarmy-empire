# Lessons

Numbered, never deleted; a superseded lesson gets a `superseded-by:` line. Each links to the event that taught it. New entries through the `empire-lesson` skill.

## L1 — Energy before ore (2026-09-06)
Queued MM6→7 and CM3→4 before the solar surplus existed; factor fell 0.97→0.83 and every mine on the planet slowed for hours. Source: `archive/STRATEGY.md`. Rule: DOCTRINE → Energy first.

## L2 — A full pool is a leak (2026-09-09 → 11)
The colony sat at its metal cap while the capital held 447k idle metal and an empty queue; days of production were discarded. Source: `archive/COLONY_GROWTH_STRATEGY.md`, `reports/status/2026-09-11T08-00.md`. Rule: DOCTRINE → Never a full pool, Never an empty queue.

## L3 — A colony ship without the licence is a lost ship (2026-09-09)
Two colony ships were sent to 5:316:2 and 5:317:12 with astrophysics 2 (allowance: 2 planets). Both arrived, neither founded a planet, one earlier attempt at 5:317:8 failed the same way. Source: `archive/COLONY_GROWTH_STRATEGY.md`. Rule: DOCTRINE → Colonize (research must be *completed* before launch); `docs/mcp/COMMANDER.md` troubleshooting.

## L4 — One scan, then simulate, then fly (2026-09-08)
2 light fighters were sent at 5:316:7 (nash1999: 3 rocket launchers + 16 light fighters, 432k resources) on the strength of a resource total; both were lost for nothing. Source: `archive/ATTACK.md`. Rule: DOCTRINE → Raid (zero expected losses in `simulate_combat`). The same day a raid on 5:316:8 (Saeed2) "won" 50 resources: an undefended target is not a target unless it holds loot.

## L5 — Crystal is the empire's limiter (2026-09-07)
Seven researches in 46 minutes took crystal from 214k to 8k and cascaded every crystal-priced build into failure. Source: `archive/OPERATIONS_LOG.md`. Rule: `empire/research.md` prices a research chain in full before starting it; crystal-world is the second colony role (decision 002).

## L6 — Session snapshots are not doctrine (2026-09-11)
Five sessions wrote their live status into the strategy files; by session six nobody could tell rule from snapshot. Rule: `AGENTS.md` → Records (one file per event, doctrine separate from state).

## L7 - A soldier dies with the connection (2026-09-11)
Both haiku soldiers were killed by the harness watchdog (600 s without progress) during an hour-long MCP hang, mid-mission. The colonize soldier had already dispatched; the ships soldier had queued 2 of 3 batches. Source: `ops/missions/2026-09-11T08-30_*.md`. Rule: after any soldier failure the Lieutenant re-reads state before redoing anything (a dead soldier may have acted); briefs must be idempotent (check before each spend). No doctrine change.

## L8 — Protection is invested score, and our own growth closes targets (2026-09-11)
Assumed the 5× rule counted held resources (our MCP doc said so) and planned raids on 5:316:8 / :5 / :7 for ~250k loot. All three launches were refused: attacker 1582→1685 vs invested 41 / 114 / 187 — the rule counts only resources *spent* (`docs/game/mechanics.md` → Protection). Between planning (score 712) and launch, 60 light fighters and four researches tripled our score and lifted the floor above every neighbour. Source: `ops/attacks/2026-09-11_G5-S316-P8_Saeed2.md`, `ops/attacks/2026-09-11_G5-S316-P7_nash1999.md`. Rule: DOCTRINE → Raid gains "target invested score ≥ our score ÷ 5, checked at planning *and* at launch; a refused launch is free intel — try it before any other check". Raid with the fleet you have before you grow the fleet or the score.

## L9 — Above the floor, light fighters do not raid (2026-09-11)
The only targets above our 5× floor (Kara6 5:310:8, yuxuanz4 5:311:7, hina_ito 5:312:10) sit behind 30–82 rocket launchers, 20–40 light lasers, heavy lasers, ion cannons and a small shield dome. 62 LF + cargo vs Kara6's wall: draw 10/10, 36 LF lost (~186k) for nothing. Source: `ops/attacks/2026-09-11_G5-S316-P7_nash1999.md` (debrief sim). Rule (Commander, 2026-09-11T15:15Z): **raiding is parked**; growth first (astro 5, mines), defence second where a planet is exposed. No new warships until the Commander reopens raiding; `empire/research.md` row 5 (impulse 4 / cruisers) drops below rows 8–9. Revisit when astro 5 is done or a target ≥ our score ÷ 5 appears with a wall the current fleet beats.


## L10 — The alliance channel is a measured playbook; read all of it (2026-09-11)
BJACK's top members publish numbers, not opinions: the counter-espionage law, the 50 % loot cap, the mine-pricing rule, the energy comparison, the "expansion beats fleet" arithmetic. One full read (`ops/diplomacy/2026-09-11_BJACK-chat.md`) rewrote four doctrine rules that five of our own sessions had not found. Rule: `empire-cycle` step 1 reads the *whole* new chat, and anything with a number goes into the diplomacy file the same cycle.

## L11 — A mine one level ahead is a third worse (2026-09-11)
We took capital mines to 16/14/11 while 5:316:9 sat at crystal 10, where the next level costs 7.9k and pays back its crystal in 5 h; the capital's crystal 15 costs 51.9k and pays back in 18 h. Source: `codex` 2026-09-11T18:10Z, BJACK measurement (NeC: 37.8 vs 28.7 per 1 000). Rule: DOCTRINE → Lowest mine first (decision 008).

## L12 — Hoarding is not a plan; the astro clock is (2026-09-11)
Three planets sat with empty queues at 17:34–18:07Z holding crystal "for astro 5", while a 2.6k-crystal mine would have paid itself back before astro 5 could be afforded, and the capital's energy factor slipped to 0.94 unnoticed. Source: `HANDOFF.md` 18:00Z, `empire_overview` 18:07Z. Rule: DOCTRINE → The astro clock, Never an empty queue (decision 009).

## L13 — Deuterium is the planet-5 gate, and the alliance is drowning in it (2026-09-11)
Astro 6+7 need 180k deuterium; we make 2.8k/h (64 h) against 27 h for the crystal. NeC hit the same wall and solved it with an 80k 1:1 trade; aranella and merttoprak hold 500–600k idle. Source: `research_tree` 18:08Z, chat 547–551. Rule: decision 009 (synthesizers on cold worlds), decision 010 (trade metal for deuterium/crystal, pending Commander).

## L14 — One probe, and know the counter before you send (2026-09-11)
Our spy skill sent three probes per target; three probes triple the counter and add no information. The law `counter = units × probes × 2^(Δesp) / 100` predicted 17/17 readings in the channel. Source: chat 592–625. Rule: DOCTRINE → Spy; `empire-spy` skill step 2.

## L15 — The loop only runs while a session is open (2026-09-12, approved 2026-09-13)
Astrophysics 5 landed 09:37:15Z with a written "Do this first" (colonize 5:316:3), but no session was open to act on it; the colony ship and all three planets' build queues sat idle until cycle 7 opened at 18:16Z (~8.7 h gap). This is the second such gap this chain (previous ~9 h overnight, 2026-09-11). `empire-cycle` already caps the in-session wake at 2 h, so the gap is not a doctrine bug — it happens between sessions, when nobody has opened a chat to run the loop. Source: `ops/colonies/G5-S316-P3.md`, `HANDOFF.md` history (08:45Z entry vs cycle-7 read). Rule: no DOCTRINE change (the 2 h cap already does its job inside a running session); flagged to the Commander as a session-continuity gap — HANDOFF's "Do this first" is only as good as how soon the next session opens.

## L16 — Check the cap of the planet that receives a sweep, before the sweep (2026-09-16, approved 2026-09-17)
Astro 9 needs 703 711 crystal at the capital; the capital's crystal cap was 700 000. Nine crystal hops (~450k) flew toward a target that could never hold the price, and the capital's deuterium sat at its 375k cap from ~12:00Z to 18:20Z (~24k lost). The per-cycle cap check was applied to the colonies' metal, not to the capital's crystal and deuterium — the two pools the whole plan was filling. Caught by the Commander at 14:50Z. Source: `empire/planets/G5-S316-P12.md` 2026-09-16T18:20Z row; `reports/status/2026-09-16T10-50Z.md` (704k and 700k printed side by side, unnoticed). Rule (proposed for DOCTRINE → Never a full pool): (1) every cycle's overview parse prints `stock / cap` for every pool on every planet and flags ≥ 80 % — a script, not an eyeball; (2) before any resource sweep, the receiving planet's cap for that resource must be ≥ the price it is being filled for, else the storage level is queued first.

## L17 — A lost probe is a doorbell; don't scan an account that can already crush you (2026-09-20)
We espionage-scanned Furukhai's 5:314:8 at 19:14:36Z on our own initiative (routine "opportunity" scan, no raid planned — he was already `avoid`). The probe was destroyed (95% counter, his espionage tech well above ours), which the game tells the target about. 42 minutes later he began a fresh probe wave on us (19:56Z) and 1–2 minutes after that launched a coordinated attack that swept all five of our populated planets over the next 65 minutes (`ops/defence/2026-09-20T19-57Z_furukhai-attack-p1.md` and related). The timing is circumstantial, not proven, but the shape matches: we poked an account already flagged `avoid` for being stronger than us, purely for intel we didn't act on, and got noticed. Rule (proposed for DOCTRINE → Spy): don't spend a probe on a target already marked `avoid` (or any account with a fleet stronger than ours) unless there is a concrete decision riding on the answer — routine neighbourhood-watch scans skip accounts we already know we can't touch. A lost probe is not free information; it's a doorbell.

## 2026-09-20 — albaycasey's raid on :3 and :9 (ops/defence/2026-09-20T05-35Z_albaycasey-attack-p3-p9.md)
- **Satellites are the soft belly of a walled planet.** :9's wall fell and took 64 satellites with it; the mines ran at ~0.5 until they were rebought (128k C). A planet that leans on satellites for > 30 % of its energy loses that production the moment its wall breaks — prefer solar plant / fusion levels on planets that get probed, and keep 2k C per satellite in reserve to rebuy fast. Rebuy runs 5 at a time (queue limit); 64 took 50 min of tending.
- **Deuterium has no crystal-free sink.** 116k D was the only real loot; it could have sat in the capital's 700k tank behind LSD + 200 RL. Rule: the hour a real fleet owner probes us, deut on the metal-worlds flies to the capital.
- **The queue is a vault.** A ship batch is charged when queued and refunded when cancelled (190k C hidden and recovered). A building level likewise — cancelling :3's mine to run satellites first returned every credit.
- **The 5× rule is not a wall.** A rank-23 account fielded 228 ships (33 BC, 14 BS). Decision 015's wall sizes (60 cruisers) are a floor for opportunists, not for a BTC fleet; the answer to a 200-ship fleet is empty planets, not turrets.
