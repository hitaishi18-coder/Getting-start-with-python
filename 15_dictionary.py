thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1876
}

print(thisdict)
print(thisdict["brand"])

# changeable 

# duplicates not allowed 

#Duplicate values will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))



thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
