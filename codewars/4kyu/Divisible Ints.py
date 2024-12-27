def get_count(n):
    print(n)
    str_n = str(n)
    candidates = []
    for x in range(len(str_n)):
        for y in range(len(str_n) + 1):
            if str_n[x:y]:
                candidates.append(int(str_n[x:y]))
    candidates = [x for x in candidates if x != n and x != 0]
    res = [x for x in candidates if n % x == 0]
    return len(res)
