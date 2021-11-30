class Tennis:
    def __init__(self):
        self.first_player_score_times = 0

    def score(self):
        if self.first_player_score_times != 0:
            return "fifteen love"
        else:
            return "love all"

    def given_first_player_score(self):
        self.first_player_score_times += 1