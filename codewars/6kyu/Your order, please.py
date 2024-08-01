def order(sentence):
    split_sent = sentence.split(" ")
    order_nums = {y: i for i, x in enumerate(split_sent) for y in x if y.isdigit()}
    sorted_order = sorted(order_nums.items())
    result = [split_sent[v] for k, v in sorted_order]
    if result:
        return " ".join(result)
    else:
        return ""
