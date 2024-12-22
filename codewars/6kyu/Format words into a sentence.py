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
