# Future plan — a Lieutenant that runs 24/7 off the Commander's Mac

- **status:** idea, not specified
- **raised:** 2026-09-11T15:15Z by the Commander, after the loop went autonomous but still lives only inside an open desktop session
- **owner:** Commander (research), Lieutenant (build once a direction is picked)

## Problem
The empire loop (`empire-cycle`) is autonomous and wake-driven, but it only exists while a Claude Code session is open on the Commander's machine. Closing the app, sleeping the Mac, or losing the network kills the loop; queues then sit idle until the next session (the failure that motivated the autonomy change).

## Why the obvious answer does not work yet
Claude Code **cloud routines** (claude.ai/code/routines) run in Anthropic's cloud on a cron, but:
- they can attach only **claude.ai connectors** (remote HTTP/SSE MCP servers); the commander MCP is `tarmy mcp` over **stdio** on the Mac, holding the saved key;
- each fire is a fresh, isolated session; minimum interval **1 hour**; no long-lived `next_event` sleep, so no alarm on `fleet.incoming` between fires.

## Options to research (high level)
1. **VPS running Claude Code + `tarmy mcp` locally** — a small always-on box (Hetzner/Fly/…): `claude` in a `tmux`/`systemd` service running the loop exactly as today; the repo cloned there, pushes go to GitHub. Closest to the current design; the key moves to the VPS; cost = a small VM + tokens. Open questions: how to authenticate Claude Code non-interactively; how the Commander talks to it (SSH + `claude --resume`, or a Slack/Telegram bridge); watchdog for hangs (L7).
2. **Expose the MCP remotely, keep Anthropic's cloud as the runner** — wrap `tarmy mcp` in an MCP proxy (`mcp-proxy` / `supergateway`) serving Streamable-HTTP behind a Cloudflare Tunnel or VPS with a bearer token; register it as a **custom connector** on claude.ai; a routine runs `/empire-cycle` hourly with the sleep step replaced by "one cycle → handover". Degrades the loop to hourly; still needs a box for the proxy.
3. **Hosted MCP from terminal.army** — ask the game to serve `mcp` over HTTP with the account key (they already run an HTTP API: `tarmy serve`, `--remote`). Would make option 2 need no box at all. Depends on a third party.
4. **Hybrid** — option 1 for the loop, plus a routine as a heartbeat that checks the VPS pushed a `HANDOFF.md` in the last N hours and alerts the Commander if not.

## Constraints to carry into any design
- The account key is the whole empire: wherever it lives must be locked down (no public MCP without auth, no key in the repo).
- `next_event` is one stream per account: two Lieutenants (local + remote) consume each other's events (`docs/mcp/COMMANDER.md`); exactly one runner at a time, or every runner re-reads state and never trusts the event alone.
- Records and handoff stay in git; the runner must be able to push.
- The Commander must still be able to interrupt and ask questions (`AGENTS.md` → The loop).

## Not yet decided
Which option; budget; whether the Commander wants chat access to the remote Lieutenant or only reads `HANDOFF.md` / status reports. Turn this into a decision file under `strategy/decisions/` when picked.
