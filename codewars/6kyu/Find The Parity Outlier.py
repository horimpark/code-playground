def find_outlier(integers):
    odds = []
    evens = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    if len(odds) == 1:
        return odds[0]
    elif len(evens) == 1:
        return evens[0]
    return None


if __name__ == "__main__":
    find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])  # 11
