from unittest.mock import patch
import random

import pytest

from hangman import choose_random_word, Game


@patch.object(random, 'choice')
def test_choose_random_word(m):
    m.return_value = 'sausages'
    assert choose_random_word() == 'sausages'


@patch("builtins.input", side_effect=['a', 'C', '9', '7', 'z', 'wibble',
                                      'a', 'g', None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 'a'
    assert game.guess() == 'c'
    # not in range a-z
    with pytest.raises(ValueError):
        game.guess()
    # not in range a-z
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 'z'
    # only single letters allowed
    with pytest.raises(ValueError):
        game.guess()
    # already guessed
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 'g'
    # user hit enter
    with pytest.raises(ValueError):
        game.guess()


def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct!', 'It took you 3 guesses']

    output = [line.strip() for line
              in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp


@patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    assert game._win is False
