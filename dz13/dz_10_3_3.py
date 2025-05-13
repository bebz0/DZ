def dec(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper



@dec
def foo(a):
    return f'goodbye {a}'


@dec
def mult(a, b):
    return a * b


a = foo('Roma')
print(a)
result = mult(3, 5)
print(result)
