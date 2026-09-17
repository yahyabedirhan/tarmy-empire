# Sources

Verbatim copies fetched 2026-09-11 from https://docs.terminal.army/ (pages: `/`, `/mechanics/`, `/commands/`, `/commander/`). The site credits its formulas to the OGame Fandom Wiki (CC-BY-SA). Kept locally for private reference only and **gitignored** (the repo is public): a fresh clone runs `docs/game/fetch.sh` to regenerate them.

Live rules that beat the manual: `mcp__commander__combat_rules`, `mcp__commander__codex`, `mcp__commander__changelog`.

Known manual-vs-codex discrepancies (research round 2, 2026-09-17; the codex wins):
- Build time early-level speed-up: the manual says "(7 − L) / 2 through level 5"; `codex` times fit `max(4 − L/2, 1)` instead (missile silo 1: 365 s = 1 280 ÷ 3.5; lunar base 4: 7 680 s = 15 360 ÷ 2; missile silo 4: 5 120 s = 10 240 ÷ 2; robotics 9: factor 1). A level-1 facility takes 1/3.5 of the plain formula.
- `fetch.sh` needs `pandoc`; when it is missing, fetch the four pages with curl and strip the `<article>` HTML by hand (round 2 did this in the scratchpad).
