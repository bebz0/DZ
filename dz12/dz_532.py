from dz_531 import Rational
from exc import RationalValueError
class RationalList:
    def __init__(self, data=None):
        self._data = []
        if data is not None:
            for item in data:
                self.append(item)

    def append(self, item):
        if isinstance(item, (Rational, int)):
            if isinstance(item, int):
                item = Rational(item, 1)
            self._data.append(item)
        else:
            raise RationalValueError()

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(value, (Rational, int)):
            if isinstance(value, int):
                value = Rational(value, 1)
            self._data[index] = value
        else:
            raise RationalValueError()

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            new_list._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            new_list.append(other)
        else:
            raise RationalValueError()
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise RationalValueError()
        return self

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self._data) + "]"

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

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            rational_list = RationalList()
            for line_number, line in enumerate(file, 1):
                text = line.strip()
                if text:
                    try:
                        elements = splitter(text)
                        for elem in elements:
                            if elem not in ('+', '-', '*', '/'):
                                rational_list.append(to_rational(elem))
                    except Exception as e:
                        print(f"Рядок {line_number}: Помилка в елементі '{text}': {e}")
            print(f"Список раціональних чисел: {rational_list}")
            sum_result = Rational(0, 1)
            for num in rational_list:
                sum_result += num
            print(f"Сума чисел у списку: {sum_result} ({sum_result():.4f})")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")

if __name__ == "__main__":
    process_file('input01 (3).txt')