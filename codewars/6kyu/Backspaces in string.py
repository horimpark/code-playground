def clean_string(s):
    res = ""
    for x in s:
        if x == "#":
            if res:
                res = res[:-1]
        else:
            res += x
    return res
