import math


def sum_average(arr):
    total = sum([sum(x) / len(x) for x in arr])
    print(total)
    return math.floor(total)
