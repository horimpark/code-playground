def solve(n):
    if n == 1:
        return 1

    row = [1]

    for _ in range(1, n):
        new_row = [1]
        for j in range(1, len(row)):
            new_row.append(row[j] + new_row[j - 1])
        new_row.append(new_row[-1])
        row = new_row

    return sum(row)


if __name__ == "__main__":
    print(solve(4))
    print(solve(5))
    print(solve(6))
    print(solve(7))
