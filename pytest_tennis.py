class Tennis:
    def __init__(self):
        self.first_player_score_times = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.first_player_score_times != 0:
            return f"{self.lookup_score[self.first_player_score_times]} love"
        else:
            return "love all"

    def given_first_player_score(self):
        self.first_player_score_times += 1
