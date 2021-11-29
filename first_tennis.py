class Tennis():
    def __init__(self, first_palyer_name, second_palyer_name):
        self.second_player_score_times = 0
        self.first_player_score_times = 0
        self.first_player_name = first_palyer_name
        self.second_player_name = second_palyer_name
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
            if self.first_player_score_times >= 3:
                return "deuce"
            else:
                return self.all_score()
        if self.first_player_score_times == 3 or self.second_player_score_times == 3:
            if self.first_player_score_times > self.second_player_score_times:
                return "Tom Advantage"
            else:
                return "Joey Advantage"
        return "love all"

    def all_score(self):
        return f"{(self.score_lookup[self.first_player_score_times])} all"

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1


