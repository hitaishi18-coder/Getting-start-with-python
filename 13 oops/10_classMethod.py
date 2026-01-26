class ChaiOrder:
    
    # Normal constructor
    # Runs when we create an object directly
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # -----------------------------
    # Class Method #1
    # Creates object from a dictionary
    # -----------------------------
    @classmethod
    def from_dict(cls, order_data):
        # cls refers to the class (ChaiOrder)
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    # -----------------------------
    # Class Method #2
    # Creates object from a formatted string
    # -----------------------------
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    

# -----------------------------
# Static Method Utility Class
# -----------------------------
class ChaiUtils:
    
    @staticmethod
    def is_valid_size(size):
        # Just checks size validity
        # No use of self or cls
        return size in ["Small", "Medium", "Large"]


# -----------------------------
# Using static method
# -----------------------------
print(ChaiUtils.is_valid_size("Medium"))
# Output: True


# -----------------------------
# Creating objects using class methods
# -----------------------------

order1 = ChaiOrder.from_dict({
    "tea_type": "masala",
    "sweetness": "medium",
    "size": "Large"
})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

# Normal object creation using constructor
order3 = ChaiOrder("Large", "Low", "Large")


# -----------------------------
# Printing stored data
# __dict__ shows object attributes
# -----------------------------
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
