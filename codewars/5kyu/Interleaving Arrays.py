def interleave(*args):
    res = [x[0] for x in zip(args)]
    max_length = max([len(x) for x in res])

    result = []
    for x in range(max_length):
        for y in range(len(res)):
            if len(res[y]) - 1 >= x:
                result.append(res[y][x])
            else:
                result.append(None)
    return result
