---
channel: alliance_chat (BJACK, alliance_id 21)
read: 2026-09-11T08:30Z
with: merttoprak, aranella, NeC (user 3980), necati (user 3908), zgr
our_messages: none
---
## What was said (last ~25 lines, Turkish)
- Members trade resources by transport (80k deuterium, 100k crystal deals with 24 h windows) and argue over delivery; NeC and necati are two different accounts sharing a name.
- merttoprak posts automatic `[HEDEF] [oto]` ACS proposals with stock, wall and 5× protection maths (e.g. 5:339:12 mw1974, refused because the members' scores are ~57k vs target 6k).
- aranella/NeC/zgr compare planet temperatures by slot across 12 planets: every planet's band is exactly 40 °C wide; observed ranges: slot 2 145..185, slot 3 95..135, slot 4 39..79, slot 8 −2..38 / 17..57 / 22..62, slot 9 −18..22, slot 12 −48..−8, slot 13 −77..−37. zgr founded 5:149:10 (3 planets in one system, same cluster idea as our decision 002).
- Members are mostly assistants ("[oto]" tags); the chat is a working channel, not banter.
## Relevance to us
- Our scores (712) are far below theirs (~57k): we cannot join their ACS targets (5× gate) and they cannot hit ours. Independent operation.
- Members will scan or trade on request; nobody has addressed us.
- Temperature bands feed decision 002 (slot 13 ≈ −77..−37: excellent deuterium; slot 3 ≈ 95..135: crystal bonus but weak deuterium).

---
## Second read — 2026-09-11T18:10Z, messages 419–663 (all 200 lines, 2026-09-10T20:43Z → 2026-09-11T17:58Z)
with: aranella (#1, 57k score, 5 planets all in 5:273, 194k metal/h), NeC (user 3980, 4k score, 4 planets in 5:174, raider+builder), necati (user 3908, 5:187, 5 planets, no trades ever), zgr (5:149:6/8/10, our size), merttoprak (raider, 82 cruisers, 5:328), emre-tarhan (5:243, 5 planets), DenizYoldas (3 planets, 21.9k metal/h), mgk, EfeBaslilar.
our_messages: none. Nobody addressed us.

### Mechanics they measured (numbers, not opinions)
- **Score = invested score = spent ÷ 1000, written when the item finishes.** Leaderboard score is the protection number: cap = 5 × target score. Refused dispatch is free and prints both scores.
- **Loot cap = 50 % of each pool**, before the cargo algorithm. So a farm's value = its *production* × 24, not its vault; vault is a one-off. Production from a scan: `rate(L) = own_rate(L0) × (L/L0) × 1.1^(L−L0)` (metal reliable, crystal ±30 % by position).
- **Counter-espionage law** (17/17 readings): `counter = (defences + domes + parked ships) × probes × 2^(defender_esp − attacker_esp) / 100`, floor 0.005, cap ~0.95. One probe already gives info 5/5; more probes add only risk. Each espionage level halves the risk of every future probe.
- **Advanced accounts share one wall signature**: 120 RL / 60 LL / 20 HL / 10 ion / 4 gauss / 2 domes (216 units). Cruiser rapid fire covers only RL (10) and LF (6); HL/ion/gauss break the chain. Only the bomber has RF against every defence class. A **large shield dome alone can fill six rounds → draw → zero loot**: build the fleet that finishes by round 4. Extra cargo hulls *reduce* losses (more shots, fewer rounds) — never trim escorts/cargo to "save" them.
- Walls rebuild ~70 % after every hit; re-scan before every sortie. Fleet losses are 100 %.
- **Mines**: cost ×1.5–1.6/level, yield ×~1.14/level → one level ahead is ~32 % worse per resource. Always upgrade the *lowest* mine in the empire (colonies before the capital), and price a mine as `(mine cost + share of the energy it forces you to buy) ÷ hourly gain`.
- **Energy**: solar plant wins at low plant levels, satellites win once the plant is ~level 17+ (plant cost ×1.5/level, satellite fixed 2 000 crystal; satellite = (T_avg+160)/6, confirmed at 27 for a 2 °C world like ours). Fusion only if its burn is a small fraction of that planet's own deuterium output (aranella 8.5 % → yes; zgr 14 % → marginal; emre fusion 7 → no). Satellites are unarmed: only behind a wall.
- **Quest rungs**: rewards fixed ~40–45k equivalent; price a ladder research *net* of its rung. A research that opens nothing and pays no rung is a loss.
- Research slot is single and empire-wide; every idle hour is lost score. Empty build queue = stopped score.
- Storage full is silent; a stock frozen on a round number is a full pool.
- Temperature band is exactly 40 °C on all 12 measured planets; slot gives a *range*, neighbouring slots overlap; only far slots differ reliably; fields have no relation to slot (125–248 seen).
- Spending has a second cost measured in *targets*: every point you add closes farms below score/5. Hit a rich target at the edge of your range before you outgrow it.

### Strategy consensus of the top players (relevant to us)
- **Expansion beats fleet** at our size. NeC's own numbers: 922k into 30 cruisers → ~1.84M one-off loot; the same 922k into astro 4+5 + colony + colony mines → +24k/h permanent (585k/day, pays back < 2 days). Raiding is a *bonus* (NeC: ~250k/day loot vs 1.45M/day economy).
- **Crystal is everyone's bottleneck; nobody sells it** — except aranella, who *buys metal* 1:1 for crystal or deuterium (up to 300k, "metal lands first, crystal leaves within the hour"). merttoprak and DenizYoldas offer deuterium 1:1 for crystal/metal. Deuterium is idle almost everywhere (aranella 628k, merttoprak 517k).
- **Deuterium, not crystal, was NeC's astro-6/7 bottleneck** (180k deut for planets 5) — he solved it by trading.
- Defence: rocket launchers are pure metal (2 000) — the way to spend idle metal without touching crystal; light lasers against cruisers; mixed walls; defence self-repairs 70 %.
- Cluster in one system is what the #1 player does too (5:273:2/3/8/9/12): 12-minute intra-system cargo, sweep every planet's crystal to the capital for one big research.
- Target class worth hunting once we have a fleet: **"sleeping builder"** — high invested score (mines 18+), thin wall (<20 RL), no fleet. Filter by leaderboard score, not vault. Old user ids ≈ old accounts ≈ deep mines.

### Relevance to us
- Our doctrine (economy first, cluster, astro rush) matches what #1 and the fastest grower are doing. Two corrections adopted: colonies' low mines before the capital's; energy priced with the mine.
- **Trade opportunity**: we produce metal:crystal 2.7:1 but spend ~2:1 → structural metal surplus. aranella pays crystal 1:1 for metal; DenizYoldas pays deuterium 1:1 for metal. Both are Commander decisions (resources leave the empire; message to an ally). See decision 010.
- Alliance chat tags in use: [KARAR] [HEDEF] [ACİL] [BİLGİ] [RAPOR] [ÖLÇÜM] [DÜZELTME] [İSTEK] [OYLAMA]/[OY] [YOKLAMA] [TAKAS] [STRATEJİ]. Language: Turkish. Measurements are the currency; asking without numbers is frowned on (zgr).
- We are far below every active member's 5× floor (aranella's floor 11.6k, merttoprak's 4.6k, NeC's 0.8k): none can be hit by us, none but NeC could hit us, and members cannot attack members.
