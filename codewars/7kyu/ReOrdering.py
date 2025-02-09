def re_ordering(text):
    split_x = text.split(" ")

    res = []
    for x in split_x:
        if x[0].isupper():
            res.insert(0, x)
        else:
            res.append(x)
    return " ".join(res)
