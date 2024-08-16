def decode(code, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    n_key = (
        str(key) * (len(code) // len(str(key)))
        + str(key)[: (len(code) % len(str(key)))]
    )
    print(n_key)
    res = ""
    for c, k in zip(code, n_key):
        res += alpha[c - 1 - int(k)]
    return res
