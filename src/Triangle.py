from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Rectangle sides can't be less than 0")
        elif (
            side_a + side_b <= side_c
            or side_c + side_b <= side_a
            or side_a + side_c <= side_b
        ):
            raise ValueError("This is not a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def get_area(self):
        t = self.get_perimeter
        p = t / 2
        return round(
            math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2
        )
