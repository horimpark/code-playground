def solve(s):
    spaces = [i for i, w in enumerate(s) if w == " "]
    full_s = [x for x in s if x != " "]
    for i in range(int(len(full_s) / 2)):
        a, b = full_s[i], full_s[len(full_s) - 1 - i]
        full_s[i] = b
        full_s[len(full_s) - 1 - i] = a
    for x in spaces:
        full_s.insert(x, " ")
    return "".join(full_s)
