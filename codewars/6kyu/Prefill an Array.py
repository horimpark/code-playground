def prefill(n,v=None):
    if (isinstance(n, int) and n < 0) or (isinstance(n, str) and not n.isdigit()) or n is None:
        return f"{n} is invalid"
    elif n == 0:
        return []
    else:
        return [v for _ in range(int(n))]