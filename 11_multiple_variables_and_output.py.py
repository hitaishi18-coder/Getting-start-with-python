#-------- OPERATOR ---------

print(10 + 5)
# Addition operator

sum1 = 100 + 20
# Adds two numbers and stores result
print(sum1)

sum2 = sum1 + 234
# Uses previous variable in calculation
print(sum2)

sum3 = sum2 + sum2
# Adds variable with itself
print(sum3)

print("-----------")


x = 15
y = 4

print(x + y)
# Addition

print(x - y)
# Subtraction

print(x * y)
# Multiplication

print(x / y)
# Division (always returns float)

print(x % y)
# Modulus (remainder)

print(x ** y)
# Exponentiation (x power y)

print(x // y)
# Floor division (returns integer quotient)


x = 12
y = 5
print(x / y)
# Normal division → float result

x = 12
y = 5
print(x // y)
# Floor division → integer result


number = [1, 2, 3, 4, 5, 6]
count = len(number)
# len() returns number of elements in list

if count > 3:
    print(f"list has {count} element")
# f-string used for formatted output

if (count := len(number)) > 3:
    print(f"list has {count} element")
# Walrus operator (:=)
# Assigns and compares value in one line

print("----------")


x = 5
y = 3

print(x == y)
# Equal to

print(x != y)
# Not equal to

print(x > y)
# Greater than

print(x < y)
# Less than

print(x >= y)
# Greater than or equal to

print(x <= y)
# Less than or equal to


x = 5
print(1 < x < 10)
# Chained comparison (Python feature)

print(1 < x and x < 10)
# Same logic using logical AND


x = 5
print(x > 0 and x < 10)
# AND operator → True if both conditions are True


x = 5
print(x < 5 or x > 10)
# OR operator → True if any condition is True


x = 5
print(not(x > 3 and x < 10))
# NOT operator → reverses result

print("----------")


x = ["apple", "banana"]
y = ["apple", "banana"]

z = x
# z refers to same object as x

print(x is z)
# True → same memory location

print(x is y)
# False → different objects in memory

print(x == y)
# True → values are same

print("----------")


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
# True → different memory locations

# is → checks identity (same memory location)
# is not → checks different memory locations


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
# True → values are equal

print(x is y)
# False → different objects in memory


fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
# Membership operator → checks presence


fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
# Checks absence in list

print("---------")


text = "Hello World"
print("H" in text)
# Checks character presence (case-sensitive)

print("hello" in text)
# False because of case mismatch

print("z" not in text)
# True → character not present


print("-------")


print(6 & 3)
# Bitwise AND

print(6 | 3)
# Bitwise OR

print(6 ^ 3)
# Bitwise XOR

print((6 + 3) - (6 + 3))
# Parentheses control order of operations

print(100 + 5 * 3)
# Multiplication happens before addition

print(5 + 4 - 7 + 3)
# Evaluated left to right
