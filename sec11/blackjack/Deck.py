from Card import Card
from random import shuffle

"""
Deck: normal collection of 52 cards
"""
class Deck():
    # tells whether the deck is shuffled (default: False)
    is_shuffled = False

    """Initialize class"""
    def __init__(self):
        # list of all 52 cards in a normal deck
        self.cards = []

        # fill up deck with the basic 52 cards
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card(suit, rank, Card.values[rank])
                self.cards.append(card)

    """Draw the top card from the deck"""
    def deal_one(self):
        return self.cards.pop()

    """Shuffle the cards in the deck"""
    def shuffle(self):
        shuffle(self.cards)
        self.is_shuffled = True

    """Return details about the deck"""
    def __str__(self):
        return "{} card/s in deck (shuffled: {})".format(len(self.cards), str(self.is_shuffled))

    """Return the total number of cards left in the deck"""
    def __len__(self):
        return len(self.cards)
