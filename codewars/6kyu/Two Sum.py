def two_sum(numbers, target):
    result = list()
    for x in range(len(numbers)):
        for y in [a for a in range(len(numbers)) if a != x]:
            if numbers[x] + numbers[y] == target:
                return (x, y)


#                 result.append(f"({x}, {y})")
#     return " or ".join(result)
