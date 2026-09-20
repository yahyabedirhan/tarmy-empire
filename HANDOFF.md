# Handoff — 2026-09-20T12:28Z (cycle 75 — BLOCKED: commander MCP token expired)

## Do this first
**Every commander call returns `http 401: invalid token` since 12:25Z** (`queue_research`, `research_levels`, `empire_overview`; `next_event` still returns empty lists). Not in `docs/mcp/COMMANDER.md` → Troubleshooting. The Commander must re-authenticate the commander MCP (tarmy login) — nothing in the loop can fix it. **The research slot is idle since 12:25:16Z (HD 4 landed): the first call after re-auth is `queue_research(tech="plasma")` 7 (256k C; capital holds ~345k C).** Then the normal cycle.

Run `/empire-cycle`. **albaycasey (BTC) raided :3 and :9 at 06:01/06:07Z** (`ops/defence/2026-09-20T05-35Z_albaycasey-attack-p3-p9.md`) — walls 70 % rebuilt, satellites rebought, deut now flows to the capital every cycle. On any attack `fleet.incoming`: fly the target's cargo + stocks to :10 or the capital, lock crystal in a probe batch (cancel after for the refund), alert the Commander. Next: **12:25:13Z HD 4 lands → `queue_research(tech="plasma")` 7 (256k C — ship from :1/:10)**; :10/:9 metal → capital for nanite 1 (1M M); 14:36:31Z :3 crystal 21 lands. 08:00Z leaderboard snapshot.

## Where we are
- Six planets GROWING, factor 1, no hostile fleets. Session resumed 17:08Z after a 9 h gap with every queue empty; all refilled this cycle. engin (BTC, rank 5) probed :10 + capital 07:03Z (caught) — no follow-up.
- Research: plasma 6, HD 1–3 landed overnight; **HD 4 → 12:25:13Z** (283473, battleship rung). Next: plasma 7 → weapons 10 → impulse 5–6. Robotics 10 landed 06:39Z → nanite 1 (1M / 500k / 100k) metal-gated.
- Crystal lane: :3 crystal 21 requeued (raid) → 14:36:31Z; :1 crystal 22 (928k M / 464k C) next by payback; capital crystal 20 (363k M / 181k C) after.
- Walls: capital 200 RL/10 LL/2 gauss/SSD/**LSD**; :10 149 RL/20 LL/10 HL/5 ion/8 gauss/SSD; :9 107 RL/15 LL/3 HL/4 ion/6 gauss/SSD (after the raid); :3 57 RL (+45 queued → 09:12Z); :14 65 RL; :1 50 RL. None holds a 228-ship fleet — keep the metal-worlds' deut/crystal low.
- Fleets: capital 1 LC; :10 3 LC (home ~18:08Z); :9 2 LC + 2 SC; :3 2 LC + 4 SC (home ~17:58Z); :14 3 LC (home ~18:18Z); :1 2 LC (home ~18:22Z). In the air: 90956 75k D :14 → capital 18:05Z; 90968 50k C :1 → capital 18:09Z.
- Alliance chat 08:36–17:53Z: 21 messages, all trade tables (crystal 1 = 5 metal; deut 1 = 3 metal) and one colony notice — none of the four watch items.

## Next actions
1. **19:55Z** leaderboard snapshot; 70k C :3 → capital.
2. **21:27Z** robotics 9 lands → queue robotics 10 if 205k M is at the capital (ship from :3 first; :10/:9 make 25k/22k M/h after their mines land).
3. **21:57Z** computer 10 lands → `queue_research(tech="plasma")` 6.
4. **21:59Z / 22:48Z** :10 / :9 crystal 20 land → 1 sat on :10; then 1 gauss/h each from own crystal (015).
5. **Status report** this cycle-68 (every 4th) — alliance skim already done above.
6. **Metal is the gate**: :3 crystal 21 (580k M) and :1 crystal 22 (928k M) wait for :10/:9 surplus; :14 deut tank 4 when it has 8k C.

## Questions for the Commander
- **Tell necati/BJACK that BTC's albaycasey attacked a pact member** (combat reports 58213, 58237)? Recommend yes. Asked 06:10Z.
- Approve `strategy/LESSONS.md` additions (2026-09-20 raid lessons) — uncommitted.
- Colony ship (built 19:14Z by the Commander): park until crystal ≥ 80k/h, or start astro 10 after plasma 6? (asked 19:20Z, recommendation: park)
- Tell necati/BJACK that three BTC accounts probed us today? (asked 23:05Z; nothing said meanwhile)
- none other open. Standing priority: planet 6 + crystal mining first, defence second (20:55Z 09-18).

## Uncommitted strategy changes awaiting approval
- none (013 clarification 03:50Z 09-19 still to fold into `strategy/decisions/013` on confirmation).

## What changed this session (2026-09-19T17:08Z →)
- Cycle 67: 5 sats + crystal 19 + robotics 9 + computer 10 (capital); crystal 20 + 4 sats (:10); 7 sats + crystal 20 (:9); robotics 8 + RL ×25 (:14); RL ×50 (:1). Cargo redeployed: 2 LC :3 → :14, 2 LC :3 → :1. Six transports fed the capital (crystal, deut, metal for the research lane).
