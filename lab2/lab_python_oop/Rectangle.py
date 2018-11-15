from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColour import FigureColour

class Rectangle(GeometricFigure):
    def __init__(self, width, height, colour):
        super().__init__()
        self.width = width
        self.height = height
        self.figure_color = FigureColour()
        self.figure_color.set_colour(colour)
        self.name = 'Прямоугольник'

    def area(self):
        return self.width * self.height

    def repr(self):
        print('{} {}\n Ширина {}\n Высота {}\n Площадь {}\n'.format(self.get_name(),
                                                                    self.figure_color.get_colour(),
                                                                    self.width, self.height,
                                                                    self.area()))

