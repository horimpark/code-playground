def min_value(arr, n):
    return [min(arr[x : x + n]) for x in range(0, len(arr) - n + 1)]
