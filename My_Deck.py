class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '{} of {},'.format(self.value, self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        suit = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        value = ('A', 'K', 'J', 'Q','10', '9', '8', '7', '6', '5', '4', '3', '2')
        for s in suit:
            for v in value:
                self.cards.append(Card(v, s))
        print(self.cards)
        
