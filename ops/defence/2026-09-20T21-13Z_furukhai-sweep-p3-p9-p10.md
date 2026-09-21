---
when: 2026-09-20T20:1X-21:20Z, three more launches from 5:314:8 landing 21:13-21:20Z (continuation of the 20:18Z double strike on :1 and the capital)
attacker: Furukhai (BTC, rank 7) from 5:314:8 (Bakim)
fleets: 99195 → :3 (42 ships, 30 CR/12 LC); 99198 → :9 (69 ships, 55 CR/14 LC); 99207 → :10 (76 ships, 25 bomber/11 CR/25 destroyer/15 LC — his heaviest wave, first sighting of bombers/destroyers)
status: closed — all three lost; discovered ~8h late (session gap 20:19Z-05:08Z 09-21, no next_event calls covered this window)
---
## Context
Same recon/strike as `2026-09-20T19-57Z_furukhai-attack-p1.md` and `…-capital.md` — a single coordinated sweep of all six planets, 20:18-21:20Z. :14 was the only planet not hit (deut-world, low crystal, presumably not worth his time). The session lost visibility for ~8h after the capital/​:1 reports (20:19Z) and only picked this up at 05:08Z 09-21 via `messages`.

**Critical miss**: the mobile fleet evacuated from the capital (98925: 62 LF, 1 LC, 2 recyclers, 1 colony ship, 8 probes + 35k M/25k C/15k D) was deployed to :10 as the "safest" planet (strongest wall). It landed there 20:24:43Z — six minutes before :10 became a target itself (99207 launched separately, landed 21:20:26Z). The evacuation fleet was caught and destroyed in the :10 battle. **The colony ship — the one asset we could not rebuild in a day — is gone.**

## After (`reports kind=combat` 60533, 60539, 60548)
- :3 21:13:16Z: 30 CR + 12 LC vs 81 RL + 30 LL + 27 sats → attacker, lost 2 LC; we lost the wall (rebuilt 58 RL/23 LL) + 27 satellites + 2 LC; loot 132k C / 114k M / 3.2k D.
- :9 21:13:46Z: 55 CR + 14 LC vs 107 RL + 15 LL + 3 HL + 4 ion + 6 gauss + dome + 65 sats → attacker, lost 10 CR + 4 LC; we lost the wall (rebuilt 81 RL/10 LL/3 HL/4 ion/4 gauss/dome) + 65 satellites + 2 LC + 2 SC; loot 114k C / 84k M / 76k D.
- :10 21:20:26Z: **25 bomber + 11 CR + 25 destroyer + 15 LC** (his real battle fleet, first time seen — not the recon-wave cruisers/cargo) vs full wall (149 RL/20 LL/10 HL/5 ion/8 gauss/dome) + the evacuated fleet (62 LF, 6 LC incl. the :10-native ones, 4 SC, 2 recyclers, 8 probes, **1 colony ship**) + 61 satellites → attacker in 5 rounds, lost 3 CR + 9 LC (his heaviest losses of the day); we lost everything present — wall (rebuilt 100 RL/13 LL/9 HL/4 ion/7 gauss/dome), 61 satellites, and the entire evacuated fleet including the colony ship; loot 74k C / 74k M / 71k D.

## Empire-wide toll (all five hit planets, 20:18-21:20Z)
- Loot to Furukhai: ≈ 593k crystal / 304k metal / 270k deuterium.
- Every wall in the empire emptied to 0 at the moment of its hit (partial auto-rebuild since); every solar satellite in the empire destroyed (0 remaining anywhere) — capital, :10, :9, :3 all sitting at production factor 0.54-0.67 as of 05:08Z 09-21.
- Fleet: only :14's and :1's 3 LC each survive. Everything else — 62 LF, colony ship, 2 recyclers, up to 9 probes, ~13 LC/SC across the empire — is gone.
- Only :14 was not attacked (deut-world, low value).

## Lessons
- **Fleet-save must not land at a planet BTC could plausibly hit next** — deploying to :10 (our strongest wall, and therefore an obvious high-value BTC target on any real sweep) put the evacuated fleet in the path of his second, heavier wave instead of out of it. A true fleet-save target should be a planet BTC has no scanned reason to hit, or the fleet should hold in orbit / bounce between planets rather than land and sit.
- Recon-to-strike was not one probe → one strike: Furukhai ran a staged sweep, recon wave (cruisers/cargo) first on some planets, heavier hardware (bombers/destroyers) held back for the planet with the most to lose (:10, strongest wall = read as highest value). Assume a first strike is not the last if the attacker has more fleet in reserve.
- The session must not go dark during an active multi-planet attack — `next_event` should have kept running through the full sweep; an 8h gap between the capital report and discovering three more attacks is a process failure, not a game one. Needs a `writing-for-agents`/skill-level fix: never let the loop's sleep exceed the doctrine's 2h cap, and treat any unread combat message as force-cycling step 2 on wake.
- 015 (class walls are a floor, not a fleet answer) is now proven at empire scale, not just in one sim: nothing we could afford stopped 76 ships including bombers/destroyers. The only real defence category left unexplored is missiles (IPM ignore shields) and alliance ACS support — worth raising with the Commander.
