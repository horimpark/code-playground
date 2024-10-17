from collections import Counter


def find_key(nums):
    nums = [str(x) for x in nums]

    res = ""
    for x in zip(*nums):
        cnt = [k for k, v in dict(Counter(x)).items() if v == 1][0]
        res += cnt
    return res


# def find_key(nums):
#     cols = [*zip(*map(str, nums))]
#     return ''.join(next(x for x in c if c.count(x) == 1) for c in cols)
