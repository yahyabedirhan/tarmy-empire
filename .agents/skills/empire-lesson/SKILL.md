---
name: empire-lesson
description: Record a lesson learned from an event and propose the doctrine change it implies. Use after any raid, colonisation, soldier mission or attack that surprised us.
---

1. Find the event file (`ops/`, `intel/`, `reports/`) and add a `lessons:` line to it.
2. Append to `strategy/LESSONS.md`: next number, one-line title with date, 2–4 lines: what we assumed, what happened, the rule that follows, the source link.
3. If a rule in `strategy/DOCTRINE.md`, `empire/research.md` or a decision's *Revisit when* should change, edit it and reference the lesson number.
4. Commit the event file (`ops:`/`intel:`); leave `strategy/` uncommitted, list the change in `HANDOFF.md` → *Questions for the Commander* as "approve strategy change: L<n>".

Done when the lesson has a number, a source link, and either a doctrine edit or the sentence "no rule change".
