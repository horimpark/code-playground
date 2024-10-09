def parse(data):
    start = 0
    res = []
    for c in data:
        if c == "i":
            start += 1
        elif c == "d":
            start -= 1
        elif c == "s":
            start *= start
        elif c == "o":
            res.append(start)
    return res
