from collections import Counter


def group(arr):
    if not arr:
        return arr

    num_arr = []
    for a in arr:
        if a not in num_arr:
            num_arr.append(a)

    arr_counter = Counter(arr)

    return [[a] * arr_counter[a] for a in num_arr]