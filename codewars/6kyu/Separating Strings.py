def sep_str(st): 
    split_st = st.split(' ')
    max_len = max([len(x) for x in split_st])
    
    sep_st = []
    for x in split_st:
        sep = [y for y in x]
        if max_len != len(sep):
            for i in range(max_len - len(sep)):
                sep.extend([''])
        sep_st.append(sep)
    
    result = []
    for col in range(len(sep_st[0])):
        tmp = []
        for row in range(len(sep_st)):
            tmp.append(sep_st[row][col])
        result.append(tmp)
    return result
