# Handoff — 2026-09-11T08:50Z

## Goal right now
First cycle under the new structure: spend the idle stockpiles (done: both queues 5/5), found planet 3 at 5:316:9 (soldier waiting on astrophysics 3, 08:59Z), build the first raid fleet (60 LF, soldier waiting on queue slots), then fly the Saeed2 campaign once the Commander answers the questions below.

## In flight
| what | wake | file |
|---|---|---|
| astrophysics 3 | 08:59Z | empire/research.md → next: computer 4 |
| colonize 5:316:9 (haiku soldier) | research done → dispatch → arrival | ops/missions/2026-09-11T08-30_colonize-5-316-9.md, ops/colonies/G5-S316-P9.md |
| ship batches LF 60 / LC 3 / REC 2 (haiku soldier) | capital queue slots at 08:46Z, 08:49Z, 09:26Z | ops/missions/2026-09-11T08-30_capital-ships.md |
| capital queue: solar 15, solar 16, metal mine 14 | 09:26Z, 10:21Z, 10:38Z | empire/planets/G5-S316-P12.md |
| colony queue: solar 13, MM11, solar 14, MM12, CM11 | 08:44Z … 09:47Z | empire/planets/G5-S316-P10.md |

## Next actions (in order)
1. When astrophysics 3 lands: `queue_research(tech="computer")`.
2. Close both missions with the soldiers' reports; create `empire/planets/G5-S316-P9.md` (BOOTSTRAP) if founded; commit.
3. Bootstrap transports to 5:316:9 each cycle (`empire-colonize` skill).
4. On the 60 LF finishing: re-scan 5:316:8 and 5:316:5, then the Saeed2 campaign if approved.
5. `/empire-cycle` every 30 min.

## Questions for the Commander
- **Raid threshold wording.** DOCTRINE says "zero expected ship losses". Against the standard 10 RL + 5 LL wall, 60 LF lose on average half a fighter (2k) per sortie for ~114k loot. Proposed wording: "expected losses ≤ 5 % of expected loot". Approve, and approve the Saeed2 campaign (`ops/attacks/2026-09-11_G5-S316-P8_Saeed2.md`)?
- **Second actor.** At 07:56–08:01Z something queued research lab 7, 2 light lasers and astrophysics 3 on the capital, and mines on the colony — before this session acted. Was that you in the TUI, or is another Claude session still running a loop? Two actors on one account will collide (shared event stream, shared queues).
- **Push policy.** You asked for a public repo and a push; `AGENTS.md` still says "never push". Change it to "push after every commit"?
- **Public repo exposure.** `intel/`, `ops/` and `strategy/` are now readable by anyone, including other players' assistants; the manual copies are kept local. Fine as is, or make it private?

## Uncommitted strategy changes awaiting approval
- none (the skill rename was committed on your instruction)

## Last cycle notes
- `next_event` is one stream per account; a second consumer eats events. Soldiers now sleep on it and re-read state (`empire-soldier` skill, `docs/mcp/COMMANDER.md`).
- Buildings, ships and defence share one 5-slot queue per planet (`build_ships` 409).
- BJACK chat is a working channel of assistants; temperature-by-slot data captured in `intel/notes.md`.
