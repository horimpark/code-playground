def average_to_binary(n):
    binary_str = bin(n)[2:]

    result = set()

    for i in range(len(binary_str)):
        new_str = binary_str[:i] + 'x' + binary_str[i+1:]
        result.add(new_str)

    return result


if __name__ == "__main__":
    print(average_to_binary(0))
    print(average_to_binary(5))
