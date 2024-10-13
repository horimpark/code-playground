def move_ten(st):
    alpha1 = {i: a for i, a in enumerate("abcdefghijklmnopqrstuvwxyz")}
    alpha2 = {a: i for i, a in enumerate("abcdefghijklmnopqrstuvwxyz")}
    print(alpha1)

    res = ""
    for x in st:
        idx = alpha2[x] + 10
        if idx > 25:
            res += alpha1[idx - 25 - 1]
        else:
            res += alpha1[idx]
    return res
