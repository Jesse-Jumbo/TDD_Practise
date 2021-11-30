import unittest

from second_tennis import Tennis


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tennis = Tennis()

    def test_fifteen_love(self):
        self.given_first_player_score()
        self.score_should_be("fifteen love")

    def test_love_all(self):
        self.score_should_be("love all")

    def score_should_be(self, expected):
        self.assertEqual(self.tennis.score(), expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
