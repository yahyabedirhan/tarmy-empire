# Handoff — 2026-09-21T17:29Z (cycle 81 — capital cleared THREATENED, crystal lift running)

## Do this first
Run `/empire-cycle`. Sleeping until **17:34:51Z** (:9's last satellite lands). All six planets at factor 1, no threats, no running missions. Two fleets in the air:
- 104046: 8 LC :10 → capital, 110k D + 60k M, lands **17:40:07Z**.
- 104057: 5 LC :14 → :3, lands **17:42:45Z**, then load :3's 61.8k C and lift to the capital.

**Once both land**, capital will have ~264k M / ~226k C / ~118k D → queue **energy 9** (0 M / 204,800 C / 102,400 D). Then spend the metal on RL 159→200 (82k M) and solar 18.

## Where we are
This session opened after a `/clear` mid-empire; the last written HANDOFF (15:17Z) was two cycles stale — a Furukhai attack on the capital (16:33Z, 70 CR + 15 LC) had already happened and been closed by the previous session (`ops/defence/2026-09-21T16-12Z_furukhai-attack-capital.md`), but no handoff was written after it. Caught up by reading git log + the ops file + a fresh `empire_overview` before acting.

**16:33Z capital strike (closed)**: loot held to 910 M / 769 C / 29k D (vs 09-20's ~178k) — probe→lift+vault worked again. Cost: 48 satellites, 56 RL, 5 LL, 1 gauss to the floor, all rebuilt/requeued same session. Reported to BJACK this cycle (msg 1982, 17:32:46Z, `ops/diplomacy/2026-09-21_furukhai-capital-strike-report.md`).

This cycle: confirmed recovery complete (48/48 sats, factor 1, shielding 8 landed) → capital THREATENED/recovering → GROWING/waiting. Found 8 LC already outbound :10→capital (not this session's action — either the prior session queued it before dying, or the Commander). Deployed :14's 5 idle LC to :3 to lift its crystal, since the capital was short ~40.6k C for energy 9. :9's metal_mine 21 + 4 satellites queued last cycle are landing on schedule (17:30–17:35Z).

## Next actions
1. 17:34:51Z: :9 sats land → queue 4 more sats there (headroom still short per the plan file `wake`).
2. 17:40:07Z: fleet 104046 lands at capital (110k D + 60k M).
3. 17:42:45Z: fleet 104057 lands at :3 → load ≥45k C → dispatch to capital.
4. Once capital crystal ≥ 204.8k: queue energy 9, then RL 159→200 and solar 18 with the metal.
5. Status report due — picture has changed twice since the last one (`empire-status` skill).

## Questions for the Commander
- merttoprak's 3:2 metal-for-crystal trade exception (asked 15:08Z, still open) — doing nothing on it until answered.
- `strategy/LESSONS.md` sign-off needed: L17 + four 09-20 raid lessons + two 09-21 09:37Z lessons (all drafted, awaiting approval) — plus a third set from the 16:33Z attack (loot-denial works, satellites are the recurring loss, treat every capital probe as a launch) still to draft.

## Uncommitted strategy changes awaiting approval
- `strategy/LESSONS.md` — as above, nothing has been merged in yet.
- 013 clarification (crystal levels compete empire-wide by payback) still to fold into `strategy/decisions/013`.

## What changed this session
- 17:29Z: read HANDOFF (stale) + git log + ops file, caught up on the 16:33Z attack already closed by the prior session.
- 17:29Z: capital THREATENED/recovering → GROWING/waiting (recovery confirmed complete).
- 17:29Z: deployed :14's 5 LC to :3 (104057) to lift crystal for energy 9's gap.
- 17:29Z: found and left in place fleet 104046 (:10 → capital, 110k D + 60k M) — not queued by this session.
- Committed `empire/planets/*.md` updates (5 files); pushed.
