import pytest
from pytest_tennis import Tennis


class TestTennisGame(object):
    def setup_class(self):
        self.tennis = Tennis()


    def test_love_fifteen(self):
        self.given_second_player_score_times(1)
        assert self.tennis.score() == "love fifteen"

    def test_thirty_love(self):
        self.given_first_player_score_times(2)
        assert self.tennis.score() == "thirty love"

    def test_fifteen_love(self):
        self.given_first_player_score_times(1)
        assert self.tennis.score() == "fifteen love"

    def test_love_all(self):
        assert self.tennis.score() == "love all"

    def given_first_player_score_times(self, times):
        for i in range(times):
            self.tennis.given_first_player_score()

    def given_second_player_score_times(self, times):
        for i in range(times):
            self.tennis.given_second_player_score()

