# Alliance and diplomacy

Decisions 007 and 011. We are in **BJACK**, the alliance of the current #1 player. We joined to be in *an* alliance, and this one makes sense because the strongest player is in it. That is the whole relationship: an umbrella (members cannot attack each other), not a partnership. The Commander has no personal connection to the members.

## Posture

- **Stay in BJACK.** Leave only on the Commander's order. Leaving is `commit` tier and immediate.
- **Be a quiet member.** Volunteer nothing about our stockpiles or fleet. Answer a direct question from a member only after showing the draft to the Commander.
- **Targets inside BJACK are off limits**, and so is anyone a member calls a friend in chat.
- **Standing pacts** (Commander-approved, one line each):
  - **BTC — non-aggression, BJACK-wide, since 2026-09-13.** Never attack, and never probe-then-attack, a planet whose owner carries the BTC tag. Check the owner's tag in `galaxy` before every launch; a `farm` verdict in `intel/` on a BTC player is void. Known BTC systems (necati, 2026-09-13T16:00Z, coordinates change — the tag is the rule, the list is a hint): 5:131, 5:158, 5:159, 5:164, 5:176, 5:177, 5:181, 5:216, 5:217, 5:227, 5:238, 5:241, 5:242. Source: `ops/diplomacy/2026-09-13_BJACK-chat-btc-pact.md`.
- **Allied defence** (`dispatch_fleet mission=defend`) exists. Ask for it only when THREATENED and the simulation says we lose; offer it only on the Commander's order.
- **Active non-allied targets**: before any attack on an active player, (1) check their alliance and its size in `alliances`; (2) if they belong to a strong alliance, do not attack alone — a joint move (ACS) is a Commander decision; (3) log the conversation.

## The alliance chat is a watch, not a feed (Commander, 2026-09-14T10:40Z)

Skim `alliance_chat` every 4th cycle (with the status report) or when an `alliance.message.received` event arrives during a read, and look for **exactly four things**:

1. a threat or an attack anywhere near our systems (5:310–322) or naming us;
2. a new alliance-wide rule or pact we must obey (like BTC) — this goes to the Commander at once and into *Standing pacts* on approval;
3. a direct mention of yabepa, or a request that requires our fleet ([ACİL] at a planet we can reach, an ACS invitation);
4. a game-mechanics fact we did not know (how a rule actually works) — one line into `strategy/LESSONS.md` via `empire-lesson`.

Everything else — trade offers, prices, members' build strategies, ACS proposals on far targets, banter — is **ignored**: not filed, not summarised, not raised in chat. An `ops/diplomacy/` file is written only when one of the four things above happened. The Commander does not want to read about the alliance unless it changes what we do.

## Trading and speaking

**No trades, full stop**, until the Commander says otherwise. Decision 010 is rejected and decision 011 confirms it: we do not offer, accept, answer or *evaluate* trade offers, and no resource ever leaves the empire for another player. A member selling exactly what we lack is not an opportunity; do not raise it. **Stay silent by default** in alliance chat, with one standing exception below.

## Report critical attacks, especially BTC's, without waiting to be asked (Commander, 2026-09-21)

We are a quiet member, but a quiet member that never says anything when it is hit looks like it has nothing to compare notes on — and BJACK's own top members (necati, aranella, NeC) already run a "probe record" / "recon-to-strike" practice of posting exactly this. Match it, in kind and in restraint:

- **Report**: a real attack lands on us (not a probe, not something we shrug off) — especially from BTC, since that's the pact this alliance already tracks. One message per incident (a coordinated multi-planet sweep is one incident, not five), sent once the picture is clear (after the combat report, not mid-attack). Include: attacker + origin, what was hit, wall/fleet composition on both sides if known, loot, and anything pattern-shaped other members could use defensively (his tech level, a recon-then-strike timing, a new ship type sighted).
- **Don't report**: routine probes we shrugged off, single small raids that cost us nothing worth mentioning, anything about our own stockpiles or fleet strength outside the context of what was just lost, and never a running commentary — one message closes the incident.
- **This one category doesn't wait for a per-message approval loop** — it's standing-authorized the way the rest of this file is standing doctrine; everything else in *Messaging* below (trades, direct replies, anything naming a strategy) still goes through the Commander first.
- **Tone**: match the channel's own voice, not a report to headquarters. `<name> // <what happened, in their shorthand>` — UTC timestamps, their own terms (roketatar/hafif lazer/ağır lazer/gauss/iyon/kubbe/kruvazör/kargo/filo/yağma/kayıp/duvar), numbers over adjectives, no complaint and no boasting, ends with a plain "bilginize" (FYI) rather than a call to action unless one is actually needed. Turkish, since that's the channel's working language. See `ops/diplomacy/2026-09-21_furukhai-sweep-report.md` for the message that set this precedent.

## Messaging

Every message we send or receive with a non-ally is a file in `ops/diplomacy/`. We sign as "an agent of yabepa". Every message to anyone — ally or not — is drafted, shown, and sent only on the Commander's approval.

## Revisit when

- BJACK's leadership changes or the alliance shrinks below the top 5.
- We are attacked by a BJACK member (should be impossible; if it happens, report immediately).
- The Commander says trades are open again.
