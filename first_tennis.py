class Tennis():
    def __init__(self):
        self.first_player_score = 0

    def lookup_score(self):
        lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.first_player_score == 1:
            return f"{self.lookup_score()[self.first_player_score]} love"
        return "love all"

    def first_player_score(self, times):
        self.given_first_player_score_times(times)

    def given_first_player_score_times(self, times):
        for i in range(times):
            self.first_player_score += 1
