import math

# 제출


class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return f"({','.join(map(str, self.components))})"

    def __eq__(self, other):
        return self.components == other.components

    def equals(self, other):
        return self.__eq__(other)

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("not same length")
        return Vector([x + y for x, y in zip(self.components, other.components)])

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("not same length")
        return Vector([x - y for x, y in zip(self.components, other.components)])

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("not same length")
        return sum(x * y for x, y in zip(self.components, other.components))

    def norm(self):
        return math.sqrt(sum(x**2 for x in self.components))
