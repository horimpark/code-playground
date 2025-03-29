import numpy as np


def comp(array1, array2):
    if array2 is None:
        return False
    if array1 is None:
        return False
    if len(array1) != len(array2):
        return False
    array1 = [np.abs(a) for a in array1]
    array2 = [np.abs(a) for a in array2]
    return all(a1 ** 2 == a2 for a1, a2 in zip(sorted(array1), sorted(array2)))
