def sum_strings(x, y):
    print(x, y)
    if x == "" and y != "":
        return y
    elif y == "" and x != "":
        return x
    elif x == "" and y == "":
        return "0"
    else:
        return str(int(x) + int(y))
