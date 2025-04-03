def rotate(arr, n):
    print(arr, n)
    if n > len(arr):
        n = n % len(arr)
    else:
        n = -n %len(arr)
        n = -n
    arr = arr[-n:] + arr[:-n]
    print(arr, n)
    return arr