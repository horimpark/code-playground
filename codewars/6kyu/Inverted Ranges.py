def inverted_ranges(ranges):
    if not ranges:
        return [(0, 100)]
    empty_ranges = []
    if len(ranges) == 1:
        if ranges[0][0] != 0:
            empty_ranges.append((0, ranges[0][0] - 1))
        if ranges[0][1] != 100:
            empty_ranges.append((ranges[0][1] + 1, 100))
    else:
        range_len = len(ranges) - 1
        for i in range(range_len):
            if i == 0 and ranges[i][0] != 0:
                empty_ranges.append((0, ranges[i][0] - 1))
            start = ranges[i][1] + 1
            end = ranges[i+1][0] - 1
            if start <= end:
                empty_ranges.append((start, end))
            if i + 1 == len(ranges) - 1:
                if ranges[i+1][1] < 100:
                    empty_ranges.append((ranges[i+1][1]+1, 100))

    return empty_ranges


"""
def inverted_ranges(ranges):
    if ranges == []:
        return [(0,100)]
    start = 0
    arr = list()
    for rng in ranges:
        if start < rng[0]:
            arr.append((start, rng[0] - 1))
        start = rng[1]+1
    if start <= 100:
        arr.append((start, 100))
    return arr
"""
