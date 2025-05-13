from copy import copy
from random import randint


class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError
        if key in self.__dict:
            raise PermissionError
        self.__dict[key] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __add__(self, other):
        result_dict = ProtectedDictInt()
        for key, val in self.__dict.items():
            result_dict[key] = val
        if isinstance(other, ProtectedDictInt):
            for key, val in other.__dict.items():
                result_dict[key] = val
        elif isinstance(other, tuple) and len(other) == 2:
            result_dict[other[0]] = other[1]
        else:
            raise ValueError
        return result_dict

    def __sub__(self, other):
        if isinstance(other, int) and other in self:
            result_dict = ProtectedDictInt()
            for key, val in self.__dict.items():
                if key != other:
                    result_dict[key] = val
            return result_dict
        else:
            raise ValueError

    def __contains__(self, key):
        return key in self.__dict

    def __len__(self):
        return len(self.__dict)

    def __str__(self):
        return str(self.__dict)

    def __iter__(self):
        return ProtectedDictIntIterator(self.__dict)


class ProtectedDictIntIterator:
    def __init__(self, collection):
        self._sorted_keys = copy(sorted(list(collection)))
        self._cursor = 0

    def __next__(self):
        try:
            key = self._sorted_keys[self._cursor]
            self._cursor += 1
            return key
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


def construct():
    object_list = []
    d = ProtectedDictInt()
    for i in range(20):
        try:
            key = randint(0, 1000)
            d[key] = key
        except:
            pass
    object_list.append(d)
    object_list.append(10)
    object_list.append("1234")
    object_list.append([1, 3, 4])
    object_list.append(ProtectedDictIntIterator([1, 3]))
    object_list.append(5.3)
    object_list.append({5: 5, 23: 23, 12: 12})
    return object_list


def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


if __name__ == "__main__":
    lst = construct()
    for obj in lst:
        if isIterable(obj):
            print(f"Iterable object: {type(obj).__name__}")
            for it in obj:
                print(it)
            print()