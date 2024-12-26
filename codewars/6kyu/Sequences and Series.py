def get_score(n):
    res = 50
    start = 100
    for x in range(n - 1):
        res += start
        start += 50
    return res


# def get_score(n):
#     return n * (n + 1) * 25
