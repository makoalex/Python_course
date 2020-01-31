class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '{} of {},'.format(self.value, self.suit)
