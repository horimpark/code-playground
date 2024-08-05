def dbl_linear(n):
    res = [1]
    for x in res:
        res.append(2 * x + 1)
        res.append(3 * x + 1)
        if len(res) > n * 9:  # 야매..ㅋ
            break

    return sorted(set(res))[n]

