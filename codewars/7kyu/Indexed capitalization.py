def capitalize(s, ind):
    res = ""
    for i, x in enumerate(s):
        if i in ind:
            res += x.upper()
        else:
            res += x
    return res
