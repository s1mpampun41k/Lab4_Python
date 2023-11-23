from cmath import cos, sin, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    @staticmethod
    def distance_between(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @classmethod
    def from_polar(cls, r, angle):
        return cls(r * cos(angle).real, r * sin(angle).real)


p1 = Point(1, 2)
p2 = Point(3, 4)
p = Point.from_polar(5,  pi / 4, )

print(p1.distance_to(p2))
print(Point.distance_between(p1, p2))
print(p.x, p.y)

# Задание 4:
# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические методы, методы класса. – 1 – 3 балла