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

    @staticmethod
    def caesar(text, num_shifts, direction):
        """
        Caesar cipher

        Substitute each letter in the plaintext with a letter
        some fixed number of positions down the alphabet.

        With a left shift of 3, D would be replaced by A, E would become B, and so on
        Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
        Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

        With a right shift of 3, D would be replaced with G, E would become H, and so on
        Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
        Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
        """

        # prepare resulting text
        result = ''

        # count number of letters A-Z
        max_num_letters = len(string.ascii_uppercase)

        # process each character in the text
        for character in text:
            # get index of capitalized character from the alphabet A-Z
            index = string.ascii_uppercase.find(character.upper())

            # check if valid alphabet/letter
            if index >= 0:
                # valid letter; continue processing

                # process shifts based on the direction
                if direction == 'L':
                    # left shift; move N shifts to the left of the index
                    shifted_index = index - num_shifts

                    # check if shifted index is within range (min: 0)
                    if shifted_index < 0:
                        # below 0; wrap around the alphabet, moving to Z
                        shifted_index = index - num_shifts + max_num_letters
                elif direction == 'R':
                    # right shift; move N shifts to the right of the index
                    shifted_index = index + num_shifts

                    # check if shifted index is within range (max: 25)
                    if shifted_index >= max_num_letters:
                        # exceeds 25; wrap around the alphabet, moving to A
                        shifted_index = index + num_shifts - max_num_letters

                # get the new character from the alphabet using the shifted index
                new_character = string.ascii_uppercase[shifted_index]
            else:
                # invalid (spaces or special characters); character remains unchanged
                new_character = character

            # add new character to resulting text
            result += new_character

        # return resulting text
        return result

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

    # process caesar cipher
    result = cipher.caesar(text, num_shifts, direction)

    # display original and resulting texts
    print(cipher.LABELS[option][0], text)
    print(cipher.LABELS[option][1], result)

if __name__ == '__main__':
    main()
