# Alliance and diplomacy

Decision 007. We are in **BJACK**, the alliance of the current #1 player. We joined for the quest; we stay because it is an umbrella: members cannot attack each other, and the biggest fleets in the universe are inside it.

## Posture

- **Stay in BJACK.** Leave only on the Commander's order. Leaving is `commit` tier and immediate.
- **Be a quiet, useful member.** Read `alliance_chat` every cycle; log anything about targets, threats or requests in `ops/diplomacy/`. Answer direct questions from members; volunteer nothing about our stockpiles or fleet.
- **Allied defence** (`dispatch_fleet mission=defend`) is available to us and from us. Ask for it only when THREATENED and the simulation says we lose; offer it only on the Commander's order.
- **Targets inside BJACK are off limits**, and so is anyone a member calls a friend in chat.
- **Active non-allied targets**: before any attack on an active player, (1) check their alliance and its size in `alliances`; (2) if they belong to a strong alliance, do not attack alone — draft a message to a relevant BJACK member proposing a joint move (ACS), show it to the Commander, send only on approval; (3) log the conversation.

## Messaging

Every message we send or receive with a non-ally is a file in `ops/diplomacy/`. We sign as "an agent of yabepa". Until the Commander says otherwise, every message to a non-ally is drafted, shown, and sent only on approval; alliance chat replies are free.

## Revisit when

- BJACK's leadership changes or the alliance shrinks below the top 5.
- We are attacked by a BJACK member (should be impossible; if it happens, report immediately).
- Our score enters the top 200 (we become worth coordinating against).
