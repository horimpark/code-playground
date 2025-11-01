def consecutive(arr):
    if len(arr) <= 1:
        return 0
    
    cnt = 0
    for x in range(min(arr), max(arr)+1):
        if x not in arr:
            cnt += 1
    return cnt