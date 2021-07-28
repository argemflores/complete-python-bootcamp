"""
Person: playing individual, can be the computer dealer or the human player
"""
class Person():
    """Initialize object"""
    def __init__(self, name):
        # name of the person
        self.name = name
        
        # sum of cards the person has for a round (default: 0 because hand is empty)
        self.value = 0
        
        # cards the person has in their hand for a round (default: empty list)
        self.hand = []
    
    """Draw a card from the deck then add to hand and compute hand value"""
    def hit(self):
        pass
    
    """Lock in hand and value for the round"""
    def stay(self):
        pass
    
    """Return person's name and hand value"""
    def __str__(self):
        return "{} | card/s: {} | value: {}".format(self.name, len(self), self.value)
    
    """Return person's no. of cards in hand"""
    def __len__(self):
        return len(self.hand)
