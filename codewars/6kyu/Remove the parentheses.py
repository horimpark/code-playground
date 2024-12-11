def remove_parentheses(st):
    res = []
    check = 0
    for x in st:
        if x == "(":
            check += 1
        elif x == ")":
            check -= 1
            continue
        else:
            if check == 0:
                res.append(x)
    return "".join(res)
