from itertools import product


def get_pins(observed):
    pos = {
        "1": "124",
        "2": "1235",
        "3": "236",
        "4": "1457",
        "5": "24568",
        "6": "3569",
        "7": "478",
        "8": "57890",
        "9": "689",
        "0": "08",
    }

    tmp = []

    for x in observed:
        tmp.append([int(y) for y in pos[x]])

    combinations = product(*tmp)
    result = ["".join(map(str, combo)) for combo in combinations]
    return result
