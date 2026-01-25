# Defining a class named Chai
class Chai:
    # Class attribute (shared by all instances)
    origin = "india"

# Accessing class attribute directly using class name
print(Chai.origin)

# Adding a new class attribute dynamically
Chai.is_hot = True
print(Chai.is_hot)

# Creating an instance (object) of Chai
masala = Chai()

# Accessing class attributes using the instance
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

# Creating an instance attribute 'is_hot' for masala
# This overrides the class attribute only for this object
masala.is_hot = False

# Printing class attribute is_hot (still True)
print("class:", Chai.is_hot)

# Printing instance attribute is_hot (False)
print("masala", masala.is_hot)

# Setting instance attribute again (still False)
masala.is_hot = False

# Class attribute remains unchanged
print("class:", Chai.is_hot)

# Instance attribute remains False
print(f"masala {masala.is_hot}")

# Adding a new attribute 'flavor' only to this instance
masala.flavor = "masala"

# Printing instance-specific attribute
print(masala.flavor)
