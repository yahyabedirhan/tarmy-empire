# Colony Growth Strategy

**Date Started:** 2026-09-09  
**Status:** Active - Autonomous Farming  
**Cycle Check Interval:** 2 minutes

## Colonies Under Management

1. **Colony 5:316:10** (existing, established)
   - Status: Producing, stable production
   - Role: Resource source, supports bootstrap operations
   
2. **Colony 5:316:2** (new, colony ship ETA 13:49:48 UTC)
   - Bootstrap cargo arriving: 13:42:53 UTC (3K metal, 1K crystal, 500 deut)
   - Status: Creation imminent
   
3. **Colony 5:317:12** (new, colony ship ETA 14:04:44 UTC)
   - Bootstrap cargo arriving: 13:53:31 UTC (3K metal, 1K crystal, 500 deut)
   - Status: Creation imminent

## Core Strategy

### Phase 1: Bootstrap (Immediate - First Hour)
- Cargo arrives before colony ships land
- Resources staged for immediate construction
- Prioritize: Solar plant → Metal storage → Mines

### Phase 2: Energy Independence (Hours 1-4)
**Energy First Rule:** All new colonies must reach 100% energy efficiency before expanding mining.

Build sequence per colony:
1. **Solar Plant Level 1** (75 metal, 30 crystal) - Power foundation
2. **Metal Storage Level 1** (1,000 metal) - Prevent production halt
3. **Metal Mine Level 1** (60 metal, 15 crystal)
4. **Solar Plant Level 2** (if energy deficit)
5. **Crystal Mine Level 1** (50 metal, 15 crystal)
6. **Deuterium Synthesizer Level 1** (50 metal, 10 crystal)

Keep cycling: Mine upgrades → Solar/power expansion → Next mine level

### Phase 3: Sustained Growth (Ongoing)
- **Continuous cargo shuttling:** Home → Colonies every 2 minutes
- **Build queue management:** Keep queues populated, avoid idle time
- **Energy target:** 100% efficiency on all colonies at all times
- **Mining expansion:** Upgrade metal/crystal/deuterium in parallel
- **Cargo ship deployment:** Use newly built cargo ships to increase bootstrap payload

## Resource Allocation

**Home Planet (5080):** Primary source
- Sends continuous cargo to 5:316:2 and 5:317:12
- Maintains minimum reserves for home production
- Cargo capacity: Limited by available small cargo + incoming large cargo ships

**Bootstrap Runs:**
- Frequency: Every 2 minutes (autonomous cycle)
- Content: Metal-heavy (3-5K), crystal (1-2K), deuterium as available
- Timing: Coordinate with build queue completion

## Key Constraints & Solutions

| Constraint | Solution |
|-----------|----------|
| Small cargo capacity (10K limit) | Build large cargo ships; leverage multiple runs |
| Energy shortage on new colonies | Prioritize solar plants before mine expansion |
| Build queue bottleneck | Keep 3+ builds queued per colony at all times |
| Resource exhaustion at home | Monitor home production; throttle sends if needed |

## Autonomous Loop Behavior

**Every 2 Minutes:**
1. Check all 3 colonies' production reports
2. Verify energy efficiency ≥ 100%
3. Check for completed cargo ships at home
4. Route cargo to colony with highest resource deficit
5. Queue next builds based on energy/resource availability
6. Prioritize: Power → Storage → Mines

**Build Priority Matrix:**
- Energy deficit? → Build solar plant immediately
- Storage full? → Build storage level
- Storage available, energy OK? → Build mine (metal > crystal > deuterium)
- All normal? → Upgrade existing mines

## Success Metrics

- All colonies reach energy independence within 1 hour of creation
- All colonies have ≥ 3 levels in all mine types within 6 hours
- Home planet sending bootstrap cargo every 2 minutes without depletion
- Build queues never empty on any colony

## Notes

- Previous colonization attempt to 5:317:8 failed (planet not created despite fleet arriving)
- Current targets (5:316:2, 5:317:12) selected for accessibility and resource positioning
- Cargo ships under construction at home will dramatically increase bootstrap efficiency once available

---

**Last Updated:** 2026-09-09 T13:26 UTC  
**Next Review:** After context compaction or every 30 minutes of autonomous operation
