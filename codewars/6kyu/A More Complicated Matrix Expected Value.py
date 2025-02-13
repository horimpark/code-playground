from fractions import Fraction


def expected_value(c: int, r: int) -> Fraction:
    total = 0
    for start_num in range(r + 1):
        total += sum([n ** 2 for n in range(start_num, start_num + c + 1)])

    low = (c + 1) * (r + 1)

    return Fraction(total, low)


def expected_value(c: int, r: int) -> Fraction:
    total = 0

    for s in range(r + 1):
        for i in range(c + 1):
            total += (s + i) ** 2

    low = (c + 1) * (r + 1)
    return Fraction(total, low)