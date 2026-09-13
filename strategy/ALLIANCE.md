# Alliance and diplomacy

Decision 007. We are in **BJACK**, the alliance of the current #1 player. We joined for the quest; we stay because it is an umbrella: members cannot attack each other, and the biggest fleets in the universe are inside it.

## Posture

- **Stay in BJACK.** Leave only on the Commander's order. Leaving is `commit` tier and immediate.
- **Be a quiet, useful member.** Read `alliance_chat` every cycle; log anything about targets, threats or requests in `ops/diplomacy/`. Answer direct questions from members; volunteer nothing about our stockpiles or fleet.
- **Allied defence** (`dispatch_fleet mission=defend`) is available to us and from us. Ask for it only when THREATENED and the simulation says we lose; offer it only on the Commander's order.
- **Targets inside BJACK are off limits**, and so is anyone a member calls a friend in chat.
- **Standing pacts** (Commander-approved, one line each):
  - **BTC — non-aggression, BJACK-wide, since 2026-09-13.** Never attack, and never probe-then-attack, a planet whose owner carries the BTC tag. Check the owner's tag in `galaxy` before every launch; a `farm` verdict in `intel/` on a BTC player is void. Known BTC systems (necati, 2026-09-13T16:00Z, coordinates change — the tag is the rule, the list is a hint): 5:131, 5:158, 5:159, 5:164, 5:176, 5:177, 5:181, 5:216, 5:217, 5:227, 5:238, 5:241, 5:242. Source: `ops/diplomacy/2026-09-13_BJACK-chat-btc-pact.md`.
- **Active non-allied targets**: before any attack on an active player, (1) check their alliance and its size in `alliances`; (2) if they belong to a strong alliance, do not attack alone — draft a message to a relevant BJACK member proposing a joint move (ACS), show it to the Commander, send only on approval; (3) log the conversation.

## Trading and speaking (Commander, 2026-09-11T18:30Z)

**No trades.** Decision 010 was rejected: we do not offer, accept or answer `[TAKAS]` lines, and no resource ever leaves the empire for another player. **Stay silent** in alliance chat. The only exception: an alliance fight in which our action is actually required (an [ACİL] defence call at a planet we can reach, an ACS we are asked to join) — then the Lieutenant puts it to the Commander with the numbers and acts only on approval. We *read* the channel every cycle for strategy and mechanics (L10) and copy what the members measure.

## Messaging

Every message we send or receive with a non-ally is a file in `ops/diplomacy/`. We sign as "an agent of yabepa". Every message to anyone — ally or not — is drafted, shown, and sent only on the Commander's approval.

## Revisit when

- BJACK's leadership changes or the alliance shrinks below the top 5.
- We are attacked by a BJACK member (should be impossible; if it happens, report immediately).
- Our score enters the top 200 (we become worth coordinating against).
