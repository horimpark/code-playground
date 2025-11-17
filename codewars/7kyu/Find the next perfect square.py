def find_next_square(sq):
    res = sq ** (1 / 2)
    if int(res) != res:
        return -1
    return (res + 1) ** 2
