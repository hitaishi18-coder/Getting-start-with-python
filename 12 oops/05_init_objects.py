# 'ChaiOrder' naam ki ek class banayi
class ChaiOrder:
    
    # Yeh ek special magic method hai jise 'Constructor' kehte hain.
    # Jab bhi hum class se naya object banate hain, yeh function automatically sabse pehle chal jata hai.
    # Iska kaam naye object ki basic setting (initialization) karna hota hai.
    # Note: 'type' ke aage underscore '_' isliye lagaya hai taaki Python ke inbuilt 'type()' function se confusion na ho.
    def __init__(self, type_, size):
        # 'self' ka matlab hai "yeh wala naya object".
        # Yahan hum naye object ko uski personal property 'type' de rahe hain jo user ne bheji hai.
        self.type = type_
        # Yahan hum us object ko uski personal property 'size' de rahe hain.
        self.size = size

    # Yeh ek normal method (function) hai jo object ka data use karke ek sentence banata hai
    def summary(self):
        # self.size aur self.type ka matlab hai us specific order (object) ka data laao
        return f"{self.size}ml of {self.type} chai"
    
# Yahan humne naya object banaya.
# Jaise hi humne bracket () mein "Masala" aur 200 likha, background mein '__init__' automatically chal gaya.
# 'order' ban gaya 'self', "Masala" ban gaya 'type_', aur 200 ban gaya 'size'.
order = ChaiOrder("Masala", 200)

# Ab hum us object ka method call kar rahe hain
# Output: 200ml of Masala chai
print(order.summary())


# Yahan humne ek bilkul naya cup (object) banaya.
# Iska apna alag '__init__' chala aur iski personal properties "Ginger" aur 220 set ho gayin.
order_two = ChaiOrder("Ginger", 220)

# Isne apna personal data use karke summary di
# Output: 220ml of Ginger chai
print(order_two.summary())