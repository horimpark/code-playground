def matrixfy(st):
    if not st:
        return "name must be at least one letter"
    target = 0
    while target**2 <= len(st):
        if target**2 >= len(st):
            break
        else:
            target += 1
    print(st, target)
    res = []
    for x in range(target):
        part = st[x*target:(x*target)+target]
        if len(part) != target:
            part += '.'*(target-len(part))
        res.append([p for p in part])
    return res
