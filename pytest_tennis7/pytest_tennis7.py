class Tennis:
    def __init__(self, first_player_name, scond_player_name):
        self.second_player_name = scond_player_name
        self.first_player_name = first_player_name
        self.second_player_score = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty"
        }
        self.first_player_score = 0

    def score(self):
        if self.is_not_end():
            if self.is_same():
                return self.which_all()
            else:
                return self.who_love()
        else:
            if self.is_adv():
                return self.who_adv()
            elif self.is_same():
                return "deuce"
            else:
                return self.who_win()

    def who_win(self):
        if self.first_player_score > self.second_player_score:
            return f"{self.first_player_name} Win"
        else:
            return f"{self.second_player_name} Win"

    def who_adv(self):
        if self.first_player_score > self.second_player_score:
            return f"{self.first_player_name} Adv"
        else:
            return f"{self.second_player_name} Adv"

    def is_adv(self):
        return abs(self.first_player_score - self.second_player_score) == 1

    def who_love(self):
        if self.first_player_score != 0:
            return f"{self.lookup_score[self.first_player_score]} love"
        if self.second_player_score != 0:
            return f"love {self.lookup_score[self.second_player_score]}"

    def which_all(self):
        return f"{self.lookup_score[self.first_player_score]} all"

    def is_same(self):
        return self.first_player_score == self.second_player_score

    def is_not_end(self):
        return self.first_player_score < 3

    def first_player_score_times(self):
        self.first_player_score += 1

    def second_player_score_times(self):
        self.second_player_score += 1


