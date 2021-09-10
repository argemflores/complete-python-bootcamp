#!/usr/bin/env python3

"""
Vigenere / Vernam / Caesar Ciphers

Functions for encrypting and decrypting data messages. Then send them to a friend.
"""

# use to get list of letters (A-Z)
import string

class Cipher:
    """
    Cipher class

    Encrypt and decrypt text using Caesar, Vernam, and Vigenere ciphers
    """

    # define constants for ciphers, options, directions, and labels
    CIPHERS = {'1': '[1] Caesar', '2': '[2] Vernam', '3': '[3] Vigenere'}
    OPTIONS = {'1': '[1] Encrypt', '2': '[2] Decrypt'}
    DIRECTIONS = {'L': '[L] Left', 'R': '[R] Right'}
    LABELS = {'1': [' Plaintext:', 'Ciphertext:'], '2': ['Ciphertext:', ' Plaintext:']}

    def ask_inputs(self):
        """
        Ask input

        Prompt user for input.
        Continue asking until valid input is provided.
        """

        # get keys and values for validation purposes
        keys = self.OPTIONS.keys()
        values = self.OPTIONS.values()

        # continue asking until valid option is provided
        while True:
            # ask option and strip whitespaces
            option = input('Choose ({}): '.format(' '.join(values))).strip()

            # check option if valid
            if option in keys:
                # valid; break out of loop
                break

            # invalid choice; ask again
            print('Invalid choice, try again.')

        # continue asking until valid text is provided
        while True:
            # ask text and strip whitespaces
            text = input('Text: ').strip()

            # check text if not empty string
            if text != '':
                # valid text; exit loop
                break

            # empty text; ask again
            print('Empty text, try again.')

        # continue asking until valid number of shifts is provided
        while True:
            try:
                # ask number of shifts
                num_shifts = int(input('Shifts (1-{}): '.format(len(string.ascii_uppercase) - 1)))

                # check if number of shifts is within range (1-25)
                if num_shifts >= 1 or num_shifts <= len(string.ascii_uppercase) - 1:
                    # valid number of shifts; exit loop
                    break

                # out of range; ask again
                print('Out of range, try again.')
            except ValueError:
                # invalid number; ask again
                print('Invalid shifts, try again.')

        # get keys and values for validation purposes
        keys = self.DIRECTIONS.keys()
        values = self.DIRECTIONS.values()

        # continue asking until valid input is provided
        while True:
            try:
                # ask direction and capitalize input
                direction = input('Direction ({}): '.format(' '.join(values))).upper()

                # check if direction is within valid values (L/R)
                if direction in keys:
                    # valid direction; exit loop
                    break

                # invalid direction; ask again
                print('Invalid direction, try again')
            except ValueError:
                # invalid direction; ask again
                print('Invalid direction, try again.')

        # return inputs
        return (option, text, num_shifts, direction)

def main():
    """
    Main function

    Executes the main flow of the script
    """

    # initialize Cipher object
    cipher = Cipher()

    # ask user inputs
    option, text, num_shifts, direction = cipher.ask_inputs()

    print(option, text, num_shifts, direction)

if __name__ == '__main__':
    main()
