def find_in_array(seq, predicate):
    for i, x in enumerate(seq):
        res = predicate(x, i)
        if res:
            return i
    return -1
