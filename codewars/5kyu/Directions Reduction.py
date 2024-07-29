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
