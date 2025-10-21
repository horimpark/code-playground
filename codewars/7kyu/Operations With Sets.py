def process_2arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    both = set1 & set2

    arr1_r = set1 - both
    arr2_r = set2 - both

    unique = len(arr1_r) + len(arr2_r)

    return [len(both), unique, len(arr1_r), len(arr2_r)]
