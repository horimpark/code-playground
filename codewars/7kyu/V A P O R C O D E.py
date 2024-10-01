def vaporcode(s):
    s = [x.upper() for x in s if x != " "]
    return "  ".join(s)
