import random as rd


class AI:
    PLAYABLE = ["p", "f", "c"]
    WIN_CASES = [["p", "f"], ["f", "c"], ["c", "p"]]

    def __init__(self, genes):
        self.genes = genes

        self.last_player_action = "c"

        self.acting_genes = self.genes[0]
        self.cum_acting_genes = [sum(self.acting_genes[:i + 1]) for i in range(len(self.acting_genes))]

        self.random_play_genes = self.genes[1]
        self.cum_random_play_genes = [sum(self.random_play_genes[:i + 1]) for i in range(len(self.random_play_genes))]

        self.strategies = [self.imitate, self.lose, self.win, self.random]

    def act(self):
        self.action = rd.choices(self.strategies, cum_weights=self.cum_acting_genes, k=1)[0]
        return self.action()

    def imitate(self):
        return self.last_player_action

    def lose(self):
        for case in AI.WIN_CASES:
            if self.last_player_action == case[1]:
                return case[0]

    def win(self):
        for case in AI.WIN_CASES:
            if self.last_player_action == case[0]:
                return case[1]

    def random(self):
        return rd.choices(AI.PLAYABLE, cum_weights=self.cum_random_play_genes, k=1)[0]
