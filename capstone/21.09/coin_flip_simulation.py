#!/usr/bin/env python3

"""Coin Flip Simulation

Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.
"""

# use to randomize results from coin flips
import random

class CoinFlip:
    """Coin Flip class

    Simulate flipping a single coin however many times the user decides.
    Record the outcomes and count the number of tails and heads.
    """

    # define constants for a coin's heads and tails
    HEADS = 0
    TAILS = 1
    COIN = {HEADS: 'heads', TAILS: 'tails'}

    # define constants for minimum and maximum flips
    MIN_FLIPS = 1
    MAX_FLIPS = 1000

    def ask_num_flips(self):
        """
        Ask number of coin flips

        Prompt user for number of coin flips.
        Continue asking until correct number within range is provided.
        """

        # continue asking until correct number of flips is inputted
        while True:
            try:
                # ask number of flips within range
                num_flips = int(input('Flips? ({}-{}): '.format(self.MIN_FLIPS, self.MAX_FLIPS)))

                # check input number if within range
                if self.MIN_FLIPS > num_flips or num_flips > self.MAX_FLIPS:
                    # ask again if outside range of flips
                    print('Out of range, try again.')
                    continue
            except ValueError:
                # ask again if non-integer value is entered
                print('Invalid, try again.')
            else:
                # exit loop, correct number is entered
                break

        # return number of flips
        return num_flips

    @staticmethod
    def ask_show_results():
        """
        Ask whether to show entire results or not

        Prompt user whether to print entire results or not
        Continue asking until correct choice is provided.
        """

        # continue asking until correct choice is inputted
        while True:
            # ask whether to show outcomes (Y) or not (N)
            shown = input('Show results? (Y/N): ').upper()

            # check choice
            if shown in ['Y', 'N']:
                # exit loop, correct choice is entered
                break

            # invalid choice, ask again
            print('Invalid, try again.')

        # return shown (True or Fals)
        return shown == 'Y'

    def simulate_coin_flip(self, num_flips):
        """
        Simulate a coin flip

        Print the number a head or tail appears as many times the user wants in the coin flip
        """

        # prepare results
        results = []
        num_heads = 0
        num_tails = 0

        # flip coin for N number of times
        for _ in range(num_flips):
            # get random result from either heads or tails
            result = random.randint(self.HEADS, self.TAILS)

            # save result to list
            results.append(result)

            # update result
            if result == self.HEADS:
                # add 1 for heads
                num_heads += 1
            elif result == self.TAILS:
                # add 1 for tails
                num_tails += 1

        # return entire results and summary counts
        return (num_flips, num_heads, num_tails, results)

    def show_results(self, results, flips):
        """Show entire results from coin flips

        Show each coin flip and corresponding result of either heads or tails
        """

        # get max character length from number of flips
        max_char_length = len(str(flips))

        # print each flip result
        for flip, result in enumerate(results):
            # print either head or tail per flip (padded by 0)
            print('#{}: {}'.format(str(flip + 1).rjust(max_char_length, '0'), self.COIN[result]))

def main():
    """Main function

    Used for the coin flip simulation
    """

    # instantiate CoinFlip
    coin_flip = CoinFlip()

    # get number of coin flips
    num_flips = coin_flip.ask_num_flips()

    # flip coin for N number of times and count results
    flips, heads, tails, results = coin_flip.simulate_coin_flip(num_flips)

    # print no. of heads and tails resulting from N coin flips
    print('Flips: {} | Heads: {} | Tails: {}'.format(flips, heads, tails))

    # ask to show entire results or not
    if coin_flip.ask_show_results():
        coin_flip.show_results(results, flips)

if __name__ == '__main__':
    main()
