class ChaiOrder:
    # Yeh humara normal Constructor (Factory) hai.
    # Yeh tab chalta hai jab hum seedha ChaiOrder("Masala", "Low", "Small") likhte hain.
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # @classmethod ka matlab hai ki yeh function kisi ek object ('self') par nahi, 
    # balki poori Class ('cls') par kaam karega.
    @classmethod
    def from_dict(cls, order_data):
        # 'cls' ka matlab yahan 'ChaiOrder' hi hai. 
        # Yeh function ek Dictionary leta hai, usme se data nikalta hai, 
        # aur naya object (cls) banakar wapas (return) bhej deta hai.
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    # Ek aur @classmethod! Yeh ek String (text) se object banayega.
    @classmethod
    def from_string(cls, order_string):
        # String ko hyphen ("-") se tod kar 3 alag variables mein daal diya
        tea_type, sweetness, size = order_string.split("-")
        # Un teeno variables ko use karke naya object (cls) banaya aur return kar diya
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    # @staticmethod: Ise object ya class kisi se matlab nahi hai. 
    # Yeh bas ek helper check hai jo batayega ki size sahi hai ya nahi.
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


# Static method ko directly class ke naam se call kiya.
# Output: True (Kyunki "Medium" list mein hai)
print(ChaiUtils.is_valid_size("Medium"))


# TARIKA 1: @classmethod 'from_dict' ka use karke object banaya (Dictionary input)
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

# TARIKA 2: @classmethod 'from_string' ka use karke object banaya (String input)
order2 = ChaiOrder.from_string("Ginger-Low-Small")

# TARIKA 3: Normal __init__ ka use karke object banaya (Direct input)
order3 = ChaiOrder("Large", "Low", "Large")


# ASLI SECRET: __dict__ (Object ki Kundali)
# Python background mein aapke object ka saara data ek dictionary ke roop mein save karta hai.
# Jab hum .__dict__ print karte hain, toh Python sab khol kar dikha deta hai. Debugging ke liye best tool!

# Output: {'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}
print(order1.__dict__)

# Output: {'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}
print(order2.__dict__)

# Output: {'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}
print(order3.__dict__)