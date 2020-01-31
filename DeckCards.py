from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        value = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        for s in suit:
            for v in value:
                self.cards.append(Card(v, s))
        print(self.cards)

    def __repr__(self):
        return 'Deck of {} cards'.format(self.count())

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError(' Only full decks can be shuffled')
        return shuffle(self.cards)

    def _deal(self, number):

        cards_removed = min(self.count(), number)
        print('We will remove {} cards from the deck'.format(cards_removed))
        if self.count() == 0:
            raise ValueError('< All cards have been dealt >')
        cards_out = self.cards[-cards_removed:]
        self.cards = self.cards[:-cards_removed]
        return cards_out

    def deal_card(self):
        if self.count ==0:
            raise ValueError ('reshuffle a new deck of cards please!')
        self.deal_card = self._deal(1)
        return self.deal_card[0]

    def deal_hand(self, hand):
        self.deal_hand = self._deal(hand)
        return self.deal_hand



c=Deck()
print(c.shuffle())
print(c.deal_hand(5))