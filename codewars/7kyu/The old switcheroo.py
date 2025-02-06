def vowel_2_index(string):
    res = ""
    for i, x in enumerate(string):
        if x.lower() in ("a", "e", "i", "o", "u"):
            res += f"{i+1}"
        else:
            res += x
    return res
