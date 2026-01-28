# Defining a class named Chai
class Chai:
    pass  # 'pass' means the class has no properties or methods yet

# Defining another class named ChaiTime
class ChaiTime:
    pass  # Empty class, just created for demonstration

# Printing the type of the class Chai itself
# In Python, classes are objects too, so their type is 'type'
print(type(Chai))

# Creating an object (instance) of class Chai
ginger_tea = Chai()

# Printing the type of the object ginger_tea
# This will show that ginger_tea is an instance of class Chai
print(type(ginger_tea))

# Checking if the type of ginger_tea is exactly Chai
# This returns True because ginger_tea was created from Chai
print(type(ginger_tea) is Chai)

# Checking if the type of ginger_tea is ChaiTime
# This returns False because ginger_tea is not an instance of ChaiTime
print(type(ginger_tea) is ChaiTime)
