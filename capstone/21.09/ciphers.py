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

def main():
    """
    Main function

    Executes the main flow of the script
    """

    # initialize Cipher object
    cipher = Cipher()

if __name__ == '__main__':
    main()
