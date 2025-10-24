from collections import Counter


def repeats(arr):
    cnt = Counter(arr)
    res = 0
    for k, v in cnt.items():
        if v == 1:
            res += k
    return res
