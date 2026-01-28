# Creating a custom exception
# It inherits from Python's built-in Exception class
class OutOfIngredientsError(Exception):
    pass   # No extra code needed, default behavior is enough


def make_chai(milk, sugar):
    
    # Check if required ingredients are missing
    if milk == 0 or sugar == 0:
        # Raise our custom exception
        raise OutOfIngredientsError("Missing milk or sugar")
    
    # If no exception, chai is made successfully
    print("Chai is ready..")


# -------------------------
# Function calls
# -------------------------

make_chai(1, 1)   # Works fine

make_chai(0, 1)   # Raises OutOfIngredientsError
