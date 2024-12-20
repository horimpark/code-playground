# time out
def parts_sums(ls):
    return [sum(ls[i:]) for i in range(len(ls))] + [0]


# 성공
def parts_sums(ls):
    total_sum = sum(ls)
    result = [total_sum]
    for num in ls:
        total_sum -= num
        result.append(total_sum)
    return result


if __name__ == "__main__":
    print(parts_sums([0, 1, 3, 6, 10]))  # [20, 20, 19, 16, 10, 0]
    print(parts_sums([1, 2, 3, 4, 5, 6]))  # [21, 20, 18, 15, 11, 6, 0]
    print(parts_sums([]))  # [0]


def parts_sums(ls):
    result = [sum(ls)]

    for x in ls:
        result.append(result[-1] - x)
    return result
