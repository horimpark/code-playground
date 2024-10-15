def solve(s):
    upp, low, num, spc = 0, 0, 0, 0
    for x in s:
        if x.isupper():
            upp += 1

        if x.islower():
            low += 1

        if x.isdigit():
            num += 1

        if not x.isdigit() and not x.isalpha():
            spc += 1
    return [upp, low, num, spc]
