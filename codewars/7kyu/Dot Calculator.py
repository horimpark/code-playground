def calculator(txt):
    split_txt = txt.split(' ')
    x, y = len(split_txt[0]), len(split_txt[2])
    op = split_txt[1]
    res = 0
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "//":
        res = x // y
    print('.'*res)
    return '.'*res
