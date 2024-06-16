from itertools import combinations_with_replacement


# 어려워서 구글링의 도움 받음
def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str(x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]


if __name__ == "__main__":
    print(find_all(10, 3))
    print(find_all(27, 3))
