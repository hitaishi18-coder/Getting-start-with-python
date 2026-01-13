# -------- Example 1: Local vs Global Scope --------

def serve_chai():
    chai_type = "masala"  # Local scope: only accessible inside this function
    print(f"inside function : {chai_type}")

# Global variable
chai_type = "lemon"

serve_chai()  # Calls function → prints local variable
print(f"outside function : {chai_type}")  # Prints global variable


# -------- Example 2: Local, Enclosing, and Global Scope --------

def chai_counter():
    chai_order = "lemon"   # Enclosing scope (for inner function)
    
    def print_order():
        chai_order = "ginger"  # Local scope (inside inner function)
        print("inner :", chai_order)
    
    print_order()  # Call inner function
    print("outer :", chai_order)  # Refers to enclosing scope variable

# Global variable
chai_order = "tulsi"   

chai_counter()   # Executes function with inner and outer scopes
print("global :", chai_order)  # Refers to global variable
