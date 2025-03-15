import math


class Error1(Exception):
    pass


class Figure:
    def dimension(self):
        raise NotImplementedError("Метод dimension() не реалізовано")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() не реалізовано")

    def square(self):
        raise NotImplementedError("Метод square() не реалізовано")

    def squareSurface(self):
        raise NotImplementedError("Метод squareSurface() не реалізовано")

    def squareBase(self):
        raise NotImplementedError("Метод squareBase() не реалізовано")

    def height(self):
        raise NotImplementedError("Метод height() не реалізовано")

    def volume(self):
        raise NotImplementedError("Метод volume() не реалізовано")


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not self._is_valid(a, b, c):
            raise Error1(f"Трикутник з сторонами {a}, {b}, {c} не існує")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_valid(a, b, c):
        return (a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b)

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def dimension(self):
        return 2

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, width, height):
        if not self._is_valid(width, height):
            raise Error1(f"Прямокутник з сторонами {width}, {height} не існує")
        self.width = width
        self.height = height

    @staticmethod
    def _is_valid(width, height):
        return width > 0 and height > 0

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.width + self.height)

    def square(self):
        return self.width * self.height

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, base1, base2, side1, side2):
        if not self._is_valid(base1, base2, side1, side2):
            raise Error1(f"Трапеція з параметрами {base1}, {base2}, {side1}, {side2} не існує")
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    @staticmethod
    def _is_valid(base1, base2, side1, side2):
        if not (base1 > 0 and base2 > 0 and side1 > 0 and side2 > 0):
            return False
        if abs(base1 - base2) >= side1 + side2:
            return False
        diff = (base1 - base2) ** 2 + side1 ** 2 - side2 ** 2
        denominator = 2 * (base1 - base2)
        if denominator == 0:
            return False
        k = diff / denominator
        discriminant = side1 ** 2 - k ** 2
        return discriminant > 0

    def dimension(self):
        return 2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def square(self):
        h = math.sqrt(self.side1 ** 2 - (((self.base1 - self.base2) ** 2 + self.side1 ** 2 - self.side2 ** 2) / (
                    2 * (self.base1 - self.base2))) ** 2)
        return (self.base1 + self.base2) / 2 * h

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, base, side, height):
        if not self._is_valid(base, side, height):
            raise Error1(f"Паралелограм з параметрами {base}, {side}, {height} не існує")
        self.base = base
        self.side = side
        self.height = height

    @staticmethod
    def _is_valid(base, side, height):
        return base > 0 and side > 0 and height > 0 and height <= side

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.base + self.side)

    def square(self):
        return self.base * self.height

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, radius):
        if not self._is_valid(radius):
            raise Error1(f"Коло з радіусом {radius} не існує")
        self.radius = radius

    @staticmethod
    def _is_valid(radius):
        return radius > 0

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2

    def volume(self):
        return self.square()


class Ball(Figure):
    def __init__(self, radius):
        if not self._is_valid(radius):
            raise Error1(f"Куля з радіусом {radius} не існує")
        self.radius = radius

    @staticmethod
    def _is_valid(radius):
        return radius > 0

    def dimension(self):
        return 3

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def squareSurface(self):
        return 4 * math.pi * self.radius ** 2


class TriangularPyramid(Triangle):
    def __init__(self, base_side, height):
        super().__init__(base_side, base_side, base_side)
        if not height > 0:
            raise Error1(f"Трикутна піраміда з висотою {height} не існує")
        self.h = height

    def dimension(self):
        return 3

    def squareSurface(self):
        return 3 * self.square()

    def squareBase(self):
        return self.square()

    def height(self):
        return self.h

    def volume(self):
        return (self.square() * self.h) / 3


