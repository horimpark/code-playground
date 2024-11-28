from collections import Counter


def triple_double(num1, num2):
    count_num1 = Counter([n for n in str(num1)])
    count_num2 = Counter([n for n in str(num2)])

    c1_3 = {k for k, v in count_num1.items() if v >= 3}
    c2_2 = {k for k, v in count_num2.items() if v >= 2}

    if c1_3 & c2_2:
        return 1
    return 0
