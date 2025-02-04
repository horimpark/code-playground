def lowest_temp(t):
    if not t:
        return None
    t = t.split(" ")

    t = [int(x) for x in t]
    return min(t)
