import unittest

from second_tennis import Tennis


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.tennis = Tennis()
        self.assertEqual(self.tennis.score(), "love all")  # add assertion here


if __name__ == '__main__':
    unittest.main()
