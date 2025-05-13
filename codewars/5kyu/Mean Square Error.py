def solution(array_a, array_b):
    res = []
    for x, y in zip(array_a, array_b):
        sums = x - y if x >= y else y - x
        res.append(sums**2)
    return sum(res)/len(res)
        
