def longest_consec(strarr, k):
    if not strarr or k <= 0 or len(strarr) < k:
        return ""
    res = []
    for x in range(0, len(strarr) - k + 1):
        res.append("".join(strarr[x : x + k]))
    length = [len(x) for x in res]
    max_idx = length.index(max(length))
    return res[max_idx]


def longest_consec(strarr, k):
    if not strarr or k <= 0 or k > len(strarr):
        return ""

    candidates = []
    for i in range(len(strarr) - k + 1):
        combined_str = "".join(strarr[i:i + k])
        candidates.append((combined_str, len(combined_str)))

    sorted_candidates = sorted(candidates, key=lambda x: (-x[1], x[0]))

    return sorted_candidates[0][0] if sorted_candidates else ""


def longest_consec(strarr, k):
    if not strarr or k <= 0 or k > len(strarr):
        return ""

    candidates = ["".join(strarr[i:i+k]) for i in range(len(strarr) - k + 1)]

    return max(candidates, key=len, default="")
