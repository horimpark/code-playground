def squared_digits_series(n):
    result_sum = 0
    idx = 0
    count = 0

    while count < n:
        if idx & (idx + 1) == 0:
            s = (idx + 1) * 10 + 1
            repeats = min(idx + 1, n - count)
            result_sum += s * repeats
            count += repeats

        idx += 1

    return result_sum


if __name__ == "__main__":
    print(squared_digits_series(1))  # 11
    print(squared_digits_series(2))
    print(squared_digits_series(3))
    print(squared_digits_series(4))
    print(squared_digits_series(5))