def michael_pays(cost):
    if cost < 5:
        return cost
    else:
        return cost - 10 if cost / 3 > 10 else cost / 3 * 2