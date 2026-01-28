# Defining a class Chaicup
class Chaicup:
    # Class attribute
    size = 150
    
    # Instance method
    # 'self' refers to the object calling the method
    def describe(self):
        return f"A {self.size} ml chai cup"

# Creating first object
cup = Chaicup()

# Calling method normally
# Python automatically passes 'cup' as self
print(cup.describe())  
# Output: A 150 ml chai cup

# Calling method using class name
# Here we manually pass the object as argument
print(Chaicup.describe(cup))  
# Output: A 150 ml chai cup

# Creating another object
cup_two = Chaicup()

# Creating an instance attribute 'size'
# This overrides class attribute for this object
cup_two.size = 100

# Calling method through class by passing object
print(Chaicup.describe(cup_two))  
# Output: A 100 ml chai cup
