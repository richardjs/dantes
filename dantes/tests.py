import unittest

import dantes


class TestCard(unittest.TestCase):
    def test_new_deck(self):
        deck = dantes.card.Deck()
        self.assertEqual(len(deck.cards), 52)

        for suit in dantes.card.Suit:
            with self.subTest(suit=suit):
                self.assertEqual(
                    len([card for card in deck.cards if card.suit == suit]), 13)

    def test_card_string(self):
        card = dantes.card.Card(12, dantes.card.Suit.HEARTS)
        self.assertEqual(str(card), 'QH')

        card = dantes.card.Card(11, dantes.card.Suit.SPADES)
        self.assertEqual(str(card), 'JS')

        card = dantes.card.Card(5, dantes.card.Suit.CLUBS)
        self.assertEqual(str(card), '5C')
