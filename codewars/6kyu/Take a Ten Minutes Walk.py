def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south_balance = walk.count('n') - walk.count('s')
    east_west_balance = walk.count('e') - walk.count('w')

    return north_south_balance == 0 and east_west_balance == 0


if __name__ == "__main__":
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True