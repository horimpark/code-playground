def scale(strng, k, v):
    if not strng:
        return ""
    split_s = strng.split("\n")
    res = []
    for x in split_s:
        tmp = ""
        for a in x:
            tmp += a * k
        for d in range(v):
            res.append(tmp)
    return "\n".join(res)
