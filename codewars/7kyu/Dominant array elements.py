def solve(arr):
    res = []

    for i in range(len(arr)):
        if i == len(arr) - 1:
            res.append(arr[i])
        else:
            if all(arr[i] > x for x in arr[i + 1 :]):
                res.append(arr[i])
    return res
