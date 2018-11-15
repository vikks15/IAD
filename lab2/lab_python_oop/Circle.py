from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColour import FigureColour
from math import pi

class Circle(GeometricFigure):
    def __init__(self, radius, colour):
        super().__init__()
        self.radius = radius
        self.figure_color = FigureColour()
        self.figure_color.set_colour(colour)
        self.name = "Круг"

    def area(self):
        return pi * self.radius * self.radius

    def repr(self):
        print('{} {}\n Радиус {}\n Площадь {}\n'.format(self.get_name(),
                                                        self.figure_color.get_colour(),
                                                        self.radius,
                                                        self.area()))