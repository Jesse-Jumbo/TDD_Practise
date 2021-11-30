class Tennis:
    def __init__(self):
        self.first_player_score = 0
        self.second_player_score = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.second_player_score != 0 or self.first_player_score != 0:
            if self.second_player_score < 3 and self.first_player_score == 0:
                return f"love {self.lookup_score[self.second_player_score]}"
            if self.first_player_score < 3 and self.second_player_score == 0:
                return f"{self.lookup_score[self.first_player_score]} love"
            if self.second_player_score >= 3:
                return "deuce"
        return "love all"

    def given_first_player_score(self):
        self.first_player_score += 1

    def given_second_player_score(self):
        self.second_player_score += 1
