from collections import defaultdict


def merge(*dicts):
    res = defaultdict(list)
    for x in dicts:
        if x:
            for k, v in x.items():
                res[k].append(v)
    return res
