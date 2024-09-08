def square_digits(num):
    return int(''.join(str(int(d) ** 2) for d in str(num)))


if __name__ == "__main__":
    print(square_digits(9119))  # 811181
    print(square_digits(0))  # 0
    print(square_digits(3212))  # 9414
    print(square_digits(2112))  # 4114
    print(square_digits(1111))  # 1111
    print(square_digits(1234321))  # 14916941