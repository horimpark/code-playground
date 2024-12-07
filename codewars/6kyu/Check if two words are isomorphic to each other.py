from collections import Counter


def isomorph(a, b):
    a_count = Counter([i for i in a])
    b_count = Counter([i for i in b])

    if len(a_count) == len(b_count) and sum(a_count.values()) == sum(b_count.values()) and set(a_count.keys()) != set(
            b_count.keys()):
        return True
    return False


