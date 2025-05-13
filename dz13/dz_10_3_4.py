def dec(cls):
    origin_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Створено екземпляр класу: {cls.__name__}")
        origin_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@dec
class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(5)
