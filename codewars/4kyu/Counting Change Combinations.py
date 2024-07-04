def count_change(amount, coins):
    change = [0] * (amount + 1)
    change[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            change[x] += change[x - coin]
    return change[amount]
