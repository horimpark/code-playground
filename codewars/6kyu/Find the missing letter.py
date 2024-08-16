def find_missing_letter(chars):
    all_c = "abcdefghijklmnopqrstuvwxyz"
    if chars[0].isupper():
        all_c = all_c.upper()
    for x, y in zip(range(all_c.index(chars[0]), all_c.index(chars[-1])), chars):
        if all_c[x] != y:
            return all_c[x]
