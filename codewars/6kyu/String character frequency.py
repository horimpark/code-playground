from collections import Counter


def solve(s):
    split_s = [x for x in s]
    cnt_s = list(Counter(split_s).values())
    for x in range(len(cnt_s)):
        tmp = [a - 1 if i == x else a for i, a in enumerate(cnt_s)]
        tmp = [x for x in tmp if x != 0]
        if len(set(tmp)) == 1:
            return True

    return False
