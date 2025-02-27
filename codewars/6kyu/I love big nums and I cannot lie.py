def biggest(nums):
    return str(int("".join(sorted(map(str, nums), key=lambda x: x * 10, reverse=True))))
