from unittest.mock import patch

"""
test with:
    pytest test_patch.py

test coverage with:
    pytest --cov-report term-missing --cov='.'
    (requires pytest-cov package installed)
"""


def get_input():
    data = input('Please enter some stuff: ')
    return data


# Using mock to automate some test data through input
@patch("builtins.input", side_effect=['12', 13, 'Craig'])
def test_get_data(inp):
    # note to self, the parameter here can be called anything
    assert get_input() == '12'
    assert get_input() == 13
    assert get_input() == 'Craig'


def I_dont_get_called():
    pass
