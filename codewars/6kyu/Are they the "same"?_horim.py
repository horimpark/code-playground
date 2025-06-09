def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    arr1 = sorted([x*x for x in array1])
    arr2 = sorted(array2)
    return True if arr1 == arr2 else False
