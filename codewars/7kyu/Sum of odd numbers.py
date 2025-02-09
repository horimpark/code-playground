def row_sum_odd_numbers(n):
    start = sum(x for x in range(n))
    return sum([2 * x + 1 for x in range(start, start + n)])


def row_sum_odd_numbers(n):
    return n**3