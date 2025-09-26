def rotate_clockwise(matrix):
    if not matrix:
        return []
    rotated = []
    for x in range(len(matrix[0])):
        rotated.append(''.join([matrix[y][x] for y in range(len(matrix)-1, -1, -1)]))
        
    return rotated