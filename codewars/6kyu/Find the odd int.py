def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
    return None


if __name__ == "__main__":
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))  # 5
    print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))  # -1
    print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))  # 5
    print(find_it([10]))  # 10
    print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))  # 10
    print(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]))  # 1
    print(find_it([10, 5, 4, 3, 2, 1, 5, 4, 3, 2, 10]))  # 1
