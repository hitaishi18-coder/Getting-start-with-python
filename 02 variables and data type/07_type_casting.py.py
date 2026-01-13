#------ DATA TYEPS---------

# NUMBERS

x = 1
# Integer number

y = 2.7
# Float number (decimal)

z = 1j
# Complex number (imaginary part)

print(type(x))
print(type(y))
print(type(z))
print("-----")
# Separator for readability


x = 1
y = 345678923456
z = -234567
# Python supports very large integers and negative numbers

print(type(x))
print(type(y))
print(type(z))
print("-----")


x = 1.12
y = 1.0
z = -34.45
# Floating point numbers

print(type(x))
print(type(y))
print(type(z))
print("-----")


x = 35e3
# Scientific notation (35 × 10^3)

y = 12E4
# Scientific notation (12 × 10^4)

z = -87.7e100
# Very large float value using exponent notation

print(type(x))
print(type(y))
print(type(z))
print("-----")


x = 3+5j
y = 5j
z = -5j
# Complex numbers consist of real and imaginary parts

print(type(x))
print(type(y))
print(type(z))
print("-----")


# type conversion

x = 1
y = 7.9
z = 1j
# Original variables of different numeric types

a = float(x)
# Converts integer to float

print(a)
print(type(a))


b = int(y)
# Converts float to integer (decimal part is removed)

print(b)
print(type(b))


c = complex(x)
# Converts integer to complex number

print(c)
print(type(c))


# random numbers
import random
# random module is used to generate random values

s = (random.randrange(1, 10))
# Generates a random number between 1 and 9
# Upper limit is excluded

print(s)
