# 003 — Dark matter: hoard

- **status:** accepted
- **date:** 2026-09-11
- **decided by:** Commander

## Context
Earned 0.02/min only while a session is open, 12 h max per unbroken session (~14/day); no cap on balance (`docs/game/mechanics.md` → Dark matter; `dark_matter` tool). Prices: rush 1/min of remaining build time (min 5); boost 100 → +25 % mines on one planet for 24 h; rename 20. Balance ~100.

## Options
1. Hoard, spend only on the Commander's word.
2. Keep a reserve, boost above it (boost compounds with production).
3. Boost now.

## Decision
Option 1. The Commander cannot see DM in the game dashboard and wants it kept for moments that matter (an emergency rush while THREATENED, or a boost when production is large enough that 25 % is meaningful). The `status` skill reports the balance so the choice stays visible.

## Revisit when
- Balance ≥ 300, or capital production ≥ 30k metal/h (a boost would return ≥ 180k).
- The Commander asks for the trade-off again.
