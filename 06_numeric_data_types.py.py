# ------ SETTING UP DATA TYPE ---------

x = str("hello world")
# Creates a string data type
# str() explicitly converts value into string

x = int(30)
# Creates an integer data type
# int() converts value into integer

x = float(20.5)
# Creates a float data type
# Used for decimal numbers


# list is mutable
x = list(("apple", "banana", "cherry"))
# list() converts tuple into a list
# Lists are ordered and changeable


# tuple is immutable
x = tuple(("apple", "banana", "cherry"))
# tuple() creates an immutable sequence
# Values cannot be modified after creation


x = range(6)
# Creates a range object from 0 to 5
# Mostly used in loops


x = dict(name="john", age=58)
# Creates a dictionary using key=value syntax
# Dictionary stores data in key-value pairs


x = set(("apple", "banana", "cherry"))
# Creates a set data type
# Sets do not allow duplicate values


x = frozenset(("apple", "banana", "cherry"))
# Creates an immutable set
# Elements cannot be added or removed


x = bytes(5)
# Creates bytes object of size 5
# All values initialized to 0


x = bytearray(5)
# Creates mutable bytearray of size 5
# Values can be changed later


x = memoryview(bytes(5))
# memoryview provides direct access to binary data
# Avoids copying data in memory
