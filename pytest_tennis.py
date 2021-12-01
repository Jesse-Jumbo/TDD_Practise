
class Tennis:
    def __init__(self, first_player_name, second_player_name):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.second_player_score_times = 0
        self.first_player_score_times = 0
        self.lookup_score = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.is_not_end():
            if self.is_same():
                return self.which_all()
            else:
                return self.which_love()
        if self.is_finally():
            if self.is_adv():
                return self.who_adv()
            if self.is_win():
                return self.who_win()
            return "deuce"

    def is_not_end(self):
        is_not_end = self.first_player_score_times < 3
        return is_not_end

    def which_all(self):
        which_all = f"{self.lookup_score[self.first_player_score_times]} all"
        return which_all

    def is_same(self):
        is_same = self.first_player_score_times == self.second_player_score_times
        return is_same

    def which_love(self):
        if self.second_player_score_times == 0:
            return f"{self.lookup_score[self.first_player_score_times]} love"
        if self.first_player_score_times == 0:
            return f"love {self.lookup_score[self.second_player_score_times]}"

    def who_win(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} Win"
        else:
            return f"{self.second_player_name} Win"

    def who_adv(self):
        if self.first_player_score_times > self.second_player_score_times:
            return f"{self.first_player_name} Adv"
        else:
            return f"{self.second_player_name} Adv"

    def is_win(self):
        is_win = abs(self.first_player_score_times-self.second_player_score_times) > 1
        return is_win

    def is_adv(self):
        is_adv = abs(self.first_player_score_times-self.second_player_score_times) == 1
        return is_adv

    def is_finally(self):
        is_finally = self.first_player_score_times >= 3
        return is_finally

    def is_different(self):
        is_different = self.first_player_score_times != self.second_player_score_times
        return is_different

    def given_first_player_score(self):
        self.first_player_score_times += 1

    def given_second_player_score(self):
        self.second_player_score_times += 1
