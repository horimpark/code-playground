def data_reverse(data):
    split = [data[x : x + 8] for x in range(0, len(data), 8)]

    res = []
    for x in range(len(split) - 1, -1, -1):
        res.extend(split[x])
    return res
