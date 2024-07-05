def count_feelings(st, arr):
    feeling_cnt = 0
    for x in arr:
        split_st = [x for x in st]
        check = []
        for a in x:
            if a in split_st:
                split_st.remove(a)
                check.append(a)
            else:
                continue
        if check == [a for a in x]:
            feeling_cnt += 1
    if feeling_cnt == 1:
        return f"{feeling_cnt} feeling."
    return f"{feeling_cnt} feelings."
