from collections import Counter


def scramble(s1, s2):
    s1 = Counter(s1)
    for x in s2:
        if x in s1:
            if s1[x] >= 1:
                s1[x] -= 1
            else:
                return False
        else:
            return False
    return True
