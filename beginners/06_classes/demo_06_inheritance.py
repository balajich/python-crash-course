class Shape:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth


class Rect(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        return self._length * self._breadth


class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self._length * self._breadth


if __name__ == "__main__":
    r = Rect(10, 20)
    print(r.area())
    s = Square(10)
    print(s.area())
