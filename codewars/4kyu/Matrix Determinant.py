def inner(a, x, y):
    return [[v for j, v in enumerate(r) if j != y]
            for i, r in enumerate(a) if i != x]

def determinant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return sum(((-1) ** j) * v * determinant(inner(m, 0, j))
               for j, v in enumerate(m[0]))


