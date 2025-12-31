# --------- DATA TYPES IN PYTHON -----------\


# int
X = 5
# Integer data type (whole numbers)

print(type(X))
# type() shows the data type of variable X


# str
x = "hello world"
# String data type (text inside quotes)

print(type(x))
print("-------")
# Separator for clean output


# int
x = 20
# Integer value reassigned to x

print(type(x))
print("-------")


# float
x = 20.5
# Float data type (decimal numbers)

print(type(x))
print("-------")


# complex
x = 1j
# Complex number (imaginary part)
# j represents the imaginary unit

print(type(x))
print("-------")


# list
x = ["apple", "banana", "cherry"]
# List data type
# Ordered, changeable (mutable), allows duplicates

print(type(x))
print("-------")


# tuple
x = ("apple", "banana", "cherry")
# Tuple data type
# Ordered, unchangeable (immutable), allows duplicates

print(type(x))
print("-------")


# range
x = range(6)
# range data type generates sequence of numbers
# Commonly used in loops

print(type(x))
print("-------")


# dict
x = {"name": "john", "age": 36}
# Dictionary data type
# Stores data in key : value pairs

print(type(x))
print("-------")


# set
x = {"apple", "banana", "cherry"}
# Set data type
# Unordered, unindexed, no duplicate values allowed

print(type(x))
print("-------")


# fronzenset
x = frozenset({"apple", "banana", "cherry"})
# Frozenset is an immutable version of set
# Values cannot be changed once created

print(type(x))
print("-------")


# boolean
x = True
# Boolean data type
# Can be either True or False

print(type(x))
print("-------")


# bytes
x = b"Hello"
# Bytes data type
# Used to represent binary data

print(type(x))
print("-------")


# byte array
x = bytearray(5)
# Bytearray data type
# Mutable version of bytes

print(type(x))
print("-------")


# memoryview
x = memoryview(bytes(5))
# memoryview allows access to binary data without copying it

print(type(x))
print("-------")


# none type
x = None
# NoneType represents absence of value

print(type(x))
print("-------")
