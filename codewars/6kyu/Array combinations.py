def solve(arr):
    res = [len(set(x)) for x in arr]
    total = 1
    for x in res:
        total *= x
    return total
