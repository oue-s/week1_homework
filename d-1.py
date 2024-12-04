import math


class Circle:
    # コードが期待通り動作するように実装
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result_area = round(self.radius**2 * math.pi, 2)
        return result_area
        # return self.radius**2 * 3.14

    def perimeter(self):
        result_perimeter = round(self.radius * 2 * math.pi, 2)
        return result_perimeter
        # return self.radius * 2 * 3.14


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
