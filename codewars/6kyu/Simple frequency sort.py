from collections import Counter


def solve(arr):
    counter = Counter(arr)
    cnt = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    result = []
    for x, y in cnt:
        for a in range(y):
            result.append(x)
    return result
