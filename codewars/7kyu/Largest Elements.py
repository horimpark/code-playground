def largest(n, xs):
    return sorted(xs)[-n:] if n != 0 else []
