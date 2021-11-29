import unittest

from first_tennis import *


class TennisTest(unittest.TestCase):
    def setUp(self):
        self.tennis = Tennis()

    def test_love_all(self):
        self.score_should_be("love all")

    def test_fifteen_love(self):
        self.given_first_player_score_times(1)
        self.score_should_be("fifteen love")

    def test_thirty_love(self):
        self.given_first_player_score_times(2)
        self.score_should_be("thirty love")

    def test_forty_love(self):
        self.given_first_player_score_times(3)
        self.score_should_be("forty love")

    def given_first_player_score_times(self, times):
        for i in range(times):
            self.tennis.first_player_score()

    def score_should_be(self, expected):
        self.assertEqual(self.tennis.score(), expected)



