encode_dict = {x: str(i + 1) for i, x in enumerate("aeiou")}
decode_dict = {str(i + 1): x for i, x in enumerate("aeiou")}


def encode(st):
    res = [encode_dict[x] if x in encode_dict else x for x in st]
    return "".join(res)


def decode(st):
    res = [decode_dict[x] if x in decode_dict else x for x in st]
    return "".join(res)
