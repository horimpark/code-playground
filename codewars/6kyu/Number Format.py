def number_format(n):
    res = []
    is_minus = False
    if n < 0:
        n = -n
        is_minus = True

    for i, x in enumerate(str(n)[::-1]):
        if (i + 1) % 3 == 0 and i != len(str(n)) - 1:
            res.insert(0, x)
            res.insert(0, ",")
        else:
            res.insert(0, x)
    return f"-{''.join(res)}" if is_minus else "".join(res)


""" ha..hahhhaha
def number_format(n):
    return f'{n:,}'
"""
