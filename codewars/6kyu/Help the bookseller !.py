def stock_list(stocklist, categories):
    category_count = {c: 0 for c in categories}
    if not stocklist:
        return ""
    for stock in stocklist:
        letter, num = stock.split(" ")
        if letter[0] not in category_count:
            continue
        category_count[letter[0]] += int(num)

    results = [f"({l} : {n})" for l, n in category_count.items()]

    return " - ".join(results)