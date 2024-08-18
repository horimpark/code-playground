from collections import Counter


def find_uniq(arr):
    cnt = Counter(arr)
    for k, v in cnt.items():
        if v == 1:
            return k
