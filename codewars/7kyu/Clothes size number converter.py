def size_to_number(size):
    if not size or not isinstance(size, str) or size == 'xm':
        return None

    x_count = size.count('x')

    base_size = size[x_count:]

    base_sizes = {'s': 36, 'm': 38, 'l': 40}

    if base_size not in base_sizes or (base_size == 'm' and x_count > 0):
        return None

    european_size = base_sizes[base_size] + x_count * 2 * (1 if base_size == 'l' else -1)

    return european_size


if __name__=="__main__":
    print(size_to_number('s'))  # 36
    print(size_to_number('m'))  # 38
    print(size_to_number('l'))  # 40
    print(size_to_number('xl'))  # 42
    print(size_to_number('xxl'))  # 44
    print(size_to_number('xxxl'))  # 46
    print(size_to_number('xxxxl'))  # None
    print(size_to_number('xm'))  # None
    print(size_to_number('sxxl'))  # None
