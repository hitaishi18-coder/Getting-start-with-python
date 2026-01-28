# Global variable
chai_type = "ginger"

def update_kitchen():
    chai_type = "elaichi"   # Enclosing scope variable

    def kitchen():
        nonlocal chai_type   # Refers to the enclosing scope variable (not global)
        chai_type = "kesar"  # Updates the enclosing variable

    kitchen()  # Call inner function
    
    # After inner function runs, enclosing variable is updated
    print("after kitchen updated :", chai_type)

# Call the outer function
update_kitchen()
