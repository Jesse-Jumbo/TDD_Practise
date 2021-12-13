class Tennis:
    def __init__(self, first_player_name, second_plyer_name):
        self.second_player_name = second_plyer_name
        self.first_player_name = first_player_name
        self.first_player_score_times = 0
        self.second_player_score_times = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.is_not_end():
            if self.is_same():
                return self.which_love()
            else:
                return self.who_love()
        if self.is_end():
            if self.is_adv():
                return self.who_adv()
            if self.is_win():
                return self.who_win()
        return "deuce"

    def who_win(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} Win"
        else:
            return f"{self.second_player_name} Win"

    def is_win(self):
        return abs(self.first_player_score_times - self.second_player_score_times) > 1

    def is_end(self):
        return self.first_player_score_times >= 3

    def who_adv(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} adv"
        else:
            return f"{self.second_player_name} adv"

    def is_adv(self):
        return abs(self.first_player_score_times - self.second_player_score_times) == 1

    def who_love(self):
        if self.first_player_score_times != 0:
            return f"{self.lookup_score[self.first_player_score_times]} love"
        if self.second_player_score_times != 0:
            return f"love {self.lookup_score[self.second_player_score_times]}"

    def which_love(self):
        return f"{self.lookup_score[self.first_player_score_times]} all"

    def is_same(self):
        return self.first_player_score_times == self.second_player_score_times

    def is_not_end(self):
        return self.first_player_score_times < 3

    def given_first_player_score(self):
        self.first_player_score_times += 1

    def given_second_player_score(self):
        self.second_player_score_times += 1
