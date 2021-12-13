class Tennis:
    def __init__(self, first_player_name, second_player_name):
        self.second_player_name = second_player_name
        self.first_player_name = first_player_name
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }
        self.first_player_score_times = 0
        self.second_player_score_times = 0

    def score(self):
        if self.is_end():
            if self.is_adv():
                return self.who_adv()
            else:
                return self.who_win()
        if self.is_not_end():
            if self.is_same():
                return self.which_all()
            else:
                return self.who_love()
        else:
            return "deuce"

    def who_win(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} Win"
        else:
            return f"{self.second_player_name} Win"

    def is_end(self):
        return self.first_player_score_times > 3 or self.second_player_score_times > 3

    def who_adv(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} Adv"
        else:
            return f"{self.second_player_name} Adv"

    def is_adv(self):
        return abs(self.first_player_score_times - self.second_player_score_times) == 1

    def who_love(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.lookup_score[self.first_player_score_times]} love"
        else:
            return f"love {self.lookup_score[self.second_player_score_times]}"

    def which_all(self):
        return f"{self.lookup_score[self.first_player_score_times]} all"

    def is_same(self):
        return self.first_player_score_times == self.second_player_score_times

    def is_not_end(self):
        return self.first_player_score_times < 3

    def given_first_player_score(self):
        self.first_player_score_times += 1

    def given_second_player_score(self):
        self.second_player_score_times += 1