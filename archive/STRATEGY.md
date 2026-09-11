# terminal.army Empire Strategy: yabepa

**Universe:** Genesis (5x economy, 4x fleet, 5x research)
**Current Status:** Rung 5/85 | 1 planet | Solo player
**Last Updated:** 2026-09-06 12:59 UTC

---

## Phase 1: Foundation & Growth (Week 1–2)

### Current Status
- **Energy Crisis:** RESOLVED ✅
  - Solar Plant 4 complete (energy 144/129)
  - SP5 & SP6 queued to reach energy 212 (massive surplus)
- **Storage:** Metal Storage 2 queued (protection against loss)
- **Production:** 749 metal/hr, 474 crystal/hr, 163 deuterium/hr @ 100% efficiency

### Immediate Build Queue (Next 3 minutes)
```
1. Solar Plant 5 (50 sec) → Finishes ~12:59:28
   Cost: 379 metal, 151 crystal
   Gain: +82 energy (144 → 161)
   Quest: "Run the plant at full burn" (progress 4/6)

2. Metal Storage 2 (96 sec) → Starts 12:59:28, finishes ~13:01:04
   Cost: 2,000 metal
   Gain: +100k metal capacity (100k → 200k)
   Quest: "Somewhere to keep it" (progress 1/2)
```

### ⚠️ ENERGY-FIRST CHECKPOINT (CRITICAL)

**Before queuing ANY consumption building (mines, synthesizers), verify:**
```
✓ Energy produced ≥ energy used + 50 MW buffer (production factor ≥ 1.15)
✗ DO NOT queue if production factor < 1.0 (efficiency < 100%)
✗ DO NOT queue if production factor < 1.05 (efficiency < 105%)
   Even if "acceptable", it's a trap that starves all resource production

If production factor drops below 1.0:
  → PAUSE all consumption buildings
  → Queue solar plants ONLY until energy surplus restored
  → This prevents the negative feedback loop
```

**Lesson Learned (2026-09-06):** Queued MM6→MM7, CM3→CM4 before securing full energy surplus. Energy dropped from 96.76% → 83.5%. Resource production starved. Required 2–3 hour wait for SP8 to recover. **Never again.**

### Phase 1a: Production Acceleration (Hours 2–4 of gameplay)

**After MS2 completes, queue in this order (ENERGY-FIRST ALWAYS):**

1. **Metal Mine 4–8** (5 upgrades, ~100 sec each) — ONLY after energy checkpoint passed
   ```
   Targets: Reach Metal Mine 8 (quest: "Drive the shaft deeper")
   Cost per level: ~202–300 metal, 50+ crystal
   Gain: Metal production 749 → ~2,000/hr by level 8
   Build time: Total ~9 minutes with Robotics Factory 1
   ```

2. **Robotics Factory 2** (priority: speeds up EVERYTHING after this)
   ```
   Cost: 800 metal, 240 crystal, 400 deuterium
   Build time: 49 sec (but critical unlock)
   Effect: All future builds take ~50% less time
   Quest: "Hire hands that build" (progress 1/2)
   ```

3. **Crystal Mine 4–8** (parallel with metal mines)
   ```
   Targets: Reach Crystal Mine 8 (quest: "Dig the crystal deeper")
   Cost: Similar scaling to metal mines
   Gain: Crystal production 474 → ~1,200/hr
   ```

4. **Research: Energy 1** (immediately after Robotics 2)
   ```
   Cost: 800 metal, 200 deuterium (check codex)
   Build time: ~3 minutes in lab
   Unlock: Tech tree (many prerequisites)
   Quest: "Prove the first theory" (active)
   ```

### Phase 1b: Storage & Infrastructure (Hours 4–6)

**Goal: Prevent resource loss, scale safely**

- Metal Storage 3–4 (doubles capacity each level)
- Crystal Storage 2–3
- Deuterium Tank 2–3
- This protects against overnight drain + raids

### Milestone: Reach Rung 15
**Current:** Rung 5/85  
**Quest ladder to 15:**
- "Full burn" (Solar Plant 6) → Rung 6
- "Room to keep it" (Metal Storage 2) → Rung 8
- "Deeper shaft" (Metal Mine 8) → Rung 9
- "Hands that build" (Robotics Factory 2) → Rung 10
- "First theory" (Energy Tech 1) → Rung 11
- Continue mining quest (Metal Mine 8) → Rung 12
- Crystal Mine 8 → Rung 13
- More quests auto-complete

**Reward when Rung 15:** ~15k metal, 10k crystal, 5k deuterium (reinvest into next phase)

---

## Phase 2: Fleet Foundation (Week 2–3)

### Gate: Unlocking Shipyard
**Prerequisite chain:**
1. Research: Combustion Drive 1
2. Build: Shipyard 1
3. Upgrade: Shipyard 2 (quest: "Open the slipway")

**Timeline:** ~24–36 hours of gameplay (5x speed economy)

### Shipyard 2 Unlocks
- Small Cargo Ships (carry 5k resources each)
- Large Cargo Ships (carry 25k resources each)

