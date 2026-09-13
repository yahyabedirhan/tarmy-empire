# Handoff — 2026-09-13T16:18Z

## Do this first
Run `/empire-cycle`. **Astro 6 lands 17:49:44Z** → at the capital: (1) `build_ships colony_ship 1` (10k/20k/10k — price with `codex` first; capital had 32k M / 12k C / 9.7k D at 16:15Z, crystal reaches 20k ~17:45Z), (2) pick the planet-5 slot from `galaxy 5 316` per decision 008 (cold deut world 5:316:13/14 preferred, else crystal world 5:316:1/2) — `empire-colonize` skill; the colony ship flies only after **astro 7** lands (planet limit = 1 + ceil(astro ÷ 2): astro 6 still allows 4). Research slot after astro 6: leave idle or a zero-crystal filler (armour 9, 256k M) — crystal and deuterium are astro 7's (115k/230k/115k).

## Where we are
- 4 planets GROWING, no hostile fleets, nothing in the air, nothing in `ops/missions/`. Rank 207 / score 5030 at 16:16Z (`reports/status/2026-09-13T16-16Z.md`).
- Research: astrophysics 6 → 17:49:44Z. Goal: planet 5 (009). Astro 7 is deuterium-gated: empire ~22k D at 16:15Z, ~5.1k D/h → 115k D ~2026-09-14 10:00–12:00Z; crystal 230k needs ~7 h of empire crystal with nothing else queued → astro 7 ~2026-09-14 12:00–14:00Z → planet 5 ~2026-09-14 20:00Z.
- Queues: 5:316:10 metal 19 → 17:07:32Z; 5:316:9 satellites 13–17 → 16:22:37Z then metal 19 (88.7k/22.2k) when crystal ≥ 22.2k (~17:45Z); capital and 5:316:3 empty on purpose (their next builds are crystal-priced).
- Stocks 16:15Z: capital 32k M / 12k C / 9.7k D; 5:316:10 36k M / 1.9k C / 5.4k D; 5:316:9 121k M / ~11k C / ~3.4k D (after satellites); 5:316:3 53k M / 18k C / 1.2k D.
- Ships home: capital 62 LF, 2 recyclers, 10 probes; 5:316:3 1 LC + 4 SC; 5:316:9 2 LC + 2 SC; 5:316:10 2 LC.
- Chat times to the Commander are GMT+3; files stay UTC.

## Next actions
1. ~17:45Z 5:316:9: metal 19 when C ≥ 22.2k (energy covered by the 5 satellites).
2. 17:49:44Z astro 6 lands → colony ship at the capital + slot choice (see *Do this first*). Research: idle or armour 9.
3. Crystal sweep for astro 7 (230k C at the capital) once deuterium is within ~2 h of 115k: 5:316:3 and 5:316:9/10 crystal → capital (3 LC at 5:316:9/10, 1 LC + 4 SC at 5:316:3). Deuterium sweep at the same time (capital makes 2.1k/h, colonies 1.3–1.6k/h each).
4. Metal is slack everywhere (5:316:9 holds 121k): zero-crystal sinks only — metal storage where a cap is near, rocket launchers per decision 006 floor, armour 9 research. Do not spend crystal on mines before astro 7 is queued unless crystal ETA(astro 7) is not the gate.
5. 5:316:3 makes 46 D/h: every satellite there needs deuterium brought in (2k D per run from 5:316:10).
6. Every threshold: check BOTH metal and crystal (and deuterium) against the codex price; satellites are `upgrade_building`; the build queue holds 5.
Later: neighbourhood watch resume (2/21, decision 005) when probes are idle — exclude BTC-tagged planets; status report every 4th cycle (last 16:16Z).

## Questions for the Commander
- Approve adding to `strategy/ALLIANCE.md` → standing pacts: "BTC: non-aggression (BJACK-wide, 2026-09-13). Never attack a BTC-tagged planet." (`ops/diplomacy/2026-09-13_BJACK-chat-btc-pact.md`). Not urgent: raiding is parked.

## Uncommitted strategy changes awaiting approval
- none

## What changed this session
- Cycles 15–16 (12:58Z → 16:18Z): capital deut 12 (14:15Z); 5:316:9 deut 10 (13:13Z) + satellites 9–17; 5:316:10 satellites 14–18 + metal 19 running (17:07Z); 5:316:3 satellites 13–15 + metal 18 (15:26Z); 2k D run 5:316:10 → 5:316:3 (fleet 64351). Status reports 12:19Z (rank 220) and 16:16Z (rank 207). Alliance: BTC non-aggression pact recorded; tarla buys deuterium 3–4:1; no-trade stands.
- Cycle 14 (12:18Z → 12:58Z): status report 12:19Z (rank 220, 4753); sweep legs 64046/64069/64113 landed; armour 8 landed 12:54:15Z → astro 6 queued (17:49:44Z); satellites queued at the capital (3) and 5:316:9 (4) for deut 12 / deut 10; 2k D sent to 5:316:3 (fleet 64351) for its satellites. Alliance chat: tweisdorf membership request routed to officers; necati closed trading for good — nothing for us.
- Cycles 9–14 (04:08Z → 12:12Z): research laser 8, hyperspace 2, armour 8 (running); capital robotics 8; 5:316:9 crystal 16, satellites 3–8, deut 8–9 (deut 514 → 1023/h); 5:316:3 crystal 15–16, metal 16–17, satellites 6–12 (`empire/planets/`).
- Commander: no deuterium trade (07:52Z); decisions 008/009 confirmed, L15 approved (09:45Z) — `strategy/` committed; question backlog cleared.
- Astro clock engaged 08:05Z: mines parked, ~110k M swept to the capital for armour 8, then the astro-6 sweep 11:42–12:22Z (~107k C + ~56k D + ~30k M in 7 legs).
- Status report `reports/status/2026-09-13T07-44Z.md` (rank 248 → 220).
- Alliance chat: whole BJACK is crystal-short (necati bids 1 C = 4 M); ACS on 1:58:9 planned then cancelled; nothing addressed to us.
