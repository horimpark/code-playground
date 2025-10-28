class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5
