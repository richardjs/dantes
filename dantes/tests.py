from unittest import TestCase

from .deal import microsoft
from .io import cardstr


class TestDeal(TestCase):
    def test_microsoft_deal_1(self):
        deal = microsoft(1)
        for i in range(len(deal)):
            # https://rosettacode.org/wiki/Deal_cards_for_FreeCell
            self.assertEqual(cardstr(deal[i]), [
                "JD", "2D", "9H", "JC", "5D", "7H", "7C", "5H",
                "KD", "KC", "9S", "5S", "AD", "QC", "KH", "3H",
                "2S", "KS", "9D", "QD", "JS", "AS", "AH", "3C",
                "4C", "5C", "TS", "QH", "4H", "AC", "4D", "7S",
                "3S", "TD", "4S", "TH", "8H", "2C", "JH", "7D",
                "6D", "8S", "8D", "QS", "6C", "3D", "8C", "TC",
                "6S", "9C", "2H", "6H",
            ][i])

    def test_microsoft_deal_9003000(self):
        deal = microsoft(9003000)
        for i in range(len(deal)):
            # https://freecellgamesolutions.com/fcs/?game=9003000
            self.assertEqual(cardstr(deal[i]), [
                "8C", "2S", "9D", "9C", "QC", "8S", "3C", "5C",
                "5D", "JD", "2D", "8H", "8D", "5S", "KH", "TS",
                "TC", "TH", "AH", "AS", "2H", "6C", "3S", "2C",
                "5H", "3D", "KC", "6D", "9H", "7H", "7D", "4S",
                "AC", "7S", "JC", "4H", "TD", "QS", "6H", "QD",
                "7C", "JS", "4D", "AD", "6S", "9S", "KS", "KD",
                "QH", "4C", "3H", "JH",
            ][i])
