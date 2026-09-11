---
name: handover
description: Rewrite HANDOFF.md so the next session resumes exactly here.
disable-model-invocation: true
---

Rewrite `HANDOFF.md` in full from the template (never append). Facts only: whatever the next session can read from a file or a tool is a pointer, not a copy. Commit `handoff: <one line>`.

```markdown
# Handoff — <ts>

## Goal right now
<the current objective in one or two lines, and which decision/doctrine rule it serves>

## In flight
| what | wake | file |
|---|---|---|
<fleets, research, builds worth knowing about, running soldiers — each with the file that tracks it>

## Next actions (in order)
1. …

## Questions for the Commander
- <non-urgent questions batched here; empty means none>

## Uncommitted strategy changes awaiting approval
- <file — what changed, or "none">

## Last cycle notes
<anything surprising this session, one line each, with a link>
```
