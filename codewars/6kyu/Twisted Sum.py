def compute_sum(n):
    sum = 0
    for x in range(1, n + 1):
        tmp = 0
        for y in str(x):
            tmp += int(y)
        sum += tmp
    return sum


#    return sum(int(c) for i in range(1, n+1) for c in str(i))
