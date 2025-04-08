def find_added(st1, st2):
    st1, st2 = list(st1), list(st2)
    for x in st1:
        if x in st2:
            st2.remove(x)
    
    st2 = sorted(st2)
    return ''.join(st2)
