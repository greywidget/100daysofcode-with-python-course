import unittest

"""
The code required to test our minmimal hello.py using the standard unittest
"""
from hello import hello_name


class TestHello(unittest.TestCase):

    def test_hello_name(self):
        self.assertEqual(hello_name('widget'), 'hello widget')


if __name__ == '__main__':
    unittest.main()
