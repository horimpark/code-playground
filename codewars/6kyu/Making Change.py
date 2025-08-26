def make_change(amount):
    money_dict = {50: "H", 25: "Q", 10: "D", 5: "N", 1: "P"}
    
    res = dict()
    for k, v in money_dict.items():
        if amount // k > 0:
            res[v] = amount // k
            amount = amount % k
        else:
            continue
    return res
            
