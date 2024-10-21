from collections import Counter, defaultdict


def find_characters(matrix):
    matrix2 = []
    for m in matrix.split("\n"):
        matrix2.extend(list(m))

    cnt = defaultdict(list)
    for x, y in sorted(dict(Counter(matrix2)).items(), key=lambda x: x[1]):
        cnt[y].append(x)
    return "".join(sorted(cnt[min(list(cnt.keys()))], key=lambda x: (x.isdigit(), x)))
