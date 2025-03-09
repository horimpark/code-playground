from collections import defaultdict


def sort_and_drop(text):
    return "".join(sorted(set(t for t in text)))


def solve(arr):
    refined_arr = [sort_and_drop(a) for a in arr]
    counter = defaultdict(list)
    for idx, ra in enumerate(refined_arr):
        counter[ra].append(idx)

    answer = []
    for k, indices in counter.items():
        if len(indices) > 1:
            answer.append(sum(indices))

    return sorted(answer)