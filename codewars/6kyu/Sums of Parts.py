def parts_sums(ls):
    return [sum(ls[i:]) for i in range(len(ls))] + [0]


if __name__ == "__main__":
    print(parts_sums([0, 1, 3, 6, 10]))  # [20, 20, 19, 16, 10, 0]
    print(parts_sums([1, 2, 3, 4, 5, 6]))  # [21, 20, 18, 15, 11, 6, 0]
    print(parts_sums([]))  # [0]