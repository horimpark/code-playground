def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for x in message:
        if x.isalpha():
            if x.isupper():
                alphabet = alphabet.upper()
            else:
                alphabet = alphabet.lower()
            idx = alphabet.index(x)
            next_idx = idx + 13
            if next_idx >= len(alphabet) - 1:
                result += alphabet[next_idx - len(alphabet)]
            else:
                result += alphabet[next_idx]
        else:
            result += x
    return result
