def sum_pairs(ints, s):
    cand = set()
    for i in ints:
        if s - i in cand:
            return [s - i, i]
        cand.add(i)
