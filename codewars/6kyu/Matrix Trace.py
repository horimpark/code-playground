def trace(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return None
    
    res = 0
    for x in range(len(matrix)):
        res += matrix[x][x]
    return res
