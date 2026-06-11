from Rectangle import Rectangle
from figure import Figure
import math

class Circle(Figure):
    def __init__(self, rad):
        if rad <= 0:
            raise ValueError ("Circle radius can't be less than 0")
        self.rad = rad

    @property
    def get_area(self):
        return round(math.pi * self.rad ** 2, 2)


    @property
    def get_perimeter(self):
        return round(2 * math.pi * self.rad, 2)

c = Circle(7)
r = Rectangle(2, 4)
print (c.add_area(r))


