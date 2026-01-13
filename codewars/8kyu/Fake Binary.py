def fake_bin(x):
    res = ["0" if int(i) < 5 else "1" for i in x]
    return "".join(res)
