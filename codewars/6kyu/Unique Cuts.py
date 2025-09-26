def split_string(st):
    if not st:
        return []

    last = {ch: i for i, ch in enumerate(st)}
    res = []
    start, end = 0, 0
    for i, ch in enumerate(st):
        end = max(end, last[ch])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res