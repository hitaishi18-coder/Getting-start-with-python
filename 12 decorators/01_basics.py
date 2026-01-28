from functools import wraps

# This is our decorator
def my_decorator(func):
    
    # wraps(func) copies metadata (like name, docstring) 
    # from original function to wrapper
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()   # Call the original function
        print("After function runs")
    
    return wrapper


# Applying decorator using @ syntax
@my_decorator
def greet():
    print("Hello from decorators class from ChaiCode")


# Calling decorated function
greet()

# Checking function name
print(greet.__name__)
