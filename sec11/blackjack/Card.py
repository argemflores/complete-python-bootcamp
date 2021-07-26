"""
Card: playing card in a normal deck
"""

class Card():
    """Initialize object"""
    def __init__(self, suit, rank, value):
        # hearts, diamonds, spades, clubs
        self.suit = suit
        
        # 2, 3, ..., 9, 10, Jack, Queen, King, Ace
        self.rank = rank
        
        # numeric value of a card; can be an integer or array (for Ace)
        # 2 to 10 count as their face value
        # J, Q, K count as 10
        # Ace counts as 1 or 11 depending on the player's choice
        self.value = value
    
    """Ask player to choose the value of the Ace card for their hand"""
    def choose(self):
        pass
