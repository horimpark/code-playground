from collections import defaultdict, Counter


def highest_rank(arr):
    cnt = Counter(arr)
    cnt_dict = defaultdict(list)
    for k, v in cnt.items():
        cnt_dict[v].append(k)
    return max(cnt_dict[max(list(cnt_dict.keys()))])


# return max(sorted(arr,reverse=True), key=arr.count)
