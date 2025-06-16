def play_pass(s, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for i, x in enumerate(s):
        if x.lower() in alphabet:
            x = x.lower()
            shift = alphabet.index(x) + n - len(alphabet) if len(alphabet) <= alphabet.index(x) + n else alphabet.index(x) + n
            res.append(alphabet[shift] if (i+1) % 2 == 0 else alphabet[shift].upper())
        elif x.isdigit():
            res.append(str(9 - int(x)))
        else:
            res.append(x)
    res.reverse()
    return ''.join(res)