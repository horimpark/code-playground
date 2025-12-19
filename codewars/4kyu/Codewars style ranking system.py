class User:
    RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    RANK_TO_IDX = {r: i for i, r in enumerate(RANKS)}

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank: int):
        if activity_rank not in self.RANK_TO_IDX:
            raise ValueError("Out of range rank")
        if self.rank == 8:
            return  # max rank: no more progress

        cur_i = self.RANK_TO_IDX[self.rank]
        act_i = self.RANK_TO_IDX[activity_rank]
        d = act_i - cur_i

        if d == 0:
            self.progress += 3
        elif d == -1:
            self.progress += 1
        elif d > 0:
            self.progress += 10 * d * d
        # d <= -2: +0

        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            cur_i += 1
            self.rank = self.RANKS[cur_i]

        if self.rank == 8:
            self.progress = 0
