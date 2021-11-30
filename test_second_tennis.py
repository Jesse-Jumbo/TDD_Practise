import unittest

from second_tennis import Tennis


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tennis = Tennis("Diana", "Diana2")

    def test_second_player_win(self):
        self.given_second_player_score_times(2)
        self.given_deuce()
        self.score_should_be("Diana2 Win")

    def test_first_player_win(self):
        self.given_first_player_score_times(2)
        self.given_deuce()
        self.score_should_be("Diana Win")

    def test_second_player_adv(self):
        self.given_second_player_score_times(1)
        self.given_deuce()
        self.score_should_be("Diana2 Adv")

    def test_first_player_adv(self):
        self.given_first_player_score_times(1)
        self.given_deuce()
        self.score_should_be("Diana Adv")

    def test_deuce(self):
        self.given_deuce()
        self.score_should_be("deuce")

    def test_love_thirty(self):
        self.given_second_player_score_times(2)
        self.score_should_be("love thirty")

    def test_love_fifteen(self):
        self.given_second_player_score_times(1)
        self.score_should_be("love fifteen")

    def test_thirty_love(self):
        self.given_first_player_score_times(2)
        self.score_should_be("thirty love")

    def test_fifteen_love(self):
        self.given_first_player_score_times(1)
        self.score_should_be("fifteen love")

    def test_forty_all(self):
        self.given_first_player_score_times(2)
        self.given_second_player_score_times(3)
        self.score_should_be("forty all")

    def test_thirty_all(self):
        self.given_first_player_score_times(2)
        self.given_second_player_score_times(2)
        self.score_should_be("thirty all")

    def test_fifteen_all(self):
        self.given_first_player_score_times(1)
        self.given_second_player_score_times(1)
        self.score_should_be("fifteen all")

    def test_love_all(self):
        self.score_should_be("love all")

    def given_deuce(self):
        self.given_first_player_score_times(3)
        self.given_second_player_score_times(3)

    def given_second_player_score_times(self, times):
        for i in range(times):
            self.tennis.given_second_player_score()

    def given_first_player_score_times(self, times):
        for i in range(times):
            self.tennis.given_first_player_score()

    def score_should_be(self, expected):
        self.assertEqual(self.tennis.score(), expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
