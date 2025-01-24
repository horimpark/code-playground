def sum_nested_numbers(arr, depth=1):
    result = 0
    for i in arr:
        if type(i) == list:
            result += sum_nested_numbers(i, depth+1)
        else:
            result += i ** depth
    return result


if __name__ == "__main__":
    print(sum_nested_numbers([1, 2, 3, [4, 5], 6]))  # 21
    print(sum_nested_numbers([1, [2], 3, [4, [5]]]))  # 149
    print(sum_nested_numbers([1, 2, 3, [4, 5], 6, [7, 8], [9, [10]]]))  # 1247
