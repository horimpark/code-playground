import math

def is_square(n):
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n


if __name__ == "__main__":
    print(is_square(-1))  # False
    print(is_square(0))  # True