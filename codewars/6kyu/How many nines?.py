def nines(n):
    return sum([1 for x in range(n+1) if "9" in str(x)])


if __name__ == "__main__":
    print(nines(1))  # 0
    print(nines(100))  # 20
    print(nines(1000))  # 300