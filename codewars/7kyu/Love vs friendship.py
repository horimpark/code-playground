def words_to_marks(s):
    scores = {x: i + 1 for i, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    return sum([scores[x] for x in s])
