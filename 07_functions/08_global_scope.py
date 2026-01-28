# Global variable
chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type   # Refers to the global variable
        chai_type = "irani"  # Updates the global variable
    
    kitchen()  # Call inner function

front_desk()

# Since global variable was updated, change is visible everywhere
print("final global chai :", chai_type)
