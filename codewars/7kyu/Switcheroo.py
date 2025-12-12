def switcheroo(s):
    res = ""
    for x in s:
        if x == "a":
            res += "b"
        elif x == "b":
            res += "a"
        else:
            res += x
    return res
