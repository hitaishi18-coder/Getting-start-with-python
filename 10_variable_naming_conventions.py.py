print(10 > 9)
# Greater than comparison
# Returns True because 10 is greater than 9

print(10 == 9)
# Equality comparison
# Returns False because 10 is not equal to 9

print(10 < 9)
# Less than comparison
# Returns False


a = 200
b = 23

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# if-else checks condition and executes corresponding block


print(bool("hello"))
# Non-empty string returns True

print(bool(13))
# Any non-zero number returns True


x = "hello"
y = 15

# Any string is True, except empty strings.
# Any number is True, except 0.

print(bool(x))
# x is non-empty string → True

print(bool(y))
# y is non-zero number → True


print(bool("abc"))
# Non-empty string → True

print(bool(123))
# Non-zero integer → True

print(bool(["apple", "cherry", "banana"]))
# Non-empty list → True


print(bool(False))
# False → False

print(bool(None))
# None represents absence of value → False

print(bool(0))
# Zero → False

print(bool(""))
# Empty string → False

print(bool(()))
# Empty tuple → False

print(bool([]))
# Empty list → False

print(bool({}))
# Empty dictionary → False


class myclass():
    def _len_(self):
        return 0
# Custom class
# _len_ method is incorrectly named, so it will NOT be called by bool()

myobj = myclass()
print(bool(myobj))
# Objects are True by default unless __len__ or __bool__ returns False


def myFunction():
    return True
# Function returning boolean value

print(myFunction())
# Prints returned value (True)


def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO!")
# If condition runs because function returns True


x = 200
print(isinstance(x, int))
# isinstance() checks if x belongs to given data type
# Returns True because x is an integer
