"""
Card: playing card in a normal deck
"""
class Card():
    """Class attributes"""
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}

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

    """Ask player to choose the value of the Ace card for their hand (1 or 11)"""
    def choose_value(self):
        # prepare prompt and value to ask player
        prompt = "Choose Ace card value ({}): ".format(" or ".join([str(value) for value in self.value]))
        value = 0

        # continue asking player until correct value is entered
        while True:
            # check entered card value
            if value not in self.value:
                # ask again if entered value is incorrect
                value = int(input(prompt))
            else:
                # correct value
                break

        # return chosen value
        self.value = value

    """Return details about the card"""
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
