def matrix_addition(a, b):
    print(a)
    x_len = len(a)
    y_len = len(a[0])
    
    res = []
    for y in range(y_len):
        tmp = []
        for x in range(x_len):
            tmp.append(a[y][x] + b[y][x])
        res.append(tmp)
    return res