from enum import Enum


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return ' CDHS'[self.value]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rank_str = ' A23456789XJQK'[self.rank]
        return f'{rank_str}{self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
