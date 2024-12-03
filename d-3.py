import math


class Square:
    # コードが期待通り動作するように実装
    def __init__(self, side):
        self.side = side

    def area(self):
        result_area = self.side**2
        if result_area * 100 % 100 == 0:
            result_area = format(result_area, ".0f")
        else:
            result_area = format((self.side) ** 2, ".2f")
        return result_area

    def diagonal(self):
        result_diagonal = math.sqrt(self.side**2 + self.side**2)
        if result_diagonal * 100 % 100 == 0:
            result_diagonal = format(result_diagonal, ".0f")
        else:
            result_diagonal = format(result_diagonal, ".2f")
        return result_diagonal


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
