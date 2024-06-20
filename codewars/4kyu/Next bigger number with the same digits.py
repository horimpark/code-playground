# from itertools import permutations
#
#
# def gen_permutations(num_list):
#     numbers = set()
#     for i in range(1, len(num_list) + 1):
#         for p in permutations(num_list, i):
#             n = int("".join(map(str, p)))
#             numbers.add(n)
#     return sorted(numbers)
#
#
# def next_bigger(n):
#     split_n = [int(x) for x in str(n)]
#     sorted_nums = gen_permutations(split_n)
#     if sorted_nums[-1] == n:
#         return -1
#     else:
#         idx = sorted_nums.index(n) + 1
#         return sorted_nums[idx]
#
#     return n


# 시간 초과..
# 6/19 제출


def next_bigger(n):
    split_n = list(str(n))
    length = len(split_n)

    for i in range(length - 2, -1, -1):
        if split_n[i] < split_n[i + 1]:
            break
    else:
        return -1

    for j in range(length - 1, i, -1):
        if split_n[j] > split_n[i]:
            break

    split_n[i], split_n[j] = split_n[j], split_n[i]
    split_n = split_n[: i + 1] + sorted(split_n[i + 1 :])
    return int("".join(split_n))
