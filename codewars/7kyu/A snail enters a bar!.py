def can_snail_reach_end(length, speed, length_increases):
    for i in range(1, 365 + 1):
        length -= speed
        length += length_increases

    return False if length > 0 else True


if __name__ == "__main__":
    can_snail_reach_end(10, 3, 2)  # True