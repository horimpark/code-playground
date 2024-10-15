def accum(st):
    return "-".join([str(st[i] * (i + 1)).capitalize() for i in range(len(st))])
