def delete_digit(n):
    n = [x for x in str(n)]
    candidates = []
    for x in range(len(n)):
        cand = n.copy()
        cand.remove(n[x])
        candidates.append(cand)
    candidates = [int(''.join(x)) for x in candidates]
    return max(candidates)