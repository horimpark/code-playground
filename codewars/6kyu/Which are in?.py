def in_array(array1, array2):
    res = []
    for x in array1:
        for y in array2:
            if x in y:
                res.append(x)
                break
    return sorted(set(res))
