from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({0}, {1})".format(self.x, self.y)

    def __add__(self, other):  # 加法 "+"
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):  # 绝对值 abs()
        return hypot(self.x, self.y)

    def __mul__(self, scalar):  # 乘法 "*"
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):  # 判断相等 "=="
        return self.x == other.x and self.y == other.y


def main():
    vector1 = Vector(3, 4)
    vector2 = Vector(2, 5)
    vector3 = Vector(3, 4)
    print(vector1 + vector2)
    print(vector1 == vector3)
    print(abs(vector1))


if __name__ == "__main__":
    main()
