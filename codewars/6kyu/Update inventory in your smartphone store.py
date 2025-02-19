from collections import defaultdict


def update_inventory(cur_stock, new_stock):
    stock = cur_stock + new_stock
    stock_dict = defaultdict(int)
    for qty, name in stock:
        stock_dict[name] += qty

    now_stock = [(v, k) for k, v in stock_dict.items()]
    return sorted(now_stock, key=lambda x: x[1])
