def to_weird_case(words):
    split_words = words.split(" ")
    res = []
    for x in split_words:
        tmp = ""
        for i, w in enumerate(x):
            if i % 2 == 0:
                tmp += w.upper()
            else:
                tmp += w.lower()
        res.append(tmp)
    return " ".join(res)
