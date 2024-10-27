def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    res = []
    for x in range(a, b + 1):
        if x == sum([int(y) ** (i + 1) for i, y in enumerate(str(x))]):
            res.append(x)
    print(res)
    return res
