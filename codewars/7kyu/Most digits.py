def find_longest(arr):
    digit = [len(str(x)) for x in arr]
    idx = digit.index(max(digit))
    return arr[idx]
