from itertools import permutations as pp


def permutations(s):
    if len(s) == 1:
        return [s]
    s = [x for x in s]
    perm = pp(s, len(s))
    res = [x for x in perm]
    return list(set("".join(x) for x in res))
