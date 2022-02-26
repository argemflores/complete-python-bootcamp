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

    """Add cards to hand"""
    def add_cards(self, cards):
        # add to hand based on the number of cards
        if type(cards) == type([]):
            # merge with existing hand if more than 1 card
            self.hand.extend(cards)
        else:
            # add 1 card to hand
            self.hand.append(cards)

    """Compute value of cards in hand"""
    def compute_value(self):
        value = 0

        # get the sum total of all card values in hand
        for card in self.hand:
            if type(card.value) == type([]):
                if self.__class__ == 'Player':
                    card.choose_value()
                else:
                    if self.value + 11 <= 21:
                        card.value = 11
                    else:
                        card.value = 1

            # add card value to total
            value += card.value

        # update hand value
        self.value = value

    """Show cards in hand"""
    def show_hand(self, limit=0):
        print("{}'s cards".format(self.name))

        # limit number of cards to display
        if limit == 0:
            # for player, show all cards and their total value
            # list all cards in hand
            for i, card in enumerate(self.hand):
                print("  [{}] {}".format(i+1, card))
        else:
            # for dealer, show only the first card
            # limit the card to show based on the limit
            for i, card in enumerate(self.hand):
                if limit > 0:
                    print("  [{}] {}".format(i+1, card))
                    limit -= 1
                else:
                    break

    """Ask whether to hit or stay"""
    def ask_action(self):
        # define choices
        choices = ['hit', 'stay']

        # ask until chosen a valid option
        while True:
            # ask choice
            choice = input("🤔 {}, do you want to [1] hit or [2] stay? ".format(self.name))

            # verify choice
            if choice == '' or choice not in ['1', '2']:
                # choice not within the valid options
                print("❌ Invalid choice, try again")
            else:
                # choice valid
                break

        # return choice
        return choices[int(choice) - 1]

    """Return person's name and hand value"""
    def __str__(self):
        return "Name: {} | card/s: {} value: {}".format(self.name, len(self), self.value)

    """Return person's no. of cards in hand"""
    def __len__(self):
        return len(self.hand)
