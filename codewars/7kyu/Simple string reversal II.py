def solve(st, a, b):
    if len(st) <= b - 1:
        b = len(st) - 1
    return st[:a] + "".join([st[x] for x in range(b, a - 1, -1)]) + st[b + 1 :]
