def count_bits(n):
    return bin(n).count("1")

print(count_bits(1234))  # 5
print(count_bits(4))  # 1