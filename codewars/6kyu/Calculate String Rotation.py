def shifted_diff(first, second):
    for x in range(len(second)):
        if first == f"{second[x:]}{second[:x]}":
            return x
    return -1
