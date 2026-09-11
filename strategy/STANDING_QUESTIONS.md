# Standing questions

Questions the Commander asks often enough that the Lieutenant keeps a live answer on hand, rather than re-deriving it from scratch each time. Revise this file at the end of every `empire-cycle` (as part of the *Record* step, before `HANDOFF.md`) and any time one of these answers changes mid-cycle. An answer that is more than one cycle stale should say so rather than mislead.

Each entry: the question, the current answer, the file(s) that are the source of truth (read those for anything more current than this file), and when it was last checked.

## What's the current plan, what are we focusing on right now?

Posture is **economy first, opportunistic raider, adequate defence** (`strategy/DOCTRINE.md`, decision 001). Right now: growing all 3 planets (queues refilled every cycle per `empire-farm`), capital researching toward the quest ladder, saving toward astrophysics 5 to unlock a 4th planet (decision 002). No active raid campaign or open mission as of the last check.

Source of truth: `HANDOFF.md` → *Where we are* / *Next actions* (rewritten every cycle — always more current than this line).
Last checked: 2026-09-11T12:10Z.

## When are we going to expand to a new planet?

Not yet. Blocked on astrophysics: we're at level 3 (allows exactly the 3 planets we hold); level 5 is needed to unlock a 4th and to open the position-3 slot (decision 002 picks **5:316:3**, +20% crystal). Astro 4→5 together cost ~59k metal / 118k crystal / 59k deuterium — the capital only holds ~22k crystal, the rest (~104k) sits on 5:316:10. Plan: transport crystal 10 → capital, then queue astro 4 then 5 back-to-back (~4.4h combined build), then send the idle colony ship at the capital to 5:316:3.

Source of truth: `strategy/decisions/002-expansion-six-planets.md`, `empire/research.md`, `research_tree` (live astro level), `empire/planets/G5-S316-P12.md` (capital resources).
Last checked: 2026-09-11T12:10Z — no crystal transport queued yet.

## When are we going to do our next attack?

Not launched yet, no open `ops/attacks/` campaign. Blocked on: (1) light_fighter 60 finishing at the capital (13:50:31Z) to have a strike force, (2) a fresh scan of the two named targets — 5:316:8 (Saeed2) and 5:316:5 (caioc) — since scans older than 6h don't satisfy the raid rule. Plan per decision 004: scan → simulate → only launch if every run wins and expected losses ≤ 5% of loot, loot ≥ 30k and ≥ 15k/hour of round trip. Target order: Saeed2 first, then caioc.

Source of truth: `strategy/DOCTRINE.md` → **Raid** rule (decision 004), `intel/targets/`, `ops/attacks/` (none open currently), `HANDOFF.md` → *Next actions*.
Last checked: 2026-09-11T12:10Z.

## Are we good on defence against a possible attack?

**No — one clear gap.** `defence_summary` as of this check:

| Planet | Turrets | Ships at home | Total weapon / shield / armour | Resources sitting there |
|---|---|---|---|---|
| capital (5:316:12) | light_laser 2, rocket_launcher 6 | 36 light_fighter, 2 large_cargo, 4 small_cargo, 1 colony_ship | 3584 / 934 / 322000 | ~221k (moderate; fleet at home covers it) |
| 5:316:10 | **none** | **none** | **0 / 0 / 0** | ~280k (metal+crystal+deut) |
| 5:316:9 | none | 2 small_cargo | 14 / 26 / 11200 | ~72k |

Decision 006's rule is defence value ≥ resources sitting there ÷ 4, plus a small shield dome per planet as soon as unlocked (`the_dome` quest is still open, progress 0/1 — no dome anywhere yet). The capital is carrying its own defence in its parked fleet. **5:316:10 is the outlier: zero defence of any kind against ~280k in resources**, and it's a same-system, easy-to-scan target. No hostile has been seen aimed at us this session (`fleets` empty), and the partial neighbourhood watch (10/31 scanned) found no active raider closer than "watch" verdicts — but that sweep isn't finished (systems 314–322 unscanned).

Recommendation: queue at least a handful of rocket launchers at 5:316:10 next time its queue frees, and keep the_dome quest in mind for all three planets once shipyard/robotics levels allow it.

Source of truth: `mcp__commander__defence_summary` (live, re-check every cycle), `strategy/DOCTRINE.md` → **Defend** rule (decision 006), `intel/` (threat picture — currently partial).
Last checked: 2026-09-11T12:10Z.
