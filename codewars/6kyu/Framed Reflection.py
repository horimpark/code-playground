def mirror(text):
    split_t = text.split(" ")

    res = []
    max_len = max([len(x) for x in split_t])
    for i in range(len(split_t)):
        space = " " * (max_len - len(split_t[i]))
        res.append(f"* {''.join([x for x in reversed(split_t[i])])}{space} *")
    res.insert(0, "*" * (max_len + 4))
    res.append("*" * (max_len + 4))
    return "\n".join(res)
