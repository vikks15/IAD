from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self):
        self.name = "Фигура"

    @abstractmethod
    def area(self):
        pass

    def get_name(self):
        return self.name