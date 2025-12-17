def get_range(length):
    odd = [x for x in range(length) if x % 2 == 0 or x == 0]
    even = [x for x in range(length) if x % 2 != 0]
    return even + odd


def decrypt(encrypted_text, n):
    if not encrypted_text or n < 0:
        return encrypted_text
    t_range = get_range(len(encrypted_text))

    count = n
    while count > 0:
        tmp = dict()
        for t, i in zip(encrypted_text, t_range):
            tmp[i] = t
        encrypted_text = "".join(list(dict(sorted(tmp.items())).values()))
        count -= 1
    return encrypted_text


def encrypt(text, n):
    if not text or n < 0:
        return text
    t_range = get_range(len(text))
    print(t_range)
    count = n
    while count > 0:
        new_text = "".join([text[x] for x in t_range])
        text = new_text
        count -= 1
    return text
