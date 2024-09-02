def last_digit(n1, n2):
    print(n1, n2)
    if n2 == 0:
        return 1

    c = 1
    pattern = []
    while True:
        last_num = int(str(n1**c)[-1])
        if c == 1 and not pattern:
            pattern.append(last_num)
        else:
            if pattern[0] == last_num:
                break
            else:
                pattern.append(last_num)
        c += 1
    print(pattern)

    if n2 <= len(pattern):
        return pattern[n2 - 1]
    else:
        n2 = n2 % len(pattern)
        return pattern[n2 - 1]
