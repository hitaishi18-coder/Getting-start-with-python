from functools import wraps

# Decorator that checks if user is admin
def require_admin(func):
    
    @wraps(func)
    def wrapper(user_role):
        # Check user role before allowing function to run
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            # If admin, call the original function
            return func(user_role)
    
    return wrapper


# Applying decorator
@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory")


# -------------------------
# Function calls
# -------------------------

access_tea_inventory("user")   # Not admin
access_tea_inventory("admin")  # Admin
