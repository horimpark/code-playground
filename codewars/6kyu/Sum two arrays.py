def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []
    arr1 = int("".join([str(x) for x in array1])) if array1 else 0
    arr2 = int("".join([str(x) for x in array2])) if array2 else 0

    res = arr1 + arr2
    minus = False
    result = []
    for x in str(res):
        if x == "-":
            minus = True
            continue
        else:
            if minus:
                result.append(int(f"-{x}"))
                minus = False
            else:
                result.append(int(x))
    return result


# def sum_arrays(array1,array2):
#     if not array1: return array2
#     if not array2: return array1
#     num = sum(map(lambda x: int(''.join(map(str, x))), [array1, array2]))
#     lst = list(map(int, str(abs(num))))
#     if num < 0: lst[0] *=-1
#     return lst
