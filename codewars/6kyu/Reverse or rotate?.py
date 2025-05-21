def rev_rot(strng, sz):
    if not strng or sz <= 0 or len(strng) < sz:
        return ''
    split_strng = [strng[x:x+sz] for x in range(0, len(strng), sz) if len(strng[x:x+sz]) == sz]
    print(strng, sz)
    print(split_strng)
    res = []
    for split_x in split_strng:
        if sum([int(x) for x in split_x]) % 2 == 0:
            res.append(''.join([x for x in reversed(split_x)]))
        else:
            res.append(f"{split_x[1:]}{split_x[0]}")
    
    return ''.join(res)
