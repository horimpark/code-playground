def order_breaker(input_list):
    def is_sorted(lst):
        return all(lst[x] <= lst[x + 1] for x in range(len(lst) - 1))

    for i in range(len(input_list)):
        temp_list = input_list[:i] + input_list[i+1:]
        if is_sorted(temp_list):
            return input_list[i]
    return None