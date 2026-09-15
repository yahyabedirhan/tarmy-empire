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

**No trades, full stop**, until the Commander says otherwise. Decision 010 is rejected and decision 011 confirms it: we do not offer, accept, answer or *evaluate* trade offers, and no resource ever leaves the empire for another player. A member selling exactly what we lack is not an opportunity; do not raise it. **Stay silent** in alliance chat. The only exception is an alliance fight in which our fleet is actually required — the Lieutenant puts it to the Commander with the numbers and acts only on approval.

## Messaging

Every message we send or receive with a non-ally is a file in `ops/diplomacy/`. We sign as "an agent of yabepa". Every message to anyone — ally or not — is drafted, shown, and sent only on the Commander's approval.

## Revisit when

- BJACK's leadership changes or the alliance shrinks below the top 5.
- We are attacked by a BJACK member (should be impossible; if it happens, report immediately).
- The Commander says trades are open again.
