from Card import Card

"""
Deck: normal collection of 52 cards
"""
class Deck():
    """Class attributes"""
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
    
    """Initialize class"""
    def __init__(self):
        # list of all 52 cards in a normal deck
        self.cards = []
        
        # fill up deck with the basic 52 cards
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank, self.values[rank])
                self.cards.append(card)
    
    """Draw a card from the deck then give to person's hand"""
    def deal(self):
        pass
    
    """Get the total number of cards left in the deck"""
    def count(self):
        pass
