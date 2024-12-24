def solution(args):
    res = []
    for x in args:
        if not res:
            res.append([x])
        else:
            if x - 1 == res[-1][-1]:
                res[-1].append(x)
            else:
                res.append([x])
    tmp = []
    for x in res:
        if len(x) > 2:
            tmp.append(f"{x[0]}-{x[-1]}")
        elif len(x) == 2:
            tmp.append(f"{x[0]}")
            tmp.append(f"{x[1]}")
        else:
            tmp.append(f"{x[0]}")
    return ",".join(tmp)
