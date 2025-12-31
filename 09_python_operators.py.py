# CASTING -- USE TO SPECIFY VARIABLE

x = int(1)
# Converts integer 1 into integer (no change)

y = int(9.7)
# Converts float to integer
# Decimal part is removed (not rounded)

z = int("6")
# Converts string "6" into integer

print(x)
print(y)
print(z)


x = float(1)
# Converts integer to float (1.0)

y = float(4.8)
# Float remains float

z = float("6")
# Converts string "6" into float (6.0)

w = float("7.8")
# Converts string "7.8" into float

print(x)
print(y)
print(z)
print(w)


x = str("s1")
# String remains string

y = str(2)
# Converts integer into string

z = str(3.0)
# Converts float into string

print(x)
print(y)
print(z)
