MyClass = type('MyClass', (), {})

obj = MyClass()
print(type(obj))
print(f"Class name: {MyClass.__name__}")
print(isinstance(obj, MyClass))