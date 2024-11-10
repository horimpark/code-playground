def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    check = []
    for x in intervals:
        if not check:
            check.append(x)
        else:
            for i, c in enumerate(check):
                if list(c)[-1] >= x[0]:
                    check[i] = sorted(list(set(c + x)))
                else:
                    check.append(x)
    return sum([x[-1] - x[0] for x in check])
