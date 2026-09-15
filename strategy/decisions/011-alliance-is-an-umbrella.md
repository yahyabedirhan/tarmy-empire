# 011 — The alliance is an umbrella, not a relationship

- **status:** accepted
- **date:** 2026-09-14
- **decided by:** Commander (direction given in chat, 2026-09-14T10:40Z)

## Context
- Cycles 9–24 read the BJACK chat every cycle, filed every trade offer and strategy thread in `ops/diplomacy/`, and raised offers (aranella, DenizYoldas, tarla) to the Commander as opportunities. Decision 010 (trading) had already been rejected on 2026-09-11.
- The Commander: "I don't have a strong connection with the alliance members. I don't know them personally. I just entered this alliance because I want to be part of one alliance, and this one makes sense because it is the alliance of the most powerful member of the game, and that's it. I won't be doing any trades anytime soon."

## Options
1. Keep reading and filing everything (status quo). Cost: Lieutenant attention and repo noise on things that never change what we do.
2. **Watch, don't feed**: skim the chat on the status-report cadence for threats, pacts, direct mentions and mechanics facts; ignore and never file trades, prices, strategy talk. No trade is ever evaluated.
3. Stop reading the chat entirely. Cost: we would have missed the BTC pact.

## Decision
Option 2. `strategy/ALLIANCE.md` → *The alliance chat is a watch, not a feed* lists the four things worth noticing. Trades are closed until the Commander reopens them; the Lieutenant does not present them as opportunities.

## Consequences
- `empire-cycle` step 1 no longer reads `alliance_chat` every cycle; the inbox (`messages`) still is.
- `ops/diplomacy/` gets a file only for one of the four watched things.
- Sleep is not interrupted by `alliance.message.received` (already the rule).

## Revisit when
- The Commander says trades are open again, or wants closer alliance ties.
- BJACK asks something of us directly.
