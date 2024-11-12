def sum_of_intervals(intervals):
    ordered_intervals = [(i, 1) for i, _ in intervals] + [(j, -1) for _, j in intervals]
    ordered_intervals.sort(key=lambda x: x[0])
    total_len = 0
    start = ordered_intervals[0]
    open_interval_count = 1

    for i, k in ordered_intervals[1:]:
        if start == None:
            start = (i, k)
        open_interval_count += k
        if open_interval_count == 0:
            total_len += i - start[0]
            start = None
    return total_len
