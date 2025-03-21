from turtle import *
import math
import time

class Figure:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._visible = False
        self._color = color

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує фігуру заданим кольором
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
        :param color: колір
        """
        pos = (self._x, self._y)


    def show(self):
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()



class Circle(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)  # Обов’язковий виклик конструктора базового класу
        self._r = r

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


class Quadrate(Figure):
    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(4):
            forward(self._a)
            left(90)
        up()

#################### клас Triangle  ############################
################################################################

class Triangle(Figure):
    """ Клас Трикутник

    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)
        self._a = a

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(3):
            forward(self._a)
            left(120)
        up()


class Car:
    """ Клас Машина """

    def __init__(self, x, y, width, height, wheel_radius, color):
        self.x = x
        self.y = y
        self.color = color

        self.body = Rectangle(x, y, width, height, color)
        self.wheels = [
            Circle(x + width * 0.2, y - wheel_radius, wheel_radius, "black"),
            Circle(x + width * 0.8, y - wheel_radius, wheel_radius, "black")
        ]

        self.roof = Trapezoid(x + (width - width * 0.7) / 2, y + height, width * 0.7, width * 0.4, color)

        self.windows = [
            Rectangle(x + width * 0.15, y + height * 0.3, width * 0.25, height * 0.4, "blue"),
            Rectangle(x + width * 0.6, y + height * 0.3, width * 0.25, height * 0.4, "blue")
        ]

    def show(self):
        self.body.show()
        self.roof.show()
        for wheel in self.wheels:
            wheel.show()
        for window in self.windows:
            window.show()

    def hide(self):
        self.body.hide()
        self.roof.hide()
        for wheel in self.wheels:
            wheel.hide()
        for window in self.windows:
            window.hide()

        def move(self, dx, dy):
            self.hide()
            self.x += dx
            self.y += dy

            self.body.move(dx, dy)
            self.roof.move(dx, dy)
            for wheel in self.wheels:
                wheel.move(dx, dy)
            for window in self.windows:
                window.move(dx, dy)

            self.show()

    def move(self, dx, dy):
        self.hide()
        self.x += dx
        self.y += dy

        self.body.move(dx, dy)
        self.roof.move(dx, dy)
        for wheel in self.wheels:
            wheel.move(dx, dy)
        for window in self.windows:
            window.move(dx, dy)

        self.show()


class Trapezoid(Figure):
    def __init__(self, x, y, a, b, color):
        super().__init__(x, y, color)
        self._a = a
        self._b = b
        delta = (self._b - self._a) / 2  # Половина різниці основ

        # Припускаємо рівнобічну трапецію
        self._h = math.sqrt(self._b ** 2 - delta ** 2)  # Висота з теореми Піфагора

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        forward(self._a)
        left(120)
        side_len = ((self._a - self._b) / 2) * (3 ** 0.5)
        forward(side_len)
        left(60)
        forward(self._b)
        left(60)
        forward(side_len)
        left(120)
        up()


class Rectangle(Figure):
    def __init__(self, x, y, a, b, color):
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a
        self._b = b

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(2):
            forward(self._a)
            left(90)
            forward(self._b)
            left(90)
        up()

    # Перевірка


if __name__ == "__main__":
    bgcolor("white")
    tracer(0, 0)

    car = Car(-200, 0, 200, 70, 30, "red")
    car.show()
    update()
    time.sleep(1)  # Пауза перед початком руху

    for _ in range(100):
        car.move(2, 0)
        update()
        time.sleep(0.02)

    done()

    # c = Circle(120, 120, 50, "blue")
    # c.show()
    # c.move(-30, -140)
    # c.hide()

    ###### Перевірка квадрата ############
    # q = Quadrate(0, 0, 150, "red")
    # q.show()
    # q.move(0, 140)
    # q.hide()

    ###### Перевірка трикутника ############
    # t = Triangle(120, 120, 50, "blue")
    # t.show()
    # t.move(-30, -140)
    # t.hide()

    ##### Перевірка трапеції ############
    # t = Trapezoid(120, 120, 50, 30, "red")
    # t.show()
    # t.move(-30, -140)
    # t.hide()

    # ###### Перевірка прямокутника ############
    # t = Rectangle(120, 120, 50, 30, "red")
    # t.show()
    # t.move(-30, -140)
    # t.hide()

