from collections import Counter

def stray(arr): 
    arr_cnt = {v: k for k, v in Counter(arr).items()}
    return arr_cnt[1]

