def avg_array(arrs):
    res = list()
    for i in range(len(arrs[0])):
        res.append(
            sum([arrs[x][i] for x in range(len(arrs))]) / len(arrs)
        )
    return res