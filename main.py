"""
File: word_guess.py
-------------------
Guess The Word!
"""

import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):
    """
    This function handles the gameplay for the Word Guess Game.
    """

    guessed_word = ['-'] * len(secret_word)
    guesses_left = INITIAL_GUESSES

    while guesses_left > 0:

        print("The word now looks like this:", ''.join(guessed_word))
        print("You have", guesses_left, "guesses left")

        guess = input(
            "Type a single letter here, then press enter: "
        ).upper()

        if len(guess) != 1:
            print("Guess should only be a single character.")
            continue

        if guess in secret_word:

            print("That guess is correct.")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess

        else:
            print("There are no " + guess + "'s in the word.")
            guesses_left -= 1

        if '-' not in guessed_word:
            print("Congratulations, the word is:", secret_word)
            return

    print("Sorry, you lost. The secret word was:", secret_word)


def get_word():
    """
    This function returns a secret word from the lexicon file.
    """

    with open(LEXICON_FILE, 'r') as file:
        word_list = file.read().splitlines()

    return random.choice(word_list)


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """

    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

