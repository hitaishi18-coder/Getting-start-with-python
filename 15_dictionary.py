thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1876
}
# Dictionary with key : value pairs
# Keys are strings, values can be any data type

print(thisdict)
# Prints the complete dictionary

print(thisdict["brand"])
# Accessing value using key
# Output: ford


# changeable
# Dictionaries are mutable (values can be changed)

# duplicates not allowed
# Duplicate keys will overwrite existing values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
# The key "year" is repeated
# The last value (2020) overwrites the previous one

print(thisdict)


print(len(thisdict))
# len() returns number of key-value pairs in dictionary


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# Dictionary can store different data types:
# string, boolean, integer, list

print(thisdict)


thisdict = dict(name="John", age=36, country="Norway")
# Creating dictionary using dict() constructor
print(thisdict)
