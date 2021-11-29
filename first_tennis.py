class Tennis():
    def __init__(self, first_player_name, second_player_name):
        self.second_player_score_times = 0
        self.first_player_score_times = 0
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.score_lookup = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def score(self):
        if self.is_score_different():
            return self.adv_state() if self.is_ready_for_game_point() else self.lookup_score()
        return "deuce" if self.is_deuse() else self.all_score()

    def is_deuse(self):
        is_deuse = self.first_player_score_times >= 3
        return is_deuse

    def is_ready_for_game_point(self):
        is_ready = self.first_player_score_times > 3 or self.second_player_score_times > 3
        return is_ready

    def is_score_different(self):
        diff = self.first_player_score_times != self.second_player_score_times
        return diff

    def lookup_score(self):
        return f"{self.score_lookup[self.first_player_score_times]} {self.score_lookup[self.second_player_score_times]}"

    def adv_score(self):
        return f"{self.adv_player()} Advantage"

    def adv_state(self):
        if self.is_adv():
            return self.adv_score()
        return self.win_score()

    def win_score(self):
        return f"{self.adv_player()} Win"

    def adv_player(self):
        adv_player = self.first_player_name if self.first_player_score_times > self.second_player_score_times else self.second_player_name
        return adv_player

    def is_adv(self):
        is_adv = abs(self.first_player_score_times - self.second_player_score_times) == 1
        return is_adv

    def all_score(self):
        return f"{(self.score_lookup[self.first_player_score_times])} all"

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1


