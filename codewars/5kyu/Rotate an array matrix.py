def rotate(matrix, direction):
    width, length = len(matrix), len(matrix[0])
    res = []

    if direction == "clockwise":
        for y in range(0, length, 1):
            tmp = []
            for x in range(width - 1, -1, -1):
                tmp.append(matrix[x][y])
            res.append(tmp)

    elif direction == "counter-clockwise":
        for y in range(length - 1, -1, -1):
            tmp = []
            for x in range(0, width, 1):
                tmp.append(matrix[x][y])
            res.append(tmp)

    return res
