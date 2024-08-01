from collections import Counter


def only_duplicates(st):
    split_st = [k for k, v in Counter([x for x in st]).items() if v > 1]
    return "".join([x for x in [x for x in st] if x in split_st])
