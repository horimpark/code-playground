def is_centered(xs: list[int], n: int) -> bool:
    for x in range(0, int(len(xs)/2)+1):
        summ = sum(xs[x:-x])
        if x == 0:
            summ = sum(xs)
        elif x == len(xs) and len(xs) % 2 != 0:
            summ = xs[x]
        if summ == n:
            return True
    return False