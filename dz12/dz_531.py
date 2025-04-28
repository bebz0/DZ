from math import gcd

from exc import RationalError, RationalValueError


class Rational:
    def __init__(self, *args):
        if len(args) == 2:
            n, d = args
            if not isinstance(n, int) or not isinstance(d, int):
                raise ValueError("Чисельник і знаменник мають бути цілими числами")
            if d == 0:
                raise RationalError()
            self._normalize(n, d)
        elif len(args) == 1:
            if not isinstance(args[0], str):
                raise ValueError("Очікується рядок у форматі 'n/d'")
            try:
                n, d = map(int, args[0].split('/'))
                if d == 0:
                    raise RationalError
                self._normalize(n, d)
            except ValueError:
                raise ValueError("Неправильний формат рядка. Очікується 'n/d'")
        else:
            raise ValueError("Неправильна кількість аргументів")

    def _normalize(self, n, d):
        sign = -1 if (n * d < 0) else 1
        n, d = abs(n), abs(d)
        divisor = gcd(n, d)
        self._n = sign * (n // divisor)
        self._d = d // divisor

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError()
        n = self._n * other._d + other._n * self._d
        d = self._d * other._d
        return Rational(n, d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError()
        n = self._n * other._d - other._n * self._d
        d = self._d * other._d
        return Rational(n, d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError()
        n = self._n * other._n
        d = self._d * other._d
        return Rational(n, d)

    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                raise RationalError()
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError()
        if other._n == 0:
            raise RationalError()
        n = self._n * other._d
        d = self._d * other._n
        return Rational(n, d)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == 'n':
            return self._n
        elif key == 'd':
            return self._d
        raise KeyError("Ключ має бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Значення має бути цілим числом")
        if key == 'n':
            self._normalize(value, self._d)
        elif key == 'd':
            if value == 0:
                raise RationalError()
            self._normalize(self._n, value)
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")

    def __str__(self):
        return f"{self._n}/{self._d}"


def splitter(text):
    return text.split()


def is_rational(elem):
    return '/' in elem and len(elem.split('/')) == 2


def to_rational(elem):
    if isinstance(elem, Rational):
        return elem
    if is_rational(elem):
        return Rational(elem)
    return Rational(int(elem), 1)


def evaluate_multiplication_division(elements):
    result = []
    i = 0
    while i < len(elements):
        elem = elements[i]
        if elem in ('*', '/'):
            if i == 0 or i == len(elements) - 1:
                raise ValueError("Неправильний вираз: оператор на початку або в кінці")
            left = to_rational(result.pop()) if result else to_rational(elements[i - 1])
            right = to_rational(elements[i + 1])
            if elem == '*':
                res = left * right
            else:
                res = left / right
            result.append(res)
            i += 2
        else:
            if i == 0 or elements[i - 1] not in ('*', '/'):
                result.append(elem)
            i += 1
    return result


def evaluate_addition_subtraction(elements):
    if not elements:
        raise ValueError("Порожній вираз")

    result = to_rational(elements[0])
    i = 1
    while i < len(elements):
        op = elements[i]
        if op in ('+', '-'):
            if i + 1 >= len(elements):
                raise ValueError("Неправильний вираз: оператор в кінці")
            right = to_rational(elements[i + 1])
            if op == '+':
                result = result + right
            else:
                result = result - right
            i += 2
        else:
            i += 1
    return result


def evaluate_expression(text):
    elements = splitter(text)
    intermediate = evaluate_multiplication_division(elements)
    final_result = evaluate_addition_subtraction(intermediate)
    return final_result


def process_file(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                text = line.strip()
                if text:
                    try:
                        result = evaluate_expression(text)
                        print(f"Рядок {line_number}: {text}")
                        print(f"Результат: {result} ({result():.4f})")
                    except Exception as e:
                        print(f"Рядок {line_number}: Помилка в виразі '{text}': {e}")
                print("-" * 50)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")


process_file('input01 (3).txt')
