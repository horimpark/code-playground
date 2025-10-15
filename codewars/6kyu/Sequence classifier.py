def is_duplicated(arr):
    if len(arr) == len(set(arr)):
        return False
    return True

def is_increasing(arr):
    if sorted(arr) == arr:
        return True
    return False

def is_decreasing(arr):
    if sorted(arr, reverse=True) == arr:
        return True
    return False

def is_constant(arr):
    if len(set(arr)) == 1:
        return True
    return False

def sequence_classifier(arr):
    if is_constant(arr):
        return 5
    elif is_increasing(arr):
        return 2 if is_duplicated(arr) else 1
    elif is_decreasing(arr):
        return 4 if is_duplicated(arr) else 3
    return 0