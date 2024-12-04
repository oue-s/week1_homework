import math


class Rectangle:
    # コードが期待通り動作するように実装
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        result_area = format((self.height) * self.width, ".2f")
        return result_area

    def diagonal(self):
        result_diagonal = format(math.sqrt(self.height**2 + self.width**2), ".2f")
        return result_diagonal


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
