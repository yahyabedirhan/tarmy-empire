<!-- verbatim copy of https://docs.terminal.army/commands/ — do not edit; re-fetch to update -->

# Commands

Commands start with `/`. Type `/help` in the client for the short list, and `/q` to quit. Most commands accept short aliases, shown in parentheses.

Command coverage is checked against the client, with fleet workflows tested through the API and an isolated PostgreSQL database.

<div class="admonition tip">

Not installed yet?

<div class="highlight">

    curl -fsSL https://terminal.army/install.sh | sh

</div>

Then [create an account](https://terminal.army/signup) and run `tarmy`.

</div>

## Joint attacks and allied defense

- `/acs` lists your joint attacks and invitations; `/acs <id>` shows the target, ships and arrival.
- `/acs create <fleet>` turns your already-flying attack into an ACS group.
- `/acs invite <id> <username>` invites another commander, even outside your alliance.
- `/acs join <id> cruiser=10 [speed=100]` sends your own fleet to that group's target.
- `/hold g:s:p 2 cruiser=10 [moon] [speed=100]` defends an alliance member for two hours.
- `/hold` alone shows allied reinforcements heading to or holding at your own planets and moons.
- `/recall <fleet>` calls back your own outbound or holding fleet.

ACS allows 5 commanders and 16 fleets; a joining fleet may delay the remaining flight by at most 30%. All fleets fight together using their owners' technologies. Loot is divided by surviving free cargo space; each fleet flies home at its own original speed. Recalling the initiating fleet closes joining but leaves the other attacks flying. Defense lasts 0-32 hours, uses a fleet slot, and prepays holding fuel (no refund on recall). Defense is for the exact planet or moon, not both. Normal player protection and attack limits remain in force.

Example: `/attack 1:20:8 cruiser=10`, then `/acs create 123`, then `/acs invite 7 friend`. The invited commander runs `/acs 7` and `/acs join 7 cruiser=20`. Use the actual fleet/group IDs printed by the client.

## Planet & economy

| Command | Description |
|----|----|
| `/planet` (`/p`, `/overview`) | Show the current planet: resources, buildings, queue. |
| `/planets` | List your planets, numbered, with their codes and coordinates. |
| `/switch <n>` | Switch planet by number, code, or name. |
| `/resources` | Resource buildings: mines, energy, storage, crawlers. |
| `/facilities` | Facilities: robotics, shipyard, lab, nanite, silo, depot. |
| `/upgrade <key>` (`/u`) | Queue a building upgrade, e.g. `/upgrade metal_mine`. |
| `/queue` | Show the active build/research queue. |
| `/refresh` | Re-fetch the current planet. |

### Abandon a planet

The web action is available now. The TUI command and Commander tools below are included in source and will ship with the next client release.

`/abandon CODE` previews a specific planet and the moon, resources, buildings, ships, defenses and queues you would lose. Only after reviewing it, enter `/abandon CODE confirm`. The preview expires after five minutes. There is no undo or refund. Use `/planets` to find a code. The web offers the same review from [Planets](https://terminal.army/planets) via **Abandon planet**.

Your last planet is protected. A homeworld can be abandoned; your oldest remaining colony replaces it. Own flights and building construction on the planet or its moon must finish or be cancelled first. Other queues on those bodies are lost. See [abandonment rules](../mechanics/#abandoning-a-planet).

## Research

| Command | Description |
|----|----|
| `/research` (`/r`) | List your technology levels, or say so when you have none yet. |
| `/research <key>` | Queue a technology from the current planet, e.g. `/research energy`. |
| `/tree` | Show the research tree and prerequisites. |

## Fleet & military

| Command | Description |
|----|----|
| `/ships [build <key> <n>]` (`/ship`, `/s`) | List ships, or build them: `/ships build small_cargo 5`. |
| `/defense [build <key> <n>]` (`/def`) | List or build defenses. |
| `/fleet` (`/fleets`) | Show fleets in flight. |
| `/attack <g:s:p> ship=n` (`/atk`) | Send an attack fleet. |
| `/colonize <g:s:p>` (`/colonise`, `/colony`) | Found a planet in an empty slot. Sends one colony ship automatically; add escort ships or `m=`, `c=`, `d=` cargo if you want them to land there too. |
| `/transport <g:s:p> m=n c=n d=n` (`/tx`) | Transport resources. |
| `/espionage <g:s:p>` (`/spy`) | Send an espionage probe. |
| `/cancel <n>` | Take a queued build back by the number `/queue` prints. Its cost comes back: all of it for a level, the unbuilt share for a batch. Everything behind it moves up. |
| `/recycle <g:s:p> recycler=<n>` (`/harvest`) | Send recyclers to the debris field at those coordinates. The galaxy view shows each field, how many recyclers it takes, and how many you have; clicking it fills this in. |
| `/missile <g:s:p> <n> [moon] [first=<defence>]` (`/ipm`) | Fire `n` interplanetary missiles from this planet's silo. Add `moon` to hit the moon in that slot. `first=gauss_cannon` names what to destroy first; without it the dearest emplacement goes first. A salvo takes no fleet slot, cannot be recalled, and the defender is not warned. |
| `/moon` | Moon fields, phalanx range and jump gate status. Lists owned moons when a planet is selected. |
| `/phalanx <g:s:p>` | From a moon with a sensor phalanx: visible fleets at that planet, with ships and arrival or return times. 5 000 deuterium a scan. Moons cannot be scanned. |
| `/jump <moon> ship=n ...` (`/gate`) | From a moon with a jump gate: move ships to another of your moons instantly. Name the destination the way `/switch` does. No cargo goes through, and both gates rest for an hour. |
| `/galaxy [g:s]` (`/g`) | View a system. With no argument, the one you are standing in. |
| `/reports` | Combat, espionage and missile reports, newest first, each with a number. |
| `/report <n>` | Open one: the battle in one line, both sides priced, what stood back up, what died in each round, and whether the raid paid. A scan shows every hull and emplacement counted, priced and weighed for attack, then what there is to take and what stands over it. |

## Dark matter

Dark matter is the one thing here that is earned by being present rather than by waiting. An open session earns it by the minute, about 1.2 an hour, credited in fractions every ten minutes, for as long as your client (or an MCP commander) holds a session open. Close it and nothing accrues. There is nothing to build, deploy or collect: the balance is always current, and one unbroken session is paid for at most twelve hours.

| Command | Description |
|----|----|
| `/mine` (`/mining`, `/dark`) | Your dark matter balance, whether a session is earning it right now, and what it buys. |
| `/rush [queue id]` | Finish the next thing in this planet's queue now, at one dark matter a minute of remaining time, five at least. |
| `/boost` | A quarter more output from this planet's mines for a day. 100 dark matter, one per planet at a time. |
| `/rename <name>` | Give this planet a new name. The first name is free; every one after it costs 20 dark matter. |

The balance sits in the resource bar, beside metal, crystal and deuterium.

## Social

| Command | Description |
|----|----|
| `/msg <user> <text>` (`/message`) | Send a player message. |
| `/messages`, `/inbox` | Who you are talking to, one row each, and one row for the server with its newest notice and how many are unread. |
| `/messages #server` | Everything the server has sent, oldest first, with the day where it changes: quests paid, fleets home, attacks, moons formed, missile strikes. Opening it marks them read. |
| `/messages <user>` | That conversation in full, oldest first. |
| `/alliance` | List / create / join / leave alliances. |
| `/ally` | Open your current alliance's private channel. Messages arrive live and opening it clears its unread count. |
| `/ally <text>` | Send a message to every current member of your alliance. |
| `/leaderboard` (`/rank`, `/lb`) | Global rankings. |

## Help & meta

| Command | Description |
|----|----|
| `/quest`, `/quests` | Your quest ladder, eighty-five rungs from the first mine to the Deathstar: what is next, what each rung pays, and what it has already paid. Nothing is claimed: a finished rung is paid the next time the board is read, and a note lands in your inbox. A rung that finished while your silos were full says it is waiting for room. |
| `/codex [key]` (`/info`) | What every building, tech, ship and defence is, then its cost, requirements and numbers. |
| `/help` (`/h`) | Command reference. |
| `/version` (`/ver`) | Your client version, the server's, and whether they agree. |
| `/changelog [version]` (`/changes`, `/whatsnew`) | What each release changed, newest first, with a mark on the one you are running. `/changelog all` lists every release on one line each; `/changelog v0.6.0` shows a single release. The same list is at [terminal.army/changelog](https://terminal.army/changelog). |
| `/settings` (`/config`, `/prefs`) | Who you are signed in as, your language and your colour theme. |
| `/settings lang <code>` (`/lang`, `/language`) | Change the language: `en`, `de`, `es`, `tr`, `ru`. |
| `/settings theme <name>` (`/theme`) | Change the colour theme: `ion`, `ember`, `mono`, `paper`. |
| `/clear` | Clear the console pane. |
| `/logout` | Log out, delete the saved session key, and quit. |
| `/q` (`/quit`, `/exit`) | Quit. |

Both settings are remembered per server, so the choice survives a restart and a logout.

Starting `tarmy` also checks your version against the server's and updates itself when you are behind. `tarmy --no-update`, or `TARMY_NO_UPDATE=1`, skips that check; see [Update](../install/#update).

## Coordinates & arguments

Coordinates are written `galaxy:system:position`, e.g. `2:88:4`. Fleet composition uses `key=count`, and cargo uses `m=`, `c=`, `d=`:

<div class="highlight">

    /attack 2:88:4 light_fighter=20 cruiser=5
    /colonize 2:88:8
    /transport 3:41:8 large_cargo=10 m=100000 c=50000
    /missile 2:88:4 12 first=plasma_turret
    /jump 2 cruiser=30 battleship=4

</div>

`/galaxy` takes a system rather than a planet, so it wants two numbers, not three, and they are separated by a colon:

<div class="highlight">

    /galaxy 2:88

</div>

Item keys are the lowercase names you see in `/codex`, such as `metal_mine`, `solar_plant`, `small_cargo` or `energy`. `/codex <key>` describes any one of them.

## Ready to play?

The commands above only mean something once you have an empire. [terminal.army](https://terminal.army/) is where you get one.
