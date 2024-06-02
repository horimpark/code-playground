def flip(st, k):
    return st[:k][::-1] + st[k:]


def flip_pancakes(stack):
    if not stack or len(stack) == 1 or sorted(stack) == stack:
        return []

    flips = []
    for size in range(len(stack), 1, -1):
        max_index = stack.index(max(stack[:size]))
        if max_index != size - 1:
            if max_index != 0:
                flips.append(max_index)
                stack = flip(stack, max_index + 1)
            flips.append(size - 1)
            stack = flip(stack, size)
    return flips


check = flip_pancakes([1,5,8,3])

