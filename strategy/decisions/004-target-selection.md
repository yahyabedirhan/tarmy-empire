# 004 — Targets: inactives freely, actives only with diplomacy and approval

- **status:** accepted
- **date:** 2026-09-11
- **decided by:** Commander

## Context
Protection: attacks refused at ≥ 5× effective score either way; 6 attacks/planet/24 h; loot ≤ half of each pool within cargo; defences leave no debris; 70 % of destroyed defences rebuild (`docs/game/mechanics.md` → Combat). L4: an unsimulated raid lost the fleet; an undefended empty target paid 50.

## Options
1. Inactives only, clean simulation, loot threshold.
2. Also actives when expected loot ≫ expected losses.
3. Anything allowed.

## Decision
Option 1 by default. Actives are a Commander decision, preceded by diplomacy (`strategy/ALLIANCE.md`): alliance players talk before hitting active players, and we do the same. Thresholds (tunable knobs in DOCTRINE → Raid): loot ≥ 30 000 and ≥ 15 000 per round-trip hour; zero expected ship losses; one fleet slot left free.

## Revisit when
- Ten campaigns are logged (recalibrate thresholds from real yields in `ops/attacks/`).
- We own cruisers (rapid fire changes what "clean" means).
