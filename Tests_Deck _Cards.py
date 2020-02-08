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
        self.assertEqual(repr(self.card), 'A of Hearts')


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_innit(self):
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)




    def test_deal_enough_cards(self):
        """deal the no of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards),10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_notEnough_cards(self):
        """deal the number  of cards left in the deck"""
        cards= self.deck._deal(80)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(),0)
    def test_deal_noCards(self):
        """deal throws a value error if the deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def testin_deal_card(self):
        """should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def testing_deal_hand(self):
        """should deal the number of cards passed within the function"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffleFullD(self):
        """should shuffle if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)
    def test_shuffle_dNotfull(self):
        """should return an error if the deck is empty"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()



        if __name__ == '__main__':
            unittest.main()
