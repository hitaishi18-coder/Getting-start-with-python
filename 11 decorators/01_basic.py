from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before decorator")
        func()
        print("after decorator")
    return wrapper

@my_decorator
def greet():
    print("hello from decorators ...")

greet()
print(greet.__name__)