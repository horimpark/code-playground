def array_diff(a, b):
    same = set(a) & set(b)

    return [x for x in a if x not in same]
