from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

if __name__ == "__main__":
    rect = Rectangle(3, 2, "синий")
    rect.repr()

    circle = Circle(5, "зеленый")
    circle.repr()

    square = Square(5, "красный")
    square.repr()

