def get_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors


def sum_for_list(lst):
    all_factors = list()
    for x in lst:
        if x < 0:
            x = -x
        all_factors.extend(get_factors(x))
    all_factors = sorted(list(set(all_factors)))
    print(all_factors)
    result = []
    for x in all_factors:
        sums = 0
        for i in lst:
            if i % x == 0:
                sums += i
        result.append([x, sums])
    return result
