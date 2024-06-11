def remov_nb(n):
    total_sum = n * (n + 1) // 2

    result = []

    for a in range(1, n):
        b = (total_sum - a) / (a + 1)

        if b.is_integer() and b > a and b <= n:
            result.append((a, int(b)))
            result.append((int(b), a))

    result.sort()

    return result