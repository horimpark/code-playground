def solve(s):
    total = len(s)
    upper = len([x for x in s if x.isupper()])

    return s.lower() if upper <= (total / 2) else s.upper()
