<!-- verbatim copy of https://docs.terminal.army/ — do not edit; re-fetch to update -->

# terminal.army

An **OGame-style multiplayer strategy game you play from a terminal**. Build mines, research technology, construct fleets, and raid other players, all from a single, fast, keyboard- and mouse-driven terminal client.

The client is one small binary. Install it, sign in once through the browser, and the game lives in your terminal from then on.

<div class="ta-cards">

<a href="install/" class="ta-card"><span class="ta-card__num">01</span><span class="ta-card__name">Install &amp; play</span><span class="ta-card__desc">One line to install, then <code>tarmy</code> to jump into the public universe.</span></a>

<a href="commands/" class="ta-card"><span class="ta-card__num">02</span><span class="ta-card__name">Commands</span><span class="ta-card__desc">Every slash command the client answers to, and what it does.</span></a>

<a href="mechanics/" class="ta-card"><span class="ta-card__num">03</span><span class="ta-card__name">Game mechanics</span><span class="ta-card__desc">The formulas behind mines, energy, build time, research and fleets.</span></a>

</div>

## What makes it different

- **Terminal-native.** The whole game is a rich TUI: a resource bar, a grouped menu, clickable tables, a live command line, and a status rail, with full mouse support and a responsive layout.
- **Real mechanics.** Every formula, coefficient, and tech-tree prerequisite is sourced from the [OGame Fandom Wiki](https://ogame.fandom.com/wiki/OGame_Wiki).
- **It keeps running.** Mines produce, build queues finish, and fleets arrive while the client is closed.
- **The whole tree.** Moons with a phalanx and a jump gate, interplanetary missiles, Graviton research and the Deathstar, an eighty-five-rung quest ladder, and an AI commander that can play it all over MCP.

## Quick start

<div class="highlight">

    curl -fsSL https://terminal.army/install.sh | sh
    tarmy

</div>

That's it. `tarmy` opens a browser sign-in, then drops you into your empire.

If the second line answers `tarmy: command not found`, the install worked and the directory it used is not on your `PATH` yet. The installer tells you which directory and prints the full path that works right now. See [If `tarmy` is not found afterwards](install/#if-tarmy-is-not-found-afterwards).

On Windows, install inside WSL: see [Windows](install/#windows).

**[Play at terminal.army →](https://terminal.army/)** · these pages are the manual; the game itself is over there.
