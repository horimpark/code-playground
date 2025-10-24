def order_weight(strng):
    weight_dict = [(x, sum([int(a) for a in x])) for x in strng.split(" ")]
    sorted_weight = sorted(weight_dict, key=lambda x: (x[1], x[0]))
    print(sorted_weight)
    return " ".join(list([a for a, b in sorted_weight]))
