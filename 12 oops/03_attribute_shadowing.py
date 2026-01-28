# Defining class Chai with class attributes
class Chai:
    temperature = "hot"
    strength = "Strong"

# Creating an instance of Chai
cutting = Chai()

# Accessing class attribute through instance
print(cutting.temperature)   # Output: hot

# Creating instance attribute 'temperature'
# This overrides class attribute for this object only
cutting.temperature = "mild"

# Creating a new instance attribute 'cup'
cutting.cup = "small"

print("after changing", cutting.temperature)  
# Output: mild (instance attribute)

print("direct look into the class", Chai.temperature)  
# Output: hot (class attribute unchanged)

# Deleting instance attribute 'temperature'
# Now instance no longer has its own temperature,
# so Python falls back to class attribute
del cutting.temperature

# Deleting instance attribute 'cup'
del cutting.cup

# Now temperature is again taken from class
print(cutting.temperature)   # Output: hot

# This will cause an ERROR 
# because 'cup' attribute does not exist in class
print(cutting.cup)
