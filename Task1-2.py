import math

class Shape:
    def __init__(self, identifier, vertices):
        self.identifier = identifier
        self.vertices = vertices

    def move(self, dx, dy):
        try:
            self.vertices = [(x + dx, y + dy) for x, y in self.vertices]
        except TypeError:
            raise ValueError("Вершины должны быть кортежами чисел")

    def area(self):
        raise NotImplementedError

    def is_intersect(self, other):
        raise NotImplementedError

class Quad(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier, vertices)
        if len(vertices) != 4:
            raise ValueError("Квадрат должен иметь ровно 4 вершины")

    def area(self):
        try:
            x = [v[0] for v in self.vertices]
            y = [v[1] for v in self.vertices]
            return 0.5 * abs(sum(x[i]*y[(i+1)%4] - x[(i+1)%4]*y[i] for i in range(4)))
        except IndexError:
            raise ValueError("Вершины должны быть кортежами из двух чисел")

class Pentagon(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier, vertices)
        if len(vertices) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин")

    def area(self):
        try:
            x = [v[0] for v in self.vertices]
            y = [v[1] for v in self.vertices]
            return 0.5 * abs(sum(x[i]*y[(i+1)%5] - x[(i+1)%5]*y[i] for i in range(5)))
        except IndexError:
            raise ValueError("Вершины должны быть кортежами из двух чисел")

    def is_intersect(self, other):
        return False

try:
    quad = Quad("Quad1", [(0, 0), (2, 0), (2, 2), (0, 2)])
    pentagon = Pentagon("Pentagon1", [(1, 1), (3, 1), (4, 3), (2, 4), (0, 3)])

    quad.move(1, 1)
    print("Вершины квадрата после перемещения:", quad.vertices)

    print("Площадь квадрата:", quad.area())
    print("Площадь пятиугольника:", pentagon.area())

    print("Пересекаются ли квадрат и пятиугольник?", quad.is_intersect(pentagon))

except ValueError as e:
    print(f"Ошибка: {e}")

try:
    invalid_quad = Quad("InvalidQuad", [(0, 0), (2, 0), (2, 2)])
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    invalid_pentagon = Pentagon("InvalidPentagon", [(1, 1), (3, 1), (4, 3), (2, 4)])
except ValueError as e:
    print(f"Ошибка: {e}"