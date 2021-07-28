from Person import Person

"""
Dealer (Person): the computer dealer
"""
class Dealer(Person):
    """Initialize object"""
    def __init__(self, name='Dealer'):
        # initialize Dealer as Person
        Person.__init__(self, name)
