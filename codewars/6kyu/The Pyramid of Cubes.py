def find_height(cubes):
    if cubes == 0:
        return 0

    height = 0
    used_cubes = 0
    layer_size = 0

    while cubes >= used_cubes:
        height += 1
        layer_size += height
        used_cubes += layer_size

        if used_cubes > cubes:
            break

    return height - 1 if used_cubes > cubes else height


if __name__ == "__main__":
    print(find_height(0))  # 0
    print(find_height(1))  # 1

