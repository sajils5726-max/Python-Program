class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(10, 20)
r2 = Rectangle(20, 10)


if r1 < r2:
    print("Rectangle 1 has smaller area than Rectangle 2")
else:
    print("Rectangle 1 has greater or equal area than Rectangle 2")
  