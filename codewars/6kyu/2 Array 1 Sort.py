def linked_sort(array_to_sort, linked_array, key=None, reverse=False):
    if key is None:
        key = str

    indices = sorted(range(len(array_to_sort)),
                     key=lambda i: key(array_to_sort[i]),
                     reverse=reverse)

    a_copy = array_to_sort[:]
    b_copy = linked_array[:]
    for new_pos, old_pos in enumerate(indices):
        array_to_sort[new_pos] = a_copy[old_pos]
        linked_array[new_pos] = b_copy[old_pos]

    return array_to_sort