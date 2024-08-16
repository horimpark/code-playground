def digital_root(n):
    while n >= 10:
        str_n = str(n)
        next_integer = 0
        for x in str_n:
            next_integer += int(x)
        n = next_integer
    return n
