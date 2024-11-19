def string_transformer(s):
    split_s = s.split(" ")
    res = []
    for i in range(len(split_s) - 1, -1, -1):
        tmp = ""
        for x in split_s[i]:
            if x.isupper():
                tmp += x.lower()
            else:
                tmp += x.upper()
        res.append(tmp)
    return " ".join(res)


# %%
# def string_transformer(s):
#     return ' ' .join(s.split(' ')[::-1]).swapcase()
