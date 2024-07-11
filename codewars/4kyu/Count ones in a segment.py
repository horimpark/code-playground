def countOnes(left, right):
    def count_ones_in_range(n):
        count = 0
        bit = 1
        while bit <= n:
            complete_blocks = n // (bit * 2)
            count += complete_blocks * bit
            remainder = n % (bit * 2)
            count += max(0, remainder - bit + 1)
            bit <<= 1
        return count

    if left == 0:
        return count_ones_in_range(right)
    else:
        return count_ones_in_range(right) - count_ones_in_range(left - 1)

print(countOnes(4, 7))
