def find_nb(m):
    n = 0
    res = 0
    while total < m:
        n += 1
        res += n ** 3
    return n if res == m else -1
