# Handoff — 2026-09-21T15:17Z (cycle 79 — lab 9 up, research chained through :10)

## Do this first
Run `/empire-cycle`. All six planets at factor 1, every queue that can be filled is filled; metal is the empire-wide gate. Wakes: 15:20Z 45k C lands at the capital; 17:23Z shielding 8 lands → queue **energy 9** (204k C / 102k D) from the capital (lab 9); 17:30Z :9 metal 21 lands → 4 more satellites there; ~17:00Z lift :1's crystal again (6 LC parked there, 5 LC at :10, 2 LC on the run). Research trick in use: a research started from :10's lab 1 leaves the capital lab free to upgrade (014 construction note) — used for hyperspace 5 and shielding 8 today.

**Open question to the Commander (15:08Z)**: merttoprak's 3:2 metal-for-crystal offer (300k C → 450k M). Decision 010 said no trades; asked for a one-time exception because crystal idles at ~480k on the capital while weapons 10 / nanite wait on metal. Do nothing on it until answered.

**12:13Z Furukhai probed all six planets; no strike followed** (`ops/defence/2026-09-21T12-13Z_furukhai-probe-sweep.md`). Every stockpile was vaulted in refundable probe/RL batches for 42 min, then cancelled — 180 probes got built before the cancel (180k C; lesson: vault behind a long item or cancel the minute the window closes).

## Where we are
**Furukhai (BTC) struck :1 and :3 again at 09:37Z** (30 CR + 10 LC, W10/S8/A11) while no session was open: :1 lost 50 RL + the 3 LC parked there, 224.6k C looted; :3 lost 82 RL + 23 LL + all 27 satellites, 121k C / 112k M / 20k D looted, factor down to 0.54 — the "bleeding energy" the Commander reported. Record: `ops/defence/2026-09-21T09-37Z_furukhai-attack-p1-p3.md`. Alliance told 11:35Z (`ops/diplomacy/2026-09-21_furukhai-second-strike-report.md`, msg 1963).

**Fixed this cycle**: :3 back to 27 satellites (all 27 queued by 11:53Z, last lands 11:57Z) + solar_plant 17 behind them (12:33Z) + RL/LL to the 015 floor (13:02Z). First cargo since the sweep: 10 LC at the capital (12:29Z); :14's 3 LC moved to :1 with 40k M / 20k D, lifted 75k C to the capital, RL ×23 queued at :1. :10 metal 21 (13:46Z) + :9 metal 20 (13:13Z) with satellites behind, secondary defence topped to the 015 floor on both. Impulse 5 in the lab (13:39Z).

**Alliance chat (read 11:35Z)**: the BTC pact is over (merttoprak 06:40Z) — BTC hit necati, DenizYoldas, EfeBaslilar, tarla the same day. necati corrected the recon-to-strike rule: counter starts when a probe lands, launch within ~20 min, arrival by distance. engin [BTC, 5:298] probed four of our planets 10:44–10:57Z; his 388-ship fleet was bound for galaxy 3, nothing inbound on us as of 11:55Z.

The soldier spawned for the satellite loop (haiku) could not call the MCP and made zero game calls (`ops/missions/2026-09-21T11-33_satellite-rebuild-p3.md`, failed); the loop was run inline. Don't re-spawn for this — inline is cheaper.

## Next actions
1. 11:59Z: 3 LC land at the capital → deploy them back to :1 (13 min) for a second 75k C lift.
2. 12:29Z: 10 LC done → :1 → capital with everything; then :14 → capital with deuterium (133k D idle there) and metal from :9/:10 to :14 for deut synth 17 (148k M).
3. 13:13Z / 13:46Z: metal mines land on :9 / :10 → queue 1 / 3 more satellites each to cover the new draw.
4. 13:39Z: impulse 5 lands → weapons 10 (409k M / 102k C) needs metal at the capital; route :9/:10 metal there with the LC.
5. Every cycle: crystal off :1 and :3 to the capital. Capital nanite 1 (1M M) still the metal sink.
6. Status report due (cycle 80 by count, but the picture changed enough — write one next cycle).

## Questions for the Commander
- BTC pact is dead on the alliance side. Furukhai farms :1/:3 whenever crystal sits there (twice in 13 h). Options: (a) cargo shuttle every cycle + keep sessions open longer (current), (b) crystal storage stays low on purpose and mines pause — no, (c) ask the alliance for a joint response. Recommendation: (a), plus report each strike as we now do.
- Approve `strategy/LESSONS.md` — L17 committed; the four 09-20 raid lessons and today's ("cargo capacity is a defence", "an unattended empire cannot evacuate") still need your sign-off before they go in.
- necati/BJACK reply on the pact question: moot now that the pact is over; drop it.

## Uncommitted strategy changes awaiting approval
- `strategy/LESSONS.md` — four 09-20 raid lessons still pending; two new ones from `ops/defence/2026-09-21T09-37Z_*` not yet drafted there.
- 013 clarification (crystal levels compete empire-wide by payback) still to fold into `strategy/decisions/013`.

## What changed this session
- 11:30Z: found :3 at factor 0.54 after Furukhai's 09:37Z strike; 27 satellites re-queued in rounds of 5, done 11:57Z.
- 11:31Z: impulse 5 queued; 10 LC queued at the capital; :14's 3 LC deployed to :1 with 40k M / 20k D.
- 11:33Z: :10 metal 21 + 4 sats + LL 7 / gauss 1 / HL 1; :9 metal 20 + 4 sats + LL 5 / gauss 2; capital LL 1.
- 11:35Z: alliance report 1963 sent (standing doctrine).
- 11:46Z: 75k C :1 → capital (102623, 11:59Z); RL ×23 at :1.
- 11:53Z: :3 solar_plant 17, RL ×27, LL ×9.
