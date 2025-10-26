def zeros(n):
    cnt = 0
    while n:
        n //= 5
        cnt += n
    return cnt
