class Tennis:
    def __init__(self, first_player_name, second_player_name):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player_score = 0
        self.second_player_score = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.not_end():
            if self.is_same():
                return self.which_all()
            else:
                return self.who_love()
        if self.is_finally():
            if self.is_adv():
                return self.who_adv()
            if self.is_win():
                return self.who_win()
        return "deuce"

    def who_love(self):
        if self.first_player_score == 0:
            return f"love {self.lookup_score[self.second_player_score]}"
        if self.second_player_score == 0:
            return f"{self.lookup_score[self.first_player_score]} love"

    def not_end(self):
        not_end = self.first_player_score < 3
        return not_end

    def which_all(self):
        which_all = f"{self.lookup_score[self.first_player_score]} all"
        return which_all

    def is_same(self):
        is_same = self.first_player_score == self.second_player_score
        return is_same

    def who_win(self):
        if self.first_player_score > self.second_player_score:
            return f"{self.first_player_name} Win"
        else:
            return f"{self.second_player_name} Win"

    def who_adv(self):
        if self.second_player_score < self.first_player_score:
            return f"{self.first_player_name} Adv"
        else:
            return f"{self.second_player_name} Adv"

    def is_win(self):
        is_win = abs(self.first_player_score - self.second_player_score) > 1
        return is_win

    def is_finally(self):
        is_finally = self.first_player_score >= 3
        return is_finally

    def is_adv(self):
        is_adv = abs(self.first_player_score - self.second_player_score) == 1
        return is_adv

    def given_first_player_score(self):
        self.first_player_score += 1

    def given_second_player_score(self):
        self.second_player_score += 1
