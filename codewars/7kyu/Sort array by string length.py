def sort_by_length(arr):
    arr_by_len = {x: len(x) for x in arr}
    sorted_res = dict(sorted(arr_by_len.items(), key=lambda x: x[1])).keys()
    return list(sorted_res)