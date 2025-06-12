def solution(a):
    jump = 0
    now = 0
    total = 0
    while 0 <= now <= len(a) - 1:
        now += a[now]
        jump += 1
        
        if jump > len(a):
            return -1
    return jump