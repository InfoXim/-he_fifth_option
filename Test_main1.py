import unittest

from main import max_digit


class MyTestCase(unittest.TestCase):
    def test_max_gigit(self):
        self.assertEqual(max_digit(5648), 8)  # add assertion here


if __name__ == '__main__':
    unittest.main()
