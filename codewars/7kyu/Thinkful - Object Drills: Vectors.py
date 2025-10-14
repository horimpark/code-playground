class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_v):
        return Vector(self.x + other_v.x, self.y + other_v.y)