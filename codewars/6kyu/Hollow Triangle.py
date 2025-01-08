def hollow_triangle(n):
    str_lth = 2 * n - 1
    res = ["#" * str_lth]

    for x in range(1, n):
        if x != n - 1:
            res.append("_" * x + "#" + "_" * (str_lth - (2 * x + 2)) + "#" + "_" * x)
        else:
            res.append("_" * x + "#" + "_" * x)

    return [res[x] for x in range(len(res) - 1, -1, -1)]
