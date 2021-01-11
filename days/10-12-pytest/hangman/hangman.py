import click
import random
import string

MAX_GUESSES = 7

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
        self._bad_guesses = 0
        self._answer = choose_random_word()
        self._win = False
        self._outword = list('_' * len(self._answer))
        self._message = ''
        self._hm = self._get_gallows()

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
            self._message = f"{guess} is correct!"
            self._update_word(guess)
            return True
        else:
            self._bad_guesses += 1
            self._message = f"Sorry, {guess} is a bad guess"
            return False

    def _draw(self, stage=0):
        """
        Draw the gallows and hangman, in stages.
        This isn't really an important part of the game, so for now I'm
        keeping it simple.
        first stage = just the gallows.
        last stage = you've been hung!
        """

        click.clear()
        click.secho(''.join(self._outword), fg='green', nl=False)
        click.secho(self._hm[stage], fg='red')
        click.secho(self._message, fg='blue')

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        """Entry point/game loop, use a loop break/continue"""
        click.clear()
        while self._bad_guesses < MAX_GUESSES:
            self._draw(stage=self._bad_guesses)

            try:
                guess = self.guess()
                self._validate_guess(guess)
            except ValueError as ve:
                self._message = str(ve)
                continue

            win = self._answer == ''.join(self._outword)
            if win:
                self._message = (
                    f'You win, it took you {self.num_guesses} guesses')
                self._win = True
                break
        else:
            # else on while/for = anti-pattern? do find it useful in this case!
            self._message = 'Sorry you have been HUNG'

        self._draw(stage=self._bad_guesses)
        click.secho("The answer was ", fg='blue', nl=False)
        click.secho(self._answer, fg='green')

    def _get_gallows(self):
        """
        Very basic stick figures for the gallows
        """

        hm = ['' for _ in range(8)]

        hm[0] = \
            """
        ____
        |  |
        |
        |
        |
        |
        |
        |
        -------"""

        hm[1] = \
            """
        ____
        |  |
        |  O
        |
        |
        |
        |
        |
        -------"""

        hm[2] = \
            """
        ____
        |  |
        |  O
        |  |
        |
        |
        |
        |
        -------"""

        hm[3] = \
            """
        ____
        |  |
        |  O
        | /|
        |
        |
        |
        |
        -------"""

        hm[4] = \
            """
        ____
        |  |
        |  O
        | /|\\
        |
        |
        |
        |
        -------"""

        hm[5] = \
            """
        ____
        |  |
        |  O
        | /|\\
        |  |
        |
        |
        |
        -------"""

        hm[6] = \
            """
        ____
        |  |
        |  O
        | /|\\
        |  |
        | /
        |
        |
        -------"""

        hm[7] = \
            """
        ____
        |  |
        |  O
        | /|\\
        |  |
        | / \\
        |
        |
        -------"""
        return hm


if __name__ == '__main__':
    game = Game()
    game()