class QuadrangularPyramid(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        if not height > 0:
            raise Error1(f"Чотирикутна піраміда з висотою {height} не існує")
        self.h = height

    def dimension(self):
        return 3

    def squareSurface(self):
        apothem = math.sqrt((self.width / 2) ** 2 + self.h ** 2)
        return 2 * apothem * (self.width + self.height)

    def squareBase(self):
        return self.square()

    def height(self):
        return self.h

    def volume(self):
        return (self.square() * self.h) / 3


class RectangularParallelepiped(Rectangle):
    def __init__(self, width, length, depth):
        super().__init__(width, length)
        if not depth > 0:
            raise Error1(f"Паралелепіпед з глибиною {depth} не існує")
        self.depth = depth

    def dimension(self):
        return 3

    def squareSurface(self):
        return 2 * (self.width * self.depth + self.height * self.depth)

    def squareBase(self):
        return self.square()

    def height(self):
        return self.depth

    def volume(self):
        return self.width * self.height * self.depth  # Fixed here


class Cone(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        if not height > 0:
            raise Error1(f"Конус з висотою {height} не існує")
        self.h = height

    def dimension(self):
        return 3

    def squareSurface(self):
        slant = math.sqrt(self.radius ** 2 + self.h ** 2)
        return math.pi * self.radius * slant

    def squareBase(self):
        return self.square()

    def height(self):
        return self.h

    def volume(self):
        return (self.square() * self.h) / 3


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, height):
        super().__init__(a, b, c)
        if not height > 0:
            raise Error1(f"Трикутна призма з висотою {height} не існує")
        self.h = height

    def dimension(self):
        return 3

    def squareSurface(self):
        return self.perimeter() * self.h

    def squareBase(self):
        return self.square()

    def height(self):
        return self.h

    def volume(self):
        return self.square() * self.h


def process_figures_from_file(filename):
    figure_classes = {
        'Triangle': Triangle,
        'Rectangle': Rectangle,
        'Trapeze': Trapeze,
        'Parallelogram': Parallelogram,
        'Circle': Circle,
        'Ball': Ball,
        'TriangularPyramid': TriangularPyramid,
        'QuadrangularPyramid': QuadrangularPyramid,
        'RectangularParallelepiped': RectangularParallelepiped,
        'Cone': Cone,
        'TriangularPrism': TriangularPrism
    }

    figures = []
    invalid_figures = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip():
                    parts = line.split()
                    figure_type = parts[0]
                    try:
                        params = [float(x) for x in parts[1:]]
                        if figure_type in figure_classes:
                            figure = figure_classes[figure_type](*params)
                            figures.append((figure, line.strip()))
                        else:
                            invalid_figures.append(f"Unknown figure type: {line.strip()}")
                    except Error1 as e:
                        invalid_figures.append(f"Invalid figure: {line.strip()} - {str(e)}")
                    except Exception as e:
                        invalid_figures.append(f"Error processing: {line.strip()} - {str(e)}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
        return None, [f"File {filename} not found"]

    if not figures:
        return None, invalid_figures

    max_figure, max_line = max(figures, key=lambda x: x[0].volume())
    return (max_figure, max_line, max_figure.volume()), invalid_figures



def print_uml_hierarchy():
    uml = [
        "UML Ієрархія класів:",
        "",
        "[Figure] (abstract)",
        "  |",
        "  +-- [Triangle]",
        "  |     |",
        "  |     +-- [TriangularPyramid]",
        "  |     +-- [TriangularPrism]",
        "  |",
        "  +-- [Rectangle]",
        "  |     |",
        "  |     +-- [QuadrangularPyramid]",
        "  |     +-- [RectangularParallelepiped]",
        "  |",
        "  +-- [Trapeze]",
        "  |",
        "  +-- [Parallelogram]",
        "  |",
        "  +-- [Circle]",
        "  |     |",
        "  |     +-- [Cone]",
        "  |",
        "  +-- [Ball]",
        "",
        "Примітка:",
        "- [Figure] є абстрактним базовим класом",
        "- Стрілки (|--) позначають спадкування",

    ]

    for line in uml:
        print(line)


if __name__ == "__main__":
    print_uml_hierarchy()
    filename = "input01.txt"
    result, invalid = process_figures_from_file(filename)



    if result:
        max_figure, max_line, max_measure = result
        print(f"Фігура з максимальною мірою:")
        print(f"Опис: {max_line}")
        print(f"Тип: {max_figure.__class__.__name__}")
        print(f"Міра: {max_measure:.2f}")
        if max_figure.dimension() == 2:
            print("(2D фігура - міра є площею)")
        else:
            print("(3D фігура - міра є об'ємом)")
    else:
        print("Не вдалося знайти валідну фігуру")

