from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColour import FigureColour

class Square(GeometricFigure):
    def __init__(self, side, colour):
        super().__init__()
        self.side = side
        self.figure_color = FigureColour()
        self.figure_color.set_colour(colour)
        self.name = "Квадрат"

    def area(self):
        return self.side * self.side

    def repr(self):
        print('{} {}\n Сторона {}\n Площадь {}\n'.format(self.get_name(),
                                                         self.figure_color.get_colour(),
                                                         self.side,
                                                         self.area()))