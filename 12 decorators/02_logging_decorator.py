from functools import wraps

# Decorator to log function activity
def log_activity(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Runs before the original function
        print(f"Calling: {func.__name__}")
        
        # Call the original function with any arguments
        result = func(*args, **kwargs)
        
        # Runs after the original function
        print(f"Finished: {func.__name__}")
        
        # Return original function's result (if any)
        return result
    
    return wrapper


# Applying decorator
@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")


# Calling function
brew_chai("Masala")
