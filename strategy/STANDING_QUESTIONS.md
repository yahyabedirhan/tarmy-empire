# Standing questions

Questions the Commander asks often enough that the Lieutenant keeps a live answer on hand, rather than re-deriving it from scratch each time. Revise this file at the end of every `empire-cycle` (as part of the *Record* step, before `HANDOFF.md`) and any time one of these answers changes mid-cycle. An answer that is more than one cycle stale should say so rather than mislead.

Each entry: the question, the current answer, the file(s) that are the source of truth (read those for anything more current than this file), and when it was last checked.

## What's the current plan, what are we focusing on right now?

Posture unchanged: **economy first, raiding parked** (decision 001, L9). Engine (decision 009): planets before fleet — every queue filled with the best-returning mine in the empire (colonies' low mines first, decision 008), crystal before metal, and the astrophysics ladder as the clock: astro 5 → planet 4 at 5:316:3 (crystal world), then astro 6+7 → planet 5 (deuterium is the gate), then 8+9 → planet 6. Proposed and waiting on the Commander: 1:1 trades of surplus metal for crystal/deuterium inside BJACK (decision 010).

Source of truth: `HANDOFF.md` → *Where we are* / *Next actions*; `strategy/decisions/009-*.md` forecast table.
Last checked: 2026-09-11T18:20Z.

## When are we going to expand to a new planet?

Astro 5 needs 37.5k / 75k / 37.5k on the capital. Empire crystal ~26k on hand, +13.2k/h → the sum exists in ~5–6 h if nothing else is bought, ~8–10 h while short-payback mines are still built (they pay back before the research lands). A 50k metal→crystal trade with aranella (decision 010) would bring it to ~2 h. Research takes 2.8 h; the colony ship is already parked at the capital; 5:316:3 is confirmed empty (18:00Z). Planet 5 (astro 6+7) is gated by 180k deuterium ≈ 64 h at today's 2.8k/h — synthesizers on 5:316:9 queued, a deuterium trade proposed.

Source of truth: `research_tree`, `strategy/decisions/009-*.md`, `empire/research.md`.
Last checked: 2026-09-11T18:20Z.

## When are we going to do our next attack?

Not before planet 5 (decision 009) unless the Commander reopens it. Reason, measured by the alliance and by us: at our size 900k in cruisers returns one-off loot; the same 900k in a colony returns +24k/h forever. Our 5× floor is 428 invested and rises with every build; everything soft in 5:310–322 is already below it (L8), and everything above it carries the standard 216-unit wall (L9). When reopened, the target class is the "sleeping builder" (mines 18+, wall < 20 turrets, no fleet, score ≥ ours ÷ 5), found by leaderboard score, valued by production not vault, hit before we outgrow it.

Source of truth: DOCTRINE → Raid, `strategy/decisions/009-*.md` revisit triggers.
Last checked: 2026-09-11T18:20Z.

## Are we good on defence against a possible attack?

Adequate for today's stockpiles, thin for the astro-5 hoard. Who can hit us: players with score 428–10.7k (5× band); BJACK members cannot; the big accounts cannot. Walls: capital 16 RL + 2 LL + 62 LF parked (~40k value) over ~110k resources; 5:316:10 20 RL over ~53k; 5:316:9 nothing over ~25k (rocket launchers are pure metal — added when its metal has no better mine to buy). Rule for the hoard (decision 006 amended): as astro crystal piles on the capital, add RL so wall value ≥ hoard ÷ 4 — 75k crystal + 37k metal + 37k deut ≈ 150k → ≥ 37k wall, which the capital already has; for astro 7's 460k the wall must reach ~115k (≈ 45 more RL, 90k metal, zero crystal). No hostile fleet seen this session.

Source of truth: `fleets` (every cycle), `defence_summary`, DOCTRINE → Defend.
Last checked: 2026-09-11T18:20Z.

## How long can we farm safely without attacking?

Indefinitely, as far as the rules go: nobody needs to be attacked to grow, and raiding is a bonus not an engine (the #1 player has attacked nobody for days — everyone is below her floor). The risk is the other direction: being farmed. That is controlled by (1) stockpiles low — spend on landing, sweep to the capital only when the research is about to be queued, (2) wall ≥ stock ÷ 4, (3) `fleets` read every cycle and `fleet.incoming` waking the loop at once. If we are raided for more than an hour of production in a week, decision 009 says reopen the fleet-save routine.

Source of truth: DOCTRINE → Defend, decision 009.
Last checked: 2026-09-11T18:20Z.
