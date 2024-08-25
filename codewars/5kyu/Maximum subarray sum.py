def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for number in arr:
        current_sum = max(0, current_sum + number)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    print(max_sequence([]))  # 0
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6