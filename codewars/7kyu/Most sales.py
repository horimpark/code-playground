def top3(products, amounts, prices):
    pro2val = {products[i]: amounts[i] * prices[i] for i in range(len(products))}
    sorted_pro2val = sorted(pro2val.items(), key=lambda x: x[1], reverse=True)

    return [x[0] for x in sorted_pro2val][:3]
