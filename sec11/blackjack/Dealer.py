from Person import Person

"""
Dealer (Person): the computer dealer
"""
class Dealer(Person):
    """Initialize object"""
    def __init__(self, name='Dealer'):
        Person.__init__(self, name)
