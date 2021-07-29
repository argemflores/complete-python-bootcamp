from Person import Person

"""
Player (Person): the human player
"""
class Player(Person):
    """Initialize object"""
    def __init__(self, name, bankroll):
        # name of the player (default: 'Player')
        self.name = name
        
        # amount of credits the player has (default: 0.0)
        self.bankroll = bankroll
        
        # amount of credits the player is waging for the round (default: 0.0)
        self.bet = 0.0
        
        # initialize Player as Person
        Person.__init__(self, name)
    
    """Ask player the amount to bet for the round"""
    def place_bet(self):
        # check bankroll if not empty
        if self.bankroll > 0:
            # bankroll has enough amount
            
            # continue asking player until right amount is bet
            while True:
                # ask player their bet
                bet = float(input("{}, place your bet (bankroll: {}): ".format(self.name, self.bankroll)))
                
                # check bankroll limits
                if bet > self.bankroll:
                    # bet must be within bankroll amount
                    print("Bet must not exceed bankroll")
                elif bet < 1:
                    # bet must not be less than 1
                    print("Bet must not be less than 1")
                else:
                    print("Bet placed: {} | Bankroll: {}".format(bet, self.bankroll))
                    
                    self.bet = bet
                    break
        else:
            # do not ask player since bankroll is not enough
            print("Bankroll not enough")
    
    """Update bankroll after winning bet"""
    def wins(self):
        print("{} wins!".format(self.name))
        
        self.bankroll += self.bet
        
    """Update bankroll after losing bet"""
    def loses(self):
        print("{} loses.".format(self.name))
        
        self.bankroll -= self.bet
    
    """Return details about the player"""
    def __str__(self):
        return Person.__str__(self) + " | bankroll: {} bet: {}".format(self.bankroll, self.bet)
