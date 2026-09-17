# Glossary

One line per term. If a term you meet is missing, add it here in the same commit.

**Game**
- **coord / slot / position** — `galaxy:system:position`, e.g. `5:316:12`. 9 galaxies × 499 systems × 15 positions in Genesis.
- **homeworld / capital** — the first planet; if abandoned the oldest colony becomes it. We call our research/fleet home the capital.
- **colony** — any planet after the first. Allowed count `1 + ceil(astrophysics/2)`.
- **fields** — building slots on a planet; fixed at birth, only the terraformer adds more (+5 per level, the level itself takes one → net +4; needs nanite 1 on that planet and energy 12 — `codex`). A moon starts with 1 field and the lunar base adds +3 per level (occupying one).
- **production factor** — energy produced ÷ energy used, capped at 1. Below 1 every mine on that planet runs at that fraction.
- **storage cap** — a resource pool stops growing at its cap; production above it is lost.
- **position bonus** — metal +17/23/35/23/17 % on positions 6–10; crystal +40/30/20 % on positions 1–3; deuterium rises as the planet gets colder (higher positions).
- **quest ladder / rung** — 85 ordered objectives; reading `quests` pays finished rungs; the order is the tech tree's real unlock order.
- **fleet slot** — how many fleets may be in the air at once. We assume computer technology + 1 (OGame rule; the manual does not state it — unsourced, see `reports/research/`).
- **mission** (fleet) — `attack transport deploy colonize espionage recycle defend`.
- **transport vs deploy** — transport drops cargo and returns; deploy moves the ships there permanently.
- **fleet-save** — sending ships and resources away so they are not on the planet when an attack lands.
- **espionage / scan / probe** — an espionage-probe fleet reads a planet; the report's detail depends on espionage technology.
- **debris field** — 30 % of destroyed *ships'* metal/crystal, left in orbit; recyclers collect it. Defences leave none.
- **moon** — formed by chance at a battle: 1 % per 100 000 *ship* debris, capped at 20 %, zero below 100 000; mines nothing; hosts phalanx and jump gate.
- **phalanx** — moon building that reveals fleets at a planet in range; range = level² − 1 systems in the same galaxy (level 1 = own system only, 2 = 3, 4 = 15); 5 000 deuterium a scan; moons cannot be scanned (manual → Moons).
- **jump gate** — moon building (2M/4M/2M, lunar base 1 + hyperspace 7) that moves ships between two of our moons instantly, no fuel, no cargo; both gates rest 60 min (manual → Moons).
- **IPM / ABM** — interplanetary missile (12.5k/2.5k/10k, silo 4): 12 000 damage to turrets only, ignores domes, nothing it kills rebuilds, range 5 × impulse − 1 systems; anti-ballistic missile (8k/0/2k, silo 2) destroys exactly one incoming IPM. A silo level holds 5 IPM and 10 ABM (manual → Missiles, `codex`).
- **nanite factory** — capital-class facility (1M/500k/100k; robotics 10 + computer 10) that halves build time of buildings, ships and turrets *on that planet only* (`2^nanite` in the build-time formula).
- **protection rule / 5× gate** — attacks refused when attacker score ≥ 5× defender *invested* score (resources spent; held resources count for neither side — `combat_rules.attack_protection_basis`, manual → Combat → Protection).
- **bashing limit** — six attacks by one commander on one planet per 24 h.
- **inactive** — a player whose planets show no growth/activity across scans; the natural raid target.
- **score** — everything ever spent ÷ 1000 (freight ships count half).
- **dark matter (DM)** — earned only while a session is open (~1.2/h, 12 h max per unbroken session); buys rush (1/min of remaining time, min 5) and boost (100 = +25 % mines on one planet for 24 h). Renaming is free, once a day per world (changelog v0.15.4; `dark_matter.prices.rename = 0`).
- **ACS** — joint attack or allied defence with alliance members.
- **BJACK** — our alliance's tag.

**Ours**
- **Commander / Lieutenant / Soldier** — user / main session / sub-agent. See `AGENTS.md`.
- **cycle / heartbeat** — one iteration of the main loop (`empire-cycle` skill).
- **wake** — the condition a planet or mission is waiting for: an event name, a timestamp, or a resource threshold.
- **state / sub-state** — a planet's high-level phase (`BOOTSTRAP GROWING STALLED STAGING THREATENED`) and the detail inside it. Defined in `strategy/DOCTRINE.md`.
- **role** — what a planet is for (`capital`, `mine-world`, `forward-base`). Long-lived.
- **tags** — `+advantage` / `-disadvantage` labels on a planet or target so its situation is readable at a glance.
- **sortie** — one fleet launch (out, fight/load, back).
- **campaign** — all sorties against one target under one plan; one file in `ops/attacks/`.
- **verdict** (intel) — what to do with a target: `farm` (raid repeatedly), `watch`, `avoid`, `empty`.
- **mission brief** — the one-page order a soldier is spawned with (`empire-soldier` skill).
- **lesson** — a numbered entry in `strategy/LESSONS.md` linked to the event that taught it.
- **decision record** — a file in `strategy/decisions/` with context, options, choice, reasoning, revisit-when.
- **handoff** — `HANDOFF.md`, the state the next session resumes from.
