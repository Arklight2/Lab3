import math

class Shape:
    def __init__(self, identifier, vertices):
        if not vertices or not isinstance(vertices, list):
            raise ValueError("Список вершин должен быть непустым")
        self.identifier = identifier
        self.vertices = self._validate_vertices(vertices)

    def _validate_vertices(self, vertices):
        for vertex in vertices:
            if not isinstance(vertex, tuple) or len(vertex) != 2 or not all(isinstance(coord, (int, float)) for coord in vertex):
                raise ValueError("Каждая вершина должна быть кортежем из двух чисел")
        return vertices

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise ValueError("Смещение должно быть числом")
        self.vertices = [(x + dx, y + dy) for x, y in self.vertices]

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
        if not isinstance(other, Shape):
            raise ValueError("Метод is_intersect принимает только объекты типа Shape")
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
        if len(vertices) != 4:
            raise ValueError("Четырёхугольник должен иметь ровно 4 вершины")
        super().__init__(identifier, vertices)

class Pentagon(Shape):
    def __init__(self, identifier, vertices):
        if len(vertices) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин")
        super().__init__(identifier, vertices)



quad = Quad("Quad1", [(0, 0), (2, 0), (2, 2), (0, 2)])
pentagon = Pentagon("Pentagon1", [(3, 3), (5, 3), (5, 5), (4, 6), (2, 5)])

print("Вершины квадрата до перемещения:", quad.vertices)
print("Вершины пятиугольника до перемещения:", pentagon.vertices)
print("Пересекаются ли квадрат и пятиугольник?", quad.is_intersect(pentagon))

quad.move(1, 1)
print("Вершины квадрата после перемещения:", quad.vertices)
print("Пересекаются ли квадрат и пятиугольник после перемещения?", quad.is_intersect(pentagon))

try:
    invalid_quad = Quad("InvalidQuad", [(0, 0), (2, 0), (2, 2)])
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    invalid_pentagon = Pentagon("InvalidPentagon", [(1, 1), (3, 1), (4, 3), (2, 4)])
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    invalid_vertices_quad = Quad("InvalidVerticesQuad", [(0, 0), (2, 0), (2, "a"), (0, 2)])
except ValueError as e:
    print(f"Ошибка: {e}")
try:
    invalid_vertices_pentagon = Pentagon("InvalidVerticesQuad", [(3, 3), ("a", 3), (5, 5), (4, 6), (2, 5)])
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    invalid_move = Quad("InvalidMove", [(0, 0), (2, 0), (2, 2), (0, 2)])
    invalid_move.move("a", 1)
except ValueError as e:
    print(f"Ошибка: {e}")
