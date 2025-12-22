def series_sum(n):
    res = []
    for x in range(n):
        if x == 0:
            res.append(1)
        else:
            res.append(1 / (3 * x + 1))
    return f"{sum(res):.2f}"
