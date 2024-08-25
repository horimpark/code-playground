def dig_pow(n, p):
    new_n = sum([int(x) ** y for x, y in zip(str(n), range(p, len(str(n)) + p))])
    if new_n % n == 0:
        return new_n // n
    return -1

def dig_pow(n, p): #hh.hwang
    s = str(n)
    total = sum(int(digit) ** (p + i) for i, digit in enumerate(s))
    if total % n == 0:
        return total // n
    else:
        return -1


if __name__ == "__main__":
    print(dig_pow(89, 1))  # 1
    print(dig_pow(92, 1))  # -1