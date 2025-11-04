def find_routes(routes):
    
    res = []
    while len(routes) != len(res):
        for x in routes:
            if not res:
                res.append(x)
            else:
                if res[-1][1] == x[0]:
                    res.append(x)
                elif res[0][0] == x[1]:
                    res.insert(0, x)
                else:
                    pass
    
    text = []
    for i in range(len(res)):
        if i == 0:
            text.append(res[i][0])
            text.append(res[i][1])
        else:
            text.append(res[i][1])
    return ', '.join(text)