### Build First Fleet: 2 Small Cargo Ships
```
Cost per ship: ~500 metal, 500 crystal, 100 deuterium
Total: 1,000 metal, 1,000 crystal, 200 deuterium
Build time: ~2 min each with Robotics 2
Purpose: Trade runs between planets / farm raids
```

### Research: Combustion Drive 2
```
Prerequisite: Energy 1 (already researched)
Cost: ~1,000 metal, 400 deuterium
Build time: ~6 minutes
Unlock: "Light the first engine" quest
Effect: Ships now move (Combustion Drive 2 required)
```

---

## Phase 3: First Farming Raids (Week 3+)

### Prerequisites Met ✅
- ✅ Energy at 100% (SP6 complete)
- ✅ Storage protected (MS2–4 complete)
- ✅ Robotics Factory 2 (build times halved)
- ✅ Shipyard 2 + Combustion Drive 2 (fleet built)
- ✅ 2–3 Small Cargo Ships (haulers ready)

### Scout & Raid Strategy

**Step 1: Scout Inactive Targets**
```
Requirements:
- Espionage Tech 1 (unlocked by Research Lab 3)
- Can see: defenses, fleet, resources on planet

Target Profile:
- Last login 7+ days ago (likely asleep)
- No fleet on planet
- Minimal defenses (0–2 rocket launchers)
- 10k+ metal/crystal in storage
```

**Step 2: Calculate Risk**
```
Assume worst case: planet has 2 rocket launchers
My fleet: 2 small cargos (weak armor, for transport not combat)
Verdict: DO NOT ATTACK with cargos alone

Better plan: Wait for cruisers (Phase 4) or use cargo as bait only
```

**Step 3: Execute Raid (Phase 4+)**
```
When: 3+ Cruisers built + Weapons Tech 2+ researched
Fleet composition: 3 cruisers = enough to break undefended colony
Target: Inactive planet with 0 defenses
Debris field: 30%+ of destroyed resources become debris
Collection: Send recyclers after battle (Phase 4)

Expected gain: 20k–50k metal + 10k–30k crystal per raid
Payoff: 2x faster growth than pure mining
```

---

## Phase 3b: Colonization (Week 3–4)

### Gate: Astrophysics Research (Critical Unlock)
**Prerequisite chain:**
1. Research Lab 3 (unlocks Espionage 1)
2. Espionage Tech 4 (requirement for Astrophysics)
3. Impulse Drive 3 (powers colony ships)

**Then research Astrophysics 1:**
```
Cost: 4,000 metal, 8,000 crystal, 4,000 deuterium
Lab time: ~72 minutes (at 5x speed)
Unlock: Positions 4 and 12 in your system become colonizable
Effect: Allows up to 2 planets total
```

### Build Colony Ships (After Astrophysics 1)
**Requirements:** Shipyard 4, Impulse Drive 3

```
Cost per ship: 10,000 metal, 20,000 crystal, 10,000 deuterium
Build time: ~144 minutes per ship (at 5x speed)
Cargo: 7,500 resources per ship
Fuel: 1,000 deuterium per unit distance
Speed: 2,500 units (travel ~30 min to adjacent planet)
```

### Colonization Process
```
Step 1: Build 1 Colony Ship (first colonization)
Step 2: Travel to empty position (4 or 12) in your system
Step 3: Land on planet → Automatic colonization
Step 4: New planet spawns with empty infrastructure

Travel time: ~30–45 minutes one way
Arrival delay: ~30 minutes on planet surface
Total: ~75–90 minutes from launch to settlement
```

### Second Planet Strategy
```
First planet (home): Continue raid support + tech research
Second planet (colony): Dedicate to metal/crystal/deuterium production only
Benefit: 2x total production = ~2x faster everything

Setup priority:
1. Metal Mine 1–8 (copy home setup)
2. Crystal Mine 1–8 (copy home setup)
3. Deuterium Synthesizer 1–8 (copy home setup)
4. Solar Plants 1–6 (energy support)
5. Storage (protect resources)
6. Skip research lab & robotics (centralize on home)
```

### When to Colonize
```
Timeline: ~70–100 hours of gameplay (Phase 3 late)
Triggers:
- ✅ Astrophysics research complete
- ✅ Shipyard 4 unlocked (from Phase 4 military tree)
- ✅ 200k+ metal available (colony ship cost)
- ✅ 20k+ crystal available (colony ship cost)
- ✅ 10k+ deuterium available (colony ship cost)
- ✅ Home planet defended (2+ rocket launchers)

Warning: Colonization requires massive resource commitment.
Plan 48–72 hours ahead before locking resources into colony ship.
```

### Why NOT to Colonize Early
```
- Astrophysics is EXPENSIVE (16k resources for one level)
- Colony ships are VERY expensive (40k resources each)
- Travel time removes fleet from home defense (72–90 min vulnerable)
- Second planet needs its own full infrastructure
- Distracts from raid economy in Phase 3

Instead: Max out Phase 3 raids first, THEN colonize when Phase 4 military is secure.
```

