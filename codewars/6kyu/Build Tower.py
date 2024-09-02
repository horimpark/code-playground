def tower_builder(n_floors):
    max_len = 1 + 2 * (n_floors - 1)

    result = []
    for x in range(n_floors):
        star = "*" * (1 + 2 * (x))
        spaces = " " * int((max_len - len(star)) / 2)
        result.append(f"{spaces}{star}{spaces}")
    return result
