<!-- verbatim copy of https://docs.terminal.army/mechanics/ — do not edit; re-fetch to update -->

# Game mechanics

Every formula below is sourced from the [OGame Fandom Wiki](https://ogame.fandom.com/wiki/OGame_Wiki) and implemented in `internal/game`. `L` is the building/research level, `speed` is the universe's economy/fleet multiplier, and costs grow as `base × factor^(L-1)`.

## Joint fleets (ACS)

ACS follows the [official OGame ACS guide](https://board.origin.ogame.gameforge.com/index.php/Thread/790-Guide-10-ACS-guide/): up to 5 attacking commanders and 16 fleets, with joins delaying the current remaining travel by at most 30%. Combat uses each fleet owner's technologies; plunder follows surviving available cargo capacity. Every fleet returns at its own speed. Recalling the founder closes joining without canceling partners.

Allied defense holds at a selected planet or moon for 0-32 hours. The host counts toward the 5-defender limit; up to 16 support fleets reserve slots. Holding fuel is prepaid, must fit alongside cargo and is not refunded. Ships and cargo remain the visitor's property. Safety probes see support already holding at their arrival time. Protections and attack limits remain active; multiple fleets from one player in the same ACS count as one attack.

This release supports defense for current alliance members, not buddy lists. The alliance depot does not resupply or extend holds yet. There is no separate war declaration, scoring ladder or automatic removal of newbie protection. See [commands](../commands/#joint-attacks-and-allied-defense) for examples.

## Resource production (per hour)

| Resource | Formula |
|----|----|
| Metal | `30 · L · 1.1^L · speed · (1 + plasma·0.01) · (1 + posBonus)` |
| Crystal | `20 · L · 1.1^L · speed · (1 + plasma·0.0066) · (1 + posBonus)` |
| Deuterium | `10 · L · 1.1^L · (1.36 − 0.004·T_avg) · speed · (1 + plasma·0.0033)` |

Every planet also receives a small passive trickle (`30·speed` metal, `15·speed` crystal) even with no mines. `T_avg` is the planet's average temperature: cooler planets synthesise more deuterium.

**Position bonuses.** Metal mines get +17/23/35/23/17% on slots 6-10; crystal mines get +40/30/20% on slots 1–3.

## Energy

Mines only run at full output while energy production covers consumption; otherwise output scales by the production factor.

| Source | Formula |
|----|----|
| Solar Plant | `floor(20 · L · 1.1^L)` |
| Fusion Reactor | `floor(30 · L · (1.05 + 0.01·energyTech)^L)` |
| Solar Satellite | `floor((T_avg + 160) / 6)` per satellite |
| Mine consumption | `ceil(coeff · L · 1.1^L)`, coeff 10 (metal/crystal) or 20 (deut) |

Fusion reactors burn `ceil(10 · speed · L · 1.1^L)` deuterium per hour.

## Storage

<div class="highlight">

    capacity(L) = 5000 · floor(2.5 · e^(20·L/33))

</div>

with a base capacity of 10,000 at level 0. Production is lost once a pool hits its cap, so storage upgrades matter.

## Build & research time

<div class="highlight">

    build_seconds   = (metal + crystal) / (2500 · (1 + robotics) · speed · 2^nanite) · 3600
    research_seconds = (metal + crystal) / (1000 · speed · (1 + lab)) · 3600

</div>

Redesigned universes apply an extra early-level speed-up (`(7 − L) / 2`) through level 5, so the opening buildings finish quickly. `lab` is the highest Research Lab across all your planets.

## Fleet movement

**Distance** between coordinates:

| Case                             | Distance                 |
|----------------------------------|--------------------------|
| Different galaxies               | `20000 · |Δgalaxy|`      |
| Same galaxy, different systems   | `2700 + 95 · |Δsystem|`  |
| Same system, different positions | `1000 + 5 · |Δposition|` |
| Same coordinates                 | `5`                      |

**Flight duration** (V = slowest ship speed, A = universe fleet speed, `spFactor` = throttle ÷ 100):

<div class="highlight">

    duration = (10 + (3500 / spFactor) · √(10 · distance / V)) / A

</div>

**Fuel** (per ship, summed): `baseFuel · count · (distance / 35000) · (1 + spFactor)²`.

**Drive bonuses** add to base ship speed: Combustion +10%/level, Impulse +20%/level, Hyperspace +30%/level.

**Galaxy view**: displaying a system other than your own costs **10 deuterium** per jump. Your own system is always free, and refreshing the system you just paid for costs nothing.

## Colonisation

`/colonize g:s:p` sends one colony ship from the current planet to an empty slot. The ship is consumed when the new planet is founded; any escort ships and cargo named on the command land on the colony.

Astrophysics sets both limits. The maximum planet count, including the homeworld, is `1 + ceil(level / 2)`. Levels 1-3 can settle positions 4-12, levels 4-5 positions 3-13, levels 6-7 positions 2-14, and level 8 or higher any position from 1-15.

## Abandoning a planet

Use **Abandon planet** on the web Planets page, `/abandon CODE` in the terminal, or Commander `preview_abandon_planet`. Review the named planet and its moon before confirming. Abandonment is immediate and cannot be undone.

- Your last planet in a universe cannot be abandoned. A homeworld can be; the oldest remaining colony becomes the new homeworld.
- The planet and its moon leave your empire together, including buildings, resources, ships and defenses. Completed research and other planets remain.
- Your own flights from either body, or heading to/holding at either body, block abandonment. Finish or cancel building construction on both bodies first.
- Ship, defense and research queues on those bodies are cancelled without refunds. Foreign flights do not block abandonment and continue normally.
- The colony allowance and score are released immediately. The coordinates stay occupied by attackable, unowned ruins. Resources and units left behind remain available to raiders, with no production or former-owner research bonuses.
- The position clears at the daily **03:00 UTC** cleanup after at least 24 hours, so the wait is 24-48 hours regardless of universe speed. The exact date is shown in the preview and galaxy view. Incoming foreign fleets survive cleanup and find an empty coordinate; they are not silently deleted.

The gameplay follows the [OGame abandonment FAQ](https://board.en.ogame.gameforge.com/index.php?pageNo=39&user-post-list%2F94133-safira%2F=), [homeworld succession explanation](https://board.en.ogame.gameforge.com/index.php?postID=6653650&thread%2F737156-abandon-homeworld-and-fields-required%2F=) and [colonization guide](https://forum.pt.ogame.gameforge.com/forum/thread/11128-planetas-coloniza%C3%A7%C3%A3o-e-campos/). Our confirmation uses your authenticated session, a typed planet code and a five-minute signed preview instead of passing an OGame-style password through MCP/chat. Server reset time here is UTC. Independent moon abandonment, relocation and Lifeform mechanics are outside this feature.

## Combat

A battle runs up to **six rounds**. Both sides fire at random targets, including units destroyed earlier in the same round. If both sides survive six rounds, the result is a draw. Weapons, Shielding and Armour add 10% per level.

- **Rapid fire.** A cruiser hitting a rocket launcher rolls a 90% chance to fire again at another random target (RF 10); against light fighters it is 5/6 (RF 6). These are extra shots, not guaranteed kills. Mixed targets can end the chain.
- **Shields and hull.** Hull is structural integrity divided by ten. Shields regenerate each round; hull damage persists. Shots at or below 1% of original shield strength bounce while shields remain; effective shield damage uses whole percentages. Below 70% hull, every effective hit can cause an explosion, including shield-only hits.
- **Stationary hulls.** Solar satellites and crawlers can be destroyed in combat and leave ship debris. They cannot fly away. Their losses reduce production.
- **Loot.** At most half of each stockpile, within surviving free cargo space. Loading follows the five-pass OGame algorithm; a metal-only target may leave empty cargo even when more metal is available.
- **Debris.** 30% of destroyed ships' metal/crystal goes into orbit. Defenses leave no debris. Seven in ten destroyed defenses rebuild, rolled per unit.
- **Protection.** Attacks at five times the defender's invested score or more are refused. Unspent resources do not count for either side. This universe's 5x gate applies at all scores.
- **Bashing.** Six attacks on one planet in twenty-four hours.
- **Vacation.** At least 48 hours, blocking hostile missions.

New reports distinguish initial firepower from actual shot counts, show moon chance as a percentage, and preserve the inputs used at arrival. Commander `combat_rules` reads the live matrix; `simulate_combat` runs the actual server resolver on supplied intelligence. Sampled outcomes are not guarantees. [Detailed rules and compatibility limits](https://github.com/cobanov/terminal-army/blob/main/docs/combat-rules.md).

## Moons

A battle at a planet can leave a **moon**: the chance is the ship debris it made **÷ 100 000, rounded down to a whole percentage and capped at 20%**. Below 100 000 new debris, the chance is zero. The moon belongs to the defender, one per planet, at the same coordinates.

A moon is not a small planet. It **mines nothing**, starts with **one field**, and only these can stand on it: Robotics Factory, Shipyard, the three storages, Lunar Base, Sensor Phalanx, Jump Gate. Any defence can be built on it. It holds no missile silo, so the anti-ballistic missiles on the planet below defend it.

| Building | Cost (base, ×2 a level) | Needs | Does |
|----|----|----|----|
| Lunar Base | 20 000 / 40 000 / 20 000 | nothing | +3 fields a level, one of which it occupies. Cannot be taken down. |
| Sensor Phalanx | 20 000 / 40 000 / 20 000 | Lunar Base 1 | Reads visible fleets at a planet, with ships and the relevant arrival or return time. Range `level² − 1` systems, same galaxy. 5 000 deuterium a scan. **Moons cannot be scanned**, which is why a fleet is parked on one. |
| Jump Gate | 2 000 000 / 4 000 000 / 2 000 000 | Lunar Base 1, Hyperspace 7 | Moves ships between two of your moons instantly, no fuel, no cargo. Both gates rest 60 minutes. |

`/moon` shows the selected moon's controls, or lists your moons. The overview also shows free fields, phalanx range and gate readiness. Commander exposes these through `moon_status`, with `phalanx_scan` and `jump_gate` for actions. Keep one free field for the next Lunar Base. Bring resources by transport; use `moon` in a terminal fleet command or `target_moon=true` in Commander.

A phalanx sees outbound deployment only at its destination; recalled deployment is invisible. Other returns are visible only at their origin. It reveals no cargo. These rules follow the [OGame moon guide](https://board.en.ogame.gameforge.com/index.php?thread/306885-moon-jumpgate-and-phalanx-faq-ver3/). Our moon system is a subset: diameter, destruction, standalone moon abandonment, relocation and class/event bonuses are not implemented. Gate cooldown remains 60 minutes at every level.

## Missiles

The Missile Silo is capacity, not a permit: **5 interplanetary and 10 anti-ballistic missiles per level**.

| Missile | Cost | Needs | Rule |
|----|----|----|----|
| Interplanetary | 12 500 / 2 500 / 10 000 | Silo 4 | 12 000 attack against emplacements only. Ignores every shield, both domes included. Cannot be met by ships, takes no fleet slot, cannot be recalled, and the defender is not warned. **Nothing it destroys rebuilds.** |
| Anti-ballistic | 8 000 / 0 / 2 000 | Silo 2 | Destroys exactly one incoming missile, launching on its own, before anything lands. |

Range is **5 × Impulse Drive − 1** systems, inside your own galaxy. Flight time is `(30 + 60 × systems) / fleet speed` seconds. Without a target order the salvo takes the dearest emplacement first; `first=` names one.

## Graviton and the Deathstar

**Graviton Technology** needs Research Lab 12 and costs no ore at all: 300 000 spare energy on one planet at the moment it is queued. The **Deathstar** (5 000 000 / 4 000 000 / 1 000 000; 200 000 attack, 50 000 shield, 9 000 000 hull; speed 100; hold 1 000 000) needs Shipyard 12, Hyperspace 6, Hyperspace Drive 7 and Graviton 1. It is the last rung of the quest ladder.

## Dark matter

Earned only while a session is open: **0.02 a minute**, about 1.2 an hour, credited every ten minutes, one unbroken session paid for at most twelve hours. It rushes a build (1 a minute of remaining time, 5 at least), boosts a planet's mines by a quarter for a day (100), and renames a planet after the first free name (20).

## Ranking

Score is everything you have **spent** ÷ 1 000: buildings, research, ships and defences at what they cost. Small cargo, large cargo, colony ship, recycler and espionage probe count **half**, because a hold full of freight is not a fleet.

## The quest ladder

Eighty-five rungs, from the first mine to the Deathstar, in the order the tech tree actually unlocks. The first two dozen are the tutorial and each pays for the next; the rest carry the order and pocket money. Nothing is claimed: a finished rung is paid the next time the board is read, and a rung that finished while your silos were full waits for room.

## Costs & prerequisites

Building and research costs grow geometrically from a per-item base and factor, and each item gates behind building/research prerequisites (e.g. Fusion Reactor needs Deuterium Synthesizer 5 + Energy Technology 3). The client resolves all of this server-side and shows you cost, time, affordability, and lock reasons per row, so you never have to compute anything by hand.

None of it is worth reading without an empire to spend it on. [Play at terminal.army →](https://terminal.army/)
