---
name: farm
description: Decide and queue the next builds and research for one planet in GROWING state, following the doctrine order (energy, storage, mines by role, facilities, ladder). Use from the cycle skill or when asked to grow a planet.
---

The build decision procedure for one planet. Input: the planet file in `empire/planets/`, its `production_report`, `build_queue`, and `codex` answers. Output: a queue with 2–5 items and an updated planet frontmatter.

1. **Energy gate.** If production factor < 1, or `codex` of the intended mine shows energy draw that would push it below 1: queue `solar_plant` (or `fusion_reactor` if `codex` shows more energy per resource at this level; on warm planets compare `solar_satellite`). Stop here if that used the budget.
2. **Storage gate.** Any pool ≥ 80 % of cap → queue that storage level, or move the surplus by transport to a planet that can spend it (a bootstrap first).
3. **Mines by role.** Favour the role's resource (`metal-world` → metal mine, …); keep the other two mines within 2 levels of the leader; capital favours whichever pool is lowest relative to what `empire/research.md` needs next. Cheapest useful level first when several are affordable.
4. **Facilities from the ladder.** Between mine levels, one facility per cycle if affordable: robotics (build speed), shipyard (capital only, ladder gates), research lab (capital only, only when no research is running), missile silo / nanite later.
5. **Research (capital only).** If nothing is in progress and the lab is not upgrading: next row of `empire/research.md` whose full chain is affordable (L5). `queue_research(tech=…)`.
6. **Ships and defence (capital).** Ladder rungs one step away and decision 006's floor: `build_ships`.
7. **Fillers.** Queue below 2 items and crystal short → a metal-only build (metal storage, robotics) rather than an empty queue.
8. **Write.** Planet frontmatter: `substate: building` with `wake: queue.completed`, or `substate: waiting` with `wake: <resource> ≥ <n> (ETA <time>)` computed from the production rate.

Done when the queue holds 2–5 items or the wake says exactly what is being waited for and until when.
