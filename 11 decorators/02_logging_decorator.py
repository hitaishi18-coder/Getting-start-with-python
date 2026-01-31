from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- LOG: calling {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- LOG: finished {func.__name__} ---")
        return result
    return wrapper


@logging
def brew_chai(type, cups, milk="no", sugar="medium"):
    print(f"Making {cups} cups of {type} chai. Milk: {milk}, Sugar: {sugar}")


brew_chai("masala", 2)                         
brew_chai("ginger", 5, milk="yes", sugar="low") 