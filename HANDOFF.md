# Handoff — 2026-09-23T10:00Z (session ended on the Commander's order)

## Do this first
Run `/empire-cycle`. Four planets are `STALLED / energy` (every solar satellite in the empire was destroyed): capital 0.71, :10 0.57, :9 0.57, :3 0.63. Solar-plant levels are already queued on :10 (11:49Z), :9 (12:01Z) and :3 (10:52Z) — when they land, queue the next plant level rather than satellites (`ops/defence/2026-09-22T17-45Z_albaycasey-and-furukhai-sweeps.md`: satellites are destroyed in every raid, plant levels never are).

## Where we are
Six planets, all held, no fleet and no cargo anywhere (11 large cargo, 141 probes, 66 satellites destroyed in two sweeps). Walls are at the free 70 % rebuild: capital 61 RL + 7 LL, :10 110 RL + 15 LL + 9 HL + 11 gauss + 2 ion + SSD, :9 34 RL + 8 HL, :3 33 RL + 7 LL, :14 54 RL, :1 29 RL. Research idle (shielding 9 landed; lab 9). Mines intact: :10 metal 22, :9 metal 22, capital metal 16→17. Dark matter 432. Stock on the ground: :10 388k M, :1 234k C, :14 207k D, :3 150k C — the crystal/deut piles cannot be spent where they sit and there is no cargo to move them (decision 013's routing assumes cargo exists).

## Next actions
1. 10:19Z / 10:40Z capital metal 17 + crystal storage 6 land → build 6–8 large cargo at the capital (shipyard 9, ~36–48k M/C) — nothing else in the empire can move resources; `empire/planets/G5-S316-P12.md`.
2. 10:52Z / 11:49Z / 12:01Z solar plants land on :3 / :10 / :9 → re-check factor, queue the next plant level on each (`empire-farm`).
3. Lift :1's 234k C and :14's 207k D to the capital the moment cargo exists; both are pure raid bait (`ops/defence/2026-09-22T17-45Z_*`).
4. Research slot is empty — cheapest useful next is ion 7 (64k M / 19k C / 6k D) once metal frees up (014 H2 lane).
5. Rebuild walls planet by planet to the **full** mixed shape (gauss + HL + LL, not RL), starting with the capital — a half-built wall cost us nothing at four planets while :10's full one cost him 13 ships (`ops/defence/2026-09-22T08-27Z_wall-sizing-sims.md`).
Later: astro/7th planet, nanite, raids — all parked until the posture question is answered.

## Questions for the Commander
- **Posture (open since 09-22 07:50Z)**: A turtle / B raid like Furukhai / **C deny + raid weak targets (my recommendation)**. Decisions 001/009/015 and the raid lane all hang on this.
- **015 wall-shape amendment**: the sims say mixed walls (gauss/HL/LL) draw or win against his cruiser slice; RL-only walls are what he farms. `strategy/decisions/015` needs your sign-off to change.
- **Trade**: merttoprak's standing 3:2 metal-for-crystal offer — decision 010 says no trades; worth a one-time exception now that crystal is stranded on :1?
- `strategy/LESSONS.md`: eight lessons drafted across 09-20 → 09-23 still unsigned.

## Uncommitted strategy changes awaiting approval
- `strategy/decisions/015` — wall shape (mixed, not RL-only); evidence in `ops/defence/2026-09-22T08-27Z_wall-sizing-sims.md`. Not edited, awaiting approval.
- `strategy/LESSONS.md` — 09-20 raid lessons + "cargo capacity is a defence", "an unattended empire cannot evacuate", "a half-built wall is worth nothing", "vault behind a long item".
- 013 clarification (crystal levels compete empire-wide by payback) still to fold into `strategy/decisions/013`.

## What changed this session (2026-09-21T11:30Z → 2026-09-23T10:00Z)
- Absorbed four BTC strikes. The one we were awake for (09-21 16:33Z capital) cost 31k thanks to vault + lift; the three we slept through cost ~2.4M (`ops/defence/2026-09-21T16-12Z_*`, `2026-09-22T17-45Z_*`).
- Answered "why can he hit us again and again" with the server simulator: cruisers have rapid-fire ×10 on rocket launchers, so our RL-only walls were the cheapest thing he could farm (`ops/defence/2026-09-22T08-27Z_wall-sizing-sims.md`).
- Grew through it: metal 22 on both metal worlds, lab 9, solar 18 + fusion 6 on the capital, research impulse 5 → hyperspace 5 → shielding 8 → energy 9 → combustion 8 → ion 6 → espionage 7 → shielding 9.
- Alliance told of each critical strike per the standing doctrine (msgs 1963, and the Commander's own 17:32Z post) — `ops/diplomacy/2026-09-21_*`.
- Probe-drill proven and its cost learned: refundable queues + lifts, cancel at +15 min if nothing comes (`ops/defence/2026-09-22T00-36Z_*`).
