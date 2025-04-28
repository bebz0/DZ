
class RationalError(ZeroDivisionError):
    def __init__(self, message="Не можна ділити на нуль"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message



class RationalValueError(Exception):
    def __init__(self, message="Некоректні дані"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
