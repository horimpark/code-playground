import math


def string_color(name):
    if len(name) < 2:
        return None
    h_code = [ord(x) for x in name]
    a = hex(sum(h_code))
    b = hex(math.prod(h_code))
    c = hex(abs(h_code[0] - sum(h_code[1:])))
    print(a, b, c)
    return f"{a[-2:].upper()}{b[-2:].upper()}{c[-2:].upper()}"
