def encrypt_this(text):
    res = []
    for x in text.split(" "):
        if len(x) >= 3:
            res.append(f"{ord(x[0])}{x[-1]}{x[2:-1]}{x[1]}")
        elif len(x) == 2:
            res.append(f"{ord(x[0])}{x[1]}")
        elif len(x) == 1:
            res.append(f"{ord(x[0])}")
        else:
            continue
    return " ".join(res)
