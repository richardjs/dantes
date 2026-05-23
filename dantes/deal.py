# https://rosettacode.org/wiki/Deal_cards_for_FreeCell
def microsoft(seed):
    def lcg_rng(seed):
        state = seed
        while True:
            state = (214013 * state + 2531011) % 2**31
            yield state // 2**16

    rng = lcg_rng(seed)

    deck = []
    for rank in range(13):
        for suit in range(4):
            deck.append((rank, suit))

    deal = []
    while deck:
        i = next(rng) % len(deck)
        deal.append(deck[i])
        deck[i] = deck[-1]
        deck.pop()

    return deal
