# Defining class ChaiOrder
class ChaiOrder:
    
    # Constructor method
    # This runs automatically when a new object is created
    def __init__(self, type_, size):
        self.type = type_   # Instance attribute
        self.size = size    # Instance attribute
    
    # Instance method to return order summary
    def summary(self):
        return f"{self.size}ml of {self.type}"

# Creating first object
order = ChaiOrder("masala", 200)

# Calling summary method
print(order.summary())  
# Output: 200ml of masala

# Creating second object
order_two = ChaiOrder("ginger", 220)

# Calling summary method
print(order_two.summary())  
# Output: 220ml of ginger
