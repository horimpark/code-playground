def group_by_commas(n):
    res = []
    n = str(n)
    length = len(str(n))
    while length != 0:
        res.append(n[-3:])
        n = n[:-3]
        length -= 3
        if length < 3:
            res.append(n[:length])
            length -= length
    res = [x for x in res[::-1] if x]
    return ",".join(res)
