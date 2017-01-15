import math


class Parallelogram(object):
    def __init__(self, base, side, theta):
        self._base = base
        self._side = side
        self._theta = theta

    def area(self):
        theta_in_radians = math.radians(self._theta)
        area = self._base * self._side * math.sin(theta_in_radians)
        return area

    def __str__(self):
        return "I am a Parallelogram with area " + str(self.area())

    def bst(self):
        bst_list = [self._base, self._side, self._theta]
        return bst_list


class Rectangle(Parallelogram):
    def __init__(self, base, side):
        theta = 90
        Parallelogram.__init__(self, base, side, theta)

    def __str__(self):
        return "I am a Rectangle with area " + str(self.area())


class Rhombus(Parallelogram):
    def __init__(self, base, theta):
        side = base
        Parallelogram.__init__(self, base, side, theta)

    def __str__(self):
        return "I am a Rhombus with area " + str(self.area())


class Square(Rectangle):
    def __init__(self, base):
        side = base
        Rectangle.__init__(self, base, side)

    def __str__(self):
        return "I am a Square with area " + str(self.area())
