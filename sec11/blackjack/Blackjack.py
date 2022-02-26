import art
# from replit import clear

from Deck import Deck
from Dealer import Dealer
from Player import Player

print(art.logo)

# prepare and shuffle deck
deck = Deck()
deck.shuffle()

# prepare player
name = input("🧑 Enter player's name (default: 'Player'): ") or "Player"
bankroll = float(input("💰 Enter player's bankroll (default: $100): $") or 100)
player = Player(name, bankroll)

# prepare dealer
name = input("👨 Enter dealer's name (default: 'Dealer'): ") or "Dealer"
dealer = Dealer(name)

# play until deck runs out of cards or player has no more money in the bankroll
while len(deck) > 0 and player.bankroll > 0:
    # clear screen and print logo
    # clear()
    print(art.logo)

    # empty hands of player and dealer
    player.hand = []
    dealer.hand = []

    # reset hand values
    player.compute_value()
    dealer.compute_value()

    # draw two cards each for both player and dealer
    player.add_cards([deck.deal_one(), deck.deal_one()])
    dealer.add_cards([deck.deal_one(), deck.deal_one()])

    # ask player to place their bet
    player.place_bet()

    # show 1 card of dealer's hand
    dealer.show_hand(1)

    # ask player to hit or stay while hand value does not exceed 21
    while player.value <= 21:
        # show player's hand and compute their value
        player.show_hand()
        player.compute_value()
        print("  Value: {}\n".format(player.value))

        # ask player to hit or stay
        action = player.ask_action()

        # hit to deal one card, else stay
        if action == 'hit':
            # add card from the deck to player's hand and show them
            player.add_cards(deck.deal_one())
            player.compute_value()
        else:
            # stay, break from loop
            break

    # player decides to stay and hand value does not exceed 21
    if action == 'stay' and player.value <= 21:
        # show dealer hand and compute their value
        dealer.show_hand()
        dealer.compute_value()
        print("  Value: {}".format(dealer.value))

        # continue hitting until hand value is more than 17
        while dealer.value <= 17:
            # hit to draw one card from deck and add to hand value
            dealer.add_cards(deck.deal_one())
            dealer.compute_value()

        # show dealer's hand
        dealer.show_hand()
        print("  Value: {}".format(dealer.value))

    # show player's hand value
    player.show_hand()
    print("  Value: {}".format(player.value))

    # decide outcome for the round
    if player.value > 21:
        # player loses (dealer wins) because player's hand value exceeds 21
        player.loses(dealer.value)
    elif dealer.value > 21:
        # player wins (dealer loses) because dealer's hand value exceeds 21
        player.wins(dealer.value)
    elif player.value > dealer.value:
        # player wins (dealer loses) because player's hand value is more than the dealer's
        player.wins(dealer.value)
    elif player.value < dealer.value:
        # player loses (dealer wins) because dealer's hand value is more than the player's
        player.loses(dealer.value)
    else:
        # draw because both dealer and player has the same hand value
        print("Draw! {}'s hand {} is similar to {}'s hand {} 😮".format(player.name, player.value, dealer.name, dealer.value))

    # ask player to continue if is still playable
    if len(deck) > 0 and player.bankroll > 0:
        # ask player to continue playing or exit game
        choice = 'X'

        # continue asking until Y or N is entered
        while choice.upper() not in ['Y', 'N']:
            choice = input("\nContinue playing? [Y] yes [N] no: ")

        # player chooses to exit game
        if choice.upper() == 'N':
            print("{}'s earnings: ${} Congratulations! 🎉\n".format(player.name, player.bankroll))
            break
        else:
            print("{}'s bankroll is ${}. Game continues! 💪\n".format(player.name, player.bankroll))

else:
    # end game
    if len(deck) == 0:
        # when deck is empty
        print("\n🤷 Deck is already empty!\n")
    elif player.bankroll == 0:
        # when player's bankroll is empty
        print("\n🤷 Player has no more money!\n")

print("Game ends! Thanks for playing! 🙂")
