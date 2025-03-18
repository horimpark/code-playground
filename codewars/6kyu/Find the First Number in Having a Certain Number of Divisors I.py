def find_min_num(num_div):
    n = 1
    while True:
        divisors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisors += 1
        if divisors == num_div:
            return n
        n += 1