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

    def get_edges(self):
        edges = []
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % num_vertices]
            edges.append((x2 - x1, y2 - y1))
        return edges

    def project(self, axis):
        dots = [axis[0] * x + axis[1] * y for x, y in self.vertices]
        return min(dots), max(dots)

    def is_intersect(self, other):
        edges = self.get_edges() + other.get_edges()
        for edge in edges:
            dx, dy = edge
            axis = (-dy, dx)
            axis_length = math.hypot(axis[0], axis[1])
            if axis_length == 0:
                continue
            axis = (axis[0] / axis_length, axis[1] / axis_length)

            proj1 = self.project(axis)
            proj2 = other.project(axis)

            if proj1[1] < proj2[0] or proj2[1] < proj1[0]:
                return False
        return True

class Quad(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier, vertices)
        if len(vertices) != 4:
            raise ValueError("Квадрат должен иметь ровно 4 вершины")

class Pentagon(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier, vertices)
        if len(vertices) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин")

try:
    quad = Quad("Quad1", [(0, 0), (2, 0), (2, 2), (0, 2)])
    pentagon = Pentagon("Pentagon1", [(3, 3), (5, 3), (5, 5), (4, 6), (2, 5)])

    print("Пересекаются ли квадрат и пятиугольник?", quad.is_intersect(pentagon))  # Должно быть False

    quad.move(1, 1)
    print("Вершины квадрата после перемещения:", quad.vertices)
    print("Пересекаются ли квадрат и пятиугольник после перемещения?", quad.is_intersect(pentagon))  # Должно быть False

except ValueError as e:
    print(f"Ошибка: {e}")