def diamond(n):
    if n < 1 or n % 2 == 0:
        return None

    diamond = ""
    for i in range(1, n + 1, 2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"

    for i in range(n - 2, 0, -2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"

    return diamond


if __name__ == "__main__":
    print(diamond(1))
    print(diamond(3))
    print(diamond(4))