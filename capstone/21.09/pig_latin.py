#!/usr/bin/env python3

"""
Pig Latin

Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
Read Wikipedia for more information on rules. https://en.wikipedia.org/wiki/Pig_Latin
"""

def pig_latinize(word):
    """
    Pig latinize a word

    Transform a word to pig latin, where the initial consonants are transposed to
    the end of the word, and either an 'ay' or 'yay' is affixed to it
    """

    # prepare strings
    altered_word = ''
    first_consonants = ''

    # look for the first consonants in the word
    for letter in word:
        # letter is a consonant
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            # save for later transformation
            first_consonants += letter
        else:
            break

    # count the first consonants
    num_consonants = len(first_consonants)

    # transform based on the number of consonants
    if num_consonants >= 1:
        # one or more consonants: transpose to the end of the word, then affix 'ay'
        altered_word = word[num_consonants:] + first_consonants + 'ay'
    else:
        # no consonants: leave the word as is, then afiix 'yay'
        altered_word = word + 'yay'

    # return the new pig latinized word
    return altered_word

def ask_word():
    """
    Ask word

    Prompt user for word to convert to pig latin
    Check basic rules, e.g. ask again if empty or invalid (does not start with a letter)
    """

    # continue asking until valid word is entered
    while True:
        # prompt new word and strip whitespaces
        word = input('Enter word: ').strip()

        # check word if valid
        if len(word) == 0:
            # empty input: ask again
            print('Empty, try again.')
        elif not word[0].isalpha():
            # input does not start with a letter: try again
            print('Invalid, try again.')
        else:
            # valid input, break out of loop
            break

    # return entered word
    return word

def main():
    """
    Main function

    Executes the main flow of the script
    """

    # ask user for a valid word
    word = ask_word()

    # transform word to pig latin
    altered_word = pig_latinize(word)

    # show the new pig latinized word
    print('Pig Latinized:', altered_word)

if __name__ == '__main__':
    main()
