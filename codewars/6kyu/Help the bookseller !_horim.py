def stock_list(stocklist, categories):
    if not stocklist:
        return ""
    
    res = {x: 0 for x in categories}
    for stock in stocklist:
        name, count = stock.split(' ')[0], stock.split(' ')[1]
        category = name[0]
        
        if category in res:
            res[category] += int(count)
    
    res = dict(sorted(res.items()))
    res = [f"({x} : {res[x]})" for x in categories]
    return ' - '.join(res)