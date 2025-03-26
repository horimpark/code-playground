def format_words(words):
    if not words:
        return ""
    words = [x for x in words if x]
    if not words:
        return ""

    res = ""
    for i, x in enumerate(words):
        if not res:
            res += x
        else:
            if i == len(words) - 1:
                res += " and " + x
            else:
                res += ", " + x
    return res


def format_words(words):
    if not words:
        return ""
    words = [w for w in words if w.isalpha()]
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    front = ", ".join(words[:-1])
    return " and ".join([front, words[-1]])