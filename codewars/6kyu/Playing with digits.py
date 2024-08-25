def dig_pow(n, p):
    new_n = sum([int(x) ** y for x, y in zip(str(n), range(p, len(str(n)) + p))])
    if new_n % n == 0:
        return new_n // n
    return -1
