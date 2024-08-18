def count_bits(n):
    return bin(n).count("1")


print(count_bits(1234))  # 5
print(count_bits(4))  # 1


# horim style
# def count_bits(n):
#     return sum([int(x) for x in str(bin(n)[2:])])
