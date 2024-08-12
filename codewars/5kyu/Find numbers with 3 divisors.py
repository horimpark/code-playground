import math


def is_simple(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(n, m):
    result = []
    i = math.ceil(math.sqrt(math.sqrt(n)))
    while i * i * i * i <= m:
        if is_simple(i):
            result.append(i * i * i * i)
        i += 1
    return result
