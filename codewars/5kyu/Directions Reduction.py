def dir_reduc(arr):
    opposite_direction = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST",
    }

    for x in range(len(arr) - 1):
        if arr[x + 1] == opposite_direction[arr[x]]:
            del arr[x], arr[x]

            return dir_reduc(arr)
    return arr


def dir_reduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []

    for direction in arr:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack