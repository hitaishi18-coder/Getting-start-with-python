# ------ VARIABLES IN PYTHON -------

myvar = "john"
# Valid variable name

my_var = "john"
# Underscore is allowed in variable names

_my_var = "john"
# Variable names can start with underscore

myVar = "john"
# Camel-style naming (case matters)

MYVAR = "john"
# Uppercase variable name (often used for constants)

myvar2 = "john"
# Numbers are allowed at the end of variable names


# ------ NOT APPLICABLE VAR NAMES --------

# 2myvar = "john"
# Variable name cannot start with a number

# my-var = "john"
# Hyphen is not allowed in variable names

# my var = "john"
# Spaces are not allowed in variable names


# ---------- CAMEL CASE -----------

myVariableName = "john abc"
# Camel case: first word small, next words start with capital letter

print(myVariableName)
# Printing camel case variable


#------------PASCAL CASE -----------

MyVariableName = "John"
# Pascal case: every word starts with a capital letter
# Commonly used in class names


#-------------- SNAKE CASE ----------

my_variable_name = "john"
# Snake case: words separated using underscore
# Most commonly used in Python


# ------------- MULTIPLE VARIABLE -----------

x, y, z = "orange", "banana", "cherry"
# Multiple variables assigned different values in a single line

print(x)
print(y)
print(z)

a = b = c = "orange"
# Multiple variables assigned the same value

print(a)
print(b)
print(c)

fruits = ["apple", "banana", "cheery"]
# List containing multiple values

x, y, z = fruits
# Unpacking values from list into variables

print(x)
print(y)
print(z)


#--------- OUTPUT VARIABLE ----------

x = "python is awesome"
print(x)
# Printing a single variable

x = "python"
y = "is"
z = "awesome"

print(x, y, z)
# print() adds spaces automatically between values

x = "python"
y = "is"
z = "awesome"

print(x + y + z)
# Using + joins strings without adding spaces

x = "python "
y = "is "
z = "awesome"

print(x + y + z)
# Spaces are manually added inside strings

x = 5
y = 10

print(x + y)
# Adds two numbers and prints the result


# x = 5
# y = "john"
# print(x + y)
# This will cause a TypeError (int + string not allowed)

x = 5
y = "john"

print(x, y)
# Using comma allows printing different data types together


# -------GLOBAL VARIABLE--------

x = "awesome"
# Global variable (accessible everywhere)

def myfunc():
    print("python is " + x)
    # Function can access global variable

myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    # This x is a local variable (inside function)
    print("python is " + x)

myfunc()

print("python is " + x)
# Global x remains unchanged


#----------- GLOBAL KEYWORD -----------

def myfunc():
    global x
    # global keyword allows modifying global variable
    x = "fantastic"

myfunc()

print("python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("python is " + x)
