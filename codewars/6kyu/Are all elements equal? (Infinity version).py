def eq_all(iterable):
    res = []
    for x in iterable:
        if res and res[-1] != x:
            return False
        res.append(x)

    return True
