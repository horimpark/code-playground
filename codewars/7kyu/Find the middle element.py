def gimme(input_array):
    sorted_arr = sorted(input_array)
    middle_v = sorted_arr[int(len(input_array) / 2)]
    return input_array.index(middle_v)
