---
name: empire-handover
description: Rewrite HANDOFF.md so the next session resumes exactly here.
disable-model-invocation: true
---

Rewrite `HANDOFF.md` in full from the template (never append). Facts only: whatever the next session can read from a file or a tool is a pointer, not a copy. Commit `handoff: <one line>` and push.

Shape the document with the rules in `.agents/skills/i-have-adhd/SKILL.md` → *Rules* (lead with the next action, numbered bounded steps, state restated, ≤ 5 items per group, no preamble). Those rules apply to **HANDOFF.md only**; do not adopt them as the session's reply style.

```markdown
# Handoff — <ts>

## Do this first
<one action the next session can take in under two minutes, e.g. "Run /empire-cycle; shielding 2 lands 10:13Z → queue shielding 3.">

## Where we are
<state in ≤ 5 lines: planets and their states, what is being built, what is in the air, score. Which decision/doctrine rule the current goal serves.>

## Next actions
1. <bounded step, with the wake it waits for and the file that tracks it>
2. …
(≤ 5; more go to the *Later* line)
Later: <one line>

## Questions for the Commander
- <none, or one line each; asked in chat, this is the backlog>

## Uncommitted strategy changes awaiting approval
- <file — what changed, or "none">

## What changed this session
<wins and surprises, ≤ 5 lines, each with a link>
```
