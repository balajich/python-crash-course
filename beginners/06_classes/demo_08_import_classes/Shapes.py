# Parent class
class Shape:
    def __init__(self, side1, side2):
        self._side1 = side1
        self._side2 = side2

    def area(self):
        return self._side1 * self._side2


# Child Class
class Rect(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)


# Child Class
class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)
