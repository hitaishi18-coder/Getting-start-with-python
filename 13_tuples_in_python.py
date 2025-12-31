#------ TUPLES-------
# immutable (values cannot be changed after creation)

mytuple = ("apple", "banana", "cherry")
# Creating a tuple with multiple items
print(mytuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# Tuples allow duplicate values
print(thistuple)


# length of tuple
thistuple = ("apple", "banana", "cherry")
# len() returns number of elements in tuple
print(len(thistuple))

thistuple = ("apple",)
# Single-item tuple
# Comma is mandatory, otherwise it is treated as string
print(type(thistuple))


# tuple items can be of any datatype
tuple1 = ("apple", "banana", "cherry")      # strings
tuple2 = (1, 6, 5, 6, 8)                     # integers
tuple3 = (True, False, False)                # booleans

tuple1 = ("abc", 54, True, 60, "male")
# Tuple with mixed data types
print(tuple1)


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# Confirms that it is a tuple


thistuple = tuple(("apple", "banana", "cherry"))
# Creating tuple using tuple() constructor
print(thistuple)


# Accessing tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])      # positive index
print(thistuple[-1])     # negative index


# Tuple slicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])    # slicing with range
print(thistuple[:4])     # from start
print(thistuple[2:])     # till end
print(thistuple[-4:-1])  # negative slicing


# Checking item existence
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


# Modifying tuple using list conversion
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# Adding elements to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

y = ("orange",)
thistuple += y
print(thistuple)


# Removing elements from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


# Deleting tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
# Accessing after deletion will raise NameError


# Tuple unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Tuple unpacking using asterisk (*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Looping through tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print("-----")

for i in range(len(thistuple)):
    print(thistuple[i])


i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1


# Joining tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
