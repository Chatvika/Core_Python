class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def print_point(self):
        return f"x is {self.x} and y is {self.y}"

    def __add__(self, B):   # better name:B
        return Point(self.x + B.x, self.y + B.y)


p1 = Point(3, 2)
p2 = Point(6, 3)

P = p1 + p2
print(P.print_point())


