def cnt_div(x):
    divs = []
    for i in range(2, x):
        if x % i == 0:
            divs.append(i)
        if len(divs) >= 3:
            break
    return True if len(divs) >= 3 else False


def solution(n, m):
    print(n, m)
    result = []
    for x in range(n, m + 1):
        if cnt_div(x):
            result.append(x)
    return result
