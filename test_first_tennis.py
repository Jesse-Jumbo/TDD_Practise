import unittest

from first_tennis import *


class TennisTest(unittest.TestCase):
    # 若setUp引發異常，測試框架會認為測試發生錯誤，測試方法不會被運行；若成功運行，無論測試是否通過，tearDown()都會運行
    def setUp(self):                            # 設置下面每個測試開始前需要執行的指令(tearDown() -> 測試完成後需要執行的指令)
        self.tennis = Tennis("Tom", "Joey")

    def test_love_all(self):                    # test 開頭，告知test runner那些物件方法為定義的測試
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

    def test_love_fifteen(self):
        self.given_second_player_score_times(1)
        self.score_should_be("love fifteen")

    def test_love_thirty(self):
        self.given_second_player_score_times(2)
        self.score_should_be("love thirty")

    def test_fifteen_all(self):
        self.given_first_player_score_times(1)
        self.given_second_player_score_times(1)
        self.score_should_be("fifteen all")

    def test_thirty_all(self):
        self.given_first_player_score_times(2)
        self.given_second_player_score_times(2)
        self.score_should_be("thirty all")

    def test_deuce(self):
        self.given_deuce()
        self.score_should_be("deuce")

    def test_first_player_advantage(self):
        self.given_deuce()
        self.given_first_player_score_times(1)
        self.score_should_be("Tom Advantage")

    def test_second_player_advantage(self):
        self.given_deuce()
        self.given_second_player_score_times(1)
        self.score_should_be("Joey Advantage")

    def test_tom_win(self):
        self.given_deuce()
        self.given_first_player_score_times(2)
        self.score_should_be("Tom Win")

    def test_joey_win(self):
        self.given_deuce()
        self.given_second_player_score_times(2)
        self.score_should_be("Joey Win")

    def given_deuce(self):
        self.given_first_player_score_times(3)
        self.given_second_player_score_times(3)

    def given_second_player_score_times(self, times):
        for i in range(times):
            self.tennis.second_player_score()

    def given_first_player_score_times(self, times):
        for i in range(times):
            self.tennis.first_player_score()

    def score_should_be(self, expected):
        self.assertEqual(self.tennis.score(), expected)     # 確認是否為期望的結果( assertTrue()、assertFalse() 用於驗證條件式)


if __name__ == '__main__':
    unittest.main()

