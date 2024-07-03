def ips_between(start, end):
    start_split = [int(x) for x in start.split(".")]
    end_split = [int(x) for x in end.split(".")]
    ranges = [y - x for x, y in zip(start_split, end_split)]
    ranges.reverse()

    return sum([256**i * x for i, x in enumerate(ranges)])
