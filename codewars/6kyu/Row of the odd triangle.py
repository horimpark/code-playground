def odd_num(x):
    return (2 * x) + 1


def odd_row(n):
    row = sum([x for x in range(n)])
    res = []
    for x in range(row, row + n):
        res.append(odd_num(x))

    return res
