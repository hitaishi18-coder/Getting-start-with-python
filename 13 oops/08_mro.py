# Base class
class A:
    label = "A : Base class"

# Class B inherits from A
class B(A):
    label = "B : Masala blend"

# Class C inherits from A
class C(A):
    label = "C : herbal blend"

# Class D inherits from C first, then B
# Order matters here!
class D(C, B):
    pass

# Create object of D
cup = D()

# Access label attribute
print(cup.label)

# Print Method Resolution Order
print(D.__mro__)
