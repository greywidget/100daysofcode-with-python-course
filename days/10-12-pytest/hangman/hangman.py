import random
import string

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
        self._outword = list('_' * len(self._answer))

    def _update_word(self, guess):
        for pos, letter in enumerate(self._answer):
            if letter == guess:
                self._outword[pos] = letter

    def guess(self):
        """Ask user for input.
           Either return a lowercase letter or raise a ValueError with:
           'Please enter a letter in the range a-z'
           'Please enter a single character'
           'Already guessed'"""
        guess = input('Guess a letter of the secret word: ')
        if not guess:
            raise ValueError('Please enter a letter')

        if len(guess) > 1:
            raise ValueError('Please enter SINGLE letters only')

        if guess.lower() not in string.ascii_lowercase:
            raise ValueError('Letter must be in the range a-z')

        if (l_guess := guess.lower()) in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(l_guess)
        return l_guess

    def _validate_guess(self, guess):
        """Check if this letter is in the word. Print the following where
           applicable:
           {guess} is correct!
           {guess} is not in the word
           Return a boolean"""
        if guess in self._answer:
            print(f"{guess} is correct!")
            self._update_word(guess)
            return True
        else:
            print(f"Sorry, {guess} is a bad guess")
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        """Entry point/game loop, use a loop break/continue"""
        while self._answer != ''.join(self._outword):
            try:
                guess = self.guess()
                self._validate_guess(guess)
            except ValueError as ve:
                print(ve)
                continue

        print(f"You guessed it! The word was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()
