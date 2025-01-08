def beeramid(bonus, price):
    if bonus < 0:
        return 0
    k = 1
    stack_price = 0
    while stack_price <= bonus:
        stack_price += (k**2) * price
        k += 1
    return k - 2


if __name__ == "__main__":
    print(beeramid(9, 2))
    print(beeramid(10, 2))
    print(beeramid(11, 2))
    print(beeramid(21, 1.5))
    print(beeramid(454, 5))
    print(beeramid(455, 5))
    print(beeramid(4, 4))
    print(beeramid(3, 4))
    print(beeramid(0, 4))
    print(beeramid(-1, 4))


# %%
# def beeramid(bonus, price):
#     histories = []
#     t_price = 0
#     height = 0
#     while t_price < bonus:
#         height += 1
#         t_price += height*height*price
#         histories.append(t_price)
#     if not histories:
#         return 0
#     return height - 1 if bonus < t_price else height
