def explode(arr):  
    w = arr[0] if isinstance(arr[0], int) else 0
    h = arr[1] if isinstance(arr[1], int) else 0
    if all(isinstance(x, int) is False for x in arr):
        return 'Void!'
    res = [arr for x in range(w+h)]
    return res
