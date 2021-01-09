from hello import hello_name

"""
The code required to test our minmimal hello.py using pytest
"""


def test_hello_name():
    assert hello_name('widget') == 'hello widget'
