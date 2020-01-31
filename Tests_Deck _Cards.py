from DeckCards import Card
from DeckCards import Deck
import unittest

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card('A', 'Hearts')
    def test_innit(self):
        self.assertEqual(self.card.suit, 'Hearts')
        self.assertEqual(self.card.value, 'A', 'giving it a value')
    def test_repr(self):
        self.assertEqual(repr(self.card), 'A of hearts')
class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    def test_innit(self):
        self.assertEqual(self.deck.cards, list)
        self.assertEqual(len(self.deck.cards), 52)
    def test_repr(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')
    def test_count(self):
        self.assertEqual(self.deck.count, len(self.deck.cards))
    def test_shuffle(self):







        if __name__ == '__main__':
             unittest.main()