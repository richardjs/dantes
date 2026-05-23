def cardstr(card):
    rank, suit = card
    rank_str = "A23456789TJQK"[rank]
    suit_str = "CDHS"[suit]
    return f"{rank_str}{suit_str}"


def print_deal(deck):
    deck = list(deck)
    for i in range(6):
        print(" ".join([cardstr(card) for card in deck[i * 8 : i * 8 + 8]]))
    print(" ".join([cardstr(card) for card in deck[48:53]]))