---

## Phase 4: Military Expansion (Week 4+)

### Gate: Cruiser Technology
**Prerequisite chain:**
1. Shipyard 4
2. Impulse Drive 4
3. Ion Tech 4

### Build 3 Cruisers
```
Each costs: ~3,000 metal, 2,000 crystal, 1,000 deuterium
Total: ~9,000 metal, 6,000 crystal, 3,000 deuterium
Build time: ~5–10 min each with Robotics 10

Capability: Kill undefended planets (colony raids)
Profit: Debris fields worth 2–3x the build cost
```

### Build Recyclers (2 ships)
```
Cost: ~2,000 metal, 1,000 crystal, 500 deuterium
Purpose: Collect debris after battles
Critical: Every battle leaves debris; without recyclers, enemy collects it
```

### Defense Layer 1: Rocket Launchers
```
Goal: 2 rocket launchers per planet (deterrent)
Cost: ~500 metal, 300 crystal each
Effect: Stops casual raiders (costs more to attack than they gain)
```

---

## Leaderboard Strategy

### Points Sources
1. **Production** (30%): Mines, refineries, storage levels
2. **Tech** (30%): Research levels, lab levels
3. **Ships** (20%): Fleet size, shipyard levels
4. **Raids** (20%): Successful attacks, debris collected

### Climb to Top 100
- **Weeks 1–2:** Steady quest completion (production + tech focus)
- **Week 3:** First raids (3–5 per week against inactive players)
- **Week 4+:** Regular farming + tech acceleration

**Assumption:** At 5x speed, equivalent to 3–4 weeks real time to competitive position (top 500).

---

## Resource Targets by Phase

| Phase | Metal Goal | Crystal Goal | Deuterium Goal | Time |
|-------|-----------|-------------|----------------|------|
| Phase 1a | 50k | 20k | 10k | 0–4 hrs |
| Phase 1b | 100k | 50k | 20k | 4–6 hrs |
| Phase 2 | 200k | 100k | 50k | 6–24 hrs |
| Phase 3 | 300k | 200k | 100k | 24–36 hrs |
| Phase 3b | 500k+ | 250k+ | 150k+ | 70–100 hrs |
| Phase 4 | 800k+ | 400k+ | 300k+ | 100+ hrs |

---

## Critical Rules (No Exceptions)

### Do NOT Attack Until:
- [ ] Energy at 100% (no production bottleneck)
- [ ] Storage 2+ (no overnight loss)
- [ ] Robotics Factory 2 (build times halved)
- [ ] Shipyard 2 + Combustion Drive 2 (fleet functional)
- [ ] 2+ combat ships (cruisers, not cargos)
- [ ] Espionage Tech 1+ (can scout targets safely)
- [ ] Target confirmed inactive 7+ days (low risk)

### Always Scout Before Attack
```
Attacking blind = fleet wipe = 10+ hour setback
Scouting costs 0 resources, takes 30 seconds
Always worth it
```

### Diversify Targets
```
Never attack same player twice in 24 hours
Never attack player in alliance (likely coordinated defense)
Spread raids across 3–5 targets minimum
```

### Protect Your Planets
```
Minimum defense: 2 rocket launchers per planet
Target: Small Shield Dome when resources allow (Phase 4)

With 2+ planets:
- Home planet: 4–6 rocket launchers (primary defense)
- Colony planets: 2 rocket launchers minimum (deterrent)
- Alliance coverage: Join early (quest reward) for shared intel + coordinated defense
- Park fleet at home: If colony is attacked, home can send reinforcements (30–40 min travel)

CRITICAL: Never colonize without alliance backup. Undefended colony = free resources.
```

---

## Immediate Next Steps (Next Agent)

1. **Monitor build queue:** SP5 & MS2 should finish within 3 minutes
2. **After MS2 completes:** Queue Metal Mine 4 (start mine upgrades)
3. **Check resources every 30 min:** Crystal is constraint, accumulates slowly
4. **After Metal Mine 8 + Robotics 2:** Start Energy 1 research
5. **Target:** Reach Rung 15 within 6 hours of gameplay

**Checkpoint:** When Rung 15 reached, review this strategy and decide:
- Continue production grind (safer, slower)
- Pivot to Shipyard unlock (faster, need more resources)

---

## Notes for Next Agent

- **This player is risk-averse:** Focus on farming/growth before any combat
- **Universe speed is 5x:** What feels like 1 week = 5 days of gameplay
- **Alliance matters:** Early join provides intel, defense coordination, shared targets
- **Quests are the guide:** Follow quest ladder religiously; rewards fund next stage
- **Crystal is bottleneck:** Watch crystal production; it gates most mid-game builds
- **Colonization is endgame:** Phase 3b is expensive but necessary for long-term growth (2x production)
- **Defend colonies:** Always have 2+ rockets per planet; undefended = vulnerable to raids
- **Two-planet strategy:** Home = combat/tech hub; Colony = production-only (mines 1–8)
