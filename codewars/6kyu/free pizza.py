def pizza_rewards(customers, min_orders, min_price):
    print(customers)
    print(min_orders, min_price)
    result = {name for name, orders in customers.items() if len([x for x in orders if x >= min_price]) >= min_orders}
    return result