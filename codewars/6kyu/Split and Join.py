def split(arr):
    print(arr)
    length = [[len(x)] for x in arr]
    sums = [y for x in arr for y in x]
    return sums, length

def join(arr1, arr2):
    length = [x[0] for x in arr2]
    res = []
    idx = 0
    for l in length:
        res.append(arr1[idx:idx+l])
        idx += l
    return res

        