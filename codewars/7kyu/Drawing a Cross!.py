def draw_a_cross(n):
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
    if n % 2 == 0:
        return "Centered cross not possible!"

    res = []
    for x in range(int(n / 2)):
        side_space = " " * x
        middle_space = " " * (n - 2 * (x + 1))
        text = f"{side_space}x{middle_space}x{side_space}"
        res.append(text)

    space = " " * int((n - 1) / 2)
    res.append(f"{space}x{space}")
    for x in range(len(res) - 2, -1, -1):
        res.append(res[x])
    return "\n".join(res)
