def points(games):
    total = 0
    for x in games:
        split_x = x.split(":")
        if int(split_x[0]) > int(split_x[1]):
            total += 3
        elif int(split_x[0]) == int(split_x[1]):
            total += 1
    return total
