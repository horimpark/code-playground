from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def product_fib(_prod):
    x = 2
    a, b = fib(x), fib(x + 1)
    while a * b <= _prod:
        a, b = fib(x), fib(x + 1)
        if a * b == _prod:
            print(a, b)
            return [a, b, True]
        x += 1

    return [fib(x - 1), fib(x), False]
