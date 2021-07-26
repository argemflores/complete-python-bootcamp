from Person import Person

"""
Player (Person): the human player
"""
class Player(Person):
    """Initialize object"""
    def __init__(self, name='Player', bankroll=0.0):
        # name of the player (default: 'Player')
        self.name = name
        
        # amount of credits the player has (default: 0.0)
        self.bankroll = bankroll
        
        # amount of credits the player is waging for the round (default: 0.0)
        self.bet = 0.0
    
    """Ask player the amount to bet for the round"""
    def wager(self):
        pass
