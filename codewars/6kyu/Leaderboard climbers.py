def leaderboard_sort(leaderboard, changes):
    for x in changes:
        name, rank = x.split(" ")[0], int(x.split(" ")[1])
        og_rank = leaderboard.index(name)
        leaderboard.remove(name)
        new_rank = og_rank - rank
        leaderboard.insert(new_rank, name)
    return leaderboard
