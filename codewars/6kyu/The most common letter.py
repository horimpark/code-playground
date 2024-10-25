from collections import Counter


def replace_common(st, letter):
    most = Counter([x for x in st if x != " "]).most_common(1)[0][0]

    return "".join([letter if x == most else x for x in st])
