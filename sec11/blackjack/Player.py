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
        
        # initialize Player as Person
        Person.__init__(self, name)
    
    """Ask player the amount to bet for the round"""
    def wager(self):
        # check bankroll if not empty
        if self.bankroll > 0:
            # bankroll has enough amount
            
            # continue asking player until right amount is bet
            while True:
                # ask player their bet
                bet = float(input("Place your bet (bankroll: {}): ".format(self.bankroll)))
                
                # check bankroll limits
                if bet > self.bankroll:
                    # bet must be within bankroll amount
                    print("Bet must not exceed bankroll")
                elif bet < 1:
                    # bet must not be less than 1
                    print("Bet must not be less than 1")
                else:
                    # place in bet, subtract from bankroll
                    self.bankroll -= bet
                    self.bet = bet
                    print("Bet placed: {} | Bankroll updated: {}".format(bet, self.bankroll))
                    break
        else:
            # do not ask player since bankroll is not enough
            print("Bankroll not enough")
    
    """Ask player to choose the value of the Ace card for their hand (1 or 11)"""
    def choose_ace_value(self, card):
        # prepare prompt and value to ask player
        prompt = "Choose Ace card value ({}): ".format(" or ".join([str(value) for value in card.value]))
        value = 0
        
        # continue asking player until correct value is entered
        while True:
            # check entered card value
            if value not in card.value:
                # ask again if entered value is incorrect
                value = int(input(prompt))
            else:
                # correct value
                break
        
        # return chosen value
        return value
    
    """Return details about the player"""
    def __str__(self):
        return Person.__str__(self) + " | bankroll: {} | bet: {}".format(self.bankroll, self.bet)
