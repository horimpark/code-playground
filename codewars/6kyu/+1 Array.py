def up_array(arr):
    if any(x < 0 or x >= 10 for x in arr) or not arr:
        return None
    print(arr)
    next_arr = [x for x in str(int("".join([str(x) for x in arr])) + 1)]
    if len(arr) > len(next_arr):
        for x in range(len(arr) - len(next_arr)):
            next_arr.insert(0, "0")
    print(next_arr)
    return [int(x) for x in next_arr]
