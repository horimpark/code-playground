def high_and_low(numbers):
    num_list = list(map(int,numbers.split(" ")))
    numbers = " ".join([str(max(num_list)), str(min(num_list))])
    return numbers


if __name__ == "__main__":
    print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))  # "542 -214"