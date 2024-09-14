def find_uniq(arr):
    unique_set = []
    for x in arr:
        unique_set.append("".join(sorted(set([w.lower() for w in x.strip()]))))

    most_common = max(set(unique_set), key=unique_set.count)
    different_element = [item for item in unique_set if item != most_common][0]
    unique_idx = unique_set.index(different_element)
    return arr[unique_idx]
