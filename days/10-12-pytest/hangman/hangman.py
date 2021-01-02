import os
import random
import time

WORDS = """
blender microwave stove pots pans kettle sink knives cutlery
breadboard taps sugar salt condiments sauce refridgerator
chopsticks""".split()


def choose_random_word():
    """Choose a random word from WORDS"""
    return random.choice(WORDS)


class Game:
    """Choose a random word from a list of things commonly
    found in the kitchen, and play hangman"""

    def __init__(self):
        self._guesses = set()
        self._answer = choose_random_word()
        self._win = False
        self._outword = {
            pos: ("_", letter) for pos, letter in enumerate(self._answer)}

        for value in self._outword.values():
            print(value[0], sep="", end="")
        print()


if __name__ == '__main__':
    game = Game()
