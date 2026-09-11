<!-- verbatim copy of https://docs.terminal.army/commander/ — do not edit; re-fetch to update -->

# Let an assistant play

`tarmy mcp` hands your empire to an AI assistant over the [Model Context Protocol](https://modelcontextprotocol.io). You keep playing in the terminal; this is a second way in, for the days when you would rather ask than type.

<div class="highlight">

    tarmy commander

</div>

That is the whole installation. The game finds every assistant on your machine that it knows how to set up (Claude Code, Codex, Gemini CLI), registers itself in each under its own full path, installs the bundled game skill, and tells you what to ask next. There is no account to create, no key to paste and nothing to configure: it uses the sign-in you already did, so if `tarmy` works then this works.

If it cannot find an assistant it knows how to set up, it prints the exact configuration and where to put it rather than guessing.

<div class="admonition tip">

Not signed in yet?

<div class="highlight">

    curl -fsSL https://terminal.army/install.sh | sh
    tarmy

</div>

Sign in once in the browser window it opens, quit with `/q`, then add the server.

</div>

## What it can do

Tools are grouped by what they cost you if they are used wrongly, not by what they touch. The question worth asking before handing over an empire is not "what does this reach" but "what can this lose".

| Tier | What it does | On by default |
|----|----|----|
| `read` | Looks at things. There is nothing to undo because nothing changes. | yes |
| `spend` | Commits resources: a level into the build queue, a batch of ships, a build rushed with dark matter. Queued levels can be cancelled for a full refund; batches refund unbuilt units. | yes |
| `commit` | Puts something at risk you cannot get back by waiting: a fleet in the air, a missile salvo, a phalanx scan paid for, a jump that rests both gates, a message another player reads, an alliance left. | yes |

`tarmy commander` hands over all three. An assistant that can look at your empire but cannot answer a message or move a fleet is a dashboard, not a commander.

Run it again whenever you like. It updates `tarmy` first if the server is running a newer release, then rewrites the entry in every assistant it finds, so there is nothing to remove first and no way to end up pointing at an old binary. A commander that is already running when a release lands says so in its own briefing, and your assistant will pass it on.

To hand over less, name the tiers you want:

<div class="highlight">

    tarmy commander --allow read,spend    # it builds and researches, it does not fly
    tarmy commander --allow read          # it only looks

</div>

A tier you did not hand over is **absent**, not present and refusing. An assistant shown a tool it cannot use will keep trying it and will tell you the game is broken.

`alliance_chat` is available in the read tier and does not clear the terminal's unread badge. `send_alliance_message` is in the commit tier because every current member can read it immediately.

## Keeping the commander current

Commander v1.2.0 adds OGame-style joint attacks. `acs_groups` and `allied_defenses` are read-tier tools. `create_acs`, `invite_acs` and `join_acs` are commit-tier tools, as are `dispatch_fleet(mission="defend", hold_hours=...)` and `recall_fleet`. Invitations send an in-game message. Joining reads the group's exact planet or moon, so no coordinate copying is needed. See the [command examples](../commands/#joint-attacks-and-allied-defense) for the equivalent terminal workflow. Reconnect an existing MCP session after updating.

Run `tarmy --version` to list the local client and Commander versions. Commander has an independent semantic version, starting at **v1.0.0**, shared by its MCP tools, briefing and bundled skill. The skill also records it in `metadata.version`. Game-only changes can leave the Commander version unchanged. The command checks installed guides against the bundle and identifies matching, outdated, customized or missing copies without modifying them or going online.

The TUI shows `tarmy <version> · commander <version>` at the bottom right; `/version` also includes Commander alongside the client and server. These are the versions in that executable. A running assistant may still use an older MCP process: its MCP handshake reports its own Commander version and the briefing identifies its tarmy build. Local version output is not a check for the latest published release; the normal launch updater still checks the server.

Starting `tarmy` updates the client and the MCP server together: both are part of the same executable at the registered path. It also refreshes previously installed game skills from the new executable. No extra command is needed for a normal upgrade, and your MCP name, server address and allowed tiers stay as you configured them. An assistant already connected to MCP keeps its running process; reconnect it or restart the assistant to load the new tools.

The skill is bundled in the release, so it does not need a separate download. Codex and Gemini use `~/.agents/skills/terminal-army/SKILL.md`; Claude Code uses `~/.claude/skills/terminal-army/SKILL.md`. Automatic refresh also recognizes previously installed copies in Gemini’s own skill directory and the legacy Codex skill directory. Only copies managed by tarmy are replaced. If you edit one yourself, tarmy preserves it and tells you where it is.

<div class="highlight">

    tarmy commander codex --skill-only  # install or refresh just the guide
    tarmy commander codex --no-skill    # register MCP without installing a guide

</div>

`--skill-only` requires no game sign-in and does not change MCP registration. `--print` prints configuration without signing in or updating anything. `--remove` removes the MCP registration; the reusable game guide stays installed. When refreshing an existing entry, keep its name and permission tier:

<div class="highlight">

    tarmy commander codex --name tarmy --allow read

</div>

## What it knows

The server sends a short briefing when a client connects, so the assistant starts out knowing the things about this game that are not true of the genre it comes from. The most expensive of those:

> Travel costs time, not fuel. One small cargo to the next system is about 3 deuterium and about 34 minutes each way.

An assistant working from general knowledge of the genre will worry about deuterium and ignore the clock, and it will be wrong in a way that costs you an afternoon.

## Asking for things

<div class="highlight">

    > what should I do next

    Your solar plant is at 8 and the production factor is 0.71, so every mine on
    the planet is running at about seven tenths. Take the plant to 9 first: 4,240
    metal and 1,590 crystal, about eleven minutes.

    The ladder paid room_to_keep_it while I was reading it: 2,500 metal landed on
    Homeworld. Next rung is deeper_shaft, metal mine 8, two levels away.

</div>

<div class="highlight">

    > is 8:260 worth looking at

    Twelve systems out. Forty minutes each way for a small cargo, four deuterium.
    Three of the fifteen slots are taken and none of the owners have been online in
    the last day. Slot 6 has a moon with four fields, so somebody parks a fleet
    there.

</div>

<div class="highlight">

    > scan 8:260:6 from my moon

    Two fleets. An attack from 8:255:3 landing at 21:14 with 40 light fighters and
    6 cruisers, and their own transport coming home at 21:40. Five thousand
    deuterium spent.

</div>

<div class="highlight">

    > break the wall at 8:260:6 before it lands

    Eleven missiles away, gauss cannons first, landing at 21:02. Their silo held
    four interceptors, so seven get through: both gauss cannons and about ten
    rocket launchers, and none of that rebuilds.

</div>

The commander reads reports the way the web does: a battle in one line, both sides priced, what stood back up, what died in each round, and whether the raid paid. A scan comes back with every hull counted and weighed for attack, then what there is to take and what stands over it.

## It is you

Every call goes out as your account, hits the same endpoints the terminal client hits, and is refused by the same rules. The server opens no new authority: an assistant cannot do anything you could not have typed yourself, and there is no tool here that reaches anybody else's empire.

## Other clients

<div class="highlight">

    tarmy commander

</div>

sets the game up in every assistant it finds on your machine: **Claude Code**, **Codex** and **Gemini CLI**. They are not alternatives, so it does not ask you to pick: somebody with two of them uses two of them. Name one to do just that one:

<div class="highlight">

    tarmy commander codex
    tarmy commander gemini

</div>

Each is told in its own syntax, and the syntaxes are theirs rather than ours: `claude mcp add`, `codex mcp add`, `gemini mcp add`. Before using any of them this checks that the version you have actually knows the subcommand, because a CLI that predates it answers an invented one with a usage error, and reporting that as a failure would send you looking for a fault in this game. When the check says no, the configuration is printed for you to paste instead.

For anything else, ask for the file it wants:

<div class="highlight">

    tarmy commander --print codex     # ~/.codex/config.toml, in TOML
    tarmy commander --print gemini    # ~/.gemini/settings.json
    tarmy commander --print cursor    # ~/.cursor/mcp.json
    tarmy commander --print           # the generic JSON, and where Claude keeps it

</div>

Codex is the one worth knowing about: it reads TOML, so the JSON every other client takes is not a file it can save anywhere.

<div class="highlight">

    [mcp_servers.commander]
    command = "/usr/local/bin/tarmy"
    args = ["mcp"]

</div>

The full path matters everywhere. Your assistant starts the server with its own environment, and a bare `tarmy` that resolves in your shell may resolve to nothing in that one, which is why `tarmy commander` writes the path it is running from.

`tarmy commander --remove` takes it back out of all of them.

## Moon controls

`moon_status` reads your moons' free fields, phalanx range, scan affordability, gate cooldown and destination gates. It makes no scan or jump. `phalanx_scan` spends 5,000 deuterium per scan; `jump_gate` moves ships between two owned gates with no cargo. Both action tools need the `commit` tier. The [moon mechanics](../mechanics/#moons) explain visibility and differences from OGame. New tools require a client release containing them.

## Combat forecasts

`combat_rules` reads the live server's rapid-fire table, unit stats, moon chance units and universe rules. `simulate_combat` calls that same server resolver with your supplied forces and technology. Both use the read tier and send no fleets. Use fresh espionage data, include stationary hulls, and treat sampled outcomes as estimates. New combat reports include `simulation_input` for reproducibility.
