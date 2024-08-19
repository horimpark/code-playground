def delete_nth(order, max_e):
    result = []
    count = {}

    for number in order:
        if count.get(number, 0) < max_e:
            result.append(number)
            count[number] = count.get(number, 0) + 1

    return result


if __name__ == "__main__":
    print(delete_nth([20, 37, 20, 21], 1))  # [20, 37, 21]
    print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))  # [1, 1, 3, 3, 7, 2, 2, 2
