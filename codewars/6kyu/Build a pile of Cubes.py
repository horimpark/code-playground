def find_nb(m):
    n = 0
    total_volume = 0

    while total_volume < m:
        n += 1
        total_volume += n ** 3

        if total_volume > m:
            return -1

    return n if total_volume == m else -1