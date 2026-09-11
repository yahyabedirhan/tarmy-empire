---
name: empire-status
description: Write a status snapshot of the empire to reports/status/ and summarise it for the Commander.
disable-model-invocation: true
---

Write `reports/status/<YYYY-MM-DDTHH-MM>Z.md` from live data, then print its *Summary* section. Never edit an old report.

1. Read `empire_overview`, `standing`, `dark_matter`, `fleets`, `research_tree` (for `in_progress`), and `production_report` + `build_queue` for each planet beyond the first. Read every `empire/planets/*.md` frontmatter and every `ops/missions/*.md` with `status: running`.
2. Fill the template below. Every cell filled; `unknown` where the tool did not say.
3. Compare with the previous report in `reports/status/`: note score delta, production delta, planets gained/lost. List any decision record whose *Revisit when* trigger has fired.
4. Commit: `report: status <timestamp>`.

```markdown
# Status <timestamp>

## Summary
<5 lines max: rank/score (Δ since last), planets, what is being built, what is in the air, the one thing the Commander should decide>

## Empire
| planet | role | state/sub | wake | M / C / D | prod M/C/D per h | factor | queue (n) |
|---|---|---|---|---|---|---|---|

## Research
in progress: <tech level, finishes at> · next per `empire/research.md`: <tech>

## Fleets and missions
| what | from → to | mission | arrives / returns | soldier |
|---|---|---|---|---|

## Threats and opportunities
<hostile fleets; intel targets with verdict farm and fresh scans; ladder rungs one step away>

## Dark matter
balance <n>, rate <n>/h (decision 003: hoard)

## Questions for the Commander
<from HANDOFF.md, or "none">

## Decisions to revisit
<decision id — trigger that fired, or "none">
```
