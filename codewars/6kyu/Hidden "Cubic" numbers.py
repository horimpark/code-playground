import re

import re


def is_cubic(n):
    return sum(int(digit) ** 3 for digit in str(n)) == n


def is_sum_of_cubes(s):
    numbers = re.findall(r'\d{1,3}', s)

    cubic_numbers = [int(num) for num in numbers if is_cubic(int(num))]

    if cubic_numbers:
        sum_cubic = sum(cubic_numbers)
        return f"{' '.join(map(str, cubic_numbers))} {sum_cubic} Lucky"
    else:
        return "Unlucky"


if __name__ == "__main__":
    print(is_sum_of_cubes("aqdf& 0 1 xyz 153 777.777"))  # "aqdf& 0 1 xyz 153 777.777 Unlucky"
    print(is_sum_of_cubes("0 9026315 -827&()"))  # "0 9026315 -827&() Happy"
    print(is_sum_of_cubes("Is 0 the same as 0"))  # "Is 0 the same as 0 Lucky"
    print(is_sum_of_cubes("Once upon a time"))  # "Once upon a time Not a cubif number"
    print(is_sum_of_cubes("8 28 512 64 729 0 1 27 729"))  # "8 28 512 64 729 0 1 27 729 Unlucky"
