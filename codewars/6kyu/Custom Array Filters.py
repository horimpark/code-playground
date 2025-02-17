class MyList(list):
    def even(self):
        return [x for x in self if isinstance(x, int) and x % 2 == 0]

    def odd(self):
        return [x for x in self if isinstance(x, int) and x % 2 != 0]

    def under(self, threshold):
        return [x for x in self if isinstance(x, int) and x < threshold]

    def over(self, threshold):
        return [x for x in self if isinstance(x, int) and x > threshold]

    def in_range(self, start, end):
        return [x for x in self if isinstance(x, int) and start <= x <= end]


list = MyList
