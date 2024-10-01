def narcissistic(value):
    value = str(value)
    point = len(value)
    res = 0
    for x in value:
        res += int(x) ** point
    if int(value) == res:
        return True
    else:
        return False
