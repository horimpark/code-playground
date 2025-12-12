class HighScoreTable:

    def __init__(self, score_range):
        self.score_range = score_range
        self.total_score = []
        self.scores = []

    def update(self, x):
        self.total_score.append(x)
        self.scores = sorted(self.total_score, reverse=True)[: self.score_range]

    def reset(self):
        self.total_score = []
        self.scores = []
