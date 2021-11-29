class Tennis():
    def __init__(self):
        self.second_player_score_times = 0
        self.first_player_score_times = 0
        self.score_lookup = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.second_player_score_times == 0 and self.first_player_score_times > 0:
            return f"{self.score_lookup[self.first_player_score_times]} love"
        if self.first_player_score_times == 0 and self.second_player_score_times > 0:
            return f"love {self.score_lookup[self.second_player_score_times]}"
        if self.first_player_score_times == self.second_player_score_times:
            return f"{(self.score_lookup[self.first_player_score_times])} all"
        return "love all"

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1


