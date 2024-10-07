def longest_consec(strarr, k):
    if not strarr or k <= 0 or len(strarr) < k:
        return ""
    res = []
    for x in range(0, len(strarr) - k + 1):
        res.append("".join(strarr[x : x + k]))
    length = [len(x) for x in res]
    max_idx = length.index(max(length))
    return res[max_idx]
